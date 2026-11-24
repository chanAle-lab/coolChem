"""Crop per-question official markscheme images directly from AQA markscheme PDFs.

Supports:
- Written-response tables (portrait or landscape), including multi-page questions
  stitched vertically.
- Section B MCQ key tables (cropping the Question | Key header + the single row).
"""

import re
from pathlib import Path
from typing import Optional

import pymupdf as fitz
from PIL import Image


def _find_table_x_bounds(page: fitz.Page, margin: float = 4.0) -> tuple[float, float]:
    """Find the left/right x-bounds of the main markscheme table on a page."""
    drawings = page.get_drawings()
    min_x, max_x = page.rect.width, 0.0
    for d in drawings:
        r = d.get("rect")
        if not r:
            continue
        if 35 < r.width < page.rect.width * 0.94 and r.y0 > 45 and r.y1 < page.rect.height - 35:
            min_x = min(min_x, r.x0)
            max_x = max(max_x, r.x1)
    if min_x < max_x:
        return max(0.0, min_x - margin), min(page.rect.width, max_x + margin)
    return 20.0, page.rect.width - 20.0


def _find_table_header_rect(page: fitz.Page) -> Optional[fitz.Rect]:
    """Locate the table header row (e.g. 'Question ... Marking Guidance' or 'Question Key')."""
    words = page.get_text("words")
    # Look for 'Question' near the top of the table (leftmost column, y between 40 and 250)
    for w in words:
        x0, y0, x1, y1, txt = w[:5]
        if txt == "Question" and x0 < 300 and 40 < y0 < 260:
            # Check if 'Marking' or 'Answers' or 'Key' is on roughly the same y line
            same_line = [
                ow for ow in words
                if abs(ow[1] - y0) < 8 and ow[4] in ("Marking", "Answers", "Key", "Mark", "Comments")
            ]
            if same_line:
                top_y = min([y0] + [ow[1] for ow in same_line]) - 4
                bot_y = max([y1] + [ow[3] for ow in same_line])
                # Check if 'Marking Guidance' wraps onto two lines
                for ow in words:
                    if abs(ow[1] - y0) < 22 and ow[1] >= y0 and ow[4] in ("Guidance", "information", "Ref."):
                        bot_y = max(bot_y, ow[3])
                rules = _find_horizontal_rules(page)
                top_y = _snap_to_rule_above(rules, top_y, max_dist=15.0)
                bot_y = _snap_to_rule_below(rules, bot_y, page.rect.height, max_dist=15.0)
                tx0, tx1 = _find_table_x_bounds(page)
                return fitz.Rect(tx0, max(0.0, top_y), tx1, bot_y)
    return None


def _find_horizontal_rules(page: fitz.Page) -> list[float]:
    """Return sorted y-coordinates of horizontal table borders on a page."""
    ys: list[float] = []
    for d in page.get_drawings():
        r = d.get("rect")
        if not r:
            continue
        if r.x0 < 100 and r.width > 35 and r.height <= 3.0 and 45 < r.y0 < page.rect.height - 30:
            ys.append(round((r.y0 + r.y1) / 2.0, 1))
        elif r.x0 < 100 and r.width > 35 and r.height > 10:
            # Rectangle border (e.g. cell box)
            if 45 < r.y0 < page.rect.height - 30:
                ys.append(round(r.y0, 1))
            if 45 < r.y1 < page.rect.height - 30:
                ys.append(round(r.y1, 1))
    # Deduplicate within 2pt
    ys.sort()
    dedup: list[float] = []
    for y in ys:
        if not dedup or y - dedup[-1] > 2.0:
            dedup.append(y)
    return dedup


def _snap_to_rule_above(rules: list[float], y: float, max_dist: float = 350.0) -> float:
    cands = [r for r in rules if r <= y + 2.0 and (y - r) <= max_dist]
    return cands[-1] if cands else max(45.0, y - 4.0)


def _snap_to_rule_below(rules: list[float], y: float, page_h: float, max_dist: float = 25.0) -> float:
    cands = [r for r in rules if r >= y - 2.0 and (r - y) <= max_dist]
    return cands[0] if cands else min(page_h - 35.0, y + 4.0)


def _normalize_qlabel(txt: str) -> str:
    return txt.strip().rstrip(".").replace(" ", "")


def _canonical_qkey(txt: str) -> str:
    """Canonical lookup key ignoring leading zeros (e.g. '09.1' == '9.1', '05' == '5')."""
    norm = _normalize_qlabel(txt)
    if "." in norm:
        parts = norm.split(".", 1)
        return f"{parts[0].lstrip('0') or '0'}.{parts[1]}"
    return norm.lstrip("0") or "0"


def _find_question_anchors(doc: fitz.Document, start_page: int = 0) -> list[dict]:
    """Scan all pages for question-number anchors in the left 'Question' column.

    Returns a list of dicts: {label, page_idx, y0, y1, is_mcq} sorted in reading order.
    """
    anchors: list[dict] = []
    # Pattern for 01.1, 01.2, 1.1, 05, 9, 13, 1(a), etc.
    q_re = re.compile(r"^(?:\d{1,2}\.\d{1,2}[a-z]?|\d{1,2}|\d{1,2}\([a-z]+\))$")

    seen_table = False
    last_q_col_max_x = 110.0
    for p_idx in range(start_page, len(doc)):
        page = doc[p_idx]
        hdr = _find_table_header_rect(page)
        if not seen_table:
            if hdr is None:
                continue
            seen_table = True
        words = page.get_text("words")
        # Detect if this is a Section B MCQ page ("Question" + "Key")
        is_mcq_page = any(w[4] == "Key" for w in words) and any(w[4] == "Section" for w in words)

        tx0, _ = _find_table_x_bounds(page)
        q_hdr_words = [w for w in words if w[4] == "Question" and w[0] < 300 and 40 < w[1] < 260]
        if q_hdr_words:
            v_borders = sorted(
                d["rect"].x0
                for d in page.get_drawings()
                if d.get("rect") and d["rect"].height > 20 and d["rect"].width <= 3.0
                and d["rect"].x0 > q_hdr_words[0][0] + 20.0
                and d["rect"].x0 < q_hdr_words[0][2] + 45.0
            )
            q_col_max_x = (v_borders[0] - 2.0) if v_borders else (q_hdr_words[0][2] + 15.0)
            last_q_col_max_x = q_col_max_x
        else:
            q_col_max_x = last_q_col_max_x

        min_y = hdr.y1 if (hdr and hdr.y0 < 130.0) else 52.0
        max_y = page.rect.height - 50.0

        for w in words:
            x0, y0, x1, y1, txt = w[:5]
            if y0 < min_y or y1 > max_y:
                continue
            if hdr and hdr.y0 - 2.0 <= y0 <= hdr.y1 + 2.0:
                continue
            if x0 < 20.0 or x0 > q_col_max_x:
                continue
            norm = _normalize_qlabel(txt)
            if not q_re.match(norm):
                continue
            if re.match(r"^\d{1,2}$", norm):
                if not (1 <= int(norm) <= 45):
                    continue
                same_line_words = [ow[4] for ow in words if abs(ow[1] - y0) < 4 and ow[0] <= q_col_max_x + 5]
                if "of" in same_line_words or "Level" in same_line_words:
                    continue
            anchors.append({
                "label": norm,
                "page_idx": p_idx,
                "y0": y0,
                "y1": y1,
                "is_mcq": is_mcq_page,
            })

    # Deduplicate same label on same page or consecutive continuation pages (e.g. '01.1 continued')
    cleaned: list[dict] = []
    for a in anchors:
        if cleaned and _canonical_qkey(cleaned[-1]["label"]) == _canonical_qkey(a["label"]):
            continue
        cleaned.append(a)
    return cleaned


def _render_rect(page: fitz.Page, rect: fitz.Rect, dpi: int = 150) -> Image.Image:
    pix = page.get_pixmap(dpi=dpi, clip=rect)
    return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


def _vstack_images(imgs: list[Image.Image]) -> Image.Image:
    if len(imgs) == 1:
        return imgs[0]
    w = max(im.width for im in imgs)
    h = sum(im.height for im in imgs)
    out = Image.new("RGB", (w, h), (255, 255, 255))
    y = 0
    for im in imgs:
        out.paste(im, (0, y))
        y += im.height
    return out


def crop_official_markschemes(
    ms_pdf_path: str | Path,
    question_labels: list[str],
    out_dir: str | Path,
    dpi: int = 150,
    start_page: int = 0,
) -> dict[str, str]:
    """Crop official markscheme images for each label in `question_labels`.

    Args:
        ms_pdf_path: Path to the official AQA markscheme PDF.
        question_labels: List of question labels matching the MS (e.g. ["01.1", "01.2", "05"]).
        out_dir: Directory where `q<label>.png` files will be saved.
        dpi: Render DPI (default 150).
        start_page: 0-based page index to start scanning (optional).

    Returns:
        Dict mapping each question_label to its saved filename (e.g. "q01-1.png").
    """
    ms_pdf_path = Path(ms_pdf_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(ms_pdf_path))
    anchors = _find_question_anchors(doc, start_page=start_page)

    # Index anchors by canonical key
    anchor_by_key: dict[str, int] = {}
    for idx, a in enumerate(anchors):
        ck = _canonical_qkey(a["label"])
        if ck not in anchor_by_key:
            anchor_by_key[ck] = idx

    results: dict[str, str] = {}
    last_hdr_img: Optional[Image.Image] = None
    last_table_x: Optional[tuple[float, float]] = None
    for raw_label in question_labels:
        norm = _normalize_qlabel(raw_label)
        ck = _canonical_qkey(raw_label)
        if ck not in anchor_by_key:
            raise KeyError(f"Question label '{raw_label}' not found in {ms_pdf_path.name}. Found: {[a['label'] for a in anchors]}")

        a_idx = anchor_by_key[ck]
        curr = anchors[a_idx]
        nxt = anchors[a_idx + 1] if a_idx + 1 < len(anchors) else None

        p_start = curr["page_idx"]
        p_end = nxt["page_idx"] if nxt else len(doc) - 1

        # If nxt is on a later page, check if nxt is right at the top of p_end (meaning curr ended at bottom of p_end - 1)
        if nxt and p_end > p_start:
            end_page_hdr = _find_table_header_rect(doc[p_end])
            hdr_bot = end_page_hdr.y1 if end_page_hdr else 75.0
            if nxt["y0"] - hdr_bot < 55.0:
                p_end = p_end - 1
                nxt_on_same_end = False
            else:
                nxt_on_same_end = True
        else:
            nxt_on_same_end = nxt is not None

        chunks: list[Image.Image] = []
        for p_idx in range(p_start, p_end + 1):
            page = doc[p_idx]
            tx0, tx1 = _find_table_x_bounds(page)
            rules = _find_horizontal_rules(page)
            hdr = _find_table_header_rect(page)
            if hdr and (tx0 < 70.0 or page.rect.width < 700):
                last_table_x = (tx0, tx1)
            elif last_table_x is not None and not curr["is_mcq"]:
                tx0 = min(tx0, last_table_x[0])
                tx1 = max(tx1, last_table_x[1]) if tx1 < last_table_x[1] else last_table_x[1]

            if p_idx == p_start:
                y0 = _snap_to_rule_above(rules, curr["y0"])
                if hdr and hdr.y0 < curr["y0"]:
                    last_hdr_img = _render_rect(page, fitz.Rect(tx0, hdr.y0, tx1, hdr.y1), dpi=dpi)
                    chunks.append(last_hdr_img)
                elif last_hdr_img is not None:
                    chunks.append(last_hdr_img)
            else:
                # Continuation page: start right below header (or top rule)
                y0 = hdr.y1 if hdr else (rules[0] if rules else 55.0)

            if p_idx == p_end and nxt and nxt["page_idx"] == p_idx:
                if hdr and y0 < hdr.y0 < nxt["y0"]:
                    pre_hdr_rules = [r for r in rules if y0 + 5 < r <= hdr.y0 - 5]
                    y1 = pre_hdr_rules[-1] if pre_hdr_rules else _snap_to_rule_above(rules, hdr.y0)
                else:
                    y1 = _snap_to_rule_above(rules, nxt["y0"])
            else:
                # End at the last horizontal rule on the page above the footer
                bottom_rules = [r for r in rules if r < page.rect.height - 35.0]
                y1 = bottom_rules[-1] if bottom_rules else page.rect.height - 40.0

            if y1 <= y0 + 5:
                continue
            chunks.append(_render_rect(page, fitz.Rect(tx0, y0, tx1, y1), dpi=dpi))

        out_img = _vstack_images(chunks)
        safe_name = "q" + norm.replace(".", "-") + ".png"
        out_path = out_dir / safe_name
        out_img.save(str(out_path))
        results[raw_label] = safe_name

    doc.close()
    return results

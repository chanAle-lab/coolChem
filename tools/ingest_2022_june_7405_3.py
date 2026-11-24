"""Ingest AQA A-level Chemistry June 2022 Paper 3 (7405/3) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530598562_fb80a7fc.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530598547_84ca846f.pdf"
)

PAPER_ID = "2022-june-7405-3"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2022,
    "series": "June",
    "unit": "7405/3",
    "level": "A-level",
    "date": "2022-06-01",
    "title": "7405/3 — A-level Paper 3: Synoptic (June 2022)",
    "totalMarks": 90,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q3-stem.jpg", "page": 10, "x0": 40, "y0": 65, "x1": 555, "y1": 265},
    {"filename": "fig-q4-fig1.jpg", "page": 15, "x0": 40, "y0": 130, "x1": 555, "y1": 495},
]

PAGE_MAP = {
    "01.1": 3, "01.2": 3, "01.3": 4, "01.4": 5, "01.5": 5, "01.6": 5, "01.7": 6, "01.8": 7,
    "02": 8,
    "03.1": 10, "03.2": 10, "03.3": 10, "03.4": 11, "03.5": 11, "03.6": 11, "03.7": 12,
    "04.1": 14, "04.2": 15, "04.3": 16, "04.4": 17, "04.5": 17,
    "05.1": 18, "05.2": 18, "05.3": 19,
    "06": 20, "07": 20,
    "08": 21, "09": 21, "10": 21,
    "11": 22, "12": 22, "13": 22,
    "14": 23, "15": 23, "16": 23,
    "17": 24, "18": 24, "19": 24,
    "20": 25, "21": 25, "22": 25,
    "23": 26, "24": 26, "25": 26,
    "26": 27, "27": 27, "28": 27,
    "29": 28, "30": 28,
    "31": 29, "32": 29, "33": 29,
    "34": 30, "35": 30,
}

MS_QNUM_MAP = {}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.8", "marks": 2, "stem": "Paper 3 Question 01.1 (Thermodynamics)."},
    {"qnum": "01.2", "specRef": "3.1.8", "marks": 3, "stem": "Paper 3 Question 01.2 (Thermodynamics)."},
    {"qnum": "01.3", "specRef": "3.1.4", "marks": 3, "stem": "Paper 3 Question 01.3 (Energetics)."},
    {"qnum": "01.4", "specRef": "RP", "marks": 1, "stem": "Paper 3 Question 01.4 (Required practical)."},
    {"qnum": "01.5", "specRef": "RP", "marks": 2, "stem": "Paper 3 Question 01.5 (Required practical)."},
    {"qnum": "01.6", "specRef": "RP", "marks": 1, "stem": "Paper 3 Question 01.6 (Required practical)."},
    {"qnum": "01.7", "specRef": "3.1.8", "marks": 4, "stem": "Paper 3 Question 01.7 (Thermodynamics)."},
    {"qnum": "01.8", "specRef": "3.1.8", "marks": 2, "stem": "Paper 3 Question 01.8 (Thermodynamics)."},
    {"qnum": "02", "specRef": "3.2.6", "marks": 6, "stem": "Paper 3 Question 02 (Reactions of ions in aqueous solution)."},
    {"qnum": "03.1", "specRef": "3.3.3", "marks": 2, "stem": "Paper 3 Question 03.1 (Halogenoalkanes).", "figures": ["fig-q3-stem.jpg"]},
    {"qnum": "03.2", "specRef": "3.3.7", "marks": 2, "stem": "Paper 3 Question 03.2 (Optical isomerism)."},
    {"qnum": "03.3", "specRef": "3.3.7", "marks": 2, "stem": "Paper 3 Question 03.3 (Optical isomerism).", "figures": ["fig-q3-stem.jpg"]},
    {"qnum": "03.4", "specRef": "3.3.3", "marks": 3, "stem": "Paper 3 Question 03.4 (Halogenoalkanes).", "figures": ["fig-q3-stem.jpg"]},
    {"qnum": "03.5", "specRef": "3.3.4", "marks": 2, "stem": "Paper 3 Question 03.5 (Alkenes).", "figures": ["fig-q3-stem.jpg"]},
    {"qnum": "03.6", "specRef": "3.3.7", "marks": 2, "stem": "Paper 3 Question 03.6 (Optical isomerism).", "figures": ["fig-q3-stem.jpg"]},
    {"qnum": "03.7", "specRef": "RP", "marks": 2, "stem": "Paper 3 Question 03.7 (Required practical)."},
    {"qnum": "04.1", "specRef": "3.1.9", "marks": 2, "stem": "Paper 3 Question 04.1 (Rate equations)."},
    {"qnum": "04.2", "specRef": "RP", "marks": 2, "stem": "Paper 3 Question 04.2 (Required practical)."},
    {"qnum": "04.3", "specRef": "3.1.9", "marks": 2, "stem": "Paper 3 Question 04.3 (Rate equations).", "figures": ["fig-q4-fig1.jpg"]},
    {"qnum": "04.4", "specRef": "RP", "marks": 2, "stem": "Paper 3 Question 04.4 (Required practical)."},
    {"qnum": "04.5", "specRef": "3.1.9", "marks": 2, "stem": "Paper 3 Question 04.5 (Rate equations)."},
    {"qnum": "05.1", "specRef": "3.2.5", "marks": 2, "stem": "Paper 3 Question 05.1 (Transition metals)."},
    {"qnum": "05.2", "specRef": "3.2.5", "marks": 6, "stem": "Paper 3 Question 05.2 (Transition metals)."},
    {"qnum": "05.3", "specRef": "3.2.5", "marks": 3, "stem": "Paper 3 Question 05.3 (Transition metals)."},
    {"qnum": "06", "specRef": "3.1.1", "marks": 1, "stem": "Paper 3 Section B Question 06."},
    {"qnum": "07", "specRef": "3.1.2", "marks": 1, "stem": "Paper 3 Section B Question 07."},
    {"qnum": "08", "specRef": "3.1.3", "marks": 1, "stem": "Paper 3 Section B Question 08."},
    {"qnum": "09", "specRef": "3.1.4", "marks": 1, "stem": "Paper 3 Section B Question 09."},
    {"qnum": "10", "specRef": "3.1.5", "marks": 1, "stem": "Paper 3 Section B Question 10."},
    {"qnum": "11", "specRef": "3.1.6", "marks": 1, "stem": "Paper 3 Section B Question 11."},
    {"qnum": "12", "specRef": "3.1.7", "marks": 1, "stem": "Paper 3 Section B Question 12."},
    {"qnum": "13", "specRef": "3.1.8", "marks": 1, "stem": "Paper 3 Section B Question 13."},
    {"qnum": "14", "specRef": "3.1.10", "marks": 1, "stem": "Paper 3 Section B Question 14."},
    {"qnum": "15", "specRef": "3.1.11", "marks": 1, "stem": "Paper 3 Section B Question 15."},
    {"qnum": "16", "specRef": "3.1.12", "marks": 1, "stem": "Paper 3 Section B Question 16."},
    {"qnum": "17", "specRef": "3.2.1", "marks": 1, "stem": "Paper 3 Section B Question 17."},
    {"qnum": "18", "specRef": "3.2.2", "marks": 1, "stem": "Paper 3 Section B Question 18."},
    {"qnum": "19", "specRef": "3.2.3", "marks": 1, "stem": "Paper 3 Section B Question 19."},
    {"qnum": "20", "specRef": "3.2.4", "marks": 1, "stem": "Paper 3 Section B Question 20."},
    {"qnum": "21", "specRef": "3.2.5", "marks": 1, "stem": "Paper 3 Section B Question 21."},
    {"qnum": "22", "specRef": "3.2.6", "marks": 1, "stem": "Paper 3 Section B Question 22."},
    {"qnum": "23", "specRef": "3.3.1", "marks": 1, "stem": "Paper 3 Section B Question 23."},
    {"qnum": "24", "specRef": "3.3.2", "marks": 1, "stem": "Paper 3 Section B Question 24."},
    {"qnum": "25", "specRef": "3.3.3", "marks": 1, "stem": "Paper 3 Section B Question 25."},
    {"qnum": "26", "specRef": "3.3.4", "marks": 1, "stem": "Paper 3 Section B Question 26."},
    {"qnum": "27", "specRef": "3.3.5", "marks": 1, "stem": "Paper 3 Section B Question 27."},
    {"qnum": "28", "specRef": "3.3.6", "marks": 1, "stem": "Paper 3 Section B Question 28."},
    {"qnum": "29", "specRef": "3.3.8", "marks": 1, "stem": "Paper 3 Section B Question 29."},
    {"qnum": "30", "specRef": "3.3.9", "marks": 1, "stem": "Paper 3 Section B Question 30."},
    {"qnum": "31", "specRef": "3.3.10", "marks": 1, "stem": "Paper 3 Section B Question 31."},
    {"qnum": "32", "specRef": "3.3.11", "marks": 1, "stem": "Paper 3 Section B Question 32."},
    {"qnum": "33", "specRef": "3.3.12", "marks": 1, "stem": "Paper 3 Section B Question 33."},
    {"qnum": "34", "specRef": "3.3.13", "marks": 1, "stem": "Paper 3 Section B Question 34."},
    {"qnum": "35", "specRef": "3.3.15", "marks": 1, "stem": "Paper 3 Section B Question 35."},
]


def extract_figures():
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(QP_PDF))
    for fig in FIGURES:
        page = doc[fig["page"] - 1]
        rect = fitz.Rect(fig["x0"], fig["y0"], fig["x1"], fig["y1"])
        pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(2.5, 2.5))
        out_path = IMG_DIR / fig["filename"]
        pix.save(str(out_path))
        print(f"Saved figure: {out_path}")
    doc.close()


def main():
    extract_figures()
    ms_labels = [MS_QNUM_MAP.get(q["qnum"], q["qnum"]) for q in QUESTIONS]
    ms_map = crop_official_markschemes(
        MS_PDF,
        ms_labels,
        IMG_DIR / "ms",
    )

    data = json.loads(DB_PATH.read_text(encoding="utf-8"))
    data["papers"] = [p for p in data["papers"] if p["id"] != PAPER_ID]
    data["questions"] = [q for q in data["questions"] if q.get("paper") != PAPER_ID]
    data["papers"].append(PAPER_META)

    total_marks = 0
    for q in QUESTIONS:
        qnum = q["qnum"]
        qnum_slug = qnum.replace(".", "-")
        ms_key = MS_QNUM_MAP.get(qnum, qnum)
        entry = {
            "id": f"{PAPER_ID}-q{qnum}",
            "paper": PAPER_ID,
            "year": PAPER_META["year"],
            "series": PAPER_META["series"],
            "unit": PAPER_META["unit"],
            "level": PAPER_META["level"],
            "question": qnum,
            "questionNumber": qnum,
            "page": PAGE_MAP[qnum],
            "marks": q["marks"],
            "topics": [q["specRef"]],
            "skills": [],
            "summary": q["stem"],
            "specRef": q["specRef"],
            "image": f"img/{PAPER_ID}/q{qnum_slug}.jpg",
            "markscheme": f"img/{PAPER_ID}/ms/{ms_map[ms_key]}",
            "figures": [f"img/{PAPER_ID}/{f}" for f in q.get("figures", [])],
        }
        if "crop_exclude_y" in q:
            entry["crop_exclude_y"] = q["crop_exclude_y"]
        data["questions"].append(entry)
        total_marks += q["marks"]

    DB_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Ingested {PAPER_ID}: {len(QUESTIONS)} questions, {total_marks} marks")


if __name__ == "__main__":
    main()

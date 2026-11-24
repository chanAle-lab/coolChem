"""Ingest AQA A-level Chemistry June 2022 Paper 2 (7405/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530598538_e168391b.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530598558_d33eb06f.pdf"
)

PAPER_ID = "2022-june-7405-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2022,
    "series": "June",
    "unit": "7405/2",
    "level": "A-level",
    "date": "2022-06-01",
    "title": "7405/2 — A-level Paper 2: Organic and Physical Chemistry (June 2022)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-fig1.jpg", "page": 4, "x0": 40, "y0": 300, "x1": 555, "y1": 595},
    {"filename": "fig-q6-spectra.jpg", "page": 18, "x0": 40, "y0": 65, "x1": 555, "y1": 845},
    {"filename": "fig-q9-y.jpg", "page": 24, "x0": 40, "y0": 65, "x1": 555, "y1": 385},
    {"filename": "fig-q10-scheme.jpg", "page": 28, "x0": 40, "y0": 65, "x1": 555, "y1": 435},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3, "01.3": 3, "01.4": 4, "01.5": 5, "01.6": 5, "01.7": 6, "01.8": 7,
    "02.1": 8, "02.2": 8, "02.3": 9, "02.4": 9, "02.5": 10,
    "03.1": 11, "03.2": 11, "03.3": 12, "03.4": 12,
    "04.1": 13, "04.2": 13, "04.3": 14, "04.4": 14, "04.5": 14,
    "05.1": 15, "05.2": 15, "05.3": 15, "05.4": 16, "05.5": 16, "05.6": 17,
    "06": 18,
    "07.1": 21, "07.2": 21, "07.3": 21, "07.4": 21,
    "08.1": 22, "08.2": 22, "08.3": 22,
    "09.1": 24, "09.2": 25, "09.3": 26, "09.4": 26, "09.5": 27,
    "10.1": 28, "10.2": 28, "10.3": 29, "10.4": 29, "10.5": 29,
}

# Official MS labels Q06 as '06.1'
MS_QNUM_MAP = {
    "06": "06.1",
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.8", "marks": 2, "stem": "Paper 2 Question 01.1 (Aldehydes and ketones)."},
    {"qnum": "01.2", "specRef": "3.1.9", "marks": 3, "stem": "Paper 2 Question 01.2 (Rate equations)."},
    {"qnum": "01.3", "specRef": "3.1.9", "marks": 1, "stem": "Paper 2 Question 01.3 (Rate equations)."},
    {"qnum": "01.4", "specRef": "RP", "marks": 1, "stem": "Paper 2 Question 01.4 (Required practical)."},
    {"qnum": "01.5", "specRef": "3.1.5", "marks": 3, "stem": "Paper 2 Question 01.5 (Kinetics / Figure 1).", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "01.6", "specRef": "3.1.5", "marks": 1, "stem": "Paper 2 Question 01.6 (Kinetics / Figure 1).", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "01.7", "specRef": "3.1.9", "marks": 5, "stem": "Paper 2 Question 01.7 (Arrhenius equation)."},
    {"qnum": "01.8", "specRef": "3.3.8", "marks": 5, "stem": "Paper 2 Question 01.8 (Aldehydes and ketones)."},
    {"qnum": "02.1", "specRef": "3.1.6", "marks": 2, "stem": "Paper 2 Question 02.1 (Equilibria)."},
    {"qnum": "02.2", "specRef": "3.1.6", "marks": 1, "stem": "Paper 2 Question 02.2 (Equilibria)."},
    {"qnum": "02.3", "specRef": "3.1.6", "marks": 3, "stem": "Paper 2 Question 02.3 (Equilibria)."},
    {"qnum": "02.4", "specRef": "3.1.6", "marks": 3, "stem": "Paper 2 Question 02.4 (Equilibria)."},
    {"qnum": "02.5", "specRef": "3.3.3", "marks": 2, "stem": "Paper 2 Question 02.5 (Halogenoalkanes)."},
    {"qnum": "03.1", "specRef": "3.3.4", "marks": 5, "stem": "Paper 2 Question 03.1 (Alkenes)."},
    {"qnum": "03.2", "specRef": "3.3.4", "marks": 3, "stem": "Paper 2 Question 03.2 (Alkenes)."},
    {"qnum": "03.3", "specRef": "3.3.4", "marks": 1, "stem": "Paper 2 Question 03.3 (Alkenes)."},
    {"qnum": "03.4", "specRef": "3.3.4", "marks": 2, "stem": "Paper 2 Question 03.4 (Alkenes)."},
    {"qnum": "04.1", "specRef": "3.3.13", "marks": 1, "stem": "Paper 2 Question 04.1 (Amino acids, proteins and DNA)."},
    {"qnum": "04.2", "specRef": "3.3.13", "marks": 2, "stem": "Paper 2 Question 04.2 (Amino acids, proteins and DNA)."},
    {"qnum": "04.3", "specRef": "3.3.13", "marks": 1, "stem": "Paper 2 Question 04.3 (Amino acids, proteins and DNA)."},
    {"qnum": "04.4", "specRef": "3.3.13", "marks": 4, "stem": "Paper 2 Question 04.4 (Amino acids, proteins and DNA)."},
    {"qnum": "04.5", "specRef": "3.3.13", "marks": 1, "stem": "Paper 2 Question 04.5 (Amino acids, proteins and DNA)."},
    {"qnum": "05.1", "specRef": "RP", "marks": 2, "stem": "Paper 2 Question 05.1 (Required practical)."},
    {"qnum": "05.2", "specRef": "RP", "marks": 1, "stem": "Paper 2 Question 05.2 (Required practical)."},
    {"qnum": "05.3", "specRef": "RP", "marks": 1, "stem": "Paper 2 Question 05.3 (Required practical)."},
    {"qnum": "05.4", "specRef": "RP", "marks": 2, "stem": "Paper 2 Question 05.4 (Required practical)."},
    {"qnum": "05.5", "specRef": "RP", "marks": 2, "stem": "Paper 2 Question 05.5 (Required practical)."},
    {"qnum": "05.6", "specRef": "3.1.2", "marks": 4, "stem": "Paper 2 Question 05.6 (Amount of substance)."},
    {"qnum": "06", "specRef": "3.3.15", "marks": 6, "stem": "Paper 2 Question 06 (NMR and IR spectroscopy).", "figures": ["fig-q6-spectra.jpg"]},
    {"qnum": "07.1", "specRef": "3.3.9", "marks": 3, "stem": "Paper 2 Question 07.1 (Carboxylic acids and derivatives)."},
    {"qnum": "07.2", "specRef": "3.3.9", "marks": 1, "stem": "Paper 2 Question 07.2 (Carboxylic acids and derivatives)."},
    {"qnum": "07.3", "specRef": "3.3.9", "marks": 1, "stem": "Paper 2 Question 07.3 (Carboxylic acids and derivatives)."},
    {"qnum": "07.4", "specRef": "3.3.9", "marks": 1, "stem": "Paper 2 Question 07.4 (Carboxylic acids and derivatives)."},
    {"qnum": "08.1", "specRef": "3.3.10", "marks": 2, "stem": "Paper 2 Question 08.1 (Aromatic chemistry)."},
    {"qnum": "08.2", "specRef": "3.3.10", "marks": 2, "stem": "Paper 2 Question 08.2 (Aromatic chemistry)."},
    {"qnum": "08.3", "specRef": "3.3.10", "marks": 3, "stem": "Paper 2 Question 08.3 (Aromatic chemistry)."},
    {"qnum": "09.1", "specRef": "RP", "marks": 2, "stem": "Paper 2 Question 09.1 (Required practical).", "figures": ["fig-q9-y.jpg"]},
    {"qnum": "09.2", "specRef": "3.1.2", "marks": 5, "stem": "Paper 2 Question 09.2 (Amount of substance).", "figures": ["fig-q9-y.jpg"]},
    {"qnum": "09.3", "specRef": "RP", "marks": 2, "stem": "Paper 2 Question 09.3 (Required practical)."},
    {"qnum": "09.4", "specRef": "RP", "marks": 1, "stem": "Paper 2 Question 09.4 (Required practical)."},
    {"qnum": "09.5", "specRef": "3.1.1", "marks": 2, "stem": "Paper 2 Question 09.5 (Atomic structure)."},
    {"qnum": "10.1", "specRef": "3.3.11", "marks": 3, "stem": "Paper 2 Question 10.1 (Amines).", "figures": ["fig-q10-scheme.jpg"]},
    {"qnum": "10.2", "specRef": "3.3.9", "marks": 1, "stem": "Paper 2 Question 10.2 (Carboxylic acids and derivatives)."},
    {"qnum": "10.3", "specRef": "3.3.2", "marks": 2, "stem": "Paper 2 Question 10.3 (Alkanes).", "figures": ["fig-q10-scheme.jpg"]},
    {"qnum": "10.4", "specRef": "3.3.11", "marks": 2, "stem": "Paper 2 Question 10.4 (Amines).", "figures": ["fig-q10-scheme.jpg"]},
    {"qnum": "10.5", "specRef": "3.3.11", "marks": 2, "stem": "Paper 2 Question 10.5 (Amines).", "figures": ["fig-q10-scheme.jpg"]},
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

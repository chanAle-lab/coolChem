"""Ingest AQA A-level Chemistry June 2023 Paper 3 (7405/3) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530732008_fdd077e8.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530731978_81760ab8.pdf"
)

PAPER_ID = "2023-june-7405-3"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2023,
    "series": "June",
    "unit": "7405/3",
    "level": "A-level",
    "date": "2023-06-23",
    "title": "7405/3 — A-level Paper 3: Synoptic (June 2023)",
    "totalMarks": 90,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-method.jpg", "page": 2, "x0": 40, "y0": 135, "x1": 555, "y1": 430},
    {"filename": "fig-q3-fig2.jpg", "page": 8, "x0": 40, "y0": 195, "x1": 555, "y1": 440},
    {"filename": "fig-q3-fig4.jpg", "page": 10, "x0": 40, "y0": 260, "x1": 555, "y1": 580},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 4, "01.5": 4, "01.6": 4, "01.7": 5, "01.8": 5,
    "02.1": 6, "02.2": 6, "02.3": 6, "02.4": 6, "02.5": 7, "02.6": 7,
    "03.1": 8, "03.2": 8, "03.3": 9, "03.4": 9, "03.5": 10, "03.6": 10, "03.7": 11,
    "04": 12,
    "05.1": 14, "05.2": 15, "05.3": 15,
    "06.1": 16, "06.2": 16,
    "07": 17, "08": 17,
    "09": 18, "10": 18,
    "11": 19, "12": 19,
    "13": 20, "14": 20, "15": 20,
    "16": 21, "17": 21, "18": 21,
    "19": 22, "20": 22, "21": 22,
    "22": 23, "23": 23, "24": 23,
    "25": 24, "26": 24,
    "27": 25, "28": 25,
    "29": 26, "30": 26,
    "31": 27, "32": 27,
    "33": 28, "34": 28, "35": 28,
    "36": 29,
}

MS_QNUM_MAP = {}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.9", "marks": 1, "stem": "State the role of concentrated sulfuric acid in the preparation of ethyl ethanoate."},
    {"qnum": "01.2", "specRef": "RP", "marks": 1, "stem": "Suggest how the flammable reaction mixture should be heated in step 1."},
    {"qnum": "01.3", "specRef": "RP", "marks": 4, "stem": "Identify two mistakes in the reflux apparatus and state the problem caused by each."},
    {"qnum": "01.4", "specRef": "RP", "marks": 2, "stem": "State why sodium carbonate is added and explain the build-up of pressure.", "figures": ["fig-q1-method.jpg"]},
    {"qnum": "01.5", "specRef": "RP", "marks": 2, "stem": "Give a reason why two layers form and suggest why ethyl ethanoate forms the upper layer.", "figures": ["fig-q1-method.jpg"]},
    {"qnum": "01.6", "specRef": "RP", "marks": 1, "stem": "State why anhydrous calcium chloride is added in step 6.", "figures": ["fig-q1-method.jpg"]},
    {"qnum": "01.7", "specRef": "3.1.2", "marks": 5, "stem": "Determine the limiting reagent and calculate the percentage yield of ethyl ethanoate."},
    {"qnum": "01.8", "specRef": "3.1.6", "marks": 1, "stem": "Suggest a reason why the percentage yield is not 100%."},
    {"qnum": "02.1", "specRef": "3.3.1", "marks": 1, "stem": "Draw the displayed formula of an unbranched position isomer of pentan-2-ol that dehydrates to a single alkene."},
    {"qnum": "02.2", "specRef": "3.3.1", "marks": 1, "stem": "Draw the skeletal formula of a chain isomer of pentan-2-ol that dehydrates to a mixture of alkenes."},
    {"qnum": "02.3", "specRef": "3.3.1", "marks": 1, "stem": "Draw the structure of an unbranched functional group isomer of pentan-2-ol."},
    {"qnum": "02.4", "specRef": "3.3.5", "marks": 1, "stem": "Draw the structure of an alcohol isomer of pentan-2-ol that is not dehydrated by concentrated H2SO4."},
    {"qnum": "02.5", "specRef": "3.3.5", "marks": 3, "stem": "Complete the dehydration mechanism with two curly arrows and name the mechanism."},
    {"qnum": "02.6", "specRef": "3.3.4", "marks": 1, "stem": "Draw the structure of the other stereoisomer formed in Question 02.5."},
    {"qnum": "03.1", "specRef": "3.3.13", "marks": 2, "stem": "Complete the structure of endomorphin-2 in Figure 2."},
    {"qnum": "03.2", "specRef": "3.3.13", "marks": 1, "stem": "Use Figure 2 to draw the skeletal formula of proline.", "figures": ["fig-q3-fig2.jpg"]},
    {"qnum": "03.3", "specRef": "3.3.13", "marks": 2, "stem": "State a reagent and conditions needed for the hydrolysis of endomorphin-2."},
    {"qnum": "03.4", "specRef": "RP", "marks": 3, "stem": "Identify the missing piece of TLC apparatus in Figure 3 and explain why it is needed."},
    {"qnum": "03.5", "specRef": "RP", "marks": 1, "stem": "State why the amino acids separate on the TLC plate."},
    {"qnum": "03.6", "specRef": "RP", "marks": 2, "stem": "Name a suitable developing agent for TLC and state why it is needed."},
    {"qnum": "03.7", "specRef": "RP", "marks": 1, "stem": "Determine the Rf value for Tyr from Figure 4.", "figures": ["fig-q3-fig4.jpg"]},
    {"qnum": "04", "specRef": "3.2.6", "marks": 6, "stem": "Identify iron salts L and M, all precipitates, explain effervescence, and give ionic equations."},
    {"qnum": "05.1", "specRef": "3.1.4", "marks": 3, "stem": "Calculate the molar enthalpy of vaporisation ΔHvap for water."},
    {"qnum": "05.2", "specRef": "3.1.3", "marks": 4, "stem": "Explain why ethanol, ethylamine, and methoxymethane are polar and why ethylamine is least polar."},
    {"qnum": "05.3", "specRef": "3.1.3", "marks": 3, "stem": "Explain the trend in boiling points of ethanol, ethylamine, and methoxymethane."},
    {"qnum": "06.1", "specRef": "3.1.2", "marks": 2, "stem": "Show by calculation that calcium hydroxide is in excess."},
    {"qnum": "06.2", "specRef": "3.1.12", "marks": 5, "stem": "Calculate the pH of a saturated Ca(OH)2 solution at 293 K."},
    {"qnum": "07", "specRef": "3.1.1", "marks": 1, "stem": "Paper 3 Section B Question 07 (Atomic structure)."},
    {"qnum": "08", "specRef": "3.1.2", "marks": 1, "stem": "Paper 3 Section B Question 08 (Mr calculation)."},
    {"qnum": "09", "specRef": "3.1.3", "marks": 1, "stem": "Paper 3 Section B Question 09 (Electron delocalisation)."},
    {"qnum": "10", "specRef": "3.1.4", "marks": 1, "stem": "Paper 3 Section B Question 10 (Enthalpy of formation)."},
    {"qnum": "11", "specRef": "3.1.5", "marks": 1, "stem": "Paper 3 Section B Question 11 (Maxwell-Boltzmann distribution)."},
    {"qnum": "12", "specRef": "3.1.5", "marks": 1, "stem": "Paper 3 Section B Question 12 (Catalyst and rate)."},
    {"qnum": "13", "specRef": "3.1.6", "marks": 1, "stem": "Paper 3 Section B Question 13 (Equilibrium constant Kc)."},
    {"qnum": "14", "specRef": "3.1.7", "marks": 1, "stem": "Paper 3 Section B Question 14 (Oxidation states)."},
    {"qnum": "15", "specRef": "3.1.8", "marks": 1, "stem": "Paper 3 Section B Question 15 (Vaporisation of water)."},
    {"qnum": "16", "specRef": "3.1.12", "marks": 1, "stem": "Paper 3 Section B Question 16 (Bronsted-Lowry acid)."},
    {"qnum": "17", "specRef": "3.1.12", "marks": 1, "stem": "Paper 3 Section B Question 17 (pH of NaOH)."},
    {"qnum": "18", "specRef": "3.1.12", "marks": 1, "stem": "Paper 3 Section B Question 18 (Ka from pH)."},
    {"qnum": "19", "specRef": "3.2.1", "marks": 1, "stem": "Paper 3 Section B Question 19 (Period 3 trends)."},
    {"qnum": "20", "specRef": "3.1.12", "marks": 1, "stem": "Paper 3 Section B Question 20 (Buffer solutions)."},
    {"qnum": "21", "specRef": "3.2.2", "marks": 1, "stem": "Paper 3 Section B Question 21 (Barium with water)."},
    {"qnum": "22", "specRef": "3.2.3", "marks": 1, "stem": "Paper 3 Section B Question 22 (Strongest reducing agent)."},
    {"qnum": "23", "specRef": "3.2.5", "marks": 1, "stem": "Paper 3 Section B Question 23 (Shapes of complex ions)."},
    {"qnum": "24", "specRef": "3.2.5", "marks": 1, "stem": "Paper 3 Section B Question 24 (Redox with MnO4-)."},
    {"qnum": "25", "specRef": "3.1.6", "marks": 1, "stem": "Paper 3 Section B Question 25 (Catalysts and equilibrium)."},
    {"qnum": "26", "specRef": "3.3.1", "marks": 1, "stem": "Paper 3 Section B Question 26 (Organic synthesis scheme)."},
    {"qnum": "27", "specRef": "3.2.5", "marks": 1, "stem": "Paper 3 Section B Question 27 (Heterogeneous catalysts)."},
    {"qnum": "28", "specRef": "3.1.2", "marks": 1, "stem": "Paper 3 Section B Question 28 (Mole fraction)."},
    {"qnum": "29", "specRef": "3.3.3", "marks": 1, "stem": "Paper 3 Section B Question 29 (Reactions of halogenoalkanes with KOH)."},
    {"qnum": "30", "specRef": "3.3.3", "marks": 1, "stem": "Paper 3 Section B Question 30 (Ozone in upper atmosphere)."},
    {"qnum": "31", "specRef": "3.3.4", "marks": 1, "stem": "Paper 3 Section B Question 31 (Alkenes to alcohols)."},
    {"qnum": "32", "specRef": "3.3.5", "marks": 1, "stem": "Paper 3 Section B Question 32 (Oxidation of 1-phenylethanol)."},
    {"qnum": "33", "specRef": "3.3.8", "marks": 1, "stem": "Paper 3 Section B Question 33 (Distinguishing ketones)."},
    {"qnum": "34", "specRef": "3.3.11", "marks": 1, "stem": "Paper 3 Section B Question 34 (Base strength of amines)."},
    {"qnum": "35", "specRef": "3.3.13", "marks": 1, "stem": "Paper 3 Section B Question 35 (Enzymes)."},
    {"qnum": "36", "specRef": "3.2.5", "marks": 1, "stem": "Paper 3 Section B Question 36 (Cisplatin and DNA)."},
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

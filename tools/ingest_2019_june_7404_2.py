"""Ingest AQA AS Chemistry June 2019 Paper 2 (7404/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521528906_e59d1101.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521528943_3a076ba8.pdf"
)

PAPER_ID = "2019-june-7404-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2019,
    "series": "June",
    "unit": "7404/2",
    "level": "AS",
    "date": "2019-05-23",
    "title": "7404/2 — AS Paper 2: Organic and Physical Chemistry (June 2019)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-stem.jpg", "page": 2, "x0": 40, "y0": 65, "x1": 555, "y1": 240},
    {"filename": "fig-q2-eq.jpg", "page": 3, "x0": 40, "y0": 65, "x1": 555, "y1": 140},
    {"filename": "fig-q6-stem.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 210},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2,
    "02.1": 3, "02.2": 3, "02.3": 3,
    "03.1": 4, "03.2": 5, "03.3": 6,
    "04.1": 7, "04.2": 7, "04.3": 8,
    "05.1": 9, "05.2": 9, "05.3": 10,
    "06.1": 12, "06.2": 13, "06.3": 13,
    "07.1": 14, "07.2": 14, "07.3": 15,
    "08.1": 16, "08.2": 17,
    "09.1": 19, "09.2": 19, "09.3": 20,
    "10": 22,
    "11": 23, "12": 23, "13": 23,
    "14": 24, "15": 24, "16": 24,
    "17": 25, "18": 25, "19": 25,
    "20": 26, "21": 26, "22": 26,
    "23": 27,
    "24": 28,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.6", "marks": 3, "stem": "Give a reagent and observations to distinguish between compounds A (pentan-2-one) and B (pentanoic acid)."},
    {"qnum": "01.2", "specRef": "3.3.6", "marks": 3, "stem": "Give a reagent and observations to distinguish between compounds A (pentan-2-one) and C (cyclohexanecarbaldehyde).", "figures": ["fig-q1-stem.jpg"]},
    {"qnum": "02.1", "specRef": "3.3.3", "marks": 2, "stem": "Outline the mechanism for the reaction of bromoethane with potassium cyanide."},
    {"qnum": "02.2", "specRef": "3.3.1", "marks": 1, "stem": "Give the IUPAC name of compound D (CH3CH2CN).", "figures": ["fig-q2-eq.jpg"]},
    {"qnum": "02.3", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the percentage atom economy for the formation of D in CH3CH2Br + KCN -> CH3CH2CN + KBr.", "figures": ["fig-q2-eq.jpg"]},
    {"qnum": "03.1", "specRef": "3.1.4", "marks": 4, "stem": "Calculate the final temperature of the water from the calorimetry data for cyclohexane combustion."},
    {"qnum": "03.2", "specRef": "3.1.4", "marks": 1, "stem": "Suggest a practical reason why the temperature rise recorded was smaller than it should have been."},
    {"qnum": "03.3", "specRef": "3.1.4", "marks": 3, "stem": "Use Table 2 enthalpies of combustion to calculate the enthalpy change for 6C(s) + 6H2(g) -> C6H12(l)."},
    {"qnum": "04.1", "specRef": "3.3.2", "marks": 1, "stem": "Give an equation for the complete combustion of octane (C8H18)."},
    {"qnum": "04.2", "specRef": "3.3.2", "marks": 1, "stem": "Give an equation for a reaction that removes nitrogen monoxide in a catalytic converter."},
    {"qnum": "04.3", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the mass, in kg, of CaO needed to react with 6.49 million tonnes of SO2."},
    {"qnum": "05.1", "specRef": "3.1.3", "marks": 3, "stem": "Draw a diagram to show how two methanol molecules interact through hydrogen bonding, including partial charges and lone pairs."},
    {"qnum": "05.2", "specRef": "3.1.3", "marks": 1, "stem": "Explain why the bond angle around the oxygen atom in methanol is smaller than 109.5 deg."},
    {"qnum": "05.3", "specRef": "3.1.6", "marks": 6, "stem": "Describe how catalyst, pressure and temperature affect equilibrium yield, reaction rate and cost in methanol synthesis."},
    {"qnum": "06.1", "specRef": "3.3.4", "marks": 5, "stem": "Name and outline the mechanism for the reaction of propene with concentrated sulfuric acid to form isomer E."},
    {"qnum": "06.2", "specRef": "3.3.4", "marks": 1, "stem": "Draw the structure of isomer F.", "figures": ["fig-q6-stem.jpg"]},
    {"qnum": "06.3", "specRef": "3.3.4", "marks": 2, "stem": "Explain why more of isomer E than isomer F is formed in this reaction.", "figures": ["fig-q6-stem.jpg"]},
    {"qnum": "07.1", "specRef": "3.3.1", "marks": 1, "stem": "Draw the skeletal formula of propanedioic acid."},
    {"qnum": "07.2", "specRef": "RP", "marks": 6, "stem": "Describe how to prepare 250 cm3 of an aqueous standard solution of propanedioic acid containing an accurately measured mass."},
    {"qnum": "07.3", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the mass, in mg, of propanedioic acid (Mr = 104.0) needed to prepare 250 cm3 of a 0.00500 mol dm-3 solution."},
    {"qnum": "08.1", "specRef": "3.1.2", "marks": 3, "stem": "Calculate the minimum volume of 0.40 mol dm-3 K2Cr2O7 needed to oxidise 6.0 cm3 of propan-1-ol to propanal."},
    {"qnum": "08.2", "specRef": "RP", "marks": 3, "stem": "Complete and label the diagram to show the assembled distillation apparatus needed to prepare propanal from propan-1-ol."},
    {"qnum": "09.1", "specRef": "3.3.3", "marks": 1, "stem": "Give an equation for the breakdown of 1,2-dichlorotetrafluoroethane to form one chlorine radical and one other species."},
    {"qnum": "09.2", "specRef": "3.3.3", "marks": 2, "stem": "Give two equations to show how chlorine radicals catalyse the decomposition of ozone."},
    {"qnum": "09.3", "specRef": "3.1.2", "marks": 6, "stem": "Calculate the gas volume, liquid volume and expansion factor for 38.8 g of butane at 272 K and 101 kPa."},
    {"qnum": "10", "specRef": "3.1.2", "marks": 1, "stem": "What is the concentration, in mol dm-3, of ethanol if there are 80 mg of ethanol per 100 cm3 of blood?"},
    {"qnum": "11", "specRef": "3.1.5", "marks": 1, "stem": "Which statement is correct for the distribution curve of molecular energies in a gas?"},
    {"qnum": "12", "specRef": "3.1.6", "marks": 1, "stem": "When 1 mol NH3 dissociates 50% in NH3 <=> 0.5 N2 + 1.5 H2, what is the total moles of gas at equilibrium?"},
    {"qnum": "13", "specRef": "3.3.1", "marks": 1, "stem": "Which compound is not an isomer of tetrahydrofuran?"},
    {"qnum": "14", "specRef": "3.3.1", "marks": 1, "stem": "How many isomers are there of C3H9N?"},
    {"qnum": "15", "specRef": "3.3.2", "marks": 1, "stem": "Which equation represents a propagation step?"},
    {"qnum": "16", "specRef": "3.3.3", "marks": 1, "stem": "Which compound can react with ammonia to produce propylamine?"},
    {"qnum": "17", "specRef": "3.3.4", "marks": 1, "stem": "Which statement is not correct about CH2=C(CH3)CH2Br?"},
    {"qnum": "18", "specRef": "3.3.5", "marks": 1, "stem": "Which compound can be oxidised to form (CH3)2CHCOCH3?"},
    {"qnum": "19", "specRef": "3.3.3", "marks": 1, "stem": "Which species can act as a nucleophile?"},
    {"qnum": "20", "specRef": "3.3.5", "marks": 1, "stem": "Which alcohol forms a mixture of alkenes when dehydrated?"},
    {"qnum": "21", "specRef": "3.1.3", "marks": 1, "stem": "Which compound has the highest boiling point?"},
    {"qnum": "22", "specRef": "3.3.3", "marks": 1, "stem": "Which compound could not be produced by reacting 2-bromo-3-methylbutane with sodium hydroxide?"},
    {"qnum": "23", "specRef": "3.3.6", "marks": 1, "stem": "Which compound produces the infrared spectrum shown?"},
    {"qnum": "24", "specRef": "3.1.4", "marks": 1, "stem": "What is the heat released by each molecule, in joules, when ethanol undergoes complete combustion?"},
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
    ms_map = crop_official_markschemes(
        MS_PDF,
        [q["qnum"] for q in QUESTIONS],
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
            "markscheme": f"img/{PAPER_ID}/ms/{ms_map[qnum]}",
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

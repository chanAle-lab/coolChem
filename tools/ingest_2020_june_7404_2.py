"""Ingest AQA AS Chemistry June 2020 Paper 2 (7404/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521576246_baa8f8f9.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521576156_66ebd000.pdf"
)

PAPER_ID = "2020-june-7404-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2020,
    "series": "June",
    "unit": "7404/2",
    "level": "AS",
    "date": "2020-05-21",
    "title": "7404/2 — AS Paper 2: Organic and Physical Chemistry (June 2020)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q2-stem.jpg", "page": 6, "x0": 40, "y0": 65, "x1": 555, "y1": 370},
    {"filename": "fig-q8-eq.jpg", "page": 19, "x0": 40, "y0": 65, "x1": 555, "y1": 150},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 3, "01.5": 4,
    "02.1": 6, "02.2": 6, "02.3": 7, "02.4": 8, "02.5": 8, "02.6": 8,
    "03": 10,
    "04.1": 12, "04.2": 13,
    "05": 14,
    "06.1": 16, "06.2": 16, "06.3": 16,
    "07.1": 17, "07.2": 17, "07.3": 18,
    "08.1": 19, "08.2": 19, "08.3": 20,
    "09": 21, "10": 21,
    "11": 22, "12": 22, "13": 22,
    "14": 23, "15": 23, "16": 23,
    "17": 24, "18": 24, "19": 24,
    "20": 25, "21": 25,
    "22": 26, "23": 26,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.4", "marks": 2, "stem": "Define the term standard enthalpy of formation."},
    {"qnum": "01.2", "specRef": "3.1.4", "marks": 3, "stem": "Calculate the standard enthalpy of formation of propan-1-ol using data from Table 1."},
    {"qnum": "01.3", "specRef": "3.3.3", "marks": 3, "stem": "State why UV light is needed and give equations for each propagation step forming 1-chloropropane from propane."},
    {"qnum": "01.4", "specRef": "3.1.3", "marks": 1, "stem": "Define the term electronegativity."},
    {"qnum": "01.5", "specRef": "3.3.3", "marks": 5, "stem": "Name and outline the mechanism for the reaction of ammonia with 1-chloropropane to form propylamine."},
    {"qnum": "02.1", "specRef": "RP", "marks": 1, "stem": "Suggest why the student records the disappearing-cross times to the nearest second rather than 0.01 s.", "figures": ["fig-q2-stem.jpg"]},
    {"qnum": "02.2", "specRef": "RP", "marks": 1, "stem": "Complete Table 2 by calculating 1/t at 54 C.", "figures": ["fig-q2-stem.jpg"]},
    {"qnum": "02.3", "specRef": "RP", "marks": 2, "stem": "Plot the values of 1/t against temperature on Figure 1 and draw a line of best fit.", "figures": ["fig-q2-stem.jpg"]},
    {"qnum": "02.4", "specRef": "RP", "marks": 1, "stem": "Use your line of best fit to estimate the time for the cross to disappear at 40 C."},
    {"qnum": "02.5", "specRef": "RP", "marks": 1, "stem": "Suggest, by considering the products of this reaction, why small amounts of reactants are used.", "figures": ["fig-q2-stem.jpg"]},
    {"qnum": "02.6", "specRef": "RP", "marks": 1, "stem": "Suggest why the student chose not to carry out experiments at temperatures in the range 1-10 C."},
    {"qnum": "03", "specRef": "3.1.2", "marks": 6, "stem": "Calculate percentage yield for Method 1, percentage atom economy for Method 2, and state their importance."},
    {"qnum": "04.1", "specRef": "3.1.3", "marks": 3, "stem": "Explain why pentan-2-ol (119 C) has a higher boiling point than pent-1-ene (30 C)."},
    {"qnum": "04.2", "specRef": "3.3.5", "marks": 5, "stem": "State the reagent and condition, and outline the mechanism for the elimination of water from pentan-2-ol to form pent-1-ene."},
    {"qnum": "05", "specRef": "3.3.1", "marks": 6, "stem": "Explain the differences between structural isomerism and stereoisomerism using examples with formula C4H8."},
    {"qnum": "06.1", "specRef": "3.3.4", "marks": 3, "stem": "Give an equation, showing structural formulas, for the conversion of chloroethene into poly(chloroethene)."},
    {"qnum": "06.2", "specRef": "3.3.4", "marks": 2, "stem": "State what you would observe if bromine water was added to poly(chloroethene) and explain this observation."},
    {"qnum": "06.3", "specRef": "3.3.4", "marks": 2, "stem": "Deduce the molecular formula of the plasticiser DEHP and state why a plasticiser is added to PVC."},
    {"qnum": "07.1", "specRef": "3.3.1", "marks": 1, "stem": "Draw the skeletal formula of ethanedioic acid."},
    {"qnum": "07.2", "specRef": "3.3.5", "marks": 2, "stem": "State suitable reagent(s) and a condition for the oxidation of ethane-1,2-diol to ethanedioic acid."},
    {"qnum": "07.3", "specRef": "3.1.2", "marks": 5, "stem": "Show that NaOH is in excess and calculate the mass, in mg, of sodium ethanedioate formed."},
    {"qnum": "08.1", "specRef": "3.1.6", "marks": 2, "stem": "Give an expression for Kc for C2H5OH(g) + H2O(g) <=> 2CO(g) + 4H2(g) and state its units.", "figures": ["fig-q8-eq.jpg"]},
    {"qnum": "08.2", "specRef": "3.1.6", "marks": 3, "stem": "Calculate Kc from the equilibrium amounts in Table 4 in a 750 cm3 container.", "figures": ["fig-q8-eq.jpg"]},
    {"qnum": "08.3", "specRef": "3.1.6", "marks": 4, "stem": "Predict and explain the effect of increasing pressure on the equilibrium yield of hydrogen and on Kc.", "figures": ["fig-q8-eq.jpg"]},
    {"qnum": "09", "specRef": "3.3.2", "marks": 1, "stem": "Which statement is correct about thermal cracking?"},
    {"qnum": "10", "specRef": "3.3.3", "marks": 1, "stem": "Which statement is not correct about ozone?"},
    {"qnum": "11", "specRef": "3.3.1", "marks": 1, "stem": "What is the IUPAC name for this compound?"},
    {"qnum": "12", "specRef": "3.3.4", "marks": 1, "stem": "What is the IUPAC name of the major product of the reaction between 2-ethylbut-1-ene and hydrogen bromide?"},
    {"qnum": "13", "specRef": "3.3.6", "marks": 1, "stem": "Which can be used to distinguish between (CH3)2CHCH2CHO and (CH3)3CCHO?"},
    {"qnum": "14", "specRef": "3.3.3", "marks": 1, "stem": "An excess of methane reacts with chlorine in the presence of UV radiation. What are the main products?"},
    {"qnum": "15", "specRef": "3.3.4", "marks": 1, "stem": "In which reaction does the inorganic reagent act initially as an electrophile?"},
    {"qnum": "16", "specRef": "3.1.2", "marks": 1, "stem": "What is the empirical formula of a hydrocarbon that contains 90% carbon by mass?"},
    {"qnum": "17", "specRef": "3.1.2", "marks": 1, "stem": "Which compound (ethanoic acid, 1-fluoropropane, propanenitrile, propylamine) has the lowest relative molecular mass?"},
    {"qnum": "18", "specRef": "3.3.5", "marks": 1, "stem": "Which statement is correct about the production and use of ethanol as a biofuel?"},
    {"qnum": "19", "specRef": "3.1.2", "marks": 1, "stem": "What is the minimum volume of 0.0500 mol dm-3 aqueous bromine needed to react completely with 0.0200 g of buta-1,3-diene?"},
    {"qnum": "20", "specRef": "3.1.5", "marks": 1, "stem": "Which statement about the molecules in a sample of a gas is correct?"},
    {"qnum": "21", "specRef": "3.1.4", "marks": 1, "stem": "What is the enthalpy change for CH4(g) -> C(s) + 4H(g)?"},
    {"qnum": "22", "specRef": "3.1.2", "marks": 1, "stem": "The temperature changed from 21.8 C to 19.2 C (+/- 0.1 C per reading). What is the percentage uncertainty?"},
    {"qnum": "23", "specRef": "3.1.4", "marks": 1, "stem": "Which expression gives the enthalpy of combustion (in J mol-1) assuming no heat loss?"},
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

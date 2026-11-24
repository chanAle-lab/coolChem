"""Ingest AQA AS Chemistry June 2021 Paper 1 (7404/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521628181_b0474f70.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521628181_8d83d596.pdf"
)

PAPER_ID = "2021-june-7404-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2021,
    "series": "June",
    "unit": "7404/1",
    "level": "AS",
    "date": "2021-06-01",
    "title": "7404/1 — AS Paper 1: Inorganic and Physical Chemistry (June 2021)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q4-table2.jpg", "page": 6, "x0": 40, "y0": 65, "x1": 555, "y1": 280},
    {"filename": "fig-q8-table3.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 320},
    {"filename": "fig-q10-eq.jpg", "page": 16, "x0": 40, "y0": 65, "x1": 555, "y1": 135},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3,
    "02.1": 4, "02.2": 4, "02.3": 4, "02.4": 4,
    "03.1": 5, "03.2": 5,
    "04.1": 6, "04.2": 6, "04.3": 7,
    "05.1": 8, "05.2": 8, "05.3": 8,
    "06": 9,
    "07.1": 10, "07.2": 10, "07.3": 11,
    "08.1": 12, "08.2": 13,
    "09": 14,
    "10.1": 16, "10.2": 16, "10.3": 17,
    "11": 18, "12": 18,
    "13": 19, "14": 19, "15": 19,
    "16": 20, "17": 20, "18": 20,
    "19": 21, "20": 21,
    "21": 22, "22": 22, "23": 22,
    "24": 23, "25": 23,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.1", "marks": 2, "stem": "State two features of Rutherford's model of the atom shown in Figure 1."},
    {"qnum": "01.2", "specRef": "3.1.1", "marks": 4, "stem": "Calculate the relative atomic mass (Ar) of the sample of tin to 1 decimal place from the TOF mass spectrum data in Table 1."},
    {"qnum": "02.1", "specRef": "3.2.2", "marks": 2, "stem": "State one observation when magnesium reacts with steam and give an equation, including state symbols."},
    {"qnum": "02.2", "specRef": "3.1.3", "marks": 2, "stem": "Describe the bonding in magnesium."},
    {"qnum": "02.3", "specRef": "3.1.3", "marks": 3, "stem": "Explain why magnesium has a higher melting point than sodium."},
    {"qnum": "02.4", "specRef": "3.2.2", "marks": 1, "stem": "State a medical use for magnesium hydroxide."},
    {"qnum": "03.1", "specRef": "3.1.7", "marks": 1, "stem": "State, in terms of electrons, the meaning of the term oxidising agent."},
    {"qnum": "03.2", "specRef": "3.1.7", "marks": 3, "stem": "Write half-equations and an overall equation for Cr2O7^2- oxidising SO3^2- in acidic conditions to Cr3+ and SO4^2-."},
    {"qnum": "04.1", "specRef": "3.2.2", "marks": 2, "stem": "Identify solutions A and B from the test-tube reactions in Table 2.", "figures": ["fig-q4-table2.jpg"]},
    {"qnum": "04.2", "specRef": "3.2.2", "marks": 2, "stem": "Give ionic equations for the reactions observed in solution A and solution B.", "figures": ["fig-q4-table2.jpg"]},
    {"qnum": "04.3", "specRef": "3.2.3", "marks": 3, "stem": "Describe a further test or tests to show whether solution C contains chloride ions or bromide ions.", "figures": ["fig-q4-table2.jpg"]},
    {"qnum": "05.1", "specRef": "3.1.3", "marks": 3, "stem": "Explain how the intermolecular forces arise between molecules of chlorine."},
    {"qnum": "05.2", "specRef": "3.2.3", "marks": 2, "stem": "Explain why bromine has a higher boiling point than chlorine."},
    {"qnum": "05.3", "specRef": "3.2.3", "marks": 1, "stem": "Give an equation for the reaction of chlorine with cold, dilute aqueous sodium hydroxide."},
    {"qnum": "06", "specRef": "3.1.2", "marks": 5, "stem": "Show that CaSO4 is the limiting reagent when 2.50 g of CaS reacts with 9.85 g of CaSO4 and calculate the total volume of SO2 formed."},
    {"qnum": "07.1", "specRef": "3.1.4", "marks": 2, "stem": "State the meaning of the term standard enthalpy of combustion."},
    {"qnum": "07.2", "specRef": "3.1.4", "marks": 3, "stem": "Calculate the enthalpy of combustion of propan-1-ol from the student's calorimetry experiment."},
    {"qnum": "07.3", "specRef": "3.1.4", "marks": 1, "stem": "Give one possible reason, other than heat loss, why the experimental enthalpy of combustion is less exothermic than the calculated value."},
    {"qnum": "08.1", "specRef": "3.1.2", "marks": 6, "stem": "Calculate the percentage by mass of ethanoic acid in the 5.60 g contaminated sample using the titration data in Table 3.", "figures": ["fig-q8-table3.jpg"]},
    {"qnum": "08.2", "specRef": "RP", "marks": 2, "stem": "State and explain the effect of rinsing the burette with deionised water before filling with NaOH on the calculated percentage by mass."},
    {"qnum": "09", "specRef": "3.1.6", "marks": 6, "stem": "Explain the industrial conditions of temperature and pressure used for the reversible reaction CH4(g) + H2O(g) <-> CO(g) + 3 H2(g)."},
    {"qnum": "10.1", "specRef": "3.1.6", "marks": 1, "stem": "Give an expression for the equilibrium constant (Kc) for 2 SO2(g) + O2(g) <-> 2 SO3(g).", "figures": ["fig-q10-eq.jpg"]},
    {"qnum": "10.2", "specRef": "3.1.6", "marks": 3, "stem": "Calculate Kc and deduce its units for the SO2 / O2 / SO3 equilibrium.", "figures": ["fig-q10-eq.jpg"]},
    {"qnum": "10.3", "specRef": "3.1.2", "marks": 5, "stem": "Calculate the temperature, in K, of the equilibrium mixture in the 3500 cm3 vessel at 255 kPa."},
    {"qnum": "11", "specRef": "3.1.1", "marks": 1, "stem": "Which species has the same electron configuration as an atom of argon?"},
    {"qnum": "12", "specRef": "3.1.3", "marks": 1, "stem": "Which molecule has a permanent dipole?"},
    {"qnum": "13", "specRef": "3.1.3", "marks": 1, "stem": "Which molecule is not able to form a co-ordinate bond with another species?"},
    {"qnum": "14", "specRef": "3.1.3", "marks": 1, "stem": "Which species has a square planar shape?"},
    {"qnum": "15", "specRef": "3.1.3", "marks": 1, "stem": "Which substance does not form hydrogen bonds between its molecules?"},
    {"qnum": "16", "specRef": "3.1.7", "marks": 1, "stem": "Which compound contains a chlorine atom with an oxidation state of +4?"},
    {"qnum": "17", "specRef": "3.2.1", "marks": 1, "stem": "Which element is classified as a d block element?"},
    {"qnum": "18", "specRef": "3.2.2", "marks": 1, "stem": "Which property decreases down Group 2?"},
    {"qnum": "19", "specRef": "3.2.3", "marks": 1, "stem": "Which pair of solutions, when mixed, reacts to form a dark brown solution?"},
    {"qnum": "20", "specRef": "3.2.3", "marks": 1, "stem": "Which solid sodium halide does not reduce concentrated sulfuric acid?"},
    {"qnum": "21", "specRef": "3.1.1", "marks": 1, "stem": "Which atom has one more proton and two more neutrons than 31P?"},
    {"qnum": "22", "specRef": "3.2.2", "marks": 1, "stem": "What is a use for barium sulfate?"},
    {"qnum": "23", "specRef": "3.1.2", "marks": 1, "stem": "Which sample has the greatest mass?"},
    {"qnum": "24", "specRef": "3.1.1", "marks": 1, "stem": "Which element has a first ionisation energy lower than that of sulfur?"},
    {"qnum": "25", "specRef": "3.1.1", "marks": 1, "stem": "Deduce the group of element Z from its first seven successive ionisation energies."},
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

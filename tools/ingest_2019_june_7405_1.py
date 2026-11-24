"""Ingest AQA A-level Chemistry June 2019 Paper 1 (7405/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521529036_e244e3b7.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521529014_f929b072.pdf"
)

PAPER_ID = "2019-june-7405-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2019,
    "series": "June",
    "unit": "7405/1",
    "level": "A-level",
    "date": "2019-06-04",
    "title": "7405/1 — A-level Paper 1: Inorganic and Physical Chemistry (June 2019)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-cycle.jpg", "page": 2, "x0": 40, "y0": 65, "x1": 555, "y1": 510},
    {"filename": "fig-q2-ms.jpg", "page": 4, "x0": 40, "y0": 65, "x1": 555, "y1": 345},
    {"filename": "fig-q4-fig3.jpg", "page": 7, "x0": 40, "y0": 65, "x1": 555, "y1": 380},
    {"filename": "fig-q5-3-eq.jpg", "page": 10, "x0": 40, "y0": 540, "x1": 555, "y1": 635},
    {"filename": "fig-q7-eq.jpg", "page": 15, "x0": 40, "y0": 65, "x1": 555, "y1": 150},
    {"filename": "fig-q9-fig4.jpg", "page": 22, "x0": 40, "y0": 65, "x1": 555, "y1": 640},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 3,
    "02.1": 4, "02.2": 5, "02.3": 5,
    "03.1": 6, "03.2": 6, "03.3": 6, "03.4": 6, "03.5": 6,
    "04.1": 7, "04.2": 7, "04.3": 7, "04.4": 8, "04.5": 8,
    "05.1": 10, "05.2": 10, "05.3": 10, "05.4": 11, "05.5": 11,
    "06.1": 12, "06.2": 13, "06.3": 13, "06.4": 13, "06.5": 13, "06.6": 14,
    "07.1": 15, "07.2": 16, "07.3": 17, "07.4": 17,
    "08.1": 18, "08.2": 18, "08.3": 19,
    "09.1": 21, "09.2": 22, "09.3": 23, "09.4": 24, "09.5": 25,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.8", "marks": 2, "stem": "Complete Figure 1 (Born-Haber cycle for CsI) by writing the formulas, including state symbols, on the two blank lines."},
    {"qnum": "01.2", "specRef": "3.1.8", "marks": 2, "stem": "Use Figure 1 and Table 1 to calculate the standard enthalpy of atomisation of iodine.", "figures": ["fig-q1-cycle.jpg"]},
    {"qnum": "01.3", "specRef": "3.1.8", "marks": 1, "stem": "Deduce what the experimental (-585) and perfect ionic (-582) lattice enthalpies indicate about bonding in caesium iodide.", "figures": ["fig-q1-cycle.jpg"]},
    {"qnum": "01.4", "specRef": "3.1.8", "marks": 4, "stem": "Use data from Table 2 to show that CsI(s) -> Cs(s) + 1/2 I2(s) is not feasible at 298 K."},
    {"qnum": "02.1", "specRef": "3.1.1", "marks": 4, "stem": "Describe the process of electrospray ionisation and give an equation for the ionisation of P."},
    {"qnum": "02.2", "specRef": "3.1.1", "marks": 1, "stem": "What is the relative molecular mass of P from Figure 2?", "figures": ["fig-q2-ms.jpg"]},
    {"qnum": "02.3", "specRef": "3.1.1", "marks": 5, "stem": "Calculate the relative molecular mass of Q from TOF mass spectrometry data."},
    {"qnum": "03.1", "specRef": "3.2.1", "marks": 1, "stem": "State the meaning of the term periodicity."},
    {"qnum": "03.2", "specRef": "3.2.1", "marks": 1, "stem": "Identify the element in Period 4 with the highest electronegativity value."},
    {"qnum": "03.3", "specRef": "3.2.1", "marks": 3, "stem": "Identify the element in Period 4 with the largest atomic radius and explain your answer."},
    {"qnum": "03.4", "specRef": "3.2.4", "marks": 1, "stem": "Name the property of arsenic(III) oxide that describes its ability to react with both HCl and NaOH."},
    {"qnum": "03.5", "specRef": "3.1.7", "marks": 1, "stem": "Complete the equation for the formation of arsenic hydride: As2O3 + Zn + HNO3 -> AsH3 + Zn(NO3)2 + H2O."},
    {"qnum": "04.1", "specRef": "3.2.6", "marks": 3, "stem": "Give the formula and colour of Precipitate J and an equation for Reaction 1."},
    {"qnum": "04.2", "specRef": "3.2.5", "marks": 2, "stem": "Give the formula of complex ion L and an equation for Reaction 2.", "figures": ["fig-q4-fig3.jpg"]},
    {"qnum": "04.3", "specRef": "3.2.6", "marks": 1, "stem": "Suggest a reagent for Reaction 3 ([Fe(H2O)6]3+ -> [Fe(H2O)6]2+).", "figures": ["fig-q4-fig3.jpg"]},
    {"qnum": "04.4", "specRef": "3.2.6", "marks": 2, "stem": "Give the formula of Precipitate M and state its colour.", "figures": ["fig-q4-fig3.jpg"]},
    {"qnum": "04.5", "specRef": "3.2.5", "marks": 6, "stem": "Describe the different shapes of transition metal complexes and how they lead to isomerism, using cobalt(II) and platinum(II) examples."},
    {"qnum": "05.1", "specRef": "3.2.3", "marks": 2, "stem": "Give an equation for the reaction of solid sodium chloride with concentrated sulfuric acid and state the role of sulfuric acid."},
    {"qnum": "05.2", "specRef": "3.2.3", "marks": 3, "stem": "Give an equation, one other observation, and the role of sulfuric acid when sodium bromide reacts with concentrated sulfuric acid."},
    {"qnum": "05.3", "specRef": "3.2.3", "marks": 1, "stem": "Give the oxidation state of chlorine in NaClO3 and in NaCl."},
    {"qnum": "05.4", "specRef": "3.2.3", "marks": 1, "stem": "State, in terms of redox, what happens to chlorine in 3Cl2 + 6NaOH -> NaClO3 + 5NaCl + 3H2O.", "figures": ["fig-q5-3-eq.jpg"]},
    {"qnum": "05.5", "specRef": "3.2.3", "marks": 6, "stem": "Give the formulas of D, E, F and equations for the reactions of solution Y in Table 3."},
    {"qnum": "06.1", "specRef": "3.1.2", "marks": 6, "stem": "Calculate the percentage of copper by mass in the alloy from the thiosulfate titration data."},
    {"qnum": "06.2", "specRef": "RP", "marks": 2, "stem": "Suggest two ways to reduce the percentage uncertainty in measuring the sodium thiosulfate volume using the same apparatus."},
    {"qnum": "06.3", "specRef": "3.1.7", "marks": 1, "stem": "State the role of iodine in the reaction with sodium thiosulfate."},
    {"qnum": "06.4", "specRef": "3.2.5", "marks": 1, "stem": "Give the full electron configuration of a copper(II) ion."},
    {"qnum": "06.5", "specRef": "3.2.5", "marks": 2, "stem": "Explain why copper(I) iodide is white."},
    {"qnum": "06.6", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the volume, in cm3, that 5.00 g of iodine vapour occupies at 185 C and 100 kPa."},
    {"qnum": "07.1", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the mass of oxygen gas in an equilibrium mixture containing 6.08 g of sulfur dioxide."},
    {"qnum": "07.2", "specRef": "3.1.10", "marks": 4, "stem": "Calculate mole fractions, give Kp expression, and calculate total pressure for the SO3/SO2/O2 equilibrium at 1050 K."},
    {"qnum": "07.3", "specRef": "3.1.10", "marks": 2, "stem": "Explain how the Kp values at 1050 K and 500 K show that the forward reaction is endothermic.", "figures": ["fig-q7-eq.jpg"]},
    {"qnum": "07.4", "specRef": "3.1.10", "marks": 2, "stem": "Calculate Kp at 500 K and deduce units for SO3(g) <=> SO2(g) + 0.5 O2(g)."},
    {"qnum": "08.1", "specRef": "3.1.3", "marks": 3, "stem": "Draw a diagram to show hydrogen bonding between two ethanol molecules, including lone pairs and partial charges."},
    {"qnum": "08.2", "specRef": "3.1.3", "marks": 3, "stem": "Explain the difference in boiling points of ethanol (78 C) and methoxymethane (-24 C) in terms of intermolecular forces."},
    {"qnum": "08.3", "specRef": "3.1.3", "marks": 5, "stem": "Draw and name the shapes of POCl3 and ClF4-, and suggest the bond angle in ClF4-."},
    {"qnum": "09.1", "specRef": "3.1.12", "marks": 4, "stem": "Explain why pure water at 40 C (pH 6.67) is not acidic and determine Kw at this temperature."},
    {"qnum": "09.2", "specRef": "3.1.12", "marks": 3, "stem": "Use Figure 4 to determine the value of Ka for propanoic acid at 25 C.", "figures": ["fig-q9-fig4.jpg"]},
    {"qnum": "09.3", "specRef": "3.1.12", "marks": 1, "stem": "Suggest which indicator is the most appropriate for the titration in Question 09.2.", "figures": ["fig-q9-fig4.jpg"]},
    {"qnum": "09.4", "specRef": "3.1.12", "marks": 6, "stem": "Calculate the pH of the HX/KX buffer solution after adding 3.00 x 10^-4 mol of KOH."},
    {"qnum": "09.5", "specRef": "3.1.12", "marks": 1, "stem": "Use a mathematical expression to explain why a buffer solution has a constant pH even when diluted."},
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

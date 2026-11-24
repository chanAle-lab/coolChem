"""Ingest AQA A-level Chemistry June 2021 Paper 1 (7405/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521642703_e16ade85.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521642565_1d766dd4.pdf"
)

PAPER_ID = "2021-june-7405-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2021,
    "series": "June",
    "unit": "7405/1",
    "level": "A-level",
    "date": "2021-06-01",
    "title": "7405/1 — A-level Paper 1: Inorganic and Physical Chemistry (June 2021)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-fig1.jpg", "page": 2, "x0": 40, "y0": 260, "x1": 555, "y1": 615},
    {"filename": "fig-q4-fig2.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 275},
    {"filename": "fig-q7-table7.jpg", "page": 24, "x0": 40, "y0": 65, "x1": 555, "y1": 325},
    {"filename": "fig-q8-table8.jpg", "page": 26, "x0": 40, "y0": 205, "x1": 555, "y1": 420},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 4, "01.5": 4, "01.6": 4,
    "02.1": 5, "02.2": 5, "02.3": 5,
    "03.1": 6, "03.2": 6, "03.3": 6, "03.4": 7, "03.5": 7, "03.6": 7,
    "04.1": 8, "04.2": 10, "04.3": 10, "04.4": 11, "04.5": 12, "04.6": 12, "04.7": 13,
    "05.1": 14, "05.2": 14, "05.3": 16, "05.4": 17,
    "06.1": 18, "06.2": 18, "06.3": 19, "06.4": 20, "06.5": 20, "06.6": 21, "06.7": 21, "06.8": 22,
    "07.1": 24, "07.2": 24, "07.3": 25,
    "08.1": 26, "08.2": 26, "08.3": 26, "08.4": 27, "08.5": 27, "08.6": 27,
    "09.1": 28, "09.2": 28, "09.3": 28, "09.4": 29, "09.5": 29, "09.6": 29,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.4", "marks": 1, "stem": "State the meaning of the term enthalpy change."},
    {"qnum": "01.2", "specRef": "3.1.8", "marks": 3, "stem": "Complete Figure 1 by writing the formulas, including state symbols, of the appropriate species on each of the three blank lines of the Born-Haber cycle for CaCl2."},
    {"qnum": "01.3", "specRef": "3.1.8", "marks": 2, "stem": "Use Figure 1 and the data in Table 1 to calculate a value for the enthalpy of lattice dissociation of calcium chloride.", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "01.4", "specRef": "3.1.8", "marks": 1, "stem": "Give an equation, including state symbols, to represent the process that occurs when the enthalpy of solution of magnesium chloride is measured."},
    {"qnum": "01.5", "specRef": "3.1.8", "marks": 2, "stem": "Use your answer to Question 01.4 and the data in Table 2 to calculate a value for the enthalpy of solution of magnesium chloride."},
    {"qnum": "01.6", "specRef": "3.1.8", "marks": 2, "stem": "Suggest why the enthalpy of hydration of Ca2+(g) (-1650 kJ mol-1) is less exothermic than that of Mg2+(g)."},
    {"qnum": "02.1", "specRef": "3.1.1", "marks": 1, "stem": "Define the mass number of an atom."},
    {"qnum": "02.2", "specRef": "3.1.1", "marks": 2, "stem": "Complete Table 3 to show the numbers of neutrons and electrons in 46Ti and 49Ti2+."},
    {"qnum": "02.3", "specRef": "3.1.1", "marks": 3, "stem": "Calculate the percentage abundance of 46Ti in a sample of titanium (Ar = 47.8) where the ratio of 46Ti:47Ti:49Ti is 2:2:1."},
    {"qnum": "03.1", "specRef": "3.2.4", "marks": 2, "stem": "Give an equation, including state symbols, for the reaction of sodium with water and suggest why it is dangerous in a boiling tube with 10 cm3 of water."},
    {"qnum": "03.2", "specRef": "3.2.4", "marks": 2, "stem": "Give an equation for the reaction of phosphorus(V) oxide with water and suggest a pH for the solution formed."},
    {"qnum": "03.3", "specRef": "3.2.4", "marks": 4, "stem": "Explain, in terms of crystal structure and bonding, why silicon(IV) oxide has a higher melting point than phosphorus(V) oxide."},
    {"qnum": "03.4", "specRef": "3.2.4", "marks": 2, "stem": "Give the formula for the amphoteric Period 3 oxide and an equation for its reaction with sulfuric acid."},
    {"qnum": "03.5", "specRef": "3.2.2", "marks": 1, "stem": "Give the formula of a hydroxide of an element in Period 3 used in medicine."},
    {"qnum": "03.6", "specRef": "3.2.1", "marks": 1, "stem": "Identify the element in Period 3, from sodium to chlorine, that has the largest atomic radius."},
    {"qnum": "04.1", "specRef": "3.2.5", "marks": 6, "stem": "Discuss the role of iron as a heterogeneous catalyst in the Haber process, including factors affecting efficiency and lifetime."},
    {"qnum": "04.2", "specRef": "3.2.5", "marks": 4, "stem": "Explain why the reaction between S2O8^2- and I- is slow before adding Fe2+ catalyst and give two equations to show how Fe2+ catalyses it."},
    {"qnum": "04.3", "specRef": "3.2.5", "marks": 1, "stem": "Give a reason why Zn2+ ions do not catalyse the reaction in Question 04.2."},
    {"qnum": "04.4", "specRef": "3.1.2", "marks": 6, "stem": "Calculate the maximum volume, in m3, of hydrogen gas produced when 0.998 g of iron reacts with 30.0 cm3 of 1.00 mol dm-3 HCl at 30 C and 100 kPa."},
    {"qnum": "04.5", "specRef": "3.2.6", "marks": 2, "stem": "Identify precipitate A and state its colour from Figure 2.", "figures": ["fig-q4-fig2.jpg"]},
    {"qnum": "04.6", "specRef": "3.2.6", "marks": 3, "stem": "Give the formula of B, state its colour, and give an ionic equation for [Fe(H2O)6]3+ with aqueous Na2CO3.", "figures": ["fig-q4-fig2.jpg"]},
    {"qnum": "04.7", "specRef": "3.2.6", "marks": 3, "stem": "Explain why an aqueous solution containing [Fe(H2O)6]3+ ions has a lower pH than an aqueous solution containing [Fe(H2O)6]2+ ions."},
    {"qnum": "05.1", "specRef": "3.1.6", "marks": 3, "stem": "State and explain the effect of a decrease in overall pressure on the equilibrium yield of SO3 in 2SO2(g) + O2(g) <-> 2SO3(g)."},
    {"qnum": "05.2", "specRef": "3.1.10", "marks": 4, "stem": "Calculate the partial pressure, in kPa, of SO2 in the equilibrium mixture at 215 kPa containing 0.180 mol SO3."},
    {"qnum": "05.3", "specRef": "3.1.10", "marks": 3, "stem": "Give an expression for Kp and calculate its value and units from the partial pressures in Table 4."},
    {"qnum": "05.4", "specRef": "3.1.10", "marks": 1, "stem": "What is the effect on the value of Kp if the pressure of this equilibrium mixture is increased at a constant temperature?"},
    {"qnum": "06.1", "specRef": "3.1.12", "marks": 1, "stem": "Explain why [H2O] is not shown in the Kw expression."},
    {"qnum": "06.2", "specRef": "3.1.12", "marks": 2, "stem": "Explain why the value of Kw increases as the temperature increases."},
    {"qnum": "06.3", "specRef": "3.1.12", "marks": 4, "stem": "Give the expression for pH, calculate the pH of pure water at 50 C, and explain why water is neutral at 50 C."},
    {"qnum": "06.4", "specRef": "RP", "marks": 1, "stem": "Use the calibration graph in Figure 3 to give the true pH value when the pH meter reading is 5.6."},
    {"qnum": "06.5", "specRef": "RP", "marks": 1, "stem": "Suggest why the pH probe is washed with distilled water between each of the calibration measurements."},
    {"qnum": "06.6", "specRef": "RP", "marks": 1, "stem": "Explain why the volume of sodium hydroxide solution added between each pH measurement is smaller as the end point is approached."},
    {"qnum": "06.7", "specRef": "3.1.12", "marks": 1, "stem": "State why all three of the indicators in Table 6 are suitable for this titration."},
    {"qnum": "06.8", "specRef": "3.1.12", "marks": 5, "stem": "Calculate the pH of the final solution at 25 C when 36.25 cm3 of 0.200 mol dm-3 NaOH is added to 25.00 cm3 of 0.150 mol dm-3 HCl."},
    {"qnum": "07.1", "specRef": "3.1.8", "marks": 1, "stem": "Explain why the standard entropy value for carbon dioxide is greater than that for carbon."},
    {"qnum": "07.2", "specRef": "3.1.8", "marks": 1, "stem": "State the temperature at which the standard entropy of aluminium is 0 J K-1 mol-1."},
    {"qnum": "07.3", "specRef": "3.1.8", "marks": 7, "stem": "Use the equation 2Al2O3(s) + 3C(s) -> 4Al(s) + 3CO2(g) and Table 7 to calculate the minimum temperature, in K, at which this reaction becomes feasible.", "figures": ["fig-q7-table7.jpg"]},
    {"qnum": "08.1", "specRef": "3.1.11", "marks": 1, "stem": "State the meaning of the term electrochemical series."},
    {"qnum": "08.2", "specRef": "3.1.11", "marks": 1, "stem": "State two conditions needed for the standard hydrogen half-cell to have Eo = 0.00 V."},
    {"qnum": "08.3", "specRef": "3.1.11", "marks": 1, "stem": "Identify the weakest reducing agent in Table 8."},
    {"qnum": "08.4", "specRef": "3.1.11", "marks": 2, "stem": "Use half-equations from Table 8 to deduce an equation for the reduction of VO2+ to form VO2+ in aqueous solution by iron.", "figures": ["fig-q8-table8.jpg"]},
    {"qnum": "08.5", "specRef": "3.1.11", "marks": 2, "stem": "Use data from Table 8 to explain why [Co(H2O)6]3+(aq) will undergo a redox reaction with [Fe(H2O)6]2+(aq) and give an equation.", "figures": ["fig-q8-table8.jpg"]},
    {"qnum": "08.6", "specRef": "3.2.5", "marks": 1, "stem": "Suggest why the two cobalt(III) complex ions in Table 8 have different electrode potentials."},
    {"qnum": "09.1", "specRef": "3.1.11", "marks": 2, "stem": "Use data in Table 9 to explain why an aqueous electrolyte is not used for a lithium cell."},
    {"qnum": "09.2", "specRef": "3.1.11", "marks": 1, "stem": "Use the data in Table 9 to calculate the cell EMF of a standard lithium-iodine cell."},
    {"qnum": "09.3", "specRef": "3.1.11", "marks": 1, "stem": "Suggest why the EMF value for a commercial lithium-iodine cell (2.80 V) is different from the value calculated in Question 09.2."},
    {"qnum": "09.4", "specRef": "3.1.7", "marks": 1, "stem": "Deduce the oxidation state of chlorine in LiClO4."},
    {"qnum": "09.5", "specRef": "3.1.11", "marks": 1, "stem": "Give an equation for the reaction that occurs at the positive lithium cobalt oxide electrode."},
    {"qnum": "09.6", "specRef": "3.1.11", "marks": 1, "stem": "Give an equation for the reaction that occurs at the negative lithium electrode."},
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

"""Ingest AQA A-level Chemistry June 2020 Paper 3 (7405/3) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521589214_040cb130.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521589098_f8264bce.pdf"
)

PAPER_ID = "2020-june-7405-3"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2020,
    "series": "June",
    "unit": "7405/3",
    "level": "A-level",
    "date": "2020-06-17",
    "title": "7405/3 — A-level Paper 3: Practical Skills & Synoptic (June 2020)",
    "totalMarks": 90,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q3-method.jpg", "page": 6, "x0": 40, "y0": 290, "x1": 555, "y1": 430},
    {"filename": "fig-q4-2-stem.jpg", "page": 8, "x0": 40, "y0": 190, "x1": 555, "y1": 235},
    {"filename": "fig-q4-table1.jpg", "page": 10, "x0": 40, "y0": 390, "x1": 555, "y1": 655},
    {"filename": "fig-q5-stem.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 280},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 2, "01.4": 3, "01.5": 3,
    "02.1": 4, "02.2": 4, "02.3": 4,
    "03.1": 6, "03.2": 6, "03.3": 7, "03.4": 7,
    "04.1": 8, "04.2": 8, "04.3": 9, "04.4": 10, "04.5": 10, "04.6": 11,
    "05.1": 12, "05.2": 12, "05.3": 13, "05.4": 13,
    "06.1": 14, "06.2": 14, "06.3": 17, "06.4": 17,
    "07": 18,
    "08": 19, "09": 19, "10": 19,
    "11": 20, "12": 20, "13": 20,
    "14": 21, "15": 21, "16": 21,
    "17": 22, "18": 22, "19": 22,
    "20": 23, "21": 23, "22": 23,
    "23": 24, "24": 24, "25": 24,
    "26": 25, "27": 25, "28": 25,
    "29": 26, "30": 26, "31": 26,
    "32": 27, "33": 27, "34": 27,
    "35": 28, "36": 28,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.2", "marks": 2, "stem": "Explain how oxides of nitrogen are formed in petrol and diesel engines."},
    {"qnum": "01.2", "specRef": "3.3.2", "marks": 1, "stem": "State why it is desirable to decrease emissions of oxides of nitrogen from vehicles."},
    {"qnum": "01.3", "specRef": "3.1.7", "marks": 2, "stem": "Give the oxidation state of N in NO2, NH3 and N2, and complete the equation for NO2 + NH3."},
    {"qnum": "01.4", "specRef": "3.2.5", "marks": 2, "stem": "State the meaning of the term heterogeneous catalyst."},
    {"qnum": "01.5", "specRef": "3.3.2", "marks": 1, "stem": "Explain why carbon particulates are formed in diesel and petrol vehicles."},
    {"qnum": "02.1", "specRef": "3.2.4", "marks": 2, "stem": "State why Na2O and MgO form alkaline solutions and why Na2O forms a solution with higher pH."},
    {"qnum": "02.2", "specRef": "3.2.4", "marks": 1, "stem": "Give an equation for the reaction between phosphorus(V) oxide and water."},
    {"qnum": "02.3", "specRef": "3.2.5", "marks": 2, "stem": "Give two equations to show how vanadium(V) oxide acts as a catalyst in the Contact process."},
    {"qnum": "03.1", "specRef": "3.2.5", "marks": 3, "stem": "Explain why complexes formed from transition metal ions are coloured."},
    {"qnum": "03.2", "specRef": "3.2.5", "marks": 3, "stem": "Calculate the energy, in J, gained by each excited electron in the absorption at 490 nm.", "figures": ["fig-q3-method.jpg"]},
    {"qnum": "03.3", "specRef": "RP", "marks": 3, "stem": "Describe how a calibration graph is produced and used to find the concentration of the iron(III) complex.", "figures": ["fig-q3-method.jpg"]},
    {"qnum": "03.4", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the mass, in mg, of iron in the tablet given [Fe3+] = 4.66 x 10^-3 mol dm-3 in 250 cm3.", "figures": ["fig-q3-method.jpg"]},
    {"qnum": "04.1", "specRef": "3.3.13", "marks": 1, "stem": "Name the process that is prevented by cisplatin during cell division."},
    {"qnum": "04.2", "specRef": "3.2.5", "marks": 2, "stem": "Give the equation for replacing one chloride ligand in cisplatin with a water molecule.", "figures": ["fig-q4-2-stem.jpg"]},
    {"qnum": "04.3", "specRef": "3.3.13", "marks": 2, "stem": "Complete Figure 1 to show how the platinum complex forms a cross-link between two guanine nucleotides."},
    {"qnum": "04.4", "specRef": "3.1.9", "marks": 3, "stem": "Explain how graphical methods can be used to confirm that the hydrolysis of cisplatin is first order."},
    {"qnum": "04.5", "specRef": "3.1.9", "marks": 2, "stem": "Complete Table 1 by calculating 1/T and ln k at 318 K.", "figures": ["fig-q4-table1.jpg"]},
    {"qnum": "04.6", "specRef": "3.1.9", "marks": 5, "stem": "Plot ln k against 1/T on Figure 2 and calculate the activation energy Ea in kJ mol-1.", "figures": ["fig-q4-table1.jpg"]},
    {"qnum": "05.1", "specRef": "3.1.4", "marks": 3, "stem": "Calculate the heat capacity Ccal of the bomb calorimeter using hexane combustion data.", "figures": ["fig-q5-stem.jpg"]},
    {"qnum": "05.2", "specRef": "3.1.4", "marks": 2, "stem": "Calculate the heat change, in kJ mol-1, for octane combusted in the bomb calorimeter."},
    {"qnum": "05.3", "specRef": "3.1.4", "marks": 1, "stem": "State why the heat change calculated from the bomb calorimeter experiment is not an enthalpy change."},
    {"qnum": "05.4", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the percentage uncertainty in temperature change (12.2 C, +/- 0.1 C) and suggest a change to reduce it."},
    {"qnum": "06.1", "specRef": "3.1.11", "marks": 3, "stem": "State the substances and conditions needed in a standard hydrogen electrode."},
    {"qnum": "06.2", "specRef": "RP", "marks": 6, "stem": "Describe an experiment using Cu2+/Cu as a secondary standard to show E0(TiO2+/Ti) = -0.88 V."},
    {"qnum": "06.3", "specRef": "3.1.7", "marks": 1, "stem": "Give the half-equation for the TiO2+(aq)/Ti(s) electrode in acidic conditions."},
    {"qnum": "06.4", "specRef": "3.1.11", "marks": 3, "stem": "Use Table 2 to explain why copper reacts with nitric acid but not most acids, and give an equation."},
    {"qnum": "07", "specRef": "3.1.2", "marks": 1, "stem": "What is the amount, in moles, of KClO3 that decomposed to form 67.2 cm3 O2 at 298 K and 110 kPa?"},
    {"qnum": "08", "specRef": "3.1.3", "marks": 1, "stem": "Which has a bond angle of 109.5 degrees?"},
    {"qnum": "09", "specRef": "3.1.8", "marks": 1, "stem": "Which reaction has an enthalpy change equal to the standard enthalpy of formation of silver iodide?"},
    {"qnum": "10", "specRef": "3.1.4", "marks": 1, "stem": "Which is the enthalpy change for CH4 + 2O2 -> CO2 + 2H2O from the bond enthalpies?"},
    {"qnum": "11", "specRef": "3.1.7", "marks": 1, "stem": "In which conversion is the metal reduced?"},
    {"qnum": "12", "specRef": "3.1.9", "marks": 1, "stem": "Which statement about rate = k[X]^2[Y] is correct?"},
    {"qnum": "13", "specRef": "3.1.12", "marks": 1, "stem": "Which statement about pH is correct?"},
    {"qnum": "14", "specRef": "3.1.12", "marks": 1, "stem": "Which acid-base pair has the highest pH at the equivalence point?"},
    {"qnum": "15", "specRef": "3.2.3", "marks": 1, "stem": "Why is dilute nitric acid added before silver nitrate solution in the halide test?"},
    {"qnum": "16", "specRef": "3.2.3", "marks": 1, "stem": "Which shows the major product(s) formed when chlorine reacts with cold, dilute, aqueous NaOH?"},
    {"qnum": "17", "specRef": "3.2.5", "marks": 1, "stem": "Which shows the electron configuration of an atom of a transition metal?"},
    {"qnum": "18", "specRef": "3.2.5", "marks": 1, "stem": "Which will not act as a ligand in the formation of a complex ion?"},
    {"qnum": "19", "specRef": "3.2.5", "marks": 1, "stem": "Which shows the correct oxidation state and co-ordination number of cobalt in [Co(NH3)5Cl]Cl2?"},
    {"qnum": "20", "specRef": "3.2.5", "marks": 1, "stem": "Which statement about shapes of complexes/ions is not correct?"},
    {"qnum": "21", "specRef": "3.2.5", "marks": 1, "stem": "Which compound decolourises acidified potassium manganate(VII) solution?"},
    {"qnum": "22", "specRef": "3.3.1", "marks": 1, "stem": "Which has E-Z isomers?"},
    {"qnum": "23", "specRef": "3.3.3", "marks": 1, "stem": "Which is the mechanism for converting methylbenzene to (chloromethyl)benzene?"},
    {"qnum": "24", "specRef": "3.3.4", "marks": 1, "stem": "Which compound decolourises bromine water in the absence of sunlight?"},
    {"qnum": "25", "specRef": "3.3.5", "marks": 1, "stem": "Which compound reacts to form a ketone when warmed with acidified potassium dichromate(VI)?"},
    {"qnum": "26", "specRef": "3.3.7", "marks": 1, "stem": "Which does not contain an asymmetric carbon atom?"},
    {"qnum": "27", "specRef": "3.3.9", "marks": 1, "stem": "Which reaction involves addition-elimination?"},
    {"qnum": "28", "specRef": "3.3.4", "marks": 1, "stem": "Which compound reacts with HBr to give 2-bromo-3-methylbutane as the major product?"},
    {"qnum": "29", "specRef": "3.3.12", "marks": 1, "stem": "Which forms a polymer with ClOC(CH2)8COCl?"},
    {"qnum": "30", "specRef": "3.3.13", "marks": 1, "stem": "Which structure shows the zwitterion of an amino acid?"},
    {"qnum": "31", "specRef": "3.2.5", "marks": 1, "stem": "What is the minimum volume of 0.02 mol dm-3 KMnO4 needed to oxidise 0.01 mol VO2+?"},
    {"qnum": "32", "specRef": "3.1.12", "marks": 1, "stem": "Which is the concentration of NaOH(aq) that has pH = 14.30?"},
    {"qnum": "33", "specRef": "3.1.9", "marks": 1, "stem": "What are the units of the rate constant for a third order reaction?"},
    {"qnum": "34", "specRef": "3.1.12", "marks": 1, "stem": "What is the pH of 0.015 mol dm-3 sulfuric acid?"},
    {"qnum": "35", "specRef": "3.3.9", "marks": 1, "stem": "Which compound is formed when phenyl benzenecarboxylate is hydrolysed under acidic conditions?"},
    {"qnum": "36", "specRef": "RP", "marks": 1, "stem": "Which rinsing error explains a larger than expected titre volume?"},
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

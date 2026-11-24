"""Ingest AQA AS Chemistry June 2019 Paper 1 (7404/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521528956_a147581f.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521528901_e517ebdc.pdf"
)

PAPER_ID = "2019-june-7404-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2019,
    "series": "June",
    "unit": "7404/1",
    "level": "AS",
    "date": "2019-05-20",
    "title": "7404/1 — AS Paper 1: Inorganic and Physical Chemistry (June 2019)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q2-stem.jpg", "page": 6, "x0": 40, "y0": 65, "x1": 555, "y1": 205},
    {"filename": "fig-q5-eq.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 125},
]

PAGE_MAP = {
    "01.1": 3, "01.2": 3, "01.3": 4, "01.4": 4, "01.5": 5,
    "02.1": 6, "02.2": 6, "02.3": 6, "02.4": 7,
    "03.1": 8, "03.2": 8, "03.3": 8, "03.4": 9, "03.5": 9, "03.6": 9, "03.7": 9,
    "04": 10,
    "05.1": 12, "05.2": 12, "05.3": 13,
    "06.1": 14, "06.2": 15, "06.3": 15, "06.4": 15,
    "07.1": 16, "07.2": 16,
    "08.1": 17, "08.2": 17,
    "09": 18, "10": 18,
    "11": 19, "12": 19, "13": 19,
    "14": 20, "15": 20, "16": 20,
    "17": 21, "18": 21, "19": 21,
    "20": 22, "21": 22,
    "22": 23, "23": 23,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.1", "marks": 2, "stem": "Explain why a fluoride ion is larger than a sodium ion."},
    {"qnum": "01.2", "specRef": "3.1.3", "marks": 2, "stem": "Explain, in terms of structure and bonding, why the melting point of sodium fluoride is high."},
    {"qnum": "01.3", "specRef": "3.1.3", "marks": 2, "stem": "Name the type of bond formed when HF reacts with H+ and explain how this bond is formed."},
    {"qnum": "01.4", "specRef": "3.1.3", "marks": 4, "stem": "Draw and name the shapes of the SbF6- and H2F+ ions, including any lone pairs."},
    {"qnum": "01.5", "specRef": "3.1.4", "marks": 3, "stem": "Use the data in Table 1 to calculate a value for the bond enthalpy of a C-F bond."},
    {"qnum": "02.1", "specRef": "3.1.1", "marks": 3, "stem": "Describe how the molecules are ionised using electrospray ionisation."},
    {"qnum": "02.2", "specRef": "3.1.1", "marks": 1, "stem": "Give the formula of the ion that reaches the detector first in the TOF mass spectrometer.", "figures": ["fig-q2-stem.jpg"]},
    {"qnum": "02.3", "specRef": "3.1.1", "marks": 1, "stem": "Give an equation, including state symbols, for the electron impact ionisation of a germanium atom."},
    {"qnum": "02.4", "specRef": "3.1.1", "marks": 5, "stem": "Calculate the mass, in g, of one mole of germanium ions from TOF data and state the mass number."},
    {"qnum": "03.1", "specRef": "3.1.1", "marks": 1, "stem": "Complete the full electron configuration of a chromium atom."},
    {"qnum": "03.2", "specRef": "3.1.1", "marks": 1, "stem": "Deduce the symbol, including mass number and atomic number, for an atom with 2 more protons and 3 more neutrons than 52Cr."},
    {"qnum": "03.3", "specRef": "3.1.1", "marks": 3, "stem": "Determine the percentage abundance of the fourth isotope of chromium and show its mass number is 50."},
    {"qnum": "03.4", "specRef": "3.1.7", "marks": 1, "stem": "Deduce the oxidation state of chromium in the Cr2O7^2- ion."},
    {"qnum": "03.5", "specRef": "3.1.7", "marks": 1, "stem": "Deduce a half-equation to show the oxidation of iodide ions to iodine."},
    {"qnum": "03.6", "specRef": "3.1.7", "marks": 1, "stem": "Deduce a half-equation for the conversion in acidic solution of Cr2O7^2- ions to Cr3+ ions."},
    {"qnum": "03.7", "specRef": "3.1.7", "marks": 1, "stem": "Deduce the overall redox equation for the reaction between iodide ions and acidified Cr2O7^2- ions."},
    {"qnum": "04", "specRef": "3.1.1", "marks": 6, "stem": "Explain the pattern in the first ionisation energies of the elements from lithium to neon."},
    {"qnum": "05.1", "specRef": "3.1.6", "marks": 2, "stem": "1.50 mol NO and 1.00 mol Cl2 reach equilibrium forming 0.350 mol NOCl. Calculate equilibrium moles of NO and Cl2."},
    {"qnum": "05.2", "specRef": "3.1.6", "marks": 1, "stem": "Give the expression for Kc for the reaction 2NO(g) + Cl2(g) <=> 2NOCl(g).", "figures": ["fig-q5-eq.jpg"]},
    {"qnum": "05.3", "specRef": "3.1.6", "marks": 4, "stem": "Determine the amount, in moles, of NOCl in an 800 cm3 equilibrium mixture given Kc = 1.32 x 10^-2.", "figures": ["fig-q5-eq.jpg"]},
    {"qnum": "06.1", "specRef": "3.1.2", "marks": 5, "stem": "Use the titration results in Table 3 to calculate the Mr of the unknown diprotic acid H2A."},
    {"qnum": "06.2", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the percentage uncertainty in using the 25.0 cm3 pipette (+/- 0.06 cm3)."},
    {"qnum": "06.3", "specRef": "RP", "marks": 1, "stem": "Explain why an air bubble below the burette tap increases the final burette reading."},
    {"qnum": "06.4", "specRef": "RP", "marks": 1, "stem": "Suggest why washing the inside of the conical flask with distilled water does not give an incorrect result."},
    {"qnum": "07.1", "specRef": "3.2.2", "marks": 2, "stem": "Give an equation for the reaction between titanium(IV) chloride and magnesium and state the role of magnesium."},
    {"qnum": "07.2", "specRef": "3.1.2", "marks": 4, "stem": "A 3200 mg mixture of MgO and Mg(OH)2 reacts with CO2 forming 210 mg H2O. Calculate % by mass of MgO."},
    {"qnum": "08.1", "specRef": "3.2.2", "marks": 3, "stem": "Give a reagent and observations to distinguish between NaCl(aq) and BaCl2(aq)."},
    {"qnum": "08.2", "specRef": "3.2.3", "marks": 3, "stem": "Give a reagent and observations to distinguish between NaCl(aq) and Na2CO3(aq)."},
    {"qnum": "09", "specRef": "3.1.2", "marks": 1, "stem": "Which sample, measured at room temperature and pressure, contains the greatest number of the stated particles?"},
    {"qnum": "10", "specRef": "3.1.2", "marks": 1, "stem": "5.0 g of an oxide of molybdenum contain 4.0 g of molybdenum. What is the empirical formula?"},
    {"qnum": "11", "specRef": "3.1.3", "marks": 1, "stem": "Which substance has delocalised electrons?"},
    {"qnum": "12", "specRef": "3.1.3", "marks": 1, "stem": "Which species is not pyramidal in shape?"},
    {"qnum": "13", "specRef": "3.1.3", "marks": 1, "stem": "Which change occurs when water is vaporised?"},
    {"qnum": "14", "specRef": "3.1.4", "marks": 1, "stem": "Which equation represents the standard enthalpy of formation for barium chloride?"},
    {"qnum": "15", "specRef": "3.1.7", "marks": 1, "stem": "Which equation does not represent a redox reaction?"},
    {"qnum": "16", "specRef": "3.2.2", "marks": 1, "stem": "Which property would you expect the element radium, Ra, to possess?"},
    {"qnum": "17", "specRef": "3.2.2", "marks": 1, "stem": "Which statement about strontium and calcium is not correct?"},
    {"qnum": "18", "specRef": "3.2.2", "marks": 1, "stem": "Which property of Group 2 elements, Ca to Ba, increases with increasing atomic number?"},
    {"qnum": "19", "specRef": "3.2.3", "marks": 1, "stem": "What is the best oxidising agent?"},
    {"qnum": "20", "specRef": "3.1.4", "marks": 1, "stem": "What is the amount of heat energy absorbed by m g of water heated by y C?"},
    {"qnum": "21", "specRef": "3.1.2", "marks": 1, "stem": "20 cm3 of butane are burned in 0.20 dm3 of oxygen. Which statement is correct?"},
    {"qnum": "22", "specRef": "3.2.3", "marks": 1, "stem": "Which statement is correct about reactions involving halide ions?"},
    {"qnum": "23", "specRef": "3.1.2", "marks": 1, "stem": "What is the percentage yield when 20 g of aluminium are produced from 50 g of aluminium oxide?"},
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

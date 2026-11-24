"""Ingest AQA A-level Chemistry June 2023 Paper 1 (7405/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530731983_ad579dfc.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530732010_dc47edfd.pdf"
)

PAPER_ID = "2023-june-7405-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2023,
    "series": "June",
    "unit": "7405/1",
    "level": "A-level",
    "date": "2023-06-12",
    "title": "7405/1 — A-level Paper 1: Inorganic and Physical Chemistry (June 2023)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q2-fig1.jpg", "page": 4, "x0": 40, "y0": 135, "x1": 555, "y1": 445},
    {"filename": "fig-q5-fig2.jpg", "page": 11, "x0": 40, "y0": 95, "x1": 555, "y1": 380},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 2, "01.4": 3, "01.5": 3, "01.6": 3, "01.7": 3,
    "02.1": 4, "02.2": 4, "02.3": 5, "02.4": 5,
    "03.1": 6, "03.2": 6, "03.3": 6, "03.4": 6, "03.5": 6,
    "04.1": 7, "04.2": 7, "04.3": 8, "04.4": 9, "04.5": 9,
    "05.1": 10, "05.2": 10, "05.3": 10, "05.4": 11, "05.5": 11, "05.6": 12, "05.7": 12,
    "06.1": 14, "06.2": 14, "06.3": 14, "06.4": 15, "06.5": 15, "06.6": 15,
    "07.1": 16, "07.2": 16, "07.3": 16, "07.4": 16, "07.5": 17, "07.6": 17, "07.7": 17, "07.8": 18,
    "08.1": 21, "08.2": 21, "08.3": 21, "08.4": 21, "08.5": 21,
    "09.1": 22, "09.2": 22, "09.3": 23, "09.4": 23, "09.5": 23,
    "10.1": 24, "10.2": 24, "10.3": 24, "10.4": 25, "10.5": 25,
}

MS_QNUM_MAP = {}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.2.5", "marks": 1, "stem": "State the meaning of the term transition metal complex."},
    {"qnum": "01.2", "specRef": "3.1.3", "marks": 2, "stem": "Draw and name the shape of a PF3 molecule, including lone pairs."},
    {"qnum": "01.3", "specRef": "3.1.7", "marks": 1, "stem": "Suggest why the oxidation state of chromium is zero in Cr(PF3)6."},
    {"qnum": "01.4", "specRef": "3.1.7", "marks": 1, "stem": "Deduce the oxidation state of chromium in [Cr(NH3)4Cl2]Cl."},
    {"qnum": "01.5", "specRef": "3.1.3", "marks": 1, "stem": "Name the type of bond between N and H in ammonia."},
    {"qnum": "01.6", "specRef": "3.2.5", "marks": 3, "stem": "Draw the two isomers of [Cr(NH3)4Cl2]+ and state the type of isomerism shown."},
    {"qnum": "01.7", "specRef": "3.2.5", "marks": 1, "stem": "Complete the equation CrCl3 + 5H2O -> ... for a Cr(III) complex."},
    {"qnum": "02.1", "specRef": "3.1.11", "marks": 2, "stem": "State the purpose of the salt bridge and identify a suitable ionic compound.", "figures": ["fig-q2-fig1.jpg"]},
    {"qnum": "02.2", "specRef": "3.1.11", "marks": 1, "stem": "State how the EMF changes if the surface area of the platinum electrode is increased.", "figures": ["fig-q2-fig1.jpg"]},
    {"qnum": "02.3", "specRef": "3.1.11", "marks": 1, "stem": "Determine the effect on the magnitude of the EMF when water is added to the MgCl2 half-cell."},
    {"qnum": "02.4", "specRef": "3.1.11", "marks": 1, "stem": "Give an equation for the overall reaction when the cell is operating.", "figures": ["fig-q2-fig1.jpg"]},
    {"qnum": "03.1", "specRef": "3.2.4", "marks": 1, "stem": "Give an equation for the reaction between phosphorus and an excess of oxygen."},
    {"qnum": "03.2", "specRef": "3.2.4", "marks": 1, "stem": "Give an equation for the reaction between sulfur dioxide and water."},
    {"qnum": "03.3", "specRef": "3.2.4", "marks": 1, "stem": "Give the displayed formula for the anion formed when sulfur trioxide reacts with water."},
    {"qnum": "03.4", "specRef": "3.2.4", "marks": 2, "stem": "Give an equation and one observation for the reaction of magnesium with steam."},
    {"qnum": "03.5", "specRef": "3.2.4", "marks": 1, "stem": "Give an equation for the reaction of excess magnesium oxide with phosphoric acid."},
    {"qnum": "04.1", "specRef": "3.1.10", "marks": 3, "stem": "Calculate the mole fraction of NO2, NO, and O2 at equilibrium."},
    {"qnum": "04.2", "specRef": "3.1.10", "marks": 1, "stem": "Calculate the partial pressure of NO2 at equilibrium when total pressure is 120 kPa."},
    {"qnum": "04.3", "specRef": "3.1.10", "marks": 3, "stem": "Give an expression for Kp and calculate the total pressure in the flask."},
    {"qnum": "04.4", "specRef": "3.1.10", "marks": 2, "stem": "Deduce the effect of compressing the equilibrium mixture on yield of oxygen and Kp."},
    {"qnum": "04.5", "specRef": "3.1.10", "marks": 2, "stem": "Explain why the equilibrium yield of oxygen decreases at a lower temperature."},
    {"qnum": "05.1", "specRef": "3.1.8", "marks": 2, "stem": "Calculate the molar enthalpy change when calcium chloride dissolves in water."},
    {"qnum": "05.2", "specRef": "3.1.8", "marks": 1, "stem": "Deduce how the temperature changes when calcium chloride dissolves in water."},
    {"qnum": "05.3", "specRef": "3.1.8", "marks": 2, "stem": "Explain why the enthalpy of hydration of F- is more negative than Cl-."},
    {"qnum": "05.4", "specRef": "3.1.8", "marks": 2, "stem": "Complete the Born-Haber cycle for calcium chloride."},
    {"qnum": "05.5", "specRef": "3.1.8", "marks": 2, "stem": "Calculate the second ionisation energy of calcium using the Born-Haber cycle.", "figures": ["fig-q5-fig2.jpg"]},
    {"qnum": "05.6", "specRef": "3.1.1", "marks": 1, "stem": "Explain why the second ionisation energy of calcium is greater than the first."},
    {"qnum": "05.7", "specRef": "3.1.8", "marks": 6, "stem": "Discuss the perfect ionic model vs Born-Haber cycle lattice enthalpies for CaCl2, KCl, and AgCl."},
    {"qnum": "06.1", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the mass of solid barium hydroxide needed to prepare 250 cm3 of 0.100 mol dm-3 solution."},
    {"qnum": "06.2", "specRef": "RP", "marks": 3, "stem": "Describe how the dissolved barium hydroxide solution is made up to 250 cm3 in a volumetric flask."},
    {"qnum": "06.3", "specRef": "RP", "marks": 1, "stem": "State why it is good practice to rinse the pipette with the barium hydroxide solution."},
    {"qnum": "06.4", "specRef": "RP", "marks": 1, "stem": "State why it is good practice to remove the funnel from the burette before the titration."},
    {"qnum": "06.5", "specRef": "3.1.2", "marks": 3, "stem": "Calculate the concentration of hydrochloric acid from the barium hydroxide titration."},
    {"qnum": "06.6", "specRef": "RP", "marks": 1, "stem": "Calculate the total percentage error in using the pipette and burette."},
    {"qnum": "07.1", "specRef": "3.1.1", "marks": 1, "stem": "Give the electron configuration of the Al3+ ion."},
    {"qnum": "07.2", "specRef": "3.2.6", "marks": 1, "stem": "Give the equation for anhydrous aluminium sulfate reacting with water to form [Al(H2O)6]3+."},
    {"qnum": "07.3", "specRef": "3.2.6", "marks": 2, "stem": "Explain why the solution containing [Al(H2O)6]3+ is acidic."},
    {"qnum": "07.4", "specRef": "3.2.5", "marks": 1, "stem": "State why the concentration of aluminium sulfate solution cannot be determined by colorimetry."},
    {"qnum": "07.5", "specRef": "3.2.6", "marks": 2, "stem": "Give an ionic equation and one observation when excess aqueous ammonia is added to [Al(H2O)6]3+."},
    {"qnum": "07.6", "specRef": "3.2.6", "marks": 1, "stem": "Identify the aluminium species produced when excess dilute sulfuric acid is added."},
    {"qnum": "07.7", "specRef": "3.2.5", "marks": 2, "stem": "Circle the atoms of two different elements in EDTA4- that form co-ordinate bonds with Al3+."},
    {"qnum": "07.8", "specRef": "3.1.2", "marks": 7, "stem": "Calculate the Mr of Al2(SO4)3.xH2O and the integer value of x from back-titration data."},
    {"qnum": "08.1", "specRef": "3.1.11", "marks": 1, "stem": "Give a half-equation for oxygen reacting with hydrogen ions at the positive electrode."},
    {"qnum": "08.2", "specRef": "3.1.11", "marks": 1, "stem": "Give a half-equation for methanol reacting with water at the negative electrode."},
    {"qnum": "08.3", "specRef": "3.1.11", "marks": 1, "stem": "Calculate the standard electrode potential for the O2 / H2O electrode."},
    {"qnum": "08.4", "specRef": "3.1.11", "marks": 1, "stem": "State why a fuel cell does not need to be electrically recharged."},
    {"qnum": "08.5", "specRef": "3.1.11", "marks": 1, "stem": "Suggest one advantage of using methanol rather than hydrogen in a fuel cell for cars."},
    {"qnum": "09.1", "specRef": "3.1.1", "marks": 1, "stem": "Give the equation, including state symbols, for the formation of Sr+ ions by electron impact."},
    {"qnum": "09.2", "specRef": "3.1.1", "marks": 5, "stem": "Deduce the mass number of the Sr+ ion from TOF mass spectrometry data."},
    {"qnum": "09.3", "specRef": "3.1.1", "marks": 2, "stem": "Explain how ions are detected in a TOF mass spectrometer and how relative abundance is determined."},
    {"qnum": "09.4", "specRef": "3.1.1", "marks": 3, "stem": "Calculate the percentage abundance of 87Sr and the relative atomic mass (Ar) of the sample."},
    {"qnum": "09.5", "specRef": "3.1.1", "marks": 1, "stem": "Suggest why electrospray ionisation is used instead of electron impact for a protein."},
    {"qnum": "10.1", "specRef": "3.1.12", "marks": 1, "stem": "Identify the most suitable indicator for a titration between propanoic acid and sodium hydroxide."},
    {"qnum": "10.2", "specRef": "3.1.12", "marks": 1, "stem": "Give the expression for Ka for propanoic acid."},
    {"qnum": "10.3", "specRef": "3.1.12", "marks": 4, "stem": "Calculate the pH of a 0.100 mol dm-3 propanoic acid solution (pKa = 4.87)."},
    {"qnum": "10.4", "specRef": "3.1.12", "marks": 5, "stem": "Calculate the pH of the buffer formed when NaOH is added to butanoic acid."},
    {"qnum": "10.5", "specRef": "3.1.12", "marks": 2, "stem": "Explain why a titration between butanoic acid and ethylamine cannot be done using an indicator."},
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

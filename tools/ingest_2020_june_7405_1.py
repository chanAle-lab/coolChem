"""Ingest AQA A-level Chemistry June 2020 Paper 1 (7405/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521589159_9b4ce3ab.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521589064_12c219bd.pdf"
)

PAPER_ID = "2020-june-7405-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2020,
    "series": "June",
    "unit": "7405/1",
    "level": "A-level",
    "date": "2020-06-02",
    "title": "7405/1 — A-level Paper 1: Inorganic and Physical Chemistry (June 2020)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-1-cont.jpg", "page": 3, "x0": 40, "y0": 65, "x1": 555, "y1": 150},
    {"filename": "fig-q1-table2.jpg", "page": 4, "x0": 40, "y0": 65, "x1": 555, "y1": 175},
    {"filename": "fig-q3-fig2.jpg", "page": 10, "x0": 40, "y0": 65, "x1": 555, "y1": 295},
    {"filename": "fig-q4-stem.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 155},
    {"filename": "fig-q5-scheme.jpg", "page": 14, "x0": 40, "y0": 65, "x1": 555, "y1": 255},
    {"filename": "fig-q6-fig3.jpg", "page": 16, "x0": 40, "y0": 65, "x1": 555, "y1": 390},
    {"filename": "fig-q8-method.jpg", "page": 20, "x0": 40, "y0": 65, "x1": 555, "y1": 375},
    {"filename": "fig-q10-table5.jpg", "page": 23, "x0": 40, "y0": 65, "x1": 555, "y1": 245},
    {"filename": "fig-q10-fig4.jpg", "page": 24, "x0": 40, "y0": 65, "x1": 555, "y1": 565},
    {"filename": "fig-q11-stem.jpg", "page": 26, "x0": 40, "y0": 65, "x1": 555, "y1": 180},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3, "01.3": 4, "01.4": 4, "01.5": 5,
    "02.1": 6, "02.2": 6, "02.3": 7, "02.4": 7, "02.5": 8,
    "03.1": 10, "03.2": 10, "03.3": 10, "03.4": 11, "03.5": 11,
    "04.1": 12, "04.2": 12, "04.3": 12, "04.4": 13,
    "05.1": 14, "05.2": 14, "05.3": 15, "05.4": 15,
    "06.1": 16, "06.2": 16, "06.3": 17, "06.4": 17, "06.5": 17,
    "07": 18,
    "08.1": 20, "08.2": 21,
    "09.1": 22, "09.2": 22, "09.3": 22, "09.4": 22,
    "10.1": 23, "10.2": 25, "10.3": 25,
    "11.1": 26, "11.2": 26, "11.3": 26, "11.4": 26, "11.5": 26,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.8", "marks": 3, "stem": "Use the Born-Haber cycle and Table 1 to calculate the electron affinity of chlorine.", "figures": ["fig-q1-1-cont.jpg"]},
    {"qnum": "01.2", "specRef": "3.1.8", "marks": 1, "stem": "Match MgCl2, MgO and BaCl2 to their enthalpies of lattice formation."},
    {"qnum": "01.3", "specRef": "3.1.8", "marks": 1, "stem": "State why there is a difference between the theoretical and experimental lattice enthalpies of AgCl.", "figures": ["fig-q1-table2.jpg"]},
    {"qnum": "01.4", "specRef": "3.1.8", "marks": 2, "stem": "Explain why the enthalpy of hydration becomes less exothermic from Li+ to K+."},
    {"qnum": "01.5", "specRef": "3.1.8", "marks": 3, "stem": "Calculate the enthalpy of hydration of bromide ions using Table 4."},
    {"qnum": "02.1", "specRef": "3.1.1", "marks": 2, "stem": "Give the meaning of the term relative atomic mass."},
    {"qnum": "02.2", "specRef": "3.1.1", "marks": 4, "stem": "Calculate the percentage abundances of 50Cr and 53Cr in a sample with Ar = 52.1 and 86.1% 52Cr."},
    {"qnum": "02.3", "specRef": "3.1.1", "marks": 2, "stem": "State one similarity and one difference between atoms of 50Cr and 53Cr in terms of fundamental particles."},
    {"qnum": "02.4", "specRef": "3.1.1", "marks": 2, "stem": "Give two reasons why it is necessary to ionise the isotopes of chromium in a TOF mass spectrometer."},
    {"qnum": "02.5", "specRef": "3.1.1", "marks": 5, "stem": "Calculate the time, in s, for a 53Cr+ ion (KE = 1.102 x 10^-13 J) to travel down a 1.25 m flight tube."},
    {"qnum": "03.1", "specRef": "3.1.1", "marks": 1, "stem": "Draw a cross on Figure 2 to show the second ionisation energy of silicon.", "figures": ["fig-q3-fig2.jpg"]},
    {"qnum": "03.2", "specRef": "3.1.1", "marks": 2, "stem": "Identify the Period 3 element with the highest second ionisation energy and give an equation with state symbols."},
    {"qnum": "03.3", "specRef": "3.2.1", "marks": 2, "stem": "Explain why atomic radius decreases across Period 3 from sodium to chlorine."},
    {"qnum": "03.4", "specRef": "3.1.3", "marks": 1, "stem": "Identify the Period 3 element, from sodium to chlorine, that has the highest electronegativity."},
    {"qnum": "03.5", "specRef": "3.2.4", "marks": 1, "stem": "Give an equation for phosphorus burning in air to form phosphorus(V) oxide."},
    {"qnum": "04.1", "specRef": "3.1.12", "marks": 1, "stem": "State the meaning of the term weak acid.", "figures": ["fig-q4-stem.jpg"]},
    {"qnum": "04.2", "specRef": "3.1.12", "marks": 1, "stem": "Give an expression for Ka for propanoic acid.", "figures": ["fig-q4-stem.jpg"]},
    {"qnum": "04.3", "specRef": "3.1.12", "marks": 4, "stem": "Calculate the pH of a diluted propanoic acid solution (25.0 cm3 of 0.500 mol dm-3 diluted to 100.0 cm3).", "figures": ["fig-q4-stem.jpg"]},
    {"qnum": "04.4", "specRef": "3.1.12", "marks": 6, "stem": "Calculate the mass x g of sodium propanoate needed to make 500 cm3 of pH 4.50 buffer with 0.250 mol dm-3 propanoic acid."},
    {"qnum": "05.1", "specRef": "3.2.6", "marks": 3, "stem": "Give the formula of white precipitate B, another observation, and an equation for [Al(H2O)6]3+ + Na2CO3.", "figures": ["fig-q5-scheme.jpg"]},
    {"qnum": "05.2", "specRef": "3.2.6", "marks": 3, "stem": "Give the formula of complex ion C, the condition needed, and an equation for its formation with NaOH.", "figures": ["fig-q5-scheme.jpg"]},
    {"qnum": "05.3", "specRef": "3.2.5", "marks": 1, "stem": "Deduce the formula of complex ion A formed with Na4EDTA.", "figures": ["fig-q5-scheme.jpg"]},
    {"qnum": "05.4", "specRef": "3.2.6", "marks": 3, "stem": "Explain, with the use of an equation, why a solution containing [Al(H2O)6]3+ has a pH < 7."},
    {"qnum": "06.1", "specRef": "3.1.6", "marks": 1, "stem": "Draw a cross on Figure 3 when the methanol synthesis mixture reaches equilibrium.", "figures": ["fig-q6-fig3.jpg"]},
    {"qnum": "06.2", "specRef": "3.1.10", "marks": 4, "stem": "Calculate the partial pressure of hydrogen at equilibrium for CO + 2H2 <=> CH3OH."},
    {"qnum": "06.3", "specRef": "3.1.10", "marks": 2, "stem": "Give an expression for Kp for CO + 2H2 <=> CH3OH and state its units.", "figures": ["fig-q6-fig3.jpg"]},
    {"qnum": "06.4", "specRef": "3.1.10", "marks": 2, "stem": "State the effect of adding more CO at constant temperature on the partial pressure of methanol and Kp."},
    {"qnum": "06.5", "specRef": "3.1.10", "marks": 2, "stem": "State and explain the effect of adding a catalyst on the value of Kp."},
    {"qnum": "07", "specRef": "3.1.3", "marks": 6, "stem": "Explain why the melting point of XeF4 is higher than that of PF3 in terms of shapes and intermolecular forces."},
    {"qnum": "08.1", "specRef": "3.1.2", "marks": 7, "stem": "Calculate the percentage by mass of NaClO in the original bleach solution from the thiosulfate titration.", "figures": ["fig-q8-method.jpg"]},
    {"qnum": "08.2", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the total percentage uncertainty in using the burette (+/- 0.15 cm3 for 33.50 cm3)."},
    {"qnum": "09.1", "specRef": "3.2.3", "marks": 1, "stem": "State what is observed when silver nitrate solution is added to sodium fluoride solution."},
    {"qnum": "09.2", "specRef": "3.2.3", "marks": 3, "stem": "State an observation, equation, and role of chloride ions when solid NaCl reacts with concentrated H2SO4."},
    {"qnum": "09.3", "specRef": "3.2.3", "marks": 3, "stem": "Give an equation for solid NaBr + concentrated H2SO4 and explain using oxidation states why it is a redox reaction."},
    {"qnum": "09.4", "specRef": "3.2.3", "marks": 2, "stem": "State what is observed and give an ionic equation when aqueous chlorine is added to sodium bromide solution."},
    {"qnum": "10.1", "specRef": "3.1.8", "marks": 6, "stem": "Calculate the Gibbs free-energy change (dG) at 890 K for CO2 + 3H2 <=> CH3OH + H2O using Table 5.", "figures": ["fig-q10-table5.jpg"]},
    {"qnum": "10.2", "specRef": "3.1.8", "marks": 4, "stem": "Use the intercept and gradient of Figure 4 to calculate dH and dS for the gas phase reaction.", "figures": ["fig-q10-fig4.jpg"]},
    {"qnum": "10.3", "specRef": "3.1.8", "marks": 1, "stem": "State what Figure 4 shows about the feasibility of the reaction.", "figures": ["fig-q10-fig4.jpg"]},
    {"qnum": "11.1", "specRef": "3.1.11", "marks": 1, "stem": "Deduce the half-equation for the reaction at the negative electrode of the glucose-oxygen fuel cell.", "figures": ["fig-q11-stem.jpg"]},
    {"qnum": "11.2", "specRef": "3.1.11", "marks": 1, "stem": "Deduce the half-equation for the reaction at the positive electrode of the glucose-oxygen fuel cell.", "figures": ["fig-q11-stem.jpg"]},
    {"qnum": "11.3", "specRef": "3.1.11", "marks": 1, "stem": "Give the equation for the overall reaction in the glucose-oxygen fuel cell.", "figures": ["fig-q11-stem.jpg"]},
    {"qnum": "11.4", "specRef": "3.1.11", "marks": 2, "stem": "Give the conventional representation for the glucose-oxygen fuel cell."},
    {"qnum": "11.5", "specRef": "3.1.11", "marks": 1, "stem": "State what must be done to maintain the EMF of this fuel cell when in use."},
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

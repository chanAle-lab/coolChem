"""Ingest AQA A-level Chemistry June 2022 Paper 1 (7405/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530579819_c0aebf68.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530579834_7f3d5f27.pdf"
)

PAPER_ID = "2022-june-7405-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2022,
    "series": "June",
    "unit": "7405/1",
    "level": "A-level",
    "date": "2022-06-01",
    "title": "7405/1 — A-level Paper 1: Inorganic and Physical Chemistry (June 2022)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-table1.jpg", "page": 5, "x0": 40, "y0": 135, "x1": 555, "y1": 235},
    {"filename": "fig-q7-scheme.jpg", "page": 26, "x0": 40, "y0": 65, "x1": 555, "y1": 220},
]

PAGE_MAP = {
    "01.1": 3, "01.2": 3, "01.3": 4, "01.4": 4, "01.5": 5, "01.6": 5,
    "02.1": 6, "02.2": 6, "02.3": 6, "02.4": 7, "02.5": 8,
    "03.1": 10, "03.2": 11, "03.3": 11, "03.4": 11, "03.5": 12,
    "04.1": 14, "04.2": 14, "04.3": 15, "04.4": 15, "04.5": 16,
    "05.1": 17, "05.2": 17, "05.3": 17, "05.4": 18, "05.5": 18, "05.6": 18, "05.7": 20,
    "06.1": 22, "06.2": 22, "06.3": 22, "06.4": 23, "06.5": 23, "06.6": 24, "06.7": 24,
    "07.1": 25, "07.2": 25, "07.3": 25, "07.4": 26, "07.5": 26, "07.6": 26, "07.7": 26,
    "08.1": 27, "08.2": 27, "08.3": 27, "08.4": 28, "08.5": 28,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.6", "marks": 2, "stem": "Give two features of a reaction in dynamic equilibrium."},
    {"qnum": "01.2", "specRef": "3.1.6", "marks": 1, "stem": "Deduce what can be said about the chemical equation when increasing pressure decreases the equilibrium yield of product."},
    {"qnum": "01.3", "specRef": "3.1.10", "marks": 3, "stem": "Calculate the amount and partial pressure of CO at equilibrium in CO(g) + 2H2(g) <-> CH3OH(g) at 250 kPa."},
    {"qnum": "01.4", "specRef": "3.1.10", "marks": 1, "stem": "Give an expression for Kp for CO(g) + 2H2(g) <-> CH3OH(g)."},
    {"qnum": "01.5", "specRef": "3.1.10", "marks": 3, "stem": "Calculate the partial pressure, in kPa, of hydrogen in the equilibrium mixture using Table 1."},
    {"qnum": "01.6", "specRef": "3.1.10", "marks": 2, "stem": "Use Kp from Table 1 to calculate Kp and its units for CH3OH(g) <-> CO(g) + 2H2(g).", "figures": ["fig-q1-table1.jpg"]},
    {"qnum": "02.1", "specRef": "3.1.1", "marks": 2, "stem": "Define the term relative atomic mass."},
    {"qnum": "02.2", "specRef": "3.1.1", "marks": 2, "stem": "Calculate the relative isotopic mass of the other rhenium isotope from Table 2 (Ar = 186.3)."},
    {"qnum": "02.3", "specRef": "3.1.1", "marks": 1, "stem": "State why the isotopes of rhenium have the same chemical properties."},
    {"qnum": "02.4", "specRef": "3.1.1", "marks": 5, "stem": "Calculate the time, in seconds, for a 185Re+ ion (KE = 1.153 x 10^-13 J) to travel through a 1.450 m TOF flight tube."},
    {"qnum": "02.5", "specRef": "3.1.1", "marks": 2, "stem": "State how the relative abundance of 185Re+ is determined in a TOF mass spectrometer."},
    {"qnum": "03.1", "specRef": "3.1.7", "marks": 5, "stem": "Give an ionic equation for MnO4- + acidified H2O2 and calculate the original concentration of H2O2 in the hair bleach solution."},
    {"qnum": "03.2", "specRef": "RP", "marks": 1, "stem": "State why an indicator is not added in this KMnO4 titration."},
    {"qnum": "03.3", "specRef": "3.1.7", "marks": 1, "stem": "Give the oxidation state of oxygen in hydrogen peroxide."},
    {"qnum": "03.4", "specRef": "3.1.2", "marks": 5, "stem": "Give an equation for the decomposition of H2O2 and calculate the moles needed to produce 185 cm3 of O2 at 100 kPa and 298 K."},
    {"qnum": "03.5", "specRef": "3.1.4", "marks": 5, "stem": "Define mean bond enthalpy and use Table 3 to calculate the O-O bond enthalpy in hydrogen peroxide."},
    {"qnum": "04.1", "specRef": "3.1.12", "marks": 3, "stem": "Calculate the pH of a 0.150 mol dm-3 solution of ethanoic acid at 25 C (Ka = 1.74 x 10^-5 mol dm-3)."},
    {"qnum": "04.2", "specRef": "3.1.12", "marks": 3, "stem": "Calculate the pH of a 0.0100 mol dm-3 solution of strontium hydroxide at 10 C (Kw = 2.93 x 10^-15 mol2 dm-6)."},
    {"qnum": "04.3", "specRef": "3.1.12", "marks": 2, "stem": "Deduce and explain the volume of HCl needed to neutralise 25 cm3 of barium hydroxide at 10 C compared to 22.45 cm3 at 50 C."},
    {"qnum": "04.4", "specRef": "3.1.12", "marks": 3, "stem": "State how a buffer solution can be made from KOH and ethanoic acid, give the equation, and state how it resists pH change when acid is added."},
    {"qnum": "04.5", "specRef": "3.1.12", "marks": 5, "stem": "Calculate the pH at 25 C of the buffer made by adding 2.00 g of NaOH to 500 cm3 of 1.00 mol dm-3 ethanoic acid."},
    {"qnum": "05.1", "specRef": "3.2.2", "marks": 1, "stem": "Tick the statement that is not correct about magnesium hydroxide."},
    {"qnum": "05.2", "specRef": "3.2.4", "marks": 1, "stem": "Give an equation for the reaction of aluminium oxide with sulfuric acid."},
    {"qnum": "05.3", "specRef": "3.2.4", "marks": 3, "stem": "Identify a reagent or test to distinguish aqueous SO2 and SO3 and state the observations."},
    {"qnum": "05.4", "specRef": "3.2.4", "marks": 2, "stem": "Give the formula of the species responsible for the peak at m/z = 124 in the mass spectrum of phosphorus."},
    {"qnum": "05.5", "specRef": "3.2.4", "marks": 1, "stem": "Give an equation for the reaction of phosphorus(V) oxide with sodium hydroxide solution."},
    {"qnum": "05.6", "specRef": "3.2.4", "marks": 1, "stem": "Draw the displayed formula of the molecule formed when phosphorus(V) oxide reacts with water."},
    {"qnum": "05.7", "specRef": "3.1.3", "marks": 6, "stem": "Explain why the melting points of sodium chloride, chlorine, and hydrogen chloride in Table 4 are different."},
    {"qnum": "06.1", "specRef": "3.2.3", "marks": 1, "stem": "State why the amount of chlorine added to drinking water must be controlled."},
    {"qnum": "06.2", "specRef": "3.2.3", "marks": 2, "stem": "Give an equation for chlorine reacting with water to form two acids and explain, with reference to electrons, why this is a redox reaction."},
    {"qnum": "06.3", "specRef": "3.2.3", "marks": 2, "stem": "State the observation and give an ionic equation when chlorine gas is bubbled through sodium iodide solution."},
    {"qnum": "06.4", "specRef": "3.2.3", "marks": 3, "stem": "Give equations for the formation of the two gaseous sulfur-containing products from NaI + conc H2SO4 and state the role of H2SO4."},
    {"qnum": "06.5", "specRef": "3.2.3", "marks": 3, "stem": "Deduce the identity of the impure sodium halide and gas formed with acidified AgNO3, and give an ionic equation for the gas."},
    {"qnum": "06.6", "specRef": "3.1.3", "marks": 3, "stem": "Draw the shape of ClF2+ (including lone pairs), explain its shape, and suggest a bond angle."},
    {"qnum": "06.7", "specRef": "3.2.2", "marks": 1, "stem": "Give an equation for the extraction of titanium from titanium(IV) chloride using magnesium."},
    {"qnum": "07.1", "specRef": "3.2.5", "marks": 2, "stem": "Explain why aqueous solutions containing [CuCl4]2- ions are yellow."},
    {"qnum": "07.2", "specRef": "3.2.5", "marks": 2, "stem": "Calculate the frequency, in s-1, of the light absorbed when a d electron transition has energy change 3.98 x 10^-19 J."},
    {"qnum": "07.3", "specRef": "3.2.5", "marks": 3, "stem": "State three ways in which a transition metal complex can be changed to alter its colour."},
    {"qnum": "07.4", "specRef": "3.2.5", "marks": 1, "stem": "Name the shape of the [CuCl4]2- ion.", "figures": ["fig-q7-scheme.jpg"]},
    {"qnum": "07.5", "specRef": "3.2.5", "marks": 1, "stem": "Give an ionic equation for the conversion of [CuCl4]2- to complex ion P.", "figures": ["fig-q7-scheme.jpg"]},
    {"qnum": "07.6", "specRef": "3.2.5", "marks": 2, "stem": "State the colour of the solution containing Q and give an ionic equation for [CuCl4]2- -> Q.", "figures": ["fig-q7-scheme.jpg"]},
    {"qnum": "07.7", "specRef": "3.2.5", "marks": 1, "stem": "Identify complex ion R.", "figures": ["fig-q7-scheme.jpg"]},
    {"qnum": "08.1", "specRef": "3.1.11", "marks": 1, "stem": "Identify the oxidising agent in the Zn / MnO2 non-rechargeable cell."},
    {"qnum": "08.2", "specRef": "3.1.11", "marks": 1, "stem": "Suggest the function of the porous separator in the silver-zinc cell in Figure 1."},
    {"qnum": "08.3", "specRef": "3.1.11", "marks": 1, "stem": "Give an equation for the overall reaction that occurs when the silver-zinc cell is recharging."},
    {"qnum": "08.4", "specRef": "3.1.11", "marks": 2, "stem": "Give the half-equation for the oxygen electrode in an alkaline H2-O2 fuel cell (EMF = +1.23 V) and calculate its Eo."},
    {"qnum": "08.5", "specRef": "3.1.11", "marks": 1, "stem": "Suggest why the EMF values of the acidic and alkaline hydrogen-oxygen fuel cells are the same."},
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

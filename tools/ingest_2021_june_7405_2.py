"""Ingest AQA A-level Chemistry June 2021 Paper 2 (7405/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521642608_2cfeb55b.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521642565_64fefd07.pdf"
)

PAPER_ID = "2021-june-7405-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2021,
    "series": "June",
    "unit": "7405/2",
    "level": "A-level",
    "date": "2021-06-01",
    "title": "7405/2 — A-level Paper 2: Organic and Physical Chemistry (June 2021)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-eq.jpg", "page": 2, "x0": 40, "y0": 100, "x1": 555, "y1": 295},
    {"filename": "fig-q4-fig3.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 600},
    {"filename": "fig-q8-scheme.jpg", "page": 22, "x0": 40, "y0": 65, "x1": 555, "y1": 280},
    {"filename": "fig-q10-fig8.jpg", "page": 28, "x0": 40, "y0": 65, "x1": 555, "y1": 700},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 4,
    "02.1": 5, "02.2": 5, "02.3": 5, "02.4": 6, "02.5": 7, "02.6": 8,
    "03.1": 10, "03.2": 10, "03.3": 11, "03.4": 11,
    "04.1": 13, "04.2": 13, "04.3": 14,
    "05.1": 15, "05.2": 15, "05.3": 16,
    "06.1": 17, "06.2": 17, "06.3": 17, "06.4": 18,
    "07.1": 19, "07.2": 20, "07.3": 21,
    "08.1": 22, "08.2": 22, "08.3": 23, "08.4": 23,
    "09.1": 24, "09.2": 24, "09.3": 24, "09.4": 24,
    "10.1": 25, "10.2": 25, "10.3": 26, "10.4": 27, "10.5": 29,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.9", "marks": 3, "stem": "Complete the equation for coconut oil triester + KOH, name the type of compound RCOOK, and give one use.", "figures": ["fig-q1-eq.jpg"]},
    {"qnum": "01.2", "specRef": "3.3.9", "marks": 3, "stem": "Deduce the value of n in CH3(CH2)n for the triester (Mr = 638.0).", "figures": ["fig-q1-eq.jpg"]},
    {"qnum": "01.3", "specRef": "3.1.2", "marks": 6, "stem": "Calculate the percentage by mass of the triester (Mr = 638.0) in the 1.450 g coconut oil sample using the back-titration data."},
    {"qnum": "01.4", "specRef": "RP", "marks": 3, "stem": "Suggest why aqueous ethanol is a suitable solvent when heating coconut oil with KOH, and give and justify a safety precaution."},
    {"qnum": "02.1", "specRef": "3.3.2", "marks": 1, "stem": "State the meaning of fraction, as used in the term petrol fraction."},
    {"qnum": "02.2", "specRef": "3.3.2", "marks": 3, "stem": "Complete the equation for cracking hexadecane (C16H34) to form hexane and cyclopentane only, and name a catalyst."},
    {"qnum": "02.3", "specRef": "3.3.16", "marks": 1, "stem": "Give a reason why carbon dioxide absorbs infrared radiation."},
    {"qnum": "02.4", "specRef": "3.3.11", "marks": 4, "stem": "Draw two curly arrows to complete Figure 1, name compound Z (HOCH2CH2NH2), and deduce the role of Z in step 2."},
    {"qnum": "02.5", "specRef": "3.1.3", "marks": 4, "stem": "Draw the shape of XNH2 and [XNH3]+, and state and explain how the H-N-H bond angle in XNH2 compares to [XNH3]+."},
    {"qnum": "02.6", "specRef": "3.3.5", "marks": 6, "stem": "Evaluate the statement that bioethanol being carbon-neutral outweighs the environmental disadvantages of producing bioethanol."},
    {"qnum": "03.1", "specRef": "RP", "marks": 2, "stem": "Design a table to record all the readings necessary to determine an experimental enthalpy of combustion for heptane."},
    {"qnum": "03.2", "specRef": "RP", "marks": 2, "stem": "Suggest two disadvantages of using a glass beaker on a tripod and gauze instead of a clamped copper calorimeter."},
    {"qnum": "03.3", "specRef": "3.1.4", "marks": 2, "stem": "Suggest two reasons why the experimental enthalpy of combustion is less exothermic than a data book value."},
    {"qnum": "03.4", "specRef": "RP", "marks": 1, "stem": "Suggest one addition to the apparatus in Figure 2 that would improve the accuracy of the enthalpy value obtained."},
    {"qnum": "04.1", "specRef": "3.3.10", "marks": 3, "stem": "Use Figure 3 and the data shown in Table 1 to calculate dH2.", "figures": ["fig-q4-fig3.jpg"]},
    {"qnum": "04.2", "specRef": "3.3.10", "marks": 1, "stem": "Explain, in terms of structure and bonding, why benzene is more thermodynamically stable than the Kekule structure."},
    {"qnum": "04.3", "specRef": "3.3.10", "marks": 5, "stem": "Name the mechanism for the nitration of benzene and complete Figure 4 by adding lone pairs and curly arrows."},
    {"qnum": "05.1", "specRef": "3.1.6", "marks": 3, "stem": "Complete Table 2 by deducing the equilibrium amounts, in terms of x, of diester, water, and diol."},
    {"qnum": "05.2", "specRef": "3.3.9", "marks": 1, "stem": "Deduce the structure of the diester C7H12O4 in Question 05.1."},
    {"qnum": "05.3", "specRef": "3.1.6", "marks": 3, "stem": "Calculate the amount of water, in mol, in the new equilibrium mixture (Kc = 0.161) using Table 3."},
    {"qnum": "06.1", "specRef": "3.3.7", "marks": 1, "stem": "Draw the skeletal formula of a branched chain aldehyde with molecular formula C5H10O that is optically active."},
    {"qnum": "06.2", "specRef": "3.3.7", "marks": 2, "stem": "Describe how you distinguish between separate samples of the two enantiomers of the branched chain aldehyde C5H10O."},
    {"qnum": "06.3", "specRef": "3.3.7", "marks": 2, "stem": "Draw the E and Z forms of a structural isomer of C5H10O that shows both optical and geometric isomerism."},
    {"qnum": "06.4", "specRef": "3.3.15", "marks": 2, "stem": "Draw two other cyclic isomers of C5H10O that have an ether functional group and only three peaks in their 13C NMR spectra."},
    {"qnum": "07.1", "specRef": "3.3.16", "marks": 1, "stem": "Identify the functional group present in compound K (C4H8O) from its infrared spectrum in Figure 5."},
    {"qnum": "07.2", "specRef": "3.3.16", "marks": 3, "stem": "Suggest three ways in which the infrared spectrum of M differs from that of L (C4H7NO) after reaction with H2 / Ni."},
    {"qnum": "07.3", "specRef": "3.3.15", "marks": 5, "stem": "Deduce the structure of Q (C3H7ClO) and explain your answer using the 1H NMR spectrum in Figure 7 and Table 4."},
    {"qnum": "08.1", "specRef": "3.3.5", "marks": 2, "stem": "State the type of reaction and name of the reagent needed for step 1 (cyclohexanol to cyclohexene).", "figures": ["fig-q8-scheme.jpg"]},
    {"qnum": "08.2", "specRef": "3.3.14", "marks": 4, "stem": "State the reagents needed and give equations for step 2 and step 3, showing the structure of Compound G.", "figures": ["fig-q8-scheme.jpg"]},
    {"qnum": "08.3", "specRef": "3.3.9", "marks": 5, "stem": "Name and complete the mechanism for cyclohexane-1,2-diol reacting with ethanedioyl dichloride to form one ester link."},
    {"qnum": "08.4", "specRef": "3.1.2", "marks": 2, "stem": "Suggest why chemists usually aim to design production methods with fewer steps and with a high percentage atom economy."},
    {"qnum": "09.1", "specRef": "3.3.3", "marks": 1, "stem": "State why the ozone layer is beneficial for living organisms."},
    {"qnum": "09.2", "specRef": "3.3.3", "marks": 1, "stem": "State how chlorofluorocarbons (CFCs) form chlorine atoms in the upper atmosphere."},
    {"qnum": "09.3", "specRef": "3.3.3", "marks": 2, "stem": "Give equations to show how chlorine atoms catalyse the decomposition of ozone."},
    {"qnum": "09.4", "specRef": "3.3.3", "marks": 3, "stem": "Complete each step in the free-radical mechanism to make an HCFC from a fluoroalkane and name the type of step."},
    {"qnum": "10.1", "specRef": "RP", "marks": 2, "stem": "Suggest why the 1.0 cm3 portions of the propanone + iodine reaction mixture are added to an excess of NaHCO3 solution."},
    {"qnum": "10.2", "specRef": "3.1.9", "marks": 2, "stem": "Suggest why the order of this reaction with respect to propanone can be ignored in this experiment."},
    {"qnum": "10.3", "specRef": "RP", "marks": 3, "stem": "Use the results in Table 5 to draw a graph of volume of sodium thiosulfate solution against time with a line of best fit."},
    {"qnum": "10.4", "specRef": "3.1.9", "marks": 2, "stem": "Explain how the graph shows that the reaction is zero-order with respect to iodine."},
    {"qnum": "10.5", "specRef": "3.1.9", "marks": 3, "stem": "Use Figure 8 (ln k against 1/T) to calculate a value for the activation energy (Ea), in kJ mol-1.", "figures": ["fig-q10-fig8.jpg"]},
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

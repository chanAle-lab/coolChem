"""Ingest AQA A-level Chemistry June 2019 Paper 3 (7405/3) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521544920_68644aad.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521544912_69d132a0.pdf"
)

PAPER_ID = "2019-june-7405-3"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2019,
    "series": "June",
    "unit": "7405/3",
    "level": "A-level",
    "date": "2019-06-19",
    "title": "7405/3 — A-level Paper 3: Practical Skills & Synoptic (June 2019)",
    "totalMarks": 90,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q3-fig1.jpg", "page": 10, "x0": 40, "y0": 65, "x1": 555, "y1": 340},
    {"filename": "fig-q3-table2.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 315},
    {"filename": "fig-q5-stem.jpg", "page": 16, "x0": 40, "y0": 65, "x1": 555, "y1": 230},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 4,
    "02.1": 6, "02.2": 6, "02.3": 7, "02.4": 8, "02.5": 8,
    "03.1": 10, "03.2": 10, "03.3": 10, "03.4": 11, "03.5": 11, "03.6": 12, "03.7": 13, "03.8": 13,
    "04.1": 14, "04.2": 14, "04.3": 15, "04.4": 15,
    "05.1": 16, "05.2": 16, "05.3": 16, "05.4": 17, "05.5": 17, "05.6": 17,
    "06": 18,
    "07": 19, "08": 19,
    "09": 20, "10": 20,
    "11": 21, "12": 21,
    "13": 22, "14": 22, "15": 22,
    "16": 23, "17": 23, "18": 23,
    "19": 24, "20": 24,
    "21": 25, "22": 25,
    "23": 26, "24": 26, "25": 26,
    "26": 27, "27": 27,
    "28": 28, "29": 28,
    "30": 29, "31": 29,
    "32": 30, "33": 30, "34": 30,
    "35": 31,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.7", "marks": 1, "stem": "Give the simplest ionic equation for the reaction of sodium thiosulfate with dilute hydrochloric acid."},
    {"qnum": "01.2", "specRef": "3.2.4", "marks": 2, "stem": "State the property of SO2 that causes pollution in rivers and give an equation for its reaction with water."},
    {"qnum": "01.3", "specRef": "3.1.3", "marks": 4, "stem": "Draw the shape of H2O, state the bond angle, and explain the shape and bond angle."},
    {"qnum": "01.4", "specRef": "RP", "marks": 6, "stem": "Describe an experiment to investigate the effect of temperature on the initial rate of the thiosulfate-acid reaction."},
    {"qnum": "02.1", "specRef": "3.1.3", "marks": 1, "stem": "Draw the displayed formula of a molecule of H2SO4."},
    {"qnum": "02.2", "specRef": "3.1.12", "marks": 2, "stem": "Give equations with appropriate arrows for each stage in the dissociation of sulfuric acid in aqueous solution."},
    {"qnum": "02.3", "specRef": "RP", "marks": 4, "stem": "Describe the method to make 250 cm3 of an aqueous solution containing an accurately measured mass of NaHSO4."},
    {"qnum": "02.4", "specRef": "3.1.12", "marks": 6, "stem": "Calculate Ka and its units for HSO4- given 605 mg NaHSO4 in 100 cm3 has pH = 1.72."},
    {"qnum": "02.5", "specRef": "3.1.12", "marks": 2, "stem": "Explain why dissolving sodium sulfate in the NaHSO4 solution increases the pH."},
    {"qnum": "03.1", "specRef": "3.1.11", "marks": 1, "stem": "Name the piece of apparatus labelled A in Figure 1."},
    {"qnum": "03.2", "specRef": "3.1.11", "marks": 1, "stem": "State the purpose of A in Figure 1.", "figures": ["fig-q3-fig1.jpg"]},
    {"qnum": "03.3", "specRef": "3.1.11", "marks": 1, "stem": "Name the substance used as electrode B in Figure 1.", "figures": ["fig-q3-fig1.jpg"]},
    {"qnum": "03.4", "specRef": "3.1.11", "marks": 4, "stem": "Complete Table 1 to identify C, D and E from Figure 1 and their essential conditions.", "figures": ["fig-q3-fig1.jpg"]},
    {"qnum": "03.5", "specRef": "3.1.11", "marks": 2, "stem": "Give the ionic equation for the cell reaction in Figure 1 and state the change needed for it to go to completion.", "figures": ["fig-q3-fig1.jpg"]},
    {"qnum": "03.6", "specRef": "RP", "marks": 3, "stem": "Complete Table 2 and plot a graph of Ecell against ln([Zn2+]/[Cu2+])."},
    {"qnum": "03.7", "specRef": "3.1.11", "marks": 3, "stem": "Calculate the gradient of your graph in 03.6 and use it to calculate the temperature T.", "figures": ["fig-q3-table2.jpg"]},
    {"qnum": "03.8", "specRef": "3.1.11", "marks": 2, "stem": "Calculate the electrode potential for Zn2+/Zn in experiment 2 and explain why it differs from the standard value.", "figures": ["fig-q3-table2.jpg"]},
    {"qnum": "04.1", "specRef": "3.3.8", "marks": 1, "stem": "Name the mechanism for the reaction between potassium cyanide and ethanal."},
    {"qnum": "04.2", "specRef": "3.3.7", "marks": 5, "stem": "Name the equal mixture of isomers formed, explain how ethanal leads to two isomers, and draw 3D representations."},
    {"qnum": "04.3", "specRef": "3.3.5", "marks": 2, "stem": "Suggest a suitable reagent and conditions to convert 2-hydroxypropanenitrile into acrylonitrile."},
    {"qnum": "04.4", "specRef": "3.3.4", "marks": 1, "stem": "Draw a section of polyacrylonitrile showing three repeating units."},
    {"qnum": "05.1", "specRef": "3.2.5", "marks": 1, "stem": "Give the equation for the reaction between iron and sulfuric acid."},
    {"qnum": "05.2", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the mean titre from Table 3."},
    {"qnum": "05.3", "specRef": "3.1.7", "marks": 1, "stem": "Give the overall ionic equation for the oxidation of Fe2+ by MnO4- in acidic conditions.", "figures": ["fig-q5-stem.jpg"]},
    {"qnum": "05.4", "specRef": "3.2.5", "marks": 1, "stem": "State the colour change seen at the end point of the titration."},
    {"qnum": "05.5", "specRef": "RP", "marks": 1, "stem": "Name the apparatus used for taking 25.0 cm3 portions and adding KMnO4 solution."},
    {"qnum": "05.6", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the percentage uncertainty in using the balance (+/- 0.005 g) to weigh 680 mg of iron wire."},
    {"qnum": "06", "specRef": "3.1.2", "marks": 1, "stem": "Which amount of NaOH would react exactly with 7.5 g of a diprotic acid H2A (Mr = 150)?"},
    {"qnum": "07", "specRef": "3.1.2", "marks": 1, "stem": "Which amount, in mol, of PbI2 is formed when 25.0 cm3 of 0.100 mol dm-3 Pb(NO3)2 and KI are mixed?"},
    {"qnum": "08", "specRef": "3.1.4", "marks": 1, "stem": "What is the enthalpy change for 4NH3 + 7O2 -> 4NO2 + 6H2O?"},
    {"qnum": "09", "specRef": "3.1.6", "marks": 1, "stem": "Which change leads to a higher concentration of SO3 in 2SO2 + O2 <=> 2SO3?"},
    {"qnum": "10", "specRef": "3.1.9", "marks": 1, "stem": "What is the initial concentration of Q in experiment 2 given rate = k[P][Q]^2?"},
    {"qnum": "11", "specRef": "3.1.10", "marks": 1, "stem": "What is the mole fraction of SO3 in the equilibrium mixture?"},
    {"qnum": "12", "specRef": "3.1.10", "marks": 1, "stem": "Which change increases the equilibrium yield of ammonia without changing Kp?"},
    {"qnum": "13", "specRef": "3.1.11", "marks": 1, "stem": "What is the EMF of the cell Fe|Fe2+||Cu2+|Cu?"},
    {"qnum": "14", "specRef": "3.1.1", "marks": 1, "stem": "Which atom has the greatest first ionisation energy?"},
    {"qnum": "15", "specRef": "3.2.2", "marks": 1, "stem": "What is the correct observation when barium metal is added to an excess of water?"},
    {"qnum": "16", "specRef": "3.2.3", "marks": 1, "stem": "Which salt gives a white precipitate with both AgNO3(aq) and dilute H2SO4?"},
    {"qnum": "17", "specRef": "3.2.3", "marks": 1, "stem": "Which statement is not correct about the trends in properties of hydrogen halides from HCl to HI?"},
    {"qnum": "18", "specRef": "3.2.5", "marks": 1, "stem": "What is observed when concentrated HCl is added to aqueous CuSO4 until no further change occurs?"},
    {"qnum": "19", "specRef": "3.2.3", "marks": 1, "stem": "What is the most suitable reagent for detecting carbonate ions in the presence of excess sulfate ions?"},
    {"qnum": "20", "specRef": "3.3.10", "marks": 1, "stem": "What is the name of the mechanism when methylbenzene reacts with conc HNO3 and conc H2SO4?"},
    {"qnum": "21", "specRef": "3.3.10", "marks": 1, "stem": "Which mechanism is not used in the synthesis shown?"},
    {"qnum": "22", "specRef": "3.3.5", "marks": 1, "stem": "Which compound is formed when 1-phenylethanol reacts with acidified K2Cr2O7?"},
    {"qnum": "23", "specRef": "3.3.8", "marks": 1, "stem": "Which row shows the correct observations with NaHCO3, acidified K2Cr2O7 and Tollens' reagent?"},
    {"qnum": "24", "specRef": "3.3.9", "marks": 1, "stem": "Which compound is formed by acid hydrolysis of phenylmethyl ethanoate?"},
    {"qnum": "25", "specRef": "RP", "marks": 1, "stem": "Which drying agent is suitable to dry a liquid sample of pentanoic acid?"},
    {"qnum": "26", "specRef": "3.3.10", "marks": 1, "stem": "Which is a correct representation of part of the mechanism for acylation of benzene?"},
    {"qnum": "27", "specRef": "3.3.11", "marks": 1, "stem": "Which compound is not a possible product when methylamine reacts with bromoethane?"},
    {"qnum": "28", "specRef": "3.3.12", "marks": 1, "stem": "Which polymer has hydrogen bonding between its chains?"},
    {"qnum": "29", "specRef": "3.3.13", "marks": 1, "stem": "Which structure shows part of a peptide link in a protein?"},
    {"qnum": "30", "specRef": "3.3.13", "marks": 1, "stem": "Which row shows the correct number of hydrogen bonds between DNA base pairs?"},
    {"qnum": "31", "specRef": "3.1.3", "marks": 1, "stem": "Which is not responsible for conduction of electricity?"},
    {"qnum": "32", "specRef": "3.3.5", "marks": 1, "stem": "Which is a likely reason why direct hydration of ethene has replaced fermentation in the UK?"},
    {"qnum": "33", "specRef": "3.3.4", "marks": 1, "stem": "Which alkene reacts with HBr to give 2-bromo-3-methylbutane as the major product?"},
    {"qnum": "34", "specRef": "RP", "marks": 1, "stem": "Which compound can be purified by forming a hot aqueous solution that recrystallises on cooling?"},
    {"qnum": "35", "specRef": "3.3.13", "marks": 1, "stem": "Which is the main aspartic acid species present in an aqueous solution at pH = 14?"},
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

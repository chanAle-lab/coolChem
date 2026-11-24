"""Ingest AQA AS Chemistry June 2022 Paper 2 (7404/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530579951_ed352888.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530579851_1dccb241.pdf"
)

PAPER_ID = "2022-june-7404-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2022,
    "series": "June",
    "unit": "7404/2",
    "level": "AS",
    "date": "2022-06-01",
    "title": "7404/2 — AS Paper 2: Organic and Physical Chemistry (June 2022)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-table1.jpg", "page": 2, "x0": 40, "y0": 65, "x1": 555, "y1": 430},
    {"filename": "fig-q7-wx.jpg", "page": 20, "x0": 40, "y0": 65, "x1": 555, "y1": 285},
    {"filename": "fig-q18-20-stem.jpg", "page": 26, "x0": 40, "y0": 235, "x1": 555, "y1": 335},
    {"filename": "fig-q21-22-stem.jpg", "page": 28, "x0": 40, "y0": 65, "x1": 555, "y1": 135},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 2, "01.4": 3, "01.5": 3, "01.6": 4,
    "02": 6,
    "03.1": 8, "03.2": 8, "03.3": 8, "03.4": 9, "03.5": 9,
    "04.1": 10, "04.2": 11, "04.3": 11,
    "05.1": 12, "05.2": 13, "05.3": 13,
    "06.1": 14, "06.2": 14, "06.3": 15,
    "07.1": 16, "07.2": 16, "07.3": 17, "07.4": 18, "07.5": 19, "07.6": 20, "07.7": 21,
    "08": 22,
    "09": 23, "10": 23,
    "11": 24, "12": 24, "13": 24,
    "14": 25, "15": 25, "16": 25,
    "17": 26, "18": 26,
    "19": 27, "20": 27,
    "21": 28, "22": 28,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.5", "marks": 1, "stem": "Complete Table 1 by calculating 1000/t for the experiment at 67 C.", "figures": ["fig-q1-table1.jpg"]},
    {"qnum": "01.2", "specRef": "RP", "marks": 1, "stem": "State the independent variable in this investigation."},
    {"qnum": "01.3", "specRef": "RP", "marks": 1, "stem": "Suggest how the student calculated the temperature values in Table 1 when temperature decreased during each experiment.", "figures": ["fig-q1-table1.jpg"]},
    {"qnum": "01.4", "specRef": "RP", "marks": 3, "stem": "Use the data in Table 1 to plot a graph of 1000/t against temperature.", "figures": ["fig-q1-table1.jpg"]},
    {"qnum": "01.5", "specRef": "RP", "marks": 1, "stem": "Use your graph in Question 01.4 to find the time taken for the mixture to go colourless at 60 C."},
    {"qnum": "01.6", "specRef": "3.1.5", "marks": 2, "stem": "Explain why a small increase in temperature causes a large increase in the rate of reaction."},
    {"qnum": "02", "specRef": "RP", "marks": 6, "stem": "Describe how simple chemical tests and a spectroscopic technique can distinguish butanoic acid, 2-methylpropanal, 2-methylpropanoic acid, and 2-methylpropan-1-ol."},
    {"qnum": "03.1", "specRef": "3.3.4", "marks": 1, "stem": "Draw the displayed formula of a position isomer of hex-2-ene that exists as E and Z isomers."},
    {"qnum": "03.2", "specRef": "3.3.4", "marks": 1, "stem": "Draw the displayed formula of a chain isomer of hex-2-ene that does not exist as E and Z isomers."},
    {"qnum": "03.3", "specRef": "3.3.6", "marks": 1, "stem": "Draw the skeletal formula of a functional group isomer of butanal with an IR absorption in the range 1680-1750 cm-1."},
    {"qnum": "03.4", "specRef": "3.3.6", "marks": 1, "stem": "Draw the skeletal formula of a structural isomer of butanal with an IR absorption in the range 3230-3550 cm-1."},
    {"qnum": "03.5", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the empirical formula of saturated halogenoalkanes containing 17.8% C, 3.0% H, 79.2% Br and give IUPAC names of two."},
    {"qnum": "04.1", "specRef": "3.1.2", "marks": 5, "stem": "Calculate the volume of gas, in m3, at 1250 C and 101000 Pa produced by the decomposition of 1.00 kg of TNT."},
    {"qnum": "04.2", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the volume of oxygen needed for the complete combustion of 200 cm3 of but-1-ene."},
    {"qnum": "04.3", "specRef": "3.3.2", "marks": 1, "stem": "Determine x in terms of n for the complete combustion of an alkane CnH2n+2 + xO2 -> nCO2 + (n+1)H2O."},
    {"qnum": "05.1", "specRef": "3.3.3", "marks": 5, "stem": "Name and outline the mechanism for the reaction of 1-iodopropane with an excess of ammonia to form propylamine."},
    {"qnum": "05.2", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the number of molecules in 5.0 cm3 of 1-iodopropane (density = 1.75 g cm-3, Mr = 169.9)."},
    {"qnum": "05.3", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the percentage yield when 10.3 g of 1-iodopropane produces 2.3 g of propylamine."},
    {"qnum": "06.1", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the percentage atom economy for the production of CCl3F in SbF3Br2 + CCl4 -> CCl3F + SbF2Br2Cl."},
    {"qnum": "06.2", "specRef": "3.3.3", "marks": 2, "stem": "Give equations to represent the two propagation steps in the conversion of CHCl2F into CCl3F."},
    {"qnum": "06.3", "specRef": "3.3.3", "marks": 1, "stem": "Give a termination step forming a compound with empirical formula CCl2F, showing its structural formula."},
    {"qnum": "07.1", "specRef": "3.3.5", "marks": 4, "stem": "Justify the statement that ethanol produced by fermentation of glucose is a carbon-neutral fuel, including equations."},
    {"qnum": "07.2", "specRef": "3.3.5", "marks": 1, "stem": "Suggest why ethanol produced in Europe using silverskin from South America is less likely to be carbon-neutral."},
    {"qnum": "07.3", "specRef": "3.1.4", "marks": 2, "stem": "Complete Table 2 (energy released per mole of CO2 produced) and deduce the fuel with the lowest environmental impact."},
    {"qnum": "07.4", "specRef": "3.1.4", "marks": 4, "stem": "Use the calorimetry results in Table 3 to calculate the final temperature of the water when 1.18 g of propanone burns."},
    {"qnum": "07.5", "specRef": "3.1.4", "marks": 3, "stem": "Use the mean bond enthalpy data in Table 4 to calculate the mean C-C bond enthalpy in gaseous butan-1-ol."},
    {"qnum": "07.6", "specRef": "3.3.4", "marks": 5, "stem": "Name and outline the mechanism to convert but-1-ene into compound W using concentrated sulfuric acid."},
    {"qnum": "07.7", "specRef": "3.3.4", "marks": 2, "stem": "Explain why there is a very low yield of butan-1-ol from but-1-ene in this manufacturing process.", "figures": ["fig-q7-wx.jpg"]},
    {"qnum": "08", "specRef": "3.3.2", "marks": 1, "stem": "Which equation represents hexadecane (C16H34) cracking to form an alkane with 8 carbons and two different unsaturated compounds?"},
    {"qnum": "09", "specRef": "3.3.2", "marks": 1, "stem": "Which statement about the industrial fractional distillation of crude oil is correct?"},
    {"qnum": "10", "specRef": "3.3.4", "marks": 1, "stem": "Which statement about poly(ethene) is correct?"},
    {"qnum": "11", "specRef": "3.3.4", "marks": 1, "stem": "Which statement is not correct about the polymer formed from CH2=CHCN?"},
    {"qnum": "12", "specRef": "3.3.5", "marks": 1, "stem": "Which alcohol when dehydrated forms a mixture of alkenes?"},
    {"qnum": "13", "specRef": "3.1.3", "marks": 1, "stem": "Which compound has the highest boiling point?"},
    {"qnum": "14", "specRef": "3.1.5", "marks": 1, "stem": "Which statement about molecules in a gas is correct?"},
    {"qnum": "15", "specRef": "3.3.5", "marks": 1, "stem": "Which compound produces (CH3)2CHCOCH3 when oxidised?"},
    {"qnum": "16", "specRef": "3.1.3", "marks": 1, "stem": "Which reaction does not result in a change in the shape around a carbon atom?"},
    {"qnum": "17", "specRef": "3.1.2", "marks": 1, "stem": "Which compound has the same empirical formula and molecular formula?"},
    {"qnum": "18", "specRef": "3.1.6", "marks": 1, "stem": "Which is the expression for Kc for CO(g) + 2H2(g) <-> CH3OH(g)?", "figures": ["fig-q18-20-stem.jpg"]},
    {"qnum": "19", "specRef": "3.1.6", "marks": 1, "stem": "What is the total amount, in mol, of gas at equilibrium when 2.0 mol CO and 3.0 mol H2 form 0.6 mol CH3OH?", "figures": ["fig-q18-20-stem.jpg"]},
    {"qnum": "20", "specRef": "3.1.6", "marks": 1, "stem": "Which change in condition will decrease the equilibrium yield of methanol?", "figures": ["fig-q18-20-stem.jpg"]},
    {"qnum": "21", "specRef": "3.3.3", "marks": 1, "stem": "Which compound is not produced when 2-bromobutane is warmed with potassium hydroxide solution?", "figures": ["fig-q21-22-stem.jpg"]},
    {"qnum": "22", "specRef": "3.3.3", "marks": 1, "stem": "What is the role of the hydroxide ions in the elimination reaction of 2-bromobutane?", "figures": ["fig-q21-22-stem.jpg"]},
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

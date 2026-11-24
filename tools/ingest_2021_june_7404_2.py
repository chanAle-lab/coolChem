"""Ingest AQA AS Chemistry June 2021 Paper 2 (7404/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521628181_badc0b20.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521628230_94d353b8.pdf"
)

PAPER_ID = "2021-june-7404-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2021,
    "series": "June",
    "unit": "7404/2",
    "level": "AS",
    "date": "2021-06-01",
    "title": "7404/2 — AS Paper 2: Organic and Physical Chemistry (June 2021)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-fig1.jpg", "page": 3, "x0": 40, "y0": 65, "x1": 555, "y1": 310},
    {"filename": "fig-q7-struct.jpg", "page": 18, "x0": 40, "y0": 65, "x1": 555, "y1": 175},
    {"filename": "fig-q14-16-stem.jpg", "page": 24, "x0": 40, "y0": 65, "x1": 555, "y1": 125},
]

PAGE_MAP = {
    "01.1": 3, "01.2": 3, "01.3": 3, "01.4": 3,
    "02.1": 4, "02.2": 5, "02.3": 5,
    "03.1": 6, "03.2": 8, "03.3": 9, "03.4": 9,
    "04.1": 10, "04.2": 10, "04.3": 11, "04.4": 11, "04.5": 11, "04.6": 12,
    "05.1": 14, "05.2": 15, "05.3": 15,
    "06.1": 16, "06.2": 17,
    "07.1": 18, "07.2": 18, "07.3": 19, "07.4": 19,
    "08.1": 20, "08.2": 20, "08.3": 21,
    "09": 22, "10": 22,
    "11": 23, "12": 23, "13": 23,
    "14": 24, "15": 24,
    "16": 25, "17": 25,
    "18": 26, "19": 26, "20": 26,
    "21": 27,
    "22": 28, "23": 28,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.5", "marks": 1, "stem": "Label the y-axis on the Maxwell-Boltzmann distribution in Figure 1.", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "01.2", "specRef": "3.1.5", "marks": 1, "stem": "State what the area under the Maxwell-Boltzmann curve represents.", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "01.3", "specRef": "3.1.5", "marks": 1, "stem": "Label the most probable energy (Emp) on Figure 1.", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "01.4", "specRef": "3.1.5", "marks": 2, "stem": "Explain why a small increase in temperature leads to a large increase in the rate of reaction.", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "02.1", "specRef": "3.3.4", "marks": 5, "stem": "Name and outline the mechanism for the reaction of cyclohexene with bromine (Br2)."},
    {"qnum": "02.2", "specRef": "3.3.4", "marks": 3, "stem": "Explain why there is an attraction between a C=C double bond and Br2."},
    {"qnum": "02.3", "specRef": "3.3.4", "marks": 1, "stem": "Draw the skeletal formula of the halogenoalkane formed when buta-1,3-diene reacts with an excess of Br2."},
    {"qnum": "03.1", "specRef": "RP", "marks": 6, "stem": "Identify three errors in the distillation apparatus in Figure 2 for making propanone from propan-2-ol and explain how to correct them."},
    {"qnum": "03.2", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the percentage yield of propanone from 2.0 cm3 of propan-2-ol."},
    {"qnum": "03.3", "specRef": "3.1.3", "marks": 2, "stem": "Complete Table 1 to suggest the shape and bond angle around the central carbon atom in propan-2-ol and propanone."},
    {"qnum": "03.4", "specRef": "3.1.3", "marks": 3, "stem": "Explain why propanone has a lower boiling point than propan-2-ol."},
    {"qnum": "04.1", "specRef": "3.3.1", "marks": 1, "stem": "Give the IUPAC name for CFC-11."},
    {"qnum": "04.2", "specRef": "3.3.3", "marks": 1, "stem": "Give an equation for the initiation step in the decomposition of ozone by CFC-11."},
    {"qnum": "04.3", "specRef": "3.1.2", "marks": 2, "stem": "Estimate the number of moles of ozone destroyed by 0.50 kg of CFC-11 (Mr = 137.5)."},
    {"qnum": "04.4", "specRef": "3.3.3", "marks": 1, "stem": "Give an overall equation for the decomposition of ozone."},
    {"qnum": "04.5", "specRef": "3.3.3", "marks": 1, "stem": "State the role of the chlorine free radical in the decomposition of ozone."},
    {"qnum": "04.6", "specRef": "3.3.16", "marks": 2, "stem": "State and explain how CFC-11 is able to contribute to global warming."},
    {"qnum": "05.1", "specRef": "3.3.4", "marks": 6, "stem": "Describe the three key steps in the manufacture of poly(propene) from crude oil (fractional distillation, cracking, and addition polymerisation)."},
    {"qnum": "05.2", "specRef": "3.3.4", "marks": 1, "stem": "Explain why poly(propene) is unreactive."},
    {"qnum": "05.3", "specRef": "3.3.4", "marks": 1, "stem": "Suggest one environmental advantage of using biodegradable polymers."},
    {"qnum": "06.1", "specRef": "3.1.2", "marks": 5, "stem": "Calculate the relative molecular mass (Mr) of liquid Y using the ideal gas equation and the data in Table 2."},
    {"qnum": "06.2", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the total number of moles of gas remaining after the complete combustion of 0.0010 mol of 2,2,4-trimethylpentane with 0.0200 mol of O2."},
    {"qnum": "07.1", "specRef": "3.3.3", "marks": 1, "stem": "Name the type of reaction when 3-chloroprop-1-ene reacts with dilute aqueous sodium hydroxide to form prop-2-en-1-ol.", "figures": ["fig-q7-struct.jpg"]},
    {"qnum": "07.2", "specRef": "3.3.5", "marks": 4, "stem": "Describe a chemical test to confirm the presence of the C=C bond and a chemical test to confirm the presence of the -OH group in prop-2-en-1-ol."},
    {"qnum": "07.3", "specRef": "3.3.4", "marks": 1, "stem": "Draw the repeating unit of poly(prop-2-en-1-ol)."},
    {"qnum": "07.4", "specRef": "3.3.6", "marks": 1, "stem": "Identify the functional group isomer of prop-2-en-1-ol from the infrared spectrum in Figure 3."},
    {"qnum": "08.1", "specRef": "3.1.4", "marks": 1, "stem": "Define the term enthalpy change."},
    {"qnum": "08.2", "specRef": "3.1.4", "marks": 4, "stem": "Calculate the mean C-H bond enthalpy in propane using the enthalpy of combustion and the bond enthalpy data provided."},
    {"qnum": "08.3", "specRef": "3.1.4", "marks": 1, "stem": "Explain why the value given for the O=O bond enthalpy in Question 08.2 is not a mean value."},
    {"qnum": "09", "specRef": "3.1.2", "marks": 1, "stem": "What is the atom economy for the formation of iron in the blast furnace reaction?"},
    {"qnum": "10", "specRef": "3.1.5", "marks": 1, "stem": "Which statement about a catalyst is correct?"},
    {"qnum": "11", "specRef": "3.1.2", "marks": 1, "stem": "What is the concentration in mol dm-3 of 80 mg of ethanol (Mr = 46.0) per 100 cm3 of blood?"},
    {"qnum": "12", "specRef": "3.3.1", "marks": 1, "stem": "Which pair of compounds are structural isomers?"},
    {"qnum": "13", "specRef": "3.3.2", "marks": 1, "stem": "Which alkane has the highest boiling point?"},
    {"qnum": "14", "specRef": "3.3.3", "marks": 1, "stem": "What is the organic product when 1-bromopropane reacts with potassium cyanide in aqueous ethanol?", "figures": ["fig-q14-16-stem.jpg"]},
    {"qnum": "15", "specRef": "3.3.3", "marks": 1, "stem": "What is the role of the cyanide ion in the reaction of 1-bromopropane with KCN?", "figures": ["fig-q14-16-stem.jpg"]},
    {"qnum": "16", "specRef": "3.3.3", "marks": 1, "stem": "Which row correctly shows the compound with a faster rate of reaction with KCN (1-bromopropane vs 1-chloropropane) and the reason?", "figures": ["fig-q14-16-stem.jpg"]},
    {"qnum": "17", "specRef": "3.3.5", "marks": 1, "stem": "Which alcohol can be oxidised to a ketone?"},
    {"qnum": "18", "specRef": "3.3.4", "marks": 1, "stem": "Which compound reacts with HBr to give 2-bromo-3-methylbutane as the major product?"},
    {"qnum": "19", "specRef": "3.3.4", "marks": 1, "stem": "Which statement is correct about stereoisomerism in alkenes?"},
    {"qnum": "20", "specRef": "3.3.6", "marks": 1, "stem": "Which compound has a molecular ion peak at m/z = 72 in its mass spectrum?"},
    {"qnum": "21", "specRef": "3.1.5", "marks": 1, "stem": "Which curve represents the reaction of excess magnesium with a different concentration and volume of hydrochloric acid?"},
    {"qnum": "22", "specRef": "3.3.2", "marks": 1, "stem": "Which statement is not correct about the pollutant sulfur dioxide?"},
    {"qnum": "23", "specRef": "3.3.1", "marks": 1, "stem": "Which species is a free radical?"},
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

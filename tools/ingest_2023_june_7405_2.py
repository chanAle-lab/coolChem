"""Ingest AQA A-level Chemistry June 2023 Paper 2 (7405/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530732038_901ebc88.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530732006_72c8e3b2.pdf"
)

PAPER_ID = "2023-june-7405-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2023,
    "series": "June",
    "unit": "7405/2",
    "level": "A-level",
    "date": "2023-06-19",
    "title": "7405/2 — A-level Paper 2: Organic and Physical Chemistry (June 2023)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q4-scheme.jpg", "page": 8, "x0": 40, "y0": 100, "x1": 555, "y1": 265},
    {"filename": "fig-q5-spectra.jpg", "page": 12, "x0": 40, "y0": 120, "x1": 555, "y1": 625},
    {"filename": "fig-q5-table2.jpg", "page": 13, "x0": 40, "y0": 100, "x1": 555, "y1": 215},
    {"filename": "fig-q6-liquids.jpg", "page": 16, "x0": 40, "y0": 100, "x1": 555, "y1": 475},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3, "01.3": 3,
    "02.1": 4, "02.2": 4,
    "03.1": 6, "03.2": 7, "03.3": 7,
    "04.1": 8, "04.2": 8, "04.3": 10, "04.4": 10, "04.5": 11, "04.6": 11,
    "05.1": 12, "05.2": 12, "05.3": 12, "05.4": 13, "05.5": 13, "05.6": 14, "05.7": 15,
    "06.1": 16, "06.2": 17, "06.3": 17, "06.4": 18,
    "07.1": 20, "07.2": 20, "07.3": 21, "07.4": 21,
    "08.1": 22, "08.2": 22, "08.3": 23, "08.4": 23, "08.5": 23, "08.6": 24, "08.7": 25,
    "09.1": 26, "09.2": 26, "09.3": 27, "09.4": 28,
}

MS_QNUM_MAP = {}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "RP", "marks": 1, "stem": "Suggest why using a conical flask instead of a beaker gives more accurate results."},
    {"qnum": "01.2", "specRef": "3.1.5", "marks": 3, "stem": "Calculate the rate of reaction at 2 minutes from Figure 2 and deduce its units."},
    {"qnum": "01.3", "specRef": "3.3.9", "marks": 3, "stem": "Sketch the curve for chloroethanoic acid and explain why it is a stronger acid than ethanoic acid."},
    {"qnum": "02.1", "specRef": "3.1.9", "marks": 3, "stem": "Complete Table 1 by calculating the missing concentrations and relative initial rates."},
    {"qnum": "02.2", "specRef": "3.1.9", "marks": 2, "stem": "Deduce the rate-determining step for the suggested mechanism and give a reason."},
    {"qnum": "03.1", "specRef": "3.3.9", "marks": 4, "stem": "Complete Figure 3 for the nucleophilic addition-elimination mechanism."},
    {"qnum": "03.2", "specRef": "3.3.10", "marks": 4, "stem": "Complete Figure 4 for the nitration of methylbenzene and name the mechanism."},
    {"qnum": "03.3", "specRef": "3.3.8", "marks": 4, "stem": "Complete Figure 5 for nucleophilic addition of hydride to propanone and name the mechanism."},
    {"qnum": "04.1", "specRef": "3.3.1", "marks": 1, "stem": "Use IUPAC rules to name isomer W.", "figures": ["fig-q4-scheme.jpg"]},
    {"qnum": "04.2", "specRef": "3.3.4", "marks": 6, "stem": "Draw the other two isomers from Reaction 1 and explain why all three form.", "figures": ["fig-q4-scheme.jpg"]},
    {"qnum": "04.3", "specRef": "3.3.3", "marks": 2, "stem": "Identify the reagent and condition needed for reaction 2."},
    {"qnum": "04.4", "specRef": "3.3.11", "marks": 2, "stem": "State the reagent, conditions, and equation for reaction 3."},
    {"qnum": "04.5", "specRef": "3.3.12", "marks": 2, "stem": "Deduce the values of x and y in the equation for the formation of nylon 4,6."},
    {"qnum": "04.6", "specRef": "3.3.12", "marks": 2, "stem": "Draw another section of nylon 4,6 showing two hydrogen bonds between the chains."},
    {"qnum": "05.1", "specRef": "3.3.16", "marks": 1, "stem": "Identify the bond that causes the IR absorption at 1725 cm-1."},
    {"qnum": "05.2", "specRef": "3.3.15", "marks": 1, "stem": "State how many different carbon environments are in a molecule of Z."},
    {"qnum": "05.3", "specRef": "3.3.15", "marks": 1, "stem": "State the type of carbon environment that causes the peak at 174 ppm."},
    {"qnum": "05.4", "specRef": "3.3.15", "marks": 5, "stem": "Explain what can be deduced from the 1H NMR peaks at 4.10 ppm and 1.26 ppm."},
    {"qnum": "05.5", "specRef": "3.3.15", "marks": 1, "stem": "Deduce the part of the structure of Z that causes the peak at 2.19 ppm."},
    {"qnum": "05.6", "specRef": "3.3.15", "marks": 1, "stem": "Suggest why it would be difficult to determine Z from Figure 9 without Table 2.", "figures": ["fig-q5-table2.jpg"]},
    {"qnum": "05.7", "specRef": "3.3.15", "marks": 1, "stem": "Deduce the structure of compound Z.", "figures": ["fig-q5-spectra.jpg"]},
    {"qnum": "06.1", "specRef": "RP", "marks": 1, "stem": "Identify the missing reagent needed in Test 1."},
    {"qnum": "06.2", "specRef": "RP", "marks": 2, "stem": "State the two mistakes in the methods for the other tests and how to correct them.", "figures": ["fig-q6-liquids.jpg"]},
    {"qnum": "06.3", "specRef": "RP", "marks": 8, "stem": "Identify which liquids J, K, L, M react in Tests 1-4 and state expected observations.", "figures": ["fig-q6-liquids.jpg"]},
    {"qnum": "06.4", "specRef": "RP", "marks": 3, "stem": "Label S, T, U in Figure 10 and explain why fractional distillation is preferred.", "figures": ["fig-q6-liquids.jpg"]},
    {"qnum": "07.1", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the volume, in cm3, of propanone in the gas syringe."},
    {"qnum": "07.2", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the decrease in volume when the gas syringe is cooled to 75 °C."},
    {"qnum": "07.3", "specRef": "RP", "marks": 2, "stem": "Calculate the uncertainty in the volume caused by the ±0.001 g balance uncertainty."},
    {"qnum": "07.4", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the total volume of the remaining gas mixture after combustion of propanone."},
    {"qnum": "08.1", "specRef": "3.3.9", "marks": 2, "stem": "Complete the equation for the acidic hydrolysis of the triester in palm oil."},
    {"qnum": "08.2", "specRef": "3.1.4", "marks": 5, "stem": "Calculate the enthalpy of combustion of palmitic acid from calorimetry data."},
    {"qnum": "08.3", "specRef": "3.1.4", "marks": 2, "stem": "State how the calculated value differs from data book values and give a reason."},
    {"qnum": "08.4", "specRef": "3.1.2", "marks": 3, "stem": "Calculate the empirical formula of the biofuel made from sewage sludge."},
    {"qnum": "08.5", "specRef": "3.3.2", "marks": 2, "stem": "Suggest one other environmental problem from complete combustion of this biofuel and its pollutant."},
    {"qnum": "08.6", "specRef": "3.1.4", "marks": 3, "stem": "Use mean bond enthalpies to calculate ΔH for the fermentation of glucose."},
    {"qnum": "08.7", "specRef": "3.1.4", "marks": 2, "stem": "Use standard enthalpies of formation to calculate ΔH for 2CO2 + 3H2O -> C2H5OH + 3O2."},
    {"qnum": "09.1", "specRef": "3.3.1", "marks": 1, "stem": "Deduce the general formula for the ketene homologous series."},
    {"qnum": "09.2", "specRef": "3.3.8", "marks": 3, "stem": "Complete the mechanism in Figure 11 for the decomposition of ethanoic anhydride."},
    {"qnum": "09.3", "specRef": "3.1.9", "marks": 3, "stem": "Use the Arrhenius equation to calculate temperature T1."},
    {"qnum": "09.4", "specRef": "3.1.5", "marks": 5, "stem": "Sketch Maxwell-Boltzmann distributions at T1 and T2 and explain why the rate is faster at T2."},
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

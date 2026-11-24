"""Ingest AQA AS Chemistry June 2020 Paper 1 (7404/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521576295_7ff8ec3e.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521576266_537ed972.pdf"
)

PAPER_ID = "2020-june-7404-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2020,
    "series": "June",
    "unit": "7404/1",
    "level": "AS",
    "date": "2020-05-18",
    "title": "7404/1 — AS Paper 1: Inorganic and Physical Chemistry (June 2020)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q7-stem.jpg", "page": 16, "x0": 40, "y0": 65, "x1": 555, "y1": 270},
    {"filename": "fig-q8-1-cont.jpg", "page": 19, "x0": 40, "y0": 65, "x1": 555, "y1": 165},
    {"filename": "fig-q8-table3.jpg", "page": 20, "x0": 40, "y0": 65, "x1": 555, "y1": 310},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3,
    "02.1": 4, "02.2": 5, "02.3": 5,
    "03.1": 6, "03.2": 6, "03.3": 7,
    "04.1": 8, "04.2": 8, "04.3": 10, "04.4": 10,
    "05.1": 11, "05.2": 11, "05.3": 12,
    "06": 13,
    "07.1": 14, "07.2": 15, "07.3": 16, "07.4": 16, "07.5": 17, "07.6": 17,
    "08.1": 18, "08.2": 19, "08.3": 20,
    "09": 21, "10": 21,
    "11": 22, "12": 22, "13": 22,
    "14": 23, "15": 23, "16": 23,
    "17": 24, "18": 24, "19": 24,
    "20": 25, "21": 25,
    "22": 26, "23": 26,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.1", "marks": 3, "stem": "Give one example of a Period 3 element that deviates from the general trend in ionisation energy and explain why."},
    {"qnum": "01.2", "specRef": "3.1.1", "marks": 1, "stem": "Give an equation, including state symbols, for the third ionisation energy of sodium."},
    {"qnum": "01.3", "specRef": "3.1.1", "marks": 3, "stem": "Identify Period 3 element X from the successive ionisation energies graph (Figure 1) and explain your choice."},
    {"qnum": "02.1", "specRef": "3.1.2", "marks": 5, "stem": "Calculate the mass of sodium hydroxide used to make 200 cm3 of solution from the titration results in Table 1."},
    {"qnum": "02.2", "specRef": "RP", "marks": 1, "stem": "Suggest why forgetting to remove the funnel from the top of the burette might affect the titre volume recorded."},
    {"qnum": "02.3", "specRef": "RP", "marks": 1, "stem": "State one advantage of using a conical flask rather than a beaker for the titration."},
    {"qnum": "03.1", "specRef": "3.1.1", "marks": 2, "stem": "Define the term relative atomic mass."},
    {"qnum": "03.2", "specRef": "3.1.1", "marks": 2, "stem": "Calculate the relative atomic mass (Ar) of the sample of krypton to 1 decimal place from Table 2."},
    {"qnum": "03.3", "specRef": "3.1.1", "marks": 4, "stem": "Calculate the length, in metres, of the TOF flight tube for an 84Kr+ ion."},
    {"qnum": "04.1", "specRef": "3.1.4", "marks": 1, "stem": "State the meaning of the term enthalpy change as applied to a chemical reaction."},
    {"qnum": "04.2", "specRef": "RP", "marks": 6, "stem": "Explain how the calorimetry method for CaCO3 + HCl can be improved and how the data can be used to determine an accurate temperature change."},
    {"qnum": "04.3", "specRef": "3.1.4", "marks": 5, "stem": "Calculate the maximum final temperature when 50.0 cm3 of 0.500 mol dm-3 HCl reacts with 50.0 cm3 of 0.500 mol dm-3 NaOH."},
    {"qnum": "04.4", "specRef": "RP", "marks": 1, "stem": "Suggest how, without changing the apparatus, the experiment in 04.3 could be improved to reduce percentage uncertainty in temperature change."},
    {"qnum": "05.1", "specRef": "3.1.3", "marks": 2, "stem": "Explain why the melting point of magnesium is higher than the melting point of sodium."},
    {"qnum": "05.2", "specRef": "3.2.2", "marks": 2, "stem": "Give an equation for the extraction of titanium using magnesium and explain, in terms of oxidation states, why magnesium is the reducing agent."},
    {"qnum": "05.3", "specRef": "3.2.2", "marks": 2, "stem": "State what is observed when dilute aqueous sodium hydroxide is added to separate solutions of magnesium chloride and barium chloride."},
    {"qnum": "06", "specRef": "3.1.3", "marks": 5, "stem": "Draw the shapes of NCl3 and NCl4+, name the shape of NCl3, and state and explain the bond angle in NCl4+."},
    {"qnum": "07.1", "specRef": "3.2.3", "marks": 3, "stem": "Give a reason why water is treated with chlorine, explain why it is added despite being toxic, and give an equation for Cl2 + cold water."},
    {"qnum": "07.2", "specRef": "3.2.3", "marks": 4, "stem": "Give half-equations, overall equation, and another sulfur-containing reduction product for solid NaI reacting with concentrated H2SO4."},
    {"qnum": "07.3", "specRef": "3.2.3", "marks": 1, "stem": "Suggest why an excess of silver nitrate is added to the mixture of NaCl and NaI.", "figures": ["fig-q7-stem.jpg"]},
    {"qnum": "07.4", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the amount, in moles, of silver iodide obtained (315 mg).", "figures": ["fig-q7-stem.jpg"]},
    {"qnum": "07.5", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the mass, in grams, of sodium iodide in the mixture.", "figures": ["fig-q7-stem.jpg"]},
    {"qnum": "07.6", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the percentage by mass of sodium chloride in the 600 mg mixture.", "figures": ["fig-q7-stem.jpg"]},
    {"qnum": "08.1", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the Mr of volatile liquid A to 3 significant figures using the gas syringe data in Table 3.", "figures": ["fig-q8-1-cont.jpg"]},
    {"qnum": "08.2", "specRef": "3.1.2", "marks": 2, "stem": "Explain the effect on the calculated Mr if some of the liquid injected into the gas syringe did not vaporise."},
    {"qnum": "08.3", "specRef": "3.1.2", "marks": 1, "stem": "Calculate the percentage uncertainty in the mass of liquid A injected (balance uncertainty +/- 0.001 g).", "figures": ["fig-q8-table3.jpg"]},
    {"qnum": "09", "specRef": "3.1.1", "marks": 1, "stem": "Which atom has the smallest number of neutrons?"},
    {"qnum": "10", "specRef": "3.1.3", "marks": 1, "stem": "Which species contains bonds that have different polarities?"},
    {"qnum": "11", "specRef": "3.1.3", "marks": 1, "stem": "Which compound has hydrogen bonding?"},
    {"qnum": "12", "specRef": "3.1.4", "marks": 1, "stem": "Which reaction has an enthalpy change equal to the standard enthalpy of formation of lithium fluoride?"},
    {"qnum": "13", "specRef": "3.1.7", "marks": 1, "stem": "NO2- ions can be reduced in acidic solution to NO. How many electrons are gained when each NO2- ion is reduced?"},
    {"qnum": "14", "specRef": "3.1.1", "marks": 1, "stem": "Which is the electron configuration of an atom with only two unpaired electrons?"},
    {"qnum": "15", "specRef": "3.1.1", "marks": 1, "stem": "Which represents the correct order of increasing radius of the ions?"},
    {"qnum": "16", "specRef": "3.1.3", "marks": 1, "stem": "Which compound contains a co-ordinate bond?"},
    {"qnum": "17", "specRef": "3.2.3", "marks": 1, "stem": "Which property increases down Group 7?"},
    {"qnum": "18", "specRef": "3.2.1", "marks": 1, "stem": "Which of these elements (Ar, Cl, Si, S) has the highest melting point?"},
    {"qnum": "19", "specRef": "3.1.6", "marks": 1, "stem": "Which statement is not always correct for a reaction at equilibrium?"},
    {"qnum": "20", "specRef": "3.1.4", "marks": 1, "stem": "What is the enthalpy change for 2FeO(s) + 1/2 O2(g) -> Fe2O3(s)?"},
    {"qnum": "21", "specRef": "3.1.7", "marks": 1, "stem": "Which compound contains chlorine in an oxidation state of +1?"},
    {"qnum": "22", "specRef": "3.2.3", "marks": 1, "stem": "Which equation shows a redox reaction that does not occur?"},
    {"qnum": "23", "specRef": "3.1.3", "marks": 1, "stem": "Which molecule has a permanent dipole?"},
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

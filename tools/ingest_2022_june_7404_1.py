"""Ingest AQA AS Chemistry June 2022 Paper 1 (7404/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530579811_b2400ab6.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795530579836_d91c0081.pdf"
)

PAPER_ID = "2022-june-7404-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2022,
    "series": "June",
    "unit": "7404/1",
    "level": "AS",
    "date": "2022-06-01",
    "title": "7404/1 — AS Paper 1: Inorganic and Physical Chemistry (June 2022)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q4-table3.jpg", "page": 8, "x0": 40, "y0": 420, "x1": 555, "y1": 520},
    {"filename": "fig-q7-fig1.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 555, "y1": 280},
    {"filename": "fig-q8-table4.jpg", "page": 16, "x0": 40, "y0": 65, "x1": 555, "y1": 275},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 2,
    "02.1": 3, "02.2": 3, "02.3": 4, "02.4": 6, "02.5": 6,
    "03": 7,
    "04.1": 8, "04.2": 8, "04.3": 8, "04.4": 9, "04.5": 9,
    "05": 10,
    "06.1": 11, "06.2": 11, "06.3": 11,
    "07.1": 12, "07.2": 13, "07.3": 13, "07.4": 14, "07.5": 14,
    "08.1": 16, "08.2": 16, "08.3": 17, "08.4": 17,
    "09": 18, "10": 18,
    "11": 19, "12": 19, "13": 19,
    "14": 20, "15": 20, "16": 20,
    "17": 21, "18": 21, "19": 21,
    "20": 22, "21": 22, "22": 22,
    "23": 23,
}

# Official MS labels Q03 as '03.1'
MS_QNUM_MAP = {
    "03": "03.1",
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.1", "marks": 2, "stem": "Explain why the first ionisation energy of the Group 2 elements decreases down the group."},
    {"qnum": "01.2", "specRef": "3.1.1", "marks": 1, "stem": "Give an equation, including state symbols, for the third ionisation energy of magnesium."},
    {"qnum": "01.3", "specRef": "3.1.1", "marks": 2, "stem": "Explain why the third ionisation energy of magnesium is much higher than the second ionisation energy of magnesium."},
    {"qnum": "02.1", "specRef": "RP", "marks": 2, "stem": "Describe a method to add an accurately known mass of solid citric acid to a beaker to make a solution."},
    {"qnum": "02.2", "specRef": "3.1.2", "marks": 3, "stem": "Calculate the concentration, in mol dm-3, of citric acid when 0.834 g is dissolved and made up to 500 cm3."},
    {"qnum": "02.3", "specRef": "RP", "marks": 6, "stem": "Identify three practical mistakes in the titration method, explain why each is a mistake, and suggest how to overcome them."},
    {"qnum": "02.4", "specRef": "RP", "marks": 2, "stem": "Complete Table 1 and calculate the mean titre from the concordant burette readings."},
    {"qnum": "02.5", "specRef": "RP", "marks": 1, "stem": "Calculate the percentage uncertainty in the use of the burette in Run 1 (+/- 0.15 cm3)."},
    {"qnum": "03", "specRef": "3.1.3", "marks": 3, "stem": "Complete Table 2 by drawing the shapes of AsF5 and KrF2 (showing lone pairs) and deduce the bond angle(s) in AsF5."},
    {"qnum": "04.1", "specRef": "3.1.3", "marks": 3, "stem": "Complete the diagram to show how one molecule of ammonia forms a hydrogen bond with one molecule of ethanol."},
    {"qnum": "04.2", "specRef": "3.1.3", "marks": 1, "stem": "Define the term electronegativity."},
    {"qnum": "04.3", "specRef": "3.1.3", "marks": 1, "stem": "Deduce the two atoms from Table 3 that will form the most polar bond.", "figures": ["fig-q4-table3.jpg"]},
    {"qnum": "04.4", "specRef": "3.1.3", "marks": 2, "stem": "Explain why CBr4 is not a polar molecule even though the C-Br bond is polar."},
    {"qnum": "04.5", "specRef": "3.1.3", "marks": 3, "stem": "Suggest, in terms of intermolecular forces, why CBr4 has a higher boiling point than CHBr3."},
    {"qnum": "05", "specRef": "3.1.1", "marks": 5, "stem": "Calculate the mass of one 121Sb+ ion in kg and the time taken for a 123Sb+ ion to travel through the 1.05 m TOF flight tube."},
    {"qnum": "06.1", "specRef": "3.1.7", "marks": 1, "stem": "State, in terms of electrons, the meaning of the term oxidising agent."},
    {"qnum": "06.2", "specRef": "3.1.7", "marks": 2, "stem": "Give the oxidation half-equation for I- -> I2 and deduce the reduction half-equation for IO3- -> I2 in acidic solution."},
    {"qnum": "06.3", "specRef": "3.2.3", "marks": 2, "stem": "Give an equation for iodide ions reacting with concentrated sulfuric acid to form sulfur, and identify the foul-smelling gas."},
    {"qnum": "07.1", "specRef": "3.1.6", "marks": 2, "stem": "Explain how Figure 1 shows that the forward reaction in this equilibrium is exothermic."},
    {"qnum": "07.2", "specRef": "3.1.6", "marks": 3, "stem": "State and explain whether the forward reaction results in an increase, decrease, or no change in moles of gas.", "figures": ["fig-q7-fig1.jpg"]},
    {"qnum": "07.3", "specRef": "3.1.6", "marks": 1, "stem": "Explain why using a catalyst has no effect on the percentage yield."},
    {"qnum": "07.4", "specRef": "3.1.6", "marks": 5, "stem": "Calculate the amount, in moles, of ammonia present in 0.150 dm3 of the equilibrium mixture at 745 K (Kc = 0.118 mol-2 dm6)."},
    {"qnum": "07.5", "specRef": "3.1.6", "marks": 2, "stem": "Calculate Kc and state its units for the reverse reaction 2NH3(g) <-> 3H2(g) + N2(g) at 745 K."},
    {"qnum": "08.1", "specRef": "3.2.2", "marks": 2, "stem": "Identify the gas formed in Test 1 (with Na2CO3) and describe a further test to confirm its identity.", "figures": ["fig-q8-table4.jpg"]},
    {"qnum": "08.2", "specRef": "3.2.3", "marks": 2, "stem": "Explain how the observations from Test 1 and Test 2 show that solution B contains hydrochloric acid.", "figures": ["fig-q8-table4.jpg"]},
    {"qnum": "08.3", "specRef": "3.2.2", "marks": 4, "stem": "Describe a series of tests to show that solution C contains ammonium sulfate.", "figures": ["fig-q8-table4.jpg"]},
    {"qnum": "08.4", "specRef": "3.2.3", "marks": 2, "stem": "Explain how the masses recorded before and after adding dilute ammonia show that solution D contains a mixture of halide ions.", "figures": ["fig-q8-table4.jpg"]},
    {"qnum": "09", "specRef": "3.1.1", "marks": 1, "stem": "Which atom has two more protons and two more neutrons than 52Cr?"},
    {"qnum": "10", "specRef": "3.1.1", "marks": 1, "stem": "Which ground-state atom contains only two unpaired electrons?"},
    {"qnum": "11", "specRef": "3.1.1", "marks": 1, "stem": "Identify the element from its first six ionisation energies (1090, 2350, 4610, 6220, 37800, 47000 kJ mol-1)."},
    {"qnum": "12", "specRef": "3.1.1", "marks": 1, "stem": "In which pair is the first ionisation energy of atom Y greater than that of atom X?"},
    {"qnum": "13", "specRef": "3.1.1", "marks": 1, "stem": "Which statement about isotopes of an element is not correct?"},
    {"qnum": "14", "specRef": "3.1.2", "marks": 1, "stem": "What is the empirical formula of an oxide where 5.0 g contains 4.0 g of molybdenum?"},
    {"qnum": "15", "specRef": "3.1.3", "marks": 1, "stem": "What type of interaction forms in AsH3 + H+ -> AsH4+?"},
    {"qnum": "16", "specRef": "3.2.3", "marks": 1, "stem": "Which is a correct trend down Group 7 from fluorine to iodine?"},
    {"qnum": "17", "specRef": "3.1.1", "marks": 1, "stem": "Which of these ions (S2-, Cl-, K+, Ca2+) has the largest ionic radius?"},
    {"qnum": "18", "specRef": "3.2.3", "marks": 1, "stem": "Which statement about halide ions as reducing agents is correct?"},
    {"qnum": "19", "specRef": "3.1.7", "marks": 1, "stem": "In which of these substances (OF2, H2O, O2, H2O2) is oxygen in the highest oxidation state?"},
    {"qnum": "20", "specRef": "3.2.1", "marks": 1, "stem": "Which block in the Periodic Table contains the element samarium (Sm)?"},
    {"qnum": "21", "specRef": "3.2.3", "marks": 1, "stem": "Which species is not a possible product of the reactions between chlorine and water?"},
    {"qnum": "22", "specRef": "3.2.2", "marks": 1, "stem": "Which statement about magnesium and its compounds is correct?"},
    {"qnum": "23", "specRef": "3.1.3", "marks": 1, "stem": "Which is not responsible for conducting electricity?"},
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

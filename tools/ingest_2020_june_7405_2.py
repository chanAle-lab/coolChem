"""Ingest AQA A-level Chemistry June 2020 Paper 2 (7405/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521589230_ca67b90f.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521589332_a222510c.pdf"
)

PAPER_ID = "2020-june-7405-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2020,
    "series": "June",
    "unit": "7405/2",
    "level": "A-level",
    "date": "2020-06-08",
    "title": "7405/2 — A-level Paper 2: Organic and Physical Chemistry (June 2020)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-fig1.jpg", "page": 2, "x0": 40, "y0": 65, "x1": 555, "y1": 515},
    {"filename": "fig-q1-rate-eq.jpg", "page": 4, "x0": 40, "y0": 340, "x1": 555, "y1": 405},
    {"filename": "fig-q2-fig3.jpg", "page": 6, "x0": 40, "y0": 65, "x1": 555, "y1": 230},
    {"filename": "fig-q3-isomers.jpg", "page": 8, "x0": 40, "y0": 65, "x1": 555, "y1": 280},
    {"filename": "fig-q4-method.jpg", "page": 10, "x0": 40, "y0": 65, "x1": 555, "y1": 320},
    {"filename": "fig-q6-scheme.jpg", "page": 16, "x0": 40, "y0": 65, "x1": 555, "y1": 250},
    {"filename": "fig-q8-fig5.jpg", "page": 22, "x0": 40, "y0": 65, "x1": 555, "y1": 205},
    {"filename": "fig-q9-eq.jpg", "page": 24, "x0": 40, "y0": 65, "x1": 555, "y1": 200},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3, "01.3": 4, "01.4": 4, "01.5": 5, "01.6": 5,
    "02.1": 6, "02.2": 6, "02.3": 6, "02.4": 7,
    "03.1": 8, "03.2": 8, "03.3": 9, "03.4": 9, "03.5": 9, "03.6": 9,
    "04.1": 10, "04.2": 10, "04.3": 10, "04.4": 11, "04.5": 11, "04.6": 12, "04.7": 12, "04.8": 12, "04.9": 12,
    "05.1": 14, "05.2": 14, "05.3": 15,
    "06.1": 16, "06.2": 16, "06.3": 17, "06.4": 17,
    "07.1": 18, "07.2": 20, "07.3": 20, "07.4": 20,
    "08.1": 21, "08.2": 21, "08.3": 22, "08.4": 22,
    "09.1": 23, "09.2": 23, "09.3": 24, "09.4": 24, "09.5": 25, "09.6": 25,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.5", "marks": 3, "stem": "Use Figure 1 to determine the initial rate of reaction and state its units.", "figures": ["fig-q1-fig1.jpg"]},
    {"qnum": "01.2", "specRef": "3.1.9", "marks": 2, "stem": "State the relationship between initial [H2PO2-] and time t in Table 1 and deduce the order."},
    {"qnum": "01.3", "specRef": "RP", "marks": 1, "stem": "Complete Figure 2 to show how hydrogen gas could be collected and measured."},
    {"qnum": "01.4", "specRef": "3.1.9", "marks": 1, "stem": "Deduce the overall effect on the rate when concentrations of both L and M are halved (rate = k[L][M]^2).", "figures": ["fig-q1-rate-eq.jpg"]},
    {"qnum": "01.5", "specRef": "3.1.9", "marks": 3, "stem": "Calculate the concentration of M given rate = 0.0250, [L] = 0.0155, k = 21.3.", "figures": ["fig-q1-rate-eq.jpg"]},
    {"qnum": "01.6", "specRef": "3.1.9", "marks": 1, "stem": "Define the term overall order of reaction."},
    {"qnum": "02.1", "specRef": "3.3.7", "marks": 1, "stem": "Draw a circle around any chiral centre(s) in prilocaine (Figure 3).", "figures": ["fig-q2-fig3.jpg"]},
    {"qnum": "02.2", "specRef": "3.3.1", "marks": 1, "stem": "Identify the functional group(s) in the prilocaine molecule.", "figures": ["fig-q2-fig3.jpg"]},
    {"qnum": "02.3", "specRef": "3.3.9", "marks": 3, "stem": "Draw the structures of the two organic products formed in complete acidic hydrolysis of prilocaine.", "figures": ["fig-q2-fig3.jpg"]},
    {"qnum": "02.4", "specRef": "3.3.12", "marks": 2, "stem": "Explain how a structural feature of the enzyme enables it to hydrolyse isomer G but not isomer F."},
    {"qnum": "03.1", "specRef": "3.3.5", "marks": 2, "stem": "Identify the isomer(s) P-U that react with acidified potassium dichromate(VI) and state the observation.", "figures": ["fig-q3-isomers.jpg"]},
    {"qnum": "03.2", "specRef": "3.3.8", "marks": 2, "stem": "Identify the isomer(s) P-U that react with Tollens' reagent and state the observation.", "figures": ["fig-q3-isomers.jpg"]},
    {"qnum": "03.3", "specRef": "3.3.9", "marks": 3, "stem": "Identify the isomer(s) reacting with ethanoic acid, how to detect reaction, and why NaHCO3(aq) is used.", "figures": ["fig-q3-isomers.jpg"]},
    {"qnum": "03.4", "specRef": "3.3.1", "marks": 1, "stem": "State the type of structural isomerism shown by isomers P, Q, R and S.", "figures": ["fig-q3-isomers.jpg"]},
    {"qnum": "03.5", "specRef": "3.3.16", "marks": 4, "stem": "Describe how infrared spectra (Table A) can be used to distinguish between isomers R, S and T.", "figures": ["fig-q3-isomers.jpg"]},
    {"qnum": "03.6", "specRef": "3.3.16", "marks": 1, "stem": "State why electrospray mass spectrometry is not suitable to distinguish between the isomers.", "figures": ["fig-q3-isomers.jpg"]},
    {"qnum": "04.1", "specRef": "RP", "marks": 2, "stem": "Describe the missing instruction in step 4 of the aspirin synthesis and justify why it is necessary.", "figures": ["fig-q4-method.jpg"]},
    {"qnum": "04.2", "specRef": "RP", "marks": 1, "stem": "Suggest a suitable piece of apparatus to measure out 10 cm3 of ethanoic anhydride in step 5.", "figures": ["fig-q4-method.jpg"]},
    {"qnum": "04.3", "specRef": "RP", "marks": 1, "stem": "Identify a hazard of using concentrated phosphoric acid in step 6.", "figures": ["fig-q4-method.jpg"]},
    {"qnum": "04.4", "specRef": "3.3.9", "marks": 1, "stem": "Complete the equation for the reaction of salicylic acid with ethanoic anhydride to produce aspirin."},
    {"qnum": "04.5", "specRef": "3.1.2", "marks": 5, "stem": "Show which reagent is in excess and calculate the mass of aspirin produced (84.1% yield)."},
    {"qnum": "04.6", "specRef": "RP", "marks": 2, "stem": "Suggest two ways the melting point of crude aspirin would differ from pure aspirin.", "figures": ["fig-q4-method.jpg"]},
    {"qnum": "04.7", "specRef": "RP", "marks": 2, "stem": "Describe two important precautions when heating ethanol and crude aspirin during recrystallisation."},
    {"qnum": "04.8", "specRef": "RP", "marks": 1, "stem": "Explain the purpose of pouring a small amount of cold ethanol through the Buchner funnel."},
    {"qnum": "04.9", "specRef": "RP", "marks": 1, "stem": "Describe one difference in appearance between crude aspirin and purified aspirin."},
    {"qnum": "05.1", "specRef": "3.1.3", "marks": 3, "stem": "Define electronegativity and explain the polarity of the C-Br bond in 2-bromopropane."},
    {"qnum": "05.2", "specRef": "3.3.3", "marks": 4, "stem": "Outline the mechanism for the reaction of 2-bromopropane with an excess of ammonia."},
    {"qnum": "05.3", "specRef": "3.3.11", "marks": 2, "stem": "Draw the skeletal formula of the main organic species formed with a large excess of 2-bromopropane and give a use."},
    {"qnum": "06.1", "specRef": "3.3.10", "marks": 3, "stem": "State the type of reaction, reagent(s), and conditions for step 1 in the synthesis of polystyrene.", "figures": ["fig-q6-scheme.jpg"]},
    {"qnum": "06.2", "specRef": "3.3.8", "marks": 3, "stem": "State the mechanism, inorganic reagent, and organic product name for step 2.", "figures": ["fig-q6-scheme.jpg"]},
    {"qnum": "06.3", "specRef": "3.3.5", "marks": 3, "stem": "Outline the mechanism for step 3 (reaction of step 2 product with concentrated sulfuric acid).", "figures": ["fig-q6-scheme.jpg"]},
    {"qnum": "06.4", "specRef": "3.3.4", "marks": 1, "stem": "Draw the repeating unit of polystyrene."},
    {"qnum": "07.1", "specRef": "3.3.15", "marks": 6, "stem": "State why Si(CH3)4, CCl4 and CDCl3 are used in 1H NMR spectroscopy and explain how their properties make them suitable."},
    {"qnum": "07.2", "specRef": "3.3.15", "marks": 3, "stem": "Deduce the splitting pattern for the H atoms labelled x, y and z in CH3CHClCOCH(CH3)2."},
    {"qnum": "07.3", "specRef": "3.3.15", "marks": 1, "stem": "Suggest why it is difficult to use Table B to predict the chemical shift of H atom y."},
    {"qnum": "07.4", "specRef": "3.3.15", "marks": 2, "stem": "Deduce the structures of two isomers of CH3CHClCOCH(CH3)2 that each have two singlet peaks with integration ratio 2:9."},
    {"qnum": "08.1", "specRef": "3.1.2", "marks": 5, "stem": "Show that the empirical formula of citric acid (H3Y.xH2O) is C3H5O4 from combustion data."},
    {"qnum": "08.2", "specRef": "3.1.2", "marks": 2, "stem": "Show that x = 1 when 3.00 g of H3Y.xH2O (Mr = 210.0) is heated to constant mass leaving 2.74 g H3Y."},
    {"qnum": "08.3", "specRef": "3.3.1", "marks": 1, "stem": "Complete the IUPAC name for H3Y (Figure 5): ___ propane-1,2,3-tricarboxylic acid.", "figures": ["fig-q8-fig5.jpg"]},
    {"qnum": "08.4", "specRef": "3.3.15", "marks": 1, "stem": "State the number of peaks expected in the 13C NMR spectrum for H3Y.", "figures": ["fig-q8-fig5.jpg"]},
    {"qnum": "09.1", "specRef": "3.1.6", "marks": 2, "stem": "Calculate the equilibrium amounts of A and B for A(aq) + 2B(aq) <=> C(aq) given 0.015 mol C."},
    {"qnum": "09.2", "specRef": "3.1.6", "marks": 4, "stem": "Calculate Kc and deduce its units for 0.30 mol A, 0.25 mol B, 0.020 mol C in 350 cm3."},
    {"qnum": "09.3", "specRef": "3.1.6", "marks": 1, "stem": "Suggest why the expression for K for chloroethanal + water can be written without [H2O].", "figures": ["fig-q9-eq.jpg"]},
    {"qnum": "09.4", "specRef": "3.1.6", "marks": 5, "stem": "Calculate the equilibrium concentration of ClCH2CH(OH)2 given 4.71 g chloroethanal in 50.0 cm3 and K = 37.0.", "figures": ["fig-q9-eq.jpg"]},
    {"qnum": "09.5", "specRef": "3.3.8", "marks": 3, "stem": "Complete the nucleophilic addition mechanism in Figure 6 for water reacting with chloroethanal."},
    {"qnum": "09.6", "specRef": "3.3.8", "marks": 3, "stem": "Suggest why the reaction of water with ethanal is slower than with chloroethanal."},
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

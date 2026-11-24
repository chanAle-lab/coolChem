"""Ingest AQA A-level Chemistry June 2021 Paper 3 (7405/3) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521642592_4a5505ae.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521642651_4508b57a.pdf"
)

PAPER_ID = "2021-june-7405-3"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2021,
    "series": "June",
    "unit": "7405/3",
    "level": "A-level",
    "date": "2021-06-01",
    "title": "7405/3 — A-level Paper 3: Synoptic (June 2021)",
    "totalMarks": 90,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q6-fig4.jpg", "page": 16, "x0": 40, "y0": 160, "x1": 555, "y1": 540},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 4, "01.5": 4, "01.6": 4, "01.7": 5, "01.8": 6,
    "02.1": 8, "02.2": 9, "02.3": 9,
    "03.1": 10, "03.2": 11, "03.3": 11,
    "04.1": 12, "04.2": 12,
    "05": 14,
    "06.1": 16, "06.2": 17, "06.3": 17, "06.4": 17, "06.5": 18, "06.6": 18,
    "07": 19, "08": 19,
    "09": 20, "10": 20, "11": 20,
    "12": 21, "13": 21, "14": 21, "15": 21,
    "16": 22, "17": 22, "18": 22,
    "19": 23, "20": 23, "21": 23,
    "22": 24, "23": 24, "24": 24,
    "25": 25, "26": 25, "27": 25,
    "28": 26, "29": 26, "30": 26,
    "31": 27, "32": 27,
    "33": 28, "34": 28,
    "35": 29, "36": 29,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.12", "marks": 2, "stem": "Draw the repeating unit of the polyester formed when ethanedioic acid reacts with propane-1,3-diol."},
    {"qnum": "01.2", "specRef": "3.3.12", "marks": 2, "stem": "Explain why polyesters are biodegradable but polyalkenes are not biodegradable."},
    {"qnum": "01.3", "specRef": "3.1.7", "marks": 4, "stem": "Calculate the concentration, in mol dm-3, of the potassium manganate(VII) solution from the sodium ethanedioate titration."},
    {"qnum": "01.4", "specRef": "RP", "marks": 1, "stem": "On Figure 1, draw the meniscus of the solution when the 25.0 cm3 pipette is ready to transfer."},
    {"qnum": "01.5", "specRef": "RP", "marks": 2, "stem": "Suggest safety precautions, other than eye protection, when filling the burette with KMnO4 and dissolving solid Na2C2O4."},
    {"qnum": "01.6", "specRef": "RP", "marks": 1, "stem": "State the colour change seen at the end point of each titration."},
    {"qnum": "01.7", "specRef": "RP", "marks": 2, "stem": "Give two practical steps needed before recording the initial burette reading in Figure 2."},
    {"qnum": "01.8", "specRef": "3.2.5", "marks": 6, "stem": "Explain why the replacement of water ligands in [Fe(H2O)6]3+ by ethanedioate ions is favourable in terms of enthalpy, entropy, and free-energy changes."},
    {"qnum": "02.1", "specRef": "3.3.13", "marks": 2, "stem": "Use Figure 3 to calculate the Rf value of the unknown amino acid and use Table 1 to identify it."},
    {"qnum": "02.2", "specRef": "3.3.16", "marks": 1, "stem": "State how the amino acids on the TLC plate can be made visible at the end of the experiment."},
    {"qnum": "02.3", "specRef": "3.3.16", "marks": 1, "stem": "State why each amino acid has a different Rf value."},
    {"qnum": "03.1", "specRef": "RP", "marks": 5, "stem": "Describe how the crystalline solid is separated and purified by recrystallisation."},
    {"qnum": "03.2", "specRef": "3.3.8", "marks": 2, "stem": "State the hazard associated with the use of KCN and suggest a reason, other than safety, why KCN is used instead of HCN."},
    {"qnum": "03.3", "specRef": "3.3.8", "marks": 4, "stem": "Outline the mechanism for the reaction of propanone with KCN followed by dilute acid."},
    {"qnum": "04.1", "specRef": "3.2.3", "marks": 2, "stem": "Give an equation for the reaction of solid sodium bromide with concentrated sulfuric acid to form bromine and state one observation."},
    {"qnum": "04.2", "specRef": "3.2.3", "marks": 5, "stem": "Explain the test for chloride and iodide ions using dilute HNO3, AgNO3(aq), and excess dilute NH3(aq), including ionic equations."},
    {"qnum": "05", "specRef": "3.1.12", "marks": 5, "stem": "Calculate the mass, in g, of sodium methanoate (HCOONa) that must be added to 25.0 cm3 of 0.100 mol dm-3 methanoic acid (pKa = 3.75) to produce a pH 4.05 buffer."},
    {"qnum": "06.1", "specRef": "RP", "marks": 2, "stem": "Give two reasons why the apparatus shown in Figure 4 is not safe.", "figures": ["fig-q6-fig4.jpg"]},
    {"qnum": "06.2", "specRef": "3.3.5", "marks": 1, "stem": "Give one additional reagent that is needed to form any propanoic acid from propan-1-ol and K2Cr2O7.", "figures": ["fig-q6-fig4.jpg"]},
    {"qnum": "06.3", "specRef": "RP", "marks": 2, "stem": "State two more mistakes in the way the apparatus is set up in Figure 4.", "figures": ["fig-q6-fig4.jpg"]},
    {"qnum": "06.4", "specRef": "RP", "marks": 1, "stem": "State the purpose of the small glass beads in the flask in Figure 4.", "figures": ["fig-q6-fig4.jpg"]},
    {"qnum": "06.5", "specRef": "3.1.2", "marks": 4, "stem": "State the name of the technique used to separate propanoic acid and calculate the percentage yield from 6.50 g of propan-1-ol forming 3.25 g of propanoic acid."},
    {"qnum": "06.6", "specRef": "3.3.5", "marks": 3, "stem": "State a simple chemical test that distinguishes propanoic acid from propan-1-ol and give one observation with each."},
    {"qnum": "07", "specRef": "3.1.1", "marks": 1, "stem": "Which does not involve the absorption of ultraviolet radiation or visible light?"},
    {"qnum": "08", "specRef": "3.2.5", "marks": 1, "stem": "Which statement about chloride ions is not correct?"},
    {"qnum": "09", "specRef": "3.1.2", "marks": 1, "stem": "What is the mole fraction of 1.0 g of a compound (Mr = 100.0) dissolved in 30.0 g of solvent (Mr = 50.0)?"},
    {"qnum": "10", "specRef": "3.1.1", "marks": 1, "stem": "Which has the electron configuration of a noble gas?"},
    {"qnum": "11", "specRef": "3.3.15", "marks": 1, "stem": "Which statement does not support the suggestion that an unknown organic compound is methyl propanoate?"},
    {"qnum": "12", "specRef": "3.1.3", "marks": 1, "stem": "Which statement about inorganic ionic compounds is always correct?"},
    {"qnum": "13", "specRef": "3.1.3", "marks": 1, "stem": "Which species has a lone pair of electrons on the central atom?"},
    {"qnum": "14", "specRef": "3.1.3", "marks": 1, "stem": "In which substance do covalent bonds break when it melts?"},
    {"qnum": "15", "specRef": "3.3.10", "marks": 1, "stem": "In which molecule are all the atoms in the same plane?"},
    {"qnum": "16", "specRef": "3.1.3", "marks": 1, "stem": "Which molecule has a permanent dipole?"},
    {"qnum": "17", "specRef": "3.3.9", "marks": 1, "stem": "Which statement about (CH3)2CHCH2COOH is correct?"},
    {"qnum": "18", "specRef": "3.1.5", "marks": 1, "stem": "Which statement is correct for a mixture of 2 dm3 of hydrogen and 1 dm3 of oxygen at room temperature?"},
    {"qnum": "19", "specRef": "3.1.5", "marks": 1, "stem": "Which statement about the distribution curve of molecular energies in an ideal gas at a given temperature is correct?"},
    {"qnum": "20", "specRef": "3.1.6", "marks": 1, "stem": "Which statement about the addition of a catalyst to an equilibrium mixture is correct?"},
    {"qnum": "21", "specRef": "3.2.5", "marks": 1, "stem": "Which equation does not show the reduction of a transition metal?"},
    {"qnum": "22", "specRef": "3.1.3", "marks": 1, "stem": "Which substance contains delocalised electrons?"},
    {"qnum": "23", "specRef": "3.3.4", "marks": 1, "stem": "Which compound has E-Z isomers?"},
    {"qnum": "24", "specRef": "3.3.12", "marks": 1, "stem": "Which polymer has hydrogen bonding between the polymer chains?"},
    {"qnum": "25", "specRef": "3.3.2", "marks": 1, "stem": "Which compound needs the greatest amount of oxygen for the complete combustion of 1 mol of the compound?"},
    {"qnum": "26", "specRef": "3.3.5", "marks": 1, "stem": "Which compound is produced when 1-phenylethanol reacts with acidified potassium dichromate(VI)?"},
    {"qnum": "27", "specRef": "3.3.1", "marks": 1, "stem": "Which is the correct general formula for non-cyclic compounds in the homologous series?"},
    {"qnum": "28", "specRef": "3.3.9", "marks": 1, "stem": "Which compound forms a white precipitate when added to aqueous silver nitrate?"},
    {"qnum": "29", "specRef": "3.1.2", "marks": 1, "stem": "What mass, in g, of methyl 3-nitrobenzoate (Mr = 181.0) is produced from 1.70 g of methyl benzoate (Mr = 136.0) at 65.0% yield?"},
    {"qnum": "30", "specRef": "3.3.11", "marks": 1, "stem": "In the two-step preparation bromoethane -> X -> propylamine, what is X?"},
    {"qnum": "31", "specRef": "3.3.9", "marks": 1, "stem": "Which compound reacts with warm dilute aqueous sodium hydroxide?"},
    {"qnum": "32", "specRef": "3.3.11", "marks": 1, "stem": "Which is not a possible product when methylamine reacts with bromoethane by nucleophilic substitution?"},
    {"qnum": "33", "specRef": "3.3.12", "marks": 1, "stem": "Which is the repeating unit of a polyamide?"},
    {"qnum": "34", "specRef": "3.3.12", "marks": 1, "stem": "Which type of polymer is not hydrolysed by heating with concentrated aqueous sodium hydroxide?"},
    {"qnum": "35", "specRef": "3.3.13", "marks": 1, "stem": "Which is the structure of a zwitterion of an amino acid?"},
    {"qnum": "36", "specRef": "3.3.13", "marks": 1, "stem": "Which row shows a pair of bases that can link two strands of DNA with three hydrogen bonds?"},
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

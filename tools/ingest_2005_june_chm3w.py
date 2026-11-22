"""
Ingestion script for 2005 June CHM3/W (Section A only)
Excludes old-spec Section B essay questions (Q5, Q6).
Renders official AQA modern mark scheme tables and precision cropped question images.
"""
import os
import json
import fitz
from PIL import Image
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382980203_a71451e6.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-june-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-june-chm3w",
    "year": 2005,
    "series": "June",
    "date": "2005-06-08",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry"
}

def extract_figures(doc):
    p6 = doc[5]
    rect = fitz.Rect(50, 110, 520, 385)
    pix = p6.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    fig_path = os.path.join(IMG_DIR, "fig-q2-scheme.jpg")
    im.save(fig_path, format="JPEG", quality=92)
    print("Saved fig-q2-scheme.jpg")

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2005-june-chm3w-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Explain what is meant by the term fraction as applied to fractional distillation.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "Compounds / mixtures / hydrocarbons / molecules with a boiling point range / similar boiling point / similar chain length / similar number of carbons", "Insist on 'similar' rather than 'same'; ignore references to size or Mr", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1aii",
        "question": "1(a)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State property of molecules in petroleum allowing mixture to be separated into fractions.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "Molecules have different boiling points / different intermolecular forces / different chain lengths / different sizes", "Ignore references to melting points; credit molecules condense at different temperatures", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1aiii",
        "question": "1(a)(iii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Describe the temperature gradient in the fractionating column.",
        "figures": [],
        "ms_rows": [
            ("1(a)(iii)", "The column has a higher temperature at the base / cooler at the top (or lower temperature at the top)", "Must express temperature difference clearly; penalise unqualified 'gradient'", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1bi",
        "question": "1(b)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Equation for incomplete combustion of C8H18 to produce CO and H2O only.",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "C8H18 + 8½O2 → 8CO + 9H2O\n(or 2C8H18 + 17O2 → 16CO + 18H2O)", "Allow correct multiples", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1bii",
        "question": "1(b)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.1", "3.3.2"],
        "skills": ["recall"],
        "summary": "Draw the structure of 2,2,3-trimethylpentane.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "Correctly drawn structure of 2,2,3-trimethylpentane:\nCH3C(CH3)2CH(CH3)CH2CH3", "Credit displayed or correctly condensed structures; penalise sticks", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2005-june-chm3w-q1c",
        "question": "1(c)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["explanation"],
        "summary": "State one economic reason for cracking petroleum fractions.",
        "figures": [],
        "ms_rows": [
            ("1(c)", "Cracking produces/makes alkenes / ethene / motor fuels / petrol OR makes more useful / higher value products OR satisfies higher demand for smaller molecules", "Ignore 'makes plastics' unqualified; demand must be qualified", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1di",
        "question": "1(d)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Give type of reactive intermediate formed during catalytic cracking.",
        "figures": [],
        "ms_rows": [
            ("1(d)(i)", "Carbocation / carbonium ion (or carbon cation)", "Do not credit examples/formulae alone", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1dii",
        "question": "1(d)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Identify a catalyst used in catalytic cracking.",
        "figures": [],
        "ms_rows": [
            ("1(d)(ii)", "Zeolite / aluminosilicate / Al2O3", "Allow silica / alumina", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1ei",
        "question": "1(e)(i)",
        "marks": 2,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Type of reactive intermediate formed during thermal cracking and how it is formed.",
        "figures": [],
        "ms_rows": [
            ("1(e)(i)", "Reactive intermediate: (Free) radical / alkyl radical", "1 mark; penalise 'radical substitution'", "1", "AO1 / 3.3.2"),
            ("", "How formed: Homolysis / homolytic fission / splitting / C–C or C–H bond breaks", "1 mark for homolytic cleavage", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2005-june-chm3w-q1eii",
        "question": "1(e)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Identify different type of hydrocarbon produced in high percentage by thermal cracking.",
        "figures": [],
        "ms_rows": [
            ("1(e)(ii)", "Alkene(s) / short-chain alkenes", "Penalise cycloalkenes or branched alkanes as contradictions", "1", "AO1 / 3.3.2")
        ]
    },

    # Q2
    {
        "id": "2005-june-chm3w-q2ai",
        "question": "2(a)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "State what is meant by the term electrophile.",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(a)(i)", "Electron pair acceptor / lone pair acceptor / seeks or bonds with an electron pair", "Insist on reference to a pair of electrons", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2005-june-chm3w-q2aii",
        "question": "2(a)(ii)",
        "marks": 4,
        "page": 6,
        "topics": ["3.3.4"],
        "skills": ["analysis"],
        "summary": "Outline mechanism for electrophilic addition of HBr to ethene.",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(a)(ii)", "M1: Curly arrow from middle of C=C bond to H atom of H–Br", "1 mark; arrow must start from C=C bond", "1", "AO2 / 3.3.4"),
            ("", "M2: Curly arrow from H–Br bond to Br atom", "1 mark; penalise formal charges on HBr", "1", "AO2 / 3.3.4"),
            ("", "M3: Correct structure for ethyl carbocation (CH3CH2+)", "1 mark; positive charge on C atom", "1", "AO2 / 3.3.4"),
            ("", "M4: Curly arrow from lone pair on bromide ion (:Br–) to C+ atom", "1 mark; lone pair and negative charge required", "1", "AO2 / 3.3.4")
        ]
    },
    {
        "id": "2005-june-chm3w-q2bi",
        "question": "2(b)(i)",
        "marks": 2,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Identify reagent and catalyst for oxidation of ethene to epoxyethane.",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(b)(i)", "Reagent: Oxygen / O2", "1 mark; do not credit air alone", "1", "AO1 / 3.3.4"),
            ("", "Catalyst: Silver / Ag (or silver-based)", "1 mark; penalise silver nitrate", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2005-june-chm3w-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Draw the structure of epoxyethane.",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(b)(ii)", "Cyclic three-membered ring containing two CH2 groups and one O atom (oxirane triangle)", "Penalise poorly presented C–O bonds", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2005-june-chm3w-q2biii",
        "question": "2(b)(iii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Identify reagent reacting with epoxyethane to form ethane-1,2-diol.",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(b)(iii)", "Water / H2O (or steam / aqueous acid / aqueous alkali)", "Insist that (aq) is included if acid/alkali used", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2005-june-chm3w-q2ci",
        "question": "2(c)(i)",
        "marks": 2,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "Identify reagent for Reaction 2 and name organic product P (bromoethane to nitrile).",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(c)(i)", "Reagent: Potassium cyanide / KCN / NaCN", "1 mark; penalise HCN", "1", "AO1 / 3.3.3"),
            ("", "Product P: Propanenitrile (or propan-1-nitrile)", "1 mark; do not allow propanitrile", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2005-june-chm3w-q2cii",
        "question": "2(c)(ii)",
        "marks": 2,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "Identify reagent for Reaction 5 and name organic product Q (bromoethane to amine).",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(c)(ii)", "Reagent: Ammonia / NH3", "1 mark; ignore conditions but penalise acidic", "1", "AO1 / 3.3.3"),
            ("", "Product Q: Ethylamine (or aminoethane)", "1 mark for name", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2005-june-chm3w-q2ciii",
        "question": "2(c)(iii)",
        "marks": 4,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["analysis"],
        "summary": "Outline mechanism for nucleophilic substitution of bromoethane with ammonia.",
        "figures": ["img/2005-june-chm3w/fig-q2-scheme.jpg"],
        "ms_rows": [
            ("2(c)(iii)", "M1: Curly arrow from lone pair on N of NH3 to C atom of C–Br", "1 mark", "1", "AO2 / 3.3.3"),
            ("", "M2: Curly arrow from C–Br bond to Br atom", "1 mark", "1", "AO2 / 3.3.3"),
            ("", "M3: Correct structure of intermediate ethylammonium ion (CH3CH2NH3+)", "1 mark", "1", "AO2 / 3.3.3"),
            ("", "M4: Curly arrow from one H–N bond to N+ atom", "1 mark", "1", "AO2 / 3.3.3")
        ]
    },

    # Q3
    {
        "id": "2005-june-chm3w-q3a",
        "question": "3(a)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1", "3.3.3"],
        "skills": ["recall"],
        "summary": "Name haloalkane CH3CHBrCH2CH3.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "2-bromobutane", "Must be 2-bromobutane", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2005-june-chm3w-q3b",
        "question": "3(b)",
        "marks": 4,
        "page": 9,
        "topics": ["3.3.3"],
        "skills": ["analysis"],
        "summary": "Name and outline mechanism for base elimination of 2-bromobutane to but-2-ene.",
        "figures": [],
        "ms_rows": [
            ("3(b)", "Name of mechanism: Elimination", "1 mark; penalise 'nucleophilic elimination'", "1", "AO1 / 3.3.3"),
            ("", "M1: Curly arrow from lone pair on OH– to H atom on correct adjacent C–H", "1 mark", "1", "AO2 / 3.3.3"),
            ("", "M2: Curly arrow from adjacent C–H bond to C–C bond to form C=C", "1 mark", "1", "AO2 / 3.3.3"),
            ("", "M3: Curly arrow from C–Br bond to Br atom", "1 mark", "1", "AO2 / 3.3.3")
        ]
    },
    {
        "id": "2005-june-chm3w-q3ci",
        "question": "3(c)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1"],
        "skills": ["recall"],
        "summary": "State what is meant by the term structural isomers.",
        "figures": [],
        "ms_rows": [
            ("3(c)(i)", "(Compounds with the) same molecular formula but different structural formulas (or different displayed formulas / structures)", "Penalise different spatial arrangements (stereoisomerism)", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2005-june-chm3w-q3cii",
        "question": "3(c)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1", "3.3.4"],
        "skills": ["recall"],
        "summary": "Draw the structure of the other alkene isomer formed (but-1-ene).",
        "figures": [],
        "ms_rows": [
            ("3(c)(ii)", "CH2=CH–CH2–CH3  (but-1-ene structure)", "Correct displayed or skeletal/condensed structure", "1", "AO1 / 3.3.1")
        ]
    },

    # Q4
    {
        "id": "2005-june-chm3w-q4ai",
        "question": "4(a)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Equation for fermentation of glucose to form ethanol.",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "C6H12O6 → 2C2H5OH + 2CO2", "Penalise C2H6O once only in question", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2005-june-chm3w-q4aii",
        "question": "4(a)(ii)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Catalyst and equation for dehydration of ethanol to form ethene.",
        "figures": [],
        "ms_rows": [
            ("4(a)(ii)", "Catalyst: Concentrated H2SO4 OR concentrated H3PO4 OR Al2O3", "1 mark; penalise aqueous/dilute acid", "1", "AO1 / 3.3.5"),
            ("", "Equation: C2H5OH → C2H4 + H2O\n(or C2H5OH → H2C=CH2 + H2O)", "1 mark for balanced equation", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2005-june-chm3w-q4b",
        "question": "4(b)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Catalyst and reagent for converting vegetable oil into margarine (hydrogenation).",
        "figures": [],
        "ms_rows": [
            ("4(b)", "Catalyst: Nickel / Ni (or platinum / Pt / palladium / Pd)", "1 mark for metal catalyst", "1", "AO1 / 3.3.4"),
            ("", "Reagent: Hydrogen / H2", "1 mark for hydrogen", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2005-june-chm3w-q4ci",
        "question": "4(c)(i)",
        "marks": 2,
        "page": 11,
        "topics": ["3.3.1"],
        "skills": ["calculation"],
        "summary": "Deduce molecular formula and empirical formula of oleic acid.",
        "figures": [],
        "ms_rows": [
            ("4(c)(i)", "Molecular formula: C18H34O2", "1 mark; only C18H34O2", "1", "AO2 / 3.3.1"),
            ("", "Empirical formula: C9H17O", "1 mark; only C9H17O", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2005-june-chm3w-q4cii",
        "question": "4(c)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "State what is meant by the term unsaturated.",
        "figures": [],
        "ms_rows": [
            ("4(c)(ii)", "Contains (at least) one double bond OR contains C=C", "Must be a positive statement", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2005-june-chm3w-q4ciii",
        "question": "4(c)(iii)",
        "marks": 2,
        "page": 11,
        "topics": ["3.3.4"],
        "skills": ["practical", "observation"],
        "summary": "Reagent and observation for simple chemical test to show oleic acid is unsaturated.",
        "figures": [],
        "ms_rows": [
            ("4(c)(iii)", "Reagent: Bromine water / Br2(aq) / bromine", "1 mark; penalise bromide water", "1", "AO3 / 3.3.4"),
            ("", "Observation: Decolourised / goes colourless (from orange/brown to colourless)", "1 mark; must be 'colourless' not 'clear'", "1", "AO3 / 3.3.4")
        ]
    }
]

def main():
    print("Opening Question Paper PDF...")
    doc_qp = fitz.open(QP_PATH)
    extract_figures(doc_qp)

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Remove existing
    db["questions"] = [q for q in db["questions"] if q.get("paper") != "2005-june-chm3w"]

    for qd in QUESTIONS_DATA:
        qid = qd["id"]
        q_label = qd["question"]
        ms_img_rel = f"img/2005-june-chm3w/ms_{qid.split('-')[-1]}.jpg"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

        answers_list = []
        extra_list = []
        spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.3"
        for r in qd["ms_rows"]:
            prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
            answers_list.append(f"{prefix}{r[1]} ({r[3]})")
            if r[2]:
                extra_list.append(f"{r[2]}")

        answers_html = "<br>".join(answers_list)
        extra_html = "<br>".join(extra_list) if extra_list else "-"

        render_official_markscheme_image(
            question_label=q_label,
            answers_html=answers_html,
            extra_html=extra_html,
            marks=qd["marks"],
            spec_ref=spec_ref,
            output_path=ms_img_abs
        )

        entry = {
            "id": qid,
            "paper": "2005-june-chm3w",
            "question": q_label,
            "marks": qd["marks"],
            "page": qd["page"],
            "topics": qd["topics"],
            "skills": qd["skills"],
            "summary": qd["summary"],
            "image": f"img/2005-june-chm3w/q_{qid.split('-')[-1]}.jpg",
            "figures": qd["figures"],
            "markscheme": ms_img_rel,
            "markscheme_text": "\n".join([f"{r[0]} {r[1]} [{r[3]}]".strip() for r in qd["ms_rows"]])
        }
        db["questions"].append(entry)
        print(f"Processed {qid} ({q_label}) - {qd['marks']} marks")

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully ingested {len(QUESTIONS_DATA)} questions for 2005-june-chm3w!")

if __name__ == "__main__":
    main()

"""
Ingestion script for 2006 June CHM3/W (Section A only)
Excludes old-spec Section B essay question (Q6).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383066769_beac6c3b.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-june-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

# Extract figures
doc = fitz.open(QP_PATH)
# fig-q4-table.jpg on page 8 (index 7)
page8 = doc[7]
rect8 = fitz.Rect(70, 100, 510, 415)
pix8 = page8.get_pixmap(clip=rect8, dpi=200)
pix8.save(os.path.join(IMG_DIR, "fig-q4-table.jpg"))

# fig-q5-table.jpg on page 10 (index 9)
page10 = doc[9]
rect10 = fitz.Rect(70, 110, 510, 490)
pix10 = page10.get_pixmap(clip=rect10, dpi=200)
pix10.save(os.path.join(IMG_DIR, "fig-q5-table.jpg"))

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2006-june-chm3w-q1a",
        "question": "1(a)",
        "marks": 3,
        "page": 2,
        "topics": ["3.3.4", "3.3.5"],
        "skills": ["recall"],
        "summary": "State type of reaction, equation, and catalyst for conversion of ethene to ethanol.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "Type of reaction: Hydration OR (electrophilic) addition<br><br>Equation: H<sub>2</sub>C=CH<sub>2</sub> + H<sub>2</sub>O → CH<sub>3</sub>CH<sub>2</sub>OH<br><br>Catalyst: conc. H<sub>2</sub>SO<sub>4</sub> OR conc. H<sub>3</sub>PO<sub>4</sub>", "1 mark for hydration / electrophilic addition [penalise 'nucleophilic addition'; credit 'direct hydration' / 'steam hydration']<br>1 mark for equation [credit C<sub>2</sub>H<sub>5</sub>OH and C<sub>2</sub>H<sub>4</sub>]<br>1 mark for conc. H<sub>2</sub>SO<sub>4</sub> or conc. H<sub>3</sub>PO<sub>4</sub>", "3", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2006-june-chm3w-q1bi",
        "question": "1(b)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2", "3.3.5"],
        "skills": ["recall"],
        "summary": "Identify the solid product formed when ethanol burns in a limited supply of oxygen.",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "Carbon OR C (credit 'soot' or 'sooty')", "Penalise 'coke' or 'coal'; credit 'carbon + carbon monoxide' provided it is clear carbon is solid", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2006-june-chm3w-q1bii",
        "question": "1(b)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2", "3.3.5"],
        "skills": ["recall"],
        "summary": "Write an equation for the incomplete combustion of ethanol to form carbon.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "CH<sub>3</sub>CH<sub>2</sub>OH + O<sub>2</sub> → 2C + 3H<sub>2</sub>O<br>OR CH<sub>3</sub>CH<sub>2</sub>OH + 1½O<sub>2</sub> → C + CO + 3H<sub>2</sub>O", "Credit multiples of these equations; credit C<sub>2</sub>H<sub>5</sub>OH", "1", "AO1 / 3.3.2")
        ]
    },
    # Q2
    {
        "id": "2006-june-chm3w-q2a",
        "question": "2(a)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2", "3.3.4"],
        "skills": ["recall"],
        "summary": "Write an equation for the cracking of ethane into ethene and hydrogen.",
        "figures": [],
        "ms_rows": [
            ("2(a)", "CH<sub>3</sub>CH<sub>3</sub> → H<sub>2</sub>C=CH<sub>2</sub> + H<sub>2</sub>", "Credit C<sub>2</sub>H<sub>6</sub> → C<sub>2</sub>H<sub>4</sub> + H<sub>2</sub>", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2006-june-chm3w-q2bi",
        "question": "2(b)(i)",
        "marks": 3,
        "page": 5,
        "topics": ["3.3.3", "3.3.4"],
        "skills": ["mechanism"],
        "summary": "Outline the mechanism for the elimination of HBr from bromoethane by hydroxide ions.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "M1: Curly arrow from lone pair on oxygen of :OH<sup>-</sup> to H of CH<sub>3</sub> group<br><br>M2: Curly arrow from middle of C-H bond to middle of C-C bond<br><br>M3: Curly arrow from middle of C-Br bond to Br atom", "M1: Insist on lone pair on O and negative charge; attack to correct H atom<br>M2: Arrow from C-H bond to C-C bond<br>M3: Arrow from C-Br bond to Br<br>[Credit full marks for E1 mechanism]", "3", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.3", "3.3.4"],
        "skills": ["evaluation"],
        "summary": "Suggest why this elimination reaction is not used commercially to make ethene.",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "Bromoethane is made from ethene OR bromoethane is expensive / not readily available OR poor yield / reaction is too slow OR substitution competes to form ethanol", "Any 1 valid commercial reason", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q2ci",
        "question": "2(c)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.4", "3.3.12"],
        "skills": ["recall"],
        "summary": "Identify the type of polymerisation when chloroethene forms poly(chloroethene).",
        "figures": [],
        "ms_rows": [
            ("2(c)(i)", "Addition (polymerisation)", "Accept 'addition'", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2006-june-chm3w-q2cii",
        "question": "2(c)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.3.4", "3.3.12"],
        "skills": ["application"],
        "summary": "Draw a repeating unit of poly(chloroethene) and identify an environmental problem with disposal by combustion.",
        "figures": [],
        "ms_rows": [
            ("2(c)(ii)", "Repeating unit: -[CH<sub>2</sub>-CH(Cl)]-<br><br>Environmental problem: Toxic fumes / toxic gases / toxic combustion products / HCl produced / dioxins produced / acid rain", "1 mark for correct repeating unit with trailing bonds<br>1 mark for toxic fumes / HCl / acid rain [penalise CO2 / greenhouse effect / non-biodegradable]", "2", "AO1 / 3.3.4")
        ]
    },
    # Q3
    {
        "id": "2006-june-chm3w-q3ai",
        "question": "3(a)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.3"],
        "skills": ["nomenclature"],
        "summary": "Give the IUPAC name for compound Q (CH3CH2CH2Br).",
        "figures": [],
        "ms_rows": [
            ("3(a)(i)", "1-bromopropane", "Credit 1-bromopropane only", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q3aii",
        "question": "3(a)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "Identify the nucleophile in Reaction 1 (Q to propan-1-ol).",
        "figures": [],
        "ms_rows": [
            ("3(a)(ii)", "Hydroxide ion OR :OH<sup>-</sup>", "Credit OH<sup>-</sup> or hydroxide [penalise OH without negative charge]", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q3aiii",
        "question": "3(a)(iii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.3"],
        "skills": ["application"],
        "summary": "Draw the structure of compound R (propyl ethanedioate / ester).",
        "figures": [],
        "ms_rows": [
            ("3(a)(iii)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OOC-COOCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub><br>(dipropyl ethanedioate)", "Correct displayed / structural formula showing both ester groups", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm3w-q3aiv",
        "question": "3(a)(iv)",
        "marks": 2,
        "page": 6,
        "topics": ["3.3.5", "3.3.8"],
        "skills": ["application"],
        "summary": "Identify reagents and conditions for the oxidation of propan-1-ol to propanal.",
        "figures": [],
        "ms_rows": [
            ("3(a)(iv)", "Reagents: Acidified potassium dichromate(VI) (or K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> / H<sub>2</sub>SO<sub>4</sub>)<br><br>Conditions: Distillation (immediately as formed)", "1 mark for K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> and acid (H<sub>2</sub>SO<sub>4</sub> / H<sup>+</sup>)<br>1 mark for distillation / warm and distill", "2", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2006-june-chm3w-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "Identify the reagent in Reaction 4 (Q to propylamine).",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "Ammonia OR NH<sub>3</sub> (in excess / ethanolic)", "Accept ammonia / NH<sub>3</sub>", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q3bii",
        "question": "3(b)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.3", "3.3.11"],
        "skills": ["application"],
        "summary": "Draw the structure of a secondary amine formed as a by-product in Reaction 4.",
        "figures": [],
        "ms_rows": [
            ("3(b)(ii)", "(CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>)<sub>2</sub>NH (dipropylamine)", "Allow (C<sub>3</sub>H<sub>7</sub>)<sub>2</sub>NH or full displayed structure", "1", "AO1 / 3.3.11")
        ]
    },
    {
        "id": "2006-june-chm3w-q3c",
        "question": "3(c)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "Identify the reagent and condition in Reaction 5 (Q to propene).",
        "figures": [],
        "ms_rows": [
            ("3(c)", "Ethanolic / alcoholic potassium hydroxide (KOH / NaOH in ethanol) and heat / reflux", "Credit 'KOH in ethanol' or 'ethanolic NaOH'", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q3di",
        "question": "3(d)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["classification"],
        "summary": "State the classification of halogenoalkane Q (1-bromopropane).",
        "figures": [],
        "ms_rows": [
            ("3(d)(i)", "Primary (or 1°)", "Credit primary or 1°", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q3dii",
        "question": "3(d)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["application"],
        "summary": "Draw the structure of an isomer of Q that is a secondary halogenoalkane.",
        "figures": [],
        "ms_rows": [
            ("3(d)(ii)", "CH<sub>3</sub>CH(Br)CH<sub>3</sub> (2-bromopropane)", "Correct displayed or structural formula", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm3w-q3diii",
        "question": "3(d)(iii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "State the type of isomerism shown by these two halogenoalkanes.",
        "figures": [],
        "ms_rows": [
            ("3(d)(iii)", "Position (isomerism) / positional", "Credit position or positional [credit structural isomerism as a second choice]", "1", "AO1 / 3.3.1")
        ]
    },
    # Q4
    {
        "id": "2006-june-chm3w-q4ai",
        "question": "4(a)(i)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.1"],
        "skills": ["recall"],
        "summary": "Explain what is meant by the term structural isomers.",
        "figures": ["img/2006-june-chm3w/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(a)(i)", "Compounds / molecules with the same molecular formula<br><br>But different structural formula / different structures / different arrangement of atoms", "1 mark for same molecular formula<br>1 mark for different structural formula / different structures [penalise 'different general formula' / 'different empirical formula']", "2", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2006-june-chm3w-q4aii",
        "question": "4(a)(ii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Complete the table to show the molecular formula of isomers C and D.",
        "figures": ["img/2006-june-chm3w/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(a)(ii)", "C<sub>3</sub>H<sub>6</sub>O", "Credit C<sub>3</sub>H<sub>6</sub>O only", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2006-june-chm3w-q4aiii",
        "question": "4(a)(iii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Give the empirical formula of isomers E and F.",
        "figures": ["img/2006-june-chm3w/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(a)(iii)", "CH<sub>2</sub>", "Credit CH<sub>2</sub> only", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2006-june-chm3w-q4b",
        "question": "4(b)",
        "marks": 3,
        "page": 8,
        "topics": ["3.3.5", "3.3.6"],
        "skills": ["practical"],
        "summary": "Identify a chemical test and observations to distinguish between isomer A (2-methylpropan-2-ol) and isomer B (butan-1-ol).",
        "figures": ["img/2006-june-chm3w/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(b)", "Test reagent: Acidified potassium dichromate(VI) (K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> / H<sub>2</sub>SO<sub>4</sub>)<br><br>Observation with isomer A: No change / remains orange<br><br>Observation with isomer B: Colour change from orange to green", "1 mark for acidified potassium dichromate(VI)<br>1 mark for no reaction / orange with A (tertiary alcohol)<br>1 mark for turns green with B (primary alcohol)", "3", "AO1 / 3.3.6")
        ]
    },
    {
        "id": "2006-june-chm3w-q4c",
        "question": "4(c)",
        "marks": 3,
        "page": 9,
        "topics": ["3.3.6", "3.3.8"],
        "skills": ["practical"],
        "summary": "Identify a chemical test and observations to distinguish between isomer C (propanal) and isomer D (propanone).",
        "figures": ["img/2006-june-chm3w/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(c)", "Test reagent: Tollens' reagent (or Fehling's solution)<br><br>Observation with isomer C: Silver mirror / black precipitate (Fehling's: red precipitate)<br><br>Observation with isomer D: No change / no reaction / colourless (Fehling's: remains blue)", "1 mark for Tollens' reagent / Fehling's<br>1 mark for silver mirror / red ppt with C (aldehyde)<br>1 mark for no change / no reaction with D (ketone)", "3", "AO1 / 3.3.6")
        ]
    },
    {
        "id": "2006-june-chm3w-q4d",
        "question": "4(d)",
        "marks": 3,
        "page": 9,
        "topics": ["3.3.4", "3.3.6"],
        "skills": ["practical"],
        "summary": "Identify a chemical test and observations to distinguish between isomer E (cyclohexane) and isomer F (hex-3-ene).",
        "figures": ["img/2006-june-chm3w/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(d)", "Test reagent: Bromine water (Br<sub>2</sub>(aq))<br><br>Observation with isomer E: No change / remains orange/brown/yellow<br><br>Observation with isomer F: Decolourised / goes colourless", "1 mark for bromine water / Br<sub>2</sub><br>1 mark for no change with E (alkane/cycloalkane)<br>1 mark for decolourised with F (alkene)", "3", "AO1 / 3.3.6")
        ]
    },
    # Q5
    {
        "id": "2006-june-chm3w-q5ai",
        "question": "5(a)(i)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.8"],
        "skills": ["nomenclature", "application"],
        "summary": "Complete the table by giving the IUPAC name for 3-methylbutanal and drawing the structure of pentan-2-one.",
        "figures": ["img/2006-june-chm3w/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(a)(i)", "Name of aldehyde: 3-methylbutanal<br><br>Structure of ketone: CH<sub>3</sub>COCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (or displayed)", "1 mark for 3-methylbutanal<br>1 mark for pentan-2-one structure", "2", "AO1 / 3.3.8")
        ]
    },
    {
        "id": "2006-june-chm3w-q5aii",
        "question": "5(a)(ii)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.8"],
        "skills": ["application"],
        "summary": "Draw the structures of the two other isomeric carbonyl compounds with molecular formula C5H10O (one aldehyde and one ketone).",
        "figures": ["img/2006-june-chm3w/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(a)(ii)", "Isomeric aldehyde: (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>CHO (or 2-methylbutanal / 2,2-dimethylpropanal if not in table)<br><br>Isomeric ketone: CH<sub>3</sub>CH<sub>2</sub>COCH<sub>2</sub>CH<sub>3</sub> (pentan-3-one) OR CH<sub>3</sub>COCH(CH<sub>3</sub>)<sub>2</sub> (3-methylbutan-2-one)", "1 mark for correct missing aldehyde<br>1 mark for correct missing ketone", "2", "AO1 / 3.3.8")
        ]
    },
    {
        "id": "2006-june-chm3w-q5bi",
        "question": "5(b)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.8", "3.3.9"],
        "skills": ["recall"],
        "summary": "Write an equation for the oxidation of pentanal to pentanoic acid using [O].",
        "figures": ["img/2006-june-chm3w/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(b)(i)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CHO + [O] → CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>COOH", "Accept C<sub>4</sub>H<sub>9</sub>CHO + [O] → C<sub>4</sub>H<sub>9</sub>COOH; insist on balanced equation", "1", "AO1 / 3.3.8")
        ]
    },
    {
        "id": "2006-june-chm3w-q5bii",
        "question": "5(b)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.8", "3.3.9"],
        "skills": ["nomenclature"],
        "summary": "Give the IUPAC name for the carboxylic acid formed by the oxidation of pentanal.",
        "figures": ["img/2006-june-chm3w/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(b)(ii)", "Pentanoic acid", "Credit pentanoic acid (or pentan-1-oic acid)", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm3w-q5ci",
        "question": "5(c)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.5", "3.3.8"],
        "skills": ["application"],
        "summary": "Identify the alcohol formed by the reduction of pentanal.",
        "figures": ["img/2006-june-chm3w/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(c)(i)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH OR pentan-1-ol", "Credit pentan-1-ol or correct structural formula", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2006-june-chm3w-q5cii",
        "question": "5(c)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.5", "3.3.8"],
        "skills": ["classification"],
        "summary": "State the class of alcohol formed by the reduction of pentanal.",
        "figures": ["img/2006-june-chm3w/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(c)(ii)", "Primary (or 1°)", "Credit primary or 1°", "1", "AO1 / 3.3.5")
        ]
    }
]

paper_id = "2006-june-chm3w"
new_questions = []

for qd in QUESTIONS_DATA:
    qid = qd["id"]
    q_label = qd["question"]
    ms_img_rel = f"img/{paper_id}/ms_{qid.split('-')[-1]}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

    answers_list = []
    extra_list = []
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.3.1"
    for r in qd["ms_rows"]:
        prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
        answers_list.append(f"{prefix}{r[1]} ({r[3]})")
        if r[2]:
            extra_list.append(f"{r[2]}")

    answers_html = "<br><br>".join(answers_list)
    extra_html = "<br><br>".join(extra_list) if extra_list else "-"

    render_official_markscheme_image(
        question_label=q_label,
        answers_html=answers_html,
        extra_html=extra_html,
        marks=qd["marks"],
        spec_ref=spec_ref,
        output_path=ms_img_abs
    )

    q_obj = {
        "id": qid,
        "paper": paper_id,
        "question": q_label,
        "marks": qd["marks"],
        "page": qd["page"],
        "topics": qd["topics"],
        "skills": qd["skills"],
        "summary": qd["summary"],
        "question_text": qd["summary"],
        "markscheme_text": "Official AQA mark scheme table",
        "image": f"img/{paper_id}/{qid}.jpg",
        "figures": qd["figures"],
        "markscheme": [ms_img_rel]
    }
    new_questions.append(q_obj)

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    db = json.load(f)

db["questions"] = [q for q in db["questions"] if q.get("paper") != paper_id]
db["questions"].extend(new_questions)

with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully ingested {len(new_questions)} questions for {paper_id}. Total marks: {sum(q['marks'] for q in new_questions)}")

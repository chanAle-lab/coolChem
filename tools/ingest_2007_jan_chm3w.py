"""
Ingestion script for 2007 January CHM3/W (Section A only)
Excludes old-spec Section B essay questions (Q6, Q7).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795469473822_32602c73.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-jan-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

# Extract fig-q3-table.jpg (isomeric alkenes table on page 6)
doc = fitz.open(QP_PATH)
page6 = doc[5]
rect = fitz.Rect(95, 110, 495, 315)
pix = page6.get_pixmap(clip=rect, dpi=200)
pix.save(os.path.join(IMG_DIR, "fig-q3-table.jpg"))

PAPER_OBJ = {
    "id": "2007-jan-chm3w",
    "year": 2007,
    "series": "January",
    "date": "2007-01-11",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2007-jan-chm3w-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State in which part of a fractionating column the temperature is highest.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "At the bottom OR lower levels", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q1aii",
        "question": "1(a)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State in which part of a fractionating column hydrocarbons with lower molecular masses condense.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "At the top OR higher levels", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q1bi",
        "question": "1(b)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["explanation"],
        "summary": "State why a high temperature is needed for the thermal cracking of alkanes.",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "To break (strong C–C) bonds &nbsp;OR&nbsp; homolytic fission", "QoL<br>(ignore free-radical substitution)<br>(ignore overcoming Van der Waals forces as additional information)", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q1bii",
        "question": "1(b)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Give the general formula for alkenes.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "C<sub>n</sub>H<sub>2n</sub> only", "-", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2007-jan-chm3w-q1biii",
        "question": "1(b)(iii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["application"],
        "summary": "Write an equation for the thermal cracking of C13H28 to give ethene and propene in a 2:1 ratio and an alkane.",
        "figures": [],
        "ms_rows": [
            ("1(b)(iii)", "C<sub>13</sub>H<sub>28</sub> &rarr; C<sub>6</sub>H<sub>14</sub> + 2C<sub>2</sub>H<sub>4</sub> + C<sub>3</sub>H<sub>6</sub><br><br>M1: correct alkene formulae (1)<br>M2: balanced equation (1)", "(accept ethene formula written as CH<sub>2</sub>CH<sub>2</sub>, CH<sub>2</sub>=CH<sub>2</sub>, H<sub>2</sub>C=CH<sub>2</sub> and similar for propene, but penalise M1 if either is incorrect e.g. CH<sub>2</sub>·CH<sub>2</sub>)<br>(accept CH<sub>3</sub>(CH<sub>2</sub>)<sub>4</sub>CH<sub>3</sub> for hexane) (ignore conditions)", "2", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q1biv",
        "question": "1(b)(iv)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "Draw the structure of the repeating unit of poly(propene).",
        "figures": [],
        "ms_rows": [
            ("1(b)(iv)", "Correct structure of repeating unit: –[CH<sub>2</sub>–CH(CH<sub>3</sub>)]–", "(ignore brackets) (ignore 'n') (be lenient on vertical C–C bond in the structure)", "1", "AO1 / 3.3.4")
        ]
    },
    # Q2
    {
        "id": "2007-jan-chm3w-q2ai",
        "question": "2(a)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["application"],
        "summary": "Write an equation for the complete combustion of pentane, C5H12.",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "C<sub>5</sub>H<sub>12</sub> + 8O<sub>2</sub> &rarr; 5CO<sub>2</sub> + 6H<sub>2</sub>O", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q2aii",
        "question": "2(a)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Identify a solid pollutant formed when pentane undergoes incomplete combustion.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "Carbon OR C OR soot(y deposits)", "(penalise \"coke\" OR \"charcoal\")", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q2aiii",
        "question": "2(a)(iii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Give one reason why sulphur dioxide gas may be found in the exhaust gases of cars.",
        "figures": [],
        "ms_rows": [
            ("2(a)(iii)", "Petrol(eum) / Fuel / hydrocarbon mixture / (alkane) fraction has sulphur (-containing impurities which burn)", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q2aiv",
        "question": "2(a)(iv)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Give one reason why sulphur dioxide is considered to be a pollutant.",
        "figures": [],
        "ms_rows": [
            ("2(a)(iv)", "(Causes) acid rain or wtte &nbsp;OR&nbsp; toxic OR corrosive OR irritant", "(penalise formation of acid / H<sub>2</sub>SO<sub>3</sub> / H<sub>2</sub>SO<sub>4</sub> alone)<br>(penalise \"harmful\" alone)", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-jan-chm3w-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "State what is meant by the term hydration.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "The addition of water / H<sub>2</sub>O", "QoL", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-jan-chm3w-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "Write an equation for the hydration of ethene.",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "C<sub>2</sub>H<sub>4</sub> + H<sub>2</sub>O &rarr; CH<sub>3</sub>CH<sub>2</sub>OH", "(accept ethene formula written as CH<sub>2</sub>CH<sub>2</sub>, CH<sub>2</sub>=CH<sub>2</sub>, H<sub>2</sub>C=CH<sub>2</sub>)<br>(accept ethanol formula written as C<sub>2</sub>H<sub>5</sub>OH in every case)<br>(penalise C<sub>2</sub>H<sub>6</sub>O once only)<br>(ignore H<sub>3</sub>PO<sub>4</sub>/H<sub>2</sub>SO<sub>4</sub> on both sides of equation)", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-jan-chm3w-q2biii",
        "question": "2(b)(iii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Write an equation for the formation of ethanol from glucose, C6H12O6.",
        "figures": [],
        "ms_rows": [
            ("2(b)(iii)", "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> &rarr; 2CH<sub>3</sub>CH<sub>2</sub>OH + 2CO<sub>2</sub>", "(possible RE for ethanol formula)", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-jan-chm3w-q2biv",
        "question": "2(b)(iv)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "Write an equation for the incomplete combustion of ethanol to produce carbon monoxide and water only.",
        "figures": [],
        "ms_rows": [
            ("2(b)(iv)", "CH<sub>3</sub>CH<sub>2</sub>OH + 2O<sub>2</sub> &rarr; 2CO + 3H<sub>2</sub>O", "(possible RE for ethanol formula)", "1", "AO2 / 3.3.5")
        ]
    },
    # Q3
    {
        "id": "2007-jan-chm3w-q3a",
        "question": "3(a)",
        "marks": 2,
        "page": 6,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Name Isomer 1 and Isomer 2 from the table of C4H8 alkenes.",
        "figures": ["img/2007-jan-chm3w/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(a)", "Isomer 1: <b>but-1-ene</b> (1)<br>Isomer 2: <b>(2-)methylpropene</b> (1)", "(credit \"methylprop-1-ene\")<br>(penalise methylpropanene and methylprop-2-ene)", "2", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-jan-chm3w-q3bi",
        "question": "3(b)(i)",
        "marks": 2,
        "page": 6,
        "topics": ["3.3.1"],
        "skills": ["recall"],
        "summary": "State what is meant by the term stereoisomers.",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "M1: Compounds with the same structural formula (1)<br>M2: but different arrangements of atoms/bonds/groups in space OR different spatial arrangements/orientations of atoms/bonds/groups (1)", "(ignore \"same M<sub>r</sub>, same molecular formula, same empirical formula, same displayed formula\", but penalise M1 if any of these is stated to be different)", "2", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-jan-chm3w-q3bii",
        "question": "3(b)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "From the table, identify two isomers which are stereoisomers.",
        "figures": ["img/2007-jan-chm3w/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(b)(ii)", "Isomer 3 <u>and</u> isomer 4", "(credit correct names OR formulas)", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-jan-chm3w-q3c",
        "question": "3(c)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "From the table, identify the isomer which is a chain isomer of Isomer 1.",
        "figures": ["img/2007-jan-chm3w/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(c)", "Isomer 2", "(credit correct name OR formula)", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-jan-chm3w-q3d",
        "question": "3(d)",
        "marks": 5,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "Name and outline a mechanism for the reaction of Isomer 2 (methylpropene) with concentrated sulphuric acid to form compound W.",
        "figures": [],
        "ms_rows": [
            ("3(d)", "<b>Electrophilic addition</b> (both words required) (1)<br><br>M1: curly arrow from C=C bond towards/alongside the side of H atom on H–OSO<sub>2</sub>OH OR H–OSO<sub>3</sub>H (1)<br>M2: curly arrow from H–O bond towards/alongside the side of the O atom on H–OSO<sub>2</sub>OH (1)<br>M3: correct structure of the carbocation (CH<sub>3</sub>)<sub>3</sub>C<sup>+</sup> (1)<br>M4: curly arrow from lone pair on an individual oxygen atom of hydrogensulphate ion towards/alongside C atom bearing the positive charge (1)", "(penalise M1 if arrow to H<sub>2</sub>SO<sub>4</sub> OR to formal charge on H of H–O bond; credit M1 and M2 if correct curly arrow to H<sup>+</sup> provided the anion is present)<br>(penalise use of 'sticks' in M3)<br>(insist that the anion has the correct formula with a lone pair of electrons and a negative charge)<br>(Award a maximum of 3 marks for use of wrong alkene)", "5", "AO2 / 3.3.4")
        ]
    },
    {
        "id": "2007-jan-chm3w-q3ei",
        "question": "3(e)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "Complete the equation for the reaction of compound W with water.",
        "figures": [],
        "ms_rows": [
            ("3(e)(i)", "Correct structure of 2-methylpropan-2-ol and H<sub>2</sub>SO<sub>4</sub> in the equation", "(be lenient on the vertical bond in the alcohol, but penalise if C–H–O is clearly drawn)", "1", "AO2 / 3.3.4")
        ]
    },
    {
        "id": "2007-jan-chm3w-q3eii",
        "question": "3(e)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "Name the alcohol produced when compound W reacts with water.",
        "figures": [],
        "ms_rows": [
            ("3(e)(ii)", "(2-)methylpropan-2-ol", "-", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2007-jan-chm3w-q3f",
        "question": "3(f)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "State the overall role of the sulphuric acid in the conversion of Isomer 2 into 2-methylpropan-2-ol.",
        "figures": [],
        "ms_rows": [
            ("3(f)", "(acid) catalyst", "(ignore \"homogeneous\" and \"heterogeneous\")", "1", "AO1 / 3.3.4")
        ]
    },
    # Q4
    {
        "id": "2007-jan-chm3w-q4ai",
        "question": "4(a)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "Balance the equation for the oxidation of ethane-1,2-diol to ethanedioic acid.",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "4[O] <u>and</u> 2H<sub>2</sub>O", "-", "1", "AO2 / 3.3.5")
        ]
    },
    {
        "id": "2007-jan-chm3w-q4aii",
        "question": "4(a)(ii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "Draw the structure of the intermediate compound with only aldehyde functional groups and empirical formula CHO.",
        "figures": [],
        "ms_rows": [
            ("4(a)(ii)", "OHC–CHO", "(insist on CHO groups drawn out)", "1", "AO2 / 3.3.5")
        ]
    },
    {
        "id": "2007-jan-chm3w-q4bi",
        "question": "4(b)(i)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.3", "3.3.4"],
        "skills": ["recall"],
        "summary": "State the type of mechanism in Reaction 1 (ethene + Br2) and Reaction 2 (BrCH2CH2Br + NaOH(aq)).",
        "figures": [],
        "ms_rows": [
            ("4(b)(i)", "Reaction 1 is <b>electrophilic addition</b> (1)<br>Reaction 2 is <b>nucleophilic substitution</b> (1)", "(in both cases, both words are required)", "2", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2007-jan-chm3w-q4bii",
        "question": "4(b)(ii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Name compound X (from ethene + O2/Ag) and state the type of reaction in Reaction 4 (X + H2O -> ethane-1,2-diol).",
        "figures": [],
        "ms_rows": [
            ("4(b)(ii)", "Compound X is <b>epoxyethane</b> (1)<br>Reaction 4 is <b>hydrolysis</b> OR <b>hydration</b> OR <b>(nucleophilic) addition</b> (1)", "(penalise \"electrophilic\" OR \"free-radical addition\")", "2", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2007-jan-chm3w-q4biii",
        "question": "4(b)(iii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.3.3"],
        "skills": ["application"],
        "summary": "Complete and balance the equation for BrCH2CH2Br + excess NH3 -> product (Mr = 60.0).",
        "figures": [],
        "ms_rows": [
            ("4(b)(iii)", "M1: Formula for H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> (1)<br>M2: Balanced equation with <b>4NH<sub>3</sub></b> and <b>2NH<sub>4</sub>Br</b> (1)", "(accept NH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> or CH<sub>2</sub>(NH<sub>2</sub>)CH<sub>2</sub>(NH<sub>2</sub>) for M1 with or without brackets)<br>(accept NH<sub>4</sub><sup>+</sup>Br<sup>-</sup>) (do not accept equations with HBr)<br>(award M2 if equation balanced with for example, C<sub>2</sub>H<sub>8</sub>N<sub>2</sub>)", "2", "AO2 / 3.3.3")
        ]
    },
    # Q5
    {
        "id": "2007-jan-chm3w-q5ai",
        "question": "5(a)(i)",
        "marks": 3,
        "page": 10,
        "topics": ["3.3.3"],
        "skills": ["application"],
        "summary": "Outline the initiation and propagation steps for the free-radical substitution of CH3F with F2 to form CH2F2.",
        "figures": [],
        "ms_rows": [
            ("5(a)(i)", "Initiation: F<sub>2</sub> &rarr; 2F· (1)<br>First propagation: CH<sub>3</sub>F + F· &rarr; ·CH<sub>2</sub>F + HF (1)<br>Second propagation: ·CH<sub>2</sub>F + F<sub>2</sub> &rarr; CH<sub>2</sub>F<sub>2</sub> + F· (1)", "(credit correct half arrows, but penalise double headed arrows)<br>(penalise Fl once only) (penalise the absence of dots once only)<br>(accept CH<sub>2</sub>F·)", "3", "AO2 / 3.3.3")
        ]
    },
    {
        "id": "2007-jan-chm3w-q5aii",
        "question": "5(a)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.3"],
        "skills": ["application"],
        "summary": "Write the overall equation for the reaction of fluorine with ethane to form pentafluoroethane, CF3CHF2.",
        "figures": [],
        "ms_rows": [
            ("5(a)(ii)", "C<sub>2</sub>H<sub>6</sub> + 5F<sub>2</sub> &rarr; CF<sub>3</sub>CHF<sub>2</sub> + 5HF", "(penalise if any radicals appear in this equation) (accept C<sub>2</sub>F<sub>5</sub>H in equation)", "1", "AO2 / 3.3.3")
        ]
    },
    {
        "id": "2007-jan-chm3w-q5bi",
        "question": "5(b)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "Write the formula for dichlorodifluoromethane (R12).",
        "figures": [],
        "ms_rows": [
            ("5(b)(i)", "CCl<sub>2</sub>F<sub>2</sub> OR CF<sub>2</sub>Cl<sub>2</sub> OR structure drawn out", "-", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2007-jan-chm3w-q5bii",
        "question": "5(b)(ii)",
        "marks": 3,
        "page": 10,
        "topics": ["3.1.2", "3.3.3"],
        "skills": ["calculation"],
        "summary": "Calculate the empirical formula of R13 given 11.5% C, 34.0% Cl, and the remainder F.",
        "figures": [],
        "ms_rows": [
            ("5(b)(ii)", "M1: % F = 54.5 (1)<br>M2: mol C = 11.5/12.0 and mol Cl = 34.0/35.5 (mol F = 54.5/19.0) (1)<br>M3: Ratio 0.958 : 0.958 : 2.87 OR 1 : 1 : 3 and <b>CClF<sub>3</sub></b> (1)", "(correct answer gains full credit)<br>(award a maximum of 2 marks for consistent use of atomic number rather than A<sub>r</sub>, since this leads to approximately the correct answer)<br>(penalise M2 for incorrect A<sub>r</sub> e.g. 35 for Cl)", "3", "AO2 / 3.1.2")
        ]
    }
]

paper_id = PAPER_OBJ["id"]
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
        if r[2] and r[2] != "-":
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
        "markscheme": ms_img_rel
    }
    new_questions.append(q_obj)

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    db = json.load(f)

db["papers"] = [p for p in db["papers"] if p.get("id") != paper_id]
db["papers"].append(PAPER_OBJ)

db["questions"] = [q for q in db["questions"] if q.get("paper") != paper_id]
db["questions"].extend(new_questions)

with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully ingested {len(new_questions)} questions for {paper_id}. Total marks: {sum(q['marks'] for q in new_questions)}")

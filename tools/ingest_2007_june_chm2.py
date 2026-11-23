"""
Ingestion script for 2007 June CHM2 (Section A only)
Excludes Section B extended question (Q5).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222360_1bff8756.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-june-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
# Extract fig-q1-axes.jpg (page 2)
doc[1].get_pixmap(clip=fitz.Rect(90, 195, 470, 372), dpi=200).save(os.path.join(IMG_DIR, "fig-q1-axes.jpg"))
# Extract fig-q3-table.jpg (page 6: equation + ΔHf table)
doc[5].get_pixmap(clip=fitz.Rect(70, 412, 525, 545), dpi=200).save(os.path.join(IMG_DIR, "fig-q3-table.jpg"))
# Extract fig-q4-eq.jpg (page 7: stem + equilibrium equation)
doc[6].get_pixmap(clip=fitz.Rect(55, 65, 525, 118), dpi=200).save(os.path.join(IMG_DIR, "fig-q4-eq.jpg"))

PAPER_OBJ = {
    "id": "2007-june-chm2",
    "year": 2007,
    "series": "June",
    "date": "2007-06-06",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DATA = [
    # Q1 (11 marks, p.2)
    {
        "id": "2007-june-chm2-q1ai",
        "question": "1(a)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.5"],
        "skills": ["practical", "recall"],
        "summary": "Draw a Maxwell-Boltzmann distribution of molecular energies for a gas at temperature T on the given axes.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "Curve starts at the origin and does not touch the x-axis on the right-hand side (asymptotic) (1)<br><br>Curve is skewed left (1)", "-", "2", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2007-june-chm2-q1aii",
        "question": "1(a)(ii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.5"],
        "skills": ["recall"],
        "summary": "State the meaning of the term activation energy.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "Minimum energy (1) needed for a reaction to occur (1)", "-", "2", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2007-june-chm2-q1aiii",
        "question": "1(a)(iii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.5"],
        "skills": ["application"],
        "summary": "Shade on the graph the area that represents the number of molecules which can react at temperature T.",
        "figures": ["img/2007-june-chm2/fig-q1-axes.jpg"],
        "ms_rows": [
            ("1(a)(iii)", "Area under candidate's curve from <i>E</i><sub>a</sub> to the right of it should be shaded", "-", "1", "AO2 / 3.1.5")
        ]
    },
    {
        "id": "2007-june-chm2-q1bi",
        "question": "1(b)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.5"],
        "skills": ["recall"],
        "summary": "State the effect on the activation energy of increasing the temperature.",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "None / no effect", "-", "1", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2007-june-chm2-q1bii",
        "question": "1(b)(ii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.5"],
        "skills": ["explanation"],
        "summary": "Explain why reactions involving gases become faster as the temperature increases.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "More molecules have energy greater than (or equal to) the activation energy (1)<br><br>Therefore there are more successful collisions (1)", "-", "2", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2007-june-chm2-q1c",
        "question": "1(c)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.5"],
        "skills": ["explanation"],
        "summary": "State and explain the effect of a catalyst on the rate of a gas-phase reaction.",
        "figures": [],
        "ms_rows": [
            ("1(c)", "<b>Effect:</b> Increases rate (1)<br><br><b>Explanation:</b> Follows an alternative route (1) which has a lower activation energy (1)", "-", "3", "AO1 / 3.1.5")
        ]
    },
    # Q2 (13 marks, p.5)
    {
        "id": "2007-june-chm2-q2ai",
        "question": "2(a)(i)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "In terms of electrons, state what is meant by reduction and reducing agent.",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "<b>Reduction:</b> the gain of electrons (1)<br><br><b>Reducing agent:</b> donates electrons (1)", "not pairs of electrons", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-june-chm2-q2aii",
        "question": "2(a)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "Identify a reducing agent that can reduce Fe2O3 to iron in the Blast Furnace and write an equation for the reaction.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "<b>Reducing agent:</b> C or CO (1)<br><br><b>Equation:</b> Fe<sub>2</sub>O<sub>3</sub> + 3C → 2Fe + 3CO<br><i>or</i> Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub><br><i>or</i> 2Fe<sub>2</sub>O<sub>3</sub> + 3C → 4Fe + 3CO<sub>2</sub> (1)", "-", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-june-chm2-q2aiii",
        "question": "2(a)(iii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "Give one essential condition needed for the reduction of Fe2O3 in the Blast Furnace.",
        "figures": [],
        "ms_rows": [
            ("2(a)(iii)", "High temperature needed (or in range 700 °C to 2000 °C)", "-", "1", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-june-chm2-q2b",
        "question": "2(b)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.7"],
        "skills": ["explanation"],
        "summary": "Explain how carbon impurity is removed from molten iron obtained from the Blast Furnace.",
        "figures": [],
        "ms_rows": [
            ("2(b)", "Blast with oxygen (1)<br><br>So the carbon is oxidised (or equation e.g. C + O<sub>2</sub> → CO<sub>2</sub>) (1)", "-", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-june-chm2-q2ci",
        "question": "2(c)(i)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "Write equations for Stage 1 and Stage 2 in the two-stage extraction of titanium from TiO2.",
        "figures": [],
        "ms_rows": [
            ("2(c)(i)", "<b>Stage 1:</b> TiO<sub>2</sub> + 2C + 2Cl<sub>2</sub> → TiCl<sub>4</sub> + 2CO &nbsp;(<i>or</i> TiO<sub>2</sub> + C + 2Cl<sub>2</sub> → TiCl<sub>4</sub> + CO<sub>2</sub>) (1)<br><br><b>Stage 2:</b> TiCl<sub>4</sub> + 4Na → Ti + 4NaCl &nbsp;(<i>or</i> TiCl<sub>4</sub> + 2Mg → Ti + 2MgCl<sub>2</sub>) (1)", "-", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-june-chm2-q2cii",
        "question": "2(c)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.7"],
        "skills": ["explanation"],
        "summary": "Give one essential condition, other than temperature, for the second stage of titanium extraction and state why it is necessary.",
        "figures": [],
        "ms_rows": [
            ("2(c)(ii)", "<b>Condition:</b> Argon (1)<br><br><b>Reason:</b> Prevent Ti reacting with oxygen, nitrogen or air (<i>or</i> prevent Na/Mg reacting with oxygen, nitrogen, water or air; <i>or</i> prevent TiCl<sub>4</sub> hydrolysing / reacting with water) (1)", "-", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-june-chm2-q2d",
        "question": "2(d)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "Give two reasons why titanium is expensive to extract.",
        "figures": [],
        "ms_rows": [
            ("2(d)", "Any <b>two</b> from:<ul><li>Mg / Na / Cl<sub>2</sub> have to be made first by electrolysis</li><li>Batch process</li><li>Argon atmosphere needed</li><li>High temperatures needed in both stages</li></ul>", "-", "2", "AO1 / 3.1.7")
        ]
    },
    # Q3 (11 marks, p.6)
    {
        "id": "2007-june-chm2-q3a",
        "question": "3(a)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "Define the term standard enthalpy of formation.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "Enthalpy change when one mole of substance (1)<br><br>is formed from its elements (1)<br><br>with all reactants and products in their standard states (1)", "-", "3", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2007-june-chm2-q3b",
        "question": "3(b)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["application"],
        "summary": "Write an equation, including state symbols, for the reaction with an enthalpy change equal to the standard enthalpy of formation of liquid nitric acid, HNO3.",
        "figures": [],
        "ms_rows": [
            ("3(b)", "<sup>1</sup>&frasl;<sub>2</sub>H<sub>2</sub>(g) + <sup>1</sup>&frasl;<sub>2</sub>N<sub>2</sub>(g) + <sup>3</sup>&frasl;<sub>2</sub>O<sub>2</sub>(g) → HNO<sub>3</sub>(l)", "(1) for equation<br>(1) for state symbols", "2", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2007-june-chm2-q3c",
        "question": "3(c)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "State Hess's Law.",
        "figures": [],
        "ms_rows": [
            ("3(c)", "Enthalpy change is independent of the route taken", "-", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2007-june-chm2-q3di",
        "question": "3(d)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "State why the standard enthalpy of formation of O2(g) is zero.",
        "figures": ["img/2007-june-chm2/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(d)(i)", "It is an element (in its standard state)", "-", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2007-june-chm2-q3dii",
        "question": "3(d)(ii)",
        "marks": 4,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Use the enthalpy of formation data and ΔH = -128 kJ mol-1 for H2O(l) + 2NO2(g) + 1/2 O2(g) -> 2HNO3(l) to calculate ΔHf for nitric acid.",
        "figures": ["img/2007-june-chm2/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(d)(ii)", "Δ<i>H</i> = ΣΔ<i>H</i><sub>f</sub>(products) − ΣΔ<i>H</i><sub>f</sub>(reactants) <i>or</i> correct cycle (1)<br><br>−128 = 2<i>x</i> − (−286 + 2(34)) (1)<br><br>2<i>x</i> = −346 (1)<br><br><i>x</i> = <b>−173 kJ mol<sup>−1</sup></b> (1)", "-", "4", "AO2 / 3.1.4")
        ]
    },
    # Q4 (10 marks, p.7)
    {
        "id": "2007-june-chm2-q4a",
        "question": "4(a)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["recall"],
        "summary": "State what is meant by dynamic equilibrium for 2NO(g) + O2(g) <-> 2NO2(g).",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Rate of forward reaction = rate of backward reaction (1)<br><br>Concentration of reactants and products are constant (QoL) (1)", "-", "2", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2007-june-chm2-q4b",
        "question": "4(b)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "State and explain how the total pressure should be changed to give a higher equilibrium yield of NO2 in 2NO(g) + O2(g) <-> 2NO2(g).",
        "figures": ["img/2007-june-chm2/fig-q4-eq.jpg"],
        "ms_rows": [
            ("4(b)", "<b>Change in pressure:</b> Increases (1)<br><br><b>Explanation:</b> More moles on the left-hand side of equation (1); equilibrium moves to reduce pressure / oppose the change (1)", "-", "3", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2007-june-chm2-q4c",
        "question": "4(c)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "State and explain the effect of an increase in temperature on the yield of NO2 in 2NO(g) + O2(g) <-> 2NO2(g), ΔH = -115 kJ mol-1.",
        "figures": ["img/2007-june-chm2/fig-q4-eq.jpg"],
        "ms_rows": [
            ("4(c)", "<b>Effect:</b> Decreases (1)<br><br><b>Explanation:</b> Reaction is exothermic (1); equilibrium moves to absorb heat / lower the temperature / oppose the change (1)", "-", "3", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2007-june-chm2-q4d",
        "question": "4(d)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Deduce the oxidation state of nitrogen in NO3- and in NO2+.",
        "figures": [],
        "ms_rows": [
            ("4(d)", "NO<sub>3</sub><sup>−</sup> : <b>(+)5</b> (1)<br><br>NO<sub>2</sub><sup>+</sup> : <b>(+)5</b> (1)", "-", "2", "AO2 / 3.1.7")
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
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.5"
    for r in qd["ms_rows"]:
        prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
        answers_list.append(f"{prefix}{r[1]} ({r[3]})" if len(qd["ms_rows"]) > 1 else r[1])
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

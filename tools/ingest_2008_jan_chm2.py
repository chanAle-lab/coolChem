"""
Ingestion script for 2008 January CHM2 (Section A only: Q1-Q5)
Excludes Section B extended question (Q6).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471418112_dfec1f4a.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2008-jan-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
# Extract fig-q2-eq.jpg (PDF p.5)
doc[4].get_pixmap(clip=fitz.Rect(55, 68, 520, 132), dpi=200).save(os.path.join(IMG_DIR, "fig-q2-eq.jpg"))
# Extract fig-q3-table.jpg (PDF p.6: table + equation)
doc[5].get_pixmap(clip=fitz.Rect(95, 290, 495, 515), dpi=200).save(os.path.join(IMG_DIR, "fig-q3-table.jpg"))

PAPER_OBJ = {
    "id": "2008-jan-chm2",
    "year": 2008,
    "series": "January",
    "date": "2008-01-10",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DATA = [
    # Q1 (9 marks, PDF p.2)
    {
        "id": "2008-jan-chm2-q1ai",
        "question": "1(a)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.2.3"],
        "skills": ["recall"],
        "summary": "State what is observed when aqueous silver nitrate is added to aqueous bromide ions and write an ionic equation.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "<b>Observation:</b> Cream / off-white precipitate (1)<br><br><b>Ionic equation:</b> Ag<sup>+</sup> + Br<sup>−</sup> → AgBr (1)", "-", "2", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2008-jan-chm2-q1aii",
        "question": "1(a)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.2.3"],
        "skills": ["recall"],
        "summary": "State what is observed when an excess of concentrated aqueous ammonia is added to the silver bromide precipitate.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "Precipitate dissolves / colourless solution formed", "-", "1", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2008-jan-chm2-q1bi",
        "question": "1(b)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.2.3"],
        "skills": ["recall"],
        "summary": "State what is observed when chlorine is added to aqueous bromide ions and write an ionic equation.",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "<b>Observation:</b> Yellow / orange / brown solution forms (1)<br><br><b>Ionic equation:</b> Cl<sub>2</sub> + 2Br<sup>−</sup> → 2Cl<sup>−</sup> + Br<sub>2</sub> (1)", "-", "2", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2008-jan-chm2-q1bii",
        "question": "1(b)(ii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.2.3"],
        "skills": ["explanation"],
        "summary": "Identify one halide ion, other than chloride, which will not react with chlorine and explain why.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "<b>Halide ion:</b> F<sup>−</sup> / fluoride ion (1)<br><br><b>Explanation:</b> Cl<sub>2</sub> is less reactive than F<sub>2</sub> / Cl<sub>2</sub> is a weaker oxidising agent than F<sub>2</sub> / F<sup>−</sup> is a worse reducing agent than Cl<sup>−</sup> (1)", "-", "2", "AO2 / 3.2.3")
        ]
    },
    {
        "id": "2008-jan-chm2-q1c",
        "question": "1(c)",
        "marks": 2,
        "page": 2,
        "topics": ["3.2.3"],
        "skills": ["application"],
        "summary": "Write an equation for the reaction of bromine with cold aqueous sodium hydroxide.",
        "figures": [],
        "ms_rows": [
            ("1(c)", "2NaOH + Br<sub>2</sub> → NaBr + NaOBr + H<sub>2</sub>O", "1 mark for products NaBr + NaOBr + H<sub>2</sub>O<br>1 mark for balanced equation", "2", "AO2 / 3.2.3")
        ]
    },
    # Q2 (8 marks, PDF p.5)
    {
        "id": "2008-jan-chm2-q2a",
        "question": "2(a)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "State and explain the effect of decreasing the temperature on the equilibrium yield of HI in H2(g) + I2(g) <-> 2HI(g), ΔH = -10 kJ mol-1.",
        "figures": [],
        "ms_rows": [
            ("2(a)", "<b>Effect:</b> Increase (1)<br><br><b>Explanation:</b> Reaction is exothermic (1); system tries to raise temperature of system / opposes the change (1)", "-", "3", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2008-jan-chm2-q2b",
        "question": "2(b)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "State and explain the effect of increasing the pressure on the equilibrium yield of HI in H2(g) + I2(g) <-> 2HI(g).",
        "figures": ["img/2008-jan-chm2/fig-q2-eq.jpg"],
        "ms_rows": [
            ("2(b)", "<b>Effect:</b> No effect (1)<br><br><b>Explanation:</b> Same number of moles on each side / each side affected equally (1)", "-", "2", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2008-jan-chm2-q2c",
        "question": "2(c)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "Explain why an increase in the concentration of hydrogen gas increases the equilibrium yield of hydrogen iodide.",
        "figures": ["img/2008-jan-chm2/fig-q2-eq.jpg"],
        "ms_rows": [
            ("2(c)", "System tries to lower concentration of hydrogen (and moves to the right)", "-", "1", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2008-jan-chm2-q2d",
        "question": "2(d)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.6"],
        "skills": ["recall"],
        "summary": "Explain why the addition of a catalyst does not alter the position of equilibrium.",
        "figures": ["img/2008-jan-chm2/fig-q2-eq.jpg"],
        "ms_rows": [
            ("2(d)", "Increases the rate of the forward and backward reactions (1)<br><br>equally (1)", "-", "2", "AO1 / 3.1.6")
        ]
    },
    # Q3 (13 marks, PDF p.6-7)
    {
        "id": "2008-jan-chm2-q3a",
        "question": "3(a)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "Define the term standard enthalpy of combustion.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "Enthalpy change when 1 mole of compound (1)<br><br>is completely burned in oxygen (1)<br><br>under standard conditions (1)", "-", "3", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2008-jan-chm2-q3b",
        "question": "3(b)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["application"],
        "summary": "Write an equation for the complete combustion of ethanol, C2H5OH.",
        "figures": [],
        "ms_rows": [
            ("3(b)", "C<sub>2</sub>H<sub>5</sub>OH + 3O<sub>2</sub> → 2CO<sub>2</sub> + 3H<sub>2</sub>O", "-", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2008-jan-chm2-q3c",
        "question": "3(c)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Use the standard enthalpies of formation in the table to calculate ΔHc of propan-1-ol, C3H7OH.",
        "figures": [],
        "ms_rows": [
            ("3(c)", "Δ<i>H</i> = ΣΔ<i>H</i><sub>f</sub>(products) − ΣΔ<i>H</i><sub>f</sub>(reactants) <i>or</i> correct cycle (1)<br><br>= (−394 × 3) + (−286 × 4) − (−315) (1)<br><br>= <b>−2011 kJ mol<sup>−1</sup></b> (1)", "(+2011 kJ mol<sup>−1</sup> scores 1 mark)", "3", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2008-jan-chm2-q3d",
        "question": "3(d)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.4"],
        "skills": ["explanation"],
        "summary": "State how the value of ΔHc obtained in part (c) would differ if gaseous water, rather than liquid water, is formed.",
        "figures": ["img/2008-jan-chm2/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(d)", "Less negative (<b>QWC</b>)", "-", "1", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2008-jan-chm2-q3e",
        "question": "3(e)",
        "marks": 4,
        "page": 7,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Calculate the enthalpy of combustion of propan-1-ol when 0.92 g raises the temperature of 250 g water by 16 °C (c = 4.2 J K-1 g-1).",
        "figures": [],
        "ms_rows": [
            ("3(e)", "<i>Q</i> = <i>mc</i>Δ<i>T</i> (1)<br><br>250 × 4.2 × 16 = 16800 J (1)<br><br>Moles propanol = 0.92 / 60 (= 0.0153) (1)<br><br>Δ<i>H</i><sub>c</sub> = −16800 / 0.0153 = <b>−1096 kJ mol<sup>−1</sup></b> (1)", "allow answers in range −1090 to −1120", "4", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2008-jan-chm2-q3f",
        "question": "3(f)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.4"],
        "skills": ["practical", "explanation"],
        "summary": "Suggest why the experimental value of enthalpy of combustion in (e) is less reliable than the calculated value in (c).",
        "figures": [],
        "ms_rows": [
            ("3(f)", "Heat loss occurs in (e) / no heat loss in (c) / incomplete combustion in (e)", "-", "1", "AO3 / 3.1.4")
        ]
    },
    # Q4 (9 marks, PDF p.8-9)
    {
        "id": "2008-jan-chm2-q4a",
        "question": "4(a)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.5"],
        "skills": ["application"],
        "summary": "On Figure 1, draw a Maxwell-Boltzmann distribution curve for one mole of gas at a higher temperature.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Curve lower and skewed to right (1)<br><br>Starts at origin and does not touch x-axis or cross drawn curve on right (1)", "-", "2", "AO2 / 3.1.5")
        ]
    },
    {
        "id": "2008-jan-chm2-q4b",
        "question": "4(b)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.5"],
        "skills": ["application"],
        "summary": "On Figure 2, draw a Maxwell-Boltzmann distribution curve for two moles of gas at 300 K.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "Peak height in same place (energy) as drawn curve (1)<br><br>Peak height twice as high as drawn curve (1)", "-", "2", "AO2 / 3.1.5")
        ]
    },
    {
        "id": "2008-jan-chm2-q4ci",
        "question": "4(c)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.5"],
        "skills": ["recall"],
        "summary": "Explain why collisions between molecules of gases A and B do not always lead to a reaction.",
        "figures": [],
        "ms_rows": [
            ("4(c)(i)", "Particles <b>A</b> and <b>B</b> may not have the activation energy required for a successful collision", "-", "1", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2008-jan-chm2-q4cii",
        "question": "4(c)(ii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.5"],
        "skills": ["explanation"],
        "summary": "Explain why increasing temperature by a small amount has a much bigger effect on reaction rate than increasing pressure by a small amount.",
        "figures": [],
        "ms_rows": [
            ("4(c)(ii)", "Increasing temperature by a small amount increases the number of particles having <i>E</i> ≥ <i>E</i><sub>a</sub> (1)<br><br>Increasing pressure by a small amount increases collisions by a small amount (<b>QWC</b>) (1)", "-", "2", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2008-jan-chm2-q4ciii",
        "question": "4(c)(iii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.5"],
        "skills": ["recall"],
        "summary": "Explain why adding a catalyst increases the rate of reaction between gases A and B.",
        "figures": [],
        "ms_rows": [
            ("4(c)(iii)", "Provides an alternative route (1)<br><br>of lower activation energy (1)", "-", "2", "AO1 / 3.1.5")
        ]
    },
    # Q5 (6 marks, PDF p.10)
    {
        "id": "2008-jan-chm2-q5a",
        "question": "5(a)",
        "marks": 2,
        "page": 10,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Deduce the oxidation state of S in SO3^2- and in SO4^2-.",
        "figures": [],
        "ms_rows": [
            ("5(a)", "SO<sub>3</sub><sup>2−</sup> : <b>(+)4</b> (1)<br><br>SO<sub>4</sub><sup>2−</sup> : <b>(+)6</b> (1)", "-", "2", "AO2 / 3.1.7")
        ]
    },
    {
        "id": "2008-jan-chm2-q5bi",
        "question": "5(b)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Write a half-equation for the conversion of Cl2 into Cl- ions.",
        "figures": [],
        "ms_rows": [
            ("5(b)(i)", "Cl<sub>2</sub> + 2e<sup>−</sup> → 2Cl<sup>−</sup>", "-", "1", "AO2 / 3.1.7")
        ]
    },
    {
        "id": "2008-jan-chm2-q5bii",
        "question": "5(b)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Write a half-equation for the conversion of aqueous SO3^2- ions into SO4^2- ions.",
        "figures": [],
        "ms_rows": [
            ("5(b)(ii)", "H<sub>2</sub>O + SO<sub>3</sub><sup>2−</sup> → SO<sub>4</sub><sup>2−</sup> + 2H<sup>+</sup> + 2e<sup>−</sup>", "-", "1", "AO2 / 3.1.7")
        ]
    },
    {
        "id": "2008-jan-chm2-q5biii",
        "question": "5(b)(iii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Write an overall equation for the reaction between Cl2 and SO3^2- ions.",
        "figures": [],
        "ms_rows": [
            ("5(b)(iii)", "Cl<sub>2</sub> + H<sub>2</sub>O + SO<sub>3</sub><sup>2−</sup> → SO<sub>4</sub><sup>2−</sup> + 2H<sup>+</sup> + 2Cl<sup>−</sup>", "-", "1", "AO2 / 3.1.7")
        ]
    },
    {
        "id": "2008-jan-chm2-q5biv",
        "question": "5(b)(iv)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Deduce the role of SO3^2- ions in the reaction with Cl2.",
        "figures": [],
        "ms_rows": [
            ("5(b)(iv)", "Reducing agent", "-", "1", "AO2 / 3.1.7")
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
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.4"
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

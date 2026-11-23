"""
Ingestion script for 2007 January CHM2 (Section A only)
Excludes old-spec Section B essay question (Q6).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795469473824_f40f348a.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-jan-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

# Extract fig-q1-table2.jpg (standard enthalpies of formation table on page 5)
doc = fitz.open(QP_PATH)
page5 = doc[4]
rect = fitz.Rect(95, 100, 505, 170)
pix = page5.get_pixmap(clip=rect, dpi=200)
pix.save(os.path.join(IMG_DIR, "fig-q1-table2.jpg"))

PAPER_OBJ = {
    "id": "2007-jan-chm2",
    "year": 2007,
    "series": "January",
    "date": "2007-01-11",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2007-jan-chm2-q1a",
        "question": "1(a)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "Explain the meaning of the term enthalpy change of a reaction.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "Heat energy change (1)<br>at constant pressure (1)", "-", "2", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2007-jan-chm2-q1b",
        "question": "1(b)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["application"],
        "summary": "Write the equation for the standard enthalpy of formation of nitrous oxide, N2O.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "N<sub>2</sub>(g) + ½ O<sub>2</sub>(g) &rarr; N<sub>2</sub>O(g)", "-", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2007-jan-chm2-q1ci",
        "question": "1(c)(i)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Calculate a value for the enthalpy of formation of nitrogen trifluoride using mean bond enthalpy values.",
        "figures": [],
        "ms_rows": [
            ("1(c)(i)", "Δ<i>H</i> = Σ bonds broken − Σ bonds made (1)<br>= ½ (945) + 3/2 (159) − 3(278) (1)<br>= <b>−123 kJ mol<sup>-1</sup></b> (1)", "+123 kJ mol<sup>-1</sup> scores 1 mark<br>Accept no units", "3", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2007-jan-chm2-q1cii",
        "question": "1(c)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["explanation"],
        "summary": "Give one reason why the calculated enthalpy of formation of NF3 differs from the data book value (–114 kJ mol-1).",
        "figures": [],
        "ms_rows": [
            ("1(c)(ii)", "The N–F bond energy is an average taken from several compounds", "-", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2007-jan-chm2-q1di",
        "question": "1(d)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "State why the enthalpy of formation of fluorine is zero.",
        "figures": ["img/2007-jan-chm2/fig-q1-table2.jpg"],
        "ms_rows": [
            ("1(d)(i)", "It is an element", "-", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2007-jan-chm2-q1dii",
        "question": "1(d)(ii)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Use standard enthalpies of formation to calculate the enthalpy change for 4NH3(g) + 3F2(g) -> NF3(g) + 3NH4F(s).",
        "figures": ["img/2007-jan-chm2/fig-q1-table2.jpg"],
        "ms_rows": [
            ("1(d)(ii)", "Δ<i>H</i> = Σ Δ<i>H</i><sub>f</sub> products − Σ Δ<i>H</i><sub>f</sub> reactants (or correct cycle) (1)<br>= −114 + 3(−467) − 4(−46) − 0 (1)<br>= <b>−1331 kJ mol<sup>-1</sup></b> (1)", "+1331 kJ mol<sup>-1</sup> scores 1 mark<br>Accept no units", "3", "AO2 / 3.1.4")
        ]
    },
    # Q2
    {
        "id": "2007-jan-chm2-q2ai",
        "question": "2(a)(i)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Deduce the oxidation states of chlorine in HClO, Cl2, and ClO3-.",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "HClO: <b>+1</b> (1)<br>Cl<sub>2</sub>: <b>0</b> (1)<br>ClO<sub>3</sub><sup>-</sup>: <b>+5</b> (1)", "-", "3", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q2aii",
        "question": "2(a)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.7"],
        "skills": ["explanation"],
        "summary": "Comment on the redox behaviour of HClO in its decomposition reaction.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "HClO is simultaneously oxidised and reduced", "-", "1", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Write the half-equation for the conversion of HClO in acid solution into chlorine gas.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "2HClO + 2H<sup>+</sup> + 2e<sup>-</sup> &rarr; Cl<sub>2</sub> + 2H<sub>2</sub>O<br>or 2ClO<sup>-</sup> + 4H<sup>+</sup> + 2e<sup>-</sup> &rarr; Cl<sub>2</sub> + 2H<sub>2</sub>O", "-", "1", "AO2 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Write the half-equation for the conversion of aqueous HClO into ClO3- ions and H+ ions.",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "HClO + 2H<sub>2</sub>O &rarr; ClO<sub>3</sub><sup>-</sup> + 5H<sup>+</sup> + 4e<sup>-</sup><br>or ClO<sup>-</sup> + 2H<sub>2</sub>O &rarr; ClO<sub>3</sub><sup>-</sup> + 4H<sup>+</sup> + 4e<sup>-</sup>", "-", "1", "AO2 / 3.1.7")
        ]
    },
    # Q3
    {
        "id": "2007-jan-chm2-q3ai",
        "question": "3(a)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.2.3"],
        "skills": ["recall"],
        "summary": "State the trend in oxidising ability of the halogens from fluorine to iodine.",
        "figures": [],
        "ms_rows": [
            ("3(a)(i)", "Decreases from fluorine to iodine", "-", "1", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2007-jan-chm2-q3aii",
        "question": "3(a)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.2.3"],
        "skills": ["application"],
        "summary": "Write an equation to show how chlorine reacts with aqueous potassium bromide.",
        "figures": [],
        "ms_rows": [
            ("3(a)(ii)", "Cl<sub>2</sub> + 2KBr &rarr; Br<sub>2</sub> + 2KCl", "Accept ionic equations", "1", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2007-jan-chm2-q3b",
        "question": "3(b)",
        "marks": 6,
        "page": 7,
        "topics": ["3.2.3"],
        "skills": ["practical", "application"],
        "summary": "Identify the sodium halides J, K, L and reaction products M, N and Q from silver nitrate and sulphuric acid tests.",
        "figures": [],
        "ms_rows": [
            ("3(b)", "<b>J:</b> NaF (accept F<sup>-</sup> or correct name) (1)<br><b>K:</b> NaI (accept I<sup>-</sup> or correct name) (1)<br><b>L:</b> NaBr (accept Br<sup>-</sup> or correct name) (1)<br><b>M:</b> Br<sub>2</sub> / bromine (1)<br><b>N and Q:</b> HBr / hydrogen bromide (1) and SO<sub>2</sub> / sulphur dioxide (1)", "-", "6", "AO3 / 3.2.3")
        ]
    },
    # Q4
    {
        "id": "2007-jan-chm2-q4a",
        "question": "4(a)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.6"],
        "skills": ["recall"],
        "summary": "Explain what is meant by a reaction in equilibrium.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Rate of the forward reaction = rate of the backward reaction (1)<br><br>Concentrations are constant (1)", "-", "2", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2007-jan-chm2-q4b",
        "question": "4(b)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "State and explain the effect on the yield of Z in X(g) + 2Y(g) <-> 2Z(g) if the overall pressure is increased.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "Effect: <b>Increase</b> (1)<br><br>Explanation: There are 3 moles on the LHS and 2 moles on the RHS (1)<br>so the system moves to the right to decrease the pressure / oppose the increase in pressure (1)", "-", "3", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2007-jan-chm2-q4c",
        "question": "4(c)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "Deduce and explain the enthalpy change for the forward reaction given that an increase in temperature decreases the yield of Z.",
        "figures": [],
        "ms_rows": [
            ("4(c)", "Enthalpy change: <b>Negative</b> (allow exothermic) (1)<br><br>Explanation: the equilibrium shifts to decrease the temperature / oppose the increase in temperature (1)", "-", "2", "AO2 / 3.1.6")
        ]
    },
    # Q5
    {
        "id": "2007-jan-chm2-q5a",
        "question": "5(a)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "State two reasons why aluminium is a commonly used metal.",
        "figures": [],
        "ms_rows": [
            ("5(a)", "Any two of:<br>• Resists corrosion (1)<br>• Abundant ore (1)<br>• Lightweight (1)", "-", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q5bi",
        "question": "5(b)(i)",
        "marks": 4,
        "page": 9,
        "topics": ["3.1.7"],
        "skills": ["recall", "application"],
        "summary": "State the conditions used in the extraction of aluminium from its oxide by electrolysis and give half-equations for each electrode.",
        "figures": [],
        "ms_rows": [
            ("5(b)(i)", "Conditions: Molten or dissolved (1) in cryolite (1)<br><br>Half-equation 1: Al<sup>3+</sup> + 3e<sup>-</sup> &rarr; Al (1)<br>Half-equation 2: 2O<sup>2-</sup> &rarr; O<sub>2</sub> + 4e<sup>-</sup> (1)", "-", "4", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q5bii",
        "question": "5(b)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "State the type of reaction occurring at the negative electrode during aluminium extraction.",
        "figures": [],
        "ms_rows": [
            ("5(b)(ii)", "Reduction", "-", "1", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q5c",
        "question": "5(c)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.7"],
        "skills": ["application"],
        "summary": "Write an equation for the thermite reaction and state the role of aluminium.",
        "figures": [],
        "ms_rows": [
            ("5(c)", "Equation: 2Al + Fe<sub>2</sub>O<sub>3</sub> &rarr; Al<sub>2</sub>O<sub>3</sub> + 2Fe (1)<br><br>Role: Reducing agent (1)", "-", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q5d",
        "question": "5(d)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.7"],
        "skills": ["recall", "application"],
        "summary": "Write an equation and state the necessary condition for the formation of iron from iron(III) oxide in the Blast Furnace.",
        "figures": [],
        "ms_rows": [
            ("5(d)", "Equation: Fe<sub>2</sub>O<sub>3</sub> + 3CO &rarr; 2Fe + 3CO<sub>2</sub><br>or Fe<sub>2</sub>O<sub>3</sub> + 3C &rarr; 2Fe + 3CO<br>or 2Fe<sub>2</sub>O<sub>3</sub> + 3C &rarr; 4Fe + 3CO<sub>2</sub> (1)<br><br>Condition: 1500 °C (or in range 1000–2000 °C; accept high temperatures) (1)", "-", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2007-jan-chm2-q5e",
        "question": "5(e)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.7"],
        "skills": ["explanation"],
        "summary": "Give two reasons why it is cheaper to produce iron in the Blast Furnace than in the thermite process.",
        "figures": [],
        "ms_rows": [
            ("5(e)", "1. Blast furnace process is continuous (1)<br>2. Coke / CO is a cheaper reducing agent than Aluminium (1)", "QoL on reason 2", "2", "AO1 / 3.1.7")
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

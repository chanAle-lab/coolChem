"""
Ingestion script for 2006 June CHM2 (Section A only)
Excludes old-spec Section B essay question (Q5).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383066798_743f5157.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-june-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

# Extract figures
doc = fitz.open(QP_PATH)
# fig-q2-curve.jpg on page 6 (index 5)
page6 = doc[5]
rect6 = fitz.Rect(100, 105, 460, 310)
pix6 = page6.get_pixmap(clip=rect6, dpi=200)
pix6.save(os.path.join(IMG_DIR, "fig-q2-curve.jpg"))

# fig-q3-table.jpg on page 7 (index 6)
page7 = doc[6]
rect7 = fitz.Rect(70, 95, 500, 255)
pix7 = page7.get_pixmap(clip=rect7, dpi=200)
pix7.save(os.path.join(IMG_DIR, "fig-q3-table.jpg"))

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2006-june-chm2-q1a",
        "question": "1(a)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "Define the term standard enthalpy of formation.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "Enthalpy change when 1 mol of compound<br><br>Is formed from its elements<br><br>All substances in their standard state", "1 mark for enthalpy change for 1 mol of compound<br>1 mark for formed from elements<br>1 mark for standard state (and at 298 K / 100 kPa)", "3", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2006-june-chm2-q1b",
        "question": "1(b)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Calculate the standard enthalpy of formation of liquid methylbenzene from enthalpies of combustion.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "Δ<i>H</i> = ΣΔ<i>H</i><sub>c</sub>°(reactants) - ΣΔ<i>H</i><sub>c</sub>°(products)<br><br>= [7 × (-394)] + [4 × (-286)] - (-3909)<br>= -2758 - 1144 + 3909<br><br>= +7 kJ mol<sup>-1</sup>", "M1: Formula or cycle: Δ<i>H</i> = ΣΔ<i>H</i><sub>c</sub>(reactants) - ΣΔ<i>H</i><sub>c</sub>(products)<br>M2: Correct numbers substituted<br>M3: +7 kJ mol<sup>-1</sup>", "3", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2006-june-chm2-q1c",
        "question": "1(c)",
        "marks": 4,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Calculate the enthalpy of combustion of methylbenzene from experimental calorimetry data.",
        "figures": [],
        "ms_rows": [
            ("1(c)", "Heat change <i>q</i> = <i>mc</i>Δ<i>T</i><br>= 250 × 4.18 × 60 = 62700 J = 62.7 kJ<br><br>Moles C<sub>7</sub>H<sub>8</sub> = 2.5 / 92 = 0.0272 mol<br><br>Δ<i>H</i> = -<i>q</i> / <i>n</i> = -62.7 / 0.0272 = -2307 kJ mol<sup>-1</sup> (allow -2300 to -2323)", "M1: <i>q</i> = <i>mc</i>Δ<i>T</i> expression<br>M2: 62.7 kJ (or 62700 J)<br>M3: Moles = 0.0272 mol<br>M4: -2307 kJ mol<sup>-1</sup> (allow -2300 to -2323; negative sign required)", "4", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2006-june-chm2-q1d",
        "question": "1(d)",
        "marks": 4,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Calculate the enthalpy of neutralisation per mole of water formed from aqueous acid-base reaction data.",
        "figures": [],
        "ms_rows": [
            ("1(d)", "Mass of water heated = 25 + 50 = 75 g AND Temperature rise = 26.5 - 18.0 = 8.5 °C<br><br>Heat change = 75 × 4.18 × 8.5 = 2665 J = 2.665 kJ<br><br>Moles HCl = 0.05 mol<br><br>Δ<i>H</i> = -2.665 / 0.05 = -53.3 kJ mol<sup>-1</sup> (allow -53 to -54)", "M1: Mass 75 g and Δ<i>T</i> = 8.5 °C (both needed for 1 mark)<br>M2: Heat change = 2.665 kJ (or 2665 J)<br>M3: Moles HCl = (50 × 1.0)/1000 = 0.05 mol<br>M4: -53.3 kJ mol<sup>-1</sup> (allow -53 to -54; negative sign required)", "4", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2006-june-chm2-q1e",
        "question": "1(e)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["evaluation"],
        "summary": "Explain why a polystyrene cup is used rather than a glass beaker in calorimetry experiments.",
        "figures": [],
        "ms_rows": [
            ("1(e)", "Less heat loss (or better insulator / lower heat capacity)", "Accept 'less heat lost to surroundings' / 'polystyrene is a good insulator'", "1", "AO1 / 3.1.4")
        ]
    },
    # Q2
    {
        "id": "2006-june-chm2-q2ai",
        "question": "2(a)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.5"],
        "skills": ["recall"],
        "summary": "State which letter represents the most probable energy of molecules on the Maxwell-Boltzmann distribution.",
        "figures": ["img/2006-june-chm2/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(a)(i)", "Z", "1 mark for Z (peak of curve)", "1", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2006-june-chm2-q2aii",
        "question": "2(a)(ii)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.5"],
        "skills": ["explanation"],
        "summary": "Explain the process that causes some molecules to have energies represented by region X.",
        "figures": ["img/2006-june-chm2/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(a)(ii)", "Collisions<br><br>Cause some molecules to slow down / lose energy", "1 mark for collisions<br>1 mark for molecules slow down / lose energy", "2", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2006-june-chm2-q2b",
        "question": "2(b)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.5"],
        "skills": ["application"],
        "summary": "Sketch a curve on the diagram to show the distribution of energies at a higher temperature.",
        "figures": ["img/2006-june-chm2/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(b)", "Curve starts at origin and peak is displaced to the right<br><br>Peak is lower and curve remains above original at higher energy, not touching the energy axis", "1 mark: starts at origin and peak displaced to the right<br>1 mark: peak is lower and tail higher, not touching the axis", "2", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2006-june-chm2-q2ci",
        "question": "2(c)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.5"],
        "skills": ["explanation"],
        "summary": "Explain why only a very small percentage of collisions lead to reaction even in a fast reaction.",
        "figures": ["img/2006-june-chm2/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(c)(i)", "Only a small percentage / very few collisions have energy <i>E</i> ≥ <i>E</i><sub>a</sub> (energy greater than or equal to activation energy)", "Accept 'only a small proportion have activation energy'", "1", "AO1 / 3.1.5")
        ]
    },
    {
        "id": "2006-june-chm2-q2cii",
        "question": "2(c)(ii)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.5"],
        "skills": ["explanation"],
        "summary": "State and explain a method other than changing temperature for increasing the proportion of successful collisions.",
        "figures": ["img/2006-june-chm2/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(c)(ii)", "Method: Add a catalyst<br><br>Explanation:<br>Lowers the activation energy (<i>E</i><sub>a</sub>) / provides alternative route with lower <i>E</i><sub>a</sub><br><br>More collisions / molecules have energy ≥ <i>E</i><sub>a</sub>", "1 mark for add a catalyst<br>1 mark for lowers activation energy<br>1 mark for more molecules/collisions have energy ≥ <i>E</i><sub>a</sub>", "3", "AO1 / 3.1.5")
        ]
    },
    # Q3
    {
        "id": "2006-june-chm2-q3a",
        "question": "3(a)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["recall"],
        "summary": "Explain the meaning of the term dynamic equilibrium.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "Rate of forward reaction = rate of backward reaction<br><br>Concentrations of reactants and products remain constant", "1 mark: rate forward = rate backward<br>1 mark: concentrations of reactants and products are constant", "2", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm2-q3b",
        "question": "3(b)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "Use Le Chatelier's principle to explain why higher pressure gives a higher yield of ammonia.",
        "figures": [],
        "ms_rows": [
            ("3(b)", "System opposes change / shifts to reduce pressure<br><br>Moves to the side with fewer moles of gas<br><br>In this case 2 moles of NH<sub>3</sub> on the right < 4 moles (1 N<sub>2</sub> + 3 H<sub>2</sub>) on the left", "1 mark: system opposes increase in pressure<br>1 mark: shifts to side with fewer moles<br>1 mark: 2 moles on right < 4 moles on left", "3", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm2-q3c",
        "question": "3(c)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["evaluation"],
        "summary": "Give a reason why very high pressures of 50 MPa are not used commercially in the Haber Process.",
        "figures": [],
        "ms_rows": [
            ("3(c)", "Too expensive to generate / high cost of equipment/pipes to withstand high pressure / safety hazard", "Accept high electrical/running costs or high plant/capital costs", "1", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm2-q3di",
        "question": "3(d)(i)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "State and explain the advantage of using a lower temperature than 800 K in the Haber process.",
        "figures": ["img/2006-june-chm2/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(d)(i)", "Advantage: Yield of ammonia increases<br><br>Explanation:<br>Forward reaction is exothermic<br><br>System moves to raise temperature / oppose decrease in temperature / favours exothermic direction", "1 mark for yield increases<br>1 mark for forward reaction is exothermic<br>1 mark for system opposes decrease in temp / shifts in exothermic direction", "3", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm2-q3dii",
        "question": "3(d)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.5", "3.1.6"],
        "skills": ["recall"],
        "summary": "State the major advantage of using a higher temperature than 800 K.",
        "figures": ["img/2006-june-chm2/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(d)(ii)", "Faster rate of reaction / reaches equilibrium faster", "Accept 'faster reaction'", "1", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm2-q3diii",
        "question": "3(d)(iii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["evaluation"],
        "summary": "Explain why 800 K is referred to as a compromise temperature in the Haber process.",
        "figures": ["img/2006-june-chm2/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(d)(iii)", "Balance between rate and yield (acceptable rate with acceptable/economic yield)", "1 mark for balance between rate and yield", "1", "AO1 / 3.1.6")
        ]
    },
    # Q4
    {
        "id": "2006-june-chm2-q4a",
        "question": "4(a)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "Explain why a batch process is more expensive to operate than a continuous process in terms of energy.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Batch process involves stopping and starting<br><br>Energy is lost when cooling down after stopping / energy needed to heat up each time", "1 mark: batch involves stopping and starting<br>1 mark: energy lost on cooling or energy needed to re-heat", "2", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm2-q4b",
        "question": "4(b)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.7", "3.2.5"],
        "skills": ["recall"],
        "summary": "Write an equation for the reduction of iron(III) oxide Fe2O3 in the blast furnace.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub><br>(or Fe<sub>2</sub>O<sub>3</sub> + 3C → 2Fe + 3CO or 2Fe<sub>2</sub>O<sub>3</sub> + 3C → 4Fe + 3CO<sub>2</sub>)", "1 mark for use of C or CO as reducing agent<br>1 mark for correctly balanced equation", "2", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2006-june-chm2-q4c",
        "question": "4(c)",
        "marks": 4,
        "page": 8,
        "topics": ["3.1.7", "3.2.5"],
        "skills": ["recall"],
        "summary": "Write two equations for the extraction of titanium from titanium(IV) oxide TiO2.",
        "figures": [],
        "ms_rows": [
            ("4(c)", "Step 1: TiO<sub>2</sub> + 2C + 2Cl<sub>2</sub> → TiCl<sub>4</sub> + 2CO<br>(or TiO<sub>2</sub> + C + 2Cl<sub>2</sub> → TiCl<sub>4</sub> + CO<sub>2</sub>)<br><br>Step 2: TiCl<sub>4</sub> + 4Na → Ti + 4NaCl<br>(or TiCl<sub>4</sub> + 2Mg → Ti + 2MgCl<sub>2</sub>)", "M1: Use of C and Cl<sub>2</sub> in Step 1<br>M2: Balanced Step 1 equation<br>M3: Use of Na or Mg in Step 2<br>M4: Balanced Step 2 equation", "4", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2006-june-chm2-q4d",
        "question": "4(d)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.7", "3.2.5"],
        "skills": ["evaluation"],
        "summary": "State one raw material, other than titanium(IV) oxide, which makes the extraction of titanium expensive.",
        "figures": [],
        "ms_rows": [
            ("4(d)", "Sodium (Na) / Magnesium (Mg) / Chlorine (Cl<sub>2</sub>)", "1 mark for Na, Mg, or Cl<sub>2</sub> is expensive", "1", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2006-june-chm2-q4e",
        "question": "4(e)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.7"],
        "skills": ["evaluation"],
        "summary": "State why extraction of aluminium by electrolysis is an expensive process.",
        "figures": [],
        "ms_rows": [
            ("4(e)", "Expensive electricity / large amount of electrical energy needed in electrolysis", "1 mark for electricity is expensive / high cost of electricity", "1", "AO1 / 3.1.7")
        ]
    }
]

paper_id = "2006-june-chm2"
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

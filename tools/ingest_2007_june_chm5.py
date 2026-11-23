"""
Ingestion script for 2007 June CHM5 (Section A only: Q1-Q4)
Excludes Section B extended questions (Q5-Q8).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222573_c7a4b8b1.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-june-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
# Extract fig-q1-cycle-table.jpg (PDF p.2)
doc[1].get_pixmap(clip=fitz.Rect(42, 160, 535, 588), dpi=200).save(os.path.join(IMG_DIR, "fig-q1-cycle-table.jpg"))
# Extract fig-q2-table.jpg (PDF p.6)
doc[5].get_pixmap(clip=fitz.Rect(115, 105, 460, 260), dpi=200).save(os.path.join(IMG_DIR, "fig-q2-table.jpg"))
# Extract fig-q3-table.jpg (PDF p.8)
doc[7].get_pixmap(clip=fitz.Rect(165, 98, 415, 245), dpi=200).save(os.path.join(IMG_DIR, "fig-q3-table.jpg"))

PAPER_OBJ = {
    "id": "2007-june-chm5",
    "year": 2007,
    "series": "June",
    "date": "2007-06-25",
    "code": "CHM5",
    "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 120,
    "duration": "2 hours"
}

QUESTIONS_DATA = [
    # Q1 (17 marks, PDF p.2 & p.5)
    {
        "id": "2007-june-chm5-q1a",
        "question": "1(a)",
        "marks": 4,
        "page": 2,
        "topics": ["3.1.8"],
        "skills": ["application"],
        "summary": "Complete the Born-Haber cycle for magnesium chloride by writing the appropriate chemical formulae with state symbols.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "<b>Top line:</b> Mg<sup>2+</sup>(g) + 2e<sup>−</sup> + 2Cl(g) (1)<br><i>(only answer for top line)</i><br><br><b>Next down:</b> Mg<sup>2+</sup>(g) + 2e<sup>−</sup> + Cl<sub>2</sub>(g) (1)<br><br><b>Next down:</b> Mg<sup>+</sup>(g) + e<sup>−</sup> + Cl<sub>2</sub>(g) (1)<br><br><b>Bottom above Mg(s) + Cl<sub>2</sub>(g):</b> Mg(g) + Cl<sub>2</sub>(g) (1)", "state symbols and electrons essential; Cl<sub>2</sub> → 2Cl can be in any order, but Mg must be in sequence", "4", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2007-june-chm5-q1b",
        "question": "1(b)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.8"],
        "skills": ["calculation"],
        "summary": "Use the Born-Haber cycle and table of data to calculate the second ionisation enthalpy of magnesium.",
        "figures": ["img/2007-june-chm5/fig-q1-cycle-table.jpg"],
        "ms_rows": [
            ("1(b)", "I.E.<sub>2</sub> + 642 + 150 + 736 + 2 × 121 = 2 × 364 + 2493<br>numbers &amp; signs (1), factors of 2 (1)<br><br>I.E.<sub>2</sub> = <b>(+)1451 (kJ mol<sup>−1</sup>)</b> (1)", "Ignore units even if wrong<br>+1208, +1087, +1572 each score one only", "3", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2007-june-chm5-q1c",
        "question": "1(c)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.8"],
        "skills": ["calculation"],
        "summary": "Calculate the enthalpy of solution of magnesium chloride using hydration enthalpies (-1920 and -364 kJ mol-1) and lattice enthalpy.",
        "figures": ["img/2007-june-chm5/fig-q1-cycle-table.jpg"],
        "ms_rows": [
            ("1(c)", "Δ<i>H</i> = −Δ<i>H</i>(lattice formation) + ΣΔ<i>H</i>(hydration) <i>or</i> cycle with state symbols / numbers / labels (1)<br><br>= +2493 − 1920 − 2 × 364 (1)<br><br>= <b>−155 (kJ mol<sup>−1</sup>)</b> (1)", "MgCl scores zero; +155 scores 1/3", "3", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2007-june-chm5-q1di",
        "question": "1(d)(i)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.8"],
        "skills": ["explanation"],
        "summary": "Explain why ammonium chloride dissolves spontaneously in water even though its enthalpy of solution is +15 kJ mol-1 (endothermic).",
        "figures": [],
        "ms_rows": [
            ("1(d)(i)", "Increase in disorder on dissolving <i>or</i> Δ<i>S</i> positive (1)<br><br>Δ<i>G</i> negative <i>or</i> <i>T</i>Δ<i>S</i> &gt; Δ<i>H</i> (1)", "-", "2", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2007-june-chm5-q1dii",
        "question": "1(d)(ii)",
        "marks": 5,
        "page": 5,
        "topics": ["3.1.4", "3.1.8"],
        "skills": ["calculation"],
        "summary": "Calculate the temperature change and final temperature when 2.0 g NH4Cl dissolves in 50 g water at 20 °C (c = 4.2 J K-1 g-1).",
        "figures": [],
        "ms_rows": [
            ("1(d)(ii)", "Moles NH<sub>4</sub>Cl = 2.0 / 53.5 = 0.0374 (1)<br><br>Heat absorbed = 15 × 0.0374 = 0.561 (kJ) (1)<br><br><i>Q</i> = <i>mc</i>Δ<i>T</i> (1)<br><br>Δ<i>T</i> = (0.561 × 1000) / (50 × 4.2) = <b>2.6 °C</b> (allow 2.5 to 2.7; can use 52) (1)<br><br>Final temperature = 20 − 2.6 = <b>17.4 °C</b> (1)", "wrong compound loses first 2, wrong <i>M</i><sub>r</sub> loses 1; at least 2 sig figs; final T = 20 − previous ans (must be &lt; 20); penalise wrong units for temperature", "5", "AO2 / 3.1.4")
        ]
    },
    # Q2 (14 marks, PDF p.6-7)
    {
        "id": "2007-june-chm5-q2a",
        "question": "2(a)",
        "marks": 8,
        "page": 6,
        "topics": ["3.1.8"],
        "skills": ["calculation"],
        "summary": "Calculate ΔH, ΔS and ΔG at 298 K for Al2O3(s) + 3C(s) -> 2Al(s) + 3CO(g) and suggest why it is not feasible at 298 K.",
        "figures": [],
        "ms_rows": [
            ("2(a)", "Δ<i>H</i> = ΣΔ<i>H</i><sub>f</sub>(products) − ΣΔ<i>H</i><sub>f</sub>(reactants) = 3(−111) − (−1669) (1) = <b>+1336 (kJ mol<sup>−1</sup>)</b> (1)<br><br>Δ<i>S</i> = Σ<i>S</i>(products) − Σ<i>S</i>(reactants) = 2(28) + 3(198) − (51 + 3×6) (1) = <b>+581 (J K<sup>−1</sup> mol<sup>−1</sup>)</b> (1)<br><br>Δ<i>G</i> = Δ<i>H</i> − <i>T</i>Δ<i>S</i> (1) = 1336 − (298 × 581) / 1000 (1) = <b>+1163 (kJ mol<sup>−1</sup>)</b> (allow 1160–1170) (1)<br><br><b>Reason:</b> Δ<i>G</i> is positive (<i>or</i> free energy <i>G</i> increases) (1)", "−1336 scores zero; omitting /1000 is CE; 1163000 with no units scores 3 marks; mark reason independently", "8", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2007-june-chm5-q2b",
        "question": "2(b)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.8"],
        "skills": ["calculation"],
        "summary": "Calculate the temperature above which the reduction of Al2O3 by carbon is feasible.",
        "figures": ["img/2007-june-chm5/fig-q2-table.jpg"],
        "ms_rows": [
            ("2(b)", "When Δ<i>G</i> = 0 &nbsp;<i>or</i>&nbsp; <i>T</i> = Δ<i>H</i> / Δ<i>S</i> (1)<br><br>= (1336 × 1000) / 581 = <b>2299 K</b> (allow 2300 K) (1)", "given data (+906 / +394) produces same answer; allow consequentially; units of T must be present and correct; negative T loses 2nd mark", "2", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2007-june-chm5-q2c",
        "question": "2(c)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.5", "3.1.8"],
        "skills": ["explanation"],
        "summary": "Give one reason why Al2O3 reduction by carbon does not occur significantly until ~1000 K above the minimum feasible temperature.",
        "figures": [],
        "ms_rows": [
            ("2(c)", "<i>E</i><sub>a</sub> too high &nbsp;<i>or</i>&nbsp; reaction too slow", "-", "1", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2007-june-chm5-q2d",
        "question": "2(d)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "State the method and essential conditions used to reduce aluminium oxide on an industrial scale.",
        "figures": [],
        "ms_rows": [
            ("2(d)", "<b>Method:</b> Electrolysis (1)<br><br><b>Conditions:</b> Molten <i>or</i> high T (500–1500 °C) <i>or</i> dissolved (1) in <b>cryolite</b> (1)", "zero if method incorrect, except if \"reduction\" stated lose M1 and mark on; ignore irrelevant conditions", "3", "AO1 / 3.1.7")
        ]
    },
    # Q3 (17 marks, PDF p.8-9)
    {
        "id": "2007-june-chm5-q3ai",
        "question": "3(a)(i)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.11"],
        "skills": ["application"],
        "summary": "Predict the products, if any, when iron metal is mixed with aqueous zinc(II) ions and explain using E° values.",
        "figures": ["img/2007-june-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(a)(i)", "<b>Products:</b> None <i>or</i> No reaction (1)<br><br><b>Explanation:</b> <i>E</i>°(Zn<sup>2+</sup>/Zn) more negative than <i>E</i>°(Fe<sup>2+</sup>/Fe) (allow converse, or cell voltage = −0.32 V) (1)", "If wrong answer do not mark on", "2", "AO2 / 3.1.11")
        ]
    },
    {
        "id": "2007-june-chm5-q3aii",
        "question": "3(a)(ii)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.11"],
        "skills": ["application"],
        "summary": "Predict the products when aqueous iron(III) ions are mixed with aqueous chromium(II) ions and explain using E° values.",
        "figures": ["img/2007-june-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(a)(ii)", "<b>Products:</b> Fe<sup>2+</sup> (1) and Cr<sup>3+</sup> (1)<br><br><b>Explanation:</b> <i>E</i>°(Fe<sup>3+</sup>/Fe<sup>2+</sup>) more positive than <i>E</i>°(Cr<sup>3+</sup>/Cr<sup>2+</sup>) (or cell voltage = +1.18 V) (1)", "apply list principle after looking at two answers; need one correct species to mark on", "3", "AO2 / 3.1.11")
        ]
    },
    {
        "id": "2007-june-chm5-q3b",
        "question": "3(b)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.11"],
        "skills": ["calculation", "application"],
        "summary": "Calculate the e.m.f. and deduce an overall equation for the cell Zn(s)|Zn2+(aq)||Cr3+(aq),Cr2+(aq)|Pt.",
        "figures": ["img/2007-june-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(b)", "<b>e.m.f.</b> = −0.41 − (−0.76) = <b>(+)0.35 (V)</b> (1)<br><br><b>Equation:</b> Zn + 2Cr<sup>3+</sup> → Zn<sup>2+</sup> + 2Cr<sup>2+</sup> (1)", "Ignore state symbols", "2", "AO2 / 3.1.11")
        ]
    },
    {
        "id": "2007-june-chm5-q3c",
        "question": "3(c)",
        "marks": 5,
        "page": 9,
        "topics": ["3.1.12", "3.2.6"],
        "skills": ["calculation"],
        "summary": "Calculate the pH of a 0.500 mol dm-3 solution of [Cr(H2O)6]3+(aq) given Ka = 1.15 x 10^-4 mol dm-3.",
        "figures": [],
        "ms_rows": [
            ("3(c)", "<i>K</i><sub>a</sub> = [H<sup>+</sup>][A<sup>−</sup>]/[HA] &nbsp;<i>or</i>&nbsp; [H<sup>+</sup>]<sup>2</sup>/[HA] (1)<br><br>[H<sup>+</sup>] = √(<i>K</i><sub>a</sub>[HA]) = √(1.15 × 10<sup>−4</sup> × 0.5) (1)<br><br>= <b>7.58 × 10<sup>−3</sup> mol dm<sup>−3</sup></b> (1)<br><br>pH = −log<sub>10</sub>[H<sup>+</sup>] (1)<br><br>pH = <b>2.12</b> (1)", "allow last two marks consequential on wrong [H<sup>+</sup>]; note that 4.24 will score last two marks", "5", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-june-chm5-q3di",
        "question": "3(d)(i)",
        "marks": 2,
        "page": 9,
        "topics": ["3.2.6"],
        "skills": ["recall"],
        "summary": "State the observation(s) and give the formula of the chromium-containing product when an excess of NaOH(aq) is added to [Cr(H2O)6]3+(aq).",
        "figures": [],
        "ms_rows": [
            ("3(d)(i)", "<b>Observation(s):</b> Green solution (1)<br><br><b>Formula:</b> [Cr(OH)<sub>6</sub>]<sup>3−</sup> &nbsp;(<i>or</i> [Cr(H<sub>2</sub>O)(OH)<sub>5</sub>]<sup>2−</sup> &nbsp;<i>or</i>&nbsp; [Cr(H<sub>2</sub>O)<sub>2</sub>(OH)<sub>4</sub>]<sup>−</sup>) (1)", "not blue-green or grey-green", "2", "AO1 / 3.2.6")
        ]
    },
    {
        "id": "2007-june-chm5-q3dii",
        "question": "3(d)(ii)",
        "marks": 3,
        "page": 9,
        "topics": ["3.2.6"],
        "skills": ["recall"],
        "summary": "State the observation(s) and give the formula of the chromium-containing product when Na2CO3(aq) is added to [Cr(H2O)6]3+(aq).",
        "figures": [],
        "ms_rows": [
            ("3(d)(ii)", "<b>Observation(s):</b> Green precipitate (allow grey-green) (1) and bubbles / gas / fizzing / effervescence (1)<br><br><b>Formula:</b> Cr(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub> &nbsp;(<i>or</i> Cr(OH)<sub>3</sub>) (1)", "not \"gives off CO<sub>2</sub>\" for observation mark", "3", "AO1 / 3.2.6")
        ]
    },
    # Q4 (12 marks, PDF p.10)
    {
        "id": "2007-june-chm5-q4a",
        "question": "4(a)",
        "marks": 2,
        "page": 10,
        "topics": ["3.1.3"],
        "skills": ["recall"],
        "summary": "Give the meaning of the term electronegativity.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Ability of an atom <i>or</i> element to attract / withdraw electrons or electron density (1)<br><br>in a covalent bond (1)", "2nd mark consequential on sensible 1st mark (e.g. if atom/element omitted lose M1 but gains M2)", "2", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2007-june-chm5-q4b",
        "question": "4(b)",
        "marks": 3,
        "page": 10,
        "topics": ["3.2.1", "3.1.3"],
        "skills": ["explanation"],
        "summary": "State and explain the trend in electronegativity across Period 3 from Na to Cl.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "<b>Trend:</b> increases <i>or</i> stronger (1)<br><br><b>Explanation:</b> more protons <i>or</i> greater nuclear charge (1); similar / same shielding <i>or</i> electrons in same shell <i>or</i> similar / smaller radius (1)", "Zero if trend is wrong", "3", "AO1 / 3.2.1")
        ]
    },
    {
        "id": "2007-june-chm5-q4ci",
        "question": "4(c)(i)",
        "marks": 2,
        "page": 10,
        "topics": ["3.2.4", "3.1.3"],
        "skills": ["recall"],
        "summary": "Name the main type of bonding in each of the Period 3 oxides MgO and P4O10.",
        "figures": [],
        "ms_rows": [
            ("4(c)(i)", "<b>MgO:</b> ionic (1)<br><br><b>P<sub>4</sub>O<sub>10</sub>:</b> covalent (1)", "zero for MgO as a contradiction if mention of molecules; ignore structure info unless contradictory", "2", "AO1 / 3.2.4")
        ]
    },
    {
        "id": "2007-june-chm5-q4cii",
        "question": "4(c)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.3", "3.2.4"],
        "skills": ["explanation"],
        "summary": "Explain how the type of bonding in P4O10 can be predicted by a consideration of electronegativity.",
        "figures": [],
        "ms_rows": [
            ("4(c)(ii)", "Electronegativity difference small <i>or</i> electronegativities similar (NOT same)<br><i>or</i> converse: big difference in electronegativity leads to ionic bonding", "consequential on covalent for P<sub>4</sub>O<sub>10</sub>", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2007-june-chm5-q4d",
        "question": "4(d)",
        "marks": 2,
        "page": 10,
        "topics": ["3.2.4"],
        "skills": ["recall"],
        "summary": "Write equations for the reaction of Na2O and of SO2 with water.",
        "figures": [],
        "ms_rows": [
            ("4(d)", "Na<sub>2</sub>O + H<sub>2</sub>O → 2Na<sup>+</sup> + 2OH<sup>−</sup> &nbsp;(<i>or</i> 2NaOH) (1)<br><br>SO<sub>2</sub> + H<sub>2</sub>O → H<sub>2</sub>SO<sub>3</sub> &nbsp;(<i>or</i> acid correctly ionised) (1)", "-", "2", "AO1 / 3.2.4")
        ]
    },
    {
        "id": "2007-june-chm5-q4e",
        "question": "4(e)",
        "marks": 1,
        "page": 10,
        "topics": ["3.2.4"],
        "skills": ["recall"],
        "summary": "Write an equation for the reaction of MgO with dilute hydrochloric acid.",
        "figures": [],
        "ms_rows": [
            ("4(e)", "MgO + 2HCl → MgCl<sub>2</sub> + H<sub>2</sub>O &nbsp;(<i>or</i> MgO + 2H<sup>+</sup> → Mg<sup>2+</sup> + H<sub>2</sub>O)", "-", "1", "AO1 / 3.2.4")
        ]
    },
    {
        "id": "2007-june-chm5-q4f",
        "question": "4(f)",
        "marks": 1,
        "page": 10,
        "topics": ["3.2.4"],
        "skills": ["recall"],
        "summary": "Write an equation for the reaction of P4O10 with an excess of aqueous sodium hydroxide.",
        "figures": [],
        "ms_rows": [
            ("4(f)", "P<sub>4</sub>O<sub>10</sub> + 12NaOH → 4Na<sub>3</sub>PO<sub>4</sub> + 6H<sub>2</sub>O<br><i>or</i> P<sub>4</sub>O<sub>10</sub> + 12OH<sup>−</sup> → 4PO<sub>4</sub><sup>3−</sup> + 6H<sub>2</sub>O", "ignore state symbols", "1", "AO1 / 3.2.4")
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
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.8"
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

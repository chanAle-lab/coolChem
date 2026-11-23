import json
import os
import sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2009-june-chm4"
QP_PDF = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472598951_fd5640a0.pdf"
IMG_DIR = os.path.join(ROOT, "img", PAPER_ID)
MS_DIR = os.path.join(IMG_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2009,
    "series": "June",
    "unit": "CHM4",
    "level": "A",
    "title": "CHM4 – Further Physical and Organic Chemistry (Section A)",
    "date": "2009-06-11",
    "totalMarks": 90,
    "duration": "1 hour 30 minutes",
}

Q1A_FIG = f"img/{PAPER_ID}/fig-q1a-table.jpg"
Q2_FIG = f"img/{PAPER_ID}/fig-q2-eqn.jpg"
Q3B_FIG = f"img/{PAPER_ID}/fig-q3b-stem.jpg"
Q4D_FIG = f"img/{PAPER_ID}/fig-q4d-z.jpg"
Q4E_FIG = f"img/{PAPER_ID}/fig-q4e-alanine.jpg"
Q5_FIG = f"img/{PAPER_ID}/fig-q5-scheme.jpg"

QUESTIONS = [
    # Q1 (7 marks) - pages 2, 5
    {
        "id": f"{PAPER_ID}-q1ai",
        "questionNumber": "1(a)(i)",
        "page": 2,
        "marks": 3,
        "topics": ["Kinetics"],
        "skills": ["Calculation"],
        "summary": "Complete the rate data table for the reaction between P and Q (rate = k[P][Q]2).",
        "specRef": "3.4.1",
        "ms_label": "1(a)(i)",
        "ms_ans": "Expt 2: 1.8 &times; 10<sup>&minus;3</sup> (or 6.75 / <i>k</i>)<br><br>Expt 3: 8.1 &times; 10<sup>&minus;5</sup> (or <i>k</i> &times; 2.16 &times; 10<sup>&minus;8</sup>)<br><br>Expt 4: 6.7 &times; 10<sup>&minus;4</sup> (or &radic;(1.67 &times; 10<sup>&minus;3</sup> / <i>k</i>); allow 0.7 &times; 10<sup>&minus;3</sup> or 7 &times; 10<sup>&minus;4</sup>)",
        "ms_extra": "If rounded <i>k</i> = 3.8 &times; 10<sup>3</sup> used: allow 1.78 &times; 10<sup>&minus;3</sup>, 8.2 &times; 10<sup>&minus;5</sup> (or 8.4 &times; 10<sup>&minus;5</sup>), 6.6 &times; 10<sup>&minus;4</sup>",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1aii",
        "questionNumber": "1(a)(ii)",
        "page": 2,
        "marks": 3,
        "topics": ["Kinetics"],
        "skills": ["Calculation"],
        "summary": "Calculate the rate constant k from Experiment 1 and state its units.",
        "specRef": "3.4.1",
        "ms_label": "1(a)(ii)",
        "ms_ans": "<i>k</i> = rate / ([P][Q]<sup>2</sup>) = 1.8 &times; 10<sup>&minus;5</sup> / ((1.2 &times; 10<sup>&minus;3</sup>)(2.0 &times; 10<sup>&minus;3</sup>)<sup>2</sup>)<br><br>= 3750 or 3.75 &times; 10<sup>3</sup> or 3.8 &times; 10<sup>3</sup><br><br>mol<sup>&minus;2</sup> dm<sup>6</sup> s<sup>&minus;1</sup>",
        "ms_extra": "Any order for units",
        "ms_marks": "1<br><br>1<br><br>1",
        "figures": [Q1A_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1b",
        "questionNumber": "1(b)",
        "page": 5,
        "marks": 1,
        "topics": ["Kinetics"],
        "skills": ["Application"],
        "summary": "Sketch the relationship between initial rate and initial [R] for a zero-order reaction.",
        "specRef": "3.4.1",
        "ms_label": "1(b)",
        "ms_ans": "Horizontal straight line",
        "ms_extra": "Be generous, they need not use a ruler",
        "ms_marks": "1",
    },
    # Q2 (10 marks) - pages 6-7
    {
        "id": f"{PAPER_ID}-q2a",
        "questionNumber": "2(a)",
        "page": 6,
        "marks": 3,
        "topics": ["Equilibria"],
        "skills": ["Calculation"],
        "summary": "Calculate the mole fraction of NO2 in the equilibrium mixture formed from 1.20 mol N2O4 containing 0.36 mol NO2.",
        "specRef": "3.4.2",
        "ms_label": "2(a)",
        "ms_ans": "mol N<sub>2</sub>O<sub>4</sub> = 1.20 &minus; &frac12;(0.36) = 1.0(2)<br><br>total moles = 1.0(2) + 0.36 = 1.36 or 1.38 or 1.4<br><br>mol fraction of NO<sub>2</sub> = 0.36 / 1.38 = 0.26 (allow 6/23 or 0.257 &ndash; 0.264)",
        "ms_extra": "",
        "ms_marks": "M1<br><br>M2<br><br>M3",
    },
    {
        "id": f"{PAPER_ID}-q2bi",
        "questionNumber": "2(b)(i)",
        "page": 6,
        "marks": 1,
        "topics": ["Equilibria"],
        "skills": ["Knowledge & Recall"],
        "summary": "Write a general expression relating partial pressure of a gas to its mole fraction.",
        "specRef": "3.4.2",
        "ms_label": "2(b)(i)",
        "ms_ans": "pp = mol fract &times; Total Pressure",
        "ms_extra": "Or allow symbols",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2bii",
        "questionNumber": "2(b)(ii)",
        "page": 6,
        "marks": 2,
        "topics": ["Equilibria"],
        "skills": ["Calculation"],
        "summary": "Calculate the partial pressures of NO2 and N2O4 when x(NO2) = 0.28 at 180 kPa total pressure.",
        "specRef": "3.4.2",
        "ms_label": "2(b)(ii)",
        "ms_ans": "ppNO<sub>2</sub> = 0.28 &times; 180 = 50(.4)<br><br>ppN<sub>2</sub>O<sub>4</sub> = 180 &minus; 50.4 = 129.6 or 130",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2ci",
        "questionNumber": "2(c)(i)",
        "page": 7,
        "marks": 1,
        "topics": ["Equilibria"],
        "skills": ["Knowledge & Recall"],
        "summary": "Write an expression for Kp for the equilibrium N2O4(g) <=> 2NO2(g).",
        "specRef": "3.4.2",
        "ms_label": "2(c)(i)",
        "ms_ans": "<i>K</i><sub>p</sub> = (<i>p</i><sub>NO<sub>2</sub></sub>)<sup>2</sup> / <i>p</i><sub>N<sub>2</sub>O<sub>4</sub></sub>",
        "ms_extra": "Penalise [ ] but mark on",
        "ms_marks": "1",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2cii",
        "questionNumber": "2(c)(ii)",
        "page": 7,
        "marks": 3,
        "topics": ["Equilibria"],
        "skills": ["Calculation"],
        "summary": "Calculate Kp and give its units when p(NO2) = 49.6 kPa and p(N2O4) = 132.0 kPa.",
        "specRef": "3.4.2",
        "ms_label": "2(c)(ii)",
        "ms_ans": "49.6<sup>2</sup> / 132.0<br><br>= 18.6 or 19<br><br>kPa",
        "ms_extra": "Conseq on their <i>K</i><sub>p</sub>",
        "ms_marks": "1<br><br>1<br><br>1",
        "figures": [Q2_FIG],
    },
    # Q3 (16 marks) - pages 8-9
    {
        "id": f"{PAPER_ID}-q3ai",
        "questionNumber": "3(a)(i)",
        "page": 8,
        "marks": 1,
        "topics": ["Acids & Bases"],
        "skills": ["Knowledge & Recall"],
        "summary": "Write an expression for the term pH.",
        "specRef": "3.4.3",
        "ms_label": "3(a)(i)",
        "ms_ans": "pH = &minus;log[H<sup>+</sup>]",
        "ms_extra": "Penalise ( ) once in question",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3aii",
        "questionNumber": "3(a)(ii)",
        "page": 8,
        "marks": 2,
        "topics": ["Acids & Bases"],
        "skills": ["Calculation"],
        "summary": "Calculate the pH of the solution formed when 5.0 cm3 of 0.135 mol dm-3 HCl is added to 995 cm3 of water.",
        "specRef": "3.4.3",
        "ms_label": "3(a)(ii)",
        "ms_ans": "mol HCl = (5.0 &times; 10<sup>&minus;3</sup>) &times; 0.135 = 6.75 &times; 10<sup>&minus;4</sup> (or 6.8 &times; 10<sup>&minus;4</sup>)<br><br>pH = 3.17",
        "ms_extra": "Penalise pH to &lt;2 dp once in the paper",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3bi",
        "questionNumber": "3(b)(i)",
        "page": 8,
        "marks": 1,
        "topics": ["Acids & Bases"],
        "skills": ["Knowledge & Recall"],
        "summary": "Write an expression for Ka for 2-chloropropanoic acid (CH3CHClCOOH).",
        "specRef": "3.4.3",
        "ms_label": "3(b)(i)",
        "ms_ans": "<i>K</i><sub>a</sub> = [H<sup>+</sup>][CH<sub>3</sub>CHClCOO<sup>&minus;</sup>] / [CH<sub>3</sub>CHClCOOH]",
        "ms_extra": "Allow molecular formulae; not allow [H<sup>+</sup>][A<sup>&minus;</sup>]/[HA]",
        "ms_marks": "M1",
    },
    {
        "id": f"{PAPER_ID}-q3bii",
        "questionNumber": "3(b)(ii)",
        "page": 8,
        "marks": 3,
        "topics": ["Acids & Bases"],
        "skills": ["Calculation"],
        "summary": "Calculate the pH of a 0.350 mol dm-3 solution of 2-chloropropanoic acid (Ka = 1.48 x 10-3).",
        "specRef": "3.4.3",
        "ms_label": "3(b)(ii)",
        "ms_ans": "<i>K</i><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [CH<sub>3</sub>CHClCOOH]<br><br>[H<sup>+</sup>] = &radic;(1.48 &times; 10<sup>&minus;3</sup> &times; 0.350) = 2.28 &times; 10<sup>&minus;2</sup><br><br>pH = 1.64",
        "ms_extra": "Use of quadratic gives 1.66",
        "ms_marks": "M2<br><br>M3<br><br>M4",
        "figures": [Q3B_FIG],
    },
    {
        "id": f"{PAPER_ID}-q3c",
        "questionNumber": "3(c)",
        "page": 9,
        "marks": 3,
        "topics": ["Acids & Bases", "Equilibria"],
        "skills": ["Explanation"],
        "summary": "Predict and explain how the pH of 2-chloropropanoic acid changes when temperature is increased.",
        "specRef": "3.4.3",
        "ms_label": "3(c)",
        "ms_ans": "Decrease (mark on if incorrect)<br><br>Increase <i>T</i> increases dissociation / favours forward reaction / moves to right / favours endothermic reaction<br><br>&there4; increases [H<sup>+</sup>] or more H<sup>+</sup>",
        "ms_extra": "",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3d",
        "questionNumber": "3(d)",
        "page": 9,
        "marks": 3,
        "topics": ["Nomenclature & Isomerism"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of stereoisomerism shown by 2-chloropropanoic acid and state how to distinguish its stereoisomers.",
        "specRef": "3.4.5",
        "ms_label": "3(d)",
        "ms_ans": "Optical<br><br>(plane) polarised light or polarimeter<br><br>(light) rotated in opposite (or wtte) directions",
        "ms_extra": "QOL; not just in different directions",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3e",
        "questionNumber": "3(e)",
        "page": 9,
        "marks": 3,
        "topics": ["Acids & Bases"],
        "skills": ["Calculation"],
        "summary": "Calculate Ka for propanoic acid in a buffer of pH 4.69 containing 0.15 mol propanoic acid and 0.10 mol sodium propanoate.",
        "specRef": "3.4.3",
        "ms_label": "3(e)",
        "ms_ans": "[H<sup>+</sup>] = 10<sup>&minus;4.69</sup> = 2.0(4) &times; 10<sup>&minus;5</sup> (or p<i>K</i><sub>a</sub> = 4.69 &minus; log(0.10/0.15))<br><br><i>K</i><sub>a</sub> = (2.04 &times; 10<sup>&minus;5</sup>)(0.10) / (0.15) (or p<i>K</i><sub>a</sub> = 4.86 or 4.87)<br><br>= 1.36 &times; 10<sup>&minus;5</sup> (allow 1.3 &times; 10<sup>&minus;5</sup> to 1.4 &times; 10<sup>&minus;5</sup>)",
        "ms_extra": "Ignore units",
        "ms_marks": "M1<br><br>M2<br><br>M3",
    },
    # Q4 (17 marks) - pages 10-11
    {
        "id": f"{PAPER_ID}-q4ai",
        "questionNumber": "4(a)(i)",
        "page": 10,
        "marks": 1,
        "topics": ["Acids & Bases"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give the meaning of the term Bronsted-Lowry base.",
        "specRef": "3.4.3",
        "ms_label": "4(a)(i)",
        "ms_ans": "proton acceptor",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4aii",
        "questionNumber": "4(a)(ii)",
        "page": 10,
        "marks": 3,
        "topics": ["Amines", "Acids & Bases"],
        "skills": ["Explanation"],
        "summary": "State and explain which of ammonia and butylamine is the stronger base.",
        "specRef": "3.4.9",
        "ms_label": "4(a)(ii)",
        "ms_ans": "butylamine<br><br>alkyl group is electron-releasing / increases e<sup>&minus;</sup> density on N / has (+) inductive effect<br><br>lone pair more available",
        "ms_extra": "Or formula; if wrong, no further marks in (a)(ii)",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4b",
        "questionNumber": "4(b)",
        "page": 10,
        "marks": 1,
        "topics": ["Amines", "Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Draw the structure of the tertiary amine which is an isomer of butylamine.",
        "specRef": "3.4.9",
        "ms_label": "4(b)",
        "ms_ans": "CH<sub>3</sub>CH<sub>2</sub>&ndash;N(CH<sub>3</sub>)<sub>2</sub>",
        "ms_extra": "Allow C<sub>2</sub>H<sub>5</sub>",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4ci",
        "questionNumber": "4(c)(i)",
        "page": 10,
        "marks": 1,
        "topics": ["Amines"],
        "skills": ["Application"],
        "summary": "Draw the structure of the species formed when CH3(CH2)17NH2 reacts with excess CH3Br.",
        "specRef": "3.4.9",
        "ms_label": "4(c)(i)",
        "ms_ans": "CH<sub>3</sub>(CH<sub>2</sub>)<sub>17</sub>N<sup>+</sup>(CH<sub>3</sub>)<sub>3</sub> (Br<sup>&minus;</sup>)",
        "ms_extra": "Mark part (ii) independent of part (i)",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4cii",
        "questionNumber": "4(c)(ii)",
        "page": 10,
        "marks": 2,
        "topics": ["Amines"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of compound formed in (c)(i) and give a use for such compounds.",
        "specRef": "3.4.9",
        "ms_label": "4(c)(ii)",
        "ms_ans": "quaternary ammonium (salt) or tetraalkylammonium (salt)<br><br>(cationic) surfactant / fabric softener / water repellent / fungicide / emulsifier / hair conditioner / detergent",
        "ms_extra": "QOL",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4di",
        "questionNumber": "4(d)(i)",
        "page": 10,
        "marks": 1,
        "topics": ["Carbonyls & Carboxylic Acids", "Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Name compound Z (CH3CONHCH3).",
        "specRef": "3.4.7",
        "ms_label": "4(d)(i)",
        "ms_ans": "<u>N</u>-methylethanamide",
        "ms_extra": "Allow <u>N</u>-methylacetamide",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4dii",
        "questionNumber": "4(d)(ii)",
        "page": 11,
        "marks": 5,
        "topics": ["Carbonyls & Carboxylic Acids", "Reaction Mechanisms"],
        "skills": ["Application"],
        "summary": "Name and outline a mechanism for the reaction in which Z is formed from CH3NH2 and CH3COCl.",
        "specRef": "3.4.7",
        "ms_label": "4(d)(ii)",
        "ms_ans": "(Nucleophilic) addition&ndash;elimination<br><br>Mechanism:<br>&bull; M1: curly arrow from N lone pair of CH<sub>3</sub>NH<sub>2</sub> to carbonyl C of CH<sub>3</sub>COCl<br>&bull; M2: curly arrow from C=O to O<br>&bull; M3: tetrahedral intermediate with O<sup>&minus;</sup>, Cl, and &minus;N<sup>+</sup>H<sub>2</sub>CH<sub>3</sub><br>&bull; M4: 3 arrows (O<sup>&minus;</sup> lone pair back to C=O, C&ndash;Cl breaking, N&ndash;H breaking)",
        "ms_extra": "Only allow M4 after correct or very close M3; lose M4 for Cl<sup>&minus;</sup> removing H<sup>+</sup>",
        "ms_marks": "1<br><br>4",
        "figures": [Q4D_FIG],
    },
    {
        "id": f"{PAPER_ID}-q4e",
        "questionNumber": "4(e)",
        "page": 11,
        "marks": 3,
        "topics": ["Amino Acids & Polymers"],
        "skills": ["Application"],
        "summary": "Draw the species formed when alanine dissolves in water, reacts with HCl, and reacts with methanol/H2SO4.",
        "specRef": "3.4.10",
        "ms_label": "4(e)",
        "ms_ans": "In water: <sup>+</sup>H<sub>3</sub>N&ndash;CH(CH<sub>3</sub>)&ndash;COO<sup>&minus;</sup><br><br>With HCl: <sup>+</sup>H<sub>3</sub>N&ndash;CH(CH<sub>3</sub>)&ndash;COOH<br><br>With methanol/conc H<sub>2</sub>SO<sub>4</sub>: H<sub>2</sub>N&ndash;CH(CH<sub>3</sub>)&ndash;COOCH<sub>3</sub> (or <sup>+</sup>H<sub>3</sub>N&ndash;CH(CH<sub>3</sub>)&ndash;COOCH<sub>3</sub>)",
        "ms_extra": "Allow &minus;CO<sub>2</sub>H / &minus;CO<sub>2</sub>CH<sub>3</sub>",
        "ms_marks": "1<br><br>1<br><br>1",
        "figures": [Q4E_FIG],
    },
    # Q5 (10 marks) - pages 12-13
    {
        "id": f"{PAPER_ID}-q5ai",
        "questionNumber": "5(a)(i)",
        "page": 12,
        "marks": 3,
        "topics": ["Aromatic Chemistry"],
        "skills": ["Knowledge & Recall", "Application"],
        "summary": "Identify two other substances needed with ethene in Step 1 and write an equation forming CH3CH2+.",
        "specRef": "3.4.8",
        "ms_label": "5(a)(i)",
        "ms_ans": "HCl or HBr<br><br>AlCl<sub>3</sub> or AlBr<sub>3</sub> / FeCl<sub>3</sub> / FeBr<sub>3</sub><br><br>H<sub>2</sub>C=CH<sub>2</sub> + HCl + AlCl<sub>3</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub><sup>+</sup> + AlCl<sub>4</sub><sup>&minus;</sup>",
        "ms_extra": "Two substances in either order; allow C<sub>2</sub>H<sub>4</sub>",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q5aii",
        "questionNumber": "5(a)(ii)",
        "page": 12,
        "marks": 4,
        "topics": ["Aromatic Chemistry", "Reaction Mechanisms"],
        "skills": ["Application"],
        "summary": "Name and outline a mechanism for the reaction of CH3CH2+ with benzene in Step 1.",
        "specRef": "3.4.8",
        "ms_label": "5(a)(ii)",
        "ms_ans": "electrophilic substitution<br><br>Mechanism:<br>&bull; M1: curly arrow from within benzene hexagon to C of <sup>+</sup>CH<sub>2</sub>CH<sub>3</sub><br>&bull; M2: horseshoe intermediate with + charge and H/CH<sub>2</sub>CH<sub>3</sub><br>&bull; M3: curly arrow from C&ndash;H bond back into hexagon",
        "ms_extra": "Not Friedel&ndash;Crafts; allow Kekul&eacute; structures",
        "ms_marks": "1<br><br>3",
        "figures": [Q5_FIG],
    },
    {
        "id": f"{PAPER_ID}-q5b",
        "questionNumber": "5(b)",
        "page": 12,
        "marks": 1,
        "topics": ["Aromatic Chemistry", "Alkenes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give one reason why ethene is preferred over chloroethane for making ethylbenzene.",
        "specRef": "3.4.8",
        "ms_label": "5(b)",
        "ms_ans": "chloroethane usually made from ethene (or more difficult to make) / ethene is a (by)product of cracking",
        "ms_extra": "Not just cheaper; not just ethene is more readily available",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q5c",
        "questionNumber": "5(c)",
        "page": 13,
        "marks": 2,
        "topics": ["Amino Acids & Polymers", "Alkenes"],
        "skills": ["Application", "Knowledge & Recall"],
        "summary": "Draw the repeating unit of poly(phenylethene) and name the type of polymerisation.",
        "specRef": "3.4.10",
        "ms_label": "5(c)",
        "ms_ans": "&ndash;CH(C<sub>6</sub>H<sub>5</sub>)&ndash;CH<sub>2</sub>&ndash; (with trailing bonds)<br><br>Addition (or radical or step)",
        "ms_extra": "QOL; ignore <i>n</i> or brackets, must have trailing bonds; not additional",
        "ms_marks": "1<br><br>1",
        "figures": [Q5_FIG],
    },
]


def extract_figures():
    doc = fitz.open(QP_PDF)
    crops = [
        (1, fitz.Rect(42, 145, 555, 390), Q1A_FIG),
        (5, fitz.Rect(42, 68, 555, 118), Q2_FIG),
        (7, fitz.Rect(42, 306, 555, 342), Q3B_FIG),
        (9, fitz.Rect(42, 650, 555, 725), Q4D_FIG),
        (10, fitz.Rect(42, 350, 555, 420), Q4E_FIG),
        (11, fitz.Rect(42, 68, 555, 188), Q5_FIG),
    ]
    for p_idx, rect, rel_path in crops:
        pix = doc[p_idx].get_pixmap(clip=rect, dpi=200)
        pix.save(os.path.join(ROOT, rel_path))
        print(f"Saved figure {rel_path}")


def main():
    extract_figures()
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    papers = [p for p in db["papers"] if p["id"] != PAPER_ID]
    papers.append(PAPER_OBJ)
    db["papers"] = papers

    questions = [q for q in db["questions"] if q.get("paper") != PAPER_ID]

    for q in QUESTIONS:
        q_slug = q["id"].split("-")[-1]
        ms_rel = f"img/{PAPER_ID}/ms/{q_slug}.png"
        ms_abs = os.path.join(ROOT, ms_rel)
        render_official_markscheme_image(
            question_label=q["ms_label"],
            answers_html=q["ms_ans"],
            extra_html=q["ms_extra"],
            marks=q["ms_marks"],
            spec_ref=q["specRef"],
            output_path=ms_abs,
        )
        questions.append({
            "id": q["id"],
            "paper": PAPER_ID,
            "year": PAPER_OBJ["year"],
            "series": PAPER_OBJ["series"],
            "unit": PAPER_OBJ["unit"],
            "level": PAPER_OBJ["level"],
            "question": q["questionNumber"],
            "questionNumber": q["questionNumber"],
            "page": q["page"],
            "marks": q["marks"],
            "topics": q["topics"],
            "skills": q["skills"],
            "summary": q["summary"],
            "specRef": q["specRef"],
            "image": f"img/{PAPER_ID}/{q_slug}.jpg",
            "markscheme": ms_rel,
            "figures": q.get("figures", []),
        })

    db["questions"] = questions
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    total_m = sum(q["marks"] for q in QUESTIONS)
    print(f"Ingested {PAPER_ID}: {len(QUESTIONS)} questions, {total_m} marks.")


if __name__ == "__main__":
    main()

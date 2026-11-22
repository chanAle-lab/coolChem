"""
Ingestion script for 2003 June CHM5 (Section A only)
Excludes old-spec Section B essay questions (Q6, Q7, Q8, Q9).
Renders official AQA modern mark scheme tables and precision cropped question images.
"""
import os
import re
import json
import fitz
from PIL import Image
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023344_5bb64768.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-june-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-june-chm5",
    "year": 2003,
    "series": "June",
    "date": "2003-06-24",
    "code": "CHM5",
    "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
    "level": "A2",
    "spec": "AQA Chemistry",
    "totalMarks": 120,
    "duration": "2 hours"
}

QUESTIONS_DEF = [
    # Page 4 (Exam page 5): Q1
    ("2003-june-chm5-q1ai", "1(a)(i)", 4, 180, 275, 1, ["3.2.4"], ["recall"], "Identify oxide which can form a solution with pH less than 3."),
    ("2003-june-chm5-q1aii", "1(a)(ii)", 4, 280, 365, 1, ["3.2.4"], ["recall"], "Identify oxide which can form a solution with pH greater than 12."),
    ("2003-june-chm5-q1bi", "1(b)(i)", 4, 370, 465, 1, ["3.2.4"], ["recall"], "Equation for reaction between MgO and HNO3."),
    ("2003-june-chm5-q1bii", "1(b)(ii)", 4, 470, 560, 1, ["3.2.4"], ["recall"], "Equation for reaction between SiO2 and NaOH."),
    ("2003-june-chm5-q1biii", "1(b)(iii)", 4, 565, 660, 1, ["3.2.4"], ["recall"], "Equation for reaction between Na2O and H3PO4."),
    ("2003-june-chm5-q1c", "1(c)", 4, 665, 840, 4, ["3.2.4"], ["explanation"], "Explain why P4O10 vaporised by gentle heat but SiO2 cannot."),

    # Page 5 (Exam page 6): Q2(a)-(b)(i)
    ("2003-june-chm5-q2ai", "2(a)(i)", 5, 80, 215, 2, ["3.2.5"], ["recall"], "Reagents for conversion of [Cr(H2O)6]3+ to CrO4 2-."),
    ("2003-june-chm5-q2aii", "2(a)(ii)", 5, 220, 285, 2, ["3.2.5"], ["recall"], "Reagents for conversion of VO2+ to [V(H2O)6]2+."),
    ("2003-june-chm5-q2aiii", "2(a)(iii)", 5, 290, 375, 1, ["3.2.5"], ["recall"], "Reagent for conversion of [Ag(NH3)2]+ to Ag(s)."),
    ("2003-june-chm5-q2bi", "2(b)(i)", 5, 380, 785, 3, ["3.1.7"], ["recall"], "Half-equations and overall equation for oxidation of H2O2 by manganate(VII)."),

    # Page 6 (Exam page 7): Q2(b)(ii)
    ("2003-june-chm5-q2bii", "2(b)(ii)", 6, 80, 480, 5, ["3.1.2", "3.1.7"], ["calculation"], "Calculate concentration in g dm-3 of hydrogen peroxide from titration with KMnO4."),

    # Page 7 (Exam page 8): Q3(a)-(c)
    ("2003-june-chm5-q3ai", "3(a)(i)", 7, 80, 215, 2, ["3.2.5"], ["recall"], "Explain the meaning of the term bidentate ligand."),
    ("2003-june-chm5-q3aii", "3(a)(ii)", 7, 220, 580, 3, ["3.2.5"], ["drawing"], "Sketch structure of octahedral complex ion formed by Fe3+ with C2O4 2- and state charge."),
    ("2003-june-chm5-q3b", "3(b)", 7, 585, 705, 2, ["3.2.5"], ["recall"], "Explain the meaning of the term chelate effect."),
    ("2003-june-chm5-q3ci", "3(c)(i)", 7, 710, 810, 1, ["3.2.5"], ["recall"], "Formula of linear complex formed when excess conc HCl added to AgCl."),
    ("2003-june-chm5-q3cii", "3(c)(ii)", 7, 815, 915, 1, ["3.2.5"], ["explanation"], "Why metal(II) ions do not usually form octahedral complexes with Cl- ligands."),

    # Page 8 (Exam page 9): Q3(d)
    ("2003-june-chm5-q3di", "3(d)(i)", 8, 80, 295, 1, ["3.2.5"], ["explanation"], "Suggest why reaction between C2O4 2- and MnO4- is very slow at first."),
    ("2003-june-chm5-q3dii", "3(d)(ii)", 8, 300, 485, 2, ["3.2.5"], ["recall"], "Meaning of autocatalytic and identify the catalyst."),
    ("2003-june-chm5-q3diii", "3(d)(iii)", 8, 490, 680, 2, ["3.2.5"], ["explanation"], "Suggest how catalyst might be involved in the reaction."),

    # Page 9 (Exam page 10): Q4(a)
    ("2003-june-chm5-q4ai", "4(a)(i)", 9, 80, 595, 4, ["3.1.8"], ["drawing"], "Draw fully-labelled Born-Haber cycle for formation of BaCl2 from its elements."),
    ("2003-june-chm5-q4aii", "4(a)(ii)", 9, 600, 910, 5, ["3.1.8"], ["calculation"], "Calculate value for electron affinity of chlorine from Born-Haber cycle data."),

    # Page 10 (Exam page 11): Q4(b)
    ("2003-june-chm5-q4b", "4(b)", 10, 80, 480, 4, ["3.1.8"], ["calculation"], "Calculate lowest temperature at which BaCl2(s) -> Ba(s) + Cl2(g) becomes feasible."),

    # Page 11 (Exam page 12): Q5(a)-(c)(ii)
    ("2003-june-chm5-q5a", "5(a)", 11, 80, 215, 1, ["3.3.2"], ["recall"], "Equation for cracking ethane to form ethene and hydrogen."),
    ("2003-june-chm5-q5b", "5(b)", 11, 220, 435, 3, ["3.1.2"], ["calculation"], "Calculate total moles of gas in 25.0 cm3 sample at 332 K and 110 kPa."),
    ("2003-june-chm5-q5ci", "5(c)(i)", 11, 440, 715, 2, ["3.1.2", "3.3.4"], ["calculation", "recall"], "Calculate moles of bromine added and equation with ethene."),
    ("2003-june-chm5-q5cii", "5(c)(ii)", 11, 720, 885, 1, ["3.1.7"], ["recall"], "Equation for reaction between aqueous potassium iodide and bromine."),

    # Page 12 (Exam page 13): Q5(c)(iii)-(iv)
    ("2003-june-chm5-q5ciii", "5(c)(iii)", 12, 80, 520, 4, ["3.1.2"], ["calculation"], "Calculate moles of I2 formed and moles of Br2 reacted with ethene."),
    ("2003-june-chm5-q5civ", "5(c)(iv)", 12, 525, 715, 2, ["3.1.2"], ["calculation"], "Calculate percentage by moles of ethene in gaseous mixture.")
]

MS_DATA = {
    "2003-june-chm5-q1ai": {
        "answers": "<b>P<sub>4</sub>O<sub>10</sub></b> OR <b>SO<sub>3</sub></b> (1)",
        "extra": "Penalise any wrong answer to zero.",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2003-june-chm5-q1aii": {
        "answers": "<b>Na<sub>2</sub>O</b> (1)",
        "extra": "Penalise any wrong answer to zero.",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2003-june-chm5-q1bi": {
        "answers": "<b>MgO + 2HNO<sub>3</sub> &rarr; Mg(NO<sub>3</sub>)<sub>2</sub> + H<sub>2</sub>O</b> (1)<br>OR ionic: <b>MgO + 2H<sup>+</sup> &rarr; Mg<sup>2+</sup> + H<sub>2</sub>O</b> (1)",
        "extra": "Not: O<sup>2&minus;</sup> + 2H<sup>+</sup> &rarr; H<sub>2</sub>O.",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2003-june-chm5-q1bii": {
        "answers": "<b>2NaOH + SiO<sub>2</sub> &rarr; Na<sub>2</sub>SiO<sub>3</sub> + H<sub>2</sub>O</b> (1)<br>OR ionic: <b>SiO<sub>2</sub> + 2OH<sup>&minus;</sup> &rarr; SiO<sub>3</sub><sup>2&minus;</sup> + H<sub>2</sub>O</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2003-june-chm5-q1biii": {
        "answers": "<b>3Na<sub>2</sub>O + 2H<sub>3</sub>PO<sub>4</sub> &rarr; 2Na<sub>3</sub>PO<sub>4</sub> + 3H<sub>2</sub>O</b> (1)<br>OR ionic: <b>Na<sub>2</sub>O + 2H<sup>+</sup> &rarr; 2Na<sup>+</sup> + H<sub>2</sub>O</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2003-june-chm5-q1c": {
        "answers": "• P<sub>4</sub>O<sub>10</sub> is <b>molecular</b> (structure) OR simple covalent (1)<br>• <b>Weak intermolecular forces</b> OR van der Waals' forces (between molecules) (1)<br>• SiO<sub>2</sub> is <b>macromolecule</b> / giant covalent / giant molecule (1) [not giant lattice]<br>• <b>(Strong) covalent bonds</b> (between atoms) must be broken (1)",
        "extra": "",
        "mark": 4,
        "spec": "3.2.4"
    },
    "2003-june-chm5-q2ai": {
        "answers": "<b>H<sub>2</sub>O<sub>2</sub></b> (1) plus <b>NaOH</b> (1) [or alkaline H<sub>2</sub>O<sub>2</sub> scores 1; Na<sub>2</sub>O<sub>2</sub> scores 2]",
        "extra": "Only allow if H<sub>2</sub>O<sub>2</sub> given.",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q2aii": {
        "answers": "<b>Zn</b> (1) plus <b>HCl / H<sub>2</sub>SO<sub>4</sub></b> (1)",
        "extra": "Only allow if Zn given.<br>Ignore conc.<br>Not: HNO<sub>3</sub>.",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q2aiii": {
        "answers": "<b>A named aldehyde</b> OR a correct formula clearly with an aldehyde group (1) [or Cu &rarr; Mg]",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q2bi": {
        "answers": "• Oxidation: <b>H<sub>2</sub>O<sub>2</sub> &rarr; O<sub>2</sub> + 2H<sup>+</sup> + 2e<sup>&minus;</sup></b> (1)<br>• Reduction: <b>MnO<sub>4</sub><sup>&minus;</sup> + 8H<sup>+</sup> + 5e<sup>&minus;</sup> &rarr; Mn<sup>2+</sup> + 4H<sub>2</sub>O</b> (1)<br>• Overall: <b>2MnO<sub>4</sub><sup>&minus;</sup> + 5H<sub>2</sub>O<sub>2</sub> + 6H<sup>+</sup> &rarr; 2Mn<sup>2+</sup> + 5O<sub>2</sub> + 8H<sub>2</sub>O</b> (1)",
        "extra": "Allow multiples.<br>Overall equation: only allow balanced equation.",
        "mark": 3,
        "spec": "3.1.7"
    },
    "2003-june-chm5-q2bii": {
        "answers": "• Moles MnO<sub>4</sub><sup>&minus;</sup> = <i>mv</i>/1000 = (15.7 &times; 0.0180)/1000 = <b>(2.82 to 2.83) &times; 10<sup>&minus;4</sup> mol</b> (1)<br>• Moles H<sub>2</sub>O<sub>2</sub> = 2.826 &times; 10<sup>&minus;4</sup> &times; (5/2) = <b>(7.06 to 7.08) &times; 10<sup>&minus;4</sup> mol</b> (1)<br>• [H<sub>2</sub>O<sub>2</sub>] = 7.065 &times; 10<sup>&minus;4</sup> &times; (1000 / 20) = <b>(3.53 to 3.54) &times; 10<sup>&minus;2</sup> mol dm<sup>&minus;3</sup></b> (1)<br>• Mass = moles &times; <i>M</i><sub>r</sub> = 3.53 &times; 10<sup>&minus;2</sup> &times; 34 = <b>1.2(0) g dm<sup>&minus;3</sup></b> (2)",
        "extra": "Ignore units.<br>Mark consequential to equation in b(i).<br>If ratio 2/5 used, max 3 (final answer 0.19).<br>NB: If using 3:5 ratio: moles H2O2 = 4.70 to 4.72 &times; 10<sup>&minus;4</sup>, [H2O2] = 2.35 to 2.36 &times; 10<sup>&minus;2</sup>, mass = 0.8(0) g dm<sup>&minus;3</sup>.",
        "mark": 5,
        "spec": "3.1.2"
    },
    "2003-june-chm5-q3ai": {
        "answers": "<b>Two lone pair donor / electron pair donor atoms</b> (2) [1 mark for two lone pairs / electron pairs, 1 mark for donor atoms]",
        "extra": "Allow: forms two coordinate bonds (1).<br>Not: atom with two lone pairs (0).",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q3aii": {
        "answers": "• Correct bidentate ethanedioate ligand structure (1)<br>• Six Fe&minus;O coordinate bonds shown in octahedral arrangement (1)<br>• Correct overall charge <b>3&minus;</b> shown on complex ion (1)",
        "extra": "Penalise any ligand error.<br>Penalise second mark if arrow from Fe shown.<br>Ignore charges on atoms.",
        "mark": 3,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q3b": {
        "answers": "• <b>Substitution of a monodentate ligand by a bi- or multidentate ligand</b> (1)<br>• Giving a <b>more stable complex</b> OR with an <b>increase in entropy / disorder</b> OR forming a ring / cage complex (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q3ci": {
        "answers": "<b>[AgCl<sub>2</sub>]<sup>&minus;</sup></b> (or AgCl<sub>2</sub><sup>&minus;</sup>) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q3cii": {
        "answers": "<b>Chloride / Cl<sup>&minus;</sup> is big / large</b> OR <b>chloride ions repel</b> (1)",
        "extra": "Not: Cl<sub>2</sub>, Cl+, Cl.<br>Allow 'chlorine ion'.",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q3di": {
        "answers": "<b>(Both) ions are negative / ions repel</b> OR <b>high <i>E</i><sub>a</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q3dii": {
        "answers": "• Meaning: <b>A product of the reaction acts as a catalyst</b> (1) [not a self-catalysing reaction]<br>• Catalyst: <b>Mn<sup>2+</sup></b> (or Mn<sup>3+</sup>) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q3diii": {
        "answers": "• Mn<sup>2+</sup> converted into <b>Mn<sup><i>n</i>+</sup></b> (or Mn<sup>2+</sup> oxidised) (1)<br>• Mn<sup><i>n</i>+</sup> / oxidised species then <b>oxidises / reacts with C<sub>2</sub>O<sub>4</sub><sup>2&minus;</sup></b> (1)",
        "extra": "Allow <i>n</i> = 3 to 6.",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-june-chm5-q4ai": {
        "answers": "• <b>Ba(s) + Cl<sub>2</sub>(g)</b> &rarr; Ba(g) + Cl<sub>2</sub>(g) [&Delta;<i>H</i><sub>at</sub>(Ba)] (1)<br>• &rarr; Ba<sup>+</sup>(g) + e<sup>&minus;</sup> + Cl<sub>2</sub>(g) [1st IE(Ba)] &rarr; Ba<sup>2+</sup>(g) + 2e<sup>&minus;</sup> + Cl<sub>2</sub>(g) [2nd IE(Ba)] (1)<br>• &rarr; Ba<sup>2+</sup>(g) + 2e<sup>&minus;</sup> + 2Cl(g) [BE of Cl<sub>2</sub> or 2&Delta;<i>H</i><sub>at</sub>(Cl)] (1)<br>• &rarr; Ba<sup>2+</sup>(g) + 2Cl<sup>&minus;</sup>(g) [2 &times; EA(Cl)] &rarr; BaCl<sub>2</sub>(s) [Lattice formation enthalpy] (1)",
        "extra": "Allow steps shown horizontally.<br>If Ba(g) &rarr; Ba<sup>2+</sup>(g) 1st + 2nd IE scores 2, but Ba(g) &rarr; Ba<sup>2+</sup>(g) IE scores 1.<br>Allow data values if given in place of name.<br>ONLY consider species involved in the step marked.",
        "mark": 4,
        "spec": "3.1.8"
    },
    "2003-june-chm5-q4aii": {
        "answers": "• Born-Haber cycle equation: &Delta;<i>H</i><sub>at</sub>(Ba) + 1st IE(Ba) + 2nd IE(Ba) + 2&Delta;<i>H</i><sub>at</sub>(Cl) + 2EA(Cl) + LE &minus; &Delta;<i>H</i><sub>f</sub>(BaCl<sub>2</sub>) = 0 (1)<br>• +180 + 503 + 965 + 2(122) + 2EA &minus; 2056 + 859 = 0 (1)<br>• 2EA = &minus;695 / 2 (1)<br>• EA = <b>&minus;347.5 kJ mol<sup>&minus;1</sup></b> (range &minus;347 to &minus;348) (2)",
        "extra": "Ignore units.<br>&minus;695 scores (2); &minus;573 scores (1); +(347 to 348) scores (2); +573 scores (0); &minus;(286 to 287) scores (2); +(286 to 287) scores (1).",
        "mark": 5,
        "spec": "3.1.8"
    },
    "2003-june-chm5-q4b": {
        "answers": "• &Delta;<i>S</i> = &Sigma;<i>S</i>(products) &minus; &Sigma;<i>S</i>(reactants) = (63 + 223) &minus; 124 = <b>162 J K<sup>&minus;1</sup> mol<sup>&minus;1</sup></b> (1)<br>• &Delta;<i>G</i> = &Delta;<i>H</i> &minus; <i>T</i>&Delta;<i>S</i> &le; 0 &rArr; <i>T</i> = &Delta;<i>H</i> / &Delta;<i>S</i> (1)<br>• &Delta;<i>H</i> = 859 &times; 10<sup>3</sup> J mol<sup>&minus;1</sup> (1)<br>• <i>T</i> = (859 &times; 10<sup>3</sup>) / 162 = <b>5302 K</b> (range <b>5300 to 5304 K</b>) (1)",
        "extra": "&minus;1 for each error + mark consequential.<br>Penalise if units &deg;C.",
        "mark": 4,
        "spec": "3.1.8"
    },
    "2003-june-chm5-q5a": {
        "answers": "<b>C<sub>2</sub>H<sub>6</sub> &rarr; C<sub>2</sub>H<sub>4</sub> + H<sub>2</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm5-q5b": {
        "answers": "• <i>pV = nRT</i> or <i>n = pV / RT</i> (1)<br>• <i>n</i> = (110 000 &times; 25 &times; 10<sup>&minus;6</sup>) / (8.31 &times; 332) (1)<br>• = <b>9.97 &times; 10<sup>&minus;4</sup> mol</b> (range <b>10 to 9.968 &times; 10<sup>&minus;4</sup> mol</b>) (1)",
        "extra": "&minus;1 for each error.",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-june-chm5-q5ci": {
        "answers": "• Calculation: 3 &times; (9.97 &times; 10<sup>&minus;4</sup>) = <b>2.99 &times; 10<sup>&minus;3</sup> mol</b> (range 3.0 to 2.99 &times; 10<sup>&minus;3</sup>) (1)<br>• Equation: <b>C<sub>2</sub>H<sub>4</sub> + Br<sub>2</sub> &rarr; C<sub>2</sub>H<sub>4</sub>Br<sub>2</sub></b> (1)",
        "extra": "Allow consequential as 3 &times; answer to (b).<br>Penalise if an incorrect structural formula given.",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2003-june-chm5-q5cii": {
        "answers": "<b>2KI + Br<sub>2</sub> &rarr; 2KBr + I<sub>2</sub></b> OR <b>2I<sup>&minus;</sup> + Br<sub>2</sub> &rarr; I<sub>2</sub> + 2Br<sup>&minus;</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-june-chm5-q5ciii": {
        "answers": "• Moles thiosulphate = 22.1 &times; 0.250 / 1000 = <b>(5.52 to 5.53) &times; 10<sup>&minus;3</sup> mol</b> (1)<br>• Moles I<sub>2</sub> = moles thio / 2 = <b>(2.76 to 2.77) &times; 10<sup>&minus;3</sup> mol</b> (1)<br>• Moles Br<sub>2</sub> reacting with ethene = 2.99 &times; 10<sup>&minus;3</sup> &minus; 2.76 &times; 10<sup>&minus;3</sup> (1)<br>• = <b>(2.25 to 2.41) &times; 10<sup>&minus;4</sup> mol</b> (1)",
        "extra": "Mark consequential even if answer is negative.",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2003-june-chm5-q5civ": {
        "answers": "• % Ethene = (moles ethene / total moles gas) &times; 100 (1)<br>• = (2.3 &times; 10<sup>&minus;4</sup> / 9.97 &times; 10<sup>&minus;4</sup>) &times; 100 = <b>23.1%</b> (range <b>22.4 to 24.2%</b>) (1)",
        "extra": "Mark consequential as c(iii) &times; 100 / (b).<br>Negative final % or answers over 100% lose the last mark.",
        "mark": 2,
        "spec": "3.1.2"
    }
}

def main():
    print("Ingesting 2003 June CHM5...")
    doc = fitz.open(QP_PATH)
    
    print("Generating official markscheme table images...")
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        ms = MS_DATA.get(q_id)
        if ms:
            out_img = os.path.join(IMG_DIR, f"ms_{q_id.split('-')[-1]}.png")
            render_official_markscheme_image(
                question_label=q_label,
                answers_html=ms["answers"],
                extra_html=ms.get("extra", ""),
                marks=ms["mark"],
                spec_ref=ms.get("spec", ""),
                output_path=out_img
            )
            
    print("Cropping question images from QP...")
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        out_jpg = os.path.join(IMG_DIR, f"q_{q_id.split('-')[-1]}.jpg")
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        im.save(out_jpg, format="JPEG", quality=92)
        
    print("Updating questions.json...")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)
        
    papers = {p["id"]: p for p in db.get("papers", [])}
    papers[PAPER_INFO["id"]] = PAPER_INFO
    db["papers"] = list(papers.values())
    
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        short_id = q_id.split('-')[-1]
        ms = MS_DATA.get(q_id, {})
        q_obj = {
            "id": q_id,
            "paper": PAPER_INFO["id"],
            "question": q_label,
            "page": p_num,
            "marks": marks,
            "topics": topics,
            "skills": skills,
            "summary": summary,
            "image": f"img/2003-june-chm5/q_{short_id}.jpg",
            "markscheme_image": f"img/2003-june-chm5/ms_{short_id}.png",
            "markscheme_text": ms.get("answers", "").replace("<br>", "\n").replace("<b>", "**").replace("</b>", "**").replace("&minus;", "-").replace("&times;", "x").replace("&le;", "<=").replace("&ge;", ">=").replace("&rArr;", "=>")
        }
        db["questions"].append(q_obj)
        
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully ingested {len(QUESTIONS_DEF)} questions for {PAPER_INFO['id']}!")

if __name__ == "__main__":
    main()

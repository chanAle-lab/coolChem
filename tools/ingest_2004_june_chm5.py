"""
Ingestion script for 2004 June CHM5 (Section A only)
Excludes old-spec Section B essay questions (Q6-Q9).
Renders official AQA modern mark scheme tables and precision cropped question images.
"""
import os
import json
import fitz
from PIL import Image
import io
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795381684205_d8d79a05.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-june-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-june-chm5",
    "year": 2004,
    "series": "June",
    "date": "2004-06-29",
    "code": "CHM5",
    "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 120,
    "duration": "2 hours"
}

# (qid, label, page, y0, y1, mark, spec_topics, skills, prompt, figures)
QUESTIONS_DEF = [
    # Page 2: Question 1(a) (Born-Haber cycle)
    ("2004-june-chm5-q1a", "1(a)", 2, 140, 775, 5, ["3.1.8"], ["recall", "analysis"], "Identify enthalpy changes (i) to (v) in the Born-Haber cycle for magnesium chloride.", []),

    # Page 5: Question 1(b)-(c)
    ("2004-june-chm5-q1b", "1(b)", 5, 80, 325, 4, ["3.1.4", "3.1.8"], ["calculation"], "Equation for decomposition of MgCl(s) to MgCl2(s) and Mg(s) and enthalpy change calculation.", []),
    ("2004-june-chm5-q1c", "1(c)", 5, 335, 615, 3, ["3.1.8"], ["calculation"], "Calculate molar enthalpy of solution of MgCl2(s) from lattice and hydration enthalpies.", []),

    # Page 6: Question 2(a)-(b)
    ("2004-june-chm5-q2ai", "2(a)(i)", 6, 80, 220, 1, ["3.1.3", "3.2.4"], ["recall"], "Deduce type of bonding present in chloride of Period 3 element X.", []),
    ("2004-june-chm5-q2aii", "2(a)(ii)", 6, 222, 285, 1, ["3.2.4"], ["recall"], "Identify Period 3 element X.", []),
    ("2004-june-chm5-q2aiii", "2(a)(iii)", 6, 288, 410, 1, ["3.2.4"], ["recall"], "Write equation for reaction between water and oxide of element X.", []),
    ("2004-june-chm5-q2bi", "2(b)(i)", 6, 412, 530, 1, ["3.1.3", "3.2.4"], ["recall"], "Deduce type of bonding present in oxide of Period 3 element Y.", []),
    ("2004-june-chm5-q2bii", "2(b)(ii)", 6, 532, 595, 1, ["3.2.4"], ["recall"], "Identify Period 3 element Y.", []),
    ("2004-june-chm5-q2biii", "2(b)(iii)", 6, 598, 775, 1, ["3.2.4"], ["recall"], "Identify acid formed when both oxide and chloride of element Y react with water.", []),

    # Page 7: Question 2(c)
    ("2004-june-chm5-q2ci", "2(c)(i)", 7, 80, 195, 1, ["3.1.3", "3.2.4"], ["recall"], "Deduce type of crystal shown by oxide of Period 3 element Z.", []),
    ("2004-june-chm5-q2cii", "2(c)(ii)", 7, 198, 260, 1, ["3.2.4"], ["recall"], "Identify Period 3 element Z.", []),
    ("2004-june-chm5-q2ciii", "2(c)(iii)", 7, 262, 400, 2, ["3.2.4"], ["recall"], "Write equation illustrating acidic nature of oxide of element Z.", []),

    # Page 8: Question 3(a)-(c)
    ("2004-june-chm5-q3ai", "3(a)(i)", 8, 355, 420, 1, ["3.2.5"], ["recall"], "State colour of Cr2O7 2- in aqueous solution.", []),
    ("2004-june-chm5-q3aii", "3(a)(ii)", 8, 422, 455, 1, ["3.2.5"], ["recall"], "State colour of Cr3+ in aqueous solution.", []),
    ("2004-june-chm5-q3aiii", "3(a)(iii)", 8, 458, 500, 1, ["3.2.5"], ["recall"], "State colour of MnO4 - in aqueous solution.", []),
    ("2004-june-chm5-q3b", "3(b)", 8, 502, 605, 1, ["3.1.11"], ["analysis"], "Select species from electrode potential table which is most powerful reducing agent.", ["img/2004-june-chm5/fig-q3-table.jpg"]),
    ("2004-june-chm5-q3ci", "3(c)(i)", 8, 608, 665, 1, ["3.1.7"], ["calculation"], "Deduce oxidation state of chromium in Cr2O7 2-.", []),
    ("2004-june-chm5-q3cii", "3(c)(ii)", 8, 668, 775, 1, ["3.1.7"], ["calculation"], "Deduce oxidation state of nitrogen in HNO2.", []),

    # Page 9: Question 3(d)-(e)
    ("2004-june-chm5-q3di", "3(d)(i)", 9, 80, 245, 2, ["3.1.11", "3.2.5"], ["analysis"], "Explain why HCl should not be used to acidify solution of iron(II) ions in titration.", ["img/2004-june-chm5/fig-q3-table.jpg"]),
    ("2004-june-chm5-q3dii", "3(d)(ii)", 9, 248, 385, 2, ["3.1.11", "3.2.5"], ["analysis"], "Explain why HNO3 should not be used to acidify solution of iron(II) ions in titration.", ["img/2004-june-chm5/fig-q3-table.jpg"]),
    ("2004-june-chm5-q3ei", "3(e)(i)", 9, 388, 475, 1, ["3.1.11"], ["calculation"], "Calculate e.m.f. of cell Mn2+, MnO4- || S2O8 2-, SO4 2-.", ["img/2004-june-chm5/fig-q3-table.jpg"]),
    ("2004-june-chm5-q3eii", "3(e)(ii)", 9, 478, 645, 2, ["3.1.11"], ["analysis"], "Deduce equation for reaction when excess S2O8 2- is added to aqueous Mn2+.", ["img/2004-june-chm5/fig-q3-table.jpg"]),

    # Page 10: Question 4(a)-(b)
    ("2004-june-chm5-q4ai", "4(a)(i)", 10, 80, 185, 1, ["3.2.5"], ["recall"], "State what is meant by the term ligand.", []),
    ("2004-june-chm5-q4aii", "4(a)(ii)", 10, 188, 250, 1, ["3.2.5"], ["recall"], "State what is meant by the term complex ion.", []),
    ("2004-june-chm5-q4aiii", "4(a)(iii)", 10, 252, 330, 1, ["3.2.5"], ["recall"], "State what is meant by the term co-ordination number.", []),
    ("2004-june-chm5-q4bi", "4(b)(i)", 10, 332, 435, 2, ["3.2.5"], ["recall"], "Equation for ligand substitution on Co2+ with no change in co-ordination number or charge.", []),
    ("2004-june-chm5-q4bii", "4(b)(ii)", 10, 438, 500, 2, ["3.2.5"], ["recall"], "Equation for ligand substitution on Co2+ with change in both co-ordination number and charge.", []),
    ("2004-june-chm5-q4biii", "4(b)(iii)", 10, 502, 560, 2, ["3.2.5"], ["recall"], "Equation for ligand substitution on Co2+ with no change in co-ordination number but change in charge.", []),
    ("2004-june-chm5-q4biv", "4(b)(iv)", 10, 562, 705, 2, ["3.2.5"], ["recall"], "Equation for ligand substitution on Co2+ with large change in entropy.", []),

    # Page 11: Question 4(c)
    ("2004-june-chm5-q4ci", "4(c)(i)", 11, 80, 185, 1, ["3.2.5"], ["recall"], "Give formula of complex ion responsible for pale-green colour of iron(II) sulphate.", []),
    ("2004-june-chm5-q4cii", "4(c)(ii)", 11, 188, 240, 1, ["3.2.5"], ["recall"], "Give formula of green precipitate formed when NaOH is added to iron(II) sulphate.", []),
    ("2004-june-chm5-q4ciii", "4(c)(iii)", 11, 242, 350, 2, ["3.2.5"], ["recall"], "Suggest explanation for change in colour of green precipitate on standing in air.", []),

    # Page 12: Question 5(a)-(c)
    ("2004-june-chm5-q5a", "5(a)", 12, 80, 155, 1, ["3.1.5", "3.2.5"], ["recall"], "State what is meant by homogeneous as applied to a catalyst.", []),
    ("2004-june-chm5-q5bi", "5(b)(i)", 12, 158, 235, 1, ["3.2.5"], ["recall"], "State what is meant by the term autocatalysis.", []),
    ("2004-june-chm5-q5bii", "5(b)(ii)", 12, 238, 325, 1, ["3.2.5"], ["recall"], "Identify species acting as autocatalyst in ethanedioate and manganate(VII) reaction.", []),
    ("2004-june-chm5-q5ci", "5(c)(i)", 12, 328, 470, 2, ["3.1.5", "3.2.5"], ["recall"], "Equation for reaction between two toxic gases in catalytic converter and identify reducing agent.", []),
    ("2004-june-chm5-q5cii", "5(c)(ii)", 12, 472, 620, 3, ["3.1.5", "3.2.5"], ["recall"], "Identify transition metal used in catalytic converters and state how effect is maximised.", []),

    # Page 13: Question 5(d)
    ("2004-june-chm5-q5di", "5(d)(i)", 13, 80, 185, 1, ["3.1.5", "3.2.5"], ["recall"], "Explain why transition metals which adsorb strongly are not usually good catalysts.", []),
    ("2004-june-chm5-q5dii", "5(d)(ii)", 13, 188, 260, 1, ["3.1.5", "3.2.5"], ["recall"], "Explain why transition metals which adsorb weakly are not usually good catalysts.", []),
]

MS_DATA = {
    "2004-june-chm5-q1a": {
        "answers": "<ul><li>(i) &Delta;<i>H</i> atomisation / sublimation of magnesium</li><li>(ii) Bond / dissociation enthalpy of Cl&minus;Cl<br><b>OR</b> 2 &times; &Delta;<i>H</i> atomisation of chlorine</li><li>(iii) Second ionisation enthalpy of magnesium</li><li>(iv) 2 &times; electron affinity of chlorine</li><li>(v) Lattice formation enthalpy of MgCl<sub>2</sub></li></ul>",
        "extra": "<p>1 mark each for (i) to (v)</p>",
        "mark": 5,
        "spec": "3.1.8"
    },
    "2004-june-chm5-q1b": {
        "answers": "<ul><li><b>Equation:</b> 2MgCl(s) &rarr; MgCl<sub>2</sub>(s) + Mg(s)</li><li><b>Calculation:</b> &Delta;<i>H</i> reaction = &Sigma;&Delta;<i>H</i><sub>f</sub>(products) &minus; &Sigma;&Delta;<i>H</i><sub>f</sub>(reactants)</li><li>= &minus;653 &minus; (2 &times; &minus;133)</li><li><b>= &minus;427 (kJ mol<sup>&minus;1</sup>)</b></li></ul>",
        "extra": "<p>State symbols not required but penalise if incorrect</p><p>Allow +427 to score (1) mark</p><p>Other answers: award (1) for correct expression</p>",
        "mark": 4,
        "spec": "3.1.8"
    },
    "2004-june-chm5-q1c": {
        "answers": "<ul><li>&Delta;<i>H</i><sub>soln</sub> MgCl<sub>2</sub> = &minus;&Delta;<i>H</i><sub>Lat.form.</sub> + &Delta;<i>H</i><sub>hyd</sub>(Mg<sup>2+</sup>) + 2&Delta;<i>H</i><sub>hyd</sub>(Cl<sup>&minus;</sup>) (or cycle)</li><li>= 2502 &minus; 1920 &minus; (2 &times; 364)</li><li><b>= &minus;146 (kJ mol<sup>&minus;1</sup>)</b></li></ul>",
        "extra": "<p>Allow +146 to score (1) mark</p><p>Other answers: award (1) for correct &Delta;<i>H</i><sub>soln</sub> expression/cycle</p>",
        "mark": 3,
        "spec": "3.1.8"
    },
    "2004-june-chm5-q2ai": {
        "answers": "Ionic",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2004-june-chm5-q2aii": {
        "answers": "Sodium / Na",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2004-june-chm5-q2aiii": {
        "answers": "Na<sub>2</sub>O + H<sub>2</sub>O &rarr; 2NaOH",
        "extra": "Ignore state symbols",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2004-june-chm5-q2bi": {
        "answers": "Covalent",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2004-june-chm5-q2bii": {
        "answers": "Phosphorus / P",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2004-june-chm5-q2biii": {
        "answers": "H<sub>3</sub>PO<sub>4</sub>",
        "extra": "or other acid with P in oxidation state (V) or (III)",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2004-june-chm5-q2ci": {
        "answers": "Macromolecular / giant covalent / giant molecular",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2004-june-chm5-q2cii": {
        "answers": "Silicon / Si",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2004-june-chm5-q2ciii": {
        "answers": "<ul><li>e.g. CaO + SiO<sub>2</sub> &rarr; CaSiO<sub>3</sub><br><b>OR</b> 2NaOH + SiO<sub>2</sub> &rarr; Na<sub>2</sub>SiO<sub>3</sub> + H<sub>2</sub>O</li></ul>",
        "extra": "<p>Base (1)</p><p>Balanced (1)</p>",
        "mark": 2,
        "spec": "3.2.4"
    },
    "2004-june-chm5-q3ai": {
        "answers": "Orange",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q3aii": {
        "answers": "Red-violet / ruby / violet / green",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q3aiii": {
        "answers": "Purple",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q3b": {
        "answers": "Fe<sup>2+</sup> or Fe(II)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.11"
    },
    "2004-june-chm5-q3ci": {
        "answers": "6 or (VI)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2004-june-chm5-q3cii": {
        "answers": "3 or (III)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2004-june-chm5-q3di": {
        "answers": "<ul><li>MnO<sub>4</sub><sup>&minus;</sup> / Mn<sup>2+</sup> has a more positive <i>E</i><sup>&ominus;</sup> value than Cl<sub>2</sub> / Cl<sup>&minus;</sup> (or data used)</li><li>and will oxidise Cl<sup>&minus;</sup> or change Cl<sup>&minus;</sup> to Cl<sub>2</sub></li></ul>",
        "extra": "<p>Allow converse answers</p>",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2004-june-chm5-q3dii": {
        "answers": "<ul><li>NO<sub>3</sub><sup>&minus;</sup> / HNO<sub>2</sub> has a more positive <i>E</i><sup>&ominus;</sup> value than Fe<sup>3+</sup> / Fe<sup>2+</sup> (or data used)</li><li>and will oxidise Fe<sup>2+</sup> or change Fe<sup>2+</sup> to Fe<sup>3+</sup></li></ul>",
        "extra": "",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2004-june-chm5-q3ei": {
        "answers": "<b>0.50 V</b> (or 0.5)",
        "extra": "<i>E</i><sup>&ominus;</sup><sub>cell</sub> = 2.01 &minus; 1.51 = 0.50 V",
        "mark": 1,
        "spec": "3.1.11"
    },
    "2004-june-chm5-q3eii": {
        "answers": "2Mn<sup>2+</sup> + 8H<sub>2</sub>O + 5S<sub>2</sub>O<sub>8</sub><sup>2&minus;</sup> &rarr; 10SO<sub>4</sub><sup>2&minus;</sup> + 2MnO<sub>4</sub><sup>&minus;</sup> + 16H<sup>+</sup>",
        "extra": "<p>Both SO<sub>4</sub><sup>2&minus;</sup> and MnO<sub>4</sub><sup>&minus;</sup> on right (1)</p><p>Balanced (1)</p>",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2004-june-chm5-q4ai": {
        "answers": "An atom, ion or molecule which can donate a lone electron pair",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4aii": {
        "answers": "A central metal ion/species surrounded by co-ordinately bonded ligands",
        "extra": "or ion in which co-ordination number exceeds oxidation state",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4aiii": {
        "answers": "The number of co-ordinate bonds formed to a central metal ion",
        "extra": "or number of electron pairs donated or donor atoms",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4bi": {
        "answers": "[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 6NH<sub>3</sub> &rarr; [Co(NH<sub>3</sub>)<sub>6</sub>]<sup>2+</sup> + 6H<sub>2</sub>O",
        "extra": "<p>Complex ions (1)</p><p>Balanced (1)</p><p>Allow reverse or partial substitution</p>",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4bii": {
        "answers": "[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 4Cl<sup>&minus;</sup> &rarr; [CoCl<sub>4</sub>]<sup>2&minus;</sup> + 6H<sub>2</sub>O",
        "extra": "<p>Complex ions (1)</p><p>Balanced (1)</p><p>or reverse, or H<sub>2</sub>O / NH<sub>3</sub> / C<sub>2</sub>O<sub>4</sub><sup>2&minus;</sup> by Cl<sup>&minus;</sup></p>",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4biii": {
        "answers": "[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 3C<sub>2</sub>O<sub>4</sub><sup>2&minus;</sup> &rarr; [Co(C<sub>2</sub>O<sub>4</sub>)<sub>3</sub>]<sup>4&minus;</sup> + 6H<sub>2</sub>O",
        "extra": "<p>Complex ions (1)</p><p>Balanced (1)</p><p>Allow reverse</p>",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4biv": {
        "answers": "[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + EDTA<sup>4&minus;</sup> &rarr; [Co(EDTA)]<sup>2&minus;</sup> + 6H<sub>2</sub>O",
        "extra": "<p>Complex ions (1)</p><p>Balanced (1)</p><p>or reverse, or H<sub>2</sub>O/NH<sub>3</sub> by C<sub>2</sub>O<sub>4</sub><sup>2&minus;</sup></p>",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4ci": {
        "answers": "[Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup>",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4cii": {
        "answers": "Fe(OH)<sub>2</sub> or Fe(OH)<sub>2</sub>(H<sub>2</sub>O)<sub><i>x</i></sub> where <i>x</i> = 0 to 4",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q4ciii": {
        "answers": "<ul><li>Fe<sup>2+</sup> is oxidised to Fe<sup>3+</sup> or Fe(OH)<sub>3</sub></li><li>by oxygen in the air</li></ul>",
        "extra": "",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q5a": {
        "answers": "A catalyst in the same phase / physical state as the reactants",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2004-june-chm5-q5bi": {
        "answers": "A reaction in which a product acts as a catalyst",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q5bii": {
        "answers": "Mn<sup>2+</sup> or Mn<sup>3+</sup>",
        "extra": "&ldquo;Self-catalysing&rdquo; not allowed",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2004-june-chm5-q5ci": {
        "answers": "<ul><li>2CO + 2NO &rarr; 2CO<sub>2</sub> + N<sub>2</sub><br>(or 4CO + 2NO<sub>2</sub> &rarr; 4CO<sub>2</sub> + N<sub>2</sub>)</li><li>Reducing agent: CO</li></ul>",
        "extra": "<p>Equation (1)</p><p>Reducing agent (1)</p><p>C not allowed as a product</p>",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2004-june-chm5-q5cii": {
        "answers": "<ul><li><b>Transition metal:</b> Pt, Pd or Rh (1)</li><li>Deposited on a ceramic honeycomb or matrix or mesh or sponge (1)</li><li>To increase surface area of catalyst (1)</li></ul>",
        "extra": "",
        "mark": 3,
        "spec": "3.1.5"
    },
    "2004-june-chm5-q5di": {
        "answers": "Reactants cannot move on surface or products not desorbed or active sites blocked",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2004-june-chm5-q5dii": {
        "answers": "Reactants not brought together or no increase in reactant concentration on catalyst surface or reactants not held long enough for a reaction to occur or reactant bonds not weakened",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
}

def main():
    doc = fitz.open(QP_PATH)
    
    # 1. Save context table for Q3
    p8 = doc[7]
    rect_table = fitz.Rect(70, 85, 545, 335)
    pix = p8.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect_table)
    im_table = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    fig_table_path = os.path.join(IMG_DIR, "fig-q3-table.jpg")
    im_table.save(fig_table_path, format="JPEG", quality=92)
    print("Saved Q3 standard electrode potential table figure.")

    new_questions = []

    for item in QUESTIONS_DEF:
        q_id, q_label, page_num, y0, y1, marks, topics, skills, summary, figures = item

        # Render Question Crop
        page = doc[page_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")

        # Save question image
        s_part = q_id.split("-")[-1]
        q_img_rel = f"img/2004-june-chm5/q_{s_part}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        # Render Mark Scheme Table
        ms = MS_DATA[q_id]
        ms_img_rel = f"img/2004-june-chm5/ms_{s_part}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_entry = {
            "id": q_id,
            "paper": "2004-june-chm5",
            "year": 2004,
            "series": "June",
            "code": "CHM5",
            "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
            "question": q_label,
            "page": page_num,
            "marks": marks,
            "topics": topics,
            "skills": skills,
            "summary": summary,
            "description": summary,
            "image": q_img_rel,
            "figures": figures,
            "markscheme": ms_img_rel
        }
        new_questions.append(q_entry)

    print(f"Prepared {len(new_questions)} questions for 2004 June CHM5.")

    # Update questions.json
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Ensure paper entry exists
    if not any(p['id'] == '2004-june-chm5' for p in db.get('papers', [])):
        db.setdefault('papers', []).append(PAPER_INFO)

    # Replace or add questions
    existing_ids = {q['id'] for q in new_questions}
    db['questions'] = [q for q in db['questions'] if q['id'] not in existing_ids]
    db['questions'].extend(new_questions)

    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("Updated questions.json successfully with June 2004 CHM5!")

if __name__ == "__main__":
    main()

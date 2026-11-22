"""
Ingestion script for 2004 January CHM3/W (Section A only)
Excludes old-spec Section B essay questions (Q5).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960886_d6991030.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-jan-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-jan-chm3w",
    "year": 2004,
    "series": "January",
    "date": "2004-01-09",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(b)
    ("2004-jan-chm3w-q1ai", "1(a)(i)", 2, 75, 215, 1, ["3.3.1"], ["recall"], "State what is meant by the term hydrocarbon."),
    ("2004-jan-chm3w-q1aii", "1(a)(ii)", 2, 218, 305, 1, ["3.3.1"], ["recall"], "State what is meant by the term saturated, as applied to a hydrocarbon."),
    ("2004-jan-chm3w-q1bi", "1(b)(i)", 2, 308, 675, 1, ["3.3.2"], ["recall"], "Name the process used to obtain fractions from crude oil."),
    ("2004-jan-chm3w-q1bii", "1(b)(ii)", 2, 678, 775, 1, ["3.3.2"], ["recall"], "Complete table by naming the missing fraction (11-15 carbon atoms)."),

    # Page 5: Question 1(c)-(d)
    ("2004-jan-chm3w-q1ci", "1(c)(i)", 5, 75, 185, 1, ["3.3.1"], ["recall"], "Give the molecular formula of an alkane with ten carbon atoms."),
    ("2004-jan-chm3w-q1cii", "1(c)(ii)", 5, 188, 305, 2, ["3.3.2"], ["recall"], "Write equation for thermal cracking of tetradecane into ethene, propene (2:1) and one other product."),
    ("2004-jan-chm3w-q1ciii", "1(c)(iii)", 5, 308, 415, 1, ["3.3.2"], ["recall"], "Name the mechanism involved in thermal cracking."),
    ("2004-jan-chm3w-q1di", "1(d)(i)", 5, 418, 555, 1, ["3.3.4"], ["recall"], "Write an equation for partial oxidation of ethene to form epoxyethane."),
    ("2004-jan-chm3w-q1dii", "1(d)(ii)", 5, 558, 775, 1, ["3.3.2"], ["recall"], "Write an equation for the complete combustion of ethene in oxygen."),

    # Page 6: Question 2
    ("2004-jan-chm3w-q2ai", "2(a)(i)", 6, 75, 215, 1, ["3.3.2"], ["recall"], "Write an equation for incomplete combustion of octane to produce CO and water only."),
    ("2004-jan-chm3w-q2aii", "2(a)(ii)", 6, 218, 415, 2, ["3.3.2"], ["recall"], "State essential condition for NO formation in engine and write equation."),
    ("2004-jan-chm3w-q2bi", "2(b)(i)", 6, 418, 515, 1, ["3.3.2"], ["recall"], "Name one metal used as catalyst in a catalytic converter."),
    ("2004-jan-chm3w-q2bii", "2(b)(ii)", 6, 518, 625, 1, ["3.3.2"], ["recall"], "Write equation to show how CO and NO react in a catalytic converter."),
    ("2004-jan-chm3w-q2c", "2(c)", 6, 628, 775, 2, ["3.3.2"], ["recall"], "State why SO2 is in exhaust gases and give one adverse environmental effect."),

    # Page 7: Question 3(a)-(b)(i)
    ("2004-jan-chm3w-q3a", "3(a)", 7, 75, 435, 2, ["3.3.1"], ["recall"], "Give molecular formula and empirical formula of but-2-ene."),
    ("2004-jan-chm3w-q3bi", "3(b)(i)", 7, 438, 775, 4, ["3.3.4"], ["analysis"], "Name and outline mechanism for methylpropene reacting with HBr."),

    # Page 8: Question 3(b)(ii)-(d)
    ("2004-jan-chm3w-q3bii", "3(b)(ii)", 8, 75, 340, 2, ["3.3.4"], ["analysis"], "Draw structure of minor product from methylpropene + HBr and explain why formed in smaller amounts."),
    ("2004-jan-chm3w-q3c", "3(c)", 8, 342, 530, 2, ["3.3.1"], ["analysis"], "Draw structures and give names of the two geometrical isomers of but-2-ene."),
    ("2004-jan-chm3w-q3di", "3(d)(i)", 8, 532, 680, 2, ["3.3.5"], ["analysis"], "Draw structure and give name of tertiary alcohol from hydration of isomer."),
    ("2004-jan-chm3w-q3dii", "3(d)(ii)", 8, 682, 775, 1, ["3.3.5"], ["recall"], "Suggest a reason why tertiary alcohols are resistant to oxidation."),

    # Page 9: Question 4(a)-(b)
    ("2004-jan-chm3w-q4ai", "4(a)(i)", 9, 75, 185, 1, ["3.3.3"], ["recall"], "Give one essential condition for reaction of chlorine with methane."),
    ("2004-jan-chm3w-q4aii", "4(a)(ii)", 9, 188, 260, 1, ["3.3.3"], ["recall"], "Name the mechanism for reaction of chlorine with methane."),
    ("2004-jan-chm3w-q4aiii", "4(a)(iii)", 9, 262, 385, 1, ["3.3.3"], ["recall"], "Identify main organic product when large excess of chlorine is used."),
    ("2004-jan-chm3w-q4bi", "4(b)(i)", 9, 388, 485, 1, ["3.3.3"], ["recall"], "Write an equation for reaction of chloromethane with potassium cyanide."),
    ("2004-jan-chm3w-q4bii", "4(b)(ii)", 9, 488, 560, 1, ["3.3.3"], ["recall"], "Name mechanism for reaction of chloromethane with potassium cyanide."),
    ("2004-jan-chm3w-q4biii", "4(b)(iii)", 9, 562, 775, 1, ["3.3.3"], ["analysis"], "Explain in terms of bond enthalpies why bromomethane reacts faster than chloromethane with KCN."),

    # Page 10: Question 4(c)-(d)
    ("2004-jan-chm3w-q4c", "4(c)", 10, 75, 215, 1, ["3.3.11", "3.3.9"], ["recall"], "Identify carboxylic acid formed from hydrolysis of ethanenitrile."),
    ("2004-jan-chm3w-q4di", "4(d)(i)", 10, 218, 345, 1, ["3.3.3"], ["recall"], "What feature of chloromethane makes it susceptible to attack by ammonia?"),
    ("2004-jan-chm3w-q4dii", "4(d)(ii)", 10, 348, 435, 1, ["3.3.11"], ["recall"], "Name the amine produced in reaction of chloromethane with ammonia."),
    ("2004-jan-chm3w-q4diii", "4(d)(iii)", 10, 438, 775, 3, ["3.3.3", "3.3.11"], ["analysis"], "Outline a mechanism for reaction of chloromethane with ammonia.")
]

MS_DATA = {
    "2004-jan-chm3w-q1ai": {
        "answers": "(A molecule / compound / consists / composed) of <b>hydrogen and carbon only</b> (1)",
        "extra": "Or clearly implied.",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2004-jan-chm3w-q1aii": {
        "answers": "<b>Only single bonds</b> (1) <i>OR</i> has no double bond",
        "extra": "Or clearly implied.<br>NOT has maximum number of hydrogen atoms.",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2004-jan-chm3w-q1bi": {
        "answers": "<b>Fractional distillation</b> <i>OR</i> <b>fractionation</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q1bii": {
        "answers": "<b>Kerosine</b> <i>OR</i> <b>Kerosene</b> <i>OR</i> <b>Paraffin</b> (1)",
        "extra": "Ignore uses.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q1ci": {
        "answers": "<b>C<sub>10</sub>H<sub>22</sub></b> only (1)",
        "extra": "NOT CH3CH2...CH3.",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2004-jan-chm3w-q1cii": {
        "answers": "• <b>C<sub>14</sub>H<sub>30</sub> &rarr; 2C<sub>2</sub>H<sub>4</sub> + C<sub>3</sub>H<sub>6</sub> + C<sub>7</sub>H<sub>16</sub></b> (2)<br>[alkene formulas (1), balanced (1)]<br><i>OR</i> C<sub>14</sub>H<sub>30</sub> &rarr; 4C<sub>2</sub>H<sub>4</sub> + 2C<sub>3</sub>H<sub>6</sub> + H<sub>2</sub>",
        "extra": "",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q1ciii": {
        "answers": "<b>(Free) radical</b> <i>OR</i> <b>homolysis</b> <i>OR</i> <b>homolytic fission</b> (1)",
        "extra": "NOT radical substitution.<br>NOT thermal decomposition.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q1di": {
        "answers": "<b>C<sub>2</sub>H<sub>4</sub> + &frac12; O<sub>2</sub> &rarr; C<sub>2</sub>H<sub>4</sub>O</b> (1)",
        "extra": "Allow CH2=CH2 + 1/2 O2 -> epoxyethane ring structure.",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2004-jan-chm3w-q1dii": {
        "answers": "<b>C<sub>2</sub>H<sub>4</sub> + 3O<sub>2</sub> &rarr; 2CO<sub>2</sub> + 2H<sub>2</sub>O</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q2ai": {
        "answers": "<b>C<sub>8</sub>H<sub>18</sub> + 8&frac12; O<sub>2</sub> &rarr; 8CO + 9H<sub>2</sub>O</b> (1)<br>(<i>OR</i> 2C<sub>8</sub>H<sub>18</sub> + 17O<sub>2</sub> &rarr; 16CO + 18H<sub>2</sub>O)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q2aii": {
        "answers": "• Condition: <b>spark</b> <i>OR</i> <b>high <i>T</i></b> <i>OR</i> <b><i>T</i> = 2500 &ndash; 4000 &deg;C</b> (1)<br>• Equation: <b>N<sub>2</sub> + O<sub>2</sub> &rarr; 2NO</b> (1)<br>(<i>OR</i> &frac12; N<sub>2</sub> + &frac12; O<sub>2</sub> &rarr; NO)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q2bi": {
        "answers": "<b>Platinum</b> <i>OR</i> <b>rhodium</b> <i>OR</i> <b>palladium</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q2bii": {
        "answers": "<b>2CO + 2NO &rarr; N<sub>2</sub> + 2CO<sub>2</sub></b> (1)<br>(<i>OR</i> CO + NO &rarr; &frac12; N<sub>2</sub> + CO<sub>2</sub>)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q2c": {
        "answers": "• Reason: fraction / petrol / fuels <b>contain sulphur</b> <i>OR</i> sulphur-containing impurities (which burn to give SO<sub>2</sub>) (1)<br>• Environmental effect: <b>acid rain</b> <i>OR</i> a specific effect (1)",
        "extra": "NOT greenhouse effect.<br>NOT damages ozone layer.",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2004-jan-chm3w-q3a": {
        "answers": "• Molecular formula: <b>C<sub>4</sub>H<sub>8</sub></b> (1)<br>• Empirical formula: <b>CH<sub>2</sub></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2004-jan-chm3w-q3bi": {
        "answers": "• Name: <b>electrophilic addition</b> (1)<br>• Mechanism:<br>&nbsp;&nbsp;&ndash; M1: arrow from C=C double bond to H of H&ndash;Br (1)<br>&nbsp;&nbsp;&ndash; M2: arrow from H&ndash;Br bond to Br (1)<br>&nbsp;&nbsp;&ndash; M3: tertiary carbocation (CH<sub>3</sub>)<sub>3</sub>C<sup>+</sup> structure (1)<br>&nbsp;&nbsp;&ndash; M4: arrow from lone pair on :Br<sup>&minus;</sup> to C<sup>+</sup> (1)",
        "extra": "Penalise delta+/delta- on double bond. Award M1 for arrow to H+. Penalise H-Br once only.",
        "mark": 4,
        "spec": "3.3.4"
    },
    "2004-jan-chm3w-q3bii": {
        "answers": "• Structure: <b>(CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>Br</b> (1)<br>• Explanation: major product formed via <b>tertiary carbocation</b> (1)<br><i>OR</i> primary carbocation less stable than tertiary carbocation (1)",
        "extra": "If wrong asymmetric alkene in (b)(i), allow consequential structure and explanation.",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2004-jan-chm3w-q3c": {
        "answers": "• Correct structures for <b><i>cis</i>-but-2-ene</b> and <b><i>trans</i>-but-2-ene</b> (1)<br>• Correct names: <i>cis</i>-but-2-ene and <i>trans</i>-but-2-ene (1)",
        "extra": "Award both marks for two correct structures and only the words cis and trans correctly placed.",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2004-jan-chm3w-q3di": {
        "answers": "• Structure: <b>(CH<sub>3</sub>)<sub>3</sub>COH</b> (1) [C&ndash;O bond clearly shown]<br>• Name: <b>2-methylpropan-2-ol</b> (1)",
        "extra": "NOT hydroxy.",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2004-jan-chm3w-q3dii": {
        "answers": "<b>Central carbon atom has no H atom</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2004-jan-chm3w-q4ai": {
        "answers": "<b>UV light</b> <i>OR</i> <b>sunlight</b> <i>OR</i> <b><i>T</i> &ge; 450 &deg;C</b> (1)",
        "extra": "NOT high T alone.",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-jan-chm3w-q4aii": {
        "answers": "<b>(Free) radical substitution</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-jan-chm3w-q4aiii": {
        "answers": "<b>CCl<sub>4</sub></b> <i>OR</i> <b>tetrachloromethane</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-jan-chm3w-q4bi": {
        "answers": "<b>CH<sub>3</sub>Cl + KCN &rarr; CH<sub>3</sub>CN + KCl</b> (1)<br>(<i>OR</i> CH<sub>3</sub>Cl + CN<sup>&minus;</sup> &rarr; CH<sub>3</sub>CN + Cl<sup>&minus;</sup>)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-jan-chm3w-q4bii": {
        "answers": "<b>Nucleophilic substitution</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-jan-chm3w-q4biii": {
        "answers": "<b>C&ndash;Br bond is weaker</b> (than C&ndash;Cl bond) (1)<br><i>OR</i> C&ndash;Br bond enthalpy is less than C&ndash;Cl",
        "extra": "Ignore electronegativity.",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-jan-chm3w-q4c": {
        "answers": "<b>CH<sub>3</sub>COOH</b> <i>OR</i> <b>ethanoic acid</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2004-jan-chm3w-q4di": {
        "answers": "<b>C&ndash;Cl is polar</b> <i>OR</i> <b>C atom is &delta;+</b> / electron deficient (1)",
        "extra": "NOT chloromethane is polar.",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-jan-chm3w-q4dii": {
        "answers": "<b>Methylamine</b> only (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.11"
    },
    "2004-jan-chm3w-q4diii": {
        "answers": "• M1: arrow from lone pair on :NH<sub>3</sub> to &delta;+ C of CH<sub>3</sub>Cl (1)<br>• M2: arrow from C&ndash;Cl bond to Cl (1)<br>• M3: structure of transition / intermediate [CH<sub>3</sub>NH<sub>3</sub>]<sup>+</sup> and arrow to N from second NH<sub>3</sub> (1)<br>(SN1 scores full marks).",
        "extra": "",
        "mark": 3,
        "spec": "3.3.3"
    }
}

def main():
    doc = fitz.open(QP_PATH)
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    existing_ids = {q["id"] for q in db["questions"]}
    added = 0

    for qid, q_label, p_num, y0, y1, mark, spec_topics, skills, prompt in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-jan-chm3w/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-jan-chm3w/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-jan-chm3w",
            "year": 2004,
            "series": "January",
            "code": "CHM3/W",
            "unit": "Unit 3(a): Introduction to Organic Chemistry",
            "question": q_label,
            "page": p_num,
            "marks": mark,
            "topics": spec_topics,
            "skills": skills,
            "description": prompt,
            "image": q_img_rel,
            "markscheme": ms_img_rel
        }

        if qid not in existing_ids:
            db["questions"].append(q_obj)
            existing_ids.add(qid)
            added += 1
        else:
            for idx, item in enumerate(db["questions"]):
                if item["id"] == qid:
                    db["questions"][idx] = q_obj
                    break

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-jan-chm3w ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

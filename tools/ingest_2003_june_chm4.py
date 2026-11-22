"""
Ingestion script for 2003 June CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q6 and Q7).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023341_0f87e524.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-june-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-june-chm4",
    "year": 2003,
    "series": "June",
    "date": "2003-06-18",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A2",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 mins"
}

QUESTIONS_DEF = [
    # Page 2 (Exam page 2): Q1
    ("2003-june-chm4-q1a", "1(a)", 2, 80, 290, 1, ["3.1.9"], ["recall"], "What is meant by the term order of reaction with respect to A."),
    ("2003-june-chm4-q1b", "1(b)", 2, 295, 385, 1, ["3.1.9"], ["recall", "maths"], "Deduce overall order of reaction when rate increases by factor of 4."),
    ("2003-june-chm4-q1ci", "1(c)(i)", 2, 390, 540, 2, ["3.1.9"], ["analysis", "calculation"], "Deduce order of reaction with respect to A and with respect to B."),
    ("2003-june-chm4-q1cii", "1(c)(ii)", 2, 545, 785, 2, ["3.1.9"], ["recall", "analysis"], "Write rate equation and suggest suitable units for the rate constant."),

    # Page 5 (Exam page 5): Q2
    ("2003-june-chm4-q2ai", "2(a)(i)", 5, 80, 250, 2, ["3.1.10"], ["calculation"], "Calculate moles of PCl3 and Cl2 in equilibrium mixture."),
    ("2003-june-chm4-q2aii", "2(a)(ii)", 5, 255, 320, 1, ["3.1.10"], ["calculation"], "Calculate total moles of gas in equilibrium mixture."),
    ("2003-june-chm4-q2b", "2(b)", 5, 325, 475, 3, ["3.1.10"], ["calculation"], "Calculate mole fraction and partial pressure of PCl3."),
    ("2003-june-chm4-q2ci", "2(c)(i)", 5, 480, 560, 1, ["3.1.10"], ["recall"], "Write expression for equilibrium constant Kp."),
    ("2003-june-chm4-q2cii", "2(c)(ii)", 5, 565, 715, 4, ["3.1.10"], ["calculation"], "Calculate value of Kp at this temperature and state its units."),
    ("2003-june-chm4-q2di", "2(d)(i)", 5, 720, 800, 1, ["3.1.10"], ["explanation"], "Effect on mole fraction of PCl3 if volume is increased at constant T."),
    ("2003-june-chm4-q2dii", "2(d)(ii)", 5, 805, 895, 1, ["3.1.10"], ["explanation"], "Effect on mole fraction of PCl3 if temperature is increased at constant V."),

    # Page 6 (Exam page 6): Q3(a)-(b)
    ("2003-june-chm4-q3ai", "3(a)(i)", 6, 80, 175, 1, ["3.1.12"], ["recall"], "Define the term Kw."),
    ("2003-june-chm4-q3aii", "3(a)(ii)", 6, 180, 245, 1, ["3.1.12"], ["recall"], "Define the term pH."),
    ("2003-june-chm4-q3aiii", "3(a)(iii)", 6, 250, 445, 3, ["3.1.12"], ["calculation", "explanation"], "Calculate pH of pure water at 50 °C and explain why it is still neutral."),
    ("2003-june-chm4-q3bi", "3(b)(i)", 6, 450, 580, 2, ["3.1.12"], ["calculation"], "Calculate pH at 25 °C of 0.150 mol dm-3 NaOH solution."),
    ("2003-june-chm4-q3bii", "3(b)(ii)", 6, 585, 885, 6, ["3.1.12"], ["calculation"], "Calculate pH of mixture of 35.0 cm3 0.150 M NaOH and 40.0 cm3 0.120 M HCl."),

    # Page 7 (Exam page 7): Q3(c)
    ("2003-june-chm4-q3ci", "3(c)(i)", 7, 80, 215, 1, ["3.1.12"], ["recall"], "Write an expression for Ka for weak acid HX."),
    ("2003-june-chm4-q3cii", "3(c)(ii)", 7, 220, 480, 4, ["3.1.12"], ["calculation"], "Calculate value of Ka for acid HX at 25 °C and state its units."),

    # Page 8 (Exam page 8): Q4(a)-(b)
    ("2003-june-chm4-q4a", "4(a)", 8, 80, 420, 5, ["3.3.6"], ["mechanism"], "Outline mechanism for reaction of butanal with HCN and name product."),
    ("2003-june-chm4-q4b", "4(b)", 8, 425, 780, 5, ["3.3.9"], ["mechanism"], "Outline mechanism for reaction of methanol with propanoyl chloride and name product."),

    # Page 9 (Exam page 9): Q4(c)
    ("2003-june-chm4-q4ci", "4(c)(i)", 9, 80, 285, 1, ["3.3.10"], ["recall"], "Formula of reactive intermediate formed from ethanoyl chloride."),
    ("2003-june-chm4-q4cii", "4(c)(ii)", 9, 290, 585, 3, ["3.3.10"], ["mechanism"], "Outline mechanism for reaction of intermediate with benzene to form phenylethanone."),

    # Page 10 (Exam page 10): Q5
    ("2003-june-chm4-q5ai", "5(a)(i)", 10, 80, 220, 1, ["3.3.1", "3.3.4"], ["recall"], "Name hydrocarbon M."),
    ("2003-june-chm4-q5aii", "5(a)(ii)", 10, 225, 360, 2, ["3.3.4"], ["recall", "drawing"], "Repeating unit of polymer formed from M and type of polymerisation."),
    ("2003-june-chm4-q5aiii", "5(a)(iii)", 10, 365, 570, 2, ["3.3.10"], ["recall", "drawing"], "Name mechanism and draw structure of major product of M with benzene."),
    ("2003-june-chm4-q5aiv", "5(a)(iv)", 10, 575, 680, 1, ["3.3.1"], ["drawing"], "Draw structural isomer of M showing geometrical isomerism."),
    ("2003-june-chm4-q5b", "5(b)", 10, 685, 905, 4, ["3.3.12"], ["recall", "drawing"], "Repeating unit, polymerisation type and linkage between butanedioic acid and hexane-1,6-diamine.")
]

MS_DATA = {
    "2003-june-chm4-q1a": {
        "answers": "<b>Power of concentration term</b> (in rate equation) OR <b>index</b> OR shown as <i>x</i> in [ ]<sup><i>x</i></sup> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2003-june-chm4-q1b": {
        "answers": "<b>2</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2003-june-chm4-q1ci": {
        "answers": "• Order with respect to A = <b>2</b> (1)<br>• Order with respect to B = <b>0</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2003-june-chm4-q1cii": {
        "answers": "• Rate equation: <b>rate = <i>k</i>[A]<sup>2</sup></b> (1)<br>• Units for rate constant: <b>mol<sup>&minus;1</sup> dm<sup>3</sup> s<sup>&minus;1</sup></b> (1)",
        "extra": "Allow consequential on c(i).<br>Units consequential on rate equation.",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2003-june-chm4-q2ai": {
        "answers": "• Moles PCl<sub>3</sub> = 0.345 &minus; 0.166 = <b>0.179</b> (1)<br>• Moles Cl<sub>2</sub> = 0.268 &minus; 0.166 = <b>0.102</b> (1)",
        "extra": "3 sig figs.",
        "mark": 2,
        "spec": "3.1.10"
    },
    "2003-june-chm4-q2aii": {
        "answers": "Total moles = 0.179 + 0.102 + 0.166 = <b>0.447</b> (1)",
        "extra": "Allow 2 sig figs.<br>Consequential on (i).",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2003-june-chm4-q2b": {
        "answers": "• Mole fraction of PCl<sub>3</sub> = 0.179 / 0.447 = <b>0.400</b> (1)<br>• Partial pressure = mol fraction &times; total P (1)<br>• = 0.400 &times; 225 = <b>90(1) kPa</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.10"
    },
    "2003-june-chm4-q2ci": {
        "answers": "<b><i>K</i><sub>p</sub> = <i>p</i>(PCl<sub>5</sub>) / [<i>p</i>(PCl<sub>3</sub>) &times; <i>p</i>(Cl<sub>2</sub>)]</b> (1)",
        "extra": "Must show <i>p</i>.<br>Ignore brackets except [ ].",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2003-june-chm4-q2cii": {
        "answers": "• Substitution: <i>K</i><sub>p</sub> = 83.6 / (90.1 &times; 51.3) (1)<br>• Value: = <b>1.81 &times; 10<sup>&minus;2</sup></b> (1)<br>• Units: <b>kPa<sup>&minus;1</sup></b> (or 1.81 &times; 10<sup>&minus;5</sup> Pa<sup>&minus;1</sup>) (1)<br>• Working shown correctly (1)",
        "extra": "If 83.6 and 51.3 wrong way round, AE &minus;1, answer = 6.81 &times; 10<sup>&minus;3</sup>.<br>If <i>K</i><sub>p</sub> inverted in (c)(i) allow max 2 for substitution and consequential units.",
        "mark": 4,
        "spec": "3.1.10"
    },
    "2003-june-chm4-q2di": {
        "answers": "<b>Increased</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2003-june-chm4-q2dii": {
        "answers": "<b>Increased</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2003-june-chm4-q3ai": {
        "answers": "<b><i>K</i><sub>w</sub> = [H<sup>+</sup>][OH<sup>&minus;</sup>]</b> (1)",
        "extra": "Or in words or below unless contradiction.<br>If <i>K</i><sub>w</sub> includes H<sub>2</sub>O allow 6.63 if seen otherwise no marks likely.",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-june-chm4-q3aii": {
        "answers": "<b>pH = &minus;log [H<sup>+</sup>]</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-june-chm4-q3aiii": {
        "answers": "• [H<sup>+</sup>] = &radic;(5.48 &times; 10<sup>&minus;14</sup>) = 2.34 &times; 10<sup>&minus;7</sup> (1)<br>• pH = <b>6.63 or 6.64</b> (1)<br>• Pure water &there4; <b>[H<sup>+</sup>] = [OH<sup>&minus;</sup>]</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.12"
    },
    "2003-june-chm4-q3bi": {
        "answers": "• [OH<sup>&minus;</sup>] = 0.150 &rArr; [H<sup>+</sup>] = 10<sup>&minus;14</sup> / 0.150 = 6.66 &times; 10<sup>&minus;14</sup> (1) [or pOH = 0.82]<br>• pH = <b>13.18</b> (or 13.17) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2003-june-chm4-q3bii": {
        "answers": "• Moles OH<sup>&minus;</sup> = (35 &times; 10<sup>&minus;3</sup>) &times; 0.150 = <b>5.25 &times; 10<sup>&minus;3</sup></b> (1)<br>• Moles H<sup>+</sup> = (40 &times; 10<sup>&minus;3</sup>) &times; 0.120 = <b>4.80 &times; 10<sup>&minus;3</sup></b> (1)<br>• Excess moles OH<sup>&minus;</sup> = 5.25 &times; 10<sup>&minus;3</sup> &minus; 4.80 &times; 10<sup>&minus;3</sup> = <b>4.5 &times; 10<sup>&minus;4</sup></b> (1)<br>• [OH<sup>&minus;</sup>] = (4.5 &times; 10<sup>&minus;4</sup>) &times; (1000 / 75) = <b>6.00 &times; 10<sup>&minus;3</sup> mol dm<sup>&minus;3</sup></b> (1)<br>• [H<sup>+</sup>] = 10<sup>&minus;14</sup> / (6.00 &times; 10<sup>&minus;3</sup>) = 1.66 &times; 10<sup>&minus;12</sup> (or pOH = 2.22) (1)<br>• pH = <b>11.78</b> (or 11.77) (1)",
        "extra": "If no volume used, max 4 (answer = 10.65).<br>If wrong volume used, max 5.<br>If no subtraction max 3.<br>If missing 1000 max 5 (answer = 8.78).<br>If uses excess as acid, max 4 (answer = 2.22).",
        "mark": 6,
        "spec": "3.1.12"
    },
    "2003-june-chm4-q3ci": {
        "answers": "<b><i>K</i><sub>a</sub> = [H<sup>+</sup>][X<sup>&minus;</sup>] / [HX]</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-june-chm4-q3cii": {
        "answers": "• [H<sup>+</sup>] = 1.80 &times; 10<sup>&minus;2</sup> &times; 0.150 = <b>2.70 &times; 10<sup>&minus;3</sup> mol dm<sup>&minus;3</sup></b> (1)<br>• <i>K</i><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [HX] (1)<br>• = (2.70 &times; 10<sup>&minus;3</sup>)<sup>2</sup> / 0.150 = <b>4.86 &times; 10<sup>&minus;5</sup></b> (or / 0.1473 = 4.95 &times; 10<sup>&minus;5</sup>) (1)<br>• Units: <b>mol dm<sup>&minus;3</sup></b> (1)",
        "extra": "If wrong K<sub>a</sub> in (i) max 2 in (ii) for [H+] and consequential units.<br>Mark on fully from minor errors (e.g. no [ ] or charges missing).",
        "mark": 4,
        "spec": "3.1.12"
    },
    "2003-june-chm4-q4a": {
        "answers": "• Nucleophilic attack: curly arrow from lone pair on :CN<sup>&minus;</sup> to carbonyl carbon (1)<br>• Carbonyl opening: curly arrow from C=O bond to oxygen (1)<br>• Intermediate tetrahedral anion structure with correct O<sup>&minus;</sup> (1)<br>• Protonation: curly arrow from :O<sup>&minus;</sup> lone pair to H<sup>+</sup> (1)<br>• Name of product: <b>2-hydroxypentanenitrile</b> (or 1-cyanobutan-1-ol) (1)",
        "extra": "Penalise HCN splitting if wrong.<br>Allow C<sub>3</sub>H<sub>7</sub> if structure shown elsewhere.<br>Be lenient on position of negative sign on :CN&minus; but arrow must come from lone pair.<br>Allow 2-hydroxypentanonitrile.",
        "mark": 5,
        "spec": "3.3.6"
    },
    "2003-june-chm4-q4b": {
        "answers": "• Nucleophilic attack: curly arrow from lone pair on :O of CH<sub>3</sub>OH to carbonyl carbon (1)<br>• Carbonyl opening: curly arrow from C=O bond to oxygen (1)<br>• Tetrahedral intermediate structure with O<sup>&minus;</sup> and O<sup>+</sup>H&minus;CH<sub>3</sub> (1)<br>• Elimination: curly arrow from :O<sup>&minus;</sup> reforming C=O and curly arrow from C&minus;Cl bond to Cl, and loss of H<sup>+</sup> (1)<br>• Name of organic product: <b>methyl propanoate</b> (1)",
        "extra": "C=O alone loses M2 but can score M1 for attack on C+.<br>In M4, allow extra :Cl&minus; attack on H, showing loss of H+.",
        "mark": 5,
        "spec": "3.3.9"
    },
    "2003-june-chm4-q4ci": {
        "answers": "<b>[CH<sub>3</sub>CO]<sup>+</sup></b> (or CH<sub>3</sub>C<sup>+</sup>=O) (1)",
        "extra": "Allow formula in an equation.<br>Be lenient on position of + on formula.",
        "mark": 1,
        "spec": "3.3.10"
    },
    "2003-june-chm4-q4cii": {
        "answers": "• Electrophilic attack: curly arrow from benzene ring &pi;-cloud to C<sup>+</sup> of [CH<sub>3</sub>CO]<sup>+</sup> (1)<br>• Intermediate: Wheland / arenium horseshoe ion with positive charge (1)<br>• Loss of proton: curly arrow from C&minus;H bond back into the ring (1)",
        "extra": "Don't be too harsh about horseshoe, but + must not be close to saturated C.<br>M3 must be final step not earlier; allow M3 even if structure (M2) is wrong.",
        "mark": 3,
        "spec": "3.3.10"
    },
    "2003-june-chm4-q5ai": {
        "answers": "<b>2-methylbut-1-ene</b> (1)",
        "extra": "Not: butan...",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2003-june-chm4-q5aii": {
        "answers": "• Repeating unit: <b>&minus;[C(CH<sub>3</sub>)(C<sub>2</sub>H<sub>5</sub>)&minus;CH<sub>2</sub>]&minus;</b> (1) [allow C<sub>2</sub>H<sub>5</sub>; allow 2X]<br>• Type of polymerisation: <b>addition</b> (or radical) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2003-june-chm4-q5aiii": {
        "answers": "• Name of mechanism: <b>electrophilic substitution</b> (1)<br>• Major product structure: <b>C<sub>6</sub>H<sub>5</sub>&minus;C(CH<sub>3</sub>)<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub></b> (benzene ring bonded to tertiary carbon of 2-methylbutane) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.10"
    },
    "2003-june-chm4-q5aiv": {
        "answers": "<b>CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub></b> (pent-2-ene) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2003-june-chm4-q5b": {
        "answers": "• Repeating unit: <b>&minus;[&minus;CO&minus;CH<sub>2</sub>&minus;CH<sub>2</sub>&minus;CO&minus;NH&minus;(CH<sub>2</sub>)<sub>6</sub>&minus;NH&minus;]&minus;</b> (2) [1 mark for dicarboxylic acid residue, 1 mark for diamine residue]<br>• Type of polymerisation: <b>condensation</b> (1)<br>• Name of linkage: <b>peptide</b> OR <b>(poly)amide</b> (1)",
        "extra": "Allow outer horizontal bonds to be omitted.<br>Allow HO&minus;[...]&minus;H if [...] shows repeating unit; if brackets missing in dimer, penalise one.<br>Allow CONH.<br>Peptide or amide must be spelled correctly.",
        "mark": 4,
        "spec": "3.3.12"
    }
}

def main():
    print("Ingesting 2003 June CHM4...")
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
            "image": f"img/2003-june-chm4/q_{short_id}.jpg",
            "markscheme_image": f"img/2003-june-chm4/ms_{short_id}.png",
            "markscheme_text": ms.get("answers", "").replace("<br>", "\n").replace("<b>", "**").replace("</b>", "**").replace("&minus;", "-").replace("&times;", "x").replace("&le;", "<=").replace("&ge;", ">=").replace("&rArr;", "=>")
        }
        db["questions"].append(q_obj)
        
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully ingested {len(QUESTIONS_DEF)} questions for {PAPER_INFO['id']}!")

if __name__ == "__main__":
    main()

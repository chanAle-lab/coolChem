"""
Ingestion script for 2003 January CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q7 and Q8).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463604_1e358153.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-jan-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-jan-chm4",
    "year": 2003,
    "series": "January",
    "date": "2003-01-22",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour 30 mins"
}

QUESTIONS_DEF = [
    # Page 4: Question 1
    ("2003-jan-chm4-q1ai", "1(a)(i)", 4, 150, 425, 3, ["3.1.9"], ["calculation"], "Complete table of initial rates and concentrations for rate = k[P]^2[Q]."),
    ("2003-jan-chm4-q1aii", "1(a)(ii)", 4, 428, 620, 3, ["3.1.9"], ["calculation"], "Calculate value of rate constant k with units from Experiment 1."),
    ("2003-jan-chm4-q1b", "1(b)", 4, 622, 705, 1, ["3.1.9"], ["recall"], "Change in reaction conditions that alters rate constant k."),
    
    # Page 5: Question 2(a)-(b)
    ("2003-jan-chm4-q2ai", "2(a)(i)", 5, 80, 305, 2, ["3.1.6"], ["calculation"], "Calculate equilibrium moles of O2 and NO from dissociation of NO2."),
    ("2003-jan-chm4-q2aii", "2(a)(ii)", 5, 308, 485, 2, ["3.1.6"], ["calculation"], "Calculate original moles of NO2 and equilibrium moles of NO2."),
    ("2003-jan-chm4-q2b", "2(b)", 5, 488, 725, 4, ["3.1.6"], ["calculation"], "Write expression for Kc and calculate its value and units at temperature T."),
    
    # Page 6: Question 2(c)-(d)
    ("2003-jan-chm4-q2c", "2(c)", 6, 80, 290, 3, ["3.1.2"], ["calculation"], "Use ideal gas equation to determine temperature T for 0.683 mol gas at 3.30x10^5 Pa."),
    ("2003-jan-chm4-q2d", "2(d)", 6, 292, 410, 2, ["3.1.6"], ["analysis"], "Effect of heating same mass in larger flask on yield of oxygen and Kc."),
    
    # Page 7: Question 3(a)-(b)
    ("2003-jan-chm4-q3a", "3(a)", 7, 80, 490, 2, ["3.1.12"], ["calculation"], "Calculate volume x of NaOH added at equivalence point on pH titration curve."),
    ("2003-jan-chm4-q3bi", "3(b)(i)", 7, 492, 570, 1, ["3.1.12"], ["recall"], "Define the term pH."),
    ("2003-jan-chm4-q3bii", "3(b)(ii)", 7, 572, 630, 1, ["3.1.12"], ["analysis"], "Suggest a value for pH at equivalence point c."),
    ("2003-jan-chm4-q3biii", "3(b)(iii)", 7, 632, 735, 1, ["3.1.12"], ["recall"], "Identify suitable indicator for titration from pH curve."),
    
    # Page 8: Question 3(c)-(d)
    ("2003-jan-chm4-q3ci", "3(c)(i)", 8, 80, 160, 1, ["3.1.12"], ["recall"], "Explain the term weak as applied to acid HA."),
    ("2003-jan-chm4-q3cii", "3(c)(ii)", 8, 162, 240, 1, ["3.1.12"], ["recall"], "Write an expression for Ka for weak acid HA."),
    ("2003-jan-chm4-q3ciii", "3(c)(iii)", 8, 242, 435, 3, ["3.1.12"], ["calculation"], "Calculate pH of 0.150 mol dm-3 HA before adding NaOH (point a)."),
    ("2003-jan-chm4-q3d", "3(d)", 8, 438, 640, 3, ["3.1.12"], ["calculation"], "Calculate pH of half-neutralised buffer solution at x/2 (point b)."),
    
    # Page 9: Question 4(a)-(c)
    ("2003-jan-chm4-q4a", "4(a)", 9, 80, 215, 1, ["3.3.13"], ["recall"], "Give systematic IUPAC name for alanine."),
    ("2003-jan-chm4-q4bi", "4(b)(i)", 9, 218, 360, 2, ["3.3.7"], ["recall"], "Explain the meaning of the term stereoisomers."),
    ("2003-jan-chm4-q4bii", "4(b)(ii)", 9, 362, 475, 2, ["3.3.7"], ["practical", "recall"], "State how stereoisomers of alanine can be distinguished."),
    ("2003-jan-chm4-q4c", "4(c)", 9, 478, 680, 1, ["3.3.13"], ["recall"], "Give structural formula of species formed by glycine at pH 14."),
    
    # Page 10: Question 4(d)-(e)
    ("2003-jan-chm4-q4d", "4(d)", 10, 80, 485, 2, ["3.3.13"], ["recall"], "Give structural formulae of two dipeptides formed from alanine and glycine."),
    ("2003-jan-chm4-q4e", "4(e)", 10, 488, 735, 1, ["3.3.13"], ["recall"], "Structural formula of organic compound from glycine, methanol and conc H2SO4."),
    
    # Page 12: Question 5(a)-(f) (referring to Page 11 NMR spectrum)
    ("2003-jan-chm4-q5a", "5(a)", 12, 80, 295, 1, ["3.3.15"], ["analysis"], "How many different types of proton are present in compound X?"),
    ("2003-jan-chm4-q5b", "5(b)", 12, 298, 360, 1, ["3.3.15"], ["analysis"], "Whole-number ratio of each type of proton in compound X."),
    ("2003-jan-chm4-q5c", "5(c)", 12, 362, 440, 1, ["3.3.15"], ["analysis"], "Part of structure of X deduced from peak at delta 2.20."),
    ("2003-jan-chm4-q5d", "5(d)", 12, 442, 595, 3, ["3.3.15"], ["analysis"], "Identify alkyl group from peaks at delta 4.13 and 1.26 and explain splitting."),
    ("2003-jan-chm4-q5e", "5(e)", 12, 598, 672, 1, ["3.3.15"], ["analysis"], "Part of structure of X deduced from splitting of peaks at delta 2.76 and 2.57."),
    ("2003-jan-chm4-q5f", "5(f)", 12, 675, 785, 2, ["3.3.15"], ["analysis"], "Deduce the structure of compound X (C7H12O3)."),
    
    # Page 13: Question 6
    ("2003-jan-chm4-q6ai", "6(a)(i)", 13, 80, 215, 2, ["3.3.11"], ["recall"], "Explain Bronsted-Lowry base and write equation for methylamine with water."),
    ("2003-jan-chm4-q6aii", "6(a)(ii)", 13, 218, 280, 1, ["3.1.12", "3.3.11"], ["recall"], "Substance added to aqueous methylamine to prepare a basic buffer."),
    ("2003-jan-chm4-q6aiii", "6(a)(iii)", 13, 282, 410, 2, ["3.1.12", "3.3.11"], ["analysis"], "Explain how basic buffer resists change in pH when NaOH is added."),
    ("2003-jan-chm4-q6b", "6(b)", 13, 412, 535, 2, ["3.3.11"], ["analysis"], "Explain why methylamine is a stronger base than ammonia."),
    ("2003-jan-chm4-q6c", "6(c)", 13, 538, 770, 2, ["3.3.11"], ["recall"], "Name mechanism and draw structure of cation from methylamine and excess bromoethane.")
]

MS_DATA = {
    "2003-jan-chm4-q1ai": {
        "answers": "• Experiment 2 Initial rate: <b>0.4(0) &times; 10<sup>&minus;3</sup></b> (1)<br>• Experiment 3 Initial [Q]: <b>0.15</b> (1)<br>• Experiment 4 Initial [P]: <b>0.28</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.9"
    },
    "2003-jan-chm4-q1aii": {
        "answers": "• <i>k</i> = (4.8 &times; 10<sup>&minus;3</sup>) / [(0.20)<sup>2</sup> &times; (0.30)] (1)<br>• = <b>0.4(0)</b> (1)<br>• Units = <b>mol<sup>&minus;2</sup> dm<sup>6</sup> s<sup>&minus;1</sup></b> (1)",
        "extra": "Consequential on calculation.",
        "mark": 3,
        "spec": "3.1.9"
    },
    "2003-jan-chm4-q1b": {
        "answers": "<b>(Change in) temperature</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2003-jan-chm4-q2ai": {
        "answers": "• Number of moles of O<sub>2</sub> = 7.04 / 32 = <b>0.22</b> (mol) (1)<br>• Number of moles of NO = <b>0.44</b> (mol) (or 2 &times; mol of oxygen) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2003-jan-chm4-q2aii": {
        "answers": "• Original moles of NO<sub>2</sub> = 21.3 / 46 = <b>0.46(3)</b> (mol) (1)<br>• Moles of NO<sub>2</sub> at equilibrium = 0.46(3) &minus; 0.44 = <b>0.02(3)</b> (mol) (1)",
        "extra": "Consequential on mol NO above.",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2003-jan-chm4-q2b": {
        "answers": "• Expression: <b><i>K</i><sub>c</sub> = [NO]<sup>2</sup> [O<sub>2</sub>] / [NO<sub>2</sub>]<sup>2</sup></b> (1)<br>• Calculation: <i>K</i><sub>c</sub> = [(0.44/11.5)<sup>2</sup> &times; (0.22/11.5)] / (0.023/11.5)<sup>2</sup> (1)<br>• = <b>7.0(0)</b> (1)<br>• Units: <b>mol dm<sup>&minus;3</sup></b> (1)",
        "extra": "If mol NO2 = 0.02: Kc = 9.26 (9.3).<br>Consequential on values from (a).<br>If vol missed: score only Kc expression and units.<br>If Kc wrong: max 2 for correct use of vol and consequential units.",
        "mark": 4,
        "spec": "3.1.6"
    },
    "2003-jan-chm4-q2c": {
        "answers": "• <i>pV</i> = <i>nRT</i> &rarr; <i>T</i> = <i>pV</i> / <i>nR</i> (1)<br>• = (3.30 &times; 10<sup>5</sup> &times; 11.5 &times; 10<sup>&minus;3</sup>) / (0.683 &times; 8.31) (1)<br>• = <b>669 K</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-jan-chm4-q2d": {
        "answers": "• Yield of oxygen: <b>Increased</b> (1)<br>• Value of <i>K</i><sub>c</sub>: <b>No effect</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2003-jan-chm4-q3a": {
        "answers": "• Moles HA = (25 / 1000) &times; 0.150 = 3.75 &times; 10<sup>&minus;3</sup> (1)<br>• Volume NaOH = (3.75 &times; 10<sup>&minus;3</sup>) / 0.20 = 1.875 &times; 10<sup>&minus;2</sup> dm<sup>3</sup> OR <b>18.75 cm<sup>3</sup></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q3bi": {
        "answers": "<b>pH = &minus;log<sub>10</sub>[H<sup>+</sup>]</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q3bii": {
        "answers": "<b>Value above 7 but below 11</b> (e.g. 8.5 to 9.5) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q3biii": {
        "answers": "<b>Phenol red</b> OR <b>thymol blue</b> OR <b>phenolphthalein</b> OR <b>thymolphthalein</b> (1)",
        "extra": "i.e. indicator with 7 < pKin < 11.",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q3ci": {
        "answers": "<b>Only slightly dissociated / ionised</b> (1)",
        "extra": "NOT 'not fully dissociated / ionised'.",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q3cii": {
        "answers": "<b><i>K</i><sub>a</sub> = [H<sup>+</sup>][A<sup>&minus;</sup>] / [HA]</b> (1)",
        "extra": "NOT [H+]^2 / [HA].",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q3ciii": {
        "answers": "• <i>K</i><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [HA] (1)<br>• [H<sup>+</sup>] = &radic;(2.75 &times; 10<sup>&minus;5</sup> &times; 0.15) = 2.03 &times; 10<sup>&minus;3</sup> (1)<br>• <b>pH = 2.69</b> (1)",
        "extra": "pH should be given to 2 decimal places; penalise answer to 1 dp once in question.",
        "mark": 3,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q3d": {
        "answers": "• Moles OH<sup>&minus;</sup> added = 1.875 &times; 10<sup>&minus;3</sup> = moles A<sup>&minus;</sup> = moles HA left [so [A<sup>&minus;</sup>] = [HA]] (1)<br>• <i>K</i><sub>a</sub> = [H<sup>+</sup>] OR <b>pH = p<i>K</i><sub>a</sub></b> (1)<br>• <b>pH = 4.56</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q4a": {
        "answers": "<b>2-aminopropanoic acid</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2003-jan-chm4-q4bi": {
        "answers": "• <b>Molecules with same structure / structural formula</b> (1)<br>• <b>but with bonds / atoms / groups arranged differently in space / 3D</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.7"
    },
    "2003-jan-chm4-q4bii": {
        "answers": "• <b>(Plane) polarised light</b> (1)<br>• <b>Rotated (equally) in opposite directions</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.7"
    },
    "2003-jan-chm4-q4c": {
        "answers": "<b>H<sub>2</sub>N&minus;CH<sub>2</sub>&minus;COO<sup>&minus;</sup></b> (1)",
        "extra": "Penalise NH2- and OH- once per paper, but CH3- is allowed.",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2003-jan-chm4-q4d": {
        "answers": "• Dipeptide 1: <b>H<sub>2</sub>N&minus;CH(CH<sub>3</sub>)&minus;CONH&minus;CH<sub>2</sub>&minus;COOH</b> (1)<br>• Dipeptide 2: <b>H<sub>2</sub>N&minus;CH<sub>2</sub>&minus;CONH&minus;CH(CH<sub>3</sub>)&minus;COOH</b> (1)",
        "extra": "Not anhydrides; not repeating units.",
        "mark": 2,
        "spec": "3.3.13"
    },
    "2003-jan-chm4-q4e": {
        "answers": "<b>H<sub>2</sub>N&minus;CH<sub>2</sub>&minus;COOCH<sub>3</sub></b> (methyl 2-aminoethanoate) (1)",
        "extra": "Allow displayed or condensed formula.",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2003-jan-chm4-q5a": {
        "answers": "<b>5</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2003-jan-chm4-q5b": {
        "answers": "<b>2 : 2 : 2 : 3 : 3</b> (1)",
        "extra": "Any order, but not multiples.",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2003-jan-chm4-q5c": {
        "answers": "<b>CH<sub>3</sub>&minus;C(=O)&minus;</b> (methyl ketone group) (1)",
        "extra": "Allow CH3CO-R.",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2003-jan-chm4-q5d": {
        "answers": "• Alkyl group: <b>CH<sub>3</sub>CH<sub>2</sub></b> OR <b>C<sub>2</sub>H<sub>5</sub></b> OR <b>ethyl</b> (1)<br>• Explanation:<br>&nbsp;&nbsp;&ndash; <b>&delta; 4.13 (quartet): CH<sub>2</sub> peak split by CH<sub>3</sub> / next to CH<sub>3</sub></b> (1)<br>&nbsp;&nbsp;&ndash; <b>&delta; 1.26 (triplet): CH<sub>3</sub> peak split by CH<sub>2</sub> / next to CH<sub>2</sub></b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.3.15"
    },
    "2003-jan-chm4-q5e": {
        "answers": "<b>&minus;CH<sub>2</sub>CH<sub>2</sub>&minus;</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2003-jan-chm4-q5f": {
        "answers": "<b>CH<sub>3</sub>&minus;CO&minus;CH<sub>2</sub>CH<sub>2</sub>&minus;COO&minus;CH<sub>2</sub>CH<sub>3</sub></b> (ethyl 4-oxopentanoate) (2)",
        "extra": "Must be C7H12O3.<br>Allow (1) for CH3COCH2CH2OCOCH2CH3 or CH3COOCH2CH2COCH2CH3.",
        "mark": 2,
        "spec": "3.3.15"
    },
    "2003-jan-chm4-q6ai": {
        "answers": "• Definition: <b>H<sup>+</sup> / proton acceptor</b> (1)<br>• Equation: <b>CH<sub>3</sub>NH<sub>2</sub> + H<sub>2</sub>O &rightleftharpoons; CH<sub>3</sub>N<sup>+</sup>H<sub>3</sub> + OH<sup>&minus;</sup></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.11"
    },
    "2003-jan-chm4-q6aii": {
        "answers": "<b>CH<sub>3</sub>NH<sub>3</sub>Cl</b> OR <b>HCl</b> (1)",
        "extra": "Allow name or formula.<br>Allow any ammonium compound or any strong acid.",
        "mark": 1,
        "spec": "3.3.11"
    },
    "2003-jan-chm4-q6aiii": {
        "answers": "<b>Any two from:</b><br>• <b>(Extra) OH<sup>&minus;</sup> reacts with CH<sub>3</sub>N<sup>+</sup>H<sub>3</sub></b> (1)<br>• <b>Reaction / equilibrium moves to left</b> (1)<br>• <b>Ratio [salt] / [base] remains almost constant</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2003-jan-chm4-q6b": {
        "answers": "• <b>Lone pair (on N) accepts H<sup>+</sup></b> (1)<br>• <b>CH<sub>3</sub> increases electron density (on N) / donates or pushes electrons / has positive inductive effect</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.11"
    },
    "2003-jan-chm4-q6c": {
        "answers": "• Name of mechanism: <b>nucleophilic substitution</b> (1)<br>• Structure: <b>[CH<sub>3</sub>&minus;N<sup>+</sup>(C<sub>2</sub>H<sub>5</sub>)<sub>3</sub>]</b> (or drawn displayed cation) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.11"
    }
}

def crop_question_image(doc, page_num, y0, y1, out_path, x0=35, x1=545, scale=2.0):
    page = doc[page_num - 1]
    rect = fitz.Rect(x0, max(0, y0), x1, min(page.rect.height, y1))
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=rect)
    im = Image.open(fitz.io.BytesIO(pix.tobytes("png")))
    im.convert("RGB").save(out_path, quality=90)
    return out_path

def main():
    print(f"Opening QP: {QP_PATH}")
    doc = fitz.open(QP_PATH)
    
    # Save NMR Spectrum figure from Page 11
    fig_rel = "img/2003-jan-chm4/fig-q5-nmr.jpg"
    fig_abs = os.path.join(REPO_DIR, fig_rel)
    crop_question_image(doc, 11, 80, 750, fig_abs)
    
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    papers = [p for p in db["papers"] if p["id"] != PAPER_INFO["id"]]
    papers.append(PAPER_INFO)
    db["papers"] = papers
    
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
    new_questions = []
    
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        sub_id = q_label.replace("(", "").replace(")", "").replace(" ", "")
        q_img_rel = f"img/2003-jan-chm4/q_q{sub_id}.jpg"
        ms_img_rel = f"img/2003-jan-chm4/ms_q{sub_id}.jpg"
        
        q_img_abs = os.path.join(REPO_DIR, q_img_rel)
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel)
        
        crop_question_image(doc, p_num, y0, y1, q_img_abs)
        
        ms_item = MS_DATA.get(q_id, {})
        render_official_markscheme_image(
            question_label=q_label,
            answers_html=ms_item.get("answers", ""),
            extra_html=ms_item.get("extra", ""),
            marks=ms_item.get("mark", marks),
            spec_ref=ms_item.get("spec", topics[0] if topics else ""),
            output_path=ms_img_abs
        )
        
        ms_text = ms_item.get("answers", "").replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "").replace("&minus;", "-").replace("&times;", "x").replace("&rarr;", "->").replace("&Sigma;", "Sum ").replace("&Delta;", "Delta ").replace("&there4;", "therefore ").replace("&nbsp;", " ")
        if ms_item.get("extra"):
            ms_text += "\n\n[Extra Information]:\n" + ms_item.get("extra", "").replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "").replace("&minus;", "-").replace("&times;", "x").replace("&rarr;", "->")
            
        figs = [fig_rel] if q_label.startswith("5") else []
        
        q_entry = {
            "id": q_id,
            "paper": PAPER_INFO["id"],
            "question": q_label,
            "marks": marks,
            "page": p_num,
            "topics": topics,
            "skills": skills,
            "summary": summary,
            "image": q_img_rel,
            "figures": figs,
            "markscheme": ms_img_rel,
            "markscheme_text": ms_text
        }
        new_questions.append(q_entry)
        
    db["questions"].extend(new_questions)
    
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully processed {len(new_questions)} Section A questions for {PAPER_INFO['id']}.")

if __name__ == "__main__":
    main()

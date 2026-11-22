"""
Ingestion script for 2003 January CHM6/W (Synoptic Multiple Choice Assessment)
Crops all 40 questions and generates modern official mark scheme tables with correct answer keys.
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463646_b66d4ace.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-jan-chm6w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-jan-chm6w",
    "year": 2003,
    "series": "January",
    "date": "2003-01-27",
    "code": "CHM6/W",
    "unit": "Unit 6a: Synoptic Assessment (Multiple Choice)",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 40,
    "duration": "1 hour"
}

KEYS = {
    1: 'B', 2: 'C', 3: 'C', 4: 'C', 5: 'D', 6: 'C', 7: 'D', 8: 'A', 9: 'C', 10: 'B',
    11: 'D', 12: 'B', 13: 'C', 14: 'B', 15: 'D', 16: 'B', 17: 'D', 18: 'C', 19: 'D', 20: 'D',
    21: 'B', 22: 'C', 23: 'B', 24: 'C', 25: 'C', 26: 'A', 27: 'C', 28: 'B', 29: 'A', 30: 'B',
    31: 'C', 32: 'D', 33: 'D', 34: 'A', 35: 'C', 36: 'A', 37: 'A', 38: 'A', 39: 'D', 40: 'A'
}

# (q_num, page_num (1-indexed), y0, y1, topics, skills, summary, figs)
MCQ_DEF = [
    # Page 4: Questions 1-2
    (1, 4, 430, 585, ["3.1.6"], ["recall"], "Equilibrium moles of O2 in gas-phase synthesis of SO3.", ["img/2003-jan-chm6w/fig-q1-5-stem.jpg"]),
    (2, 4, 588, 760, ["3.1.6"], ["calculation"], "Mole fraction of SO3 in equilibrium mixture.", ["img/2003-jan-chm6w/fig-q1-5-stem.jpg"]),
    
    # Page 5: Questions 3-6
    (3, 5, 80, 240, ["3.1.10"], ["recall"], "Units for equilibrium constant Kp.", ["img/2003-jan-chm6w/fig-q1-5-stem.jpg"]),
    (4, 5, 242, 395, ["3.1.8"], ["calculation"], "Standard entropy change Delta S for 2SO2 + O2 -> 2SO3.", ["img/2003-jan-chm6w/fig-q1-5-stem.jpg"]),
    (5, 5, 398, 590, ["3.1.5", "3.1.6"], ["analysis"], "Effect of catalyst on equilibrium composition and rate.", ["img/2003-jan-chm6w/fig-q1-5-stem.jpg"]),
    (6, 5, 592, 770, ["3.1.2"], ["calculation"], "Mass of water containing same number of atoms as 3.0 g of NO.", []),
    
    # Page 6: Questions 7-10
    (7, 6, 80, 250, ["3.1.8"], ["analysis"], "Why lattice enthalpy of MgCl2 is much greater than that of NaCl.", []),
    (8, 6, 252, 420, ["3.1.4"], ["calculation"], "Enthalpy change of solution calculation.", []),
    (9, 6, 422, 590, ["3.1.5"], ["analysis"], "Activation energy on Maxwell-Boltzmann distribution.", []),
    (10, 6, 592, 765, ["3.1.12"], ["calculation"], "pH of mixture of strong acid and strong base.", []),
    
    # Page 7: Questions 11-13
    (11, 7, 80, 250, ["3.2.2"], ["practical"], "Solution that would not give white precipitate with BaCl2.", []),
    (12, 7, 252, 410, ["3.2.5"], ["recall"], "Electronic configuration of transition metal ion in complex.", []),
    (13, 7, 412, 765, ["3.1.11"], ["analysis"], "Standard electrode potentials and feasibility of redox reaction.", []),
    
    # Page 8: Questions 14-16
    (14, 8, 80, 370, ["3.1.2"], ["calculation"], "Percentage of copper in salt by thiosulphate titration.", []),
    (15, 8, 380, 680, ["3.3.4", "3.3.5"], ["analysis"], "Reaction sequence A to C: identify reagent for Step 1.", []),
    (16, 8, 682, 765, ["3.3.4", "3.3.5"], ["analysis"], "Reaction sequence A to C: identify intermediate B.", []),
    
    # Page 9: Questions 17-19
    (17, 9, 80, 435, ["3.3.2", "3.3.4"], ["analysis"], "Propane reaction sequence: reaction type for Step 1.", []),
    (18, 9, 438, 605, ["3.3.3", "3.3.4"], ["analysis"], "Propane reaction sequence: identify reagent for Step 2.", []),
    (19, 9, 608, 765, ["3.3.1"], ["recall"], "Number of structural isomers with molecular formula C4H9Cl.", []),
    
    # Page 10: Questions 20-21
    (20, 10, 80, 240, ["3.3.6"], ["analysis"], "Compound with major peak in mass spectrum at m/z = 57.", []),
    (21, 10, 242, 765, ["3.3.7"], ["recall"], "Compound which exhibits optical isomerism.", []),
    
    # Page 11: Questions 22-23
    (22, 11, 265, 630, ["3.1.6"], ["analysis"], "Methanol synthesis: effect of increasing total pressure.", []),
    (23, 11, 632, 765, ["3.1.6"], ["analysis"], "Methanol synthesis: effect of temperature on equilibrium.", []),
    
    # Page 12: Questions 24-26
    (24, 12, 175, 345, ["3.3.5"], ["recall"], "Hazards associated with industrial methanol synthesis.", []),
    (25, 12, 348, 515, ["3.1.1"], ["recall"], "Statements regarding isotopes of chlorine 35Cl and 37Cl.", []),
    (26, 12, 518, 765, ["3.1.3"], ["recall"], "Molecules that possess a dipole moment.", []),
    
    # Page 13: Questions 27-29
    (27, 13, 175, 335, ["3.2.5"], ["recall"], "Solutions that are colourless: identification.", []),
    (28, 13, 338, 500, ["3.2.1"], ["recall"], "Period 3 elements: properties and trends.", []),
    (29, 13, 505, 765, ["3.1.2"], ["calculation"], "Extraction of iron from Fe2O3: stoichiometric statements.", []),
    
    # Page 14: Questions 30-31
    (30, 14, 175, 565, ["3.2.5"], ["analysis"], "Chromium reaction scheme: oxidation states and equilibria.", []),
    (31, 14, 570, 765, ["3.1.12"], ["recall"], "Properties and pH of aqueous solutions of salts.", []),
    
    # Page 15: Questions 32-34
    (32, 15, 175, 335, ["3.1.7"], ["recall"], "Identification of redox reactions among given pairs.", []),
    (33, 15, 338, 490, ["3.2.2"], ["recall"], "Group II compounds: solubility and reaction with acid.", []),
    (34, 15, 492, 765, ["3.3.3"], ["recall"], "Reactions involving halogenoalkanes.", []),
    
    # Page 16: Questions 35-37
    (35, 16, 175, 330, ["3.3.5"], ["recall"], "Methods for obtaining ethane-1,2-diol.", []),
    (36, 16, 332, 495, ["3.3.8"], ["recall"], "Reactions and oxidation of carbonyl compounds.", []),
    (37, 16, 500, 765, ["3.3.9"], ["recall"], "Esters and carboxylic acids reactions.", []),
    
    # Page 17: Questions 38-40
    (38, 17, 175, 345, ["3.3.2"], ["recall"], "Chlorination of methane in UV light: products.", []),
    (39, 17, 348, 500, ["3.3.15"], ["analysis"], "1H NMR splitting patterns and chemical shifts.", []),
    (40, 17, 505, 765, ["3.3.1"], ["recall"], "Isomerism and functional group identification.", [])
]

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
    
    # Crop shared figure for Questions 1-5 stem from Page 4
    fig_stem_rel = "img/2003-jan-chm6w/fig-q1-5-stem.jpg"
    crop_question_image(doc, 4, 150, 425, os.path.join(REPO_DIR, fig_stem_rel))
    
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    papers = [p for p in db["papers"] if p["id"] != PAPER_INFO["id"]]
    papers.append(PAPER_INFO)
    db["papers"] = papers
    
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
    new_questions = []
    
    for q_num, p_num, y0, y1, topics, skills, summary, figs in MCQ_DEF:
        q_label = str(q_num)
        q_id = f"2003-jan-chm6w-q{q_num}"
        key = KEYS[q_num]
        
        q_img_rel = f"img/2003-jan-chm6w/q_q{q_num}.jpg"
        ms_img_rel = f"img/2003-jan-chm6w/ms_q{q_num}.jpg"
        
        q_img_abs = os.path.join(REPO_DIR, q_img_rel)
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel)
        
        crop_question_image(doc, p_num, y0, y1, q_img_abs)
        
        ans_html = f"<b>Correct Key: {key}</b>"
        extra_html = "Multiple Choice Question"
        
        render_official_markscheme_image(
            question_label=f"Question {q_num}",
            answers_html=ans_html,
            extra_html=extra_html,
            marks=1,
            spec_ref=topics[0] if topics else "",
            output_path=ms_img_abs
        )
        
        ms_text = f"Correct Answer: {key}\n(1 mark)\n[Extra Information]: Multiple Choice Question"
        
        q_entry = {
            "id": q_id,
            "paper": PAPER_INFO["id"],
            "question": q_label,
            "marks": 1,
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
        
    print(f"Successfully processed {len(new_questions)} MCQ questions for {PAPER_INFO['id']}.")

if __name__ == "__main__":
    main()

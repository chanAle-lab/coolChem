"""
Ingestion script for 2004 June CHM6/W (Synoptic Unit 6a)
40 Multiple Choice Questions (1 mark each).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795381684229_21b2f7b1.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-june-chm6w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-june-chm6w",
    "year": 2004,
    "series": "June",
    "date": "2004-06-29",
    "code": "CHM6/W",
    "unit": "Unit 6(a): Synoptic Paper",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 40,
    "duration": "1 hour"
}

KEYS = {
    1: 'D', 2: 'C', 3: 'A', 4: 'C', 5: 'B', 6: 'D', 7: 'A', 8: 'A', 9: 'A', 10: 'D',
    11: 'B', 12: 'D', 13: 'B', 14: 'D', 15: 'C', 16: 'B', 17: 'B', 18: 'A', 19: 'B', 20: 'D',
    21: 'B', 22: 'A', 23: 'C', 24: 'D', 25: 'B', 26: 'B', 27: 'D', 28: 'B', 29: 'B', 30: 'A',
    31: 'B', 32: 'A', 33: 'A', 34: 'A', 35: 'C', 36: 'A', 37: 'A', 38: 'B', 39: 'A', 40: 'A'
}

# (q_num, page, y0, y1, spec_topics, skills, prompt_summary, figures)
QUESTIONS = [
    # Page 5: Q1-3
    (1, 5, 150, 465, ["3.1.4"], ["calculation"], "Enthalpy of thermal dissociation when butane forms propane, hydrogen and carbon.", []),
    (2, 5, 468, 610, ["3.1.4"], ["calculation"], "Enthalpy of combustion of propane calculated from formation data.", ["img/2004-june-chm6w/fig-q1-2-stem.jpg"]),
    (3, 5, 612, 795, ["3.1.2"], ["calculation"], "Mole fraction of butane in mixture with minimum oxygen for complete combustion.", []),

    # Page 6: Q4-6
    (4, 6, 80, 380, ["3.1.6"], ["calculation"], "Equilibrium constant for ethanoic acid and ethanol esterification.", []),
    (5, 6, 382, 535, ["3.1.2", "3.1.6"], ["calculation"], "Percentage of ethanoic acid converted into ethyl ethanoate ester.", ["img/2004-june-chm6w/fig-q4-6-stem.jpg"]),
    (6, 6, 538, 675, ["3.3.5", "3.3.6"], ["analysis"], "Statement that is not correct concerning the ester ethyl ethanoate.", ["img/2004-june-chm6w/fig-q4-6-stem.jpg"]),

    # Page 7: Q7-9
    (7, 7, 80, 235, ["3.2.2"], ["recall"], "Hydroxide that will produce a saturated solution with the highest pH.", []),
    (8, 7, 238, 405, ["3.1.2"], ["calculation"], "Maximum mass of iron extracted from 1.0 tonne of 85% Fe2O3 ore.", []),
    (9, 7, 408, 600, ["3.1.7"], ["recall"], "Reaction in which hydrogen does not act as a reducing agent.", []),

    # Page 8: Q10-12
    (10, 8, 80, 300, ["3.1.7"], ["recall"], "Reaction where the role of the reagent is stated correctly.", []),
    (11, 8, 302, 450, ["3.1.7", "3.2.5"], ["recall"], "Species that could act either as an oxidising agent or as a reducing agent.", []),
    (12, 8, 452, 720, ["3.1.11"], ["calculation"], "Species that could reduce 0.012 mol of bromine based on electrode potentials.", []),

    # Page 9: Q13-17
    (13, 9, 80, 280, ["3.1.2"], ["calculation"], "Volume of oxygen required to burn 0.1 mol of butane to steam and CO at 295K and 100kPa.", []),
    (14, 9, 282, 415, ["3.3.5", "3.3.6"], ["recall"], "Ketone that does not have a major peak in its mass spectrum at m/z = 43.", []),
    (15, 9, 418, 550, ["3.3.6"], ["analysis"], "Ester that does not have a singlet peak in its proton NMR spectrum.", []),
    (16, 9, 552, 680, ["3.1.2"], ["calculation"], "Relative molecular mass of benzene-1,4-dicarboxylic acid.", []),
    (17, 9, 682, 785, ["3.3.1"], ["recall"], "Incorrect general formula for the listed non-cyclic compounds.", []),

    # Page 10: Q18-20
    (18, 10, 80, 520, ["3.3.3", "3.3.5"], ["recall"], "Statement that is not correct concerning the organic reaction scheme.", []),
    (19, 10, 522, 665, ["3.3.3"], ["recall"], "Reagent that would not bring about the indicated step in reaction scheme.", ["img/2004-june-chm6w/fig-q18-20-stem.jpg"]),
    (20, 10, 668, 775, ["3.3.1", "3.3.6"], ["analysis"], "Statement that is not correct concerning species W, X, Y and Z.", ["img/2004-june-chm6w/fig-q18-20-stem.jpg"]),

    # Page 11: Q21-23 (Directions summarised starts)
    (21, 11, 150, 535, ["3.1.5"], ["analysis"], "Correct statements about propanone + iodine rate equation.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (22, 11, 538, 665, ["3.1.5"], ["analysis"], "Correct statements about effects of temperature, NaOH and I2 on reaction rate.", ["img/2004-june-chm6w/fig-q21-22-stem.jpg", "img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (23, 11, 668, 795, ["3.1.3"], ["recall"], "Molecules with shape influenced by one or more lone pairs of electrons.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),

    # Page 12: Q24-27
    (24, 12, 175, 318, ["3.1.3"], ["recall"], "Substances in which covalent bonds must break on melting.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (25, 12, 320, 460, ["3.1.7"], ["recall"], "Reactions that are redox reactions.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (26, 12, 462, 605, ["3.1.12"], ["calculation"], "Acid solutions with a pH of 1.0.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (27, 12, 608, 775, ["3.1.8"], ["analysis"], "Reactions that will become feasible if the temperature is raised based on entropy.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),

    # Page 13: Q28-30
    (28, 13, 175, 330, ["3.2.5", "3.3.3"], ["recall"], "Reactions with ammonia that are substitution reactions.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (29, 13, 332, 485, ["3.1.7", "3.2.5"], ["analysis"], "Processes in which oxidation state of metal in complex ion is decreased.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (30, 13, 488, 660, ["3.1.3", "3.2.3", "3.3.10"], ["recall"], "Correct statements about AlCl3, BrF4-, AgI precipitate and Br2 vs I2 boiling point.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),

    # Page 14: Q31-34
    (31, 14, 175, 318, ["3.1.7"], ["recall"], "Reactions where the same element undergoes simultaneous oxidation and reduction.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (32, 14, 320, 475, ["3.1.1", "3.2.3"], ["recall"], "Correct statements about chloride ions.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (33, 14, 478, 615, ["3.3.13"], ["recall"], "Correct statements about amino acid glycine H2NCH2COOH.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (34, 14, 618, 795, ["3.1.2"], ["calculation"], "Compounds matching empirical composition 40% C, 6.67% H, 53.33% O.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),

    # Page 15: Q35-38
    (35, 15, 175, 330, ["3.3.5", "3.3.7"], ["analysis"], "Correct statements about marshmallow compound CH3CH(OH)CH2COOCH3.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (36, 15, 332, 475, ["3.3.2", "3.3.10"], ["recall"], "Reactions or processes where a carbocation is involved.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (37, 15, 478, 615, ["3.3.1"], ["recall"], "Pairs that are functional group isomers.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (38, 15, 618, 775, ["3.3.7"], ["recall"], "Compounds that possess stereoisomers (optical or geometric).", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),

    # Page 16: Q39-40
    (39, 16, 175, 460, ["3.3.2", "3.3.3"], ["recall"], "Types of reaction mechanism involved in the organic sequence.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
    (40, 16, 462, 750, ["3.3.9"], ["analysis"], "Correct statements about mechanism between ammonia and ethanoyl chloride.", ["img/2004-june-chm6w/fig-mcq-directions.jpg"]),
]

def main():
    doc = fitz.open(QP_PATH)

    # 1. Save shared stems
    # Q1-2 stem (Page 5)
    p5 = doc[4]
    rect_s1 = fitz.Rect(45, 150, 545, 315)
    pix = p5.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect_s1)
    Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").save(os.path.join(IMG_DIR, "fig-q1-2-stem.jpg"), quality=92)

    # Q4-6 stem (Page 6)
    p6 = doc[5]
    rect_s4 = fitz.Rect(45, 80, 545, 225)
    pix = p6.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect_s4)
    Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").save(os.path.join(IMG_DIR, "fig-q4-6-stem.jpg"), quality=92)

    # Q18-20 stem (Page 10)
    p10 = doc[9]
    rect_s18 = fitz.Rect(45, 80, 545, 355)
    pix = p10.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect_s18)
    Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").save(os.path.join(IMG_DIR, "fig-q18-20-stem.jpg"), quality=92)

    # Q21-22 stem (Page 11)
    p11 = doc[10]
    rect_s21 = fitz.Rect(45, 150, 545, 410)
    pix = p11.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect_s21)
    Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").save(os.path.join(IMG_DIR, "fig-q21-22-stem.jpg"), quality=92)

    # MCQ Directions box (Page 11)
    rect_dir = fitz.Rect(45, 80, 545, 270)
    pix = p11.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect_dir)
    Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").save(os.path.join(IMG_DIR, "fig-mcq-directions.jpg"), quality=92)

    print("Saved shared stems and directions figure.")

    new_questions = []

    for q_num, page_num, y0, y1, spec_topics, skills, prompt, figures in QUESTIONS:
        qid = f"2004-june-chm6w-q{q_num}"
        key = KEYS[q_num]
        q_label = str(q_num)

        # Question image crop
        page = doc[page_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-june-chm6w/q_q{q_num}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        # Official Mark Scheme Table
        ms_img_rel = f"img/2004-june-chm6w/ms_q{q_num}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ans_html = f"<b>{key}</b>"
        render_official_markscheme_image(q_label, ans_html, "", 1, spec_topics[0], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-june-chm6w",
            "year": 2004,
            "series": "June",
            "code": "CHM6/W",
            "unit": "Unit 6(a): Synoptic Paper",
            "question": q_label,
            "page": page_num,
            "marks": 1,
            "topics": spec_topics,
            "skills": skills,
            "summary": prompt,
            "description": prompt,
            "image": q_img_rel,
            "figures": figures,
            "markscheme": ms_img_rel,
            "markscheme_text": f"Key: {key} (1)"
        }
        new_questions.append(q_obj)

    print(f"Prepared {len(new_questions)} questions for 2004 June CHM6/W.")

    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    if not any(p["id"] == PAPER_INFO["id"] for p in db.get("papers", [])):
        db.setdefault("papers", []).append(PAPER_INFO)

    existing_ids = {q['id'] for q in new_questions}
    db['questions'] = [q for q in db['questions'] if q['id'] not in existing_ids]
    db['questions'].extend(new_questions)

    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("Saved questions.json successfully with June 2004 CHM6/W.")

if __name__ == "__main__":
    main()

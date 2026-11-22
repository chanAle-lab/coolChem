"""
Ingestion script for 2004 January CHM6/W (Synoptic Unit 6a)
40 Multiple Choice Questions (1 mark each).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377961015_0dd0a392.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-jan-chm6w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-jan-chm6w",
    "year": 2004,
    "series": "January",
    "date": "2004-01-26",
    "code": "CHM6/W",
    "unit": "Unit 6(a): Synoptic Paper",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 40,
    "duration": "1 hour"
}

KEYS = {
    1: 'B', 2: 'D', 3: 'A', 4: 'A', 5: 'B', 6: 'C', 7: 'C', 8: 'D', 9: 'B', 10: 'C',
    11: 'D', 12: 'D', 13: 'A', 14: 'D', 15: 'D', 16: 'D', 17: 'B', 18: 'C', 19: 'C', 20: 'D',
    21: 'A', 22: 'A', 23: 'B', 24: 'D', 25: 'B', 26: 'A', 27: 'A', 28: 'B', 29: 'B', 30: 'C',
    31: 'A', 32: 'D', 33: 'A', 34: 'A', 35: 'C', 36: 'C', 37: 'B', 38: 'A', 39: 'B', 40: 'C'
}

# (q_num, page, y0, y1, spec_topics, skills, prompt_summary, figures)
QUESTIONS = [
    # Page 5: Q1-3 (context at y=150)
    (1, 5, 150, 455, ["3.1.6"], ["recall"], "Units for equilibrium constant Kc for Reaction 2 in nitric acid production.", []),
    (2, 5, 458, 605, ["3.1.6"], ["recall"], "Conditions to increase equilibrium yield in all three industrial nitric acid reactions.", ["img/2004-jan-chm6w/fig-q1-3-stem.jpg"]),
    (3, 5, 608, 785, ["3.1.4"], ["calculation"], "Standard enthalpy change for direct oxidation of ammonia to nitrogen dioxide.", ["img/2004-jan-chm6w/fig-q1-3-stem.jpg"]),

    # Page 6: Q4-6
    (4, 6, 80, 295, ["3.1.2"], ["calculation"], "Volume of CO2 gas at 298K and 101kPa from decomposing 0.0500 mol NaHCO3.", []),
    (5, 6, 305, 540, ["3.1.12"], ["calculation"], "pH of 0.0010 mol dm-3 ethanedioic acid neglecting second ionisation.", []),
    (6, 6, 543, 775, ["3.1.2", "3.1.12"], ["calculation"], "Minimum volume of 0.150 mol dm-3 NaOH to neutralise 0.00500 mol ethanedioic acid.", ["img/2004-jan-chm6w/fig-q5-8-stem.jpg"]),

    # Page 7: Q7-9
    (7, 7, 80, 235, ["3.3.3", "3.3.10"], ["recall"], "Reaction that would not lead to the formation of ethanedioic acid.", ["img/2004-jan-chm6w/fig-q5-8-stem.jpg"]),
    (8, 7, 238, 425, ["3.3.10"], ["recall"], "Statement about ethanedioic acid that is not correct.", ["img/2004-jan-chm6w/fig-q5-8-stem.jpg"]),
    (9, 7, 430, 775, ["3.1.7"], ["recall"], "Identify the reaction that is a redox reaction.", []),

    # Page 8: Q10-11 (table context at y=80)
    (10, 8, 80, 505, ["3.1.11"], ["analysis"], "Identify the most powerful oxidising agent from standard electrode potential table.", []),
    (11, 8, 510, 775, ["3.1.11"], ["analysis"], "Statement that is not correct based on electrode potential values.", ["img/2004-jan-chm6w/fig-q10-11-stem.jpg"]),

    # Page 9: Q12-14 (context at y=80)
    (12, 9, 80, 345, ["3.1.2"], ["calculation"], "Concentration of Mg2+(aq) ions in saturated Mg(OH)2 solution.", []),
    (13, 9, 348, 530, ["3.1.12"], ["calculation"], "pH of saturated solution of magnesium hydroxide at 298 K.", ["img/2004-jan-chm6w/fig-q12-14-stem.jpg"]),
    (14, 9, 533, 775, ["3.1.12"], ["calculation"], "Value of solubility product Ksp for magnesium hydroxide.", ["img/2004-jan-chm6w/fig-q12-14-stem.jpg"]),

    # Page 10: Q15-16
    (15, 10, 80, 260, ["3.1.2"], ["calculation"], "Minimum mass of bauxite ore (55% Al2O3) needed to produce 1.0 tonne aluminium.", []),
    (16, 10, 265, 775, ["3.3.3", "3.3.6"], ["recall"], "True statement about properties or reactions of halogenoalkanes.", []),

    # Page 11: Q17-18 (context at y=80)
    (17, 11, 80, 500, ["3.3.4", "3.3.9"], ["recall"], "Set of reagents not suitable for indicated step in methyl methacrylate preparation.", []),
    (18, 11, 505, 775, ["3.3.4", "3.3.10"], ["recall"], "True statement about compounds and polymers in reaction scheme.", ["img/2004-jan-chm6w/fig-q17-18-stem.jpg"]),

    # Page 12: Q19
    (19, 12, 80, 775, ["3.3.12"], ["recall"], "True statement regarding Terylene polyester.", []),

    # Page 13: Q20-22 (context at y=80)
    (20, 13, 80, 410, ["3.3.10", "3.3.11"], ["recall"], "Species not involved in phenylamine synthesis sequence.", []),
    (21, 13, 412, 575, ["3.3.10"], ["recall"], "Mechanism of reaction step converting benzene to nitrobenzene.", ["img/2004-jan-chm6w/fig-q20-22-stem.jpg"]),
    (22, 13, 578, 775, ["3.3.11"], ["recall"], "Relative basicity of phenylamine compared to ammonia and ethylamine.", ["img/2004-jan-chm6w/fig-q20-22-stem.jpg"]),

    # Page 14: Q23-24
    (23, 14, 80, 310, ["3.3.1", "3.3.9"], ["analysis"], "Observation that does not support identity of unknown carbonyl compound.", []),
    (24, 14, 312, 775, ["3.1.9"], ["analysis"], "Rate equation and mechanism consistency for multi-step reaction.", []),

    # Page 15: Q25-27 (Section 2 Multiple completion)
    (25, 15, 245, 410, ["3.1.8"], ["recall"], "Reactions with a positive value for entropy change Delta S.", []),
    (26, 15, 412, 565, ["3.1.1"], ["recall"], "True statements about atomic structure, ionisation energies and isotopes.", []),
    (27, 15, 568, 775, ["3.1.7"], ["recall"], "Identify which of the given reactions are redox reactions.", []),

    # Page 16: Q28-29
    (28, 16, 175, 410, ["3.2.4", "3.1.7"], ["recall"], "True statements about the industrial extraction of titanium.", []),
    (29, 16, 412, 775, ["3.2.1"], ["recall"], "True statements about trends in Period 3 elements.", []),

    # Page 17: Q30-32 (context at y=175)
    (30, 17, 175, 535, ["3.2.5"], ["recall"], "True statements about chromium complex ions and colours.", []),
    (31, 17, 538, 675, ["3.2.5"], ["recall"], "Properties and reactions of chromium species in reaction scheme.", ["img/2004-jan-chm6w/fig-q30-32-stem.jpg"]),
    (32, 17, 678, 800, ["3.2.5"], ["recall"], "Correct equations for ligand substitution/redox steps of chromium complexes.", ["img/2004-jan-chm6w/fig-q30-32-stem.jpg"]),

    # Page 18: Q33-35
    (33, 18, 175, 335, ["3.2.5"], ["recall"], "Correct statements about [Co(en)3]3+ complex ion.", []),
    (34, 18, 338, 515, ["3.3.1", "3.3.7"], ["recall"], "Correct statements about structure and optical activity of 2-methylbutanal.", []),
    (35, 18, 518, 775, ["3.3.10"], ["recall"], "Correct statements about aspirin and ester hydrolysis.", []),

    # Page 19: Q36-37 (context at y=175)
    (36, 19, 175, 590, ["3.1.7", "3.3.9"], ["recall"], "Conversions that are reductions in reaction sequence.", []),
    (37, 19, 593, 775, ["3.3.9", "3.3.10"], ["recall"], "Correct statements about organic intermediates in reaction sequence.", ["img/2004-jan-chm6w/fig-q36-37-stem.jpg"]),

    # Page 20: Q38-39
    (38, 20, 175, 330, ["3.3.1"], ["recall"], "Correct statements about isomerism in non-cyclic compounds.", []),
    (39, 20, 332, 775, ["3.3.3", "3.3.6"], ["recall"], "Types of reaction that the given multi-functional molecule can undergo.", []),

    # Page 21: Q40
    (40, 21, 175, 775, ["3.1.3"], ["recall"], "Atoms around which the bonds are arranged tetrahedrally.", [])
]

STEM_CROPS = [
    ("fig-q1-3-stem.jpg", 5, 150, 305),
    ("fig-q5-8-stem.jpg", 6, 305, 375),
    ("fig-q10-11-stem.jpg", 8, 80, 350),
    ("fig-q12-14-stem.jpg", 9, 80, 180),
    ("fig-q17-18-stem.jpg", 11, 80, 350),
    ("fig-q20-22-stem.jpg", 13, 80, 250),
    ("fig-q30-32-stem.jpg", 17, 175, 395),
    ("fig-q36-37-stem.jpg", 19, 175, 435),
]

def main():
    print("Opening Question Paper PDF...")
    doc = fitz.open(QP_PATH)

    # 1. Crop stems
    for fname, p_num, y0, y1 in STEM_CROPS:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        out_path = os.path.join(IMG_DIR, fname)
        im.save(out_path, format="JPEG", quality=92)
        print(f"Saved stem figure: {fname}")

    # 2. Load questions.json
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Ensure paper entry exists
    if not any(p["id"] == PAPER_INFO["id"] for p in db.get("papers", [])):
        db.setdefault("papers", []).append(PAPER_INFO)

    existing_ids = {q["id"] for q in db["questions"]}
    added = 0

    for q_num, p_num, y0, y1, spec_topics, skills, prompt, figs in QUESTIONS:
        qid = f"2004-jan-chm6w-q{q_num}"
        q_label = str(q_num)
        ans_letter = KEYS[q_num]

        # Crop question image
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-jan-chm6w/q_q{q_num}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        # Render official mark scheme table
        ms_img_rel = f"img/2004-jan-chm6w/ms_q{q_num}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        render_official_markscheme_image(
            q_label,
            f"<b>{ans_letter}</b> (1)",
            "Multiple choice key",
            1,
            spec_topics[0] if spec_topics else "Synoptic",
            ms_img_abs
        )

        q_obj = {
            "id": qid,
            "paper": "2004-jan-chm6w",
            "year": 2004,
            "series": "January",
            "code": "CHM6/W",
            "unit": "Unit 6(a): Synoptic Paper",
            "question": q_label,
            "page": p_num,
            "marks": 1,
            "topics": spec_topics,
            "skills": skills,
            "description": prompt,
            "image": q_img_rel,
            "markscheme": ms_img_rel
        }
        if figs:
            q_obj["figures"] = figs

        if qid not in existing_ids:
            db["questions"].append(q_obj)
            existing_ids.add(qid)
            added += 1
        else:
            for idx, item in enumerate(db["questions"]):
                if item["id"] == qid:
                    db["questions"][idx] = q_obj
                    break

    print(f"Ingested {len(QUESTIONS)} questions for 2004-jan-chm6w ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

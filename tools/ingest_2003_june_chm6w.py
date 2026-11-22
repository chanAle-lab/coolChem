"""
Ingestion script for 2003 June CHM6/W (Synoptic Unit 6a)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023400_9dd73bd6.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-june-chm6w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-june-chm6w",
    "year": 2003,
    "series": "June",
    "date": "2003-06-18",
    "code": "CHM6/W",
    "unit": "Unit 6(a): Synoptic Paper",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 40,
    "duration": "1 hour"
}

# (qid, q_label, page, y0, y1, mark, spec_topics, skills, prompt_summary, answer_letter)
QUESTIONS = [
    # Page 4: Q1-3 (context at y=150)
    ("2003-june-chm6w-q1", "1", 4, 150, 385, 1, ["3.1.6"], ["recall"], "Increase equilibrium yield of ethanoic acid from methyl ethanoate hydrolysis.", "C"),
    ("2003-june-chm6w-q2", "2", 4, 388, 565, 1, ["3.1.6"], ["calculation"], "Value of Kc at 298K from 3mol ester and 3mol water giving 2mol ethanoic acid.", "D"),
    ("2003-june-chm6w-q3", "3", 4, 568, 735, 1, ["3.1.3", "3.3.1"], ["recall"], "Compound from reaction mixture with no hydrogen bonds between pure molecules.", "A"),

    # Page 5: Q4-6 (context at y=150)
    ("2003-june-chm6w-q4", "4", 5, 150, 395, 1, ["3.1.4"], ["calculation"], "Standard enthalpy of formation of steam from Fe2O3 and H2 table data.", "C"),
    ("2003-june-chm6w-q5", "5", 5, 398, 550, 1, ["3.1.8"], ["recall"], "Standard entropy value for steam.", "B"),
    ("2003-june-chm6w-q6", "6", 5, 553, 775, 1, ["3.1.1"], ["recall"], "True statement about 58Ni2+ and 60Ni2+ isotopes.", "D"),

    # Page 6: Q7-10
    ("2003-june-chm6w-q7", "7", 6, 75, 245, 1, ["3.2.4", "3.1.3"], ["recall"], "True statement about carbon monoxide.", "A"),
    ("2003-june-chm6w-q8", "8", 6, 248, 402, 1, ["3.1.7"], ["recall"], "Identify reaction that is not a redox reaction.", "C"),
    ("2003-june-chm6w-q9", "9", 6, 405, 558, 1, ["3.2.5"], ["recall"], "Species that could not act as a ligand.", "B"),
    ("2003-june-chm6w-q10", "10", 6, 560, 775, 1, ["3.1.7"], ["recall"], "Reaction in which H2O2 behaves as a reducing agent.", "C"),

    # Page 7: Q11-14
    ("2003-june-chm6w-q11", "11", 7, 75, 235, 1, ["3.1.8"], ["recall"], "Reaction resulting in a decrease in entropy of the system.", "C"),
    ("2003-june-chm6w-q12", "12", 7, 238, 428, 1, ["3.2.6"], ["recall"], "Identify green precipitate turning brown on standing with NaOH.", "B"),
    ("2003-june-chm6w-q13", "13", 7, 430, 650, 1, ["3.2.5"], ["recall"], "Complex ion with tetrahedral shape and total charge +2.", "D"),
    ("2003-june-chm6w-q14", "14", 7, 652, 775, 1, ["3.1.7", "3.2.4"], ["recall"], "Substance that will not reduce acidified potassium dichromate(VI).", "A"),

    # Page 8: Q15-17 (context at y=75)
    ("2003-june-chm6w-q15", "15", 8, 75, 440, 1, ["3.3.10"], ["recall"], "Reagents and conditions for converting butan-1-ol into butyl propanoate.", "B"),
    ("2003-june-chm6w-q16", "16", 8, 443, 595, 1, ["3.3.16"], ["analysis"], "Infra-red absorption wavenumbers not present in butyl propanoate.", "B"),
    ("2003-june-chm6w-q17", "17", 8, 598, 775, 1, ["3.3.10"], ["calculation"], "Percentage yield of butyl propanoate from 0.050 mol butan-1-ol.", "C"),

    # Page 9: Q18-20 (context at y=75)
    ("2003-june-chm6w-q18", "18", 9, 75, 248, 1, ["3.1.9"], ["analysis"], "Rate equation consistent with data from benzene sulphonation.", "D"),
    ("2003-june-chm6w-q19", "19", 9, 250, 418, 1, ["3.1.9"], ["analysis"], "Effect on rate when concentration of benzenesulphonic acid is doubled.", "C"),
    ("2003-june-chm6w-q20", "20", 9, 420, 775, 1, ["3.3.11", "3.1.12"], ["recall"], "Statement about amine basicity that is not true.", "C"),

    # Page 10: Q21-22 (Section 2 begins)
    ("2003-june-chm6w-q21", "21", 10, 415, 575, 1, ["3.1.3"], ["recall"], "True statements about lattice enthalpy and bonding in MgO vs NaCl.", "B"),
    ("2003-june-chm6w-q22", "22", 10, 578, 775, 1, ["3.1.2"], ["calculation"], "True statements about reacting masses and volumes of gases.", "C"),

    # Page 11: Q23-24
    ("2003-june-chm6w-q23", "23", 11, 160, 395, 1, ["3.1.11"], ["analysis"], "True statements concerning Pt|H2|H+||Cu2+|Cu electrochemical cell.", "A"),
    ("2003-june-chm6w-q24", "24", 11, 398, 775, 1, ["3.1.7"], ["recall"], "Processes that do not involve a redox reaction.", "C"),

    # Page 12: Q25-26
    ("2003-june-chm6w-q25", "25", 12, 160, 510, 1, ["3.1.11"], ["analysis"], "True statements deduced from electrode potential values.", "B"),
    ("2003-june-chm6w-q26", "26", 12, 513, 775, 1, ["3.1.3"], ["recall"], "Species that boron trifluoride BF3 can form a co-ordinate bond with.", "C"),

    # Page 13: Q27-28
    ("2003-june-chm6w-q27", "27", 13, 425, 600, 1, ["3.1.4"], ["recall"], "Enthalpy changes representing formation, ionisation and atomisation.", "D"),
    ("2003-june-chm6w-q28", "28", 13, 603, 775, 1, ["3.1.8"], ["recall"], "Entropy and lattice enthalpy factors in Born-Haber cycle for NaCl.", "C"),

    # Page 14: Q29-30
    ("2003-june-chm6w-q29", "29", 14, 160, 328, 1, ["3.1.7"], ["recall"], "Reaction where indicated element increases its oxidation state.", "C"),
    ("2003-june-chm6w-q30", "30", 14, 330, 775, 1, ["3.2.4"], ["recall"], "Correct statements about phosphorus and silicon chemistry.", "A"),

    # Page 15: Q31-33
    ("2003-june-chm6w-q31", "31", 15, 280, 432, 1, ["3.2.5"], ["recall"], "Species with only two unpaired electrons in 3d sub-level.", "C"),
    ("2003-june-chm6w-q32", "32", 15, 435, 588, 1, ["3.2.5"], ["recall"], "Transition metal ions with maximum oxidation state of +6.", "B"),
    ("2003-june-chm6w-q33", "33", 15, 590, 775, 1, ["3.2.5"], ["recall"], "True statements about bidentate ligand 1,2-diaminoethane.", "A"),

    # Page 16: Q34
    ("2003-june-chm6w-q34", "34", 16, 160, 775, 1, ["3.3.11", "3.3.12"], ["analysis"], "Functional groups and features present in Viagra structure.", "B"),

    # Page 17: Q35-36 (reaction scheme at y=150)
    ("2003-june-chm6w-q35", "35", 17, 150, 600, 1, ["3.3.3", "3.3.4"], ["recall"], "Reaction types involved in multi-step organic sequence.", "A"),
    ("2003-june-chm6w-q36", "36", 17, 603, 775, 1, ["3.3.3", "3.3.4"], ["recall"], "Reaction mechanisms involved in multi-step organic sequence.", "A"),

    # Page 18: Q37-39
    ("2003-june-chm6w-q37", "37", 18, 160, 432, 1, ["3.3.1", "3.3.3"], ["recall"], "Distinguishing tests for four pairs of organic reagents.", "B"),
    ("2003-june-chm6w-q38", "38", 18, 435, 588, 1, ["3.3.11", "3.3.12"], ["recall"], "Correct statements about aliphatic and aromatic nitriles.", "A"),
    ("2003-june-chm6w-q39", "39", 18, 590, 775, 1, ["3.3.9", "3.3.3"], ["recall"], "Reactions and stereoisomerism of pent-2-enoic acid.", "C"),

    # Page 19: Q40
    ("2003-june-chm6w-q40", "40", 19, 160, 775, 1, ["3.3.1", "3.3.3"], ["analysis"], "Reactions of organolithium compound LiCH3 as base and nucleophile.", "B")
]

def main():
    doc = fitz.open(QP_PATH)
    
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    existing_ids = {q["id"] for q in db["questions"]}
    added = 0
    
    for qid, q_label, p_num, y0, y1, mark, spec_topics, skills, prompt, answer_letter in QUESTIONS:
        # 1. Render Question Image
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        
        q_img_rel = f"img/2003-june-chm6w/q_q{q_label}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)
        
        # 2. Render Official Mark Scheme Image
        ms_img_rel = f"img/2003-june-chm6w/ms_q{q_label}.jpg"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        
        ms_html = f"<b>{answer_letter}</b>"
        ms_extra = "(1 mark)"
        render_official_markscheme_image(q_label, ms_html, ms_extra, mark, "AO1", ms_img_abs)
        
        # 3. Add to questions.json
        q_obj = {
            "id": qid,
            "paper": "2003-june-chm6w",
            "year": 2003,
            "series": "June",
            "code": "CHM6/W",
            "unit": "Unit 6(a): Synoptic Paper",
            "question": q_label,
            "page": p_num,
            "marks": mark,
            "topics": spec_topics,
            "skills": skills,
            "description": prompt,
            "image": q_img_rel,
            "markscheme": ms_img_rel,
            "markscheme_text": answer_letter,
            "answer_key": answer_letter
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
                    
    print(f"Ingested {len(QUESTIONS)} questions for 2003-june-chm6w ({added} newly added).")
    
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Successfully saved questions.json!")

if __name__ == "__main__":
    main()

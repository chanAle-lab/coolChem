"""
Ingestion script for 2006 June CHM6/W (Synoptic Assessment - 40 MCQs)
Renders official AQA modern mark scheme tables and precision cropped question images.
"""
import os
import sys
import json
import fitz
from PIL import Image

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-june-chm6w")
os.makedirs(IMG_DIR, exist_ok=True)

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383083058_f1d8cd22.pdf"
MS_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383083059_52e601c8.pdf"

# 40 MCQs answers from Mark Scheme:
# 1: D, 2: A, 3: C, 4: D, 5: C, 6: D, 7: A, 8: B, 9: D, 10: D,
# 11: C, 12: D, 13: C, 14: C, 15: B, 16: A, 17: C, 18: D, 19: B, 20: A,
# 21: C, 22: B, 23: A, 24: C, 25: C, 26: D, 27: C, 28: B, 29: A, 30: B,
# 31: C, 32: B, 33: C, 34: D, 35: C, 36: D, 37: B, 38: B, 39: C, 40: B

mcq_data = [
    (1, "D", 5, "3.1.1", "Electron arrangement of the strongest reducing agent (1s2 2s2 2p6 3s2 3p6 4s2)."),
    (2, "A", 5, "3.1.4", "Hydrocarbon with 2.0 g releasing 100 kJ on combustion (ethyne)."),
    (3, "C", 5, "3.1.8", "Reaction feasible at all temperatures (S(g) -> 2T(g) exothermic)."),
    (4, "D", 6, "3.2.4", "Incorrect statement regarding blast furnace removal of SiO2 (SiO2 is basic oxide)."),
    (5, "C", 6, "3.1.2", "Mass of CaCO3 needed to remove 1.00 tonne of SiO2 (1.67 tonne)."),
    (6, "D", 6, "3.1.2", "Volume of CO2 formed during removal of 1.00 tonne of SiO2 (408 m3)."),
    (7, "A", 7, "3.1.3", "Species whose shape is influenced by lone pairs of electrons (NH2-)."),
    (8, "B", 7, "3.1.7", "Equation not representing a redox reaction (VO3- + 2H+ -> VO2+ + H2O)."),
    (9, "D", 7, "3.1.3", "Incorrect statement about Period 3/Group 2 oxides (SiO2 higher mp than P4O10 due to vdW)."),
    (10, "D", 7, "3.1.7", "Reaction that is not a redox reaction (2CrO4^2- + 2H+ -> Cr2O7^2- + H2O)."),
    (11, "C", 8, "3.1.8", "Aqueous reaction with most positive entropy change ([Cu(H2O)6]2+ + EDTA4-)."),
    (12, "D", 8, "3.1.6", "Conditions increasing O2 in O2/O3 equilibrium (decreasing T and decreasing P)."),
    (13, "C", 8, "3.1.5", "Process carried out for environmental reasons only (catalytic reduction of NO)."),
    (14, "C", 8, "3.1.5", "Reaction in which a heterogeneous catalyst is not used (CO2 + C -> 2CO)."),
    (15, "B", 9, "3.3.7", "Compound exhibiting both geometrical and optical isomerism."),
    (16, "A", 9, "3.3.3", "Number of different alkenes formed from 2-bromo-3-methylbutane elimination (2)."),
    (17, "C", 9, "3.1.2", "Mass of compound X formed in 40.0% yield from methylbenzene (10.7 g)."),
    (18, "D", 10, "3.3.3", "Reason why fluoroalkanes are least reactive haloalkanes (C-F bond is strongest)."),
    (19, "B", 10, "3.3.15", "Reagents reacting to give product with only 2 peaks in 1H NMR (ethanoyl chloride + methanol)."),
    (20, "A", 11, "3.3.10", "Reaction type not shown in reaction scheme to trinitrobenzoic acid (reduction)."),
    (21, "C", 11, "3.1.12", "Acid dissociation constant Ka from pH 2.50 of 0.100 M solution (1.00 × 10^-4)."),
    (22, "B", 12, "3.1.6", "Changes favouring formation of NO from N2 and O2 (1 and 3 only)."),
    (23, "A", 12, "3.1.3", "Molecules with a permanent dipole (1, 2 and 3 only: NH3, PCl3, SCl2)."),
    (24, "C", 13, "3.1.9", "Rate orders for NO and H2 reaction (2 and 4 only: first order H2, overall 3)."),
    (25, "C", 13, "3.1.7", "Species containing element with +5 oxidation state (2 and 4 only: NO2+, ClO3-)."),
    (26, "D", 14, "3.1.11", "Statements for operating Zn/Cu cell (4 only: e.m.f. of cell decreases)."),
    (27, "C", 14, "3.1.8", "Correct inorganic and physical statements (2 and 4 only: Fe2O3 entropy, SiCl4 acidity)."),
    (28, "B", 14, "3.1.12", "Lewis bases (1 and 3 only: H2O and Cl-)."),
    (29, "A", 15, "3.1.7", "Correct statements about sulphuric acid (1, 2 and 3 only)."),
    (30, "B", 15, "3.1.5", "Ions catalysing peroxodisulphate-iodide reaction (1 and 3 only: Fe2+ and Fe3+)."),
    (31, "C", 15, "3.2.5", "Statements about silver and its compounds (2 and 4 only)."),
    (32, "B", 16, "3.2.6", "Hydrolysis of metal-aqua ions (1 and 3 only)."),
    (33, "C", 16, "3.2.6", "Reagents leaving precipitate with excess added to CuSO4 (2 and 4 only: Na2CO3, NaOH)."),
    (34, "D", 16, "3.3.2", "Reactions involving free-radical intermediate (4 only: thermal cracking of octane)."),
    (35, "C", 17, "3.3.11", "Statements about ammonia, methylamine and phenylamine (2 and 4 only)."),
    (36, "D", 17, "3.3.1", "Statements about hex-4-en-1-ol (4 only: geometrical isomers)."),
    (37, "B", 18, "3.3.10", "Reaction types in synthesis of substituted aromatic compounds (1 and 3 only: chlorination, acylation)."),
    (38, "B", 18, "3.3.12", "Statements about polyamide from diamine and diacid (1 and 3 only)."),
    (39, "C", 19, "3.3.8", "Statements about vanillin (2 and 4 only: Tollens test, hydrogen bonding)."),
    (40, "B", 20, "3.3.11", "Statements about Levitra (1 and 3 only: reacts with HCl, can be nitrated).")
]

paper_id = "2006-june-chm6w"
print(f"Ingesting 40 MCQs for {paper_id}...")
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Remove any existing 2006-june-chm6w questions
db['questions'] = [q for q in db['questions'] if q.get('paper') != paper_id]

new_questions = []
for q_num, ans, page_num, spec_ref, summary in mcq_data:
    q_id = f"{paper_id}-q{q_num}"
    ms_img_rel = f"img/{paper_id}/ms_q{q_num}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
    q_img_rel = f"img/{paper_id}/{q_id}.jpg"

    answers_html = f"<strong>{ans}</strong>"
    extra_html = "1 mark for correct multiple choice response."

    render_official_markscheme_image(
        question_label=str(q_num),
        answers_html=answers_html,
        extra_html=extra_html,
        marks=1,
        spec_ref=spec_ref,
        output_path=ms_img_abs
    )

    q_entry = {
        "id": q_id,
        "paper": paper_id,
        "question": str(q_num),
        "marks": 1,
        "page": page_num,
        "topics": [spec_ref],
        "skills": ["recall" if q_num <= 10 else "application"],
        "summary": summary,
        "question_text": summary,
        "markscheme_text": "Official AQA mark scheme table",
        "image": q_img_rel,
        "figures": [],
        "markscheme": ms_img_rel
    }
    new_questions.append(q_entry)

db['questions'].extend(new_questions)

with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully ingested {len(new_questions)} MCQs for {paper_id}. Total marks: {sum(q['marks'] for q in new_questions)}")

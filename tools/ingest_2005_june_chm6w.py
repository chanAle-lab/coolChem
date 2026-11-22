import os
import sys
import json
import fitz
from PIL import Image

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-june-chm6w")
os.makedirs(IMG_DIR, exist_ok=True)

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003756_890ad502.pdf"
MS_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003746_63100a17.pdf"

# 40 MCQs answers from Mark Scheme:
# 1: C, 2: B, 3: D, 4: C, 5: C, 6: A, 7: B, 8: B, 9: D, 10: D,
# 11: D, 12: B, 13: D, 14: B, 15: A, 16: C, 17: D, 18: D, 19: B, 20: D,
# 21: C, 22: D, 23: B, 24: B, 25: B, 26: C, 27: B, 28: C, 29: B, 30: C,
# 31: A, 32: B, 33: A, 34: C, 35: C, 36: A, 37: A, 38: A, 39: C, 40: C

mcq_data = [
    (1, "C", 5, "3.1.4", "Enthalpy of combustion of propane."),
    (2, "B", 5, "3.2.2", "Electronegativity trend in Group 2 elements."),
    (3, "D", 5, "3.1.1", "Mass spectrum peaks of bromoethane isotopes."),
    (4, "C", 6, "3.1.12", "pH comparison of ester equilibrium mixtures F and G."),
    (5, "C", 6, "3.1.10", "Equilibrium constant Kc for propanoic acid esterification."),
    (6, "A", 6, "3.1.7", "Redox identification in hydrogen iodide equilibrium."),
    (7, "B", 7, "3.1.2", "Concentration of ethanedioic acid from KOH titration."),
    (8, "B", 7, "3.1.3", "Non-planar geometry of nitrogen trichloride (NCl3)."),
    (9, "D", 7, "3.2.3", "Bonding and structure of aluminium chloride."),
    (10, "D", 7, "3.1.3", "Reaction not involving donation of an electron pair."),
    (11, "D", 8, "3.1.1", "Correct electron arrangement of Cu+ ([Ar]3d10)."),
    (12, "B", 8, "3.1.7", "Cu+ acting as reducing agent in photochromic glass."),
    (13, "D", 9, "3.1.2", "Maximum mass of silver obtained from Ag2O reduction."),
    (14, "B", 9, "3.3.3", "Double bond determining the cis prefix in cis-retinal."),
    (15, "A", 10, "3.3.5", "Number of alkenes formed from 2-bromo-2-methylbutane elimination."),
    (16, "C", 10, "3.3.1", "Pair of functional group isomers (methoxyethane and propan-2-ol)."),
    (17, "D", 10, "3.3.10", "Incorrect statement about vitamin C structure."),
    (18, "D", 11, "3.3.7", "Reaction producing organic compound with optical isomers."),
    (19, "B", 11, "3.1.2", "Mass of TNT formed in 27.0% yield reaction."),
    (20, "D", 11, "3.3.15", "Reaction yielding product with only two singlets in 1H NMR."),
    (21, "C", 12, "3.1.8", "Reactions with positive entropy change (2 and 4 only)."),
    (22, "D", 12, "3.1.8", "Enthalpy not involved in Born-Haber cycle for CaH2 (4 only)."),
    (23, "B", 13, "3.2.5", "Pairs representing stereoisomers (1 and 3 only)."),
    (24, "B", 14, "3.1.11", "Statements regarding peroxodisulphate-iodide redox (1 and 3 only)."),
    (25, "B", 14, "3.2.5", "Catalysis and electron configuration of Fe3+ (1 and 3 only)."),
    (26, "C", 15, "3.1.11", "Cell e.m.f. values for peroxodisulphate-iron reactions (2 and 4 only)."),
    (27, "B", 15, "3.1.3", "Molecules with a permanent overall dipole (1 and 3 only)."),
    (28, "C", 15, "3.1.7", "Reactions in which oxidation state increases (2 and 4 only)."),
    (29, "B", 15, "3.2.4", "Substances releasing CO2 with sodium carbonate (1 and 3 only)."),
    (30, "C", 16, "3.2.3", "Precipitate with AgNO3 in excess aqueous ammonia (2 and 4 only)."),
    (31, "A", 16, "3.3.5", "Reactions of concentrated sulphuric acid (1, 2 and 3 only)."),
    (32, "B", 16, "3.1.7", "Disproportionation reactions of the same species (1 and 3 only)."),
    (33, "A", 16, "3.2.5", "Species containing two or more co-ordinate bonds (1, 2 and 3 only)."),
    (34, "C", 17, "3.1.2", "Combustion requiring exactly 9 mol of O2 (2 and 4 only)."),
    (35, "C", 17, "3.1.3", "Liquids exhibiting hydrogen bonding (2 and 4 only)."),
    (36, "A", 17, "3.3.2", "Statements regarding ethyl carbocation (1, 2 and 3 only)."),
    (37, "A", 17, "3.3.15", "Spectroscopic features of methyl 4-oxopentanoate (1, 2 and 3 only)."),
    (38, "A", 18, "3.3.8", "Reactions and spectra of dihydroxyacetone (1, 2 and 3 only)."),
    (39, "C", 18, "3.3.8", "Correct mechanistic steps for organic reactions (2 and 4 only)."),
    (40, "C", 19, "3.3.9", "Properties and NMR of 2,2-dimethylpropanoic acid (2 and 4 only).")
]

print("Ingesting 40 MCQs for June 2005 CHM6/W...")
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Remove any existing 2005-june-chm6w questions
db['questions'] = [q for q in db['questions'] if q['paper'] != '2005-june-chm6w']

for q_num, ans, page_num, spec_ref, summary in mcq_data:
    q_id = f"2005-june-chm6w-q{q_num}"
    ms_img_rel = f"img/2005-june-chm6w/ms_q{q_num}.png"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
    q_img_rel = f"img/2005-june-chm6w/q_q{q_num}.jpg"

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
        "paper": "2005-june-chm6w",
        "question": str(q_num),
        "marks": 1,
        "summary": summary,
        "description": f"Multiple choice question {q_num}: {summary}",
        "topic": spec_ref,
        "tags": ["CHM6/W", "Synoptic", "MCQ", "AQA", "A-Level"],
        "page": page_num,
        "image": q_img_rel,
        "markscheme": ms_img_rel
    }
    db['questions'].append(q_entry)
    print(f"Processed MCQ {q_num} -> Answer {ans}")

with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully ingested 40 MCQs for 2005-june-chm6w!")

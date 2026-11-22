"""
Ingestion script for 2005 January CHM6/W Synoptic Assessment (40 MCQs)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382904766_6115b880.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-jan-chm6w")
os.makedirs(IMG_DIR, exist_ok=True)

# Official Mark Scheme Keys from Page 4:
KEYS = {
    1: 'B', 2: 'B', 3: 'A', 4: 'B', 5: 'A',
    6: 'D', 7: 'C', 8: 'C', 9: 'A', 10: 'B',
    11: 'B', 12: 'D', 13: 'A', 14: 'C', 15: 'C',
    16: 'D', 17: 'C', 18: 'A', 19: 'C', 20: 'B',
    21: 'A', 22: 'C', 23: 'B', 24: 'A', 25: 'A',
    26: 'C', 27: 'C', 28: 'B', 29: 'A', 30: 'A',
    31: 'C', 32: 'B', 33: 'C', 34: 'A', 35: 'B',
    36: 'C', 37: 'C', 38: 'A', 39: 'B', 40: 'A'
}

PAGES = {
    1: 5, 2: 5,
    3: 6, 4: 6, 5: 6,
    6: 7, 7: 7,
    8: 8, 9: 8, 10: 8,
    11: 9, 12: 9,
    13: 10, 14: 10, 15: 10, 16: 10,
    17: 11, 18: 11, 19: 11,
    20: 12,
    21: 13, 22: 13,
    23: 14, 24: 14, 25: 14,
    26: 15, 27: 15, 28: 15, 29: 15,
    30: 16, 31: 16, 32: 16, 33: 16,
    34: 17, 35: 17, 36: 17,
    37: 18, 38: 18,
    39: 19, 40: 19
}

SUMMARIES = {
    1: "Standard enthalpy change for reaction of CO with H2O.",
    2: "Incorrect statement regarding activation energy and temperature.",
    3: "Standard entropy change for reaction.",
    4: "Gas-phase reaction with Delta H and Delta S.",
    5: "Species with greatest bond angle.",
    6: "EMF of the cell Ag(s)|Ag+(aq)||Pb2+(aq)|Pb(s).",
    7: "Factor that increases EMF of Pt(s)|H2|H+||Ag+|Ag cell.",
    8: "Enthalpy of hydration / lattice enthalpy comparison.",
    9: "Compound that forms precipitate with AgNO3 and dissolves in dilute NH3.",
    10: "Oxidation state of metal in complex ion.",
    11: "Identification of organic product formed by elimination.",
    12: "Reagent used to distinguish pair of organic compounds.",
    13: "Order of reaction with respect to reactants.",
    14: "Deduction from rate equation data.",
    15: "Structure of monomer forming given condensation polymer.",
    16: "Number of peaks in 13C NMR spectrum.",
    17: "Incorrect statement about reaction scheme for polymer P.",
    18: "Percentage yield of intermediate J from benzene.",
    19: "pH calculation for weak acid K.",
    20: "Volume of diamine required to neutralise dicarboxylic acid.",
    21: "Correct statements regarding thermodynamics of methanol synthesis.",
    22: "Conditions that increase yield of exothermic methanol synthesis.",
    23: "Species that act as nucleophiles.",
    24: "Reactions that produce a gas.",
    25: "Compounds that exhibit stereoisomerism.",
    26: "Solutions with pH greater than 7.",
    27: "Species with tetrahedral geometry.",
    28: "Properties of period 3 elements and oxides.",
    29: "Pairs of reagents that react to form an ester.",
    30: "Molecules that can form hydrogen bonds with water.",
    31: "Reactions that involve oxidation.",
    32: "Compounds that decolourise bromine water.",
    33: "Transition metal complexes and colours.",
    34: "Equilibrium position shift upon temperature/pressure change.",
    35: "Buffer solution components and characteristics.",
    36: "Methods of separating mixtures.",
    37: "Intermolecular forces in organic liquids.",
    38: "Identification of isomers with formula C4H8.",
    39: "Types of mechanism shown in terpene reactions.",
    40: "Properties and reactions of terpene compound X."
}

def extract_figures(doc):
    # 1. Directions summarised table (page 13)
    p13 = doc[12]
    rect_dir = fitz.Rect(45, 140, 545, 235)
    pix_dir = p13.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect_dir)
    im_dir = Image.frombytes("RGB", [pix_dir.width, pix_dir.height], pix_dir.samples)
    im_dir.save(os.path.join(IMG_DIR, "fig-mcq-directions.jpg"), format="JPEG", quality=92)
    print("Saved fig-mcq-directions.jpg")

    # 2. Q1-2 stem (page 5)
    p5 = doc[4]
    rect1_2 = fitz.Rect(45, 155, 545, 335)
    pix1_2 = p5.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect1_2)
    im1_2 = Image.frombytes("RGB", [pix1_2.width, pix1_2.height], pix1_2.samples)
    im1_2.save(os.path.join(IMG_DIR, "fig-q1-2-stem.jpg"), format="JPEG", quality=92)
    print("Saved fig-q1-2-stem.jpg")

    # 3. Q6-7 stem (page 7)
    p7 = doc[6]
    rect6_7 = fitz.Rect(45, 85, 545, 235)
    pix6_7 = p7.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect6_7)
    im6_7 = Image.frombytes("RGB", [pix6_7.width, pix6_7.height], pix6_7.samples)
    im6_7.save(os.path.join(IMG_DIR, "fig-q6-7-stem.jpg"), format="JPEG", quality=92)
    print("Saved fig-q6-7-stem.jpg")

    # 4. Q17-20 stem (page 11)
    p11 = doc[10]
    rect17_20 = fitz.Rect(45, 85, 545, 335)
    pix17_20 = p11.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect17_20)
    im17_20 = Image.frombytes("RGB", [pix17_20.width, pix17_20.height], pix17_20.samples)
    im17_20.save(os.path.join(IMG_DIR, "fig-q17-20-stem.jpg"), format="JPEG", quality=92)
    print("Saved fig-q17-20-stem.jpg")

    # 5. Q21-22 stem (page 13)
    rect21_22 = fitz.Rect(45, 255, 545, 455)
    pix21_22 = p13.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect21_22)
    im21_22 = Image.frombytes("RGB", [pix21_22.width, pix21_22.height], pix21_22.samples)
    im21_22.save(os.path.join(IMG_DIR, "fig-q21-22-stem.jpg"), format="JPEG", quality=92)
    print("Saved fig-q21-22-stem.jpg")

    # 6. Q39-40 stem (page 19)
    p19 = doc[18]
    rect39_40 = fitz.Rect(45, 175, 545, 440)
    pix39_40 = p19.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect39_40)
    im39_40 = Image.frombytes("RGB", [pix39_40.width, pix39_40.height], pix39_40.samples)
    im39_40.save(os.path.join(IMG_DIR, "fig-q39-40-stem.jpg"), format="JPEG", quality=92)
    print("Saved fig-q39-40-stem.jpg")

def main():
    print("Opening Question Paper PDF...")
    doc_qp = fitz.open(QP_PATH)
    extract_figures(doc_qp)

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Remove existing
    db["questions"] = [q for q in db["questions"] if q.get("paper") != "2005-jan-chm6w"]

    for q_num in range(1, 41):
        key = KEYS[q_num]
        p_num = PAGES[q_num]
        qid = f"2005-jan-chm6w-q{q_num}"
        q_label = str(q_num)
        summary = SUMMARIES[q_num]

        figs = []
        if q_num in [1, 2]:
            figs.append("img/2005-jan-chm6w/fig-q1-2-stem.jpg")
        elif q_num in [6, 7]:
            figs.append("img/2005-jan-chm6w/fig-q6-7-stem.jpg")
        elif q_num in [17, 18, 19, 20]:
            figs.append("img/2005-jan-chm6w/fig-q17-20-stem.jpg")
        elif q_num in [21, 22]:
            figs.append("img/2005-jan-chm6w/fig-q21-22-stem.jpg")
        elif q_num in [39, 40]:
            figs.append("img/2005-jan-chm6w/fig-q39-40-stem.jpg")

        if q_num >= 21:
            figs.append("img/2005-jan-chm6w/fig-mcq-directions.jpg")

        ms_img_rel = f"img/2005-jan-chm6w/ms_q{q_num}.jpg"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

        answers_html = f"<strong>{key}</strong>"
        if q_num >= 21:
            code_desc = {
                'A': '1, 2 and 3 only are correct',
                'B': '1 and 3 only are correct',
                'C': '2 and 4 only are correct',
                'D': '4 only is correct'
            }.get(key, '')
            extra_html = f"Multiple completion: {code_desc}"
        else:
            extra_html = f"Standard 4-choice MCQ"

        render_official_markscheme_image(
            question_label=q_label,
            answers_html=answers_html,
            extra_html=extra_html,
            marks=1,
            spec_ref="AO1 / Synoptic",
            output_path=ms_img_abs
        )

        entry = {
            "id": qid,
            "paper": "2005-jan-chm6w",
            "question": q_label,
            "marks": 1,
            "page": p_num,
            "topics": ["3.1" if q_num <= 10 else ("3.2" if q_num <= 25 else "3.3")],
            "skills": ["recall", "analysis"],
            "summary": summary,
            "image": f"img/2005-jan-chm6w/q_{q_num}.jpg",
            "figures": figs,
            "markscheme": ms_img_rel,
            "markscheme_text": f"Question {q_num}: {key} (1 mark)"
        }
        db["questions"].append(entry)
        print(f"Processed {qid} - Key: {key}")

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully ingested 40 questions for 2005-jan-chm6w!")

if __name__ == "__main__":
    main()

"""
Ingestion script for 2005 January CHM1 (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382849471_29d4088b.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-jan-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-jan-chm1",
    "year": 2005,
    "series": "January",
    "date": "2005-01-11",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2005-jan-chm1-q1ai", "1(a)(i)", 2, 80, 200, 1, ["3.1.1"], ["recall"], "Define the term mass number of an atom."),
    ("2005-jan-chm1-q1aii", "1(a)(ii)", 2, 205, 360, 2, ["3.1.2"], ["recall"], "Define the term relative molecular mass."),
    ("2005-jan-chm1-q1bi", "1(b)(i)", 2, 365, 450, 1, ["3.1.1"], ["recall"], "Complete the electron arrangement for a copper atom."),
    ("2005-jan-chm1-q1bii", "1(b)(ii)", 2, 455, 530, 1, ["3.1.1", "3.2.1"], ["recall"], "Identify the block in the Periodic Table to which copper belongs."),
    ("2005-jan-chm1-q1biii", "1(b)(iii)", 2, 535, 630, 1, ["3.1.1"], ["calculation"], "Deduce the number of neutrons in one atom of 65Cu."),

    # Page 5: Question 1(c)
    ("2005-jan-chm1-q1ci", "1(c)(i)", 5, 80, 210, 1, ["3.1.1"], ["explanation"], "Explain why the Ar of this copper sample is less than 64."),
    ("2005-jan-chm1-q1cii", "1(c)(ii)", 5, 215, 330, 2, ["3.1.1"], ["recall"], "Explain how Cu atoms are converted into Cu+ ions in a mass spectrometer."),
    ("2005-jan-chm1-q1ciii", "1(c)(iii)", 5, 335, 610, 3, ["3.1.1"], ["explanation"], "Identify ion responsible for peak at m/z = 31.5, explain m/z value and suggest reason why peak is small."),

    # Page 6: Question 2(a)
    ("2005-jan-chm1-q2ai", "2(a)(i)", 6, 80, 280, 1, ["3.1.2"], ["calculation"], "Calculate original moles of NaOH in 100 cm3 of 0.500 mol dm-3 aqueous NaOH."),
    ("2005-jan-chm1-q2aii", "2(a)(ii)", 6, 285, 385, 1, ["3.1.2"], ["calculation"], "Calculate moles of HCl in 27.3 cm3 of 0.600 mol dm-3 hydrochloric acid."),
    ("2005-jan-chm1-q2aiii", "2(a)(iii)", 6, 390, 480, 1, ["3.1.2"], ["calculation"], "Deduce moles of unreacted NaOH neutralised by hydrochloric acid."),
    ("2005-jan-chm1-q2aiv", "2(a)(iv)", 6, 485, 575, 1, ["3.1.2"], ["calculation"], "Calculate moles of NaOH which reacted with ammonium sulphate."),
    ("2005-jan-chm1-q2av", "2(a)(v)", 6, 580, 775, 3, ["3.1.2"], ["calculation"], "Calculate moles and mass of ammonium sulphate in sample."),

    # Page 7: Question 2(b)
    ("2005-jan-chm1-q2b", "2(b)", 7, 80, 460, 4, ["3.1.2"], ["calculation"], "State ideal gas equation, calculate moles of ammonia and deduce temperature T."),

    # Page 8: Question 3
    ("2005-jan-chm1-q3ai", "3(a)(i)", 8, 80, 200, 2, ["3.1.3"], ["explanation"], "Explain how each of the ions in magnesium chloride is formed."),
    ("2005-jan-chm1-q3aii", "3(a)(ii)", 8, 205, 320, 2, ["3.1.3"], ["explanation"], "Explain why compounds with ionic bonding tend to have high melting points."),
    ("2005-jan-chm1-q3bi", "3(b)(i)", 8, 325, 435, 2, ["3.1.3"], ["recall"], "Define the term electronegativity."),
    ("2005-jan-chm1-q3bii", "3(b)(ii)", 8, 440, 565, 2, ["3.1.3", "3.2.1"], ["explanation"], "Explain why electronegativity increases across a period in Periodic Table."),
    ("2005-jan-chm1-q3ci", "3(c)(i)", 8, 570, 680, 2, ["3.1.3"], ["recall"], "State what is meant by the term polarised."),
    ("2005-jan-chm1-q3cii", "3(c)(ii)", 8, 685, 785, 2, ["3.1.3"], ["explanation"], "Why is a chloride ion polarised more by aluminium ion than by magnesium ion?"),
    ("2005-jan-chm1-q3ciii", "3(c)(iii)", 8, 790, 850, 1, ["3.1.3"], ["recall"], "Predict the type of bonding in aluminium chloride."),

    # Page 9: Question 4
    ("2005-jan-chm1-q4ai", "4(a)(i)", 9, 80, 180, 1, ["3.1.2"], ["recall"], "Write equation for reaction between ammonia and sodium."),
    ("2005-jan-chm1-q4aii", "4(a)(ii)", 9, 185, 375, 2, ["3.1.3"], ["recall"], "Draw shape of NH3 molecule and amide ion NH2-, showing lone pairs."),
    ("2005-jan-chm1-q4aiii", "4(a)(iii)", 9, 380, 460, 1, ["3.1.3"], ["recall"], "State the bond angle found in an ammonia molecule."),
    ("2005-jan-chm1-q4aiv", "4(a)(iv)", 9, 465, 605, 2, ["3.1.3"], ["explanation"], "Explain why bond angle in amide ion is smaller than in ammonia molecule."),
    ("2005-jan-chm1-q4bi", "4(b)(i)", 9, 610, 715, 1, ["3.1.2"], ["recall"], "State what is meant by the term empirical formula."),
    ("2005-jan-chm1-q4bii", "4(b)(ii)", 9, 720, 870, 2, ["3.1.2"], ["calculation"], "Determine empirical formula of X (16.2% Mg, 18.9% N, 64.9% O).")
]

MS_DEF = {
    "2005-jan-chm1-q1ai": {
        "answers": "p + n / number of nucleons (accept protons and neutrons)",
        "extra": "(Incorrect reference to electrons = contradiction)",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2005-jan-chm1-q1aii": {
        "answers": "Mean / average mass of an molecule/entity/formula (1)<br>1/12th mass of atom of <sup>12</sup>C (1)<br>[Not 1/12th mass of molecule of <sup>12</sup>C] (mark independently)<br><b>OR</b> Mass of 1 mole of molecules/entities (1)<br>1/12th mass of 1 mole of <sup>12</sup>C (1)<br><b>OR</b> Average mass of a molecule/entity (1)<br>Relative to the mass of a <sup>12</sup>C atom taken as 12 / 12.000 (1)",
        "extra": "(Mean/average = stated or explained)<br>(mass = stated or explained)<br>(Penalise 'weight' once only)<br>(Ignore 'average' mass of <sup>12</sup>C)<br>(Do not allow 'mass of average molecule')",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q1bi": {
        "answers": "2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>6</sup> 4s<sup>1</sup> 3d<sup>10</sup> (accept 3d<sup>9</sup> 4s<sup>2</sup>)",
        "extra": "(accept subscripts or caps)<br>[Penalise missing shell numbers]",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2005-jan-chm1-q1bii": {
        "answers": "d / D",
        "extra": "[NOT 3d / 'transition element']",
        "mark": 1,
        "spec": "3.1.1 / 3.2.1"
    },
    "2005-jan-chm1-q1biii": {
        "answers": "36",
        "extra": "[NOT 36.0]",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2005-jan-chm1-q1ci": {
        "answers": "More <sup>63</sup>Cu atoms than <sup>65</sup>Cu atoms",
        "extra": "(idea of more abundant <sup>63</sup>Cu isotope – NOT just reference to peak heights)",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2005-jan-chm1-q1cii": {
        "answers": "Electron from electron gun / high speed electron / high energy electron (accept electron gun fired at) (1)<br>knock electron off (Cu atom) / idea of loss of e<sup>–</sup> / appropriate equation (1)",
        "extra": "[NOT 'bombarded with electrons']<br>(Mark independently)",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2005-jan-chm1-q1ciii": {
        "answers": "Identity: <sup>63</sup>Cu<sup>2+</sup> or equivalent (1)<br>Explanation: m/z = 63/2 (= 31.5) or equivalent (1)<br>Reason: More energy needed to remove second electron OR <sup>63</sup>Cu<sup>2+</sup> statistically less likely to remove second electron (1)",
        "extra": "[NOT 63.0 - penalise this error once only]<br>(Idea that not many <sup>63</sup>Cu<sup>2+</sup> ions formed OR explains why few are formed e.g. more energy needed)<br>If '<sup>63</sup>Cu' not given, can only award M2 & M3<br>[If 65 used, lose M1 and M2]<br>[If mass number missing from identity but appears in explanation, penalise M1 but allow M2 if earned]",
        "mark": 3,
        "spec": "3.1.1"
    },
    "2005-jan-chm1-q2ai": {
        "answers": "100 × 10<sup>–3</sup> × 0.500 = 5.00 × 10<sup>–2</sup> (mol)",
        "extra": "accept 5 × 10<sup>–2</sup> / 0.05",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q2aii": {
        "answers": "27.3 × 10<sup>–3</sup> × 0.600 = 1.64 × 10<sup>–2</sup> / 1.638 × 10<sup>–2</sup> (mol)",
        "extra": "only",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q2aiii": {
        "answers": "1.64 × 10<sup>–2</sup> (mol)",
        "extra": "Mark conseq on (ii)",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q2aiv": {
        "answers": "5.00 × 10<sup>–2</sup> – 1.64 × 10<sup>–2</sup> = 3.36 × 10<sup>–2</sup> (mol)",
        "extra": "Mark conseq on (i) & (iii)",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q2av": {
        "answers": "3.36 × 10<sup>–2</sup> × ½ = 1.68 × 10<sup>–2</sup> (mol) (1)<br>1.68 × 10<sup>–2</sup> × 132(.1) (1)<br>= 2.22 g (1)",
        "extra": "Mark conseq on (iv)<br>If 2.78 × 10<sup>–2</sup> used, 1.39 × 10<sup>–2</sup> mol, mass = 1.83 g",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q2b": {
        "answers": "pV = nRT (1)<br>n = 0.143 / 17 = 8.4(1) × 10<sup>–3</sup> (mol) (1)<br>T = pV / nR = (100000 × 2.86 × 10<sup>–4</sup>) / (8.31 × 8.41 × 10<sup>–3</sup>) (1)<br>= 408.5 – 410.5 (K) (1)",
        "extra": "Mark conseq on moles<br>Sig. fig. penalty - apply once if single sf given, unless calc works exactly",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q3ai": {
        "answers": "Electron transfers from Mg to Cl / Mg loses e<sup>–</sup> and Cl gains e<sup>–</sup> (1)<br>Mg loses 2e<sup>–</sup>, each Cl gains 1e<sup>–</sup> (1)",
        "extra": "(Marks can be awarded from diagrams/equations)",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q3aii": {
        "answers": "Electrostatic attractions / attractions between oppositely charged ions (1)<br>Are strong or require much energy to overcome (1)",
        "extra": "(molecules = CE = 0)<br>Tied to M1<br>'Ionic bonds are strong' score 1 mark",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q3bi": {
        "answers": "Tendency / strength / ability / power of an atom / element / nucleus to attract / withdraw electrons / e<sup>–</sup> density / bonding pair / shared pair (1)<br>In a covalent bond (1)",
        "extra": "(tied to M1 – unless silly slip in M1)<br>(If molecule/ion then = CE = 0) (NOT electron (singular) for M1)",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q3bii": {
        "answers": "Increasing proton number / nuclear charge (1)<br>Decreasing size / same shielding / same shells (1)",
        "extra": "(NOT atomic number)",
        "mark": 2,
        "spec": "3.1.3 / 3.2.1"
    },
    "2005-jan-chm1-q3ci": {
        "answers": "Electron cloud/distribution (around anion) (1)<br>Is distorted or is unequally distributed (1)",
        "extra": "Marks may be awarded from diagrams<br>'Chloride ion is distorted' scores 1 mark<br>(Reference to dipoles or polarised bond = CE)",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q3cii": {
        "answers": "Smaller size (1)<br>Higher charge or 3+/2+ specified (1)",
        "extra": "(Ignore m/z references)<br>('Higher charge density' scores 1 mark if neither mark awarded above)",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q3ciii": {
        "answers": "Covalent / covalent character / polar covalent / coordinate / dative",
        "extra": "[NOT ionic with covalent character]",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q4ai": {
        "answers": "2Na + 2NH<sub>3</sub> → 2NaNH<sub>2</sub> + H<sub>2</sub>",
        "extra": "(or multiples)",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q4aii": {
        "answers": "NH<sub>3</sub>: Pyramidal shape with 1 lone pair on N and 3 N-H bonds (1)<br>NH<sub>2</sub><sup>–</sup>: Bent shape with 2 lone pairs on N and 2 N-H bonds (1)",
        "extra": "(Missing 'H' penalise once only)<br>[NOT dot-and-cross diagrams]<br>[NOT 90° / 180° angles] (need 2 lp & 'bent' shape)",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q4aiii": {
        "answers": "107°",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q4aiv": {
        "answers": "More lone pairs on NH<sub>2</sub><sup>–</sup> than on NH<sub>3</sub> (1)<br>Lone pairs repel more than bonding pairs (1)",
        "extra": "Must be comparison<br>(Mark separately)<br>[NOT repulsion between atoms or between bonds]",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2005-jan-chm1-q4bi": {
        "answers": "Simplest ratio of atoms of each element in a compound / substance / species / entity / molecule",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2005-jan-chm1-q4bii": {
        "answers": "Mg = 16.2/24.3 = 0.667; N = 18.9/14 = 1.37; O = 64.9/16 = 4.06 (1)<br>Ratio 1 : 2 : 6 → MgN<sub>2</sub>O<sub>6</sub> (1)",
        "extra": "(Mark M1 first. If any wrong Ar used = CE = 0)<br>(Accept Mg(NO<sub>3</sub>)<sub>2</sub> for M2 if above working shown)",
        "mark": 2,
        "spec": "3.1.2"
    }
}

def main():
    print("Opening Question Paper PDF...")
    doc = fitz.open(QP_PATH)

    new_questions = []

    for qid, q_label, p_num, y0, y1, marks, spec, skills, desc in QUESTIONS_DEF:
        # Render initial crop image
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        
        subpart_name = qid.split("-")[-1]
        img_filename = f"q_{subpart_name}.jpg"
        img_rel = f"img/2005-jan-chm1/{img_filename}"
        img_abs = os.path.join(REPO_DIR, img_rel.replace("/", os.sep))
        
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        im.save(img_abs, format="JPEG", quality=92)
        
        # Render official mark scheme image
        ms_data = MS_DEF[qid]
        ms_filename = f"ms_{subpart_name}.png"
        ms_img_rel = f"img/2005-jan-chm1/{ms_filename}"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        
        render_official_markscheme_image(
            q_label,
            ms_data["answers"],
            ms_data["extra"],
            ms_data["mark"],
            ms_data["spec"],
            ms_img_abs
        )

        q_entry = {
            "id": qid,
            "paper": PAPER_INFO["id"],
            "year": PAPER_INFO["year"],
            "series": PAPER_INFO["series"],
            "unit": PAPER_INFO["unit"],
            "date": PAPER_INFO["date"],
            "question": q_label,
            "description": desc,
            "marks": marks,
            "topics": spec,
            "skills": skills,
            "image": img_rel,
            "markscheme": {
                "image": ms_img_rel
            },
            "page": p_num
        }
        new_questions.append(q_entry)
        print(f"Processed {qid} ({q_label}) - {marks} marks")

    # Load questions.json and update
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Ensure paper metadata exists in papers
    if not any(p["id"] == PAPER_INFO["id"] for p in db.get("papers", [])):
        db.setdefault("papers", []).append(PAPER_INFO)

    # Filter out existing entries for this paper if any
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    db["questions"].extend(new_questions)

    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully ingested {len(new_questions)} questions for {PAPER_INFO['id']}!")

if __name__ == "__main__":
    main()

"""
Ingestion script for 2004 June CHM1 (Section A only)
Excludes old-spec Section B essay questions (Q6).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921122_4c1e5527.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-june-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-june-chm1",
    "year": 2004,
    "series": "June",
    "date": "2004-06-10",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

# (qid, q_label, page, y0, y1, mark, spec_topics, skills, prompt)
QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(c)
    ("2004-june-chm1-q1a", "1(a)", 2, 75, 335, 2, ["3.1.1"], ["recall"], "Complete table of relative mass and relative charge for proton and electron."),
    ("2004-june-chm1-q1bi", "1(b)(i)", 2, 340, 445, 1, ["3.1.1"], ["recall"], "Give the number of protons in an atom of 27Al."),
    ("2004-june-chm1-q1bii", "1(b)(ii)", 2, 448, 565, 2, ["3.1.1"], ["recall"], "Deduce symbol, mass number and atomic number for atom of element Q."),
    ("2004-june-chm1-q1c", "1(c)", 2, 570, 775, 2, ["3.1.1"], ["recall"], "Define the term relative atomic mass of an element."),

    # Page 5: Question 1(d)-(e)
    ("2004-june-chm1-q1d", "1(d)", 5, 75, 395, 2, ["3.1.1"], ["calculation"], "Calculate relative atomic mass of magnesium from mass spectrum isotopic abundance data."),
    ("2004-june-chm1-q1e", "1(e)", 5, 398, 775, 1, ["3.1.1"], ["recall"], "State how relative molecular mass of a covalent compound is obtained from mass spectrum."),

    # Page 6: Question 2(a)-(b)
    ("2004-june-chm1-q2ai", "2(a)(i)", 6, 75, 320, 1, ["3.1.2"], ["calculation"], "Calculate number of moles of HCl in 24.3 cm3 of 0.200 mol dm-3 hydrochloric acid."),
    ("2004-june-chm1-q2aii", "2(a)(ii)", 6, 322, 385, 1, ["3.1.2"], ["calculation"], "Deduce number of moles of Na2CO3 in 25.0 cm3 of solution."),
    ("2004-june-chm1-q2aiii", "2(a)(iii)", 6, 388, 450, 1, ["3.1.2"], ["calculation"], "Deduce number of moles of Na2CO3 in original 250 cm3 of solution."),
    ("2004-june-chm1-q2aiv", "2(a)(iv)", 6, 452, 570, 2, ["3.1.2"], ["calculation"], "Calculate the Mr of the hydrated sodium carbonate."),
    ("2004-june-chm1-q2b", "2(b)", 6, 572, 775, 3, ["3.1.2"], ["calculation"], "Calculate number of molecules of water of crystallisation x when Mr is 250."),

    # Page 7: Question 2(c)
    ("2004-june-chm1-q2ci", "2(c)(i)", 7, 75, 185, 1, ["3.1.2"], ["recall"], "Give the ideal gas equation."),
    ("2004-june-chm1-q2cii", "2(c)(ii)", 7, 188, 775, 4, ["3.1.2"], ["calculation"], "Use ideal gas equation to calculate pressure of argon gas in cylinder."),

    # Page 8: Question 3
    ("2004-june-chm1-q3a", "3(a)", 8, 75, 275, 2, ["3.1.1"], ["recall"], "Explain the meaning of the term first ionisation energy of an atom."),
    ("2004-june-chm1-q3b", "3(b)", 8, 278, 395, 2, ["3.1.1"], ["recall"], "Write an equation illustrating the second ionisation energy of magnesium."),
    ("2004-june-chm1-q3c", "3(c)", 8, 398, 545, 2, ["3.1.1"], ["analysis"], "Explain why first ionisation energy of magnesium is higher than sodium."),
    ("2004-june-chm1-q3d", "3(d)", 8, 548, 775, 2, ["3.1.1"], ["analysis"], "Explain why first ionisation energy of neon is higher than sodium."),

    # Page 9: Question 4
    ("2004-june-chm1-q4a", "4(a)", 9, 75, 245, 1, ["3.1.2"], ["recall"], "Balance equation for reaction between LiH and AlCl3."),
    ("2004-june-chm1-q4b", "4(b)", 9, 248, 325, 1, ["3.1.1"], ["recall"], "Give the electronic configuration of the hydride ion, H-."),
    ("2004-june-chm1-q4c", "4(c)", 9, 328, 495, 3, ["3.1.3"], ["recall"], "Predict shape of AlH4- ion and explain why it has this shape."),
    ("2004-june-chm1-q4d", "4(d)", 9, 498, 775, 3, ["3.1.3"], ["recall"], "Name bond H->Al in AlH4- and explain how it is formed."),

    # Page 10: Question 5
    ("2004-june-chm1-q5a", "5(a)", 10, 75, 275, 3, ["3.2.2"], ["recall"], "State trend in reactivity of Group II with water, conditions for Mg, and equation."),
    ("2004-june-chm1-q5b", "5(b)", 10, 278, 775, 4, ["3.2.2"], ["recall"], "Describe observations and equations when NaOH is added to BeCl2 drops then excess.")
]

MS_DATA = {
    "2004-june-chm1-q1a": {
        "answers": "• Proton: mass = 1, charge = +1 (1)<br>• Electron: mass &le; 1/1800 or &le; 5.6 &times; 10<sup>&minus;4</sup>, charge = &minus;1 (1)",
        "extra": "do not accept +1 for proton mass or 'g' units",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q1bi": {
        "answers": "13 (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q1bii": {
        "answers": "• Si (1)<br>• Mass number = 28 and atomic number = 14 (1)<br>(Symbol: <sup>28</sup><sub>14</sub>Si)",
        "extra": "do not accept 28.1 or 28.0 or 'Silicon'",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q1c": {
        "answers": "Mean (average) mass of an atom / all the isotopes (1)<br>Relative to 1/12th mass of atom of <sup>12</sup>C (1)<br><i>OR</i><br>Mass of 1 mole of atoms of an element (1)<br>Relative to 1/12th mass of 1 mole of <sup>12</sup>C (1)",
        "extra": "penalise 'weight' once only<br>ignore 'average' mass of 12C<br>do not allow 'mass of average atom'",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q1d": {
        "answers": "• A<sub>r</sub> = (24 &times; 0.735) + (25 &times; 0.101) + (26 &times; 0.164) (1)<br>• = 24.4 (1)",
        "extra": "mark M2 conseq on transcription error or incorrect addition of %",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q1e": {
        "answers": "M<sub>r</sub> = highest m/z value (1)",
        "extra": "NOT 'highest/largest/right-hand' peak",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q2ai": {
        "answers": "4.86 &times; 10<sup>&minus;3</sup> (mol) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q2aii": {
        "answers": "2.43 &times; 10<sup>&minus;3</sup> (mol) (1)",
        "extra": "mark consequential on (a)(i)",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q2aiii": {
        "answers": "2.43 &times; 10<sup>&minus;2</sup> (mol) (1)",
        "extra": "mark consequential on (a)(ii)",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q2aiv": {
        "answers": "• 3.01 / (2.43 &times; 10<sup>&minus;2</sup>) (1)<br>• = 124 (1)",
        "extra": "mark consequential on (a)(iii)<br>do not allow 124 without evidence of appropriate calculation in (a)(iii)",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q2b": {
        "answers": "• M<sub>r</sub>(Na<sub>2</sub>CO<sub>3</sub>) = 106 (1)<br>• M<sub>r</sub>(xH<sub>2</sub>O) = 250 &minus; 106 = 144 (1)<br>• x = 144 / 18 = 8 (1)",
        "extra": "M2 and M3 consequential on previous steps<br>penalise sf errors once only",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q2ci": {
        "answers": "pV = nRT (1)",
        "extra": "allow PV = nRT",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q2cii": {
        "answers": "• Moles Ar = 325 / 39.9 = 8.15 (1) (accept M<sub>r</sub> = 40)<br>• p = nRT / V = (8.15 &times; 8.31 &times; 298) / (5.00 &times; 10<sup>&minus;3</sup>) (1)<br>• = 4.03 &times; 10<sup>6</sup> Pa <i>OR</i> 4.03 &times; 10<sup>3</sup> kPa (1)<br>• Range = 4.02 &times; 10<sup>6</sup> Pa to 4.04 &times; 10<sup>6</sup> Pa (1)",
        "extra": "if equation incorrectly rearranged, M3 & M4 = 0; if n = 325, lose M2<br>allow M1 if gas law in (ii) if not given in (i)",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q3a": {
        "answers": "• Enthalpy change / energy required when an electron is removed / knocked out / displaced (1)<br>• From a gaseous atom (1)",
        "extra": "ignore 'minimum' energy<br>could get gaseous atom mark from equation",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q3b": {
        "answers": "• Mg<sup>+</sup>(g) &rarr; Mg<sup>2+</sup>(g) + e<sup>&minus;</sup> (1)<br>• State symbols (g) on Mg<sup>+</sup> and Mg<sup>2+</sup> (1)",
        "extra": "or Mg+(g) + e- -> Mg2+(g) + 2e-<br>state symbols tied to correct equation",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q3c": {
        "answers": "• Increased / stronger nuclear charge or more protons (in Mg) (1)<br>• Smaller atom or electrons enter the same shell or same / similar shielding (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q3d": {
        "answers": "• Electron removed from a shell of lower energy or smaller atom or e<sup>&minus;</sup> nearer nucleus or e<sup>&minus;</sup> removed from 2p rather than 3s (1)<br>• Less shielding (1)",
        "extra": "do not accept 'e- from inner shell'",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q4a": {
        "answers": "4LiH + AlCl<sub>3</sub> &rarr; LiAlH<sub>4</sub> + 3LiCl (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-june-chm1-q4b": {
        "answers": "1s<sup>2</sup> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-june-chm1-q4c": {
        "answers": "• Tetrahedral (or diagram) (1)<br>• (Equal) repulsion (1)<br>• Between four bonding pairs / bonds (1)",
        "extra": "not distorted tetrahedral<br>not repulsion between H atoms (loses M2 and M3)<br>not 'separate as far as possible'<br>'4' may be inferred from a correct diagram",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2004-june-chm1-q4d": {
        "answers": "• Dative (covalent) or coordinate (1)<br>• Lone pair or non-bonding pair of electrons (1)<br>• Donated from H<sup>&minus;</sup> to Al or shared between H and Al (1)",
        "extra": "M3 tied to M2<br>not 'from H atom', not 'to Al ion', not 'e-s transferred'",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2004-june-chm1-q5a": {
        "answers": "• Trend: Increases (1)<br>• Conditions: Heat or steam or gas phase or high temperature (>100 &deg;C) (1)<br>• Equation: Mg + H<sub>2</sub>O &rarr; MgO + H<sub>2</sub> (1)",
        "extra": "NOT 'hot'<br>ignore state symbols even if wrong",
        "mark": 3,
        "spec": "3.2.2"
    },
    "2004-june-chm1-q5b": {
        "answers": "• Observation drops: White precipitate / solid / suspension (1)<br>• Equation drops: BeCl<sub>2</sub> + 2NaOH &rarr; Be(OH)<sub>2</sub> + 2NaCl (1) <i>or</i> Be<sup>2+</sup> + 2OH<sup>&minus;</sup> &rarr; Be(OH)<sub>2</sub><br>• Observation excess: Precipitate (re)dissolves or solution goes clear (1)<br>• Equation excess: Be(OH)<sub>2</sub> + 2OH<sup>&minus;</sup> &rarr; [Be(OH)<sub>4</sub>]<sup>2&minus;</sup> (1) <i>or</i> Be(OH)<sub>2</sub> + 2NaOH &rarr; Na<sub>2</sub>Be(OH)<sub>4</sub>",
        "extra": "drops: not 'cloudy/milky'; allow BeCl2 + 2OH- -> Be(OH)2 + 2Cl-<br>excess: allow 'ppt disappears', NOT 'solution forms'; NOT [Be(OH)6]4-",
        "mark": 4,
        "spec": "3.2.2"
    }
}

def main():
    doc = fitz.open(QP_PATH)
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    if not any(p["id"] == PAPER_INFO["id"] for p in db.get("papers", [])):
        db.setdefault("papers", []).append(PAPER_INFO)

    existing_ids = {q["id"] for q in db["questions"]}
    added = 0

    for qid, q_label, p_num, y0, y1, mark, spec_topics, skills, prompt in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-june-chm1/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-june-chm1/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-june-chm1",
            "year": 2004,
            "series": "June",
            "code": "CHM1",
            "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
            "question": q_label,
            "page": p_num,
            "marks": mark,
            "topics": spec_topics,
            "skills": skills,
            "description": prompt,
            "image": q_img_rel,
            "markscheme": ms_img_rel
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

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-june-chm1 ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

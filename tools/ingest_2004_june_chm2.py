"""
Ingestion script for 2004 June CHM2 (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921125_fadf2276.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-june-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-june-chm2",
    "year": 2004,
    "series": "June",
    "date": "2004-06-10",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(c)(i)
    ("2004-june-chm2-q1a", "1(a)", 2, 75, 520, 3, ["3.1.4"], ["calculation"], "Calculate enthalpy change for decomposition of H2O2 from mean bond enthalpies."),
    ("2004-june-chm2-q1b", "1(b)", 2, 522, 640, 2, ["3.1.4"], ["recall"], "Write equation with state symbols for standard enthalpy of formation of methane."),
    ("2004-june-chm2-q1ci", "1(c)(i)", 2, 642, 775, 1, ["3.1.3"], ["recall"], "Suggest why a large amount of heat energy is required to produce free carbon atoms from solid carbon."),

    # Page 5: Question 1(c)(ii)-(iii)
    ("2004-june-chm2-q1cii", "1(c)(ii)", 5, 75, 360, 3, ["3.1.4"], ["calculation"], "Calculate enthalpy change for CH4(g) -> C(g) + 4H(g) using Hess's Law."),
    ("2004-june-chm2-q1ciii", "1(c)(iii)", 5, 362, 775, 1, ["3.1.4"], ["calculation"], "Calculate mean bond enthalpy of C-H bond in methane."),

    # Page 7: Question 2
    ("2004-june-chm2-q2a", "2(a)", 7, 75, 475, 3, ["3.1.5"], ["analysis"], "Draw Maxwell-Boltzmann distribution curve for gas G."),
    ("2004-june-chm2-q2b", "2(b)", 7, 478, 595, 2, ["3.1.5"], ["recall"], "Define the term activation energy."),
    ("2004-june-chm2-q2c", "2(c)", 7, 598, 720, 2, ["3.1.5"], ["analysis"], "Suggest why at constant temperature most of G eventually decomposes."),
    ("2004-june-chm2-q2d", "2(d)", 7, 722, 775, 3, ["3.1.5"], ["analysis"], "State effect of catalyst on time for decomposition and explain in general terms."),

    # Page 8: Question 3(a)-(c)
    ("2004-june-chm2-q3a", "3(a)", 8, 75, 360, 1, ["3.1.6"], ["recall"], "Compare rate of forward reaction with backward reaction at equilibrium."),
    ("2004-june-chm2-q3bi", "3(b)(i)", 8, 362, 530, 3, ["3.1.6"], ["analysis"], "Deduce effect and explanation of reduced pressure on equilibrium yield of methanol."),
    ("2004-june-chm2-q3bii", "3(b)(ii)", 8, 532, 665, 2, ["3.1.6"], ["recall"], "Give two reasons why industry prefers to operate processes at lower pressures."),
    ("2004-june-chm2-q3c", "3(c)", 8, 668, 775, 2, ["3.1.6"], ["analysis"], "Deduce effect and explanation of more efficient catalyst on equilibrium yield."),

    # Page 9: Question 3(d)-(e)
    ("2004-june-chm2-q3d", "3(d)", 9, 75, 350, 3, ["3.1.6"], ["analysis"], "Deduce sign of enthalpy change for reaction from lower temperature conversion data."),
    ("2004-june-chm2-q3e", "3(e)", 9, 352, 775, 1, ["3.1.6"], ["recall"], "Suggest what is done with unreacted carbon dioxide and hydrogen."),

    # Page 10: Question 4(a)-(e)
    ("2004-june-chm2-q4a", "4(a)", 10, 75, 215, 1, ["3.1.7"], ["recall"], "Define an oxidising agent in terms of electrons."),
    ("2004-june-chm2-q4bi", "4(b)(i)", 10, 218, 335, 2, ["3.1.7"], ["recall"], "Deduce oxidation state of sulphur in SO2 and in SO4(2-)."),
    ("2004-june-chm2-q4bii", "4(b)(ii)", 10, 338, 400, 1, ["3.1.7"], ["recall"], "Deduce half-equation for reduction of bromine in aqueous solution."),
    ("2004-june-chm2-q4biii", "4(b)(iii)", 10, 402, 470, 1, ["3.1.7"], ["recall"], "Deduce half-equation for oxidation of SO2 forming SO4(2-) and H+ ions."),
    ("2004-june-chm2-q4biv", "4(b)(iv)", 10, 472, 570, 1, ["3.1.7"], ["recall"], "Construct overall equation for reaction between aqueous bromine and sulphur dioxide."),
    ("2004-june-chm2-q4c", "4(c)", 10, 490, 615, 3, ["3.2.3"], ["recall"], "Equation for reaction of chlorine with water and oxidation states of chlorine."),
    ("2004-june-chm2-q4d", "4(d)", 10, 615, 700, 1, ["3.2.3"], ["recall"], "Reason why chlorine is not formed when solid KCl reacts with conc H2SO4."),
    ("2004-june-chm2-q4e", "4(e)", 10, 700, 775, 1, ["3.2.3"], ["recall"], "Equation for reaction between solid potassium chloride and concentrated sulphuric acid."),

    # Page 11: Question 4(f)
    ("2004-june-chm2-q4fi", "4(f)(i)", 11, 75, 160, 1, ["3.2.3"], ["recall"], "Give oxidation product formed from potassium bromide and conc sulphuric acid."),
    ("2004-june-chm2-q4fii", "4(f)(ii)", 11, 162, 775, 1, ["3.2.3"], ["recall"], "Give reduction product formed from sulphuric acid and potassium bromide.")
]

MS_DATA = {
    "2004-june-chm2-q1a": {
        "answers": "• &Delta;H = &Sigma;(bonds broken) &minus; &Sigma;(bonds formed) (or cycle) (1)<br>• = +146 &minus; 496/2 (or 2 &times; 463 + 146 &minus; (2 &times; 463 + 496/2)) (1)<br>• = &minus;102 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "accept no units, wrong units loses a mark; +102 scores (1) only",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2004-june-chm2-q1b": {
        "answers": "• C(s) + 2H<sub>2</sub>(g) &rarr; CH<sub>4</sub>(g) (1)<br>• Correct state symbols (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2004-june-chm2-q1ci": {
        "answers": "Macromolecular (1)",
        "extra": "accept giant molecule or carbon has many (4) bonds",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2004-june-chm2-q1cii": {
        "answers": "• &Delta;H = &Sigma;&Delta;H<sub>f</sub>(products) &minus; &Sigma;&Delta;H<sub>f</sub>(reactants) (or cycle) (1)<br>• = 715 + 4 &times; 218 &minus; (&minus;74.9) (1)<br>• = 1662 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "accept no units, wrong units loses one mark, allow 1660 to 1663; &minus;1662 scores one mark only",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2004-june-chm2-q1ciii": {
        "answers": "1662 / 4 = 415.5 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "mark is for divide by four, allow consequential if answer to (c)(ii) is wrong",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2004-june-chm2-q2a": {
        "answers": "• Graph starts at origin (1)<br>• Graph skewed to left and has decreasing gradient to maximum (1)<br>• Graph after maximum decreases in steepness, never touches x axis, levels out less than 5 mm from x axis (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.5"
    },
    "2004-june-chm2-q2b": {
        "answers": "• Minimum energy (1)<br>• To start a reaction (or for a reaction to occur) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2004-june-chm2-q2c": {
        "answers": "• Molecules gain energy (or always some molecules have E > E<sub>a</sub>) (1)<br>• Due to collisions (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2004-june-chm2-q2d": {
        "answers": "• Time for decomposition: Decreases (1)<br>• Explanation: E<sub>a</sub> lowered (1) by alternative route (1) so more molecules have energy &gt; E<sub>a</sub> (1) [max 2 for explanation]",
        "extra": "max 2 for explanation",
        "mark": 3,
        "spec": "3.1.5"
    },
    "2004-june-chm2-q3a": {
        "answers": "Same (or equal) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2004-june-chm2-q3bi": {
        "answers": "• Yield: Decreases (1)<br>• More moles on left hand side (4 mol vs 2 mol) (1)<br>• Equilibrium moves to increase the pressure (or to oppose change / compensate for low pressure) (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.6"
    },
    "2004-june-chm2-q3bii": {
        "answers": "Any two from:<br>• Cost of producing high pressure (1)<br>• Cost of plant to resist high pressure (1)<br>• Correct safety factor with reason (1)",
        "extra": "max 2 marks",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2004-june-chm2-q3c": {
        "answers": "• Yield: No change (1)<br>• Catalyst has no effect on equilibrium position / affects rate of forward and backwards reactions equally (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2004-june-chm2-q3d": {
        "answers": "• Sign: Negative (1)<br>• Reaction (or equilibrium) moves in exothermic direction / to the right (1)<br>• In order to oppose the change / raise temperature (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.6"
    },
    "2004-june-chm2-q3e": {
        "answers": "Recycled (or re-used or 'put back in') (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2004-june-chm2-q4a": {
        "answers": "Gains electrons (or removes electrons) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2004-june-chm2-q4bi": {
        "answers": "• SO<sub>2</sub>: +4 (1)<br>• SO<sub>4</sub><sup>2&minus;</sup>: +6 (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.7"
    },
    "2004-june-chm2-q4bii": {
        "answers": "Br<sub>2</sub> + 2e<sup>&minus;</sup> &rarr; 2Br<sup>&minus;</sup> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2004-june-chm2-q4biii": {
        "answers": "SO<sub>2</sub> + 2H<sub>2</sub>O &rarr; 4H<sup>+</sup> + SO<sub>4</sub><sup>2&minus;</sup> + 2e<sup>&minus;</sup> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2004-june-chm2-q4biv": {
        "answers": "Br<sub>2</sub> + SO<sub>2</sub> + 2H<sub>2</sub>O &rarr; 2Br<sup>&minus;</sup> + 4H<sup>+</sup> + SO<sub>4</sub><sup>2&minus;</sup> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2004-june-chm2-q4c": {
        "answers": "• Cl<sub>2</sub> + H<sub>2</sub>O &rarr; H<sup>+</sup> + Cl<sup>&minus;</sup> + HOCl (1)<br>• Chloride: &minus;1 (1)<br>• Chlorate(I): +1 (1)",
        "extra": "allow HCl + HClO",
        "mark": 3,
        "spec": "3.2.3"
    },
    "2004-june-chm2-q4d": {
        "answers": "Chloride ions cannot reduce sulphuric acid (1)",
        "extra": "or chloride ions are weak reducing agents / sulphuric acid is not strong enough oxidising agent / sulphuric acid is weaker oxidising agent than chlorine",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2004-june-chm2-q4e": {
        "answers": "KCl + H<sub>2</sub>SO<sub>4</sub> &rarr; HCl + KHSO<sub>4</sub> (1)",
        "extra": "allow 2KCl + H2SO4 -> 2HCl + K2SO4",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2004-june-chm2-q4fi": {
        "answers": "Bromine (1)",
        "extra": "allow Br2",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2004-june-chm2-q4fii": {
        "answers": "Sulphur dioxide (1)",
        "extra": "allow SO2",
        "mark": 1,
        "spec": "3.2.3"
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
        q_img_rel = f"img/2004-june-chm2/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-june-chm2/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-june-chm2",
            "year": 2004,
            "series": "June",
            "code": "CHM2",
            "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
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

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-june-chm2 ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

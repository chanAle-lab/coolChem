"""
Ingestion script for 2004 January CHM2 (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960738_8da10bc5.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-jan-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-jan-chm2",
    "year": 2004,
    "series": "January",
    "date": "2004-01-09",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2004-jan-chm2-q1a", "1(a)", 2, 75, 230, 1, ["3.1.6"], ["recall"], "State Le Chatelier's principle."),
    ("2004-jan-chm2-q1bi", "1(b)(i)", 2, 232, 420, 3, ["3.1.6"], ["recall"], "Predict and explain effect of increased overall pressure on hydrogen yield."),
    ("2004-jan-chm2-q1bii", "1(b)(ii)", 2, 422, 595, 3, ["3.1.6"], ["recall"], "Predict and explain effect of increased steam concentration on hydrogen yield."),
    ("2004-jan-chm2-q1c", "1(c)", 2, 598, 775, 2, ["3.1.6"], ["analysis"], "Two reasons why operating temperature higher than 1200 K is not used industrially."),

    # Page 5: Question 2
    ("2004-jan-chm2-q2a", "2(a)", 5, 75, 245, 2, ["3.1.5"], ["recall"], "Label axes on Maxwell-Boltzmann distribution diagram."),
    ("2004-jan-chm2-q2b", "2(b)", 5, 248, 340, 2, ["3.1.5"], ["analysis"], "Draw Maxwell-Boltzmann distribution curve for sample at lower temperature."),
    ("2004-jan-chm2-q2c", "2(c)", 5, 342, 428, 1, ["3.1.5"], ["recall"], "Explain why most particle collisions do not result in a reaction."),
    ("2004-jan-chm2-q2d", "2(d)", 5, 430, 520, 1, ["3.1.5"], ["recall"], "State one way collision frequency between gas particles can be increased without changing temperature."),
    ("2004-jan-chm2-q2e", "2(e)", 5, 522, 650, 2, ["3.1.5"], ["recall"], "Suggest why small temperature increase leads to large increase in reaction rate."),
    ("2004-jan-chm2-q2f", "2(f)", 5, 652, 775, 2, ["3.1.5"], ["recall"], "Explain in general terms how a catalyst works."),

    # Page 6: Question 3
    ("2004-jan-chm2-q3a", "3(a)", 6, 75, 170, 1, ["3.2.3"], ["recall"], "Identify halogen that is the strongest oxidising agent."),
    ("2004-jan-chm2-q3b", "3(b)", 6, 172, 250, 1, ["3.2.3"], ["recall"], "Give formula of halide ion that is the strongest reducing agent."),
    ("2004-jan-chm2-q3c", "3(c)", 6, 252, 430, 3, ["3.2.3"], ["recall"], "Observations with NaF and NaI upon adding AgNO3, and equation for NaI with state symbols."),
    ("2004-jan-chm2-q3d", "3(d)", 6, 432, 545, 2, ["3.2.3"], ["recall"], "Observation and equation for concentrated sulphuric acid added to solid NaCl."),
    ("2004-jan-chm2-q3e", "3(e)", 6, 548, 690, 4, ["3.2.3"], ["recall"], "Two observations and equation for concentrated sulphuric acid added to solid NaI."),
    ("2004-jan-chm2-q3f", "3(f)", 6, 692, 775, 3, ["3.2.3", "3.1.7"], ["recall"], "Colour change with starch and equation for iodine reaction with Na2S2O3."),

    # Page 7: Question 4
    ("2004-jan-chm2-q4a", "4(a)", 7, 75, 220, 1, ["3.1.7"], ["recall"], "State in terms of electrons what happens in a redox reaction."),
    ("2004-jan-chm2-q4bi", "4(b)(i)", 7, 222, 420, 3, ["3.2.4", "3.1.7"], ["recall"], "Equation for TiO2 converted to TiCl4, identifying oxidising and reducing agents."),
    ("2004-jan-chm2-q4bii", "4(b)(ii)", 7, 422, 690, 5, ["3.2.4"], ["recall"], "Equation for TiCl4 reduced to Ti metal, stating two conditions and explanations."),
    ("2004-jan-chm2-q4c", "4(c)", 7, 692, 775, 1, ["3.2.4"], ["recall"], "Give major reason why recycling aluminium is economically viable.")
]

MS_DATA = {
    "2004-jan-chm2-q1a": {
        "answers": "An <b>equilibrium opposes change</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2004-jan-chm2-q1bi": {
        "answers": "• Effect on yield of hydrogen: <b>decrease</b> (1)<br>• Explanation: pressure lowered (or increase opposed) (1)<br>• by favouring <b>fewer moles (of gas)</b> (1)",
        "extra": "CE if not decrease but mark on if no answer.",
        "mark": 3,
        "spec": "3.1.6"
    },
    "2004-jan-chm2-q1bii": {
        "answers": "• Effect on yield of hydrogen: <b>increase</b> (1)<br>• Explanation: [reactants / steam] concentration reduced <i>OR</i> steam removed (1)<br>• by shifting to right / forward reaction favoured (1)",
        "extra": "CE if wrong as above.",
        "mark": 3,
        "spec": "3.1.6"
    },
    "2004-jan-chm2-q1c": {
        "answers": "• Reason 1: cost of high temperature / energy too high (1)<br>• Reason 2: cost of plant (to resist high T) too high <i>OR</i> plant could not contain high T (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2004-jan-chm2-q2a": {
        "answers": "• <i>y</i>-axis: <b>fraction / % / number of molecules / particles</b> (1) [NOT moles]<br>• <i>x</i>-axis: <b>(kinetic / molecular) energy</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2004-jan-chm2-q2b": {
        "answers": "• Peak higher and displaced to the left (1)<br>• Must cross once only, must NOT cross <i>x</i>-axis, must go through origin (1)",
        "extra": "Can only score second mark if first mark obtained.",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2004-jan-chm2-q2c": {
        "answers": "<b>Energy &lt; <i>E</i><sub>a</sub></b> <i>OR</i> must have enough energy (to react) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2004-jan-chm2-q2d": {
        "answers": "<b>Increase concentration (or pressure)</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2004-jan-chm2-q2e": {
        "answers": "(Many) (1) <b>more molecules have <i>E</i> &ge; <i>E</i><sub>a</sub></b> / enough energy (1)",
        "extra": "NOT KE increases with T.",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2004-jan-chm2-q2f": {
        "answers": "• Lowers <b><i>E</i><sub>a</sub></b> (1)<br>• <b>Alternative route</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2004-jan-chm2-q3a": {
        "answers": "<b>Fluorine</b> <i>OR</i> <b>F<sub>2</sub></b> <i>OR</i> <b>F</b> (1)",
        "extra": "NOT Fl.",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2004-jan-chm2-q3b": {
        "answers": "<b>I<sup>&minus;</sup></b> (or At<sup>&minus;</sup>) (1)",
        "extra": "Allow +e- but not equation.",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2004-jan-chm2-q3c": {
        "answers": "• Observation with NaF(aq): <b>no change</b> <i>OR</i> remains colourless (1)<br>• Observation with NaI(aq): <b>yellow solid / precipitate</b> (1)<br>• Equation: <b>I<sup>&minus;</sup>(aq) + Ag<sup>+</sup>(aq) &rarr; AgI(s)</b> (1)<br><i>OR</i> NaI(aq) + AgNO<sub>3</sub>(aq) &rarr; NaNO<sub>3</sub>(aq) + AgI(s)<br>(State symbols required on ionic equation).",
        "extra": "No state symbols on equation loses mark.",
        "mark": 3,
        "spec": "3.2.3"
    },
    "2004-jan-chm2-q3d": {
        "answers": "• Observation: <b>steamy / white / misty fumes</b> (1) [NOT smoke / gas]<br>• Equation: <b>NaCl + H<sub>2</sub>SO<sub>4</sub> &rarr; NaHSO<sub>4</sub> + HCl</b> (1)",
        "extra": "Ignore state symbols.",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2004-jan-chm2-q3e": {
        "answers": "• Observation 1: <b>black / grey solid</b> <i>OR</i> <b>purple gas / lilac</b> (1)<br>• Observation 2: <b>yellow solid</b> <i>OR</i> <b>smell bad eggs / stink bombs</b> <i>OR</i> pungent / choking / steamy fumes (1) [any two observations]<br>• Equation: <b>2NaI + 2H<sub>2</sub>SO<sub>4</sub> &rarr; Na<sub>2</sub>SO<sub>4</sub> + 2H<sub>2</sub>O + I<sub>2</sub> + SO<sub>2</sub></b> (2)<br>[Two reduction products from Na2SO4 (1) and balanced equation (1); allow H2S or S as reduction products].",
        "extra": "",
        "mark": 4,
        "spec": "3.2.3"
    },
    "2004-jan-chm2-q3f": {
        "answers": "• Observation: (starts) <b>blue or black</b> (1) &rarr; <b>colourless</b> (1)<br>• Equation: <b>I<sub>2</sub> + 2Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub> &rarr; 2NaI + Na<sub>2</sub>S<sub>4</sub>O<sub>6</sub></b> (1)<br>(<i>OR</i> I<sub>2</sub> + 2S<sub>2</sub>O<sub>3</sub><sup>2&minus;</sup> &rarr; 2I<sup>&minus;</sup> + S<sub>4</sub>O<sub>6</sub><sup>2&minus;</sup>)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.3"
    },
    "2004-jan-chm2-q4a": {
        "answers": "<b>Electrons transferred</b> (1)<br><i>OR</i> some lose e<sup>&minus;</sup>, some gain e<sup>&minus;</sup> <i>OR</i> oxidation is loss of e<sup>&minus;</sup>, reduction is gain in e<sup>&minus;</sup>",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2004-jan-chm2-q4bi": {
        "answers": "• Equation: <b>TiO<sub>2</sub> + 2C + 2Cl<sub>2</sub> &rarr; TiCl<sub>4</sub> + 2CO</b> (1)<br>[<i>OR</i> TiO<sub>2</sub> + C + 2Cl<sub>2</sub> &rarr; TiCl<sub>4</sub> + CO<sub>2</sub>]<br>• Oxidising agent: <b>Cl<sub>2</sub></b> (1)<br>• Reducing agent: <b>C</b> (1) [allow coke, not coal]",
        "extra": "Con = 0 marks if more than 1 species.",
        "mark": 3,
        "spec": "3.2.4"
    },
    "2004-jan-chm2-q4bii": {
        "answers": "• Equation: <b>TiCl<sub>4</sub> + 2Mg &rarr; Ti + 2MgCl<sub>2</sub></b> (1) [<i>OR</i> TiCl<sub>4</sub> + 4Na &rarr; Ti + 4NaCl]<br>• Condition 1: <b>High temp / (500 &ndash; 1000 &deg;C)</b> (1)<br>• Explanation 1: to speed up reaction / makes more reactants with <i>E</i> &gt; <i>E</i><sub>a</sub> (1)<br>• Condition 2: <b>Argon (atmosphere)</b> (1) [NOT inert atmosphere alone]<br>• Explanation 2: prevents oxidation of Mg/Na/Ti <i>OR</i> prevents contamination of Ti with O/N <i>OR</i> prevents H<sub>2</sub>O reacting with TiCl<sub>4</sub>/Na/Mg (1)",
        "extra": "",
        "mark": 5,
        "spec": "3.2.4"
    },
    "2004-jan-chm2-q4c": {
        "answers": "<b>Electrolysis is expensive / large electricity / energy cost</b> to reduce Al<sub>2</sub>O<sub>3</sub> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    }
}

def main():
    doc = fitz.open(QP_PATH)
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    existing_ids = {q["id"] for q in db["questions"]}
    added = 0

    for qid, q_label, p_num, y0, y1, mark, spec_topics, skills, prompt in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-jan-chm2/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-jan-chm2/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-jan-chm2",
            "year": 2004,
            "series": "January",
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

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-jan-chm2 ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

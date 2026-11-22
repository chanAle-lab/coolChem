"""
Ingestion script for 2004 January CHM5 (Section A only)
Excludes old-spec Section B essay questions (Q7-Q10).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960895_e3fc9c52.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-jan-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-jan-chm5",
    "year": 2004,
    "series": "January",
    "date": "2004-01-23",
    "code": "CHM5",
    "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 120,
    "duration": "2 hours"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)
    ("2004-jan-chm5-q1a", "1(a)", 2, 75, 775, 6, ["3.1.8"], ["calculation"], "Calculate standard enthalpy change and entropy change for 4HCl + O2 <=> 2Cl2 + 2H2O."),

    # Page 5: Question 1(b)
    ("2004-jan-chm5-q1bi", "1(b)(i)", 5, 75, 340, 2, ["3.1.6"], ["recall"], "Deduce effect and explanation of temperature increase on equilibrium position."),
    ("2004-jan-chm5-q1bii", "1(b)(ii)", 5, 342, 775, 3, ["3.1.8"], ["calculation"], "Calculate minimum temperature at which reaction is feasible (delta G <= 0)."),

    # Page 6: Question 2
    ("2004-jan-chm5-q2ai", "2(a)(i)", 6, 75, 320, 3, ["3.1.3"], ["recall"], "State bonding, structure and reason for high melting point of solid silicon dioxide."),
    ("2004-jan-chm5-q2aii", "2(a)(ii)", 6, 322, 410, 1, ["3.2.4"], ["recall"], "Write equation for reaction of SiO2, carbon and chlorine to form SiCl4 and CO."),
    ("2004-jan-chm5-q2aiii", "2(a)(iii)", 6, 412, 570, 2, ["3.1.3"], ["recall"], "State bonding in SiCl4 and explain why it has a low melting point."),
    ("2004-jan-chm5-q2b", "2(b)", 6, 572, 775, 3, ["3.2.4"], ["recall"], "Describe observations and equation for reaction when silicon tetrachloride is added to water."),

    # Page 7: Question 3
    ("2004-jan-chm5-q3a", "3(a)", 7, 75, 310, 1, ["3.1.3"], ["recall"], "State type of bonding present in Group II solid chloride B."),
    ("2004-jan-chm5-q3b", "3(b)", 7, 312, 395, 1, ["3.2.2"], ["recall"], "Identify Group II chloride B."),
    ("2004-jan-chm5-q3c", "3(c)", 7, 398, 485, 1, ["3.2.2"], ["recall"], "Write an equation for formation of chloride B from element A."),
    ("2004-jan-chm5-q3d", "3(d)", 7, 488, 575, 1, ["3.2.2"], ["recall"], "Identify white precipitate C formed with aqueous sodium hydroxide."),
    ("2004-jan-chm5-q3e", "3(e)", 7, 578, 665, 1, ["3.2.2"], ["recall"], "Write an equation for reaction in which precipitate C is formed."),
    ("2004-jan-chm5-q3f", "3(f)", 7, 668, 775, 1, ["3.2.2"], ["recall"], "Write an equation for reaction of precipitate C with aqueous sulphuric acid."),

    # Page 8: Question 4(a)-(b)
    ("2004-jan-chm5-q4a", "4(a)", 8, 75, 420, 2, ["3.1.11"], ["recall"], "State hydrogen ion concentration and gas pressure for standard hydrogen electrode."),
    ("2004-jan-chm5-q4b", "4(b)", 8, 422, 775, 3, ["3.1.11"], ["analysis"], "Explain effect of reducing hydrogen ion concentration on electrode potential."),

    # Page 9: Question 4(c)
    ("2004-jan-chm5-q4ci", "4(c)(i)", 9, 75, 530, 1, ["3.1.11"], ["calculation"], "Calculate e.m.f. of electrochemical cell under standard conditions."),
    ("2004-jan-chm5-q4cii", "4(c)(ii)", 9, 532, 775, 3, ["3.1.11"], ["recall"], "Write half-equation at electrode X and overall cell reaction equation."),

    # Page 10: Question 5(a)-(d)
    ("2004-jan-chm5-q5a", "5(a)", 10, 75, 235, 2, ["3.1.3"], ["recall"], "Explain why ammonia is very soluble in water by reference to intermolecular forces."),
    ("2004-jan-chm5-q5bi", "5(b)(i)", 10, 238, 330, 1, ["3.1.12"], ["recall"], "Write an equation for the reaction of ammonia with water."),
    ("2004-jan-chm5-q5bii", "5(b)(ii)", 10, 332, 465, 2, ["3.1.12"], ["recall"], "Explain why pH of 1.0 mol dm-3 ammonia solution is less than 14 at 298 K."),
    ("2004-jan-chm5-q5c", "5(c)", 10, 468, 570, 1, ["3.1.12"], ["recall"], "State what is meant by the term Bronsted-Lowry acid."),
    ("2004-jan-chm5-q5d", "5(d)", 10, 572, 775, 3, ["3.1.12"], ["recall"], "Define buffer solution and identify reagent added to ammonia to form buffer."),

    # Page 11: Question 5(e)
    ("2004-jan-chm5-q5ei", "5(e)(i)", 11, 75, 520, 4, ["3.1.12"], ["calculation"], "Calculate pH of buffer solution of sodium ethanoate and ethanoic acid."),
    ("2004-jan-chm5-q5eii", "5(e)(ii)", 11, 522, 775, 1, ["3.1.12"], ["recall"], "Write ionic equation for small volume of dilute HCl added to buffer solution."),

    # Page 12: Question 6
    ("2004-jan-chm5-q6a", "6(a)", 12, 75, 205, 2, ["3.2.5"], ["recall"], "Explain why complex ions with partially filled d sub-levels are usually coloured."),
    ("2004-jan-chm5-q6bi", "6(b)(i)", 12, 208, 350, 2, ["3.2.6"], ["recall"], "Identify cobalt-containing species in CoSO4(aq) and blue precipitate M."),
    ("2004-jan-chm5-q6bii", "6(b)(ii)", 12, 352, 440, 1, ["3.2.6"], ["recall"], "Identify pale brown cobalt-containing species P formed with excess ammonia."),
    ("2004-jan-chm5-q6biii", "6(b)(iii)", 12, 442, 570, 2, ["3.2.6"], ["recall"], "State type of reaction when P changes into Q and identify reactant responsible."),
    ("2004-jan-chm5-q6biv", "6(b)(iv)", 12, 572, 775, 2, ["3.2.6", "3.1.7"], ["analysis"], "Identify R and explain its formation when acidified KI added to solution of Q.")
]

MS_DATA = {
    "2004-jan-chm5-q1a": {
        "answers": "• &Delta;<i>H</i> = &sum;&Delta;<i>H</i><sub>f</sub>(products) &minus; &sum;&Delta;<i>H</i><sub>f</sub>(reactants) (1)<br>&nbsp;&nbsp;= [0 + 2(&minus;242)] &minus; [4(&minus;92)] (1) = <b>&minus;116 kJ mol<sup>&minus;1</sup></b> (1) [allow max 1 for +116]<br>• &Delta;<i>S</i> = &sum;<i>S</i>(products) &minus; &sum;<i>S</i>(reactants) (1)<br>&nbsp;&nbsp;= [2(223) + 2(189)] &minus; [205 + 4(187)] (1) = <b>&minus;129 J K<sup>&minus;1</sup> mol<sup>&minus;1</sup></b> (1) [allow max 1 for +129]",
        "extra": "",
        "mark": 6,
        "spec": "3.1.8"
    },
    "2004-jan-chm5-q1bi": {
        "answers": "• Effect: <b>equilibrium displaced to right / to products</b> (1)<br>• Explanation: <b>reaction is endothermic</b> (1)<br>(Mark separately). Constraint reduced.",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2004-jan-chm5-q1bii": {
        "answers": "• Feasible when <b>&Delta;<i>G</i> &le; 0</b> (1)<br>• &Delta;<i>G</i> = &Delta;<i>H</i> &minus; <i>T</i>&Delta;<i>S</i> (1)<br>• <i>T</i> = &Delta;<i>H</i>/&Delta;<i>S</i> = (208 &times; 1000) / 253 = <b>822 K</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.8"
    },
    "2004-jan-chm5-q2ai": {
        "answers": "• Type of bonding: <b>covalent</b> (1)<br>• Type of structure: <b>macromolecular / giant covalent</b> (1)<br>• Reason: <b>many strong (covalent) bonds must be broken</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2004-jan-chm5-q2aii": {
        "answers": "<b>SiO<sub>2</sub> + 2Cl<sub>2</sub> + 2C &rarr; SiCl<sub>4</sub> + 2CO</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2004-jan-chm5-q2aiii": {
        "answers": "• Type of bonding: <b>covalent</b> (1)<br>• Reason: <b>weak van der Waals / intermolecular forces between molecules</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2004-jan-chm5-q2b": {
        "answers": "• Observations: <b>white / colourless precipitate or gel</b> (1); <b>vigorous / exothermic reaction OR gas evolved</b> (1)<br>• Equation: <b>SiCl<sub>4</sub> + 4H<sub>2</sub>O &rarr; Si(OH)<sub>4</sub> + 4HCl</b> (1)<br>(<i>OR</i> SiCl<sub>4</sub> + 2H<sub>2</sub>O &rarr; SiO<sub>2</sub> + 4HCl)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.4"
    },
    "2004-jan-chm5-q3a": {
        "answers": "<b>Ionic</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2004-jan-chm5-q3b": {
        "answers": "<b>MgCl<sub>2</sub></b> (1)",
        "extra": "Allow other Group II chlorides except BeCl2.",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm5-q3c": {
        "answers": "<b>Mg + Cl<sub>2</sub> &rarr; MgCl<sub>2</sub></b> (1)",
        "extra": "Conseq to (b).",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm5-q3d": {
        "answers": "<b>Mg(OH)<sub>2</sub></b> (1)",
        "extra": "Only allow this answer.",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm5-q3e": {
        "answers": "<b>MgCl<sub>2</sub> + 2NaOH &rarr; Mg(OH)<sub>2</sub> + 2NaCl</b> (1)",
        "extra": "Allow conseq to hydroxide in (d).",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm5-q3f": {
        "answers": "<b>Mg(OH)<sub>2</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; MgSO<sub>4</sub> + 2H<sub>2</sub>O</b> (1)",
        "extra": "Only allow for MgO or Mg(OH)2.",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm5-q4a": {
        "answers": "• Hydrogen ion concentration: <b>1.00 mol dm<sup>&minus;3</sup></b> (1)<br>• Hydrogen gas pressure: <b>100 kPa</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2004-jan-chm5-q4b": {
        "answers": "• Explanation: <b>equilibrium displaced to left</b> (1) to reduce constraint / oppose decrease (1)<br>• Change in potential: <b>becomes more negative OR decreases</b> (1)",
        "extra": "Allow 'more negative'.",
        "mark": 3,
        "spec": "3.1.11"
    },
    "2004-jan-chm5-q4ci": {
        "answers": "<b>0.43 V</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.11"
    },
    "2004-jan-chm5-q4cii": {
        "answers": "• Half-equation: <b>2Br<sup>&minus;</sup> &rarr; Br<sub>2</sub> + 2e<sup>&minus;</sup></b> (1)<br>• Overall equation: <b>2BrO<sub>3</sub><sup>&minus;</sup> + 10Br<sup>&minus;</sup> + 12H<sup>+</sup> &rarr; 6Br<sub>2</sub> + 6H<sub>2</sub>O</b> (2)<br>[species (1), balanced (1)]<br>(<i>OR</i> BrO<sub>3</sub><sup>&minus;</sup> + 5Br<sup>&minus;</sup> + 6H<sup>+</sup> &rarr; 3Br<sub>2</sub> + 3H<sub>2</sub>O)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.11"
    },
    "2004-jan-chm5-q5a": {
        "answers": "<b>Hydrogen bonding</b> (1) <b>between H<sub>2</sub>O and NH<sub>3</sub></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2004-jan-chm5-q5bi": {
        "answers": "<b>NH<sub>3</sub> + H<sub>2</sub>O &hArr; NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2004-jan-chm5-q5bii": {
        "answers": "Ammonia is a <b>weak base / not partially ionised</b> (1)<br><b>Equilibrium to left</b> or incomplete reaction (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2004-jan-chm5-q5c": {
        "answers": "A <b>proton donor</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2004-jan-chm5-q5d": {
        "answers": "• Buffer solution: A solution which <b>resists change in pH</b> (1) when small amounts of acid or base added or on dilution (1)<br>• Reagent: <b>NH<sub>4</sub>Cl</b> (1) [allow a correct strong acid]",
        "extra": "",
        "mark": 3,
        "spec": "3.1.12"
    },
    "2004-jan-chm5-q5ei": {
        "answers": "• <i>K</i><sub>a</sub> = [H<sup>+</sup>][A<sup>&minus;</sup>] / [HA] (1)<br>• = [H<sup>+</sup>](0.125 &times; 4) / 1.00 (1)<br>• [H<sup>+</sup>] = (1.70 &times; 10<sup>&minus;5</sup>) / (0.125 &times; 4) = 3.40 &times; 10<sup>&minus;5</sup> (1)<br>• pH = &minus;log<sub>10</sub>[H<sup>+</sup>] = <b>4.47</b> (1) [allow pH conseq to [H+], must be 2 decimal places]",
        "extra": "",
        "mark": 4,
        "spec": "3.1.12"
    },
    "2004-jan-chm5-q5eii": {
        "answers": "<b>H<sup>+</sup> + CH<sub>3</sub>COO<sup>&minus;</sup> &rarr; CH<sub>3</sub>COOH</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2004-jan-chm5-q6a": {
        "answers": "Electrons excited / <b>transitions from ground to excited state</b> (1)<br><b>Energy absorbed from visible light / spectrum</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2004-jan-chm5-q6bi": {
        "answers": "• Cobalt-containing species: <b>[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup></b> (1)<br>• Precipitate M: <b>Co(H<sub>2</sub>O)<sub>4</sub>(OH)<sub>2</sub></b> <i>OR</i> <b>Co(OH)<sub>2</sub></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.6"
    },
    "2004-jan-chm5-q6bii": {
        "answers": "<b>[Co(NH<sub>3</sub>)<sub>6</sub>]<sup>2+</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.6"
    },
    "2004-jan-chm5-q6biii": {
        "answers": "• Type of reaction: <b>Co<sup>2+</sup> oxidised to Co<sup>3+</sup></b> / oxidation (1)<br>• Reactant responsible: <b>oxygen / air</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.6"
    },
    "2004-jan-chm5-q6biv": {
        "answers": "• Identity of R: <b>iodine / I<sub>2</sub></b> (1)<br>• Explanation: <b>I<sup>&minus;</sup> oxidised (by Co<sup>3+</sup> which is reduced to Co<sup>2+</sup>)</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.6"
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
        q_img_rel = f"img/2004-jan-chm5/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-jan-chm5/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-jan-chm5",
            "year": 2004,
            "series": "January",
            "code": "CHM5",
            "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
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

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-jan-chm5 ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

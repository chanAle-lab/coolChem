"""
Ingestion script for 2006 January CHM2 (Section A only)
Excludes old-spec Section B essay questions (Q5).
Renders official AQA modern mark scheme tables.
"""
import os
import json
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-jan-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2006-jan-chm2",
    "year": 2006,
    "series": "January",
    "date": "2006-01-11",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(c)
    ("2006-jan-chm2-q1a", "1(a)", 2, 3, ["3.1.4"], ["recall"], "Define the term standard enthalpy of combustion."),
    ("2006-jan-chm2-q1b", "1(b)", 2, 3, ["3.1.4"], ["calculation"], "Calculate standard enthalpy of combustion of propene using bond enthalpy data."),
    ("2006-jan-chm2-q1c", "1(c)", 2, 1, ["3.1.4"], ["recall"], "State why standard enthalpy of formation of oxygen is zero."),

    # Page 5: Question 1(d)-(e)
    ("2006-jan-chm2-q1d", "1(d)", 5, 3, ["3.1.4"], ["calculation"], "Calculate standard enthalpy of combustion of propene using enthalpies of formation."),
    ("2006-jan-chm2-q1e", "1(e)", 5, 2, ["3.1.4"], ["explanation"], "Explain why bond enthalpy calculation is less accurate than formation enthalpy calculation."),

    # Page 6: Question 2
    ("2006-jan-chm2-q2a", "2(a)", 6, 2, ["3.1.5"], ["recall"], "Define the term activation energy."),
    ("2006-jan-chm2-q2b", "2(b)", 6, 1, ["3.1.5"], ["explanation"], "Give one reason why reaction between hydrogen and chlorine is very slow at room temperature."),
    ("2006-jan-chm2-q2c", "2(c)", 6, 2, ["3.1.5"], ["explanation"], "Explain why an increase in pressure increases rate of reaction between hydrogen and chlorine."),
    ("2006-jan-chm2-q2d", "2(d)", 6, 2, ["3.1.5"], ["explanation"], "Explain why a small increase in temperature can lead to a large increase in rate of reaction."),
    ("2006-jan-chm2-q2e", "2(e)", 6, 1, ["3.1.5"], ["recall"], "Give the meaning of the term catalyst."),
    ("2006-jan-chm2-q2f", "2(f)", 6, 1, ["3.1.5"], ["explanation"], "Suggest one reason why a solid catalyst for a gas-phase reaction is often powdered."),

    # Page 7: Question 3
    ("2006-jan-chm2-q3a", "3(a)", 7, 1, ["3.1.7"], ["recall"], "In terms of electrons, give the meaning of the term oxidation."),
    ("2006-jan-chm2-q3b", "3(b)", 7, 6, ["3.1.6"], ["explanation"], "State and explain effect of increase in pressure and temperature on yield of nitrogen monoxide."),
    ("2006-jan-chm2-q3ci", "3(c)(i)", 7, 2, ["3.1.7"], ["recall"], "Deduce the oxidation state of nitrogen in NO and in NO3-."),
    ("2006-jan-chm2-q3cii", "3(c)(ii)", 7, 1, ["3.1.7"], ["recall"], "Write half-equation for reduction of NO3- in acid solution to form NO and water."),
    ("2006-jan-chm2-q3ciii", "3(c)(iii)", 7, 1, ["3.1.7"], ["recall"], "Write half-equation for oxidation of silver metal to Ag+(aq) ions."),
    ("2006-jan-chm2-q3civ", "3(c)(iv)", 7, 1, ["3.1.7"], ["recall"], "Deduce overall equation for reaction between silver metal and nitrate ions in acid solution."),

    # Page 8: Question 4
    ("2006-jan-chm2-q4a", "4(a)", 8, 3, ["3.2.3"], ["explanation"], "State and explain trend in electronegativity of elements down Group VII."),
    ("2006-jan-chm2-q4bi", "4(b)(i)", 8, 1, ["3.2.3"], ["recall"], "State the trend in reducing ability of halide ions down Group VII."),
    ("2006-jan-chm2-q4bii", "4(b)(ii)", 8, 1, ["3.2.3"], ["recall"], "Give an example of a reagent used to show reducing ability of bromide ions differs from chloride ions."),
    ("2006-jan-chm2-q4c", "4(c)", 8, 4, ["3.2.3"], ["recall"], "State observations when silver nitrate followed by dilute aqueous ammonia is added to chloride and bromide ions."),
    ("2006-jan-chm2-q4d", "4(d)", 8, 3, ["3.2.3"], ["recall"], "Write equation for reaction between chlorine and cold dilute NaOH, and give two uses of resulting solution.")
]

MS_DEF = {
    "2006-jan-chm2-q1a": (
        "Enthalpy change / heat energy change when <b>1 mol of a substance</b> (1)<br>"
        "is <b>completely burned in oxygen</b> (1)<br>"
        "at <b>298 K and 100 kPa</b> (or standard conditions) (1)",
        "Not 1 atm.",
        3, "AO1"
    ),
    "2006-jan-chm2-q1b": (
        "&Delta;<i>H</i> = &sum; bonds broken &minus; &sum; bonds formed (1)<br>"
        "= [6(412) + 612 + 348 + 4.5(496)] &minus; [6(743) + 6(463)] (1)<br>"
        "= 5664 &minus; 7236 = <b>&minus;1572 kJ mol<sup>&minus;1</sup></b> (1)",
        "Correct answer scores 3 marks.<br>Units not required but penalise incorrect units.",
        3, "AO2"
    ),
    "2006-jan-chm2-q1c": (
        "By definition, &Delta;<i>H</i><sub>f</sub> is formation from an element (in its standard state)",
        "Allow oxygen is an element in its standard state.",
        1, "AO1"
    ),
    "2006-jan-chm2-q1d": (
        "&Delta;<i>H</i><sub>c</sub> = &sum; &Delta;<i>H</i><sub>f</sub>(products) &minus; &sum; &Delta;<i>H</i><sub>f</sub>(reactants) (1)<br>"
        "= [3(&minus;394) + 3(&minus;242)] &minus; (+20) (1)<br>"
        "= &minus;1182 &minus; 726 &minus; 20 = <b>&minus;1928 kJ mol<sup>&minus;1</sup></b> (1)",
        "Correct answer scores 3 marks.",
        3, "AO2"
    ),
    "2006-jan-chm2-q1e": (
        "Bond enthalpies are <b>mean / average values</b> (1)<br>"
        "taken from a <b>range of compounds / environments</b> (1)",
        "Do not accept just 'they are estimates'.",
        2, "AO1"
    ),
    "2006-jan-chm2-q2a": (
        "<b>Minimum energy</b> (1)<br>"
        "to start a reaction / for a reaction to occur / for a successful collision (1)",
        "Both parts required for 2 marks.",
        2, "AO1"
    ),
    "2006-jan-chm2-q2b": (
        "Activation energy is high / few molecules have sufficient energy to react / breaking bonds needs much energy",
        "Accept very few collisions have <i>E</i> &ge; <i>E</i><sub>a</sub>.",
        1, "AO1"
    ),
    "2006-jan-chm2-q2c": (
        "Molecules / particles are closer together / more particles in a given volume (1)<br>"
        "therefore collide more often / higher collision frequency (1)",
        "Not just 'more collisions'.",
        2, "AO1"
    ),
    "2006-jan-chm2-q2d": (
        "<b>Many more</b> molecules / particles (1)<br>"
        "have energy greater than (or equal to) the activation energy / <i>E</i> &ge; <i>E</i><sub>a</sub> (1)",
        "Quality of Language mark for 'many more'.",
        2, "AO1"
    ),
    "2006-jan-chm2-q2e": (
        "Speeds up a reaction but is chemically unchanged at the end (or not used up)",
        "Accept provides an alternative reaction pathway with a lower activation energy.",
        1, "AO1"
    ),
    "2006-jan-chm2-q2f": (
        "Increases the surface area (giving more active sites for collision)",
        "Accept greater surface area.",
        1, "AO1"
    ),
    "2006-jan-chm2-q3a": (
        "Loss / removal of electrons",
        "OIL RIG.",
        1, "AO1"
    ),
    "2006-jan-chm2-q3b": (
        "<b>Pressure:</b><br>"
        "Effect on yield: <b>no change</b> (1)<br>"
        "Explanation: <b>equal number of gaseous moles</b> on both sides (1), both sides affected equally (1)<br><br>"
        "<b>Temperature:</b><br>"
        "Effect on yield: <b>increases</b> (1)<br>"
        "Explanation: equilibrium shifts to oppose increase in temp / to lower temperature (1), <b>forward reaction is endothermic</b> / endothermic direction favoured (1)",
        "3 marks for pressure, 3 marks for temperature.",
        6, "AO2"
    ),
    "2006-jan-chm2-q3ci": (
        "NO: <b>+2</b> (1)<br>"
        "NO<sub>3</sub><sup>&minus;</sup>: <b>+5</b> (1)",
        "1 mark each. Allow Roman numerals (II, V).",
        2, "AO1"
    ),
    "2006-jan-chm2-q3cii": (
        "NO<sub>3</sub><sup>&minus;</sup> + 4H<sup>+</sup> + 3e<sup>&minus;</sup> &rarr; NO + 2H<sub>2</sub>O",
        "Allow multiples/fractions.",
        1, "AO2"
    ),
    "2006-jan-chm2-q3ciii": (
        "Ag &rarr; Ag<sup>+</sup> + e<sup>&minus;</sup>",
        "Accept Ag &minus; e<sup>&minus;</sup> &rarr; Ag<sup>+</sup>.",
        1, "AO2"
    ),
    "2006-jan-chm2-q3civ": (
        "NO<sub>3</sub><sup>&minus;</sup> + 4H<sup>+</sup> + 3Ag &rarr; NO + 2H<sub>2</sub>O + 3Ag<sup>+</sup>",
        "Balanced equation.",
        1, "AO2"
    ),
    "2006-jan-chm2-q4a": (
        "Trend: <b>decreases</b> (1)<br>"
        "Explanation: Number of shells increases / shielding increases / atomic radius increases (1)<br>"
        "Weaker attraction between nucleus and bonding pair / shared pair of electrons in a covalent bond (1)",
        "3 marks total.",
        3, "AO1"
    ),
    "2006-jan-chm2-q4bi": (
        "<b>Increases</b>",
        "Accept goes up / gets stronger.",
        1, "AO1"
    ),
    "2006-jan-chm2-q4bii": (
        "<b>Concentrated sulphuric acid</b> / conc H<sub>2</sub>SO<sub>4</sub>",
        "Must specify concentrated.",
        1, "AO1"
    ),
    "2006-jan-chm2-q4c": (
        "<b>Chloride ions:</b><br>"
        "white precipitate (1)<br>"
        "soluble / dissolves in dilute ammonia (1)<br><br>"
        "<b>Bromide ions:</b><br>"
        "cream precipitate (1)<br>"
        "partially soluble / insoluble in dilute ammonia (1)",
        "4 marks total: 2 for chloride, 2 for bromide.",
        4, "AO1"
    ),
    "2006-jan-chm2-q4d": (
        "Equation: <b>Cl<sub>2</sub> + 2NaOH &rarr; NaCl + NaOCl + H<sub>2</sub>O</b> (1)<br>"
        "Use 1: <b>bleach</b> (1)<br>"
        "Use 2: <b>disinfectant / steriliser / kills bacteria</b> / water treatment (1)",
        "Allow NaClO for sodium chlorate(I).",
        3, "AO1"
    )
}

def main():
    print("Loading questions.json...")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    db["questions"] = [q for q in db["questions"] if q["paper"] != "2006-jan-chm2"]

    print("Rendering mark scheme images...")
    new_questions = []
    for qid, qnum, page, marks, topics, qtypes, title in QUESTIONS_DEF:
        ans_html, extra_html, ms_marks, ao_spec = MS_DEF[qid]
        ms_fname = f"ms_q{qnum.replace('(', '').replace(')', '')}.jpg"
        ms_rel = f"img/2006-jan-chm2/{ms_fname}"
        ms_abs = os.path.join(REPO_DIR, ms_rel.replace("/", os.sep))

        render_official_markscheme_image(
            question_label=qnum,
            answers_html=ans_html,
            extra_html=extra_html,
            marks=ms_marks,
            spec_ref=ao_spec,
            output_path=ms_abs,
            width_pt=520
        )

        q_img_rel = f"img/2006-jan-chm2/q_q{qnum.replace('(', '').replace(')', '')}.jpg"

        q_obj = {
            "id": qid,
            "paper": "2006-jan-chm2",
            "year": 2006,
            "series": "January",
            "date": "2006-01-11",
            "code": "CHM2",
            "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
            "level": "AS",
            "spec": "AQA Chemistry",
            "question": qnum,
            "page": page,
            "marks": marks,
            "topics": topics,
            "types": qtypes,
            "title": title,
            "image": q_img_rel,
            "markscheme": ms_rel,
            "figures": []
        }
        new_questions.append(q_obj)

    db["questions"].extend(new_questions)

    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully added {len(new_questions)} questions for 2006-jan-chm2 to questions.json!")

if __name__ == "__main__":
    main()

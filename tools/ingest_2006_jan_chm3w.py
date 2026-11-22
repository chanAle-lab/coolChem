"""
Ingestion script for 2006 January CHM3/W (Section A only)
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
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-jan-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2006-jan-chm3w",
    "year": 2006,
    "series": "January",
    "date": "2006-01-11",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(b)
    ("2006-jan-chm3w-q1ai", "1(a)(i)", 2, 2, ["3.3.1"], ["recall"], "State two other characteristics of homologous series."),
    ("2006-jan-chm3w-q1aii", "1(a)(ii)", 2, 1, ["3.3.2"], ["recall"], "Name the process which is used to obtain fractions from petroleum."),
    ("2006-jan-chm3w-q1aiii", "1(a)(iii)", 2, 1, ["3.3.1", "3.3.2"], ["recall"], "State what is meant by the term saturated, as applied to hydrocarbons."),
    ("2006-jan-chm3w-q1bi", "1(b)(i)", 2, 1, ["3.3.1"], ["recall"], "State what is meant by the term molecular formula."),
    ("2006-jan-chm3w-q1bii", "1(b)(ii)", 2, 1, ["3.3.1", "3.3.2"], ["recall"], "Give the molecular formula of the alkane which contains 14 carbon atoms."),
    ("2006-jan-chm3w-q1biii", "1(b)(iii)", 2, 1, ["3.3.2"], ["recall"], "Write an equation for the incomplete combustion of decane to produce carbon and water only."),

    # Page 5: Question 1(c)
    ("2006-jan-chm3w-q1ci", "1(c)(i)", 5, 1, ["3.3.2"], ["recall"], "Write an equation for the reaction between nitrogen and oxygen to form nitrogen monoxide."),
    ("2006-jan-chm3w-q1cii", "1(c)(ii)", 5, 1, ["3.3.2"], ["recall"], "Identify a catalyst used in a catalytic converter."),
    ("2006-jan-chm3w-q1ciii", "1(c)(iii)", 5, 1, ["3.3.2"], ["recall"], "Write an equation showing how nitrogen monoxide is removed in a catalytic converter."),

    # Page 6: Question 2(a)-(b)
    ("2006-jan-chm3w-q2a", "2(a)", 6, 2, ["3.3.4"], ["recall"], "Give a suitable catalyst for Reaction 1 and name compound V."),
    ("2006-jan-chm3w-q2b", "2(b)", 6, 5, ["3.3.4"], ["recall"], "Name and outline a mechanism for Reaction 2 (ethene + conc H2SO4)."),

    # Page 7: Question 2(c)
    ("2006-jan-chm3w-q2ci", "2(c)(i)", 7, 2, ["3.3.5"], ["recall"], "Name compound W and draw its structure."),
    ("2006-jan-chm3w-q2cii", "2(c)(ii)", 7, 1, ["3.3.5"], ["recall"], "Name the type of reaction shown by Reaction 4."),

    # Page 8: Question 3
    ("2006-jan-chm3w-q3ai", "3(a)(i)", 8, 4, ["3.3.2"], ["recall"], "Name type of mechanism and write equations for initiation, first and second propagation steps."),
    ("2006-jan-chm3w-q3aii", "3(a)(ii)", 8, 1, ["3.3.2"], ["recall"], "Write an overall equation for the formation of dichloromethane from chloromethane."),
    ("2006-jan-chm3w-q3b", "3(b)", 8, 3, ["3.1.2"], ["calculation"], "Calculate the molecular formula of compound containing 10.1% C and 89.9% Cl with Mr = 237.0."),
    ("2006-jan-chm3w-q3c", "3(c)", 8, 2, ["3.3.2"], ["recall"], "Suggest formulae of two bromine-containing organic compounds formed from CH2Br2 + Br2."),

    # Page 9: Question 4(a)-(b)
    ("2006-jan-chm3w-q4a", "4(a)", 9, 2, ["3.3.1", "3.3.3"], ["recall"], "Complete table of names and structures of C4H9Br isomers."),
    ("2006-jan-chm3w-q4b", "4(b)", 9, 4, ["3.3.3"], ["recall"], "Name and outline a mechanism for reaction of 2-bromo-2-methylpropane with ethanolic KOH."),

    # Page 10: Question 4(c)-(e)
    ("2006-jan-chm3w-q4ci", "4(c)(i)", 10, 2, ["3.3.1"], ["recall"], "Explain what is meant by the term stereoisomers."),
    ("2006-jan-chm3w-q4cii", "4(c)(ii)", 10, 2, ["3.3.1", "3.3.4"], ["recall"], "Draw structures and give names of the two stereoisomers of but-2-ene."),
    ("2006-jan-chm3w-q4ciii", "4(c)(iii)", 10, 1, ["3.3.1", "3.3.4"], ["recall"], "Name this type of stereoisomerism."),
    ("2006-jan-chm3w-q4d", "4(d)", 10, 1, ["3.3.3"], ["recall"], "State the role of the hydroxide ions in reaction with aqueous potassium hydroxide."),
    ("2006-jan-chm3w-q4e", "4(e)", 10, 3, ["3.3.3"], ["recall"], "Write an equation for reaction of 1-bromobutane with excess ammonia and name organic product.")
]

MS_DEF = {
    "2006-jan-chm3w-q1ai": (
        "Any <b>two</b> from:<br>"
        "&bull; Show a gradation / trend / gradual change in physical properties (or specified property)<br>"
        "&bull; Differ by CH<sub>2</sub><br>"
        "&bull; Chemically similar / react in the same way<br>"
        "&bull; Have the same functional group",
        "Penalise 'same molecular formula'.<br>Penalise 'same empirical formula'.<br>1 mark each, max 2.",
        2, "AO1"
    ),
    "2006-jan-chm3w-q1aii": (
        "<b>Fractional distillation</b> / fractionation",
        "Do not accept distillation alone.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q1aiii": (
        "Contains only single bonds / has no double (or multiple) bonds",
        "Credit 'every carbon is bonded to four other atoms', provided it does not suggest this will always be H.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q1bi": (
        "Gives the <b>actual number of atoms</b> of each element / type in a molecule / compound / formula",
        "Penalise 'amount of atoms' or 'ratio of atoms'.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q1bii": (
        "<b>C<sub>14</sub>H<sub>30</sub></b>",
        "Penalise as contradiction if accompanied by incorrect structural formulae.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q1biii": (
        "C<sub>10</sub>H<sub>22</sub> + 5&frac12;O<sub>2</sub> &rarr; 10C + 11H<sub>2</sub>O",
        "Or double: 2C<sub>10</sub>H<sub>22</sub> + 11O<sub>2</sub> &rarr; 20C + 22H<sub>2</sub>O.",
        1, "AO2"
    ),
    "2006-jan-chm3w-q1ci": (
        "&frac12;N<sub>2</sub> + &frac12;O<sub>2</sub> &rarr; NO",
        "Or N<sub>2</sub> + O<sub>2</sub> &rarr; 2NO.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q1cii": (
        "<b>Platinum</b> <i>or</i> <b>palladium</b> <i>or</i> <b>rhodium</b> (Pt / Pd / Rh)",
        "Allow combination of these.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q1ciii": (
        "2CO + 2NO &rarr; 2CO<sub>2</sub> + N<sub>2</sub><br>"
        "<i>or</i> 2NO &rarr; N<sub>2</sub> + O<sub>2</sub><br>"
        "<i>or</i> C<sub>8</sub>H<sub>18</sub> + 25NO &rarr; 8CO<sub>2</sub> + 12&frac12;N<sub>2</sub> + 9H<sub>2</sub>O",
        "Allow multiples/fractions.<br>Ignore extra O<sub>2</sub> molecules provided equation balances.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q2a": (
        "Catalyst: <b>Ag / silver</b> (or silver-based / silver on alumina) (1)<br>"
        "Compound V: <b>epoxyethane</b> (1)",
        "Penalise specific silver compounds (e.g. AgNO<sub>3</sub>).",
        2, "AO1"
    ),
    "2006-jan-chm3w-q2b": (
        "Name of mechanism: <b>electrophilic addition</b> (1)<br><br>"
        "<b>Mechanism:</b><br>"
        "M1: curly arrow from C=C bond to H atom on H&mdash;OSO<sub>2</sub>OH (1)<br>"
        "M2: curly arrow from H&mdash;O bond to O atom on H&mdash;OSO<sub>2</sub>OH (1)<br>"
        "M3: correct carbocation structure CH<sub>3</sub>CH<sub>2</sub><sup>+</sup> (1)<br>"
        "M4: curly arrow from lone pair on O of <sup>&minus;</sup>OSO<sub>2</sub>OH to C<sup>+</sup> (1)",
        "Penalise M1 if arrow to H<sub>2</sub>SO<sub>4</sub> or to formal charge.<br>Penalise use of 'sticks' in carbocation.<br>Insist on lone pair and negative charge on hydrogensulphate ion.",
        5, "AO2"
    ),
    "2006-jan-chm3w-q2ci": (
        "Name: <b>ethanal</b> (1)<br>"
        "Structure: <b>CH<sub>3</sub>&mdash;C(=O)&mdash;H</b> (1)",
        "Aldehyde functional group &mdash;CHO must be drawn out showing C=O and C&mdash;H.",
        2, "AO1"
    ),
    "2006-jan-chm3w-q2cii": (
        "<b>Oxidation</b> / redox",
        "Accept oxidation.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q3ai": (
        "Type of mechanism: <b>(free-)radical substitution</b> (1)<br>"
        "Initiation: <b>Cl<sub>2</sub> &rarr; 2Cl&bull;</b> (1)<br>"
        "First propagation: <b>CH<sub>3</sub>Cl + Cl&bull; &rarr; &bull;CH<sub>2</sub>Cl + HCl</b> (1)<br>"
        "Second propagation: <b>&bull;CH<sub>2</sub>Cl + Cl<sub>2</sub> &rarr; CH<sub>2</sub>Cl<sub>2</sub> + Cl&bull;</b> (1)",
        "Both words required for mechanism name.<br>Penalise double-headed arrows in initiation.<br>Penalise absence of radical dots once only.",
        4, "AO1"
    ),
    "2006-jan-chm3w-q3aii": (
        "CH<sub>3</sub>Cl + Cl<sub>2</sub> &rarr; CH<sub>2</sub>Cl<sub>2</sub> + HCl",
        "Penalise if any radicals appear in this overall equation.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q3b": (
        "mol C = 10.1 / 12.0 = 0.842 &nbsp;and&nbsp; mol Cl = 89.9 / 35.5 = 2.53 (1)<br>"
        "Ratio = 0.842 : 2.53 &rarr; 1 : 3 &rarr; empirical formula = <b>CCl<sub>3</sub></b> (1)<br>"
        "237.0 / <i>M</i><sub>r</sub>(CCl<sub>3</sub>) = 237.0 / 118.5 = 2 &rarr; <b>C<sub>2</sub>Cl<sub>6</sub></b> (1)",
        "Correct answer gains full credit (3 marks).<br>Alternative: C = 237 &times; 0.101 = 23.9 g (2 mol); Cl = 237 &times; 0.899 = 213 g (6 mol) &rarr; C<sub>2</sub>Cl<sub>6</sub>.",
        3, "AO2"
    ),
    "2006-jan-chm3w-q3c": (
        "Any <b>two</b> from:<br>"
        "<b>CHBr<sub>3</sub></b> <i>or</i> <b>CBr<sub>4</sub></b> <i>or</i> <b>C<sub>2</sub>H<sub>2</sub>Br<sub>4</sub></b> (CHBr<sub>2</sub>CHBr<sub>2</sub>) <i>or</i> <b>C<sub>2</sub>Br<sub>6</sub></b> (CBr<sub>3</sub>CBr<sub>3</sub>)",
        "Ignore HBr or H<sub>2</sub>.<br>Penalise names alone; formulae required.",
        2, "AO2"
    ),
    "2006-jan-chm3w-q4a": (
        "Row 1 name: <b>1-bromobutane</b> (1)<br>"
        "Row 3 structure: <b>(CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>Br</b> (drawn out clearly showing C&mdash;C bonds) (1)",
        "Allow 1-bromo butane.<br>C&mdash;C bonds must be clear.",
        2, "AO1"
    ),
    "2006-jan-chm3w-q4b": (
        "Name of mechanism: <b>(base) elimination</b> (1)<br><br>"
        "<b>Mechanism:</b><br>"
        "M1: curly arrow from lone pair on :OH<sup>&minus;</sup> to H atom on CH<sub>3</sub> group (1)<br>"
        "M2: curly arrow from middle of C&mdash;H bond to middle of C&mdash;C bond (1)<br>"
        "M3: curly arrow from middle of C&mdash;Br bond towards/alongside Br atom (1)",
        "Penalise other words before 'elimination' e.g. nucleophilic.<br>Insist on lone pair and negative charge on hydroxide ion.<br>Credit full marks for correct E1 mechanism.",
        4, "AO2"
    ),
    "2006-jan-chm3w-q4ci": (
        "Compounds with the <b>same structural formula</b> (1)<br>"
        "but the bonds / atoms / groups have <b>different spatial arrangements / orientation in space</b> (1)",
        "Ignore reference to same molecular formula for M1.",
        2, "AO1"
    ),
    "2006-jan-chm3w-q4cii": (
        "<b>cis-but-2-ene:</b> both CH<sub>3</sub> on same side of C=C (1)<br>"
        "<b>trans-but-2-ene:</b> CH<sub>3</sub> on opposite sides of C=C (1)",
        "Award 1 mark for two correct structures with either wrong or no names.<br>Must clearly show planar C=C geometry.",
        2, "AO1"
    ),
    "2006-jan-chm3w-q4ciii": (
        "<b>Geometric(al)</b> <i>or</i> <b>cis-trans</b>",
        "Accept E-Z.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q4d": (
        "<b>Nucleophile</b> / electron pair donor",
        "Penalise 'base'.",
        1, "AO1"
    ),
    "2006-jan-chm3w-q4e": (
        "Equation: <b>CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>Br + 2NH<sub>3</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> + NH<sub>4</sub>Br</b> (2)<br>"
        "Name of product: <b>(1-)butylamine</b> <i>or</i> <b>1-aminobutane</b> (1)",
        "M1 for correct product (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>), M2 for balanced equation using 2NH<sub>3</sub>.<br>Award QoL mark for correct spelling of butylamine/aminobutane.",
        3, "AO1"
    )
}

def main():
    print("Loading questions.json...")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    db["questions"] = [q for q in db["questions"] if q["paper"] != "2006-jan-chm3w"]

    print("Rendering mark scheme images...")
    new_questions = []
    for qid, qnum, page, marks, topics, qtypes, title in QUESTIONS_DEF:
        ans_html, extra_html, ms_marks, ao_spec = MS_DEF[qid]
        ms_fname = f"ms_q{qnum.replace('(', '').replace(')', '')}.jpg"
        ms_rel = f"img/2006-jan-chm3w/{ms_fname}"
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

        q_img_rel = f"img/2006-jan-chm3w/q_q{qnum.replace('(', '').replace(')', '')}.jpg"

        # Figures for Q2
        figs = []
        if qnum in ["2(b)", "2(c)(i)", "2(c)(ii)"]:
            figs = ["img/2006-jan-chm3w/fig-q2-scheme.jpg"]

        q_obj = {
            "id": qid,
            "paper": "2006-jan-chm3w",
            "year": 2006,
            "series": "January",
            "date": "2006-01-11",
            "code": "CHM3/W",
            "unit": "Unit 3(a): Introduction to Organic Chemistry",
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
            "figures": figs
        }
        new_questions.append(q_obj)

    db["questions"].extend(new_questions)

    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully added {len(new_questions)} questions for 2006-jan-chm3w to questions.json!")

if __name__ == "__main__":
    main()

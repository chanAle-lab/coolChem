"""
Ingestion script for 2006 January CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q7, Q8).
Renders official AQA modern mark scheme tables.
"""
import os
import json
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-jan-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2006-jan-chm4",
    "year": 2006,
    "series": "January",
    "date": "2006-01-23",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A2",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 minutes"
}

QUESTIONS_DEF = [
    # Page 5: Question 1
    ("2006-jan-chm4-q1a", "1(a)", 5, 3, ["3.1.9"], ["calculation"], "Complete the table of rate data for the reaction between NO and H2."),
    ("2006-jan-chm4-q1b", "1(b)", 5, 3, ["3.1.9"], ["calculation"], "Calculate a value for the rate constant k and state its units using experiment 1."),

    # Page 6: Question 2(a) & 2(b)(i)
    ("2006-jan-chm4-q2ai", "2(a)(i)", 6, 2, ["3.1.12"], ["recall"], "Write expressions for the ionic product of water, Kw, and for pH."),
    ("2006-jan-chm4-q2aii", "2(a)(ii)", 6, 1, ["3.1.12"], ["explanation"], "State why pure water is not acidic at 318 K where pH is 6.70."),
    ("2006-jan-chm4-q2aiii", "2(a)(iii)", 6, 1, ["3.1.12"], ["calculation"], "Calculate moles of NaOH in 2.00 cm3 of 0.500 mol dm-3 aqueous NaOH."),
    ("2006-jan-chm4-q2aiv", "2(a)(iv)", 6, 2, ["3.1.12"], ["calculation"], "Calculate pH of solution formed when NaOH is added to pure water at 318 K."),
    ("2006-jan-chm4-q2bi", "2(b)(i)", 6, 1, ["3.1.12"], ["recall"], "Write an expression for Ka for propanoic acid."),

    # Page 7: Question 2(b)(ii) & 2(c)
    ("2006-jan-chm4-q2bii", "2(b)(ii)", 7, 3, ["3.1.12"], ["calculation"], "Calculate pH of 0.125 mol dm-3 aqueous propanoic acid at 298 K."),
    ("2006-jan-chm4-q2ci", "2(c)(i)", 7, 1, ["3.1.12"], ["calculation"], "Calculate moles of propanoic acid in 50.0 cm3 of 0.125 mol dm-3 propanoic acid."),
    ("2006-jan-chm4-q2cii", "2(c)(ii)", 7, 1, ["3.1.12"], ["calculation"], "Calculate moles of propanoic acid remaining in buffer solution."),
    ("2006-jan-chm4-q2ciii", "2(c)(iii)", 7, 4, ["3.1.12"], ["calculation"], "Hence calculate pH of this buffer solution at 298 K."),

    # Page 8: Question 3(a) & 3(b)(i)-(ii)
    ("2006-jan-chm4-q3ai", "3(a)(i)", 8, 1, ["3.1.10"], ["recall"], "Write an equation for the forward reaction from the given Kc expression."),
    ("2006-jan-chm4-q3aii", "3(a)(ii)", 8, 1, ["3.1.10"], ["calculation"], "Deduce the units of Kc."),
    ("2006-jan-chm4-q3aiii", "3(a)(iii)", 8, 1, ["3.1.10"], ["explanation"], "State what can be deduced from Kc being larger at lower temperature."),
    ("2006-jan-chm4-q3bi", "3(b)(i)", 8, 2, ["3.1.2"], ["calculation"], "Calculate the number of moles of N2O4 in 36.8 g sample."),
    ("2006-jan-chm4-q3bii", "3(b)(ii)", 8, 2, ["3.1.10"], ["calculation"], "Calculate the number of moles of NO2 in the equilibrium mixture."),

    # Page 9: Question 3(b)(iii)-(iv)
    ("2006-jan-chm4-q3biii", "3(b)(iii)", 9, 3, ["3.1.10"], ["calculation"], "Write expression for Kc and calculate its value under these conditions."),
    ("2006-jan-chm4-q3biv", "3(b)(iv)", 9, 2, ["3.1.10"], ["explanation"], "State effect of using larger flask on position of equilibrium and value of Kc."),

    # Page 10: Question 4(a)-(b)
    ("2006-jan-chm4-q4a", "4(a)", 10, 5, ["3.3.8"], ["recall"], "Name and outline a mechanism for Reaction 1 (propanal + HCN)."),
    ("2006-jan-chm4-q4bi", "4(b)(i)", 10, 1, ["3.3.8"], ["recall"], "Name compound Q."),
    ("2006-jan-chm4-q4bii", "4(b)(ii)", 10, 2, ["3.3.1", "3.3.9"], ["recall"], "Draw structure of isomer of Q showing geometrical isomerism formed from ammonia and acyl chloride."),

    # Page 11: Question 4(c)
    ("2006-jan-chm4-q4ci", "4(c)(i)", 11, 1, ["3.3.9"], ["recall"], "Draw structure of product when R reacts with methanol in presence of conc H2SO4."),
    ("2006-jan-chm4-q4cii", "4(c)(ii)", 11, 1, ["3.3.5", "3.3.9"], ["recall"], "Draw structure of product when R reacts with acidified potassium dichromate(VI)."),
    ("2006-jan-chm4-q4ciii", "4(c)(iii)", 11, 1, ["3.3.5", "3.3.9"], ["recall"], "Draw structure of product when R reacts with conc H2SO4 in an elimination reaction."),

    # Page 12: Question 5
    ("2006-jan-chm4-q5a", "5(a)", 12, 1, ["3.3.11"], ["recall"], "Name the compound (CH3)2NH."),
    ("2006-jan-chm4-q5b", "5(b)", 12, 5, ["3.3.11"], ["recall"], "Name and outline a mechanism for reaction of excess CH3NH2 with CH3Br."),
    ("2006-jan-chm4-q5c", "5(c)", 12, 2, ["3.3.11"], ["recall"], "Name type of compound formed with large excess of CH3Br and give a use."),
    ("2006-jan-chm4-q5d", "5(d)", 12, 2, ["3.3.9", "3.3.11"], ["recall"], "Draw structures of two compounds formed in reaction of CH3NH2 with ethanoic anhydride."),

    # Page 13: Question 6
    ("2006-jan-chm4-q6a", "6(a)", 13, 2, ["3.3.12"], ["recall"], "Name type of polymer and type of polymerisation shown by repeating unit."),
    ("2006-jan-chm4-q6b", "6(b)", 13, 1, ["3.3.13"], ["recall"], "Draw structure of species present in solid aminoethanoic acid."),
    ("2006-jan-chm4-q6c", "6(c)", 13, 2, ["3.3.13"], ["explanation"], "Explain why melting point of aminoethanoic acid is much higher than hydroxyethanoic acid.")
]

MS_DEF = {
    "2006-jan-chm4-q1a": (
        "Experiment 2: <b>4.0 &times; 10<sup>&minus;3</sup></b> (1)<br>"
        "Experiment 3: <b>0.45 &times; 10<sup>&minus;5</sup></b> (<i>or</i> 4.5 &times; 10<sup>&minus;6</sup>) (1)<br>"
        "Experiment 4: <b>9.0 &times; 10<sup>&minus;3</sup></b> (1)",
        "1 mark each.",
        3, "AO2"
    ),
    "2006-jan-chm4-q1b": (
        "<i>k</i> = rate / ([NO]<sup>2</sup>[H<sub>2</sub>])<br>"
        "= (1.8 &times; 10<sup>&minus;5</sup>) / [(3.0 &times; 10<sup>&minus;3</sup>)<sup>2</sup> &times; (1.0 &times; 10<sup>&minus;3</sup>)] (1)<br>"
        "= <b>2000</b> (1)<br>"
        "Units: <b>mol<sup>&minus;2</sup> dm<sup>6</sup> s<sup>&minus;1</sup></b> (1)",
        "Allow consequential units on wrong rate equation if used.<br>Correct answer scores all 3 marks.",
        3, "AO2"
    ),
    "2006-jan-chm4-q2ai": (
        "<i>K</i><sub>w</sub> = <b>[H<sup>+</sup>][OH<sup>&minus;</sup>]</b> (1)<br>"
        "pH = <b>&minus;log<sub>10</sub>[H<sup>+</sup>]</b> (1)",
        "Allow &minus;log[H<sup>+</sup>].<br>Must have square brackets.",
        2, "AO1"
    ),
    "2006-jan-chm4-q2aii": (
        "<b>[H<sup>+</sup>] = [OH<sup>&minus;</sup>]</b>",
        "Concentration of H<sup>+</sup> equals concentration of OH<sup>&minus;</sup>.",
        1, "AO1"
    ),
    "2006-jan-chm4-q2aiii": (
        "moles NaOH = (2.00 &times; 10<sup>&minus;3</sup>) &times; 0.500 = <b>1.0 &times; 10<sup>&minus;3</sup> mol</b>",
        "Accept 0.001 mol.",
        1, "AO2"
    ),
    "2006-jan-chm4-q2aiv": (
        "[OH<sup>&minus;</sup>] = 1.0 &times; 10<sup>&minus;3</sup> / 1.00 = 1.0 &times; 10<sup>&minus;3</sup> mol dm<sup>&minus;3</sup><br>"
        "[H<sup>+</sup>] = <i>K</i><sub>w</sub> / [OH<sup>&minus;</sup>] = (4.02 &times; 10<sup>&minus;14</sup>) / (1.0 &times; 10<sup>&minus;3</sup>) = 4.02 &times; 10<sup>&minus;11</sup> mol dm<sup>&minus;3</sup> (1)<br>"
        "pH = &minus;log(4.02 &times; 10<sup>&minus;11</sup>) = <b>10.40</b> (1)",
        "Must be 2 decimal places.<br>Consequential on answer to (a)(iii).",
        2, "AO2"
    ),
    "2006-jan-chm4-q2bi": (
        "<i>K</i><sub>a</sub> = <b>[H<sup>+</sup>][CH<sub>3</sub>CH<sub>2</sub>COO<sup>&minus;</sup>] / [CH<sub>3</sub>CH<sub>2</sub>COOH]</b>",
        "Square brackets required.",
        1, "AO1"
    ),
    "2006-jan-chm4-q2bii": (
        "<i>K</i><sub>a</sub> &approx; [H<sup>+</sup>]<sup>2</sup> / [CH<sub>3</sub>CH<sub>2</sub>COOH] (1)<br>"
        "[H<sup>+</sup>] = &radic;(1.35 &times; 10<sup>&minus;5</sup> &times; 0.125) = 1.30 &times; 10<sup>&minus;3</sup> mol dm<sup>&minus;3</sup> (1)<br>"
        "pH = &minus;log(1.30 &times; 10<sup>&minus;3</sup>) = <b>2.89</b> (1)",
        "Must be 2 decimal places.<br>Correct answer scores 3 marks.",
        3, "AO2"
    ),
    "2006-jan-chm4-q2ci": (
        "moles propanoic acid = (50.0 &times; 10<sup>&minus;3</sup>) &times; 0.125 = <b>6.25 &times; 10<sup>&minus;3</sup> mol</b>",
        "Accept 0.00625 mol.",
        1, "AO2"
    ),
    "2006-jan-chm4-q2cii": (
        "moles remaining = (6.25 &times; 10<sup>&minus;3</sup>) &minus; (1.0 &times; 10<sup>&minus;3</sup>) = <b>5.25 &times; 10<sup>&minus;3</sup> mol</b>",
        "Consequential on (a)(iii) and (c)(i).",
        1, "AO2"
    ),
    "2006-jan-chm4-q2ciii": (
        "moles salt formed = 1.0 &times; 10<sup>&minus;3</sup> mol (1)<br>"
        "[H<sup>+</sup>] = <i>K</i><sub>a</sub> &times; [acid] / [salt] (1)<br>"
        "[H<sup>+</sup>] = (1.35 &times; 10<sup>&minus;5</sup>) &times; (5.25 &times; 10<sup>&minus;3</sup> / <i>V</i>) / (1.0 &times; 10<sup>&minus;3</sup> / <i>V</i>) = 7.088 &times; 10<sup>&minus;5</sup> (1)<br>"
        "pH = &minus;log(7.088 &times; 10<sup>&minus;5</sup>) = <b>4.15</b> (1)",
        "Must be 2 decimal places.<br>Volumes cancel.",
        4, "AO2"
    ),
    "2006-jan-chm4-q3ai": (
        "<b>C + 3D &rarr; 2A + B</b>",
        "Or multiples.",
        1, "AO1"
    ),
    "2006-jan-chm4-q3aii": (
        "<b>mol dm<sup>&minus;3</sup></b>",
        "Accept (mol dm<sup>&minus;3</sup>)<sup>1</sup>.",
        1, "AO1"
    ),
    "2006-jan-chm4-q3aiii": (
        "The forward reaction is <b>exothermic</b> (or more products formed at lower temp)",
        "Accept &Delta;<i>H</i> is negative for forward reaction.",
        1, "AO1"
    ),
    "2006-jan-chm4-q3bi": (
        "<i>M</i><sub>r</sub>(N<sub>2</sub>O<sub>4</sub>) = 92.0 (1)<br>"
        "moles = 36.8 / 92.0 = <b>0.400 mol</b> (1)",
        "2 marks total.",
        2, "AO2"
    ),
    "2006-jan-chm4-q3bii": (
        "moles N<sub>2</sub>O<sub>4</sub> reacted = 0.400 &minus; 0.180 = 0.220 mol (1)<br>"
        "moles NO<sub>2</sub> formed = 2 &times; 0.220 = <b>0.440 mol</b> (1)",
        "Consequential on (b)(i).",
        2, "AO2"
    ),
    "2006-jan-chm4-q3biii": (
        "<i>K</i><sub>c</sub> = [NO<sub>2</sub>]<sup>2</sup> / [N<sub>2</sub>O<sub>4</sub>] (1)<br>"
        "= (0.440 / 16.0)<sup>2</sup> / (0.180 / 16.0) (1)<br>"
        "= <b>0.067</b> (mol dm<sup>&minus;3</sup>) (1)",
        "Accept 0.0672.<br>3 marks total.",
        3, "AO2"
    ),
    "2006-jan-chm4-q3biv": (
        "Effect on position of equilibrium: <b>shifts to the right / towards NO<sub>2</sub> / forwards</b> (1)<br>"
        "Effect on value of <i>K</i><sub>c</sub>: <b>none / no change / unchanged</b> (1)",
        "2 marks total.",
        2, "AO1"
    ),
    "2006-jan-chm4-q4a": (
        "Name of mechanism: <b>nucleophilic addition</b> (1)<br><br>"
        "<b>Mechanism:</b><br>"
        "M1: curly arrow from lone pair on :CN<sup>&minus;</sup> to carbonyl carbon (1)<br>"
        "M2: curly arrow from C=O bond to oxygen atom (1)<br>"
        "M3: correct structure of tetrahedral intermediate with negative charge on oxygen (1)<br>"
        "M4: curly arrow from lone pair on O<sup>&minus;</sup> to H<sup>+</sup> (or H of HCN) (1)",
        "Penalise M1 if arrow originates from formal charge or from N.",
        5, "AO2"
    ),
    "2006-jan-chm4-q4bi": (
        "<b>2-hydroxybutanenitrile</b>",
        "Allow 2-hydroxybutane-1-nitrile.",
        1, "AO1"
    ),
    "2006-jan-chm4-q4bii": (
        "<b>CH<sub>3</sub>CH=CHCONH<sub>2</sub></b><br>"
        "drawn clearly showing <i>cis</i> or <i>trans</i> geometry around C=C and the &mdash;CONH<sub>2</sub> group",
        "Allow 1 mark for amide structure (RCONH<sub>2</sub>) even if not C<sub>4</sub>H<sub>7</sub>NO.<br>If not amide, allow 1 mark for any isomer of C<sub>4</sub>H<sub>7</sub>NO showing geometric isomerism.",
        2, "AO2"
    ),
    "2006-jan-chm4-q4ci": (
        "<b>CH<sub>3</sub>CH<sub>2</sub>CH(OH)COOCH<sub>3</sub></b><br>"
        "(methyl 2-hydroxybutanoate)",
        "Structure must be correct.",
        1, "AO1"
    ),
    "2006-jan-chm4-q4cii": (
        "<b>CH<sub>3</sub>CH<sub>2</sub>COCOOH</b><br>"
        "(2-oxobutanoic acid)",
        "Secondary alcohol oxidised to ketone.",
        1, "AO1"
    ),
    "2006-jan-chm4-q4ciii": (
        "<b>CH<sub>3</sub>CH=CHCOOH</b><br>"
        "(but-2-enoic acid)",
        "Acid-catalysed dehydration/elimination of alcohol.",
        1, "AO1"
    ),
    "2006-jan-chm4-q5a": (
        "<b>dimethylamine</b>",
        "Allow N-methylmethanamine.",
        1, "AO1"
    ),
    "2006-jan-chm4-q5b": (
        "Name of mechanism: <b>nucleophilic substitution</b> (1)<br><br>"
        "<b>Mechanism:</b><br>"
        "M1: curly arrow from lone pair on N of CH<sub>3</sub>NH<sub>2</sub> to carbon of CH<sub>3</sub>Br (1)<br>"
        "M2: curly arrow from C&mdash;Br bond to Br atom (1)<br>"
        "M3: correct intermediate (CH<sub>3</sub>)<sub>2</sub>NH<sub>2</sub><sup>+</sup> (1)<br>"
        "M4: curly arrow from lone pair on second CH<sub>3</sub>NH<sub>2</sub> (or Br<sup>&minus;</sup>) to H on N<sup>+</sup> (1)",
        "5 marks total.",
        5, "AO2"
    ),
    "2006-jan-chm4-q5c": (
        "Type of compound: <b>quaternary ammonium salt</b> (1)<br>"
        "Use: <b>(cationic) surfactant / bactericide / detergent / fabric softener / hair conditioner</b> (1)",
        "2 marks total.",
        2, "AO1"
    ),
    "2006-jan-chm4-q5d": (
        "<b>CH<sub>3</sub>CONHCH<sub>3</sub></b> (N-methylacetamide / N-methylethanamide) (1)<br>"
        "<b>CH<sub>3</sub>COOH</b> (ethanoic acid) <i>or</i> <b>CH<sub>3</sub>COO<sup>&minus;</sup>CH<sub>3</sub>NH<sub>3</sub><sup>+</sup></b> (methylammonium ethanoate) (1)",
        "2 marks total.",
        2, "AO2"
    ),
    "2006-jan-chm4-q6a": (
        "Type of polymer: <b>polyamide</b> <i>or</i> <b>nylon (2,4)</b> (1)<br>"
        "Type of polymerisation: <b>condensation</b> (1)",
        "Allow nylon without numbers, but if numbers are present they must be correct (2,4).",
        2, "AO1"
    ),
    "2006-jan-chm4-q6b": (
        "<b><sup>+</sup>H<sub>3</sub>N&mdash;CH<sub>2</sub>&mdash;COO<sup>&minus;</sup></b>",
        "Zwitterion structure.",
        1, "AO1"
    ),
    "2006-jan-chm4-q6c": (
        "<b>Ionic bonding / ionic lattice</b> in aminoethanoic acid (1)<br>"
        "<b>Stronger attractions / electrostatic forces</b> than the hydrogen bonding in hydroxyethanoic acid (1)",
        "Must specify that aminoethanoic acid is ionic / has ionic bonding.",
        2, "AO1"
    )
}

def main():
    print("Loading questions.json...")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    db["questions"] = [q for q in db["questions"] if q["paper"] != "2006-jan-chm4"]

    print("Rendering mark scheme images...")
    new_questions = []
    for qid, qnum, page, marks, topics, qtypes, title in QUESTIONS_DEF:
        ans_html, extra_html, ms_marks, ao_spec = MS_DEF[qid]
        ms_fname = f"ms_q{qnum.replace('(', '').replace(')', '')}.jpg"
        ms_rel = f"img/2006-jan-chm4/{ms_fname}"
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

        q_img_rel = f"img/2006-jan-chm4/q_q{qnum.replace('(', '').replace(')', '')}.jpg"

        # Figures for Q4
        figs = []
        if qnum in ["4(b)(i)", "4(b)(ii)", "4(c)(i)", "4(c)(ii)", "4(c)(iii)"]:
            figs = ["img/2006-jan-chm4/fig-q4-scheme.jpg"]

        q_obj = {
            "id": qid,
            "paper": "2006-jan-chm4",
            "year": 2006,
            "series": "January",
            "date": "2006-01-23",
            "code": "CHM4",
            "unit": "Unit 4: Further Physical and Organic Chemistry",
            "level": "A2",
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

    print(f"Successfully added {len(new_questions)} questions for 2006-jan-chm4 to questions.json!")

if __name__ == "__main__":
    main()

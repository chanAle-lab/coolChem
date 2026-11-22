"""
Ingestion script for 2006 January CHM1 (Section A only)
Excludes old-spec Section B essay questions (Q5, Q6).
Renders official AQA modern mark scheme tables.
"""
import os
import json
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-jan-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2006-jan-chm1",
    "year": 2006,
    "series": "January",
    "date": "2006-01-11",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2006-jan-chm1-q1a", "1(a)", 2, 2, ["3.1.1"], ["recall"], "Complete the table showing relative mass and charge of neutron and electron."),
    ("2006-jan-chm1-q1b", "1(b)", 2, 2, ["3.1.1"], ["calculation", "recall"], "Deduce symbol, including mass number, of atom with twice protons and four more neutrons than 9Be."),
    ("2006-jan-chm1-q1c", "1(c)", 2, 4, ["3.1.3"], ["recall"], "Draw shapes of BeCl2 and Cl2O, show lone pairs on central atom, and name shapes."),
    ("2006-jan-chm1-q1d", "1(d)", 2, 4, ["3.1.2"], ["calculation"], "Calculate volume in cm3 of 1.00 mol dm-3 HCl required to react with 1.00 g Mg(OH)2."),

    # Page 5: Question 2
    ("2006-jan-chm1-q2ai", "2(a)(i)", 5, 1, ["3.1.2"], ["calculation"], "Calculate number of moles of KNO3 in 1.00 g sample."),
    ("2006-jan-chm1-q2aii", "2(a)(ii)", 5, 4, ["3.1.2"], ["calculation"], "State ideal gas equation and calculate moles of oxygen produced."),
    ("2006-jan-chm1-q2bi", "2(b)(i)", 5, 1, ["3.1.2"], ["recall"], "State what is meant by the term empirical formula."),
    ("2006-jan-chm1-q2bii", "2(b)(ii)", 5, 3, ["3.1.2"], ["calculation"], "Calculate empirical formula of Y from percentage composition."),
    ("2006-jan-chm1-q2c", "2(c)", 5, 1, ["3.1.2"], ["recall"], "Deduce equation for decomposition of KNO3 into Y and oxygen."),

    # Page 6: Question 3
    ("2006-jan-chm1-q3a", "3(a)", 6, 2, ["3.1.3"], ["recall"], "Define the term electronegativity."),
    ("2006-jan-chm1-q3bi", "3(b)(i)", 6, 3, ["3.1.3"], ["recall"], "Name the strongest intermolecular force present in liquid F2, CH3F, and HF."),
    ("2006-jan-chm1-q3bii", "3(b)(ii)", 6, 3, ["3.1.3"], ["explanation"], "Explain how the strongest type of intermolecular force in liquid HF arises."),

    # Page 7: Question 3(c)
    ("2006-jan-chm1-q3ci", "3(c)(i)", 7, 2, ["3.1.3"], ["explanation"], "Explain the trend in boiling points of hydrogen halides from HCl to HI."),
    ("2006-jan-chm1-q3cii", "3(c)(ii)", 7, 1, ["3.1.3"], ["explanation"], "Give one reason why boiling point of HF is higher than all other hydrogen halides."),

    # Page 8: Question 4
    ("2006-jan-chm1-q4a", "4(a)", 8, 2, ["3.1.1"], ["recall"], "State the meaning of the term first ionisation energy of an atom."),
    ("2006-jan-chm1-q4b", "4(b)", 8, 1, ["3.1.1"], ["recall"], "Complete electron arrangement for Mg2+ ion."),
    ("2006-jan-chm1-q4c", "4(c)", 8, 1, ["3.1.1", "3.2.1"], ["recall"], "Identify the block in the Periodic Table to which magnesium belongs."),
    ("2006-jan-chm1-q4d", "4(d)", 8, 1, ["3.1.1"], ["recall"], "Write equation illustrating second ionisation energy of magnesium."),
    ("2006-jan-chm1-q4e", "4(e)", 8, 2, ["3.1.1"], ["explanation"], "Give two reasons why first IE of neon is lower than third IE of magnesium."),

    # Page 9: Question 4(f)
    ("2006-jan-chm1-q4fi", "4(f)(i)", 9, 3, ["3.1.1", "3.2.1"], ["explanation"], "State and explain general trend in first ionisation energies of Period 3 elements, Na-Ar."),
    ("2006-jan-chm1-q4fii", "4(f)(ii)", 9, 2, ["3.1.1", "3.2.1"], ["explanation"], "Explain why first ionisation energy of sulphur is lower than predicted from general trend.")
]

MS_DEF = {
    "2006-jan-chm1-q1a": (
        "neutron: relative mass = 1, relative charge = 0<br>"
        "electron: relative mass = 1/1800 &rarr; 0 / negligible <i>or</i> 5.56 &times; 10<sup>&minus;4</sup> &rarr; 0, relative charge = &minus;1",
        "Do not accept 'neutral' for charge of neutron.<br>1 mark each for neutron and electron.",
        2, "AO1"
    ),
    "2006-jan-chm1-q1b": (
        "<sup>17</sup>O / O<sup>17</sup><br>"
        "mass number = 17<br>"
        "symbol: O",
        "Do not accept 17.0.<br>If 'O' + 'mass number = 17' award 1 mark.<br>If atomic number given but &ne; 8, treat as contradiction.",
        2, "AO2"
    ),
    "2006-jan-chm1-q1c": (
        "<b>BeCl<sub>2</sub>:</b><br>"
        "Cl&mdash;Be&mdash;Cl<br>"
        "shape: <b>linear</b><br><br>"
        "<b>Cl<sub>2</sub>O:</b><br>"
        "V-shaped / bent / angular with 2 lone pairs on O<br>"
        "shape: <b>bent / V-shaped / angular</b>",
        "1 mark for BeCl<sub>2</sub> diagram, 1 mark for 'linear'.<br>1 mark for Cl<sub>2</sub>O diagram showing lone pairs, 1 mark for 'bent/V-shaped/angular'.<br>Mark name and shape independently.<br>Accept (distorted) tetrahedral for shape description. Penalise missing 'Cl' once only.",
        4, "AO1"
    ),
    "2006-jan-chm1-q1d": (
        "<i>M</i><sub>r</sub>(Mg(OH)<sub>2</sub>) = 58(.3)<br>"
        "moles Mg(OH)<sub>2</sub> = 1.00 / 58.3 = 0.0172 mol<br>"
        "moles HCl = 2 &times; 0.0172 = 0.0343 &ndash; 0.0344 mol<br>"
        "volume HCl = 0.0343 &times; 1000 / 1.00 = <b>34.3 &ndash; 34.5 cm<sup>3</sup></b>",
        "Consequential marking on wrong <i>M</i><sub>r</sub>.<br>Process mark for 2:1 ratio.<br>If candidate used 0.017 or 0.0171 lose M2.<br>Just answer with no working: if in range scores 4 marks; if e.g. 34 then 2 marks.",
        4, "AO2"
    ),
    "2006-jan-chm1-q2ai": (
        "moles KNO<sub>3</sub> = 1.00 / 101.1 = <b>9.89 &times; 10<sup>&minus;3</sup> mol</b>",
        "Accept 0.00989 mol.",
        1, "AO2"
    ),
    "2006-jan-chm1-q2aii": (
        "<i>pV</i> = <i>nRT</i> &nbsp;<i>or</i>&nbsp; <i>n</i> = <i>pV</i> / <i>RT</i> (1)<br>"
        "<i>n</i> = (100 000 &times; 1.22 &times; 10<sup>&minus;4</sup>) / (8.31 &times; 298) (2)<br>"
        "= <b>4.93 &times; 10<sup>&minus;3</sup> mol</b> (1)",
        "Mark answer first &ndash; check back if wrong.<br>Transcription error lose M3, mark M4 consequential on error.<br>If wrong temperature conversion, lose M3 consequential M4.",
        4, "AO2"
    ),
    "2006-jan-chm1-q2bi": (
        "Simplest / lowest ratio of atoms of each element in a compound / substance / molecule",
        "Penalise 'amount of atoms' or 'ratio of molecules'.",
        1, "AO1"
    ),
    "2006-jan-chm1-q2bii": (
        "K: 45.9 / 39.1 = 1.17<br>"
        "N: 16.5 / 14.0 = 1.18<br>"
        "O: 37.6 / 16.0 = 2.35 (1)<br>"
        "Ratio = 1 : 1 : 2 (1)<br>"
        "Empirical formula = <b>KNO<sub>2</sub></b> (1)",
        "M3 tied to M2.<br>If calculation inverted, lose M2 and M3.<br>If % of O missing, award M2 only.",
        3, "AO2"
    ),
    "2006-jan-chm1-q2c": (
        "2KNO<sub>3</sub> &rarr; 2KNO<sub>2</sub> + O<sub>2</sub>",
        "Allow fractions/multiples.<br>Accept 2KNO<sub>3</sub> &rarr; K<sub>2</sub>N<sub>2</sub>O<sub>4</sub> + O<sub>2</sub>.<br>Do NOT accept 'Y' in equation.",
        1, "AO2"
    ),
    "2006-jan-chm1-q3a": (
        "Tendency / ability / power of an atom / element / nucleus to attract / pull / withdraw electrons / bonding pair / shared pair (1)<br>"
        "in a covalent bond (1)",
        "2 marks: 1 for attraction of electrons/bonding pair, 1 for in a covalent bond.",
        2, "AO1"
    ),
    "2006-jan-chm1-q3bi": (
        "Liquid F<sub>2</sub>: <b>van der Waals' / induced dipole-dipole / London / dispersion forces</b> (1)<br>"
        "Liquid CH<sub>3</sub>F: <b>dipole-dipole</b> (1)<br>"
        "Liquid HF: <b>hydrogen bonding</b> (1)",
        "For CH<sub>3</sub>F: not just 'dipole'.<br>For HF: not just 'H' / 'hydrogen'.",
        3, "AO1"
    ),
    "2006-jan-chm1-q3bii": (
        "Large difference in electronegativity between H and F / F is much more electronegative than H (1)<br>"
        "&delta;+ H&mdash;F &delta;&minus; dipole created / polar bond (1)<br>"
        "Attraction between &delta;+ H and lone pair on F of another molecule (1)",
        "May score from a clearly labelled diagram.<br>Contradiction if full charges shown (lose M2 and M3).",
        3, "AO1"
    ),
    "2006-jan-chm1-q3ci": (
        "Van der Waals' forces / induced dipole-dipole attractions (1)<br>"
        "increase with increasing <i>M</i><sub>r</sub> / size / mass / number of electrons / size of electron cloud (1)",
        "Ignore references to permanent dipole-dipole.<br>If ionic or 'covalent bonds broken', CE = 0/2.",
        2, "AO1"
    ),
    "2006-jan-chm1-q3cii": (
        "Hydrogen bonding is stronger than van der Waals' attractions / forces (between molecules)",
        "Accept hydrogen bonding is very strong / strongest.<br>Accept 'HF has hydrogen bonds, others only have van der Waals'. Not just 'HF has hydrogen bonding'.",
        1, "AO1"
    ),
    "2006-jan-chm1-q4a": (
        "Enthalpy / energy change / required when an electron is removed / knocked out to form a uni-positive ion (1)<br>"
        "from a gaseous atom (1)",
        "Ignore 'minimum' energy.<br>Could get M2 from a correct equation: X(g) &rarr; X<sup>+</sup>(g) + e<sup>&minus;</sup>.<br>Accept molar definitions.",
        2, "AO1"
    ),
    "2006-jan-chm1-q4b": (
        "1s<sup>2</sup> <b>2s<sup>2</sup> 2p<sup>6</sup></b>",
        "Accept capitals and subscripts.",
        1, "AO1"
    ),
    "2006-jan-chm1-q4c": (
        "<b>s</b> block",
        "Not a specific 's' orbital (e.g. 2s).",
        1, "AO1"
    ),
    "2006-jan-chm1-q4d": (
        "Mg<sup>+</sup>(g) &rarr; Mg<sup>2+</sup>(g) + e<sup>&minus;</sup>",
        "Accept Mg<sup>+</sup>(g) &minus; e<sup>&minus;</sup> &rarr; Mg<sup>2+</sup>(g) or Mg<sup>+</sup>(g) + e<sup>&minus;</sup> &rarr; Mg<sup>2+</sup>(g) + 2e<sup>&minus;</sup>.<br>State symbols required.",
        1, "AO1"
    ),
    "2006-jan-chm1-q4e": (
        "1. Mg<sup>2+</sup> ion is smaller than Ne atom / Mg<sup>2+</sup> valence electrons closer to nucleus (1)<br>"
        "2. Mg<sup>2+</sup> has more protons than Ne / higher nuclear charge (<i>or</i> e<sup>&minus;</sup> is removed from a charged Mg<sup>2+</sup> ion vs neutral Ne atom) (1)",
        "Do not accept 'atomic radius' for Mg<sup>2+</sup>.<br>Accept converse arguments.",
        2, "AO1"
    ),
    "2006-jan-chm1-q4fi": (
        "Trend: <b>increases</b> (1)<br>"
        "Explanation: More protons / increased nuclear charge (1)<br>"
        "Same shell / same shielding / smaller atomic radius (1)",
        "If trend given as 'decreases', CE = 0/3.<br>NOT 'increased atomic number'.",
        3, "AO1"
    ),
    "2006-jan-chm1-q4fii": (
        "Reference to electron pair in 3p sub-level / 3p orbital (1)<br>"
        "Repulsion between the electrons in this electron pair (makes electron easier to remove) (1)",
        "Penalise if wrong shell quoted (e.g. 2p).<br>Mark points independently.",
        2, "AO1"
    )
}

def main():
    print("Loading questions.json...")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Remove existing 2006-jan-chm1 questions if any
    db["questions"] = [q for q in db["questions"] if q["paper"] != "2006-jan-chm1"]

    print("Rendering mark scheme images...")
    new_questions = []
    for qid, qnum, page, marks, topics, qtypes, title in QUESTIONS_DEF:
        ans_html, extra_html, ms_marks, ao_spec = MS_DEF[qid]
        ms_fname = f"ms_q{qnum.replace('(', '').replace(')', '')}.jpg"
        ms_rel = f"img/2006-jan-chm1/{ms_fname}"
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

        q_img_rel = f"img/2006-jan-chm1/q_q{qnum.replace('(', '').replace(')', '')}.jpg"

        q_obj = {
            "id": qid,
            "paper": "2006-jan-chm1",
            "year": 2006,
            "series": "January",
            "date": "2006-01-11",
            "code": "CHM1",
            "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
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

    print(f"Successfully added {len(new_questions)} questions for 2006-jan-chm1 to questions.json!")

if __name__ == "__main__":
    main()

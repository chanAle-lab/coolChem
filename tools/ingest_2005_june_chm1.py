"""
Ingestion script for 2005 June CHM1 (Section A only)
Excludes old-spec Section B essay questions (Q6, Q7).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382980188_94874931.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-june-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-june-chm1",
    "year": 2005,
    "series": "June",
    "date": "2005-06-08",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry"
}

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2005-june-chm1-q1ai",
        "question": "1(a)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "State what is meant by the term isotopes.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "(Atoms with the) same number of protons / same atomic number / atoms of the same element", "1 mark; molecules = contradiction", "1", "AO1 / 3.1.1"),
            ("", "But different number of neutrons / different mass number", "1 mark; do not allow different atomic mass or Ar", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-june-chm1-q1aii",
        "question": "1(a)(ii)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall", "explanation"],
        "summary": "Explain how ions are detected and how their abundance is measured in a mass spectrometer.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "Detected by: positive (+ve) ions collide with / are deflected to / collected at the detector", "1 mark for detection location", "1", "AO1 / 3.1.1"),
            ("", "Causing current to flow / detected electrically / voltage generated", "1 mark; do not allow charge produced or detected electronically", "1", "AO1 / 3.1.1"),
            ("", "Abundance measured: current size depends on abundance / number of ions hitting detector", "1 mark for current proportional to abundance", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-june-chm1-q1bi",
        "question": "1(b)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Define the term relative atomic mass of an element.",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "Mean / average mass of an atom / all the isotopes (of an element)", "1 mark; penalise 'weight' once only", "1", "AO1 / 3.1.1"),
            ("", "1/12th mass of an atom of 12C\n(OR relative to 12C taken as 12 / 12.000)", "1 mark; mark independently; do not allow mass of average atom", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-june-chm1-q1bii",
        "question": "1(b)(ii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["calculation"],
        "summary": "Calculate relative atomic mass of iron sample from isotope abundance table.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "[(54 × 5.8) + (56 × 91.6) + (57 × 2.6)] / 100", "1 mark for correct method", "1", "AO2 / 3.1.1"),
            ("", "= 55.9", "1 mark for answer to 1 d.p.", "1", "AO2 / 3.1.1")
        ]
    },
    {
        "id": "2005-june-chm1-q1ci",
        "question": "1(c)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Give the electron arrangement of an Fe2+ ion.",
        "figures": [],
        "ms_rows": [
            ("1(c)(i)", "1s2 2s2 2p6 3s2 3p6 3d6", "Accept subscripts or caps; ignore 4s0; penalise missing shell numbers", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-june-chm1-q1cii",
        "question": "1(c)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.1", "3.2.1"],
        "skills": ["recall"],
        "summary": "State why iron is placed in the d block of the Periodic Table.",
        "figures": [],
        "ms_rows": [
            ("1(c)(ii)", "Highest energy level / last sub-shell to be filled is (3)d\nOR outermost electrons in the d sub-shell / orbital", "Do not allow incomplete d sub-shell alone", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-june-chm1-q1ciii",
        "question": "1(c)(iii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.1"],
        "skills": ["explanation"],
        "summary": "Difference in chemical properties of isotopes of the same element and explanation.",
        "figures": [],
        "ms_rows": [
            ("1(c)(iii)", "Difference: No difference / same", "1 mark for stating no difference", "1", "AO1 / 3.1.1"),
            ("", "Explanation: Same electron arrangement / same number of electrons / chemical properties determined by electrons", "1 mark; M2 tied to correct answer for M1", "1", "AO1 / 3.1.1")
        ]
    },

    # Q2
    {
        "id": "2005-june-chm1-q2a",
        "question": "2(a)",
        "marks": 4,
        "page": 6,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate maximum mass of lead(II) nitrate obtained from 175 cm3 of 1.50 mol dm–3 HNO3.",
        "figures": [],
        "ms_rows": [
            ("2(a)", "Moles HNO3 = 175 × 10^(–3) × 1.50 = 0.2625 mol", "1 mark", "1", "AO2 / 3.1.2"),
            ("", "Moles Pb(NO3)2 = 0.5 × 0.2625 = 0.131 mol", "1 mark for mole ratio 1:2", "1", "AO2 / 3.1.2"),
            ("", "Mr Pb(NO3)2 = 331.2", "1 mark for relative formula mass", "1", "AO2 / 3.1.2"),
            ("", "Mass Pb(NO3)2 = 331.2 × 0.131 = 43.5 g (accept 43.2 – 43.8 g)", "1 mark; consequential if M1, M2 correct", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2005-june-chm1-q2bi",
        "question": "2(b)(i)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "State ideal gas equation and calculate total moles of gas produced in thermal decomposition.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "pV = nRT", "1 mark for equation", "1", "AO1 / 3.1.2"),
            ("", "n = pV / RT = (100000 × 1.50 × 10^(–4)) / (8.31 × 500) = 3.61 × 10^(–3) mol", "1 mark; if pressure not converted to Pa, max 1", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2005-june-chm1-q2bii",
        "question": "2(b)(ii)",
        "marks": 5,
        "page": 7,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Deduce number of moles and mass of NO2 present in gaseous decomposition mixture.",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "Mole fraction NO2 = 4/5 (from 4NO2 / 5 gas moles)", "1 mark for 4/5 ratio", "1", "AO2 / 3.1.2"),
            ("", "Moles NO2 = 4/5 × 3.61 × 10^(–3) = 2.89 × 10^(–3) mol\n(or 1.78 × 10^(–3) if 2.23 × 10^(–3) used)", "1 mark for moles of NO2", "1", "AO2 / 3.1.2"),
            ("", "Mr NO2 = 46.0", "1 mark for Mr", "1", "AO1 / 3.1.2"),
            ("", "Mass NO2 = 46 × 2.89 × 10^(–3) = 0.133 g\n(or 0.0821 g if 2.23 × 10^(–3) used)", "1 mark for mass", "1", "AO2 / 3.1.2")
        ]
    },

    # Q3
    {
        "id": "2005-june-chm1-q3a",
        "question": "3(a)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.2", "3.2.1"],
        "skills": ["recall"],
        "summary": "Write equation for reaction of aluminium with aqueous copper(II) chloride.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "2Al + 3CuCl2 → 2AlCl3 + 3Cu\n(OR 2Al + 3Cu2+ → 2Al3+ + 3Cu)", "Accept multiples / fractions", "1", "AO1 / 3.1.2")
        ]
    },
    {
        "id": "2005-june-chm1-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.1", "3.2.1"],
        "skills": ["recall"],
        "summary": "State general trend in first ionisation energy of Period 3 elements from Na to Ar.",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "Increases", "General trend increases across Period 3", "1", "AO1 / 3.2.1")
        ]
    },
    {
        "id": "2005-june-chm1-q3bii",
        "question": "3(b)(ii)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.1", "3.2.1"],
        "skills": ["explanation"],
        "summary": "Explain why first ionisation energy of aluminium deviates from general Period 3 trend.",
        "figures": [],
        "ms_rows": [
            ("3(b)(ii)", "Lower than expected / lower than Mg / less energy needed to ionise", "1 mark for stating lower", "1", "AO1 / 3.2.1"),
            ("", "Electron removed from (3)p sub-level (rather than 3s)", "1 mark for identifying 3p electron", "1", "AO1 / 3.2.1"),
            ("", "3p electron of higher energy / further from nucleus / shielded by 3s electrons", "1 mark for shielding / energy explanation", "1", "AO1 / 3.2.1")
        ]
    },
    {
        "id": "2005-june-chm1-q3c",
        "question": "3(c)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Equation including state symbols for second ionisation energy of aluminium.",
        "figures": [],
        "ms_rows": [
            ("3(c)", "Al+(g) → Al2+(g) + e–", "State symbols required", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-june-chm1-q3d",
        "question": "3(d)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.3", "3.2.1"],
        "skills": ["explanation"],
        "summary": "State and explain trend in melting points of Period 3 metals Na, Mg and Al.",
        "figures": [],
        "ms_rows": [
            ("3(d)", "Trend: Increases (from Na to Mg to Al)", "1 mark for trend", "1", "AO1 / 3.2.1"),
            ("", "More protons / higher charge on cation / more delocalised electrons / smaller ionic radius", "1 mark for cation charge / delocalised e–", "1", "AO1 / 3.1.3"),
            ("", "Stronger attraction between cations and delocalised electrons / stronger metallic bonding", "1 mark for metallic bond strength", "1", "AO1 / 3.1.3")
        ]
    },

    # Q4
    {
        "id": "2005-june-chm1-q4a",
        "question": "4(a)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.3"],
        "skills": ["recall", "explanation"],
        "summary": "Type of bond formed between phosphine and H+ and explanation of formation.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Dative / coordinate (covalent) bond", "1 mark for bond type", "1", "AO1 / 3.1.3"),
            ("", "Lone / non-bonding pair of electrons", "1 mark; insist on pair of electrons", "1", "AO1 / 3.1.3"),
            ("", "(Donated) from P to H+", "1 mark for donor and acceptor", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2005-june-chm1-q4b",
        "question": "4(b)",
        "marks": 4,
        "page": 9,
        "topics": ["3.1.3"],
        "skills": ["recall", "explanation"],
        "summary": "Shapes of PH3 and PH4+, name of PH3 shape, and bond angle in PH4+.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "PH3: Pyramidal diagram with 3 bonding pairs and 1 lone pair on P", "1 mark for correct PH3 shape & lone pair", "1", "AO1 / 3.1.3"),
            ("", "PH4+: Tetrahedral diagram with 4 bonding pairs and positive charge", "1 mark for correct PH4+ shape & charge", "1", "AO1 / 3.1.3"),
            ("", "Shape of PH3: Pyramidal / trigonal pyramid", "1 mark for shape name", "1", "AO1 / 3.1.3"),
            ("", "Bond angle in PH4+: 109.5° (accept 109° – 109.5°)", "1 mark for bond angle", "1", "AO1 / 3.1.3")
        ]
    },

    # Q5
    {
        "id": "2005-june-chm1-q5a",
        "question": "5(a)",
        "marks": 2,
        "page": 10,
        "topics": ["3.1.3"],
        "skills": ["explanation"],
        "summary": "Explain why O–H bond in methanol molecule is polar.",
        "figures": [],
        "ms_rows": [
            ("5(a)", "Oxygen is more electronegative than hydrogen / stronger attraction for bonding electrons", "1 mark for electronegativity difference", "1", "AO1 / 3.1.3"),
            ("", "Causes higher electron density round oxygen atom / causes delta– on O and delta+ on H", "1 mark for resulting charge separation", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2005-june-chm1-q5b",
        "question": "5(b)",
        "marks": 3,
        "page": 10,
        "topics": ["3.1.3"],
        "skills": ["explanation"],
        "summary": "Explain why boiling point of methanol (+65 °C) is much higher than oxygen (–183 °C).",
        "figures": [],
        "ms_rows": [
            ("5(b)", "Van der Waals forces between oxygen molecules", "1 mark for identifying VdW in O2", "1", "AO1 / 3.1.3"),
            ("", "Hydrogen bonding between methanol molecules", "1 mark for identifying H-bonding in CH3OH", "1", "AO1 / 3.1.3"),
            ("", "Hydrogen bonding is stronger than van der Waals forces / stronger intermolecular forces in methanol", "1 mark for IMF comparison", "1", "AO1 / 3.1.3")
        ]
    }
]

def main():
    print("Opening Question Paper PDF...")
    doc_qp = fitz.open(QP_PATH)

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Remove existing
    db["questions"] = [q for q in db["questions"] if q.get("paper") != "2005-june-chm1"]

    for qd in QUESTIONS_DATA:
        qid = qd["id"]
        q_label = qd["question"]
        ms_img_rel = f"img/2005-june-chm1/ms_{qid.split('-')[-1]}.jpg"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

        answers_list = []
        extra_list = []
        spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1"
        for r in qd["ms_rows"]:
            prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
            answers_list.append(f"{prefix}{r[1]} ({r[3]})")
            if r[2]:
                extra_list.append(f"{r[2]}")

        answers_html = "<br>".join(answers_list)
        extra_html = "<br>".join(extra_list) if extra_list else "-"

        render_official_markscheme_image(
            question_label=q_label,
            answers_html=answers_html,
            extra_html=extra_html,
            marks=qd["marks"],
            spec_ref=spec_ref,
            output_path=ms_img_abs
        )

        entry = {
            "id": qid,
            "paper": "2005-june-chm1",
            "question": q_label,
            "marks": qd["marks"],
            "page": qd["page"],
            "topics": qd["topics"],
            "skills": qd["skills"],
            "summary": qd["summary"],
            "image": f"img/2005-june-chm1/q_{qid.split('-')[-1]}.jpg",
            "figures": qd["figures"],
            "markscheme": ms_img_rel,
            "markscheme_text": "\n".join([f"{r[0]} {r[1]} [{r[3]}]".strip() for r in qd["ms_rows"]])
        }
        db["questions"].append(entry)
        print(f"Processed {qid} ({q_label}) - {qd['marks']} marks")

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully ingested {len(QUESTIONS_DATA)} questions for 2005-june-chm1!")

if __name__ == "__main__":
    main()

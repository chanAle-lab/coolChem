"""
Ingestion script for 2006 June CHM1 (Section A only)
Excludes old-spec Section B essay question (Q5).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383066745_4f369b0a.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-june-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

# Extract fig-q4-graph.jpg
doc = fitz.open(QP_PATH)
page = doc[8] # page 9
rect = fitz.Rect(130, 105, 470, 315)
pix = page.get_pixmap(clip=rect, dpi=200)
pix.save(os.path.join(IMG_DIR, "fig-q4-graph.jpg"))

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2006-june-chm1-q1a",
        "question": "1(a)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Define the term isotopes.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "Atoms / isotopes / particles / species with the same (number of) protons and different (number of) neutrons", "Not atomic number / mass number / molecules / same element / diff electrons", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2006-june-chm1-q1b",
        "question": "1(b)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["application"],
        "summary": "Identify the isotope that has 20 neutrons and a +1 charge, giving symbol, mass number and atomic number.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "Mass number: 37<br>Atomic number & symbol: 17 and Cl (or <sup>37</sup><sub>17</sub>Cl)", "1 mark for mass number 37 [Not 37.0]<br>1 mark for 17 and Cl<br>Mark independently; ignore charges", "2", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2006-june-chm1-q1ci",
        "question": "1(c)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "State the electronic configuration of a germanium atom.",
        "figures": [],
        "ms_rows": [
            ("1(c)(i)", "1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>6</sup> 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>2</sup><br>(or 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>6</sup> 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>2</sup>)", "Allow reversed 4s<sup>2</sup> 3d<sup>10</sup>; allow capitals/subscripts", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2006-june-chm1-q1cii",
        "question": "1(c)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.1"],
        "skills": ["calculation"],
        "summary": "Calculate the relative atomic mass of the sample of germanium.",
        "figures": [],
        "ms_rows": [
            ("1(c)(ii)", "<i>A</i><sub>r</sub> = [(70 × 24.4) + (72 × 32.4) + (74 × 43.2)] / 100<br>= (1708 + 2332.8 + 3196.8) / 100<br>= 72.4", "M1: Correct expression divided by 100 (Wrong approach or not dividing by 100 = CE = 0)<br>M2: 72.4 (Answer to 1 d.p.)<br>Mark conseq on transcription error", "2", "AO2 / 3.1.1")
        ]
    },
    {
        "id": "2006-june-chm1-q1ciii",
        "question": "1(c)(iii)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.1"],
        "skills": ["explanation"],
        "summary": "State what causes the deflection of ions in a mass spectrometer and explain why they are deflected by different amounts.",
        "figures": [],
        "ms_rows": [
            ("1(c)(iii)", "Magnet / electromagnet / magnetic field (or electric field / charge on negative/accelerator plate)<br><br>Correct link between deflection and <i>m/z</i> (e.g. smaller <i>m/z</i> deflected more)<br><br>Correct link between deflection and field (e.g. stronger field gives greater deflection)", "1 mark for magnetic field / magnet<br>1 mark for deflection linked to <i>m/z</i><br>1 mark for deflection linked to field strength<br>[Penalise 'reflected'/'diffracted' once only]<br>[Ignore references to molecules/atoms/particles]<br>[Consolation mark: allow correct link between mass and deflection for 1 mark out of the 2]", "3", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2006-june-chm1-q1civ",
        "question": "1(c)(iv)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.1"],
        "skills": ["application"],
        "summary": "Identify the ion that causes the peak at m/z = 36 and explain its presence.",
        "figures": [],
        "ms_rows": [
            ("1(c)(iv)", "<sup>72</sup>Ge<sup>2+</sup> only<br><br>Same <i>m/z</i> as <sup>36</sup>S<sup>+</sup> (or <i>m/z</i> = 72/2 = 36)", "1 mark for <sup>72</sup>Ge<sup>2+</sup><br>1 mark for same <i>m/z</i> / ratio 72/2 = 36<br>Mark independently", "2", "AO1 / 3.1.1")
        ]
    },
    # Q2
    {
        "id": "2006-june-chm1-q2a",
        "question": "2(a)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.3"],
        "skills": ["recall"],
        "summary": "Draw representations of the lattice structure of sodium metal and of sodium chloride.",
        "figures": [],
        "ms_rows": [
            ("2(a)", "Sodium metal: Regular array of positive ions (Na<sup>+</sup>) surrounded by delocalised electrons (e<sup>-</sup>)<br><br>Sodium chloride: 3D alternating lattice / cubic arrangement of Na<sup>+</sup> and Cl<sup>-</sup> ions", "1 mark for sodium metal lattice (positive ions with delocalised electrons)<br>1 mark for NaCl ionic lattice (alternating oppositely charged ions)<br>[Diagrams must be complete and accurate]", "2", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.3"],
        "skills": ["recall"],
        "summary": "State the type of bonding in sodium metal.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "Attraction / electrostatic forces between (positive) ions / lattice and delocalised / free electrons / sea of electrons", "Not metallic bonding (name already given); Not just 'forces'", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.3"],
        "skills": ["recall"],
        "summary": "State the type of bonding in sodium chloride.",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "Electrostatic attractions / forces between ions OR attractions between (oppositely charged) ions / Na<sup>+</sup> & Cl<sup>-</sup>", "Not ionic bonding (name already given)", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q2biii",
        "question": "2(b)(iii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.3"],
        "skills": ["explanation"],
        "summary": "Explain why the melting point of sodium chloride is higher than that of sodium metal.",
        "figures": [],
        "ms_rows": [
            ("2(b)(iii)", "(Here) the ionic bonding in NaCl is stronger / requires more energy to break than the metallic bonding in Na", "QoL mark. Accept 'bonding/forces of attraction in NaCl is stronger than in Na'<br>[If IMF/molecules/van der Waals'/dipole-dipole mentioned in parts (i) or (ii), then CE = 0 for (i)/(ii) and CE = 0 for (iii)]", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q2c",
        "question": "2(c)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.3"],
        "skills": ["comparison", "explanation"],
        "summary": "Compare and explain the electrical conductivities of solid sodium and solid sodium chloride.",
        "figures": [],
        "ms_rows": [
            ("2(c)", "Comparison: Sodium conducts and sodium chloride does NOT conduct<br><br>Explanation:<br>(Delocalised) electrons flow through the metal / carry current<br><br>Ions cannot move in solid salt / lattice", "1 mark: Comparison (Allow 'only Na conducts' or 'Na conducts, NaCl only conducts when molten'; do not accept sodium conducts better than NaCl)<br>1 mark: (Delocalised) electrons move/flow through metal [Not 'electrons carry electricity']<br>1 mark: Ions cannot move in solid salt [Not 'NaCl has no free charged particles']", "3", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q2d",
        "question": "2(d)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.3"],
        "skills": ["explanation"],
        "summary": "Explain why sodium metal is malleable.",
        "figures": [],
        "ms_rows": [
            ("2(d)", "Layers (of ions / atoms / particles) can slide over each other", "Not molecules; Not layers separate", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q2ei",
        "question": "2(e)(i)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.3"],
        "skills": ["application"],
        "summary": "Predict the shape and bond angle of the ammonium ion NH4+.",
        "figures": [],
        "ms_rows": [
            ("2(e)(i)", "Shape: Tetrahedral<br>Bond angle: 109.5° (or 109° / 109½°)", "1 mark for tetrahedral (not distorted/tetrahedron)<br>1 mark for 109.5° / 109° / 109½°", "2", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q2eii",
        "question": "2(e)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.3"],
        "skills": ["recall"],
        "summary": "Identify the bond formed between NH3 and H+ in NH4+.",
        "figures": [],
        "ms_rows": [
            ("2(e)(ii)", "Dative covalent / co-ordinate (bond)", "Accept dative / coordinate", "1", "AO1 / 3.1.3")
        ]
    },
    # Q3
    {
        "id": "2006-june-chm1-q3ai",
        "question": "3(a)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.2"],
        "skills": ["recall"],
        "summary": "State what is meant by the term one mole of molecules.",
        "figures": [],
        "ms_rows": [
            ("3(a)(i)", "Avogadro's number/constant of molecules/particles/species (or 6.02 × 10<sup>23</sup> molecules) OR the same number of molecules/particles as there are atoms in exactly 12 g of <sup>12</sup>C", "Not just 'atoms' for Avogadro; Not molecules in <sup>12</sup>C", "1", "AO1 / 3.1.2")
        ]
    },
    {
        "id": "2006-june-chm1-q3aii",
        "question": "3(a)(ii)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the total moles of gas produced from the decomposition of 0.350 g of oxygen.",
        "figures": [],
        "ms_rows": [
            ("3(a)(ii)", "Moles of O<sub>2</sub> = 0.350 / 32 = 1.09 × 10<sup>-2</sup> mol (or 0.01094 mol)<br><br>Total moles of gas = 29 × (1.09 × 10<sup>-2</sup>)<br>= 0.316 - 0.317 mol", "M1: Moles of O<sub>2</sub> = 0.350 / 32 (= 1.09 × 10<sup>-2</sup> mol)<br>M2: Ratio 29 (× 1.09 × 10<sup>-2</sup>) [Accept answers via 4 separate mole calculations]<br>M3: 0.316 - 0.317 mol (to 3+ sf)<br>Mark conseq on errors in M1/M2", "3", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2006-june-chm1-q3aiii",
        "question": "3(a)(iii)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the mass of nitroglycerine that decomposes to produce 0.350 g of oxygen.",
        "figures": [],
        "ms_rows": [
            ("3(a)(iii)", "Moles of nitroglycerine = 4 × 1.09 × 10<sup>-2</sup> = 0.0438 mol<br><br><i>M</i><sub>r</sub> of nitroglycerine C<sub>3</sub>H<sub>5</sub>N<sub>3</sub>O<sub>9</sub> = (3×12) + (5×1) + (3×14) + (9×16) = 227<br><br>Mass = 227 × 0.0438 = 9.90 - 9.93 g", "M1: Moles nitroglycerine = 4 × moles O<sub>2</sub> (conseq on their moles O<sub>2</sub>)<br>M2: <i>M</i><sub>r</sub> = 227 or number string<br>M3: Mass = 9.90 - 9.93 g (answer to 3+ sf)<br>Mark conseq on error in <i>M</i><sub>r</sub>; penalise wrong units; penalise sig. fig. errors once only in Q3", "3", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2006-june-chm1-q3b",
        "question": "3(b)",
        "marks": 4,
        "page": 8,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the total pressure generated in a 1.00 dm3 container by 0.873 mol of gas at 1100 K.",
        "figures": [],
        "ms_rows": [
            ("3(b)", "<i>pV</i> = <i>nRT</i>  =>  <i>p</i> = <i>nRT</i> / <i>V</i><br><br><i>p</i> = (0.873 × 8.31 × 1100) / (1.00 × 10<sup>-3</sup>)<br><br>= 7.98 × 10<sup>6</sup> Pa  (or 7980 kPa / 7.98 MPa)<br><br>Units: Pa (or kPa / MPa as appropriate)", "M1: <i>pV</i> = <i>nRT</i> rearranged (<i>p</i> = <i>nRT</i> / <i>V</i>)<br>M2: Correct substitution with <i>V</i> = 1.00 × 10<sup>-3</sup> m<sup>3</sup><br>M3: 7980093 / 7980 / 7.98 (ignore sf)<br>M4: Units = Pa / kPa / MPa as appropriate<br>[If error in conversion from Pa, treat as contradiction of units mark]<br>[If <i>T</i> = 1373 K used, penalise M2]", "4", "AO2 / 3.1.2")
        ]
    },
    # Q4
    {
        "id": "2006-june-chm1-q4ai",
        "question": "4(a)(i)",
        "marks": 3,
        "page": 9,
        "topics": ["3.2.1"],
        "skills": ["application"],
        "summary": "Plot approximate positions of melting points of silicon, chlorine and argon on the Period 3 diagram.",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "Si: cross ≥ 1200 K<br><br>Cl: cross below S<br><br>Ar: cross below Cl", "M1: Si cross ≥ 1200 K<br>M2: Cl cross below S<br>M3: Ar cross below Cl [allow even if M2 wrong; if Cl cross missing and Ar below S, allow M3]", "3", "AO1 / 3.2.1")
        ]
    },
    {
        "id": "2006-june-chm1-q4aii",
        "question": "4(a)(ii)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.3", "3.2.1"],
        "skills": ["explanation"],
        "summary": "Explain the high melting point of silicon by referring to its structure and bonding.",
        "figures": ["img/2006-june-chm1/fig-q4-graph.jpg"],
        "ms_rows": [
            ("4(a)(ii)", "Silicon is macromolecular / giant molecular / giant covalent / giant atomic<br><br>Covalent bonds need to be broken / overcome [Not loosened/weakened]<br><br>Covalent bonds are strong / many covalent bonds / requires much energy to break", "M1: Macromolecular / giant covalent<br>M2: Covalent bonds need to be broken<br>M3: Covalent bonds are strong / many bonds / requires much energy<br>[Must mention 'covalent' somewhere to earn M2/M3; If van der Waals'/IMF mentioned M2/M3 = CE = 0; If ions mentioned M1/M2/M3 = CE = 0]", "3", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q4aiii",
        "question": "4(a)(iii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.3", "3.2.1"],
        "skills": ["comparison", "explanation"],
        "summary": "Explain why the melting point of sulphur S8 is higher than that of phosphorus P4.",
        "figures": ["img/2006-june-chm1/fig-q4-graph.jpg"],
        "ms_rows": [
            ("4(a)(iii)", "Intermolecular force = van der Waals' / induced dipole-dipole / dispersion forces<br><br>Sulphur (S<sub>8</sub>) has greater <i>M</i><sub>r</sub> / larger size / larger surface area / more electrons / more atoms so stronger intermolecular / van der Waals' forces", "1 mark for van der Waals' forces<br>1 mark (QoL) for comparison: S<sub>8</sub> is bigger / more electrons so stronger van der Waals' forces [Not 'more shells']<br>Mark separately", "2", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2006-june-chm1-q4b",
        "question": "4(b)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.3", "3.2.2"],
        "skills": ["trend", "explanation"],
        "summary": "State and explain the trend in melting point of the Group II elements Ca-Ba.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "Trend: Decreases<br><br>Explanation:<br>Increase in size of ion / atom / more shells / decrease in charge density<br><br>Weaker attraction for delocalised / free electrons / weaker metallic bonding", "M1: Decreases [If trend wrong = CE = 0]<br>M2: Increase in size of ion / more shells / decrease in charge density<br>M3: Weaker attraction between positive ions and delocalised electrons / weaker metallic bonding [Ignore shielding; van der Waals' = CE = 0 for M2 and M3]", "3", "AO1 / 3.2.2")
        ]
    }
]

paper_id = "2006-june-chm1"
new_questions = []

for qd in QUESTIONS_DATA:
    qid = qd["id"]
    q_label = qd["question"]
    ms_img_rel = f"img/{paper_id}/ms_{qid.split('-')[-1]}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

    answers_list = []
    extra_list = []
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.1"
    for r in qd["ms_rows"]:
        prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
        answers_list.append(f"{prefix}{r[1]} ({r[3]})")
        if r[2]:
            extra_list.append(f"{r[2]}")

    answers_html = "<br><br>".join(answers_list)
    extra_html = "<br><br>".join(extra_list) if extra_list else "-"

    render_official_markscheme_image(
        question_label=q_label,
        answers_html=answers_html,
        extra_html=extra_html,
        marks=qd["marks"],
        spec_ref=spec_ref,
        output_path=ms_img_abs
    )

    q_obj = {
        "id": qid,
        "paper": paper_id,
        "question": q_label,
        "marks": qd["marks"],
        "page": qd["page"],
        "topics": qd["topics"],
        "skills": qd["skills"],
        "summary": qd["summary"],
        "question_text": qd["summary"],
        "markscheme_text": "Official AQA mark scheme table",
        "image": f"img/{paper_id}/{qid}.jpg",
        "figures": qd["figures"],
        "markscheme": [ms_img_rel]
    }
    new_questions.append(q_obj)

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    db = json.load(f)

db["questions"] = [q for q in db["questions"] if q.get("paper") != paper_id]
db["questions"].extend(new_questions)

with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully ingested {len(new_questions)} questions for {paper_id}. Total marks: {sum(q['marks'] for q in new_questions)}")

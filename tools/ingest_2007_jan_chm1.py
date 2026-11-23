"""
Ingestion script for 2007 January CHM1 (Section A only)
Excludes old-spec Section B essay questions (Q5, Q6).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-jan-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": "2007-jan-chm1",
    "year": 2007,
    "series": "January",
    "date": "2007-01-11",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2007-jan-chm1-q1a",
        "question": "1(a)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Complete the table giving the relative mass and relative charge of a proton and an electron.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "Proton: relative mass = <b>1</b>, relative charge = <b>+1</b><br><br>Electron: relative mass = <b>1/1800</b> (accept &lt; 5.6 × 10<sup>-4</sup> / negligible / 0), relative charge = <b>-1</b>", "1 mark per complete row", "2", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2007-jan-chm1-q1b",
        "question": "1(b)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["application"],
        "summary": "Deduce the symbol, including the mass number, of an atom with twice as many protons and twice as many neutrons as 19F.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "<sup>38</sup>Ar<br>Mass number: <b>38</b> (1)<br>Element: <b>Ar</b> (1)", "[Not AR] [M1: Not 38.0 / M2: Not symbol with a charge]<br>[Wrong proton number = 'con' for M2] [<sub>38</sub>Ar scores 1 mark]", "2", "AO2 / 3.1.1")
        ]
    },
    {
        "id": "2007-jan-chm1-q1ci",
        "question": "1(c)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Give the electron arrangement of Al3+ and Na+ ions.",
        "figures": [],
        "ms_rows": [
            ("1(c)(i)", "1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup>", "[Allow upper case letters and subscripted numbers] [Not [He]2s<sup>2</sup> 2p<sup>6</sup>]", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2007-jan-chm1-q1cii",
        "question": "1(c)(ii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["explanation"],
        "summary": "Explain why more energy is needed to remove an electron from the Al3+ ion than from the Na+ ion.",
        "figures": [],
        "ms_rows": [
            ("1(c)(ii)", "Any 2 points:<br>• More protons / atomic number / proton number / higher or stronger nuclear charge<br>• Al<sup>3+</sup> smaller (size) than Na<sup>+</sup> / e<sup>-</sup> closer to nucleus<br>• More attraction for e<sup>-</sup> from / e<sup>-</sup> held/pulled more strongly by Al<sup>3+</sup>", "[M3 Al<sup>3+</sup> may be inferred] [M2 Not 'atomic radius' / 'atom' / 'molecule' = 'con']<br>Greater charge density / charge-size ratio = alternative for either M1 or M2 but not for both", "2", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2007-jan-chm1-q1di",
        "question": "1(d)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Explain how atoms are ionised in a mass spectrometer.",
        "figures": [],
        "ms_rows": [
            ("1(d)(i)", "High energy/speed electrons / electrons from an electron gun / electron gun fires e<sup>-</sup> (1)<br><br>Knock off / displaces / removes an electron/electrons (from the gaseous atom) (1)", "[Accept correct equation for M2]", "2", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2007-jan-chm1-q1dii",
        "question": "1(d)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "State what is used to accelerate ions in a mass spectrometer.",
        "figures": [],
        "ms_rows": [
            ("1(d)(ii)", "Electric field / -ve plate / electrostatic field / oppositely charged plates", "[Not electronic field; magnetic field / electric current / high pd / high voltage]", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2007-jan-chm1-q1e",
        "question": "1(e)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.1"],
        "skills": ["calculation"],
        "summary": "Calculate the relative atomic mass of a sample of platinum from isotopic abundance data to one decimal place.",
        "figures": [],
        "ms_rows": [
            ("1(e)", "[(194 × 32.8) + (195 × 30.6) + (196 × 25.4) + (198 × 11.2)] / 100 (1)<br><br>= <b>195.3</b> (1 d.p. only) (1)", "[Mark M2 conseq. on transcription error]", "2", "AO2 / 3.1.1")
        ]
    },
    # Q2
    {
        "id": "2007-jan-chm1-q2ai",
        "question": "2(a)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the number of moles of NaOH in 21.70 cm3 of 0.150 mol dm-3 aqueous NaOH.",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "21.7 × 10<sup>-3</sup> × 0.150 = <b>3.255 × 10<sup>-3</sup></b> (mol)", "[Accept 3.25 – 3.26 × 10<sup>-3</sup>]", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q2aii",
        "question": "2(a)(ii)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of H2X in 25.0 cm3 of solution and deduce the moles of H2X in the 1.92 g sample.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "In 25 cm<sup>3</sup> = (3.255 × 10<sup>-3</sup>) / 2 = <b>1.63 × 10<sup>-3</sup></b> (mol) (1)<br><br>In sample = <b>1.63 × 10<sup>-2</sup></b> (mol) (1)", "[Conseq on (i)]<br>[Conseq on (ii)]", "2", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q2aiii",
        "question": "2(a)(iii)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the relative molecular mass, Mr, of H2X.",
        "figures": [],
        "ms_rows": [
            ("2(a)(iii)", "<i>M</i><sub>r</sub> = 1.92 / 1.63 × 10<sup>-2</sup> [Process mark] (1)<br><br>= 117.9 = <b>118</b> (1)", "[Conseq on (ii)] [M5 Tied to M4]<br>[Accept 117.7 – 118.2]<br>[If '÷ 2' not done in M2, CE = 0 for M2 and M5]<br>[If 1.63 × 10<sup>-3</sup> used in (a)(iii), lose M3 only]", "2", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.2"],
        "skills": ["recall"],
        "summary": "State what is meant by the term empirical formula.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "Simplest / lowest ratio of atoms of each element (in a compound)", "QoL [Allow 'elements' for 'each element'] ['atoms' needed in molar definitions]<br>[Not atoms of an element]", "1", "AO1 / 3.1.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q2bii",
        "question": "2(b)(ii)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the empirical formula and the molecular formula of compound Y (Mr = 146.0).",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "C: 49.31/12 = 4.11; H: 6.85/1 = 6.85; O: 43.84/16 = 2.74<br>÷ 2.74 => 1.5 : 2.5 : 1 (1)<br><br>Ratio 3 : 5 : 2 or <b>C<sub>3</sub>H<sub>5</sub>O<sub>2</sub></b> (1)<br><br>Molecular formula = C<sub>3</sub>H<sub>5</sub>O<sub>2</sub> × (146/73) = <b>C<sub>6</sub>H<sub>10</sub>O<sub>4</sub></b> (1)", "[If any A<sub>r</sub> value used is wrong / calculation inverted = CE = 0]<br>[If transcription error in % data, allow M1 only]<br>[Not (C<sub>3</sub>H<sub>5</sub>O<sub>2</sub>)<sub>2</sub>]", "3", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q2ci",
        "question": "2(c)(i)",
        "marks": 4,
        "page": 7,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "State the ideal gas equation and calculate the moles of CO2 formed in the decomposition of NaHCO3.",
        "figures": [],
        "ms_rows": [
            ("2(c)(i)", "<i>pV</i> = <i>nRT</i> (1)<br><br><i>n</i> = <i>pV</i> / <i>RT</i> = (100000 × 352 × 10<sup>-6</sup>) / (8.31 × 298) (2: volume conversion + numbers correct)<br><br>Moles CO<sub>2</sub> = <b>0.0142</b> (mol) (1)", "[If transcription error, lose M3 – so, '325' loses M2 (no conversion) and M3 (transcription error)]<br>[If expression inverted (i.e. RT/pV calculated) = CE = 0 for M3 and M4]", "4", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q2cii",
        "question": "2(c)(ii)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the mass of NaHCO3 that has decomposed.",
        "figures": [],
        "ms_rows": [
            ("2(c)(ii)", "Moles NaHCO<sub>3</sub> = 0.0142 × 2 (= 0.0284 mol) [Process] (1)<br><br>Mass NaHCO<sub>3</sub> = 84 × 0.0284 [mark for M<sub>r</sub>] (1)<br><br>= <b>2.38 – 2.39 g</b> [Conseq on M<sub>r</sub> error] (1)", "[If '× 2' not used – i.e. M5 = 0, then CE and M7 is also lost. Can get M6 for M<sub>r</sub>]<br>Answers using 0.0230 mol: Moles NaHCO<sub>3</sub> = 0.0460; Mass = 3.86–3.87 g<br>[Sig figs for whole question. For &lt;3 sf (unless 2sf dead) award 1 mark penalty ONLY for sf errors]", "3", "AO2 / 3.1.2")
        ]
    },
    # Q3
    {
        "id": "2007-jan-chm1-q3ai",
        "question": "3(a)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.3"],
        "skills": ["recall"],
        "summary": "State what is meant by the term polar when applied to a covalent bond.",
        "figures": [],
        "ms_rows": [
            ("3(a)(i)", "(A covalent bond in which) the electron density is / electrons are unequally shared.", "[Allow idea of δ+ and δ- across bond / charge separation / bonding pair / e<sup>-</sup>s closer to one atom] [accept clear diagram]<br>[Not electron cloud unless clearly describing a covalent bond]", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2007-jan-chm1-q3aii",
        "question": "3(a)(ii)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.3"],
        "skills": ["explanation"],
        "summary": "State whether the covalent bonds in hydrogen and in water are polar or non-polar and explain your answers.",
        "figures": [],
        "ms_rows": [
            ("3(a)(ii)", "Bonds in hydrogen: <b>non-polar</b>; Bonds in water: <b>polar</b> [need both] (1)<br><br>Atoms in a non-polar bond / in H<sub>2</sub> have the <u>same electronegativity</u> (1)<br><br>Atoms in a polar bond have <u>different electronegativities</u> OR O more/very electronegative / has different electronegativity than H (1)", "[If bond types reversed, lose M1, not CE]<br>[Allow M1 in 'Explanation' section if gaps in bond type section]<br>[If 'gaps' and bond types not identified in explanation, allow 1 mark for H<sub>2</sub> has no electronegativity diff. but H and O have electronegativity diff.]<br>[If M1 = wrong, e.g. van der Waals' etc, then CE = 0]", "3", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2007-jan-chm1-q3bi",
        "question": "3(b)(i)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.3"],
        "skills": ["application"],
        "summary": "Complete the diagram to show how an ammonia molecule forms a hydrogen bond with a water molecule.",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "At least one dipole (δ+ / δ-) on each molecule (1)<br><br>Lone pair on N and H-Bond (dashed/dotted line from lone pair on N to δ+ H of H<sub>2</sub>O) correctly indicated (1)<br><br>Two lone pairs on oxygen (1)", "[Not arrows or solid lines for H-bond]<br>[An extra, incorrect, hydrogen bond contradicts a correct one]", "3", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2007-jan-chm1-q3bii",
        "question": "3(b)(ii)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.3"],
        "skills": ["explanation"],
        "summary": "State the bond angle in an ammonia molecule and explain why it is different from that in water (104.5°).",
        "figures": [],
        "ms_rows": [
            ("3(b)(ii)", "Bond angle in ammonia = <b>106.5°–107.5°</b> (1)<br><br>Idea that lone pair repulsion &gt; bonding pair repulsion (1)<br><br>Oxygen / water has more lone pairs than nitrogen / ammonia (1)", "Mark points independently", "3", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2007-jan-chm1-q3c",
        "question": "3(c)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.3"],
        "skills": ["recall", "explanation"],
        "summary": "Name the type of bond formed between the nitrogen and aluminium atoms in H3N->AlCl3 and explain how it is formed.",
        "figures": [],
        "ms_rows": [
            ("3(c)", "Type of bond = <b>Dative bond / coordinate bond</b> (1)<br><br>Lone pair donated from/by N (to Al) / N provides both electrons (1)", "[Accept NH<sub>3</sub> in place of N]", "2", "AO1 / 3.1.3")
        ]
    },
    # Q4
    {
        "id": "2007-jan-chm1-q4a",
        "question": "4(a)",
        "marks": 1,
        "page": 10,
        "topics": ["3.2.2"],
        "skills": ["recall"],
        "summary": "Give the formula of the least soluble hydroxide of the Group II elements Mg to Ba.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Mg(OH)<sub>2</sub>", "-", "1", "AO1 / 3.2.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q4bi",
        "question": "4(b)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.2.2", "3.2.3"],
        "skills": ["practical"],
        "summary": "Identify a reagent to distinguish between aqueous sodium chloride and aqueous sodium sulphate.",
        "figures": [],
        "ms_rows": [
            ("4(b)(i)", "BaCl<sub>2</sub> / any soluble barium cpd &nbsp;OR&nbsp; AgNO<sub>3</sub> / any soluble silver cpd", "[If formula used, must be correct] [Not Ba<sup>2+</sup> ions / Ba element]<br>[If 'impossible' reagent, e.g. BaSO<sub>4</sub> or NaOH, = CE = 0]", "1", "AO3 / 3.2.2")
        ]
    },
    {
        "id": "2007-jan-chm1-q4bii",
        "question": "4(b)(ii)",
        "marks": 3,
        "page": 10,
        "topics": ["3.2.2", "3.2.3"],
        "skills": ["practical", "application"],
        "summary": "State the observations with sodium chloride and sodium sulphate and write an equation for any reaction.",
        "figures": [],
        "ms_rows": [
            ("4(b)(ii)", "Obs with NaCl = <b>no change/ppt/reaction</b> (OR white ppt* with AgNO<sub>3</sub>) (1)<br><br>Obs with Na<sub>2</sub>SO<sub>4</sub> = <b>white ppt* / solid</b> (OR no change etc. with AgNO<sub>3</sub>) (1)<br><br>Equation = <b>Ba<sup>2+</sup> + SO<sub>4</sub><sup>2-</sup> &rarr; BaSO<sub>4</sub></b> (OR <b>Ag<sup>+</sup> + Cl<sup>-</sup> &rarr; AgCl</b>) (1)", "[If Ba / Ba<sup>2+</sup> / wrong formula – i.e. M1 lost but not 'impossible' reagent, allow M2/3/4]<br>[Ignore state symbols in the equation – even if wrong]<br>[*ppt or solid or powder or suspension] [Not cloudy, milky, emulsion, residue, opaque] [Not nothing / no observations / none]", "3", "AO3 / 3.2.2")
        ]
    }
]

paper_id = PAPER_OBJ["id"]
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
        if r[2] and r[2] != "-":
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
        "markscheme": ms_img_rel
    }
    new_questions.append(q_obj)

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    db = json.load(f)

db["papers"] = [p for p in db["papers"] if p.get("id") != paper_id]
db["papers"].append(PAPER_OBJ)

db["questions"] = [q for q in db["questions"] if q.get("paper") != paper_id]
db["questions"].extend(new_questions)

with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully ingested {len(new_questions)} questions for {paper_id}. Total marks: {sum(q['marks'] for q in new_questions)}")

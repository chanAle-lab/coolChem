import json
import os
import sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2009-jan-chm1"
QP_PDF = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472259568_4e901e40.pdf"
IMG_DIR = os.path.join(ROOT, "img", PAPER_ID)
MS_DIR = os.path.join(IMG_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2009,
    "series": "January",
    "unit": "CHM1",
    "level": "AS",
    "title": "CHM1 – Atomic Structure, Bonding and Periodicity",
    "date": "2009-01-09",
    "totalMarks": 60,
    "duration": "1 hour",
}

Q1_FIG = f"img/{PAPER_ID}/fig-q1-ms.jpg"

QUESTIONS = [
    # Q1 (10 marks)
    {
        "id": f"{PAPER_ID}-q1a",
        "questionNumber": "1(a)",
        "page": 2,
        "marks": 1,
        "topics": ["Atomic Structure"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify part A in the simplified mass spectrometer diagram.",
        "specRef": "3.1.1",
        "ms_label": "1(a)",
        "ms_ans": "Part <b>A</b> = electron gun / ionisation chamber",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1bi",
        "questionNumber": "1(b)(i)",
        "page": 2,
        "marks": 1,
        "topics": ["Atomic Structure"],
        "skills": ["Application"],
        "summary": "Draw the path followed by 88Sr+ ions compared to 87Sr+ ions in the mass spectrometer.",
        "specRef": "3.1.1",
        "ms_label": "1(b)(i)",
        "ms_ans": "Path deviates at the start of the magnet and deflects less than <sup>87</sup>Sr<sup>+</sup>",
        "ms_extra": "Allow deviation to start between dashes 3 and 7; curve is smooth and path goes through slits",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1bii",
        "questionNumber": "1(b)(ii)",
        "page": 2,
        "marks": 2,
        "topics": ["Atomic Structure"],
        "skills": ["Explanation"],
        "summary": "Explain why the path of 88Sr+ ions differs from that of 87Sr+ ions.",
        "specRef": "3.1.1",
        "ms_label": "1(b)(ii)",
        "ms_ans": "<i>m/z</i> of <sup>88</sup>Sr &gt; <sup>87</sup>Sr (allow mass / mass no / atomic mass <sup>88</sup>Sr &gt; <sup>87</sup>Sr)<br><br>Magnetic field has less effect on higher <i>m/z</i> / heavier ions",
        "ms_extra": "Not &lsquo;heavier&rsquo;/atomic number for M1<br><br>Ind: Needs link with magnetic field &ndash; not just &lsquo;deflects more/less&rsquo;",
        "ms_marks": "1<br><br>1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1c",
        "questionNumber": "1(c)",
        "page": 5,
        "marks": 2,
        "topics": ["Atomic Structure"],
        "skills": ["Explanation"],
        "summary": "State and explain one adjustment to the mass spectrometer to detect 88Sr+ ions.",
        "specRef": "3.1.1",
        "ms_label": "1(c)",
        "ms_ans": "Increase magnetic field strength / decrease in electric field<br><br>So that ions hit the detector",
        "ms_extra": "If decrease magnetic field = CE = 0<br><br>(Tied to M1 or near miss)",
        "ms_marks": "1<br><br>1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1d",
        "questionNumber": "1(d)",
        "page": 5,
        "marks": 2,
        "topics": ["Atomic Structure", "Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the relative atomic mass of strontium to 1 d.p. from isotopic abundances.",
        "specRef": "3.1.1",
        "ms_label": "1(d)",
        "ms_ans": "[(84 &times; 0.56) + (86 &times; 9.86) + (87 &times; 7.02) + (88 &times; 82.56)] / 100<br><br>= 87.7",
        "ms_extra": "<br>Ignore &lsquo;g&rsquo;",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1e",
        "questionNumber": "1(e)",
        "page": 5,
        "marks": 2,
        "topics": ["Atomic Structure", "Periodicity"],
        "skills": ["Knowledge & Recall", "Explanation"],
        "summary": "State and explain the block in the Periodic Table to which strontium belongs.",
        "specRef": "3.1.1",
        "ms_label": "1(e)",
        "ms_ans": "&lsquo;s&rsquo; block<br><br>Highest energy / outermost electron in (5)s sublevel",
        "ms_extra": "&lsquo;d&rsquo; block etc. = CE = 0<br>Allow missing principal QN but penalise incorrect one (tied to M1); Allow sub-shell/orbital; Not sub-orbital/level/shell",
        "ms_marks": "1<br><br>1",
    },
    # Q2 (15 marks)
    {
        "id": f"{PAPER_ID}-q2a",
        "questionNumber": "2(a)",
        "page": 6,
        "marks": 1,
        "topics": ["Alkanes", "Amount of Substance"],
        "skills": ["Chemical Equations"],
        "summary": "Write an equation for the complete combustion of ethyne (C2H2).",
        "specRef": "3.1.2",
        "ms_label": "2(a)",
        "ms_ans": "2C<sub>2</sub>H<sub>2</sub> + 5O<sub>2</sub> &rarr; 4CO<sub>2</sub> + 2H<sub>2</sub>O",
        "ms_extra": "Allow multiples/fractions",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2b",
        "questionNumber": "2(b)",
        "page": 6,
        "marks": 4,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "State the ideal gas equation and calculate the moles of ethyne collected.",
        "specRef": "3.1.2",
        "ms_label": "2(b)",
        "ms_ans": "<i>pV</i> = <i>nRT</i><br><br><i>n</i> = <i>pV</i> / <i>RT</i> = (1.01 &times; 10<sup>5</sup> &times; 3.88 &times; 10<sup>&minus;4</sup>) / (8.31 &times; 284)<br>&bull; pressure conversion (1)<br>&bull; all numbers correct (1)<br><br>= 0.0166 / 0.0165 / 0.017 mol",
        "ms_extra": "If error in rearrangement, lose M3/M4<br>(allow missing units/mol/moles)<br>Not 0.0170",
        "ms_marks": "1<br><br>1<br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2c",
        "questionNumber": "2(c)",
        "page": 7,
        "marks": 4,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the mass of CaC2 reacted and the percentage purity of the 1.33 g sample.",
        "specRef": "3.1.2",
        "ms_label": "2(c)",
        "ms_ans": "Moles CaC<sub>2</sub> = 0.0166 mol (conseq all)<br>Mass of CaC<sub>2</sub> = 0.0166 &times; 64.1 = 1.06 g<br>% purity = (1.06 / 1.33) &times; 100<br>= 79.7 to 80.0 %",
        "ms_extra": "(0.017 &rarr; 81.9; 0.0155 &rarr; 74.7)<br>If answer &gt; 100% allow M3 but not M4.<br>Inverted expression = CE = 0 for M3/M4.<br>If % impurity calculated lose M4 unless 80% etc. appears.",
        "ms_marks": "1<br>1<br>1<br>1",
    },
    {
        "id": f"{PAPER_ID}-q2d",
        "questionNumber": "2(d)",
        "page": 7,
        "marks": 1,
        "topics": ["Bonding"],
        "skills": ["Structure & Bonding"],
        "summary": "Draw a diagram showing the bonding in a molecule of C2H2.",
        "specRef": "3.1.3",
        "ms_label": "2(d)",
        "ms_ans": "H&ndash;C&equiv;C&ndash;H or dot-and-cross showing triple bond (3 shared pairs between C atoms) and single C&ndash;H bonds",
        "ms_extra": "Any unambiguous structure &ndash; must show triple bond.<br>Allow diagram with all dots/crosses or non-linear.",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2ei",
        "questionNumber": "2(e)(i)",
        "page": 7,
        "marks": 1,
        "topics": ["Amount of Substance"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term empirical formula.",
        "specRef": "3.1.2",
        "ms_label": "2(e)(i)",
        "ms_ans": "Simplest/lowest (whole number) ratio of atoms of each element in a compound/molecule",
        "ms_extra": "QoL",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2eii",
        "questionNumber": "2(e)(ii)",
        "page": 7,
        "marks": 1,
        "topics": ["Amount of Substance"],
        "skills": ["Application"],
        "summary": "Deduce the empirical formula of ethyne.",
        "specRef": "3.1.2",
        "ms_label": "2(e)(ii)",
        "ms_ans": "Empirical formula = CH",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2f",
        "questionNumber": "2(f)",
        "page": 8,
        "marks": 3,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the empirical and molecular formulae of compound B (Mr = 215.8).",
        "specRef": "3.1.2",
        "ms_label": "2(f)",
        "ms_ans": "C: 22.24/12 = 1.85; H: 3.71/1 = 3.71; Br: 74.05/79.9 = 0.927<br><br>ratio C:H:Br = 2:4:1 &there4; C<sub>2</sub>H<sub>4</sub>Br<br><br>(emp mass = 108 &there4; mol formula = 215.8/107.9 &times; C<sub>2</sub>H<sub>4</sub>Br =) C<sub>4</sub>H<sub>8</sub>Br<sub>2</sub>",
        "ms_extra": "CE if inverted or At No used (allow 80 for Br)",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    # Q3 (13 marks)
    {
        "id": f"{PAPER_ID}-q3ai",
        "questionNumber": "3(a)(i)",
        "page": 10,
        "marks": 1,
        "topics": ["Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "State one way particle movement in a liquid differs from that in a solid.",
        "specRef": "3.1.3",
        "ms_label": "3(a)(i)",
        "ms_ans": "Difference = particles mobile / free to move / solid particles in fixed positions",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3aii",
        "questionNumber": "3(a)(ii)",
        "page": 10,
        "marks": 1,
        "topics": ["Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "State one way particle positioning in a liquid differs from that in a gas.",
        "specRef": "3.1.3",
        "ms_label": "3(a)(ii)",
        "ms_ans": "Difference = particles close together / gas particles far apart",
        "ms_extra": "Not closer etc.",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3b",
        "questionNumber": "3(b)",
        "page": 10,
        "marks": 2,
        "topics": ["Bonding", "Energetics"],
        "skills": ["Explanation"],
        "summary": "Explain the heat energy change associated with boiling.",
        "specRef": "3.1.3",
        "ms_label": "3(b)",
        "ms_ans": "Enthalpy change / energy is used / put in / endothermic to overcome<br><br>the forces holding the particles together",
        "ms_extra": "Allow for specific system<br>CE = 0 for bond break",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3ci",
        "questionNumber": "3(c)(i)",
        "page": 10,
        "marks": 2,
        "topics": ["Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "Define the term electronegativity.",
        "specRef": "3.1.3",
        "ms_label": "3(c)(i)",
        "ms_ans": "Tendency / strength / ability / power of an atom / element / nucleus to attract / withdraw electrons / e<sup>&minus;</sup> density / bonding pair / shared pair<br><br>In a covalent bond",
        "ms_extra": "Not &lsquo;affinity&rsquo;<br><br>(tied to M1 &ndash; unless silly slip in M1)",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3cii",
        "questionNumber": "3(c)(ii)",
        "page": 10,
        "marks": 2,
        "topics": ["Bonding"],
        "skills": ["Explanation"],
        "summary": "Explain in terms of electronegativity why hydrogen bonds form in H2O but not H2S.",
        "specRef": "3.1.3",
        "ms_label": "3(c)(ii)",
        "ms_ans": "O more electronegative than S / electronegativity difference OH &gt; SH<br><br>Electronegativity difference in SH too small to cause H bonding / e.n. diff in O&ndash;H is much greater than in S&ndash;H (minimum threshold)",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3ciii",
        "questionNumber": "3(c)(iii)",
        "page": 11,
        "marks": 1,
        "topics": ["Bonding"],
        "skills": ["Explanation"],
        "summary": "Explain in terms of intermolecular forces why H2S has a much lower boiling point than H2O.",
        "specRef": "3.1.3",
        "ms_label": "3(c)(iii)",
        "ms_ans": "IMF in H<sub>2</sub>S = dipole-dipole / van der Waals&rsquo;, which are <u>much</u> weaker than hydrogen bonding",
        "ms_extra": "QoL: Allow H bonding = strong + vdW = weak",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3civ",
        "questionNumber": "3(c)(iv)",
        "page": 11,
        "marks": 1,
        "topics": ["Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify an element other than oxygen that can form hydrogen bonds when bonded to H.",
        "specRef": "3.1.3",
        "ms_label": "3(c)(iv)",
        "ms_ans": "N (nitrogen) OR F (fluorine)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3d",
        "questionNumber": "3(d)",
        "page": 11,
        "marks": 3,
        "topics": ["Bonding"],
        "skills": ["Structure & Bonding"],
        "summary": "Draw a diagram showing hydrogen bonding between two water molecules with partial charges and lone pairs.",
        "specRef": "3.1.3",
        "ms_label": "3(d)",
        "ms_ans": "Partial charges shown on H and O used in H bond (min requirement)<br>2 lp on each oxygen<br>H-bond indicated between lp on O and H on second molecule",
        "ms_extra": "Apply &lsquo;con&rsquo; if any charges incorrect; HO<sub>2</sub> = CE = 0.<br>If H-bond between 2 H atoms, allow M2 only. Penalise H&divide;O 1 mark.",
        "ms_marks": "1<br>1<br>1",
    },
    # Q4 (7 marks)
    {
        "id": f"{PAPER_ID}-q4a",
        "questionNumber": "4(a)",
        "page": 12,
        "marks": 2,
        "topics": ["Bonding"],
        "skills": ["Knowledge & Recall", "Explanation"],
        "summary": "Name and describe how the bond forms between :CH2 and H+ to make CH3+.",
        "specRef": "3.1.3",
        "ms_label": "4(a)",
        "ms_ans": "Dative / coordinate<br><br>Electron pair donated from C / CH<sub>2</sub> / to H<sup>(+)</sup>",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4b",
        "questionNumber": "4(b)",
        "page": 12,
        "marks": 2,
        "topics": ["Bonding"],
        "skills": ["Structure & Bonding"],
        "summary": "Draw the shapes of CH2 (including lone pair) and CH3+.",
        "specRef": "3.1.3",
        "ms_label": "4(b)",
        "ms_ans": ":CH<sub>2</sub> shown as &lsquo;bent&rsquo; (trigonal planar with lp and 2 C&ndash;H bonds)<br><br>CH<sub>3</sub><sup>+</sup> shown as trigonal planar",
        "ms_extra": "<br>Don&rsquo;t penalise missing charge",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4c",
        "questionNumber": "4(c)",
        "page": 12,
        "marks": 2,
        "topics": ["Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the shapes of the CH2 molecule and the CH3+ ion.",
        "specRef": "3.1.3",
        "ms_label": "4(c)",
        "ms_ans": ":CH<sub>2</sub> = bent or V-shaped / angular / distorted or irregular trigonal planar<br><br>CH<sub>3</sub><sup>+</sup> = trigonal planar",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4d",
        "questionNumber": "4(d)",
        "page": 12,
        "marks": 1,
        "topics": ["Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "State the bond angle in the CH3+ ion.",
        "specRef": "3.1.3",
        "ms_label": "4(d)",
        "ms_ans": "120&deg; only",
        "ms_extra": "",
        "ms_marks": "1",
    },
]


def extract_figures():
    doc = fitz.open(QP_PDF)
    page = doc[1]  # Page 2
    rect = fitz.Rect(42, 142, 555, 475)
    pix = page.get_pixmap(clip=rect, dpi=200)
    pix.save(os.path.join(ROOT, Q1_FIG))
    print(f"Saved figure {Q1_FIG}")


def main():
    extract_figures()
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    papers = [p for p in db["papers"] if p["id"] != PAPER_ID]
    papers.append(PAPER_OBJ)
    db["papers"] = papers

    questions = [q for q in db["questions"] if q.get("paper") != PAPER_ID]

    for q in QUESTIONS:
        q_slug = q["id"].split("-")[-1]
        ms_rel = f"img/{PAPER_ID}/ms/{q_slug}.png"
        ms_abs = os.path.join(ROOT, ms_rel)
        render_official_markscheme_image(
            question_label=q["ms_label"],
            answers_html=q["ms_ans"],
            extra_html=q["ms_extra"],
            marks=q["ms_marks"],
            spec_ref=q["specRef"],
            output_path=ms_abs,
        )
        questions.append({
            "id": q["id"],
            "paper": PAPER_ID,
            "year": PAPER_OBJ["year"],
            "series": PAPER_OBJ["series"],
            "unit": PAPER_OBJ["unit"],
            "level": PAPER_OBJ["level"],
            "question": q["questionNumber"],
            "questionNumber": q["questionNumber"],
            "page": q["page"],
            "marks": q["marks"],
            "topics": q["topics"],
            "skills": q["skills"],
            "summary": q["summary"],
            "specRef": q["specRef"],
            "image": f"img/{PAPER_ID}/{q_slug}.jpg",
            "markscheme": ms_rel,
            "figures": q.get("figures", []),
        })

    db["questions"] = questions
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    total_m = sum(q["marks"] for q in QUESTIONS)
    print(f"Ingested {PAPER_ID}: {len(QUESTIONS)} questions, {total_m} marks.")


if __name__ == "__main__":
    main()

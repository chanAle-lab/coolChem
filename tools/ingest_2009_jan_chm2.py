import json
import os
import sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2009-jan-chm2"
QP_PDF = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472259573_661408ee.pdf"
IMG_DIR = os.path.join(ROOT, "img", PAPER_ID)
MS_DIR = os.path.join(IMG_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2009,
    "series": "January",
    "unit": "CHM2",
    "level": "AS",
    "title": "CHM2 – Foundation Physical and Inorganic Chemistry",
    "date": "2009-01-09",
    "totalMarks": 60,
    "duration": "1 hour",
}

Q1_FIG = f"img/{PAPER_ID}/fig-q1-eq.jpg"
Q3C_FIG = f"img/{PAPER_ID}/fig-q3c.jpg"

QUESTIONS = [
    # Q1 (13 marks)
    {
        "id": f"{PAPER_ID}-q1a",
        "questionNumber": "1(a)",
        "page": 2,
        "marks": 1,
        "topics": ["Equilibria"],
        "skills": ["Data Analysis"],
        "summary": "Mark X on the time axis where equilibrium is first established.",
        "specRef": "3.1.6",
        "ms_label": "1(a)",
        "ms_ans": "<b>X</b> on the time axis under the H of H<sub>2</sub>O",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1b",
        "questionNumber": "1(b)",
        "page": 2,
        "marks": 1,
        "topics": ["Equilibria"],
        "skills": ["Knowledge & Recall"],
        "summary": "State Le Chatelier's principle.",
        "specRef": "3.1.6",
        "ms_label": "1(b)",
        "ms_ans": "System at equilibrium opposes any change made to it",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1c",
        "questionNumber": "1(c)",
        "page": 2,
        "marks": 2,
        "topics": ["Equilibria"],
        "skills": ["Explanation"],
        "summary": "State and explain the effect of increasing pressure on the equilibrium yield of hydrogen.",
        "specRef": "3.1.6",
        "ms_label": "1(c)",
        "ms_ans": "None<br><br>Same number of moles / molecules / particles on each side",
        "ms_extra": "If this is wrong lose both marks in this section.<br>Not atoms.",
        "ms_marks": "1<br><br>1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1di",
        "questionNumber": "1(d)(i)",
        "page": 3,
        "marks": 2,
        "topics": ["Kinetics"],
        "skills": ["Explanation"],
        "summary": "State and explain the effect of raising temperature above 450 C on the rate of hydrogen production.",
        "specRef": "3.1.4",
        "ms_label": "1(d)(i)",
        "ms_ans": "Increase rate<br><br>More particles / collisions have <i>E</i> &gt; <i>E</i><sub>a</sub>",
        "ms_extra": "If this is wrong lose both marks.<br>Allow sufficient/enough energy. Not more frequent/forceful collisions or <i>E</i><sub>a</sub> lower.",
        "ms_marks": "1<br><br>1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1dii",
        "questionNumber": "1(d)(ii)",
        "page": 3,
        "marks": 3,
        "topics": ["Kinetics"],
        "skills": ["Explanation"],
        "summary": "State and explain the effect of a catalyst on the rate of a reaction.",
        "specRef": "3.1.4",
        "ms_label": "1(d)(ii)",
        "ms_ans": "Increase<br><br>Finds an alternative route / correct orientation / surface to react on<br><br>Lower activation energy",
        "ms_extra": "If this is wrong lose all marks in this section",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1diii",
        "questionNumber": "1(d)(iii)",
        "page": 3,
        "marks": 1,
        "topics": ["Equilibria"],
        "skills": ["Application"],
        "summary": "Deduce the sign of the enthalpy change given that yield decreases above 450 C.",
        "specRef": "3.1.6",
        "ms_label": "1(d)(iii)",
        "ms_ans": "Exothermic / negative / &minus;ve / heat (energy) given out",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1e",
        "questionNumber": "1(e)",
        "page": 3,
        "marks": 3,
        "topics": ["Equilibria"],
        "skills": ["Explanation"],
        "summary": "State and explain the effect on equilibrium yield of hydrogen if CO2 is removed.",
        "specRef": "3.1.6",
        "ms_label": "1(e)",
        "ms_ans": "Increase<br><br>Opposes the change<br><br>Moves to right / replace CO<sub>2</sub>",
        "ms_extra": "If this is wrong lose all marks in this section.<br>Allow favours forward reaction.",
        "ms_marks": "1<br><br>1<br><br>1",
        "figures": [Q1_FIG],
    },
    # Q2 (11 marks)
    {
        "id": f"{PAPER_ID}-q2ai",
        "questionNumber": "2(a)(i)",
        "page": 4,
        "marks": 1,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give the formula of the aluminium compound in bauxite.",
        "specRef": "3.2.4",
        "ms_label": "2(a)(i)",
        "ms_ans": "Al<sub>2</sub>O<sub>3</sub>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2aii",
        "questionNumber": "2(a)(ii)",
        "page": 4,
        "marks": 1,
        "topics": ["Extraction of Metals", "Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "State why aluminium electrolysis requires a molten electrolyte.",
        "specRef": "3.2.4",
        "ms_label": "2(a)(ii)",
        "ms_ans": "Ions move",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2aiii",
        "questionNumber": "2(a)(iii)",
        "page": 4,
        "marks": 1,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give one reason why molten bauxite alone is not used in aluminium electrolysis.",
        "specRef": "3.2.4",
        "ms_label": "2(a)(iii)",
        "ms_ans": "Lowers temp / m.p. bauxite too high",
        "ms_extra": "Must be temp related, not energy.",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2aiv",
        "questionNumber": "2(a)(iv)",
        "page": 4,
        "marks": 2,
        "topics": ["Extraction of Metals", "Redox"],
        "skills": ["Chemical Equations"],
        "summary": "Write half-equations for the electrode reactions in aluminium extraction.",
        "specRef": "3.2.4",
        "ms_label": "2(a)(iv)",
        "ms_ans": "Al<sup>3+</sup> + 3e<sup>&minus;</sup> &rarr; Al<br><br>2O<sup>2&minus;</sup> &rarr; O<sub>2</sub> + 4e<sup>&minus;</sup>",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2b",
        "questionNumber": "2(b)",
        "page": 4,
        "marks": 2,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "State two reasons why aluminium is recycled despite plentiful bauxite.",
        "specRef": "3.2.4",
        "ms_label": "2(b)",
        "ms_ans": "Any 2 from:<br>Conserves bauxite / prevents mining / prevents landfill / prevents eyesore on landscapes / saves energy or electricity / cost of purifying bauxite too high / reduces greenhouse gases",
        "ms_extra": "2 max",
        "ms_marks": "2",
    },
    {
        "id": f"{PAPER_ID}-q2ci",
        "questionNumber": "2(c)(i)",
        "page": 5,
        "marks": 2,
        "topics": ["Extraction of Metals"],
        "skills": ["Chemical Equations", "Knowledge & Recall"],
        "summary": "Write an equation and state a condition for the reduction of iron(III) oxide with CO.",
        "specRef": "3.2.4",
        "ms_label": "2(c)(i)",
        "ms_ans": "Fe<sub>2</sub>O<sub>3</sub> + 3CO &rarr; 2Fe + 3CO<sub>2</sub><br><br>High temp / 1500 &deg;C / accept temp in range 1000&ndash;2000 &deg;C",
        "ms_extra": "<br>Do not allow hot air",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2cii",
        "questionNumber": "2(c)(ii)",
        "page": 5,
        "marks": 1,
        "topics": ["Extraction of Metals", "Redox"],
        "skills": ["Knowledge & Recall"],
        "summary": "State the role of carbon monoxide in the reduction of iron(III) oxide.",
        "specRef": "3.2.4",
        "ms_label": "2(c)(ii)",
        "ms_ans": "Reducing agent / reductant / electron donor",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2ciii",
        "questionNumber": "2(c)(iii)",
        "page": 5,
        "marks": 1,
        "topics": ["Extraction of Metals", "Kinetics"],
        "skills": ["Explanation"],
        "summary": "Suggest why iron(III) oxide is more likely to react with CO than with carbon.",
        "specRef": "3.2.4",
        "ms_label": "2(c)(iii)",
        "ms_ans": "<u>CO</u> is a <u>gas</u> whereas <u>C</u> is a <u>solid</u>",
        "ms_extra": "QWC; Allow correct energy explanation.",
        "ms_marks": "1",
    },
    # Q3 (12 marks)
    {
        "id": f"{PAPER_ID}-q3a",
        "questionNumber": "3(a)",
        "page": 6,
        "marks": 2,
        "topics": ["Energetics"],
        "skills": ["Knowledge & Recall"],
        "summary": "Explain the meaning of the term enthalpy change of a reaction.",
        "specRef": "3.1.5",
        "ms_label": "3(a)",
        "ms_ans": "Heat (energy) change / required / needed<br><br>At constant / fixed pressure",
        "ms_extra": "<br>Lose 2nd mark if standard or a specified pressure.",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3b",
        "questionNumber": "3(b)",
        "page": 6,
        "marks": 2,
        "topics": ["Energetics"],
        "skills": ["Chemical Equations"],
        "summary": "Write an equation with state symbols for the standard enthalpy of formation of CS2(l).",
        "specRef": "3.1.5",
        "ms_label": "3(b)",
        "ms_ans": "C(s) + 2S(s) &rarr; CS<sub>2</sub>(l)",
        "ms_extra": "Accept &frac14; S<sub>8</sub> (not S<sub>2</sub>).<br>1 mark for equation and 1 mark for state symbols (conseq on first mark).",
        "ms_marks": "2",
    },
    {
        "id": f"{PAPER_ID}-q3c",
        "questionNumber": "3(c)",
        "page": 6,
        "marks": 3,
        "topics": ["Energetics"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the standard enthalpy of formation of carbon disulphide from enthalpy data.",
        "specRef": "3.1.5",
        "ms_label": "3(c)",
        "ms_ans": "&minus;1076 = &Sigma;&Delta;<i>H</i><sub>f</sub> products &minus; &Sigma;&Delta;<i>H</i><sub>f</sub> reactants<br>&minus;1076 = &minus;394 + (&minus;297 &times; 2) &minus; &Delta;<i>H</i><sub>f</sub>(CS<sub>2</sub>)<br>&minus;1076 = &minus;988 &minus; &Delta;<i>H</i><sub>f</sub>(CS<sub>2</sub>)<br>&Delta;<i>H</i><sub>f</sub>(CS<sub>2</sub>) = &minus;988 + 1076 = 88 kJ mol<sup>&minus;1</sup>",
        "ms_extra": "&minus;88 = 1 mark.<br>Ignore units even if incorrect.",
        "ms_marks": "1<br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3di",
        "questionNumber": "3(d)(i)",
        "page": 7,
        "marks": 4,
        "topics": ["Energetics"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the heat produced and molar enthalpy change of combustion of CS2 from calorimetry data.",
        "specRef": "3.1.5",
        "ms_label": "3(d)(i)",
        "ms_ans": "<i>Q</i> = <i>mc</i>&Delta;<i>T</i><br>= 75 &times; 4.2 &times; 8 = 2520 J<br>Moles = 0.45 / 76.2 = 0.00591<br>Molar heat change = 2520 / 0.00591 = &minus;427 (kJ or kJ mol<sup>&minus;1</sup>)",
        "ms_extra": "Last mark must show the minus sign and the correct answer.<br>Penalise wrong units. Accept range 424 &ndash; 427.",
        "ms_marks": "1<br>1<br>1<br>1",
    },
    {
        "id": f"{PAPER_ID}-q3dii",
        "questionNumber": "3(d)(ii)",
        "page": 7,
        "marks": 1,
        "topics": ["Energetics"],
        "skills": ["Practical Skills"],
        "summary": "Explain why the experimental enthalpy of combustion of CS2 is lower than the data book value.",
        "specRef": "3.1.5",
        "ms_label": "3(d)(ii)",
        "ms_ans": "Heat loss / incomplete combustion",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q3C_FIG],
    },
    # Q4 (9 marks)
    {
        "id": f"{PAPER_ID}-q4a",
        "questionNumber": "4(a)",
        "page": 8,
        "marks": 2,
        "topics": ["Redox"],
        "skills": ["Knowledge & Recall"],
        "summary": "Define reduction and reducing agent in terms of electrons.",
        "specRef": "3.1.6",
        "ms_label": "4(a)",
        "ms_ans": "Reduction: Gain of electrons<br><br>Reducing agent: Donates / gives / loses electrons",
        "ms_extra": "Penalise pairs in both parts.",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4b",
        "questionNumber": "4(b)",
        "page": 8,
        "marks": 3,
        "topics": ["Redox"],
        "skills": ["Application"],
        "summary": "Deduce the oxidation state of nitrogen in NaNO3, NO2, and Mg3N2.",
        "specRef": "3.1.6",
        "ms_label": "4(b)",
        "ms_ans": "(+)5<br>(+)4<br>&minus;3",
        "ms_extra": "",
        "ms_marks": "1<br>1<br>1",
    },
    {
        "id": f"{PAPER_ID}-q4ci",
        "questionNumber": "4(c)(i)",
        "page": 8,
        "marks": 1,
        "topics": ["Redox"],
        "skills": ["Chemical Equations"],
        "summary": "Write a half-equation for sulphur being converted into sulphuric acid.",
        "specRef": "3.1.6",
        "ms_label": "4(c)(i)",
        "ms_ans": "4H<sub>2</sub>O + S &rarr; H<sub>2</sub>SO<sub>4</sub> + 6H<sup>+</sup> + 6e<sup>&minus;</sup>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4cii",
        "questionNumber": "4(c)(ii)",
        "page": 8,
        "marks": 1,
        "topics": ["Redox"],
        "skills": ["Chemical Equations"],
        "summary": "Write a half-equation for nitric acid being converted into NO2 and water.",
        "specRef": "3.1.6",
        "ms_label": "4(c)(ii)",
        "ms_ans": "e<sup>&minus;</sup> + H<sup>+</sup> + HNO<sub>3</sub> &rarr; NO<sub>2</sub> + H<sub>2</sub>O",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4ciii",
        "questionNumber": "4(c)(iii)",
        "page": 8,
        "marks": 1,
        "topics": ["Redox"],
        "skills": ["Chemical Equations"],
        "summary": "Write the overall equation for concentrated nitric acid reacting with sulphur.",
        "specRef": "3.1.6",
        "ms_label": "4(c)(iii)",
        "ms_ans": "6HNO<sub>3</sub> + S &rarr; H<sub>2</sub>SO<sub>4</sub> + 6NO<sub>2</sub> + 2H<sub>2</sub>O",
        "ms_extra": "Allow uncancelled H<sup>+</sup> or H<sub>2</sub>O",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4civ",
        "questionNumber": "4(c)(iv)",
        "page": 8,
        "marks": 1,
        "topics": ["Redox"],
        "skills": ["Application"],
        "summary": "State the role of sulphur in its reaction with concentrated nitric acid.",
        "specRef": "3.1.6",
        "ms_label": "4(c)(iv)",
        "ms_ans": "Reducing agent / reductant / electron donor",
        "ms_extra": "",
        "ms_marks": "1",
    },
]


def extract_figures():
    doc = fitz.open(QP_PDF)
    crops = [
        (1, fitz.Rect(42, 140, 555, 465), Q1_FIG),  # Page 2: Q1 eq + concentration-time graph
        (5, fitz.Rect(42, 275, 555, 358), Q3C_FIG), # Page 6: Q3(c) CS2 combustion equation
    ]
    for pno, rect, rel in crops:
        pix = doc[pno].get_pixmap(clip=rect, dpi=200)
        pix.save(os.path.join(ROOT, rel))
        print(f"Saved figure {rel}")


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

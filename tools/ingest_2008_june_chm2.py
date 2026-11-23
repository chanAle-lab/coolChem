import json
import os
import sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2008-june-chm2"
QP_PDF = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471943570_80c22de0.pdf"
IMG_DIR = os.path.join(ROOT, "img", PAPER_ID)
MS_DIR = os.path.join(IMG_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2008,
    "series": "June",
    "unit": "CHM2",
    "level": "AS",
    "title": "CHM2 – Foundation Physical and Inorganic Chemistry",
    "date": "2008-06-04",
    "totalMarks": 60,
    "duration": "1 hour",
}

Q4_FIG = f"img/{PAPER_ID}/fig-q4-eq.jpg"

QUESTIONS = [
    # Q1 (14 marks)
    {
        "id": f"{PAPER_ID}-q1ai",
        "questionNumber": "1(a)(i)",
        "marks": 2,
        "topics": ["Extraction of Metals"],
        "skills": ["Chemical Equations"],
        "summary": "Write equations for the reduction of titanium(IV) chloride using sodium and using hydrogen.",
        "specRef": "3.2.4",
        "ms_label": "1(a)(i)",
        "ms_ans": "TiCl<sub>4</sub> + 4Na &rarr; Ti + 4NaCl<br><br>TiCl<sub>4</sub> + 2H<sub>2</sub> &rarr; Ti + 4HCl",
        "ms_extra": "Accept multiples<br><br>Accept multiples; Not [H]<br>Penalise CL, NA, h once",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1aii",
        "questionNumber": "1(a)(ii)",
        "marks": 1,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give one reason, other than cost, why hydrogen is not the preferred reducing agent for titanium extraction.",
        "specRef": "3.2.4",
        "ms_label": "1(a)(ii)",
        "ms_ans": "Hydrogen/it is explosive / HCl is an acid / forms an acid / hydrogen stored under high pressure / HCl corrosive / HCl toxic / HCl reacts with metal",
        "ms_extra": "Not flammable or dangerous alone<br>Not HCl produced",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1b",
        "questionNumber": "1(b)",
        "marks": 1,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "Suggest why carbon is not a suitable reducing agent for the extraction of titanium.",
        "specRef": "3.2.4",
        "ms_label": "1(b)",
        "ms_ans": "Titanium carbide forms / TiC forms / Ti goes brittle",
        "ms_extra": "Not Ti reacts with C",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1ci",
        "questionNumber": "1(c)(i)",
        "marks": 2,
        "topics": ["Extraction of Metals"],
        "skills": ["Chemical Equations", "Knowledge & Recall"],
        "summary": "Write an equation and state a condition for the reduction of iron(III) oxide with carbon.",
        "specRef": "3.2.4",
        "ms_label": "1(c)(i)",
        "ms_ans": "Fe<sub>2</sub>O<sub>3</sub> + 3C &rarr; 2Fe + 3CO<br>or 2Fe<sub>2</sub>O<sub>3</sub> + 3C &rarr; 4Fe + 3CO<sub>2</sub><br><br>High temperature / 1500 &deg;C",
        "ms_extra": "Accept multiples<br>Not equations from Fe<sub>3</sub>O<sub>4</sub> or FeO<br><br>Accept in range 1000&ndash;2000 &deg;C<br>Do not accept heat",
        "ms_marks": "1<br><br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1cii",
        "questionNumber": "1(c)(ii)",
        "marks": 3,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall", "Chemical Equations"],
        "summary": "Name the raw material used to remove SiO2 impurity in iron extraction and write equations for slag formation.",
        "specRef": "3.2.4",
        "ms_label": "1(c)(ii)",
        "ms_ans": "Limestone / calcium carbonate<br><br>CaCO<sub>3</sub> &rarr; CaO + CO<sub>2</sub><br>CaO + SiO<sub>2</sub> &rarr; CaSiO<sub>3</sub>",
        "ms_extra": "Must have name; penalise contradiction of name and formula<br><br>Allow CaCO<sub>3</sub> + SiO<sub>2</sub> &rarr; CaSiO<sub>3</sub> + CO<sub>2</sub> for 2 marks; allow multiples",
        "ms_marks": "1<br><br>1<br>1",
    },
    {
        "id": f"{PAPER_ID}-q1ciii",
        "questionNumber": "1(c)(iii)",
        "marks": 1,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "State one use of slag.",
        "specRef": "3.2.4",
        "ms_label": "1(c)(iii)",
        "ms_ans": "roads / breezeblocks / concrete slabs / cement / tarmac / ballast for railway sleepers / insulation blocks / hard core / aggregate",
        "ms_extra": "Not just building materials / blocks / bricks",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1di",
        "questionNumber": "1(d)(i)",
        "marks": 2,
        "topics": ["Extraction of Metals", "Redox"],
        "skills": ["Chemical Equations"],
        "summary": "Write half-equations for both electrode reactions in the extraction of aluminium.",
        "specRef": "3.2.4",
        "ms_label": "1(d)(i)",
        "ms_ans": "Al<sup>3+</sup> + 3e<sup>&minus;</sup> &rarr; Al<br><br>2O<sup>2&minus;</sup> &rarr; O<sub>2</sub> + 4e<sup>&minus;</sup>",
        "ms_extra": "Accept multiples<br><br>Not O",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1dii",
        "questionNumber": "1(d)(ii)",
        "marks": 1,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give one reason why cryolite is used in aluminium extraction.",
        "specRef": "3.2.4",
        "ms_label": "1(d)(ii)",
        "ms_ans": "Lowers melting point / solvent / dissolves bauxite / reduces temperature",
        "ms_extra": "Not lowers mp of Al; Lowers mp of Al<sub>2</sub>O<sub>3</sub> is OK<br>Ignore temps if quoted; Not conductor/catalyst",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1e",
        "questionNumber": "1(e)",
        "marks": 1,
        "topics": ["Extraction of Metals"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give the major reason why recycling aluminium is economically viable.",
        "specRef": "3.2.4",
        "ms_label": "1(e)",
        "ms_ans": "Saves energy / saves electricity",
        "ms_extra": "Ignore cost / mining / melting<br>Can have comparison answers w.r.t. electrolysis",
        "ms_marks": "1",
    },
    # Q2 (10 marks)
    {
        "id": f"{PAPER_ID}-q2a",
        "questionNumber": "2(a)",
        "marks": 3,
        "topics": ["Energetics"],
        "skills": ["Knowledge & Recall"],
        "summary": "Define the term standard enthalpy of combustion.",
        "specRef": "3.1.5",
        "ms_label": "2(a)",
        "ms_ans": "Enthalpy change when 1 mole of substance<br><br>Completely burns or reacts in oxygen / burns in XS oxygen<br><br>Under standard conditions",
        "ms_extra": "Accept heat energy change<br><br>Not in air<br><br>298 K and 100 kPa; Accept 1 bar; Not 1 atm",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2b",
        "questionNumber": "2(b)",
        "marks": 1,
        "topics": ["Energetics"],
        "skills": ["Knowledge & Recall"],
        "summary": "State Hess's Law.",
        "specRef": "3.1.5",
        "ms_label": "2(b)",
        "ms_ans": "Enthalpy change is independent of the route taken",
        "ms_extra": "Accept heat energy change",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2c",
        "questionNumber": "2(c)",
        "marks": 3,
        "topics": ["Energetics"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the standard enthalpy of formation of buta-1,3-diene from enthalpy of combustion data.",
        "specRef": "3.1.5",
        "ms_label": "2(c)",
        "ms_ans": "(&Delta;<i>H</i><sub>f</sub>) = &Sigma;&Delta;<i>H</i><sub>reactants</sub> &minus; &Sigma;&Delta;<i>H</i><sub>products</sub><br>= (&minus;394 &times; 4) + (&minus;286 &times; 3) &minus; (&minus;2542)<br>= &minus;2434 &minus; (&minus;2542)<br>= (+) 108 (kJ mol<sup>&minus;1</sup>)",
        "ms_extra": "allow &Delta;<i>H</i><sub>c</sub> C<sub>4</sub>H<sub>6</sub> = &Sigma;&Delta;<i>H</i><sub>prods</sub> &minus; &Sigma;&Delta;<i>H</i><sub>reacts</sub> or good cycle as alternative to M1<br>If +108 give 3 ticks; ignore units even if wrong<br>&minus;108 = 1 mark; If AE for M2 mark on for M3",
        "ms_marks": "1<br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2d",
        "questionNumber": "2(d)",
        "marks": 3,
        "topics": ["Energetics"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the C=C bond enthalpy from the enthalpy of hydrogenation of buta-1,3-diene.",
        "specRef": "3.1.5",
        "ms_label": "2(d)",
        "ms_ans": "&Delta;<i>H</i> / &minus;240 = &Sigma;Bonds broken &minus; &Sigma;Bonds made<br>&minus;240 = (6 &times; 412) + 2(C=C) + 348 + (2 &times; 436) &minus; [(3 &times; 348) + (10 &times; 412)]<br>&minus;240 = 3692 + 2(C=C) &minus; 5164<br>2(C=C) = 1232<br>C=C = 616 (kJ mol<sup>&minus;1</sup>)",
        "ms_extra": "Allow &minus;240 = 2(C=C) + 872 &minus; (696 + 1648)<br>If 616 give 3 ticks; If 1232 give 2 ticks; Ignore units<br>Last mark is for &divide;2; &minus;616 = max 1",
        "ms_marks": "1<br>1<br><br><br>1",
    },
    # Q3 (12 marks)
    {
        "id": f"{PAPER_ID}-q3a",
        "questionNumber": "3(a)",
        "marks": 1,
        "topics": ["Redox"],
        "skills": ["Knowledge & Recall"],
        "summary": "State, in terms of electrons, what happens to an oxidising agent in a redox reaction.",
        "specRef": "3.1.6",
        "ms_label": "3(a)",
        "ms_ans": "Gains / receives / accepts / takes electrons",
        "ms_extra": "Not pairs of electrons",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3bi",
        "questionNumber": "3(b)(i)",
        "marks": 1,
        "topics": ["Redox", "Group 7"],
        "skills": ["Chemical Equations"],
        "summary": "Write a half-equation showing how SO2 is formed from concentrated sulphuric acid.",
        "specRef": "3.2.3",
        "ms_label": "3(b)(i)",
        "ms_ans": "H<sub>2</sub>SO<sub>4</sub> + 2H<sup>+</sup> + 2e<sup>&minus;</sup> &rarr; SO<sub>2</sub> + 2H<sub>2</sub>O<br>or SO<sub>4</sub><sup>2&minus;</sup> + 4H<sup>+</sup> + 2e<sup>&minus;</sup> &rarr; SO<sub>2</sub> + 2H<sub>2</sub>O",
        "ms_extra": "allow multiples",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3bii",
        "questionNumber": "3(b)(ii)",
        "marks": 1,
        "topics": ["Redox", "Group 7"],
        "skills": ["Chemical Equations"],
        "summary": "Write a half-equation showing how Br2 is formed from Br- ions.",
        "specRef": "3.2.3",
        "ms_label": "3(b)(ii)",
        "ms_ans": "2Br<sup>&minus;</sup> &rarr; Br<sub>2</sub> + 2e<sup>&minus;</sup>",
        "ms_extra": "allow multiples",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3biii",
        "questionNumber": "3(b)(iii)",
        "marks": 1,
        "topics": ["Redox", "Group 7"],
        "skills": ["Chemical Equations"],
        "summary": "Write an overall equation for the reaction of Br- ions with concentrated sulphuric acid.",
        "specRef": "3.2.3",
        "ms_label": "3(b)(iii)",
        "ms_ans": "H<sub>2</sub>SO<sub>4</sub> + 2H<sup>+</sup> + 2Br<sup>&minus;</sup> &rarr; SO<sub>2</sub> + Br<sub>2</sub> + 2H<sub>2</sub>O<br>or SO<sub>4</sub><sup>2&minus;</sup> + 4H<sup>+</sup> + 2Br<sup>&minus;</sup> &rarr; SO<sub>2</sub> + Br<sub>2</sub> + 2H<sub>2</sub>O",
        "ms_extra": "allow multiples; penalise BR, br, h once in (b)(i), (ii) and (iii)<br>allow equation with 2HBr; accept equation with NaBr and spectator Na<sup>+</sup> on RHS",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3biv",
        "questionNumber": "3(b)(iv)",
        "marks": 1,
        "topics": ["Redox", "Group 7"],
        "skills": ["Application"],
        "summary": "Deduce the role of Br- ions in their reaction with concentrated sulphuric acid.",
        "specRef": "3.2.3",
        "ms_label": "3(b)(iv)",
        "ms_ans": "Reducing agent / electron donor / reduces sulphuric acid / reduces H<sub>2</sub>SO<sub>4</sub>",
        "ms_extra": "Not electron proton donor i.e. contradictions",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3ci",
        "questionNumber": "3(c)(i)",
        "marks": 1,
        "topics": ["Group 7"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify a halide ion that does not produce SO2 when reacted with concentrated sulphuric acid.",
        "specRef": "3.2.3",
        "ms_label": "3(c)(i)",
        "ms_ans": "Cl<sup>&minus;</sup> or F<sup>&minus;</sup> or chloride or fluoride",
        "ms_extra": "Not chlorine / Cl / fluorine / F / chlorine ion / fluorine ion",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3cii",
        "questionNumber": "3(c)(ii)",
        "marks": 1,
        "topics": ["Group 7"],
        "skills": ["Chemical Equations"],
        "summary": "Write an equation for the reaction of concentrated sulphuric acid with Cl- or F-.",
        "specRef": "3.2.3",
        "ms_label": "3(c)(ii)",
        "ms_ans": "Cl<sup>&minus;</sup> + H<sub>2</sub>SO<sub>4</sub> &rarr; HCl + HSO<sub>4</sub><sup>&minus;</sup><br>(or with F<sup>&minus;</sup>, NaCl, NaF; or 2NaCl + H<sub>2</sub>SO<sub>4</sub> &rarr; 2HCl + Na<sub>2</sub>SO<sub>4</sub>)",
        "ms_extra": "Allow multiples",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3ciii",
        "questionNumber": "3(c)(iii)",
        "marks": 1,
        "topics": ["Group 7"],
        "skills": ["Knowledge & Recall"],
        "summary": "State the role of sulphuric acid in its reaction with Cl- or F-.",
        "specRef": "3.2.3",
        "ms_label": "3(c)(iii)",
        "ms_ans": "Acid / proton donor",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3d",
        "questionNumber": "3(d)",
        "marks": 1,
        "topics": ["Redox", "Group 7"],
        "skills": ["Application"],
        "summary": "Deduce the role of Cl2 in its reaction with aqueous sodium bromide.",
        "specRef": "3.2.3",
        "ms_label": "3(d)",
        "ms_ans": "Oxidising agent / electron acceptor / oxidises NaBr / oxidises Br<sup>&minus;</sup>",
        "ms_extra": "Not electron pair acceptor",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3ei",
        "questionNumber": "3(e)(i)",
        "marks": 1,
        "topics": ["Group 7"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify a halide ion whose silver nitrate precipitate dissolves completely in dilute ammonia.",
        "specRef": "3.2.3",
        "ms_label": "3(e)(i)",
        "ms_ans": "Cl<sup>&minus;</sup> or chloride",
        "ms_extra": "Not chlorine / Cl / chlorine ion",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3eii",
        "questionNumber": "3(e)(ii)",
        "marks": 1,
        "topics": ["Group 7"],
        "skills": ["Chemical Equations"],
        "summary": "Write an ionic equation for the reaction between silver nitrate and chloride ions.",
        "specRef": "3.2.3",
        "ms_label": "3(e)(ii)",
        "ms_ans": "Ag<sup>+</sup> + Cl<sup>&minus;</sup> &rarr; AgCl<br>or AgNO<sub>3</sub> + Cl<sup>&minus;</sup> &rarr; AgCl + NO<sub>3</sub><sup>&minus;</sup>",
        "ms_extra": "Accept multiples",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3eiii",
        "questionNumber": "3(e)(iii)",
        "marks": 1,
        "topics": ["Group 7"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify the halide ion that cannot be detected using silver nitrate.",
        "specRef": "3.2.3",
        "ms_label": "3(e)(iii)",
        "ms_ans": "F<sup>&minus;</sup> or fluoride",
        "ms_extra": "Not fluorine / F / fluorine ion",
        "ms_marks": "1",
    },
    # Q4 (9 marks)
    {
        "id": f"{PAPER_ID}-q4a",
        "questionNumber": "4(a)",
        "marks": 1,
        "topics": ["Equilibria"],
        "skills": ["Knowledge & Recall"],
        "summary": "Explain why reactant and product concentrations remain constant at equilibrium.",
        "specRef": "3.1.6",
        "ms_label": "4(a)",
        "ms_ans": "Rate of forward reaction = rate of backward reaction",
        "ms_extra": "Accept speed of F reaction = speed of B reaction<br>Accept rate of both rxns is same; Not speeds are constant",
        "ms_marks": "1",
        "figures": [Q4_FIG],
    },
    {
        "id": f"{PAPER_ID}-q4bi",
        "questionNumber": "4(b)(i)",
        "marks": 2,
        "topics": ["Equilibria"],
        "skills": ["Explanation"],
        "summary": "Explain why a high temperature is needed for a high equilibrium yield of hydrogen.",
        "specRef": "3.1.6",
        "ms_label": "4(b)(i)",
        "ms_ans": "Reaction is endothermic<br><br>System moves to absorb heat / oppose or counter change / decrease temp",
        "ms_extra": "If exo CE = 0",
        "ms_marks": "1<br><br>1",
        "figures": [Q4_FIG],
    },
    {
        "id": f"{PAPER_ID}-q4bii",
        "questionNumber": "4(b)(ii)",
        "marks": 1,
        "topics": ["Equilibria"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give one disadvantage of using temperatures much higher than 1000 C.",
        "specRef": "3.1.6",
        "ms_label": "4(b)(ii)",
        "ms_ans": "Cost (of energy) is high / expensive / amount of energy is high<br>or safety factor with a reason",
        "ms_extra": "Not dangerous",
        "ms_marks": "1",
        "figures": [Q4_FIG],
    },
    {
        "id": f"{PAPER_ID}-q4c",
        "questionNumber": "4(c)",
        "marks": 3,
        "topics": ["Equilibria"],
        "skills": ["Explanation"],
        "summary": "State and explain how overall pressure must be changed to increase equilibrium yield of hydrogen.",
        "specRef": "3.1.6",
        "ms_label": "4(c)",
        "ms_ans": "Decrease<br><br>2 moles on left and 4 moles on right / more moles on right / goes to side with more moles<br><br>System opposes change / increases pressure",
        "ms_extra": "If trend wrong CE = 0; If blank mark on<br>If no&rsquo;s they must be correct",
        "ms_marks": "1<br><br>1<br><br>1",
        "figures": [Q4_FIG],
    },
    {
        "id": f"{PAPER_ID}-q4d",
        "questionNumber": "4(d)",
        "marks": 2,
        "topics": ["Equilibria", "Kinetics"],
        "skills": ["Explanation"],
        "summary": "Explain why adding a catalyst has no effect on the equilibrium yield of hydrogen.",
        "specRef": "3.1.6",
        "ms_label": "4(d)",
        "ms_ans": "Changes / speeds up / increases the rate of both the forward and backward reactions<br><br>equally",
        "ms_extra": "Look for rate/speed and change/increase rate<br><br>Dependent on first mark",
        "ms_marks": "1<br><br>1",
        "figures": [Q4_FIG],
    },
]


def extract_figures():
    doc = fitz.open(QP_PDF)
    page = doc[7]  # Page 8 (0-indexed 7)
    rect = fitz.Rect(42, 65, 555, 118)
    pix = page.get_pixmap(clip=rect, dpi=200)
    out = os.path.join(ROOT, Q4_FIG)
    pix.save(out)
    print(f"Saved figure {Q4_FIG}")


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
            "questionNumber": q["questionNumber"],
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

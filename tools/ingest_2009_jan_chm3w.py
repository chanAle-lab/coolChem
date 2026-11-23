import json
import os
import sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2009-jan-chm3w"
QP_PDF = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472300683_c1be80ef.pdf"
IMG_DIR = os.path.join(ROOT, "img", PAPER_ID)
MS_DIR = os.path.join(IMG_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2009,
    "series": "January",
    "unit": "CHM3/W",
    "level": "AS",
    "title": "CHM3/W – Introduction to Organic Chemistry (Section A)",
    "date": "2009-01-09",
    "totalMarks": 60,
    "duration": "1 hour",
}

Q1_FIG = f"img/{PAPER_ID}/fig-q1-scheme.jpg"
Q2_FIG = f"img/{PAPER_ID}/fig-q2-scheme.jpg"
Q2D_FIG = f"img/{PAPER_ID}/fig-q2d.jpg"
Q4_FIG = f"img/{PAPER_ID}/fig-q4-eqn.jpg"

QUESTIONS = [
    # Q1 (8 marks)
    {
        "id": f"{PAPER_ID}-q1a",
        "questionNumber": "1(a)",
        "page": 2,
        "marks": 1,
        "topics": ["Alkanes", "Reaction Mechanisms"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of mechanism in Reaction 1 (cyclohexane to chlorocyclohexane).",
        "specRef": "3.3.1",
        "ms_label": "1(a)",
        "ms_ans": "(free) radical substitution",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1b",
        "questionNumber": "1(b)",
        "page": 2,
        "marks": 1,
        "topics": ["Haloalkanes", "Reaction Mechanisms"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of mechanism in Reaction 2 (chlorocyclohexane to cyclohexanol with KOH(aq)).",
        "specRef": "3.3.2",
        "ms_label": "1(b)",
        "ms_ans": "nucleophilic substitution",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1c",
        "questionNumber": "1(c)",
        "page": 2,
        "marks": 1,
        "topics": ["Alcohols", "Alkenes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify a catalyst for Reaction 3 (dehydration of cyclohexanol to cyclohexene).",
        "specRef": "3.3.4",
        "ms_label": "1(c)",
        "ms_ans": "concentrated H<sub>2</sub>SO<sub>4</sub> / concentrated H<sub>3</sub>PO<sub>4</sub> / Al<sub>2</sub>O<sub>3</sub> (or H<sup>+</sup> / acid)",
        "ms_extra": "Must be concentrated if sulphuric or phosphoric acid is stated",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1di",
        "questionNumber": "1(d)(i)",
        "page": 3,
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Application"],
        "summary": "State the class of alcohols to which cyclohexanol belongs.",
        "specRef": "3.3.4",
        "ms_label": "1(d)(i)",
        "ms_ans": "secondary (or 2&deg;)",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1dii",
        "questionNumber": "1(d)(ii)",
        "page": 3,
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify the functional group formed when cyclohexanol is oxidised by acidified potassium dichromate(VI).",
        "specRef": "3.3.4",
        "ms_label": "1(d)(ii)",
        "ms_ans": "ketone / carbonyl / C=O",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1ei",
        "questionNumber": "1(e)(i)",
        "page": 3,
        "marks": 1,
        "topics": ["Alkenes"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term unsaturated as applied to a hydrocarbon.",
        "specRef": "3.3.3",
        "ms_label": "1(e)(i)",
        "ms_ans": "contains a C=C / carbon&ndash;carbon double bond (or multiple bond)",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q1_FIG],
    },
    {
        "id": f"{PAPER_ID}-q1eii",
        "questionNumber": "1(e)(ii)",
        "page": 3,
        "marks": 2,
        "topics": ["Alkenes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify a reagent and a catalyst for Reaction 4 (cyclohexene to cyclohexane).",
        "specRef": "3.3.3",
        "ms_label": "1(e)(ii)",
        "ms_ans": "Reagent: hydrogen / H<sub>2</sub><br><br>Catalyst: nickel / Ni (or Pd / Pt)",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
        "figures": [Q1_FIG],
    },
    # Q2 (13 marks)
    {
        "id": f"{PAPER_ID}-q2a",
        "questionNumber": "2(a)",
        "page": 4,
        "marks": 1,
        "topics": ["Haloalkanes", "Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Name the major product of the reaction between methylpropene and hydrogen bromide.",
        "specRef": "3.3.3",
        "ms_label": "2(a)",
        "ms_ans": "2-bromo-2-methylpropane",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2b",
        "questionNumber": "2(b)",
        "page": 4,
        "marks": 5,
        "topics": ["Alkenes", "Reaction Mechanisms"],
        "skills": ["Application"],
        "summary": "Name and outline the mechanism for the reaction between methylpropene and hydrogen bromide.",
        "specRef": "3.3.3",
        "ms_label": "2(b)",
        "ms_ans": "Electrophilic addition<br><br>Mechanism:<br>&bull; Curly arrow from C=C double bond to H of H&ndash;Br (with &delta;+ on H, &delta;&minus; on Br)<br>&bull; Curly arrow from H&ndash;Br bond to Br<br>&bull; Correct tertiary carbocation intermediate (CH<sub>3</sub>)<sub>2</sub>C<sup>+</sup>CH<sub>3</sub><br>&bull; Curly arrow from lone pair on Br<sup>&minus;</sup> to C<sup>+</sup>",
        "ms_extra": "Penalise wrong carbocation",
        "ms_marks": "1<br><br>4",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2ci",
        "questionNumber": "2(c)(i)",
        "page": 4,
        "marks": 1,
        "topics": ["Alkenes", "Haloalkanes"],
        "skills": ["Application"],
        "summary": "Draw the structure of the minor product formed when methylpropene reacts with hydrogen bromide.",
        "specRef": "3.3.3",
        "ms_label": "2(c)(i)",
        "ms_ans": "(CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>Br (1-bromo-2-methylpropane)",
        "ms_extra": "Must show structure clearly",
        "ms_marks": "1",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2cii",
        "questionNumber": "2(c)(ii)",
        "page": 5,
        "marks": 2,
        "topics": ["Alkenes", "Reaction Mechanisms"],
        "skills": ["Explanation"],
        "summary": "Explain why only a relatively small amount of the minor product is formed.",
        "specRef": "3.3.3",
        "ms_label": "2(c)(ii)",
        "ms_ans": "Formed via primary carbocation (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub><sup>+</sup><br><br>Primary carbocation is less stable than tertiary carbocation (CH<sub>3</sub>)<sub>3</sub>C<sup>+</sup>",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2di",
        "questionNumber": "2(d)(i)",
        "page": 5,
        "marks": 1,
        "topics": ["Alkenes", "Alcohols"],
        "skills": ["Application"],
        "summary": "State the overall role of the sulphuric acid in the two-stage conversion of methylpropene to a tertiary alcohol.",
        "specRef": "3.3.3",
        "ms_label": "2(d)(i)",
        "ms_ans": "catalyst",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q2D_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2dii",
        "questionNumber": "2(d)(ii)",
        "page": 5,
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of reaction in Stage 2 (reaction of alkyl hydrogensulphate with water).",
        "specRef": "3.3.3",
        "ms_label": "2(d)(ii)",
        "ms_ans": "hydrolysis (or nucleophilic substitution)",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q2D_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2diii",
        "questionNumber": "2(d)(iii)",
        "page": 5,
        "marks": 1,
        "topics": ["Alcohols", "Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Name the tertiary alcohol formed by this two-stage process.",
        "specRef": "3.3.4",
        "ms_label": "2(d)(iii)",
        "ms_ans": "(2-)methylpropan-2-ol",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q2D_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2div",
        "questionNumber": "2(d)(iv)",
        "page": 5,
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Explanation"],
        "summary": "State why tertiary alcohols are resistant to oxidation by acidified potassium dichromate(VI).",
        "specRef": "3.3.4",
        "ms_label": "2(d)(iv)",
        "ms_ans": "No H atom bonded to the C atom attached to the OH group (or would require breaking a C&ndash;C bond)",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q2D_FIG],
    },
    # Q3 (8 marks)
    {
        "id": f"{PAPER_ID}-q3a",
        "questionNumber": "3(a)",
        "page": 6,
        "marks": 3,
        "topics": ["Amount of Substance", "Alcohols"],
        "skills": ["Application"],
        "summary": "Give the empirical formula of glucose and name the two different types of functional group present.",
        "specRef": "3.1.2",
        "ms_label": "3(a)",
        "ms_ans": "Empirical formula: CH<sub>2</sub>O<br><br>Functional group 1: alcohol / hydroxyl (OH)<br><br>Functional group 2: aldehyde (CHO)",
        "ms_extra": "",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3bi",
        "questionNumber": "3(b)(i)",
        "page": 6,
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the process converting aqueous glucose into ethanol and carbon dioxide.",
        "specRef": "3.3.4",
        "ms_label": "3(b)(i)",
        "ms_ans": "fermentation",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3bii",
        "questionNumber": "3(b)(ii)",
        "page": 6,
        "marks": 1,
        "topics": ["Alcohols", "Amount of Substance"],
        "skills": ["Application"],
        "summary": "Write an equation for the fermentation of glucose.",
        "specRef": "3.3.4",
        "ms_label": "3(b)(ii)",
        "ms_ans": "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> &rarr; 2CH<sub>3</sub>CH<sub>2</sub>OH + 2CO<sub>2</sub>",
        "ms_extra": "Allow C<sub>2</sub>H<sub>5</sub>OH",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3biii",
        "questionNumber": "3(b)(iii)",
        "page": 6,
        "marks": 2,
        "topics": ["Alcohols"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give two disadvantages (excluding cost) of making ethanol by fermentation on a large scale.",
        "specRef": "3.3.4",
        "ms_label": "3(b)(iii)",
        "ms_ans": "Any two from:<br>&bull; slow rate of reaction<br>&bull; batch process<br>&bull; impure product / low yield (~15% ethanol) / requires fractional distillation<br>&bull; requires land/crops that could be used for food",
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "id": f"{PAPER_ID}-q3biv",
        "questionNumber": "3(b)(iv)",
        "page": 6,
        "marks": 1,
        "topics": ["Alcohols", "Energetics"],
        "skills": ["Application"],
        "summary": "Write an equation for the complete combustion of ethanol.",
        "specRef": "3.3.4",
        "ms_label": "3(b)(iv)",
        "ms_ans": "CH<sub>3</sub>CH<sub>2</sub>OH + 3O<sub>2</sub> &rarr; 2CO<sub>2</sub> + 3H<sub>2</sub>O",
        "ms_extra": "Allow C<sub>2</sub>H<sub>5</sub>OH or multiples",
        "ms_marks": "1",
    },
    # Q4 (7 marks)
    {
        "id": f"{PAPER_ID}-q4a",
        "questionNumber": "4(a)",
        "page": 7,
        "marks": 5,
        "topics": ["Haloalkanes", "Reaction Mechanisms"],
        "skills": ["Application"],
        "summary": "Name and outline a mechanism for the reaction of ammonia with 1-bromobutane.",
        "specRef": "3.3.2",
        "ms_label": "4(a)",
        "ms_ans": "Nucleophilic substitution<br><br>Mechanism:<br>&bull; Curly arrow from lone pair on N of NH<sub>3</sub> to C of C&ndash;Br<br>&bull; Curly arrow from C&ndash;Br bond to Br<br>&bull; Correct alkylammonium ion intermediate CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>N<sup>+</sup>H<sub>3</sub><br>&bull; Curly arrow from N&ndash;H bond to N<sup>+</sup> (with second NH<sub>3</sub> removing H<sup>+</sup>)",
        "ms_extra": "",
        "ms_marks": "1<br><br>4",
        "figures": [Q4_FIG],
    },
    {
        "id": f"{PAPER_ID}-q4b",
        "questionNumber": "4(b)",
        "page": 7,
        "marks": 2,
        "topics": ["Haloalkanes", "Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Name compound Q (CH3CH2CH2CH2NH2) and draw the structure of a position isomer of Q.",
        "specRef": "3.3.2",
        "ms_label": "4(b)",
        "ms_ans": "Name of Q: butylamine / 1-butylamine / butan-1-amine / 1-aminobutane<br><br>Position isomer: CH<sub>3</sub>CH<sub>2</sub>CH(NH<sub>2</sub>)CH<sub>3</sub>",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
        "figures": [Q4_FIG],
    },
    # Q5 (9 marks)
    {
        "id": f"{PAPER_ID}-q5a",
        "questionNumber": "5(a)",
        "page": 8,
        "marks": 4,
        "topics": ["Haloalkanes", "Reaction Mechanisms"],
        "skills": ["Application"],
        "summary": "Name and outline a mechanism for the formation of but-2-ene from 2-bromobutane with NaOH.",
        "specRef": "3.3.2",
        "ms_label": "5(a)",
        "ms_ans": "Elimination<br><br>Mechanism:<br>&bull; Curly arrow from lone pair on HO<sup>&minus;</sup> to an H atom on C3 (adjacent to C&ndash;Br)<br>&bull; Curly arrow from C&ndash;H bond to form C=C double bond<br>&bull; Curly arrow from C&ndash;Br bond to Br",
        "ms_extra": "H attacked must lead to but-2-ene (i.e. on C3, not C1)",
        "ms_marks": "1<br><br>3",
    },
    {
        "id": f"{PAPER_ID}-q5bi",
        "questionNumber": "5(b)(i)",
        "page": 8,
        "marks": 2,
        "topics": ["Alkenes", "Nomenclature & Isomerism"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term stereoisomers.",
        "specRef": "3.3.3",
        "ms_label": "5(b)(i)",
        "ms_ans": "Same structural formula<br><br>Different arrangement of atoms / groups in space",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q5bii",
        "questionNumber": "5(b)(ii)",
        "page": 8,
        "marks": 1,
        "topics": ["Alkenes", "Nomenclature & Isomerism"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of stereoisomerism shown by but-2-ene.",
        "specRef": "3.3.3",
        "ms_label": "5(b)(ii)",
        "ms_ans": "geometric(al) / <i>cis</i>&ndash;<i>trans</i> / <i>E</i>&ndash;<i>Z</i>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q5biii",
        "questionNumber": "5(b)(iii)",
        "page": 8,
        "marks": 2,
        "topics": ["Alkenes", "Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Draw and name the structures of the two stereoisomers of but-2-ene.",
        "specRef": "3.3.3",
        "ms_label": "5(b)(iii)",
        "ms_ans": "Stereoisomer 1: <i>cis</i>-but-2-ene / (<i>Z</i>)-but-2-ene (both CH<sub>3</sub> groups on same side of C=C)<br><br>Stereoisomer 2: <i>trans</i>-but-2-ene / (<i>E</i>)-but-2-ene (CH<sub>3</sub> groups on opposite sides of C=C)",
        "ms_extra": "1 mark for each correct structure matched to its name",
        "ms_marks": "1<br><br>1",
    },
]


def extract_figures():
    doc = fitz.open(QP_PDF)
    crops = [
        (1, fitz.Rect(42, 145, 555, 505), Q1_FIG),
        (3, fitz.Rect(42, 68, 555, 172), Q2_FIG),
        (4, fitz.Rect(42, 236, 555, 408), Q2D_FIG),
        (6, fitz.Rect(42, 68, 555, 142), Q4_FIG),
    ]
    for p_idx, rect, rel_path in crops:
        pix = doc[p_idx].get_pixmap(clip=rect, dpi=200)
        pix.save(os.path.join(ROOT, rel_path))
        print(f"Saved figure {rel_path}")


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

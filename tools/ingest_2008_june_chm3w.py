import json
import os
import sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2008-june-chm3w"
QP_PDF = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471943585_f4dd83b9.pdf"
IMG_DIR = os.path.join(ROOT, "img", PAPER_ID)
MS_DIR = os.path.join(IMG_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2008,
    "series": "June",
    "unit": "CHM3/W",
    "level": "AS",
    "title": "CHM3/W – Introduction to Organic Chemistry",
    "date": "2008-06-04",
    "totalMarks": 60,
    "duration": "1 hour",
}

Q2_FIG = f"img/{PAPER_ID}/fig-q2-table.jpg"
Q4_FIG = f"img/{PAPER_ID}/fig-q4-scheme.jpg"
Q5_FIG = f"img/{PAPER_ID}/fig-q5-conv.jpg"

QUESTIONS = [
    # Q1 (8 marks)
    {
        "id": f"{PAPER_ID}-q1ai",
        "questionNumber": "1(a)(i)",
        "marks": 1,
        "topics": ["Alkanes"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term hydrocarbon.",
        "specRef": "3.3.2",
        "ms_label": "1(a)(i)",
        "ms_ans": "A compound OR molecule containing OR consisting of hydrogen and carbon only",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1aii",
        "questionNumber": "1(a)(ii)",
        "marks": 1,
        "topics": ["Alkanes"],
        "skills": ["Chemical Equations"],
        "summary": "Write an equation for the incomplete combustion of nonane (C9H20) to form CO and H2O.",
        "specRef": "3.3.2",
        "ms_label": "1(a)(ii)",
        "ms_ans": "C<sub>9</sub>H<sub>20</sub> + 9&frac12;O<sub>2</sub> &rarr; 9CO + 10H<sub>2</sub>O",
        "ms_extra": "Or multiple",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1aiii",
        "questionNumber": "1(a)(iii)",
        "marks": 2,
        "topics": ["Alkanes"],
        "skills": ["Knowledge & Recall", "Chemical Equations"],
        "summary": "State one essential condition and write an equation for the formation of NO from air in a petrol engine.",
        "specRef": "3.3.2",
        "ms_label": "1(a)(iii)",
        "ms_ans": "M1: High temperature OR spark OR 2500 &deg;C &le; <i>T</i> &le; 4000 &deg;C<br><br>M2: &frac12;N<sub>2</sub> + &frac12;O<sub>2</sub> &rarr; NO",
        "ms_extra": "Ignore &ldquo;very&rdquo; when referring to high temperature<br><br>Or multiple",
        "ms_marks": "2",
    },
    {
        "id": f"{PAPER_ID}-q1bi",
        "questionNumber": "1(b)(i)",
        "marks": 1,
        "topics": ["Alkanes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify a metal used as a catalyst in a catalytic converter.",
        "specRef": "3.3.2",
        "ms_label": "1(b)(i)",
        "ms_ans": "Platinum OR Pt<br>OR Palladium OR Pd<br>OR Rhodium OR Rh",
        "ms_extra": "Credit phonetic spelling",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1bii",
        "questionNumber": "1(b)(ii)",
        "marks": 1,
        "topics": ["Alkanes", "Amount of Substance"],
        "skills": ["Chemical Equations"],
        "summary": "Balance the equation for the reaction of octane with nitrogen monoxide in a catalytic converter.",
        "specRef": "3.3.2",
        "ms_label": "1(b)(ii)",
        "ms_ans": "C<sub>8</sub>H<sub>18</sub> + <b>25</b>NO &rarr; <b>8</b>CO<sub>2</sub> + <b>12&frac12;</b>N<sub>2</sub> + <b>9</b>H<sub>2</sub>O",
        "ms_extra": "Credit whole equation doubled",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1c",
        "questionNumber": "1(c)",
        "marks": 1,
        "topics": ["Alkanes", "Energetics"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term fuel.",
        "specRef": "3.3.2",
        "ms_label": "1(c)",
        "ms_ans": "Releases OR is a source of OR provides a useable form of heat OR energy (when burned)",
        "ms_extra": "Ignore &ldquo;enthalpy&rdquo;; Ignore &ldquo;exothermic&rdquo;",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1d",
        "questionNumber": "1(d)",
        "marks": 1,
        "topics": ["Alkanes"],
        "skills": ["Chemical Equations"],
        "summary": "Write an equation for the combustion of H2S in air to give SO2 and H2O.",
        "specRef": "3.3.2",
        "ms_label": "1(d)",
        "ms_ans": "H<sub>2</sub>S + 1&frac12;O<sub>2</sub> &rarr; SO<sub>2</sub> + H<sub>2</sub>O",
        "ms_extra": "Or multiple",
        "ms_marks": "1",
    },
    # Q2 (11 marks)
    {
        "id": f"{PAPER_ID}-q2a",
        "questionNumber": "2(a)",
        "marks": 2,
        "topics": ["Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Complete the table of C3H6O isomers by naming propanone and drawing propanal.",
        "specRef": "3.3.1",
        "ms_label": "2(a)",
        "ms_ans": "M1: propanone<br><br>M2: CH<sub>3</sub>CH<sub>2</sub>CHO OR correct aldehyde with functional group drawn out",
        "ms_extra": "Credit propan-2-one as the only other acceptable response.<br>Penalise CH=O for the aldehyde group.",
        "ms_marks": "2",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2b",
        "questionNumber": "2(b)",
        "marks": 1,
        "topics": ["Nomenclature & Isomerism"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of structural isomerism shown by propanone, propanal, and prop-2-en-1-ol.",
        "specRef": "3.3.1",
        "ms_label": "2(b)",
        "ms_ans": "Functional group (isomerism) ONLY",
        "ms_extra": "Both words needed",
        "ms_marks": "1",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2c",
        "questionNumber": "2(c)",
        "marks": 1,
        "topics": ["Nomenclature & Isomerism"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term molecular formula.",
        "specRef": "3.3.1",
        "ms_label": "2(c)",
        "ms_ans": "The formula which shows the (actual) number of each type of atom OR atoms of each element in the molecule / compound.",
        "ms_extra": "Penalise reference to ratio of atoms",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2d",
        "questionNumber": "2(d)",
        "marks": 1,
        "topics": ["Nomenclature & Isomerism"],
        "skills": ["Application"],
        "summary": "Give the molecular formula for the C3H6O isomers.",
        "specRef": "3.3.1",
        "ms_label": "2(d)",
        "ms_ans": "C<sub>3</sub>H<sub>6</sub>O ONLY",
        "ms_extra": "Elements in any order",
        "ms_marks": "1",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2ei",
        "questionNumber": "2(e)(i)",
        "marks": 1,
        "topics": ["Alcohols", "Redox"],
        "skills": ["Knowledge & Recall"],
        "summary": "State the type of reaction when propanal reacts with acidified potassium dichromate(VI).",
        "specRef": "3.3.5",
        "ms_label": "2(e)(i)",
        "ms_ans": "Redox OR Oxidation",
        "ms_extra": "Either word ONLY",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2eii",
        "questionNumber": "2(e)(ii)",
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Application"],
        "summary": "Draw the structure of the carboxylic acid formed from propanal.",
        "specRef": "3.3.5",
        "ms_label": "2(e)(ii)",
        "ms_ans": "Structure of propanoic acid: CH<sub>3</sub>CH<sub>2</sub>COOH (or C<sub>2</sub>H<sub>5</sub>COOH) with C=O and C&ndash;OH drawn out",
        "ms_extra": "Carboxylic acid group must show both the double and the single bonds to oxygen.<br>Formula could show C<sub>2</sub>H<sub>5</sub> OR CH<sub>3</sub>CH<sub>2</sub>.",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2eiii",
        "questionNumber": "2(e)(iii)",
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Practical Skills"],
        "summary": "Choose Tollens' or Fehling's reagent and state the observation if propanal is present.",
        "specRef": "3.3.5",
        "ms_label": "2(e)(iii)",
        "ms_ans": "If Tollens&rsquo; is chosen: silver mirror / coating OR black precipitate / solid<br><br>If Fehling&rsquo;s is chosen: red precipitate / solid",
        "ms_extra": "No mark for choice of reagent, but do not award mark if no reagent given.<br>Insist on Tollens&rsquo; OR Fehling&rsquo;s as the ONLY reagents.",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2fi",
        "questionNumber": "2(f)(i)",
        "marks": 1,
        "topics": ["Alkenes"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term unsaturated.",
        "specRef": "3.3.4",
        "ms_label": "2(f)(i)",
        "ms_ans": "Contains a C=C OR double bond",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2fii",
        "questionNumber": "2(f)(ii)",
        "marks": 1,
        "topics": ["Alcohols"],
        "skills": ["Application"],
        "summary": "Identify the class of alcohol to which prop-2-en-1-ol belongs.",
        "specRef": "3.3.5",
        "ms_label": "2(f)(ii)",
        "ms_ans": "1&deg; OR Primary (alcohol)",
        "ms_extra": "",
        "ms_marks": "1",
        "figures": [Q2_FIG],
    },
    {
        "id": f"{PAPER_ID}-q2fiii",
        "questionNumber": "2(f)(iii)",
        "marks": 1,
        "topics": ["Alkenes"],
        "skills": ["Application"],
        "summary": "Draw the structure of the product formed when prop-2-en-1-ol reacts with bromine.",
        "specRef": "3.3.4",
        "ms_label": "2(f)(iii)",
        "ms_ans": "Structure for CH<sub>2</sub>BrCHBrCH<sub>2</sub>OH (as shown or drawn out)",
        "ms_extra": "Structure must be clear.<br>Accept CH<sub>2</sub>BrCHBrCHO and CH<sub>2</sub>BrCHBrCOOH.",
        "ms_marks": "1",
        "figures": [Q2_FIG],
    },
    # Q3 (8 marks)
    {
        "id": f"{PAPER_ID}-q3ai",
        "questionNumber": "3(a)(i)",
        "marks": 1,
        "topics": ["Alkanes", "Haloalkanes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of mechanism for the reaction of chlorine with trichloromethane in sunlight.",
        "specRef": "3.3.2",
        "ms_label": "3(a)(i)",
        "ms_ans": "(free-) radical substitution",
        "ms_extra": "Both words needed",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3aii",
        "questionNumber": "3(a)(ii)",
        "marks": 4,
        "topics": ["Alkanes", "Haloalkanes"],
        "skills": ["Mechanisms"],
        "summary": "Outline initiation, propagation, and termination steps for the free-radical substitution of CHCl3 to form CCl4.",
        "specRef": "3.3.2",
        "ms_label": "3(a)(ii)",
        "ms_ans": "<b>Initiation:</b> Cl<sub>2</sub> &rarr; 2Cl&bull;<br><b>First propagation:</b> Cl&bull; + CHCl<sub>3</sub> &rarr; &bull;CCl<sub>3</sub> + HCl<br><b>Second propagation:</b> Cl<sub>2</sub> + &bull;CCl<sub>3</sub> &rarr; CCl<sub>4</sub> + Cl&bull;<br><b>Termination:</b> 2&bull;CCl<sub>3</sub> &rarr; C<sub>2</sub>Cl<sub>6</sub> OR &bull;CCl<sub>3</sub> + Cl&bull; &rarr; CCl<sub>4</sub> OR 2Cl&bull; &rarr; Cl<sub>2</sub>",
        "ms_extra": "Ignore reference to uv/sunlight/heat.<br>The dot can be anywhere on CCl<sub>3</sub>.<br>Penalise absence of a dot once only.<br>If half-arrows used, they must be correct.",
        "ms_marks": "4",
    },
    {
        "id": f"{PAPER_ID}-q3bi",
        "questionNumber": "3(b)(i)",
        "marks": 1,
        "topics": ["Nomenclature & Isomerism", "Haloalkanes"],
        "skills": ["Application"],
        "summary": "Give the IUPAC name of CF2Cl2.",
        "specRef": "3.3.3",
        "ms_label": "3(b)(i)",
        "ms_ans": "dichlorodifluoromethane<br>OR 1,1-dichloro-1,1-difluoromethane",
        "ms_extra": "ONLY these; QoL: penalise &ldquo;cloro&rdquo; and &ldquo;flouro&rdquo;",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3bii",
        "questionNumber": "3(b)(ii)",
        "marks": 1,
        "topics": ["Haloalkanes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of reactive intermediate shown in the ozone depletion mechanism.",
        "specRef": "3.3.3",
        "ms_label": "3(b)(ii)",
        "ms_ans": "(free- OR chlorine-) radical OR chlorine atoms",
        "ms_extra": "Penalise reference to &ldquo;substitution&rdquo;; Ignore &ldquo;alkyl&rdquo;",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q3biii",
        "questionNumber": "3(b)(iii)",
        "marks": 1,
        "topics": ["Haloalkanes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of mechanistic step illustrated by Step 3 (O3 + ClO. -> 2O2 + Cl.).",
        "specRef": "3.3.3",
        "ms_label": "3(b)(iii)",
        "ms_ans": "propagation (step)",
        "ms_extra": "Ignore &ldquo;first&rdquo; or &ldquo;second&rdquo;",
        "ms_marks": "1",
    },
    # Q4 (9 marks)
    {
        "id": f"{PAPER_ID}-q4ai",
        "questionNumber": "4(a)(i)",
        "marks": 1,
        "topics": ["Haloalkanes", "Bonding"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what feature of bromoethane makes it susceptible to attack by ammonia.",
        "specRef": "3.3.3",
        "ms_label": "4(a)(i)",
        "ms_ans": "Polar C&ndash;Br (bond) OR &delta;+ C &ndash; (&delta;&minus;) Br<br>OR partially positive carbon atom on C&ndash;Br (bond)",
        "ms_extra": "The C&ndash;Br bond needs to be drawn out or stated",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4aii",
        "questionNumber": "4(a)(ii)",
        "marks": 4,
        "topics": ["Haloalkanes"],
        "skills": ["Mechanisms"],
        "summary": "Outline the nucleophilic substitution mechanism for bromoethane reacting with ammonia.",
        "specRef": "3.3.3",
        "ms_label": "4(a)(ii)",
        "ms_ans": "M1: curly arrow from lone pair on N of NH<sub>3</sub> to C atom of C&ndash;Br<br>M2: curly arrow from C&ndash;Br bond to Br atom (independent)<br>M3: structure of alkylammonium ion CH<sub>3</sub>CH<sub>2</sub>NH<sub>3</sub><sup>+</sup><br>M4: curly arrow from N&ndash;H bond to N atom",
        "ms_extra": "2nd mole of NH<sub>3</sub> not essential. Award full marks for S<sub>N</sub>1 with M1 on carbocation.<br>Penalise M1 if negative charge on NH<sub>3</sub>.<br>Penalise M2 for formal charge on C or incorrect partial charges.<br>Max 3 marks for wrong reactant or &ldquo;sticks&rdquo;.",
        "ms_marks": "4",
    },
    {
        "id": f"{PAPER_ID}-q4b",
        "questionNumber": "4(b)",
        "marks": 2,
        "topics": ["Haloalkanes", "Nomenclature & Isomerism"],
        "skills": ["Knowledge & Recall", "Application"],
        "summary": "Identify reagent A (to form CH3CH2CN from bromoethane) and name compound B.",
        "specRef": "3.3.3",
        "ms_label": "4(b)",
        "ms_ans": "Reagent: KCN OR potassium cyanide OR NaCN OR sodium cyanide<br><br>Name: propan(e)nitrile OR propan(e)-1-nitrile",
        "ms_extra": "Penalise &ldquo;acidic&rdquo; as a condition but ignore other conditions.<br><br>ONLY these names",
        "ms_marks": "1<br><br>1",
        "figures": [Q4_FIG],
    },
    {
        "id": f"{PAPER_ID}-q4ci",
        "questionNumber": "4(c)(i)",
        "marks": 1,
        "topics": ["Haloalkanes"],
        "skills": ["Knowledge & Recall"],
        "summary": "State what is meant by the term nucleophile.",
        "specRef": "3.3.3",
        "ms_label": "4(c)(i)",
        "ms_ans": "Electron pair donor<br>OR forms a coordinate / covalent bond by attack of an electron pair",
        "ms_extra": "Insist on both &ldquo;electron pair&rdquo; and an action by the electron pair. Accept &ldquo;lone pair&rdquo;.",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4cii",
        "questionNumber": "4(c)(ii)",
        "marks": 1,
        "topics": ["Haloalkanes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify the nucleophile in the reaction of aqueous KOH with bromoethane.",
        "specRef": "3.3.3",
        "ms_label": "4(c)(ii)",
        "ms_ans": "Hydroxide ion OR OH<sup>&minus;</sup> ONLY",
        "ms_extra": "Minus sign can be anywhere on OH; electron pair (if drawn) MUST be on O atom.",
        "ms_marks": "1",
        "figures": [Q4_FIG],
    },
    # Q5 (9 marks)
    {
        "id": f"{PAPER_ID}-q5a",
        "questionNumber": "5(a)",
        "marks": 1,
        "topics": ["Nomenclature & Isomerism", "Alkenes"],
        "skills": ["Application"],
        "summary": "Give the IUPAC name of compound Q, (CH3)2CHCH=CH2.",
        "specRef": "3.3.1",
        "ms_label": "5(a)",
        "ms_ans": "3-methylbut-1-ene",
        "ms_extra": "ONLY",
        "ms_marks": "1",
        "figures": [Q5_FIG],
    },
    {
        "id": f"{PAPER_ID}-q5b",
        "questionNumber": "5(b)",
        "marks": 4,
        "topics": ["Haloalkanes", "Alkenes"],
        "skills": ["Mechanisms"],
        "summary": "Name and outline the elimination mechanism for converting compound P into compound Q.",
        "specRef": "3.3.3",
        "ms_label": "5(b)",
        "ms_ans": "Elimination<br><br>M1: arrow from lone pair on O of negatively charged OH<sup>&minus;</sup> to correct H atom<br>M2: arrow from correct C&ndash;H bond to correct C&ndash;C bond (only if M1 attempted)<br>M3: arrow from C&ndash;Br bond to Br (independent; or E1 via carbocation)",
        "ms_extra": "Credit &ldquo;base elimination&rdquo; NOT &ldquo;nucleophilic elimination&rdquo;; no other prefix.<br>Penalise M1 if covalent KOH; penalise M3 for formal charge on C / wrong partial charges / arrow from Br to K<sup>+</sup>.<br>Max 2 marks for mechanism for wrong reactant or &ldquo;sticks&rdquo;; ignore wrong organic product.",
        "ms_marks": "1<br><br>3",
        "figures": [Q5_FIG],
    },
    {
        "id": f"{PAPER_ID}-q5ci",
        "questionNumber": "5(c)(i)",
        "marks": 1,
        "topics": ["Alkenes", "Haloalkanes"],
        "skills": ["Application"],
        "summary": "Identify compound R formed when Q reacts with HBr (a position isomer of P).",
        "specRef": "3.3.4",
        "ms_label": "5(c)(i)",
        "ms_ans": "2-bromo-3-methylbutane OR (CH<sub>3</sub>)<sub>2</sub>CHCHBrCH<sub>3</sub>",
        "ms_extra": "If name given it must be correct with &ldquo;bromo&rdquo; before &ldquo;methyl&rdquo;.<br>Apply list principle if both structure and name given.",
        "ms_marks": "1",
        "figures": [Q5_FIG],
    },
    {
        "id": f"{PAPER_ID}-q5cii",
        "questionNumber": "5(c)(ii)",
        "marks": 1,
        "topics": ["Alkenes"],
        "skills": ["Knowledge & Recall"],
        "summary": "Name the type of mechanism for the conversion of alkene Q into bromoalkane R.",
        "specRef": "3.3.4",
        "ms_label": "5(c)(ii)",
        "ms_ans": "Electrophilic addition ONLY",
        "ms_extra": "Both words",
        "ms_marks": "1",
        "figures": [Q5_FIG],
    },
    {
        "id": f"{PAPER_ID}-q5d",
        "questionNumber": "5(d)",
        "marks": 2,
        "topics": ["Nomenclature & Isomerism", "Alkenes"],
        "skills": ["Application", "Knowledge & Recall"],
        "summary": "Draw an alkene isomer of Q showing stereoisomerism and state the type of stereoisomerism.",
        "specRef": "3.3.1",
        "ms_label": "5(d)",
        "ms_ans": "M1: Structure of pent-2-ene ONLY: CH<sub>3</sub>CH<sub>2</sub>CH=CHCH<sub>3</sub> (MUST show double bond)<br><br>M2: Geometric(al) OR cis-trans (OR E/Z)",
        "ms_extra": "M1 and M2 marked independently.<br>Credit M1 with linear or cis or trans (or both).",
        "ms_marks": "2",
        "figures": [Q5_FIG],
    },
]


def extract_figures():
    doc = fitz.open(QP_PDF)
    crops = [
        (3, fitz.Rect(42, 65, 555, 340), Q2_FIG),   # Page 4: Q2 isomer table
        (7, fitz.Rect(42, 65, 555, 245), Q4_FIG),   # Page 8: Q4 reaction scheme
        (9, fitz.Rect(42, 65, 555, 175), Q5_FIG),   # Page 10: Q5 P->Q conversion
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

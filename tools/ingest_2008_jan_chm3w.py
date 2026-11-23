"""
Ingestion script for 2008 January CHM3/W (Section A only: Q1-Q5)
Excludes Section B extended question (Q6).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471418121_ead38ac6.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2008-jan-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
# Extract fig-q3-table.jpg (PDF p.6: Geraniol, Nerol, Citronellol table)
doc[5].get_pixmap(clip=fitz.Rect(95, 102, 475, 355), dpi=200).save(os.path.join(IMG_DIR, "fig-q3-table.jpg"))

PAPER_OBJ = {
    "id": "2008-jan-chm3w",
    "year": 2008,
    "series": "January",
    "date": "2008-01-10",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

Q3_FIG = ["img/2008-jan-chm3w/fig-q3-table.jpg"]

QUESTIONS_DATA = [
    # Q1 (8 marks, PDF p.2-3)
    {
        "id": "2008-jan-chm3w-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Name the process used to separate petroleum into useful fractions.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "<u>Fractional distillation</u> <i>or</i> <u>fractionation</u>", "concs not allowed; not \"cracking\"; not distillation; reasonable spelling", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q1aii",
        "question": "1(a)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State what is meant by the term petroleum fraction.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "Compounds / mixtures / alkanes / hydrocarbons with a boiling point <u>range</u><br><i>or</i> <u>similar</u> boiling points <i>or</i> <u>similar</u> chain length", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q1b",
        "question": "1(b)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State what is meant by the term saturated hydrocarbon.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "Contains <u>single</u> carbon-carbon bonds <u>only</u>", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q1ci",
        "question": "1(c)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["application"],
        "summary": "Write an equation for the incomplete combustion of decane (C10H22) to give carbon monoxide and water only.",
        "figures": [],
        "ms_rows": [
            ("1(c)(i)", "C<sub>10</sub>H<sub>22</sub> + 10<sup>1</sup>&frasl;<sub>2</sub>O<sub>2</sub> → 10CO + 11H<sub>2</sub>O", "credit double this equation", "1", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q1cii",
        "question": "1(c)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Identify a solid pollutant which could form during the incomplete combustion of decane.",
        "figures": [],
        "ms_rows": [
            ("1(c)(ii)", "Carbon <i>or</i> soot(y deposits) <i>or</i> C", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q1ciii",
        "question": "1(c)(iii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Identify the pollutant formed from sulphur-containing impurities in petroleum when burned.",
        "figures": [],
        "ms_rows": [
            ("1(c)(iii)", "Sulfur dioxide <i>or</i> SO<sub>2</sub>", "Not SO<sub>3</sub>; Not SO", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q1di",
        "question": "1(d)(i)",
        "marks": 1,
        "page": 3,
        "topics": ["3.3.5", "3.3.2"],
        "skills": ["application"],
        "summary": "Write an equation for the complete combustion of methanol, CH3OH.",
        "figures": [],
        "ms_rows": [
            ("1(d)(i)", "CH<sub>3</sub>OH + 1<sup>1</sup>&frasl;<sub>2</sub>O<sub>2</sub> → CO<sub>2</sub> + 2H<sub>2</sub>O", "credit double this equation", "1", "AO2 / 3.3.5")
        ]
    },
    {
        "id": "2008-jan-chm3w-q1dii",
        "question": "1(d)(ii)",
        "marks": 1,
        "page": 3,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Give one reason, other than fewer pollutants, why it may be desirable to increase the use of ethanol as a fuel.",
        "figures": [],
        "ms_rows": [
            ("1(d)(ii)", "Petroleum is finite <i>or</i> sugar is renewable", "-", "1", "AO1 / 3.3.5")
        ]
    },
    # Q2 (11 marks, PDF p.4-5)
    {
        "id": "2008-jan-chm3w-q2ai",
        "question": "2(a)(i)",
        "marks": 1,
        "page": 4,
        "topics": ["3.3.1"],
        "skills": ["recall"],
        "summary": "Give the general formula for the homologous series of alkenes.",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "C<sub>n</sub>H<sub>2n</sub> <i>or</i> C<sub>x</sub>H<sub>2x</sub> <b>ONLY</b>", "Not C<sub>2</sub>H<sub>4</sub>, but C<sub>2</sub>H<sub>4n</sub> OK", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2aii",
        "question": "2(a)(ii)",
        "marks": 2,
        "page": 4,
        "topics": ["3.3.1"],
        "skills": ["recall"],
        "summary": "State two characteristics of an homologous series other than having a general formula.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "Any <b>TWO</b> from:<ul><li>Gradation / trend / gradual change in <u>physical</u> properties / specified physical property</li><li>Each member differs by CH<sub>2</sub> from the last</li><li><u>Chemically similar</u> <i>or</i> react in the same / similar way <i>or</i> same chemical properties</li><li>Same functional group</li></ul>", "Penalise \"same molecular formula\" or \"same empirical formula\"; do not credit \"same/different properties\" unless clearly chemical/physical", "2", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2b",
        "question": "2(b)",
        "marks": 1,
        "page": 4,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Give the molecular formula for the next member of the alkene homologous series after pent-1-ene.",
        "figures": [],
        "ms_rows": [
            ("2(b)", "C<sub>6</sub>H<sub>12</sub> <b>ONLY</b>", "Not C<sup>6</sup>H<sup>12</sup>", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2c",
        "question": "2(c)",
        "marks": 1,
        "page": 4,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Draw the structure of the position isomer of pent-1-ene.",
        "figures": [],
        "ms_rows": [
            ("2(c)", "CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub>", "Structure can be like this or drawn out – possibly as cis or trans isomer; give credit for a correct structure for pent-2-ene", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2di",
        "question": "2(d)(i)",
        "marks": 1,
        "page": 4,
        "topics": ["3.1.2"],
        "skills": ["recall"],
        "summary": "State what is meant by the term empirical formula.",
        "figures": [],
        "ms_rows": [
            ("2(d)(i)", "The empirical formula shows the <u>simplest whole number ratio</u> of atoms of each <u>element / type</u> in the compound / formula / molecule", "-", "1", "AO1 / 3.1.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2dii",
        "question": "2(d)(ii)",
        "marks": 1,
        "page": 4,
        "topics": ["3.1.2"],
        "skills": ["application"],
        "summary": "Give the empirical formula of buta-1,3-diene (H2C=CH-CH=CH2).",
        "figures": [],
        "ms_rows": [
            ("2(d)(ii)", "C<sub>2</sub>H<sub>3</sub> <b>ONLY</b>", "Not C<sup>2</sup>H<sup>3</sup>; anything else is wrong", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2ei",
        "question": "2(e)(i)",
        "marks": 2,
        "page": 5,
        "topics": ["3.3.4"],
        "skills": ["explanation"],
        "summary": "Explain why non-polar bromine molecules are able to react with the double bonds in alkenes.",
        "figures": [],
        "ms_rows": [
            ("2(e)(i)", "<b>TWO</b> ideas:<ul><li>Double bonds are electron-rich / electron pair donors / centres of electron density (1)</li><li>Bromine becomes polarised <i>or</i> has an induced dipole (1)</li></ul>", "-", "2", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2eii",
        "question": "2(e)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Name the type of mechanism involved in the reaction of bromine with alkenes.",
        "figures": [],
        "ms_rows": [
            ("2(e)(ii)", "Electrophilic addition <b>ONLY</b>", "(Both words) Spelling mistakes OK", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2008-jan-chm3w-q2eiii",
        "question": "2(e)(iii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "Draw the structure of the compound with Mr = 373.6 formed when buta-1,3-diene reacts with an excess of bromine.",
        "figures": [],
        "ms_rows": [
            ("2(e)(iii)", "CH<sub>2</sub>BrCHBrCHBrCH<sub>2</sub>Br", "Structure can be like this or drawn out; give credit for a correct structure for 1,2,3,4-tetrabromobutane", "1", "AO2 / 3.3.4")
        ]
    },
    # Q3 (9 marks, PDF p.6-7)
    {
        "id": "2008-jan-chm3w-q3ai",
        "question": "3(a)(i)",
        "marks": 2,
        "page": 6,
        "topics": ["3.3.1"],
        "skills": ["recall"],
        "summary": "State what is meant by the term stereoisomers.",
        "figures": [],
        "ms_rows": [
            ("3(a)(i)", "<b>M1:</b> Compounds with the <u>same structural formula</u> (1)<br><br><b>M2:</b> but with <u>atoms / bonds / groups arranged differently in space</u> <i>or</i> with <u>different spatial arrangements</u> (1)", "Penalise M1 if \"same structure\"; ignore references to \"same molecular formula\"", "2", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2008-jan-chm3w-q3aii",
        "question": "3(a)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "State the type of stereoisomerism shown by geraniol and nerol.",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(a)(ii)", "Geometric(al) <i>or</i> cis-trans (stereoisomerism) <b>ONLY</b>", "both 'cis' + 'trans'; E-Z", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2008-jan-chm3w-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "State the type of chemical reaction by which citronellol can be formed from either geraniol or nerol.",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(b)(i)", "Reduction <i>or</i> hydrogenation <b>ONLY</b><br><i>or</i> Addition (of hydrogen)", "-", "1", "AO2 / 3.3.4")
        ]
    },
    {
        "id": "2008-jan-chm3w-q3bii",
        "question": "3(b)(ii)",
        "marks": 2,
        "page": 6,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Give a reagent and a catalyst for converting geraniol or nerol into citronellol.",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(b)(ii)", "<b>Reagent:</b> H<sub>2</sub> <i>or</i> hydrogen (gas) (1)<br><br><b>Catalyst:</b> Ni <i>or</i> Nickel <i>or</i> Pd <i>or</i> Palladium (1)", "penalise incorrect state symbol, but otherwise ignore; Not H; Not solid (s) or liquid (l); mark independently", "2", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2008-jan-chm3w-q3c",
        "question": "3(c)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "State the class of alcohols to which citronellol belongs.",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(c)", "Primary (alcohol) <i>or</i> 1° (alcohol) <b>ONLY</b>", "-", "1", "AO2 / 3.3.5")
        ]
    },
    {
        "id": "2008-jan-chm3w-q3d",
        "question": "3(d)",
        "marks": 2,
        "page": 7,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "State the type of reaction and a reagent or combination of reagents to convert citronellol into the aldehyde citronellal.",
        "figures": [],
        "ms_rows": [
            ("3(d)", "<b>Type of reaction:</b> Oxidation <i>or</i> Redox <b>ONLY</b> (1)<br><br><b>Reagent:</b> Acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> <i>or</i> acidified potassium dichromate <i>or</i> H<sub>2</sub>SO<sub>4</sub> / K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> <i>or</i> names of these two reagents (1)", "penalise incomplete reagent e.g. \"dichromate\" or acidified dichromate; if oxidation state or formula given it must be correct; accept any other correct acid", "2", "AO1 / 3.3.5")
        ]
    },
    # Q4 (10 marks, PDF p.8)
    {
        "id": "2008-jan-chm3w-q4a",
        "question": "4(a)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Write an equation for the reaction between NO and CO in a catalytic converter and identify a catalyst used.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "<b>Equation:</b> 2NO + 2CO → N<sub>2</sub> + 2CO<sub>2</sub> (1)<br><br><b>Catalyst:</b> Platinum (Pt) <i>or</i> Palladium (Pd) <i>or</i> Rhodium (Rh) (1)", "-", "2", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q4b",
        "question": "4(b)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Draw the structure of epoxyethane and identify the catalyst used in its manufacture from ethene and oxygen.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "<b>Structure:</b> 3-membered ring of H<sub>2</sub>C–CH<sub>2</sub> bonded to O (showing correct C–O and C–C bonds) (1)<br><br><b>Catalyst:</b> Ag <i>or</i> Silver <i>or</i> silver-based (1)", "-", "2", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2008-jan-chm3w-q4c",
        "question": "4(c)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.2"],
        "skills": ["application"],
        "summary": "Write an equation for the catalytic cracking of dodecane (C12H26) to form cyclohexane and one other alkane, and identify the catalyst.",
        "figures": [],
        "ms_rows": [
            ("4(c)", "<b>Equation:</b> C<sub>12</sub>H<sub>26</sub> → C<sub>6</sub>H<sub>12</sub> + C<sub>6</sub>H<sub>14</sub> (1)<br><br><b>Catalyst:</b> Zeolite <i>or</i> aluminosilicate (1)", "-", "2", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q4d",
        "question": "4(d)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Write an equation for the fermentation of glucose (C6H12O6) and identify a catalyst for this process.",
        "figures": [],
        "ms_rows": [
            ("4(d)", "<b>Equation:</b> C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> → 2CH<sub>3</sub>CH<sub>2</sub>OH + 2CO<sub>2</sub> (1)<br><br><b>Catalyst:</b> Yeast <i>or</i> suitable enzyme (zymase) (1)", "The ethanol can be C<sub>2</sub>H<sub>5</sub>OH but NOT C<sub>2</sub>H<sub>6</sub>O", "2", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2008-jan-chm3w-q4e",
        "question": "4(e)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "Write an equation for the elimination of water from butan-1-ol showing the structures of the organic compounds and identify a catalyst.",
        "figures": [],
        "ms_rows": [
            ("4(e)", "<b>Equation:</b> CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH → CH<sub>3</sub>CH<sub>2</sub>CH=CH<sub>2</sub> + H<sub>2</sub>O (1)<br><br><b>Catalyst:</b> <u>Concentrated</u> H<sub>2</sub>SO<sub>4</sub> <i>or</i> <u>Concentrated</u> H<sub>3</sub>PO<sub>4</sub> <i>or</i> Al<sub>2</sub>O<sub>3</sub> (1)", "The structure of the butan-1-ol and but-1-ene must be obvious", "2", "AO1 / 3.3.5")
        ]
    },
    # Q5 (7 marks, PDF p.9)
    {
        "id": "2008-jan-chm3w-q5a",
        "question": "5(a)",
        "marks": 3,
        "page": 9,
        "topics": ["3.3.2", "3.3.3"],
        "skills": ["mechanism"],
        "summary": "Write equations for the initiation and first and second propagation steps in the free-radical substitution of CH3Br with Br2 to form CH2Br2.",
        "figures": [],
        "ms_rows": [
            ("5(a)", "<b>Initiation:</b> Br<sub>2</sub> → 2Br• (1)<br><br><b>First propagation:</b> Br• + CH<sub>3</sub>Br → •CH<sub>2</sub>Br + HBr (1)<br><br><b>Second propagation:</b> Br<sub>2</sub> + •CH<sub>2</sub>Br → CH<sub>2</sub>Br<sub>2</sub> + Br• (1)", "-", "3", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q5bi",
        "question": "5(b)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.2", "3.3.3"],
        "skills": ["application"],
        "summary": "Write an overall equation for the conversion of bromomethane (CH3Br) into tetrabromomethane (CBr4).",
        "figures": [],
        "ms_rows": [
            ("5(b)(i)", "CH<sub>3</sub>Br + 3Br<sub>2</sub> → CBr<sub>4</sub> + 3HBr", "-", "1", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q5bii",
        "question": "5(b)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.2"],
        "skills": ["application"],
        "summary": "State how the reaction conditions would have to be adjusted to produce the highest possible yield of tetrabromomethane.",
        "figures": [],
        "ms_rows": [
            ("5(b)(ii)", "Use <u>excess</u> bromine / Br<sub>2</sub>", "-", "1", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2008-jan-chm3w-q5c",
        "question": "5(c)",
        "marks": 2,
        "page": 9,
        "topics": ["3.3.3"],
        "skills": ["application"],
        "summary": "Complete and balance the equation for the reaction of ammonia with bromomethane and name the organic product.",
        "figures": [],
        "ms_rows": [
            ("5(c)", "<b>In the equation:</b> 2NH<sub>3</sub> <u>and</u> CH<sub>3</sub>NH<sub>2</sub> (1)<br><br><b>Name of product:</b> methylamine (1)", "Accept \"aminomethane\" as an alternative name", "2", "AO2 / 3.3.3")
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
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.3.1"
    for r in qd["ms_rows"]:
        prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
        answers_list.append(f"{prefix}{r[1]} ({r[3]})" if len(qd["ms_rows"]) > 1 else r[1])
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

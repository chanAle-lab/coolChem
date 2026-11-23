"""
Ingestion script for 2007 June CHM3/W (Section A only)
Excludes Section B extended question (Q6).
NOTE: PDF page 1 is an Erratum Notice, so 1-based PDF page = printed page + 1.
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222448_63b0d554.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-june-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
# Extract fig-q3-scheme.jpg (PDF p.7 / printed p.6)
doc[6].get_pixmap(clip=fitz.Rect(90, 92, 485, 265), dpi=200).save(os.path.join(IMG_DIR, "fig-q3-scheme.jpg"))
# Extract fig-q5-table.jpg (PDF p.11 / printed p.10)
doc[10].get_pixmap(clip=fitz.Rect(68, 95, 535, 260), dpi=200).save(os.path.join(IMG_DIR, "fig-q5-table.jpg"))

PAPER_OBJ = {
    "id": "2007-june-chm3w",
    "year": 2007,
    "series": "June",
    "date": "2007-06-06",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

Q3_FIG = ["img/2007-june-chm3w/fig-q3-scheme.jpg"]
Q5_FIG = ["img/2007-june-chm3w/fig-q5-table.jpg"]

QUESTIONS_DATA = [
    # Q1 (6 marks, PDF p.4)
    {
        "id": "2007-june-chm3w-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 4,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State what is meant by the term hydrocarbon.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "A compound <i>or</i> molecule (which) contains / consists of / is made up of <b>hydrogen and carbon only</b>", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q1aii",
        "question": "1(a)(ii)",
        "marks": 2,
        "page": 4,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State the two physical changes which occur during the fractional distillation of petroleum.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "<b>Change 1:</b> liquid to gas <i>or</i> boiling / evaporation / vaporisation (1)<br><br><b>Change 2:</b> gas to liquid <i>or</i> condensation / condensing (1)", "(Answers can be in either order and should be marked independently)<br>(Penalise contradictions e.g. \"melting\")<br>(Penalise \"becomes a gas/liquid\" or \"liquefied\")", "2", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q1bi",
        "question": "1(b)(i)",
        "marks": 1,
        "page": 4,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "Draw the structure of the repeating unit of poly(ethene).",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "–CH<sub>2</sub>–CH<sub>2</sub>– &nbsp;(<i>or</i> displayed: –C(H)<sub>2</sub>–C(H)<sub>2</sub>– with all C–H bonds and trailing bonds)", "(Insist on only two CH<sub>2</sub> groups and on bonds on both sides of both CH<sub>2</sub> groups)<br>(Ignore brackets and \"n\")<br>(Penalise lower case 'h'; accept a balanced equation)", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2007-june-chm3w-q1bii",
        "question": "1(b)(ii)",
        "marks": 1,
        "page": 4,
        "topics": ["3.3.4"],
        "skills": ["explanation"],
        "summary": "State why epoxyethane is a very reactive compound.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "Strained ring / structure / molecule / compound<br><i>or</i> 60° bond angle<br><i>or</i> bond angle much less than tetrahedral / 109° / 109.5°", "(Do not credit \"stressed\" ring)<br>(Ignore \"strained bond angles\" and \"strained bonds\")<br>(Ignore \"unstable\" and \"weak bonds\" unless C–O bond is specified)", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2007-june-chm3w-q1biii",
        "question": "1(b)(iii)",
        "marks": 1,
        "page": 4,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Name the product formed when epoxyethane reacts with water.",
        "figures": [],
        "ms_rows": [
            ("1(b)(iii)", "Ethane-1,2-diol <i>or</i> ethan-1,2-diol", "-", "1", "AO1 / 3.3.4")
        ]
    },
    # Q2 (12 marks, PDF p.5-6)
    {
        "id": "2007-june-chm3w-q2ai",
        "question": "2(a)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Name the type of reactive intermediate formed during the catalytic cracking of alkanes.",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "Carbocation <i>or</i> carbonium ion", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2aii",
        "question": "2(a)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Identify a catalyst used in catalytic cracking.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "Zeolite <i>or</i> aluminosilicate <i>or</i> pumice <i>or</i> porous pot <i>or</i> Al<sub>2</sub>O<sub>3</sub> / aluminium oxide <i>or</i> ceramic", "(Ignore \"aluminium silicate\" and \"clay\")<br>(Credit phonetic spelling of zeolite)", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Name the type of reactive intermediate formed during the thermal cracking of alkanes.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "Free radical <i>or</i> alkyl radical intermediate", "(Penalise \"carbon radical\")", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["application"],
        "summary": "Write an equation for the thermal cracking of one molecule of C10H22 to produce a different alkane and propene only.",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "C<sub>10</sub>H<sub>22</sub> → C<sub>3</sub>H<sub>6</sub> + C<sub>7</sub>H<sub>16</sub><br><i>or</i> C<sub>10</sub>H<sub>22</sub> → 2C<sub>3</sub>H<sub>6</sub> + C<sub>4</sub>H<sub>10</sub><br><i>or</i> C<sub>10</sub>H<sub>22</sub> → 3C<sub>3</sub>H<sub>6</sub> + CH<sub>4</sub>", "(Credit structures of different types provided they are correct)", "1", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2ci",
        "question": "2(c)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State which type of cracking is more likely to produce cyclohexane as one of the products.",
        "figures": [],
        "ms_rows": [
            ("2(c)(i)", "Catalytic cracking", "-", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2cii",
        "question": "2(c)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "State the conditions necessary for cyclohexane to undergo complete combustion.",
        "figures": [],
        "ms_rows": [
            ("2(c)(ii)", "Excess / plentiful / lots of oxygen <i>or</i> O<sub>2</sub> <i>or</i> air", "(Penalise \"good supply\", \"sufficient\" and penalise use of a \"catalyst\")<br>(Ignore references to T and P)", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2ciii",
        "question": "2(c)(iii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Draw the structure of cyclohexane.",
        "figures": [],
        "ms_rows": [
            ("2(c)(iii)", "Six-membered ring of CH<sub>2</sub> groups <i>or</i> skeletal hexagon (cyclohexane ring)", "(Individual C–H bonds can be drawn out; H<sub>2</sub>C on LHS can be written CH<sub>2</sub>)", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q2civ",
        "question": "2(c)(iv)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.2"],
        "skills": ["application"],
        "summary": "Write an equation for the incomplete combustion of C6H12 to form carbon and water only.",
        "figures": [],
        "ms_rows": [
            ("2(c)(iv)", "C<sub>6</sub>H<sub>12</sub> + 3O<sub>2</sub> → 6C + 6H<sub>2</sub>O", "(Credit 3O<sub>2</sub> being placed over the arrow)", "1", "AO2 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2di",
        "question": "2(d)(i)",
        "marks": 2,
        "page": 6,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Write an equation for the formation of nitrogen monoxide in a petrol engine and state one essential condition.",
        "figures": [],
        "ms_rows": [
            ("2(d)(i)", "<b>M1:</b> <sup>1</sup>&frasl;<sub>2</sub>N<sub>2</sub> + <sup>1</sup>&frasl;<sub>2</sub>O<sub>2</sub> → NO &nbsp;<i>or</i>&nbsp; N<sub>2</sub> + O<sub>2</sub> → 2NO (1)<br><br><b>M2:</b> spark <i>or</i> high temperature <i>or</i> 2500 °C ≤ T ≤ 4000 °C (1)", "(Ignore references to pressure)", "2", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2dii",
        "question": "2(d)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Identify one of the metals used as a catalyst in a catalytic converter.",
        "figures": [],
        "ms_rows": [
            ("2(d)(ii)", "Platinum <i>or</i> Pt <i>or</i> rhodium <i>or</i> Rh <i>or</i> palladium <i>or</i> Pd", "(Penalise \"platinium\")<br>(Penalise contradictory symbol and name, but credit correct name even if attempted symbol is inaccurate)", "1", "AO1 / 3.3.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q2diii",
        "question": "2(d)(iii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.3.2"],
        "skills": ["recall"],
        "summary": "Write an equation to show how carbon monoxide and nitrogen monoxide react together in a catalytic converter.",
        "figures": [],
        "ms_rows": [
            ("2(d)(iii)", "CO + NO → CO<sub>2</sub> + <sup>1</sup>&frasl;<sub>2</sub>N<sub>2</sub><br><i>or</i> 2CO + 2NO → 2CO<sub>2</sub> + N<sub>2</sub>", "-", "1", "AO1 / 3.3.2")
        ]
    },
    # Q3 (10 marks, PDF p.7-8)
    {
        "id": "2007-june-chm3w-q3ai",
        "question": "3(a)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Name the process occurring in Reaction 1 (glucose with yeast to form ethanol).",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(a)(i)", "Fermentation", "(Credit correct phonetic spelling)", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-june-chm3w-q3aii",
        "question": "3(a)(ii)",
        "marks": 2,
        "page": 7,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Write an equation for Reaction 1 (fermentation of glucose) and state a suitable temperature.",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(a)(ii)", "<b>M1:</b> C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> → 2CH<sub>3</sub>CH<sub>2</sub>OH + 2CO<sub>2</sub><br><i>or</i> C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> → 2C<sub>2</sub>H<sub>5</sub>OH + 2CO<sub>2</sub> (1)<br><br><b>M2:</b> Any temperature or range in <b>30 °C to 42 °C</b> (<i>or</i> 303 K to 315 K) (1)", "(Penalise C<sub>2</sub>H<sub>6</sub>O)<br>(Assume units are correct if not specified, but penalise incorrect units)", "2", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-june-chm3w-q3b",
        "question": "3(b)",
        "marks": 1,
        "page": 7,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Name the type of mechanism in Reaction 2 (ethanol to ethene).",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(b)", "Elimination", "(Penalise \"dehydration\" on its own, but not in addition to correct answer)<br>(Credit \"acid-catalysed elimination\" or \"acid elimination\"; penalise other words before elimination)", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-june-chm3w-q3c",
        "question": "3(c)",
        "marks": 4,
        "page": 7,
        "topics": ["3.3.4"],
        "skills": ["mechanism"],
        "summary": "Outline a mechanism for Reaction 3 (ethene + Br2 -> 1,2-dibromoethane).",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(c)", "<b>Electrophilic addition</b> of Br<sub>2</sub> to H<sub>2</sub>C=CH<sub>2</sub>:<br><b>M1:</b> curly arrow from C=C double bond to Br atom of Br–Br (1)<br><b>M2:</b> curly arrow from Br–Br bond to second Br atom (1)<br><b>M3:</b> carbocation intermediate <sup>+</sup>H<sub>2</sub>C–CH<sub>2</sub>Br (1)<br><b>M4:</b> curly arrow from lone pair on :Br<sup>−</sup> to positively charged C atom (1)", "(Penalise M3 if HBr or wrong alkene is used)<br>(Penalise M2 if polarity on Br–Br is incorrect or formal charges used)<br>(Penalise M1 if partial charges are placed on the double bond)", "4", "AO2 / 3.3.4")
        ]
    },
    {
        "id": "2007-june-chm3w-q3di",
        "question": "3(d)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.3.3"],
        "skills": ["recall"],
        "summary": "Name the type of mechanism in Reaction 4 (1,2-dibromoethane with KCN -> Compound W).",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(d)(i)", "Nucleophilic substitution", "(Insist on both words and credit correct phonetic spelling)", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2007-june-chm3w-q3dii",
        "question": "3(d)(ii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.3.3"],
        "skills": ["application"],
        "summary": "Draw the structural formula of compound W (Mr = 80.0), showing all of the bonds in the molecule.",
        "figures": Q3_FIG,
        "ms_rows": [
            ("3(d)(ii)", "Displayed formula of butanedinitrile:<br><b>N≡C–CH<sub>2</sub>–CH<sub>2</sub>–C≡N</b> with all C–H, C–C and C≡N bonds drawn out<br>(<i>or</i> with –CN group shown)", "(Both Br atoms substituted to give C<sub>4</sub>H<sub>4</sub>N<sub>2</sub>, <i>M</i><sub>r</sub> = 80.0)", "1", "AO2 / 3.3.3")
        ]
    },
    # Q4 (10 marks, PDF p.9-10)
    {
        "id": "2007-june-chm3w-q4ai",
        "question": "4(a)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Name Compound X, CH3CH(OH)CH3.",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "Propan-2-ol", "-", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4aii",
        "question": "4(a)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Draw the structure of the position isomer of Compound X (CH3CH(OH)CH3).",
        "figures": [],
        "ms_rows": [
            ("4(a)(ii)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>OH", "(Credit displayed formula for propan-1-ol but insist that, if drawn, the C–OH bond is clearly from C to O)", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4bi",
        "question": "4(b)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Name Compound Y, (CH3)2C=C(CH3)2.",
        "figures": [],
        "ms_rows": [
            ("4(b)(i)", "2,3-dimethylbut-2-ene", "-", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4bii",
        "question": "4(b)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Draw the structure of a straight-chain isomer of Compound Y ((CH3)2C=C(CH3)2).",
        "figures": [],
        "ms_rows": [
            ("4(b)(ii)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH=CH<sub>2</sub><br><i>or</i> CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH=CHCH<sub>3</sub><br><i>or</i> CH<sub>3</sub>CH<sub>2</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub>", "(or displayed formula for hex-1-ene, hex-2-ene or hex-3-ene, clearly showing the double bond)", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4ci",
        "question": "4(c)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Name Compound Z, CH3CH2COCH2CH3.",
        "figures": [],
        "ms_rows": [
            ("4(c)(i)", "Pentan-3-one", "-", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4cii",
        "question": "4(c)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Draw the structure of a functional group isomer of Compound Z (CH3CH2COCH2CH3) which contains a C=O group.",
        "figures": [],
        "ms_rows": [
            ("4(c)(ii)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CHO<br><i>or</i> CH<sub>3</sub>CH<sub>2</sub>(CH<sub>3</sub>)CHCHO<br><i>or</i> (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>CHO<br><i>or</i> (CH<sub>3</sub>)<sub>3</sub>CCHO", "(Credit correct structure for any of these four aldehydes)<br>(If drawn out, only credit if the structure shows correct bonds)", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4di",
        "question": "4(d)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.1"],
        "skills": ["recall"],
        "summary": "Name the type of stereoisomerism shown by 1,2-dibromoethene.",
        "figures": [],
        "ms_rows": [
            ("4(d)(i)", "Geometric(al) <i>or</i> cis-trans", "-", "1", "AO1 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4dii",
        "question": "4(d)(ii)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Draw and name the two stereoisomers of 1,2-dibromoethene.",
        "figures": [],
        "ms_rows": [
            ("4(d)(ii)", "<b>M1:</b> <i>trans</i>-1,2-dibromoethene: Br atoms on opposite sides across C=C (H–C(Br)=C(H)–Br) (1)<br><br><b>M2:</b> <i>cis</i>-1,2-dibromoethene: Br atoms on same side across C=C (1)", "(Mark vertically, but award 1 mark for two correct structures with either no names or incorrect names)<br>(Credit structures which have 90° bond angles)", "2", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q4e",
        "question": "4(e)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.1"],
        "skills": ["explanation"],
        "summary": "State what feature of the double bond in 1,2-dibromoethene prevents Stereoisomer 1 from changing into Stereoisomer 2.",
        "figures": [],
        "ms_rows": [
            ("4(e)", "No rotation <i>or</i> restricted rotation <i>or</i> \"it does not rotate\" (<b>QoL</b>)", "(Insist on reference to rotation for the QoL mark)<br>(If a longer statement is made, it must be clear that the lack of rotation is of the double bond and not the whole molecule)", "1", "AO1 / 3.3.1")
        ]
    },
    # Q5 (7 marks, PDF p.11)
    {
        "id": "2007-june-chm3w-q5a",
        "question": "5(a)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Give the molecular formula of stearic acid, CH3(CH2)16COOH.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(a)", "C<sub>18</sub>H<sub>36</sub>O<sub>2</sub>", "(The elements could be in any order)<br>(No other structures should be drawn)", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm3w-q5bi",
        "question": "5(b)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.2"],
        "skills": ["application"],
        "summary": "Give the empirical formula of linoleic acid, CH3(CH2)4CH=CHCH2CH=CH(CH2)7COOH.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(b)(i)", "C<sub>9</sub>H<sub>16</sub>O", "(The elements could be in any order)<br>(No other structures should be drawn)", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-june-chm3w-q5bii",
        "question": "5(b)(ii)",
        "marks": 2,
        "page": 11,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Identify the reagent and catalyst needed to convert linoleic acid into stearic acid.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(b)(ii)", "<b>Reagent:</b> Hydrogen <i>or</i> H<sub>2</sub> (1)<br><br><b>Catalyst:</b> Nickel <i>or</i> Ni (1)", "(Credit platinum / Pt or palladium / Pd)<br>(Credit phonetic spellings)", "2", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2007-june-chm3w-q5ci",
        "question": "5(c)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.4"],
        "skills": ["recall"],
        "summary": "Name the type of reaction involved in converting linoleic acid into ricinoleic acid.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(c)(i)", "Hydration <i>or</i> (electrophilic) addition", "(Ignore references to \"direct\" or \"indirect\" hydration)", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2007-june-chm3w-q5cii",
        "question": "5(c)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.4"],
        "skills": ["explanation"],
        "summary": "Suggest why the conversion of linoleic acid into ricinoleic acid leads to the formation of more than one organic product.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(c)(ii)", "Both double bonds <i>or</i> the other double bond could react / be used<br><i>or</i> addition could occur either way on the double bond<br><i>or</i> other secondary / same-stability / similar-stability carbocations can form<br><i>or</i> an ester could form between the acid and alcohol", "(Do not credit simply stating linoleic acid has two double bonds)<br>(Penalise references to different stability carbocations, primary/tertiary carbocations, or major/minor products due to stability difference)", "1", "AO2 / 3.3.4")
        ]
    },
    {
        "id": "2007-june-chm3w-q5d",
        "question": "5(d)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "Identify the class of alcohols to which ricinoleic acid, CH3(CH2)4CH2CH(OH)CH2CH=CH(CH2)7COOH, belongs.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(d)", "Secondary <i>or</i> 2°", "(Credit phonetic spelling)", "1", "AO2 / 3.3.5")
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

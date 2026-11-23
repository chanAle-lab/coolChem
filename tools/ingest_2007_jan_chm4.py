"""
Ingestion script for 2007 January CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q6, Q7).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795469473872_8c753ee3.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-jan-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
# Extract fig-q1-table.jpg (page 5)
pix1 = doc[4].get_pixmap(clip=fitz.Rect(85, 130, 505, 235), dpi=200)
pix1.save(os.path.join(IMG_DIR, "fig-q1-table.jpg"))
# Extract fig-q4-nmr.jpg (page 11)
pix4 = doc[10].get_pixmap(clip=fitz.Rect(145, 225, 435, 360), dpi=200)
pix4.save(os.path.join(IMG_DIR, "fig-q4-nmr.jpg"))
# Extract fig-q5-curve.jpg (page 13)
pix5 = doc[12].get_pixmap(clip=fitz.Rect(110, 100, 445, 250), dpi=200)
pix5.save(os.path.join(IMG_DIR, "fig-q5-curve.jpg"))

PAPER_OBJ = {
    "id": "2007-jan-chm4",
    "year": 2007,
    "series": "January",
    "date": "2007-01-23",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 mins"
}

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2007-jan-chm4-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.9"],
        "skills": ["application"],
        "summary": "Deduce the order of reaction with respect to A from initial rate data.",
        "figures": ["img/2007-jan-chm4/fig-q1-table.jpg"],
        "ms_rows": [
            ("1(a)(i)", "2", "-", "1", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2007-jan-chm4-q1aii",
        "question": "1(a)(ii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.9"],
        "skills": ["application"],
        "summary": "Deduce the order of reaction with respect to B from initial rate data.",
        "figures": ["img/2007-jan-chm4/fig-q1-table.jpg"],
        "ms_rows": [
            ("1(a)(ii)", "1", "-", "1", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2007-jan-chm4-q1aiii",
        "question": "1(a)(iii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.9"],
        "skills": ["application"],
        "summary": "Deduce the order of reaction with respect to C from initial rate data.",
        "figures": ["img/2007-jan-chm4/fig-q1-table.jpg"],
        "ms_rows": [
            ("1(a)(iii)", "0", "-", "1", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2007-jan-chm4-q1b",
        "question": "1(b)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.9"],
        "skills": ["calculation"],
        "summary": "Calculate a value for the rate constant k for rate = k[D]^2[E] and deduce its units.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "<i>k</i> = rate / ([D]<sup>2</sup>[E]) &nbsp;or&nbsp; (8.36 × 10<sup>-4</sup>) / ((0.84)<sup>2</sup> × 1.16) (1)<br><br>= <b>1.0(2) × 10<sup>-3</sup> to 1.05 × 10<sup>-3</sup></b> (1)<br><br>Units: <b>mol<sup>-2</sup> dm<sup>6</sup> s<sup>-1</sup></b> (1)", "-", "3", "AO2 / 3.1.9")
        ]
    },
    # Q2
    {
        "id": "2007-jan-chm4-q2a",
        "question": "2(a)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of Cl2 and total number of moles of gas present at equilibrium when 2.60 mol PCl5 dissociates leaving 1.40 mol.",
        "figures": [],
        "ms_rows": [
            ("2(a)", "mol Cl<sub>2</sub> = <b>1.2(0)</b> (1)<br><br>total mol = <b>3.8(0)</b> (1)", "no consequential marks on wrong mol Cl<sub>2</sub> in (a) unless obvious AE", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-jan-chm4-q2b",
        "question": "2(b)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the mole fractions of PCl5 and Cl2 in the equilibrium mixture.",
        "figures": [],
        "ms_rows": [
            ("2(b)", "mol fraction PCl<sub>5</sub> = 1.4 / 3.8 = <b>0.368</b> (or 0.37) (1)<br><br>mol fraction Cl<sub>2</sub> = 1.2 / 3.8 = <b>0.316</b> (or 0.32) (1)", "allow 1.4 / total mol from (a)<br>allow mol Cl<sub>2</sub> / total mol from (a)", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-jan-chm4-q2ci",
        "question": "2(c)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["recall"],
        "summary": "Write a general expression for the partial pressure of a gas in a mixture of gases.",
        "figures": [],
        "ms_rows": [
            ("2(c)(i)", "(pp =) mol fraction × total P &nbsp;or&nbsp; total P = P<sub>A</sub> + P<sub>B</sub> + P<sub>C</sub>...<br>or p<sub>A</sub> = x<sub>A</sub> × P<sub>T</sub>", "-", "1", "AO1 / 3.1.10")
        ]
    },
    {
        "id": "2007-jan-chm4-q2cii",
        "question": "2(c)(ii)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the partial pressures of PCl5 and Cl2 in the equilibrium mixture (total pressure 125 kPa).",
        "figures": [],
        "ms_rows": [
            ("2(c)(ii)", "pp PCl<sub>5</sub> = 0.368 × 125 = <b>46(.0)</b> (range 46.0 – 46.3) (1)<br><br>pp Cl<sub>2</sub> = 0.316 × 125 = <b>39.47</b> (range 39.47 – 40.0) (1)", "Or conseq on (b)", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-jan-chm4-q2d",
        "question": "2(d)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["application"],
        "summary": "Write an expression for the equilibrium constant, Kp, for PCl5(g) <-> PCl3(g) + Cl2(g).",
        "figures": [],
        "ms_rows": [
            ("2(d)", "<i>K</i><sub>p</sub> = (<i>p</i><sub>PCl<sub>3</sub></sub> × <i>p</i><sub>Cl<sub>2</sub></sub>) / <i>p</i><sub>PCl<sub>5</sub></sub>", "not numbers; penalise [ ] but mark on; allow extra ( ) brackets; needs all P", "1", "AO1 / 3.1.10")
        ]
    },
    {
        "id": "2007-jan-chm4-q2ei",
        "question": "2(e)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.10"],
        "skills": ["recall"],
        "summary": "State the effect on Kp of adding more PCl5 at a constant temperature.",
        "figures": [],
        "ms_rows": [
            ("2(e)(i)", "no effect", "-", "1", "AO1 / 3.1.10")
        ]
    },
    {
        "id": "2007-jan-chm4-q2eii",
        "question": "2(e)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.10"],
        "skills": ["application"],
        "summary": "State the effect on Kp of increasing the temperature of the container (ΔH = +93 kJ mol-1).",
        "figures": [],
        "ms_rows": [
            ("2(e)(ii)", "increase", "-", "1", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-jan-chm4-q2f",
        "question": "2(f)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate Kp and give its units when p(PCl5) = 36.9 kPa and p(Cl2) = 42.6 kPa.",
        "figures": [],
        "ms_rows": [
            ("2(f)", "42.6<sup>2</sup> / 36.9 (1)<br>= <b>49.2</b> (or 4.92 × 10<sup>4</sup> tied to Pa) (1)<br>Units: <b>kPa</b> (1)", "If K<sub>p</sub> wrong, allow units mark conseq within (f)", "3", "AO2 / 3.1.10")
        ]
    },
    # Q3
    {
        "id": "2007-jan-chm4-q3ai",
        "question": "3(a)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "State what is meant by the term Brønsted-Lowry acid.",
        "figures": [],
        "ms_rows": [
            ("3(a)(i)", "proton donor – alone", "-", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3aii",
        "question": "3(a)(ii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "State why hydrochloric acid is described as strong.",
        "figures": [],
        "ms_rows": [
            ("3(a)(ii)", "completely dissociated", "-", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the concentration of hydrochloric acid containing 7.05 × 10^-3 mol in 50 cm3.",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "7.05 × 10<sup>-3</sup> × 10<sup>3</sup> / 50 = <b>0.14(1)</b> (mol dm<sup>-3</sup>)", "-", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3bii",
        "question": "3(b)(ii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "Write an expression for the term pH.",
        "figures": [],
        "ms_rows": [
            ("3(b)(ii)", "–log [H<sup>+</sup>] &nbsp;or&nbsp; log 1/[H<sup>+</sup>]", "-", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3biii",
        "question": "3(b)(iii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH of the 0.141 mol dm-3 hydrochloric acid.",
        "figures": [],
        "ms_rows": [
            ("3(b)(iii)", "<b>0.85</b> or conseq on (b)(i)", "penalise dp of final answer &lt;2&gt; once per paper", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3biv",
        "question": "3(b)(iv)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the total volume of the diluted solution when the pH becomes 1.00.",
        "figures": [],
        "ms_rows": [
            ("3(b)(iv)", "M1: pH = 1 => [H<sup>+</sup>] = 0.1(0) (mol dm<sup>-3</sup>) (1)<br>M2: (7.05 × 10<sup>-3</sup>) / 0.10 (1)<br>M3: vol = <b>7.05 × 10<sup>-2</sup> dm<sup>3</sup></b> or <b>70.5 cm<sup>3</sup></b> (1)", "if M1 wrong, max 1 for M2; addition or subtraction loses M2<br>Units tied (allow 71 but not 70)", "3", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3ci",
        "question": "3(c)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "Write an expression for the acid dissociation constant, Ka, for weak acid HX.",
        "figures": [],
        "ms_rows": [
            ("3(c)(i)", "<i>K</i><sub>a</sub> = [H<sup>+</sup>][X<sup>-</sup>] / [HX]", "not [H<sup>+</sup>]<sup>2</sup> / [HX] but mark on; allow HA etc", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3cii",
        "question": "3(c)(ii)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH of a 0.255 mol dm-3 solution of HX (Ka = 6.10 × 10^-5 mol dm-3).",
        "figures": [],
        "ms_rows": [
            ("3(c)(ii)", "<i>K</i><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [HX] (1)<br>[H<sup>+</sup>] = √(6.10 × 10<sup>-5</sup> × 0.255) = 3.94 × 10<sup>-3</sup> (1)<br>pH = <b>2.40</b> (if rounded to 3.9 × 10<sup>-3</sup> allow 2.41) (1)", "If K<sub>a</sub> expression wrong or missing: max 1 in part (ii) for correct calculation of pH from their [H<sup>+</sup>]<br>if write √ but forget to take sq rt this gives pH = 4.81 which can get 2 marks max", "3", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3di",
        "question": "3(d)(i)",
        "marks": 4,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the value of pKa for acid HY in a buffer containing 6.85 × 10^-3 mol HY and 2.98 × 10^-3 mol NaY at pH 3.78.",
        "figures": [],
        "ms_rows": [
            ("3(d)(i)", "[H<sup>+</sup>] = 1.66 × 10<sup>-4</sup> (1)<br><i>K</i><sub>a</sub> = (1.66 × 10<sup>-4</sup>)(2.98 × 10<sup>-3</sup>) / (6.85 × 10<sup>-3</sup>) (1)<br>= 7.22 × 10<sup>-5</sup> (1)<br>p<i>K</i><sub>a</sub> = <b>4.14</b> (1)", "if wrong method, no further marks in d(i)", "4", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q3dii",
        "question": "3(d)(ii)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["explanation"],
        "summary": "State and explain the effect on the pH of the buffer solution when a small amount of HCl is added.",
        "figures": [],
        "ms_rows": [
            ("3(d)(ii)", "Effect: none / negligible / v small decrease / v small change (1)<br><br>M1: Salt or Y<sup>-</sup> reacts with extra H<sup>+</sup> (or eqm HY ⇌ H<sup>+</sup> + Y<sup>-</sup> shifts to LHS) (1)<br>M2: ∴ [H<sup>+</sup>] or ratio [HY]/[Y<sup>-</sup>] or ratio [Y<sup>-</sup>]/[HY] remains almost constant (1)", "not just pH goes down – must be v small decrease<br>M2 only gained if M1 correct", "3", "AO1 / 3.1.12")
        ]
    },
    # Q4
    {
        "id": "2007-jan-chm4-q4a",
        "question": "4(a)",
        "marks": 3,
        "page": 10,
        "topics": ["3.3.15"],
        "skills": ["recall"],
        "summary": "Draw the structure of TMS and give two reasons why it is used as a standard in proton n.m.r.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Structure: Si(CH<sub>3</sub>)<sub>4</sub> (drawn out or formula) (1)<br><br>Any 2 reasons (2):<br>• inert / non-toxic / volatile or low bp<br>• single intense peak / signal upfield of others / (protons) very shielded", "ignore 'cheap'", "3", "AO1 / 3.3.15")
        ]
    },
    {
        "id": "2007-jan-chm4-q4b",
        "question": "4(b)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "State the number of peaks in the proton n.m.r. spectrum of CH3OCH2CH2OCH3.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "2", "-", "1", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2007-jan-chm4-q4ci",
        "question": "4(c)(i)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Predict the splitting pattern of peaks a and b in the proton n.m.r. spectrum of CH3CH2OCH2CH2OH.",
        "figures": [],
        "ms_rows": [
            ("4(c)(i)", "a = <b>quartet</b> or 4 (1)<br>b = <b>triplet</b> or 3 (1)", "allow explained alternative interpretation of splitting by rather than of these H: a causes triplet, b causes triplet", "2", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2007-jan-chm4-q4cii",
        "question": "4(c)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.6"],
        "skills": ["application"],
        "summary": "Identify the wavenumber of an IR absorption present in K (CH3CH2OCH2CH2OH) but not in J (CH3OCH2CH2OCH3).",
        "figures": [],
        "ms_rows": [
            ("4(c)(ii)", "3230 – 3550 (cm<sup>-1</sup>)", "-", "1", "AO2 / 3.3.6")
        ]
    },
    {
        "id": "2007-jan-chm4-q4di",
        "question": "4(d)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Give the name of isomer L, HOCH2CH2CH2CH2OH.",
        "figures": [],
        "ms_rows": [
            ("4(d)(i)", "butan(e)-1,4-diol or 1,4-butan(e)diol or 1,4-dihydroxybutane", "-", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-jan-chm4-q4dii",
        "question": "4(d)(ii)",
        "marks": 3,
        "page": 11,
        "topics": ["3.3.12"],
        "skills": ["application"],
        "summary": "Name the type of polymerisation and draw the repeating unit of the polyester formed from butane-1,4-diol and pentanedioic acid.",
        "figures": [],
        "ms_rows": [
            ("4(d)(ii)", "Type: <b>condensation</b> or <b>addition-elimination</b> (1)<br><br>Repeating unit: –O–(CH<sub>2</sub>)<sub>4</sub>–O–CO–(CH<sub>2</sub>)<sub>3</sub>–CO–<br>ester group (1), (CH<sub>2</sub>)<sub>3</sub> and (CH<sub>2</sub>)<sub>4</sub> (1)", "must have both carbon chains and ester group to score at all; –1 for each error", "3", "AO2 / 3.3.12")
        ]
    },
    {
        "id": "2007-jan-chm4-q4ei",
        "question": "4(e)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Deduce information from the integration value for the peak at δ 3.3 in the proton n.m.r. spectrum of M.",
        "figures": ["img/2007-jan-chm4/fig-q4-nmr.jpg"],
        "ms_rows": [
            ("4(e)(i)", "6(H) or 2 × CH<sub>3</sub> groups", "-", "1", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2007-jan-chm4-q4eii",
        "question": "4(e)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Use Table 1 to identify the type of proton leading to the peak at δ 3.3.",
        "figures": ["img/2007-jan-chm4/fig-q4-nmr.jpg"],
        "ms_rows": [
            ("4(e)(ii)", "(R)OCH<sub>3</sub>", "-", "1", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2007-jan-chm4-q4eiii",
        "question": "4(e)(iii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Draw the part of the structure deduced from the splitting and integration of peaks at δ 1.3 and δ 4.6.",
        "figures": ["img/2007-jan-chm4/fig-q4-nmr.jpg"],
        "ms_rows": [
            ("4(e)(iii)", "CH<sub>3</sub>(–)CH(–O)", "penalise any extra H; Not R attached to CH", "1", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2007-jan-chm4-q4eiv",
        "question": "4(e)(iv)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Deduce the structure of isomer M.",
        "figures": ["img/2007-jan-chm4/fig-q4-nmr.jpg"],
        "ms_rows": [
            ("4(e)(iv)", "H<sub>3</sub>C–CH(OCH<sub>3</sub>)<sub>2</sub>", "-", "1", "AO2 / 3.3.15")
        ]
    },
    # Q5
    {
        "id": "2007-jan-chm4-q5a",
        "question": "5(a)",
        "marks": 1,
        "page": 12,
        "topics": ["3.3.13"],
        "skills": ["recall"],
        "summary": "Give the systematic name for alanine.",
        "figures": [],
        "ms_rows": [
            ("5(a)", "<u>2-aminopropanoic acid</u> or <u>2-aminopropionic acid</u>", "-", "1", "AO1 / 3.3.13")
        ]
    },
    {
        "id": "2007-jan-chm4-q5bi",
        "question": "5(b)(i)",
        "marks": 1,
        "page": 12,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the dipeptide formed from two alanine molecules showing the peptide link.",
        "figures": [],
        "ms_rows": [
            ("5(b)(i)", "H<sub>2</sub>N–CH(CH<sub>3</sub>)–CO–NH–CH(CH<sub>3</sub>)–COOH (with C=O and N–H drawn out)", "Do NOT allow -CONH- or -COHN-; allow zwitterion; Not repeating unit", "1", "AO2 / 3.3.13")
        ]
    },
    {
        "id": "2007-jan-chm4-q5bii",
        "question": "5(b)(ii)",
        "marks": 1,
        "page": 12,
        "topics": ["3.3.9", "3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the organic compound formed by reacting alanine with propan-2-ol in conc. H2SO4.",
        "figures": [],
        "ms_rows": [
            ("5(b)(ii)", "H<sub>2</sub>N–CH(CH<sub>3</sub>)–COOCH(CH<sub>3</sub>)<sub>2</sub>", "not C<sub>3</sub>H<sub>7</sub>; allow <sup>+</sup>H<sub>3</sub>N–", "1", "AO2 / 3.3.9")
        ]
    },
    {
        "id": "2007-jan-chm4-q5biii",
        "question": "5(b)(iii)",
        "marks": 2,
        "page": 12,
        "topics": ["3.3.9", "3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the N-substituted amide formed from alanine and ethanoyl chloride and name the mechanism.",
        "figures": [],
        "ms_rows": [
            ("5(b)(iii)", "Structure: H<sub>3</sub>C–CO–NH–CH(CH<sub>3</sub>)–COOH (1)<br><br>Mechanism: <b>(nucleophilic) addition-elimination</b> (1)", "allow -CONH- or -COHN-", "2", "AO2 / 3.3.9")
        ]
    },
    {
        "id": "2007-jan-chm4-q5ci",
        "question": "5(c)(i)",
        "marks": 1,
        "page": 13,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the alanine species present at point X (acidic) on the titration curve.",
        "figures": ["img/2007-jan-chm4/fig-q5-curve.jpg"],
        "ms_rows": [
            ("5(c)(i)", "<sup>+</sup>H<sub>3</sub>N–CH(CH<sub>3</sub>)–COOH", "allow <sup>+</sup>H<sub>3</sub>N-", "1", "AO2 / 3.3.13")
        ]
    },
    {
        "id": "2007-jan-chm4-q5cii",
        "question": "5(c)(ii)",
        "marks": 1,
        "page": 13,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the alanine species present at point Y (neutral/zwitterion) on the titration curve.",
        "figures": ["img/2007-jan-chm4/fig-q5-curve.jpg"],
        "ms_rows": [
            ("5(c)(ii)", "<sup>+</sup>H<sub>3</sub>N–CH(CH<sub>3</sub>)–COO<sup>-</sup>", "if only mistake in X is e.g. <sup>+</sup>H<sub>2</sub>N- and this is repeated in Y but otherwise Y shows COO<sup>-</sup>, allow one for Y (ecf)", "1", "AO2 / 3.3.13")
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
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.9"
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

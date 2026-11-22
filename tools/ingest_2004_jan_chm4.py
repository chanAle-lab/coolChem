"""
Ingestion script for 2004 January CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q7 and Q8).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960916_d1c191c7.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-jan-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-jan-chm4",
    "year": 2004,
    "series": "January",
    "date": "2004-01-21",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 mins"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)
    ("2004-jan-chm4-q1ai", "1(a)(i)", 2, 75, 520, 1, ["3.1.9"], ["analysis"], "Deduce the order of reaction with respect to A from rate table."),
    ("2004-jan-chm4-q1aii", "1(a)(ii)", 2, 522, 775, 1, ["3.1.9"], ["analysis"], "Deduce the order of reaction with respect to B from rate table."),

    # Page 5: Question 1(b)
    ("2004-jan-chm4-q1bi", "1(b)(i)", 5, 75, 530, 3, ["3.1.9"], ["calculation"], "Calculate value of rate constant k with units from Experiment 4."),
    ("2004-jan-chm4-q1bii", "1(b)(ii)", 5, 532, 775, 1, ["3.1.9"], ["calculation"], "Calculate initial rate in Experiment 5 using rate equation."),

    # Page 6: Question 2(a)-(d)
    ("2004-jan-chm4-q2a", "2(a)", 6, 75, 290, 1, ["3.1.10"], ["recall"], "Write an expression for equilibrium constant Kp for SO2Cl2 dissociation."),
    ("2004-jan-chm4-q2b", "2(b)", 6, 292, 410, 2, ["3.1.10"], ["calculation"], "Calculate total number of moles of gas present in equilibrium mixture."),
    ("2004-jan-chm4-q2ci", "2(c)(i)", 6, 412, 530, 1, ["3.1.10"], ["recall"], "General expression for partial pressure of a gas in terms of total pressure."),
    ("2004-jan-chm4-q2cii", "2(c)(ii)", 6, 532, 695, 4, ["3.1.10"], ["calculation"], "Calculate partial pressures of SO2Cl2 and Cl2 in equilibrium mixture."),
    ("2004-jan-chm4-q2d", "2(d)", 6, 698, 775, 3, ["3.1.10"], ["calculation"], "Calculate value for equilibrium constant Kp and give its units."),

    # Page 7: Question 2(e)-(f)
    ("2004-jan-chm4-q2e", "2(e)", 7, 75, 260, 2, ["3.1.10"], ["analysis"], "State and explain effect of temperature increase on value of Kp."),
    ("2004-jan-chm4-q2f", "2(f)", 7, 262, 775, 1, ["3.1.10"], ["recall"], "State effect of total pressure increase on value of Kp."),

    # Page 8: Question 3(a)-(b)
    ("2004-jan-chm4-q3ai", "3(a)(i)", 8, 75, 195, 1, ["3.1.12"], ["recall"], "Write an expression for pH."),
    ("2004-jan-chm4-q3aii", "3(a)(ii)", 8, 198, 440, 4, ["3.1.12"], ["calculation"], "Write expression for Ka and calculate value at 298 K for weak acid HX."),
    ("2004-jan-chm4-q3bi", "3(b)(i)", 8, 442, 545, 2, ["3.1.12"], ["recall"], "Write expression for ionic product of water Kw and give value at 298 K."),
    ("2004-jan-chm4-q3bii", "3(b)(ii)", 8, 548, 775, 2, ["3.1.12"], ["calculation"], "Calculate pH of 0.0450 mol dm-3 sodium hydroxide solution at 298 K."),

    # Page 9: Question 3(c)-(d)
    ("2004-jan-chm4-q3ci", "3(c)(i)", 9, 75, 235, 1, ["3.1.12"], ["recall"], "Equation for reaction completed at first equivalence point of ethanedioic acid."),
    ("2004-jan-chm4-q3cii", "3(c)(ii)", 9, 238, 475, 3, ["3.1.12"], ["calculation"], "Calculate concentration of ethanedioic acid solution from titration data."),
    ("2004-jan-chm4-q3di", "3(d)(i)", 9, 478, 675, 1, ["3.3.9", "3.3.10"], ["analysis"], "Draw structure of organic product from ethanedioic acid with excess methanol."),
    ("2004-jan-chm4-q3dii", "3(d)(ii)", 9, 678, 775, 1, ["3.3.10", "3.3.12"], ["analysis"], "Draw structure of product from ethanedioic acid with ethane-1,2-diol."),

    # Page 10: Question 4(a)
    ("2004-jan-chm4-q4ai", "4(a)(i)", 10, 75, 310, 1, ["3.3.13"], ["analysis"], "Draw structure of amino acid species present in solution at pH 12."),
    ("2004-jan-chm4-q4aii", "4(a)(ii)", 10, 312, 600, 1, ["3.3.13"], ["analysis"], "Draw structure of dipeptide formed from two molecules of this amino acid."),
    ("2004-jan-chm4-q4aiii", "4(a)(iii)", 10, 602, 775, 1, ["3.3.13"], ["recall"], "Name type of interaction responsible for holding protein chain in helix shape."),

    # Page 11: Question 4(b)
    ("2004-jan-chm4-q4bi", "4(b)(i)", 11, 75, 375, 2, ["3.3.4", "3.3.12"], ["recall"], "Name type of polymerisation and draw repeating unit of (CH3)2C=CHCH3."),
    ("2004-jan-chm4-q4bii", "4(b)(ii)", 11, 378, 560, 1, ["3.3.1"], ["analysis"], "Draw structure of isomer of G showing geometrical isomerism."),
    ("2004-jan-chm4-q4biii", "4(b)(iii)", 11, 562, 775, 1, ["3.3.1", "3.3.4"], ["analysis"], "Draw structure of isomer of G that does not react with bromine water."),

    # Page 12: Question 5(a)-(c)
    ("2004-jan-chm4-q5a", "5(a)", 12, 75, 240, 1, ["3.3.16"], ["recall"], "Identify bond responsible for IR absorption at 1724 cm-1 in compound Q."),
    ("2004-jan-chm4-q5bi", "5(b)(i)", 12, 242, 345, 1, ["3.1.1", "3.3.16"], ["recall"], "Suggest why there are two molecular ion peaks at m/z = 106 and 108."),
    ("2004-jan-chm4-q5bii", "5(b)(ii)", 12, 348, 510, 2, ["3.3.16"], ["analysis"], "Identify fragment ion at m/z = 43 and write equation for its formation."),
    ("2004-jan-chm4-q5ci", "5(c)(i)", 12, 512, 600, 1, ["3.3.15"], ["recall"], "Suggest suitable solvent for use in recording proton n.m.r. spectrum of Q."),
    ("2004-jan-chm4-q5cii", "5(c)(ii)", 12, 602, 775, 1, ["3.3.15"], ["recall"], "Formula of standard reference compound used in proton n.m.r. spectra."),

    # Page 13: Question 5(d)-(f)
    ("2004-jan-chm4-q5d", "5(d)", 13, 75, 335, 1, ["3.3.15"], ["analysis"], "Complete table of adjacent non-equivalent protons for splitting pattern."),
    ("2004-jan-chm4-q5e", "5(e)", 13, 338, 520, 1, ["3.3.15"], ["analysis"], "Deduce structure of compound Q (C4H7ClO)."),
    ("2004-jan-chm4-q5f", "5(f)", 13, 522, 775, 1, ["3.3.10"], ["analysis"], "Suggest structure for structural isomer of Q reacting with cold water to give misty fumes."),

    # Page 14: Question 6
    ("2004-jan-chm4-q6ai", "6(a)(i)", 14, 75, 275, 1, ["3.3.10"], ["recall"], "Name ester compound C (HCOOCH2CH2CH3)."),
    ("2004-jan-chm4-q6aii", "6(a)(ii)", 14, 278, 440, 3, ["3.3.9", "3.3.10"], ["practical"], "Reagent and observations to distinguish between ester C and carboxylic acid D."),
    ("2004-jan-chm4-q6bi", "6(b)(i)", 14, 442, 610, 1, ["3.3.8"], ["recall"], "Name ketone compound E (CH3COCH2CH2CH3)."),
    ("2004-jan-chm4-q6bii", "6(b)(ii)", 14, 612, 745, 3, ["3.3.8"], ["practical"], "Reagent and observations to distinguish between ketone E and aldehyde F."),
    ("2004-jan-chm4-q6c", "6(c)", 14, 748, 775, 1, ["3.3.7"], ["analysis"], "Draw structure of chain isomer of pentanal showing optical isomerism.")
]

MS_DATA = {
    "2004-jan-chm4-q1ai": {
        "answers": "Order with respect to A: <b>2</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2004-jan-chm4-q1aii": {
        "answers": "Order with respect to B: <b>0</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2004-jan-chm4-q1bi": {
        "answers": "• <i>k</i> = rate / ([NO]<sup>2</sup> [O<sub>2</sub>]) = (6.5 &times; 10<sup>&minus;4</sup>) / [(5.0 &times; 10<sup>&minus;2</sup>)<sup>2</sup> &times; (2.0 &times; 10<sup>&minus;2</sup>)] (1)<br>• = <b>13</b> (1)<br>• Units = <b>mol<sup>&minus;2</sup> dm<sup>6</sup> s<sup>&minus;1</sup></b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.9"
    },
    "2004-jan-chm4-q1bii": {
        "answers": "• rate = 13 &times; (6.5 &times; 10<sup>&minus;2</sup>)<sup>2</sup> &times; (3.4 &times; 10<sup>&minus;2</sup>) (1)<br>• = <b>1.9 &times; 10<sup>&minus;3</sup> (mol dm<sup>&minus;3</sup> s<sup>&minus;1</sup>)</b> (1)",
        "extra": "If k wrong, mark in (ii) may be gained conseq for their k &times; 1.437 &times; 10^-4.",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2004-jan-chm4-q2a": {
        "answers": "<b><i>K</i><sub>p</sub> = (<i>p</i><sub>SO<sub>2</sub></sub> &times; <i>p</i><sub>Cl<sub>2</sub></sub>) / <i>p</i><sub>SO<sub>2</sub>Cl<sub>2</sub></sub></b> (1)",
        "extra": "If Kp has [ ] lose mark in (a) but allow full marks in (d).",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2004-jan-chm4-q2b": {
        "answers": "0.25 + 0.75 + 0.75 (1) = <b>1.75 (mol)</b> (1)",
        "extra": "1.75 gets [2]. If moles of SO2Cl2 = 1, CE - 2 marks penalty.",
        "mark": 2,
        "spec": "3.1.10"
    },
    "2004-jan-chm4-q2ci": {
        "answers": "<b><i>p</i> = Total pressure &times; mol fraction</b> (1)<br>(<i>OR</i> <i>p</i><sub>A</sub> = <i>x</i><sub>A</sub> &times; <i>P</i><sub>tot</sub>)",
        "extra": "Allow 'Total pressure = sum of partial pressures' for [1].",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2004-jan-chm4-q2cii": {
        "answers": "• <i>p</i><sub>SO<sub>2</sub>Cl<sub>2</sub></sub> = 125 &times; (0.25 / 1.75) (1) = <b>17.9 kPa</b> (1)<br>• <i>p</i><sub>Cl<sub>2</sub></sub> = 125 &times; (0.75 / 1.75) (1) = <b>53.6 kPa</b> (1)",
        "extra": "First mark is for mole fraction.",
        "mark": 4,
        "spec": "3.1.10"
    },
    "2004-jan-chm4-q2d": {
        "answers": "• <i>K</i><sub>p</sub> = (53.6 &times; 53.6) / 17.9 (1) = <b>161</b> (1)<br>• Units = <b>kPa</b> (1)",
        "extra": "SIG FIGS: must be 3 sig figs in (b) but allow 2 sig figs in (c) and (d).",
        "mark": 3,
        "spec": "3.1.10"
    },
    "2004-jan-chm4-q2e": {
        "answers": "• Effect on <i>K</i><sub>p</sub>: <b>increase</b> (1)<br>• Explanation: increase <i>T</i> sends equilibrium in <b>endothermic direction</b> (1)",
        "extra": "If effect wrong, no marks for explanation. 'Endothermic' is essential.",
        "mark": 2,
        "spec": "3.1.10"
    },
    "2004-jan-chm4-q2f": {
        "answers": "<b>No effect</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2004-jan-chm4-q3ai": {
        "answers": "<b>pH = &minus;log [H<sup>+</sup>]</b> (1)",
        "extra": "Penalise missing [ ] once in question.",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2004-jan-chm4-q3aii": {
        "answers": "• <i>K</i><sub>a</sub> = [H<sup>+</sup>][X<sup>&minus;</sup>] / [HX] (1)<br>• [H<sup>+</sup>] = 10<sup>&minus;2.56</sup> = 2.75 &times; 10<sup>&minus;3</sup> (1)<br>• <i>K</i><sub>a</sub> = (2.75 &times; 10<sup>&minus;3</sup>)<sup>2</sup> / 0.12 (1) = <b>6.32 &times; 10<sup>&minus;5</sup> (mol dm<sup>&minus;3</sup>)</b> (1)<br>[allow 6.30 &ndash; 6.32 &times; 10^-5]",
        "extra": "",
        "mark": 4,
        "spec": "3.1.12"
    },
    "2004-jan-chm4-q3bi": {
        "answers": "• <i>K</i><sub>w</sub> = <b>[H<sup>+</sup>][OH<sup>&minus;</sup>]</b> (1)<br>• Value = <b>1.0 &times; 10<sup>&minus;14</sup> (mol<sup>2</sup> dm<sup>&minus;6</sup>)</b> (1)",
        "extra": "Ignore units.",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2004-jan-chm4-q3bii": {
        "answers": "• [H<sup>+</sup>] = 1.0 &times; 10<sup>&minus;14</sup> / 0.0450 = 2.22 &times; 10<sup>&minus;13</sup> (1)<br>(<i>OR</i> pOH = 1.35)<br>• pH = <b>12.65</b> (1) [must be 2 dp in final answer]",
        "extra": "",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2004-jan-chm4-q3ci": {
        "answers": "<b>H<sub>2</sub>C<sub>2</sub>O<sub>4</sub> + OH<sup>&minus;</sup> &rarr; HC<sub>2</sub>O<sub>4</sub><sup>&minus;</sup> + H<sub>2</sub>O</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2004-jan-chm4-q3cii": {
        "answers": "• mol OH<sup>&minus;</sup> = (41.6 &times; 10<sup>&minus;3</sup>) &times; 0.0450 = 1.87 &times; 10<sup>&minus;3</sup> (1)<br>• mol H<sub>2</sub>C<sub>2</sub>O<sub>4</sub> = 1.87 &times; 10<sup>&minus;3</sup> / 2 = 9.36 &times; 10<sup>&minus;4</sup> (1)<br>• [H<sub>2</sub>C<sub>2</sub>O<sub>4</sub>] = 9.36 &times; 10<sup>&minus;4</sup> &times; (10<sup>3</sup> / 25) = <b>0.0374 (mol dm<sup>&minus;3</sup>)</b> (1)",
        "extra": "If moles of H2C2O4 not equal to half moles of OH-, no further marks gained.",
        "mark": 3,
        "spec": "3.1.12"
    },
    "2004-jan-chm4-q3di": {
        "answers": "Structure of dimethyl ethanedioate: <b>CH<sub>3</sub>OOC&ndash;COOCH<sub>3</sub></b> drawn showing ester linkages (1)",
        "extra": "Must be diester. Allow CH3OOCCOOCH3 or CH3O2CCO2CH3.",
        "mark": 1,
        "spec": "3.3.10"
    },
    "2004-jan-chm4-q3dii": {
        "answers": "Repeating unit of polyester: <b>[&ndash;OCH<sub>2</sub>CH<sub>2</sub>&ndash;O&ndash;C(=O)&ndash;C(=O)&ndash;]<sub><i>n</i></sub></b> (1)<br><i>OR</i> cyclic diester structure",
        "extra": "Must be 1:1 proportion. Allow repeating unit alone.",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2004-jan-chm4-q4ai": {
        "answers": "Structure: <b>H<sub>2</sub>N&ndash;CH(CH(CH<sub>3</sub>)<sub>2</sub>)&ndash;COO<sup>&minus;</sup></b> (1)",
        "extra": "Ignore Na+ unless covalently bonded.",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2004-jan-chm4-q4aii": {
        "answers": "Structure of dipeptide: <b>H<sub>2</sub>N&ndash;CH(R)&ndash;CONH&ndash;CH(R)&ndash;COOH</b> (1)<br>(where R = CH(CH<sub>3</sub>)<sub>2</sub>; allow zwitterion)",
        "extra": "Must be dipeptide, not polymer nor anhydride.",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2004-jan-chm4-q4aiii": {
        "answers": "<b>Hydrogen bonding</b> (1)",
        "extra": "Allow with dipole-dipole or van der Waals, but not dipole-dipole alone.",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2004-jan-chm4-q4bi": {
        "answers": "• Type: <b>addition</b> (1)<br>• Repeating unit: <b>&ndash;[C(CH<sub>3</sub>)<sub>2</sub>&ndash;CH(CH<sub>3</sub>)]&ndash;</b> with open linking bonds (1)",
        "extra": "Must show linking bonds. Allow n.",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2004-jan-chm4-q4bii": {
        "answers": "Structure: <b>CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub></b> (pent-2-ene) (1)",
        "extra": "Double bond must be shown.",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2004-jan-chm4-q4biii": {
        "answers": "Structure: <b>cyclopentane</b> <i>OR</i> <b>methylcyclobutane</b> <i>OR</i> <b>dimethylcyclopropane</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2004-jan-chm4-q5a": {
        "answers": "<b>C=O</b> <i>OR</i> <b>carbonyl</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.16"
    },
    "2004-jan-chm4-q5bi": {
        "answers": "<b>Cl has (2) isotopes</b> (1) [allow <sup>35</sup>Cl and <sup>37</sup>Cl without word isotope]",
        "extra": "",
        "mark": 1,
        "spec": "3.3.16"
    },
    "2004-jan-chm4-q5bii": {
        "answers": "• Fragment ion: <b>CH<sub>3</sub>C<sup>+</sup>=O</b> (1) [must be an ion]<br>• Equation: <b>C<sub>4</sub>H<sub>7</sub>ClO<sup>+&bull;</sup> &rarr; CH<sub>3</sub>CO<sup>+</sup> + C<sub>2</sub>H<sub>4</sub>Cl<sup>&bull;</sup></b> (1)",
        "extra": "Must have 3 different elements, i.e. not C3H7+. Allow C2H3O+.",
        "mark": 2,
        "spec": "3.3.16"
    },
    "2004-jan-chm4-q5ci": {
        "answers": "<b>CDCl<sub>3</sub></b> <i>OR</i> <b>CCl<sub>4</sub></b> <i>OR</i> <b>D<sub>2</sub>O</b> <i>OR</i> <b>C<sub>6</sub>D<sub>6</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2004-jan-chm4-q5cii": {
        "answers": "<b>Si(CH<sub>3</sub>)<sub>4</sub></b> <i>OR</i> <b>SiC<sub>4</sub>H<sub>12</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2004-jan-chm4-q5d": {
        "answers": "Peak 2: <b>0</b> (singlet); Peak 3: <b>3</b> (quartet) (1)",
        "extra": "Both correct for 1 mark.",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2004-jan-chm4-q5e": {
        "answers": "Structure: <b>CH<sub>3</sub>&ndash;CO&ndash;CH(Cl)&ndash;CH<sub>3</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2004-jan-chm4-q5f": {
        "answers": "Structure: <b>CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COCl</b> <i>OR</i> <b>(CH<sub>3</sub>)<sub>2</sub>CHCOCl</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.10"
    },
    "2004-jan-chm4-q6ai": {
        "answers": "<b>Propyl methanoate</b> (1)",
        "extra": "NOT propanyl.",
        "mark": 1,
        "spec": "3.3.10"
    },
    "2004-jan-chm4-q6aii": {
        "answers": "• Reagent: <b>NaHCO<sub>3</sub></b> <i>OR</i> <b>Na<sub>2</sub>CO<sub>3</sub></b> <i>OR</i> <b>Mg</b> (1)<br>• Observation with C: <b>no reaction</b> (1)<br>• Observation with D: <b>effervescence / bubbles of CO<sub>2</sub> (or H<sub>2</sub>)</b> (1)<br>(Allow acidified K2Cr2O7 or correct indicator).",
        "extra": "NOT Tollens.",
        "mark": 3,
        "spec": "3.3.9"
    },
    "2004-jan-chm4-q6bi": {
        "answers": "<b>Pentan-2-one</b> <i>OR</i> 2-pentanone (1)",
        "extra": "NOT pent-2-one.",
        "mark": 1,
        "spec": "3.3.8"
    },
    "2004-jan-chm4-q6bii": {
        "answers": "• Reagent: <b>Tollens' reagent</b> <i>OR</i> <b>Fehling's solution</b> (1)<br>• Observation with E: <b>no reaction</b> (1)<br>• Observation with F: <b>silver mirror / grey ppt</b> (with Tollens') <i>OR</i> <b>red ppt</b> (with Fehling's) (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.3.8"
    },
    "2004-jan-chm4-q6c": {
        "answers": "Structure of 2-methylbutanal: <b>CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CHO</b> (1)",
        "extra": "Must be an aldehyde. Allow C2H5 for CH3CH2.",
        "mark": 1,
        "spec": "3.3.7"
    }
}

def main():
    doc = fitz.open(QP_PATH)
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    existing_ids = {q["id"] for q in db["questions"]}
    added = 0

    for qid, q_label, p_num, y0, y1, mark, spec_topics, skills, prompt in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-jan-chm4/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-jan-chm4/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-jan-chm4",
            "year": 2004,
            "series": "January",
            "code": "CHM4",
            "unit": "Unit 4: Further Physical and Organic Chemistry",
            "question": q_label,
            "page": p_num,
            "marks": mark,
            "topics": spec_topics,
            "skills": skills,
            "description": prompt,
            "image": q_img_rel,
            "markscheme": ms_img_rel
        }

        if qid not in existing_ids:
            db["questions"].append(q_obj)
            existing_ids.add(qid)
            added += 1
        else:
            for idx, item in enumerate(db["questions"]):
                if item["id"] == qid:
                    db["questions"][idx] = q_obj
                    break

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-jan-chm4 ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

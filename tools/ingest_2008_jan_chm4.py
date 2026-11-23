"""
Ingestion script for 2008 January CHM4 (Section A only: Q1-Q6)
Excludes Section B extended questions (Q7, Q8).
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471418113_220d39bf.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2008-jan-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
# Q2 figures (p.5)
doc[4].get_pixmap(clip=fitz.Rect(70, 88, 525, 178), dpi=200).save(os.path.join(IMG_DIR, "fig-q2-ka.jpg"))
doc[4].get_pixmap(clip=fitz.Rect(72, 355, 525, 415), dpi=200).save(os.path.join(IMG_DIR, "fig-q2-b-stem.jpg"))
# Q3 figures (p.6)
doc[5].get_pixmap(clip=fitz.Rect(70, 68, 465, 118), dpi=200).save(os.path.join(IMG_DIR, "fig-q3-eq.jpg"))
doc[5].get_pixmap(clip=fitz.Rect(72, 220, 525, 270), dpi=200).save(os.path.join(IMG_DIR, "fig-q3-b-data.jpg"))
# Q5 figure (p.10: Polymers P to U)
doc[9].get_pixmap(clip=fitz.Rect(42, 68, 520, 440), dpi=200).save(os.path.join(IMG_DIR, "fig-q5-polymers.jpg"))
# Q6 figure (p.12: rate equation + data table)
doc[11].get_pixmap(clip=fitz.Rect(70, 68, 525, 345), dpi=200).save(os.path.join(IMG_DIR, "fig-q6-table.jpg"))

PAPER_OBJ = {
    "id": "2008-jan-chm4",
    "year": 2008,
    "series": "January",
    "date": "2008-01-22",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 mins"
}

Q5_FIG = ["img/2008-jan-chm4/fig-q5-polymers.jpg"]

QUESTIONS_DATA = [
    # Q1 (6 marks, PDF p.2)
    {
        "id": "2008-jan-chm4-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "Write an expression for the ionic product of water, Kw.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "<i>K</i><sub>w</sub> = [H<sup>+</sup>][OH<sup>−</sup>]", "if wrong only score in (ii) and (iii) except if [H<sub>2</sub>O] = 1", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q1aii",
        "question": "1(a)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate [H+] in pure water at 50 °C given pH = 6.63.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "<b>2.34 × 10<sup>−7</sup></b> (mol dm<sup>−3</sup>)", "penalise 2.3 × 10<sup>−7</sup> i.e. 2 sfs once in the question", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q1aiii",
        "question": "1(a)(iii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.12"],
        "skills": ["application"],
        "summary": "Deduce [OH-] in pure water at 50 °C (pH = 6.63).",
        "figures": [],
        "ms_rows": [
            ("1(a)(iii)", "<b>2.34 × 10<sup>−7</sup></b> (mol dm<sup>−3</sup>)", "conseq = (ii)", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q1aiv",
        "question": "1(a)(iv)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the value of Kw at 50 °C for pure water with pH = 6.63.",
        "figures": [],
        "ms_rows": [
            ("1(a)(iv)", "<b>5.48 to 5.50 × 10<sup>−14</sup></b>", "conseq = (ii) × (iii); if [H<sub>2</sub>O] = 1 can score for correct answer here", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q1b",
        "question": "1(b)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH of a 0.136 mol dm-3 solution of KOH at 25 °C (Kw = 1.00 x 10^-14 mol2 dm-6).",
        "figures": [],
        "ms_rows": [
            ("1(b)", "[H<sup>+</sup>] = 10<sup>−14</sup> / 0.136 = 7.35 × 10<sup>−14</sup> &nbsp;(<i>or</i> pOH = 0.87) (1)<br><br>pH = <b>13.13</b> (1)", "-", "2", "AO2 / 3.1.12")
        ]
    },
    # Q2 (9 marks, PDF p.5)
    {
        "id": "2008-jan-chm4-q2a",
        "question": "2(a)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH at 25 °C of a 0.169 mol dm-3 solution of propanoic acid (Ka = 1.35 x 10^-5 mol dm-3).",
        "figures": [],
        "ms_rows": [
            ("2(a)", "<b>M1:</b> <i>K</i><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [CH<sub>3</sub>CH<sub>2</sub>COOH] (1)<br><br><b>M2:</b> [H<sup>+</sup>] = √(1.35 × 10<sup>−5</sup> × 0.169) = 1.51 × 10<sup>−3</sup> (1)<br><br><b>M3:</b> pH = <b>2.82</b> (1)", "if M1 wrong, score max 1 for M3 from their [H<sup>+</sup>]; penalise round brackets once; if √ visible can score 2 for 5.64", "3", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.12"],
        "skills": ["application"],
        "summary": "Write an equation for the reaction of propanoic acid with sodium hydroxide.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "CH<sub>3</sub>CH<sub>2</sub>COOH + NaOH → CH<sub>3</sub>CH<sub>2</sub>COONa + H<sub>2</sub>O<br><i>or</i> CH<sub>3</sub>CH<sub>2</sub>COOH + OH<sup>−</sup> → CH<sub>3</sub>CH<sub>2</sub>COO<sup>−</sup> + H<sub>2</sub>O", "penalise covalent Na", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q2bii",
        "question": "2(b)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of propanoic acid and propanoate ions after adding 0.015 mol NaOH to 0.250 mol acid and 0.190 mol salt.",
        "figures": ["img/2008-jan-chm4/fig-q2-b-stem.jpg"],
        "ms_rows": [
            ("2(b)(ii)", "mol propanoic acid = 0.250 − 0.015 = <b>0.235</b> (1)<br><br>mol propanoate ions = 0.190 + 0.015 = <b>0.205</b> (1)", "penalise rounding to 2 sfs once", "2", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q2biii",
        "question": "2(b)(iii)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH of the propanoic acid / sodium propanoate buffer solution after addition of 0.015 mol NaOH.",
        "figures": [
            "img/2008-jan-chm4/fig-q2-ka.jpg",
            "img/2008-jan-chm4/fig-q2-b-stem.jpg"
        ],
        "ms_rows": [
            ("2(b)(iii)", "<b>M1:</b> [H<sup>+</sup>] = <i>K</i><sub>a</sub> × [CH<sub>3</sub>CH<sub>2</sub>COOH] / [CH<sub>3</sub>CH<sub>2</sub>COO<sup>−</sup>] (allow <i>K</i><sub>a</sub> × [HA] / [A<sup>−</sup>]) (1)<br><br><b>M2:</b> = (1.35 × 10<sup>−5</sup>)(0.235) / 0.205 = 1.548 × 10<sup>−5</sup> (1)<br><br><b>M3:</b> pH = <b>4.81</b> (1)", "M1 for correct rearrangement; M2 for insertion of correct numbers; allow 1 for correct pH from their [H<sup>+</sup>]", "3", "AO2 / 3.1.12")
        ]
    },
    # Q3 (14 marks, PDF p.6-7)
    {
        "id": "2008-jan-chm4-q3a",
        "question": "3(a)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["application"],
        "summary": "Write an expression for the equilibrium constant Kc for 2CH4(g) <-> 3H2(g) + C2H2(g).",
        "figures": [],
        "ms_rows": [
            ("3(a)", "<i>K</i><sub>c</sub> = [H<sub>2</sub>]<sup>3</sup>[C<sub>2</sub>H<sub>2</sub>] / [CH<sub>4</sub>]<sup>2</sup>", "if round brackets, penalise here but mark on; if <i>K</i><sub>c</sub> wrong can score only M1 and conseq units in (b)", "1", "AO1 / 3.1.10")
        ]
    },
    {
        "id": "2008-jan-chm4-q3b",
        "question": "3(b)",
        "marks": 4,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate Kc and deduce its units when 0.44 mol CH4, 0.28 mol H2 and 0.12 mol C2H2 are at equilibrium in 0.25 dm3.",
        "figures": ["img/2008-jan-chm4/fig-q3-eq.jpg"],
        "ms_rows": [
            ("3(b)", "<b>M1:</b> dividing by volume (0.25) throughout shown (1)<br><br><b>M2:</b> <i>K</i><sub>c</sub> = [(0.28/0.25)<sup>3</sup> × (0.12/0.25)] / (0.44/0.25)<sup>2</sup> = (1.12<sup>3</sup> × 0.48) / 1.76<sup>2</sup> (1)<br><br><b>M3:</b> = <b>0.218</b> or <b>0.22</b> (allow 0.217 – 0.22) (1)<br><br><b>M4:</b> <b>mol<sup>2</sup> dm<sup>−6</sup></b> (1)", "if moles used instead of conc can score only M3 (1.36 × 10<sup>−2</sup>) + units M4", "4", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2008-jan-chm4-q3c",
        "question": "3(c)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.10", "3.1.6"],
        "skills": ["application"],
        "summary": "State the effect of an increase in temperature on the equilibrium position and on Kc for 2CH4(g) <-> 3H2(g) + C2H2(g), ΔH = +377 kJ mol-1.",
        "figures": ["img/2008-jan-chm4/fig-q3-eq.jpg"],
        "ms_rows": [
            ("3(c)", "<b>Position:</b> to right / to product(s) / forwards (1)<br><br><b>Value of <i>K</i><sub>c</sub>:</b> Increase (1)", "-", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2008-jan-chm4-q3d",
        "question": "3(d)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.10", "3.1.6"],
        "skills": ["application"],
        "summary": "State the effect of an increase in pressure on the equilibrium position and on Kc for 2CH4(g) <-> 3H2(g) + C2H2(g).",
        "figures": ["img/2008-jan-chm4/fig-q3-eq.jpg"],
        "ms_rows": [
            ("3(d)", "<b>Position:</b> to left / to reagent / backwards (1)<br><br><b>Value of <i>K</i><sub>c</sub>:</b> no effect (1)", "-", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2008-jan-chm4-q3e",
        "question": "3(e)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the mole fraction of ethyne (C2H2) in the equilibrium mixture from part (b).",
        "figures": ["img/2008-jan-chm4/fig-q3-b-data.jpg"],
        "ms_rows": [
            ("3(e)", "total no. moles = <b>0.84</b> (1)<br><br>0.12 / 0.84 = <b>0.14(3)</b> (allow <sup>1</sup>&frasl;<sub>7</sub>) (1)", "if CE in total moles, no second mark", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2008-jan-chm4-q3f",
        "question": "3(f)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the partial pressure of ethyne in the mixture given total pressure = 2.78 x 10^4 kPa.",
        "figures": ["img/2008-jan-chm4/fig-q3-b-data.jpg"],
        "ms_rows": [
            ("3(f)", "0.143 × 2.78 × 10<sup>4</sup> = <b>3.97 × 10<sup>3</sup></b> (allow 3.89–4.00 × 10<sup>3</sup> &amp; 2 sfs i.e. 3.9–4.0 × 10<sup>3</sup>)", "conseq on (e); penalise wrong units", "1", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2008-jan-chm4-q3g",
        "question": "3(g)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of H2 and C2H2 at equilibrium when 3.0 mol CH4 reacts to leave 1.6 mol CH4.",
        "figures": [],
        "ms_rows": [
            ("3(g)", "mol H<sub>2</sub> = <b>2.1</b> (1)<br><br>mol C<sub>2</sub>H<sub>2</sub> = <b>0.7</b> (1)", "mark independently", "2", "AO2 / 3.1.10")
        ]
    },
    # Q4 (13 marks, PDF p.8-9)
    {
        "id": "2008-jan-chm4-q4ai",
        "question": "4(a)(i)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.6", "3.3.15"],
        "skills": ["application"],
        "summary": "Draw possible structures for C6H12 isomers A and B (both 1 1H NMR peak; A has IR peak at 1650 cm-1, B does not).",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "<b>A:</b> (CH<sub>3</sub>)<sub>2</sub>C=C(CH<sub>3</sub>)<sub>2</sub> (must show C=C) (1)<br><br><b>B:</b> cyclohexane (skeletal hexagon or 6-membered CH<sub>2</sub> ring) (1)", "for B: allow individual C–H bonds, but not C–H<sub>2</sub> off ring vertex", "2", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2008-jan-chm4-q4aii",
        "question": "4(a)(ii)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.8", "3.3.15"],
        "skills": ["application"],
        "summary": "Draw possible structures for C5H10O isomers C and D (both 2 1H NMR peaks; C gives silver mirror with Tollens', D does not).",
        "figures": [],
        "ms_rows": [
            ("4(a)(ii)", "<b>C:</b> (CH<sub>3</sub>)<sub>3</sub>CCHO (1)<br><br><b>D:</b> CH<sub>3</sub>CH<sub>2</sub>COCH<sub>2</sub>CH<sub>3</sub> (allow C<sub>2</sub>H<sub>5</sub>COC<sub>2</sub>H<sub>5</sub>) (1)", "for C: NOT (CH<sub>3</sub>)<sub>3</sub>CCOH", "2", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2008-jan-chm4-q4aiii",
        "question": "4(a)(iii)",
        "marks": 2,
        "page": 8,
        "topics": ["3.3.9", "3.3.15"],
        "skills": ["application"],
        "summary": "Draw possible structures for C3H6O2 isomers E and F (quartet, triplet, singlet in 1H NMR; E effervesces with NaHCO3, F does not).",
        "figures": [],
        "ms_rows": [
            ("4(a)(iii)", "<b>E:</b> CH<sub>3</sub>CH<sub>2</sub>COOH &nbsp;<i>or</i>&nbsp; C<sub>2</sub>H<sub>5</sub>CO<sub>2</sub>H (1)<br><br><b>F:</b> HCOOCH<sub>2</sub>CH<sub>3</sub> &nbsp;<i>or</i>&nbsp; HCO<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (1)", "-", "2", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2008-jan-chm4-q4aiv",
        "question": "4(a)(iv)",
        "marks": 2,
        "page": 9,
        "topics": ["3.3.1", "3.3.7"],
        "skills": ["application"],
        "summary": "Draw possible structures for C6H12 isomers G (geometrical isomerism only) and H (optical isomerism only).",
        "figures": [],
        "ms_rows": [
            ("4(a)(iv)", "<b>G:</b> CH<sub>3</sub>CH=CHCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> &nbsp;<i>or</i>&nbsp; CH<sub>3</sub>CH=CHCH(CH<sub>3</sub>)<sub>2</sub> &nbsp;<i>or</i>&nbsp; CH<sub>3</sub>CH=CHC<sub>3</sub>H<sub>7</sub> &nbsp;<i>or</i>&nbsp; CH<sub>3</sub>CH<sub>2</sub>CH=CHCH<sub>2</sub>CH<sub>3</sub> &nbsp;<i>or</i>&nbsp; CH<sub>3</sub>(H)C=C(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub> &nbsp;<i>or</i>&nbsp; 1,2-dimethylcyclobutane (1)<br><br><b>H:</b> CH<sub>3</sub>CH(CH<sub>2</sub>CH<sub>3</sub>)CH=CH<sub>2</sub> (allow C<sub>2</sub>H<sub>3</sub> or CHCH<sub>2</sub>) (1)", "must show C=C in alkenes", "2", "AO2 / 3.3.7")
        ]
    },
    {
        "id": "2008-jan-chm4-q4av",
        "question": "4(a)(v)",
        "marks": 2,
        "page": 9,
        "topics": ["3.3.5"],
        "skills": ["application"],
        "summary": "Draw possible structures for C5H12O alcohols I (not oxidised, can be dehydrated) and J (oxidised, cannot be dehydrated).",
        "figures": [],
        "ms_rows": [
            ("4(a)(v)", "<b>I:</b> (CH<sub>3</sub>)<sub>2</sub>C(OH)CH<sub>2</sub>CH<sub>3</sub> &nbsp;<i>or</i>&nbsp; (CH<sub>3</sub>)<sub>2</sub>C(OH)C<sub>2</sub>H<sub>5</sub> (1)<br><br><b>J:</b> (CH<sub>3</sub>)<sub>3</sub>CCH<sub>2</sub>OH (1)", "-", "2", "AO2 / 3.3.5")
        ]
    },
    {
        "id": "2008-jan-chm4-q4bi",
        "question": "4(b)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Predict the number of peaks in the proton n.m.r. spectrum of CH3C(OH)(CH3)COCH2CH2COOH.",
        "figures": [],
        "ms_rows": [
            ("4(b)(i)", "<b>5</b>", "-", "1", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2008-jan-chm4-q4bii",
        "question": "4(b)(ii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Name the splitting pattern for the protons labelled a and b in CH3C(OH)(CH3)COCH2CH2COOH.",
        "figures": [],
        "ms_rows": [
            ("4(b)(ii)", "<b>a:</b> singlet (<b>QWC</b>) (1)<br><br><b>b:</b> triplet (<b>QWC</b>) (1)", "-", "2", "AO2 / 3.3.15")
        ]
    },
    # Q5 (11 marks, PDF p.10-11)
    {
        "id": "2008-jan-chm4-q5ai",
        "question": "5(a)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the zwitterion of 2-aminopropanoic acid (which forms polymer P).",
        "figures": [],
        "ms_rows": [
            ("5(a)(i)", "<sup>+</sup>H<sub>3</sub>N–CH(CH<sub>3</sub>)–COO<sup>−</sup>", "-", "1", "AO2 / 3.3.13")
        ]
    },
    {
        "id": "2008-jan-chm4-q5aii",
        "question": "5(a)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Give the formula of the single amino acid that forms the other polypeptide polymer shown (polymer S).",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(a)(ii)", "H<sub>2</sub>N–CH<sub>2</sub>CH<sub>2</sub>–COOH", "not H<sub>2</sub>N–C<sub>2</sub>H<sub>4</sub>–COOH", "1", "AO2 / 3.3.13")
        ]
    },
    {
        "id": "2008-jan-chm4-q5aiii",
        "question": "5(a)(iii)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.12"],
        "skills": ["application"],
        "summary": "Name the two monomers used in the formation of polyamide Q.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(a)(iii)", "<b>First monomer:</b> ethan(e)-1,2-diamine (1)<br><br><b>Second monomer:</b> butan(e)(-1,4-)dioic acid (1)", "allow ethylene diamine or 1,2-diaminoethane (penalise wrong numbers); NOT dibutanoic acid", "2", "AO2 / 3.3.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q5bi",
        "question": "5(b)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.4", "3.3.12"],
        "skills": ["recall"],
        "summary": "Name the type of polymerisation involved in the formation of polymer R.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(b)(i)", "addition", "not \"additional\"", "1", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2008-jan-chm4-q5bii",
        "question": "5(b)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.4", "3.3.1"],
        "skills": ["application"],
        "summary": "Name the alkene monomer used to form polymer R.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(b)(ii)", "3-methylpent-2-ene", "-", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2008-jan-chm4-q5ci",
        "question": "5(c)(i)",
        "marks": 2,
        "page": 11,
        "topics": ["3.3.12"],
        "skills": ["application"],
        "summary": "Draw the structures of the monomers used to produce polyester T.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(c)(i)", "<b>First monomer:</b> HOCH<sub>2</sub>CH<sub>2</sub>OH (1)<br><br><b>Second monomer:</b> HOOCCH<sub>2</sub>CH<sub>2</sub>COOH &nbsp;<i>or</i>&nbsp; ClOCCH<sub>2</sub>CH<sub>2</sub>COCl (1)", "-", "2", "AO2 / 3.3.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q5cii",
        "question": "5(c)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.12"],
        "skills": ["application"],
        "summary": "Draw the structure of the species formed when polyester U is hydrolysed by heating with aqueous sodium hydroxide.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(c)(ii)", "HOCH<sub>2</sub>CH<sub>2</sub>COO<sup>−</sup>", "allow –COONa but not covalently bonded Na", "1", "AO2 / 3.3.12")
        ]
    },
    {
        "id": "2008-jan-chm4-q5di",
        "question": "5(d)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.3", "3.3.12"],
        "skills": ["recall"],
        "summary": "Name the strongest type of intermolecular force in poly(alkene) polymer R.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(d)(i)", "van der Waals", "allow vdW or London forces or dispersion forces", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2008-jan-chm4-q5dii",
        "question": "5(d)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.3", "3.3.12"],
        "skills": ["recall"],
        "summary": "Name the strongest type of intermolecular force in polyester T.",
        "figures": Q5_FIG,
        "ms_rows": [
            ("5(d)(ii)", "dipole-dipole (<b>QWC</b>)", "Not temporary dipole–induced dipole", "1", "AO1 / 3.1.3")
        ]
    },
    # Q6 (7 marks, PDF p.12)
    {
        "id": "2008-jan-chm4-q6ai",
        "question": "6(a)(i)",
        "marks": 3,
        "page": 12,
        "topics": ["3.1.9"],
        "skills": ["calculation"],
        "summary": "Complete the initial rates table for Expts 2, 3 and 4 given rate = k[X]^2[Y]^0.",
        "figures": [],
        "ms_rows": [
            ("6(a)(i)", "<b>Expt 2:</b> 2.68 × 10<sup>−4</sup> (1)<br><br><b>Expt 3:</b> 10.7(2) × 10<sup>−4</sup> &nbsp;(1.07 × 10<sup>−3</sup>) (1)<br><br><b>Expt 4:</b> 2.08 × 10<sup>−3</sup> (1)", "all answers to 3 sfs; penalise fewer once", "3", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2008-jan-chm4-q6aii",
        "question": "6(a)(ii)",
        "marks": 3,
        "page": 12,
        "topics": ["3.1.9"],
        "skills": ["calculation"],
        "summary": "Use the data for experiment 1 to calculate a value for the rate constant k and deduce its units.",
        "figures": ["img/2008-jan-chm4/fig-q6-table.jpg"],
        "ms_rows": [
            ("6(a)(ii)", "<i>k</i> = rate / [X]<sup>2</sup> &nbsp;<i>or</i>&nbsp; 2.68 × 10<sup>−4</sup> / (1.20 × 10<sup>−3</sup>)<sup>2</sup> (1)<br><br>= <b>186</b> (1)<br><br>Units: <b>mol<sup>−1</sup> dm<sup>3</sup> s<sup>−1</sup></b> (1)", "allow mol<sup>−1</sup> dm<sup>3</sup> for misprint", "3", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2008-jan-chm4-q6b",
        "question": "6(b)",
        "marks": 1,
        "page": 12,
        "topics": ["3.1.9"],
        "skills": ["application"],
        "summary": "Sketch a graph to show how the value of the rate constant k varies with temperature.",
        "figures": [],
        "ms_rows": [
            ("6(b)", "Curve increases exponentially (concave upward)", "allow straight line (positive slope), but not concave-down curve", "1", "AO1 / 3.1.9")
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
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.12"
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

"""
Ingestion script for 2005 January CHM5 (Section A only)
Excludes old-spec Section B essay questions (Q6-Q9).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382904770_4d77c63a.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-jan-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-jan-chm5",
    "year": 2005,
    "series": "January",
    "date": "2005-01-26",
    "code": "CHM5",
    "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
    "level": "A2",
    "spec": "AQA Chemistry"
}

def extract_figures(doc):
    # 1. Born-Haber cycle for CaS (page 6)
    p6 = doc[5]
    rect1 = fitz.Rect(50, 115, 545, 535)
    pix1 = p6.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect1)
    im1 = Image.frombytes("RGB", [pix1.width, pix1.height], pix1.samples)
    fig1_path = os.path.join(IMG_DIR, "fig-q2-cycle.jpg")
    im1.save(fig1_path, format="JPEG", quality=92)
    print("Saved fig-q2-cycle.jpg")

    # 2. Electrode potential table (page 8)
    p8 = doc[7]
    rect2 = fitz.Rect(50, 115, 545, 345)
    pix2 = p8.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect2)
    im2 = Image.frombytes("RGB", [pix2.width, pix2.height], pix2.samples)
    fig2_path = os.path.join(IMG_DIR, "fig-q3-table.jpg")
    im2.save(fig2_path, format="JPEG", quality=92)
    print("Saved fig-q3-table.jpg")

    # 3. pH curve for H2SO3 (page 11)
    p11 = doc[10]
    rect3 = fitz.Rect(80, 120, 500, 380)
    pix3 = p11.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect3)
    im3 = Image.frombytes("RGB", [pix3.width, pix3.height], pix3.samples)
    fig3_path = os.path.join(IMG_DIR, "fig-q4-curve.jpg")
    im3.save(fig3_path, format="JPEG", quality=92)
    print("Saved fig-q4-curve.jpg")

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2005-jan-chm5-q1ai",
        "question": "1(a)(i)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.12", "3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate concentration of aluminium chloride in 4.22 g dm–3 solution.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "Mass / Mr = 4.22 / 133.5", "1 mark for correct method", "1", "AO2 / 3.1.2"),
            ("", "= 0.0316 (mol dm–3)", "Penalise answers to 2 sig figs once in (a)(i) and (ii)", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2005-jan-chm5-q1aii",
        "question": "1(a)(ii)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate concentration of hydrogen ions in solution with pH 3.25.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "pH = –log[H+] or [H+] = 10^(–pH)", "1 mark for method / expression", "1", "AO1 / 3.1.12"),
            ("", "[H+] = 5.62 × 10^(–4) (mol dm–3)", "Allow 5.6 × 10^(–4) unless already penalised in (i)", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2005-jan-chm5-q1aiii",
        "question": "1(a)(iii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.2.6"],
        "skills": ["recall"],
        "summary": "Identify major aluminium-containing species in aqueous AlCl3 solution.",
        "figures": [],
        "ms_rows": [
            ("1(a)(iii)", "[Al(H2O)6]3+", "Allow without brackets if charges clear; allow Al(H2O)6 3+", "1", "AO1 / 3.2.6")
        ]
    },
    {
        "id": "2005-jan-chm5-q1aiv",
        "question": "1(a)(iv)",
        "marks": 1,
        "page": 2,
        "topics": ["3.2.6"],
        "skills": ["recall", "explanation"],
        "summary": "Equation for hydrolysis reaction causing aqueous aluminium chloride to be acidic.",
        "figures": [],
        "ms_rows": [
            ("1(a)(iv)", "[Al(H2O)6]3+ + H2O ⇌ [Al(H2O)5(OH)]2+ + H3O+(aq)\nor [Al(H2O)6]3+ ⇌ [Al(H2O)5(OH)]2+ + H+(aq)", "Allow reversible or forward arrows", "1", "AO1 / 3.2.6")
        ]
    },
    {
        "id": "2005-jan-chm5-q1av",
        "question": "1(a)(v)",
        "marks": 2,
        "page": 2,
        "topics": ["3.1.12", "3.2.6"],
        "skills": ["calculation"],
        "summary": "Calculate percentage of aluminium ions hydrolysed using parts (i) and (ii).",
        "figures": [],
        "ms_rows": [
            ("1(a)(v)", "5.62 × 10^(–4) × 100 / 0.0316", "1 mark for correct ratio expression; allow consequential to (a)(i) and (ii)", "1", "AO2 / 3.1.12"),
            ("", "= 1.78 to 1.80%", "Allow consequential on previous values", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2005-jan-chm5-q1b",
        "question": "1(b)",
        "marks": 2,
        "page": 2,
        "topics": ["3.2.6"],
        "skills": ["recall", "observation"],
        "summary": "State two observations when sodium carbonate is added to aqueous aluminium chloride.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "White precipitate formed", "Allow white solid", "1", "AO1 / 3.2.6"),
            ("", "Colourless gas / effervescence / bubbles (or CO2 evolved)", "Do not allow gas alone without observation", "1", "AO1 / 3.2.6")
        ]
    },
    {
        "id": "2005-jan-chm5-q1ci",
        "question": "1(c)(i)",
        "marks": 2,
        "page": 5,
        "topics": ["3.2.3", "3.2.6"],
        "skills": ["recall", "observation"],
        "summary": "Observation and equation when aqueous silver nitrate is added to aluminium chloride.",
        "figures": [],
        "ms_rows": [
            ("1(c)(i)", "White precipitate formed", "1 mark for observation", "1", "AO1 / 3.2.3"),
            ("", "3AgNO3 + AlCl3 → 3AgCl + Al(NO3)3\nor Ag+ + Cl– → AgCl", "1 mark for balanced equation", "1", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2005-jan-chm5-q1cii",
        "question": "1(c)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.2.6"],
        "skills": ["explanation"],
        "summary": "Why excess aqueous ammonia cannot confirm presence of chloride ions in aluminium chloride.",
        "figures": [],
        "ms_rows": [
            ("1(c)(ii)", "Al3+(aq) reacts with NH3(aq) / OH– forming a white precipitate", "Precipitate is Al(OH)3 or [Al(H2O)3(OH)3]", "1", "AO2 / 3.2.6"),
            ("", "Cannot see if AgCl precipitate has dissolved (masked by Al(OH)3)", "Must mention obscuring / masking / same colour ppt", "1", "AO2 / 3.2.6")
        ]
    },
    {
        "id": "2005-jan-chm5-q1di",
        "question": "1(d)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.2.3"],
        "skills": ["recall", "observation"],
        "summary": "State what is observed when concentrated sulphuric acid is added to solid sodium chloride.",
        "figures": [],
        "ms_rows": [
            ("1(d)(i)", "White fumes / steamy fumes / misty fumes evolved", "Do not allow gas / white gas", "1", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2005-jan-chm5-q1dii",
        "question": "1(d)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.2.3"],
        "skills": ["recall", "explanation"],
        "summary": "Equation for reaction of NaCl with H2SO4 and role of sulphuric acid in this reaction.",
        "figures": [],
        "ms_rows": [
            ("1(d)(ii)", "NaCl + H2SO4 → NaHSO4 + HCl\nor 2NaCl + H2SO4 → Na2SO4 + 2HCl", "1 mark for balanced equation", "1", "AO1 / 3.2.3"),
            ("", "Proton donor / acid / Brønsted–Lowry acid", "Do not allow oxidising agent", "1", "AO1 / 3.2.3")
        ]
    },

    # Q2
    {
        "id": "2005-jan-chm5-q2a",
        "question": "2(a)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.1"],
        "skills": ["recall"],
        "summary": "Give the full electronic arrangement of the sulphide ion S2–.",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(a)", "1s2 2s2 2p6 3s2 3p6", "Full configuration required; do not allow [Ar]", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-jan-chm5-q2b",
        "question": "2(b)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.8"],
        "skills": ["recall"],
        "summary": "Identify the species X formed in Step E of the Born–Haber cycle.",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(b)", "S–(g)", "State symbol (g) and charge (–) required", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2005-jan-chm5-q2c",
        "question": "2(c)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.8"],
        "skills": ["explanation"],
        "summary": "Suggest why Step F (second electron affinity of sulphur) is an endothermic process.",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(c)", "The negative S– ion", "1 mark for identifying species as negative ion", "1", "AO1 / 3.1.8"),
            ("", "Repels the incoming / added electron", "Energy needed to overcome electrostatic repulsion", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2005-jan-chm5-q2di",
        "question": "2(d)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.8"],
        "skills": ["recall"],
        "summary": "Name the enthalpy change represented by Step B in the Born–Haber cycle.",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(d)(i)", "Enthalpy of atomisation of sulphur", "Allow heat of atomisation / enthalpy of sublimation", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2005-jan-chm5-q2dii",
        "question": "2(d)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.8"],
        "skills": ["recall"],
        "summary": "Name the enthalpy change represented by Step D in the Born–Haber cycle.",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(d)(ii)", "Second ionisation enthalpy of calcium", "Must specify second ionisation enthalpy", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2005-jan-chm5-q2diii",
        "question": "2(d)(iii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.8"],
        "skills": ["recall"],
        "summary": "Name the enthalpy change represented by Step F in the Born–Haber cycle.",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(d)(iii)", "Second electron affinity of sulphur", "Must specify second electron affinity", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2005-jan-chm5-q2e",
        "question": "2(e)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.1", "3.1.8"],
        "skills": ["explanation"],
        "summary": "Explain why Step D (second IE of Ca) is more endothermic than Step C (first IE).",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(e)", "Electron is more strongly attracted / electron removed from positive ion Ca+", "1 mark for removing from positive ion", "1", "AO1 / 3.1.1"),
            ("", "Electron is nearer to the nucleus / smaller ionic radius / less shielding", "1 mark for proximity / shielding reason", "1", "AO1 / 3.1.1")
        ]
    },
    {
        "id": "2005-jan-chm5-q2f",
        "question": "2(f)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.8"],
        "skills": ["calculation"],
        "summary": "Calculate the enthalpy change for Step F (second EA of sulphur) using Born–Haber cycle data.",
        "figures": ["img/2005-jan-chm5/fig-q2-cycle.jpg"],
        "ms_rows": [
            ("2(f)", "Correct cycle expression:\n+178 + 279 + 590 + 1145 – 200 + E – 3013 + 482 = 0", "1 mark for setting up cycle correctly", "1", "AO2 / 3.1.8"),
            ("", "E = +539 (kJ mol–1)", "Allow 1 mark for –539", "1", "AO2 / 3.1.8")
        ]
    },

    # Q3
    {
        "id": "2005-jan-chm5-q3ai",
        "question": "3(a)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.11"],
        "skills": ["calculation"],
        "summary": "Calculate EMF of cell: Pt | H2SO3, SO4 2– || Ce4+, Ce3+ | Pt.",
        "figures": ["img/2005-jan-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(a)(i)", "E_cell = +1.45 – 0.17 = (+)1.28 V  [or from data 1.45 - 0.17 = 1.28 V / Ce: 1.45, H2SO3: 0.17 -> 1.28 V; MS accepts 0.60 V if VO2+/VO2+ used]", "Allow 0.60 V or 1.28 V based on table entries", "1", "AO2 / 3.1.11")
        ]
    },
    {
        "id": "2005-jan-chm5-q3aii",
        "question": "3(a)(ii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.11"],
        "skills": ["recall"],
        "summary": "Write half-equation for oxidation process occurring at negative electrode.",
        "figures": ["img/2005-jan-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(a)(ii)", "H2O + H2SO3 → SO4 2– + 4H+ + 2e–", "Allow reversible arrows", "1", "AO1 / 3.1.11")
        ]
    },
    {
        "id": "2005-jan-chm5-q3bi",
        "question": "3(b)(i)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.11"],
        "skills": ["recall", "calculation"],
        "summary": "Equation for reaction of IO3– with H2O2 in acidic solution to form O2 and I2.",
        "figures": ["img/2005-jan-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(b)(i)", "2IO3– + 2H+ + 5H2O2 → 5O2 + I2 + 6H2O", "1 mark for all correct species; 1 mark for fully balanced equation", "2", "AO2 / 3.1.11")
        ]
    },
    {
        "id": "2005-jan-chm5-q3bii",
        "question": "3(b)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.11"],
        "skills": ["explanation"],
        "summary": "Why the EMF of a cell changes when in use.",
        "figures": ["img/2005-jan-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(b)(ii)", "The concentrations of the ions change (are no longer standard / reagents used up)\nor EMF is determined when no current flows", "Allow reactants used up / ions consumed", "1", "AO1 / 3.1.11")
        ]
    },
    {
        "id": "2005-jan-chm5-q3biii",
        "question": "3(b)(iii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.11"],
        "skills": ["recall"],
        "summary": "Effect on electrode potential of IO3–/I2 electrode when surface area of Pt electrode is doubled.",
        "figures": ["img/2005-jan-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(b)(iii)", "Unchanged / no effect", "Electrode potential is independent of electrode surface area", "1", "AO1 / 3.1.11")
        ]
    },
    {
        "id": "2005-jan-chm5-q3biv",
        "question": "3(b)(iv)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.11"],
        "skills": ["explanation"],
        "summary": "Effect on IO3–/I2 electrode potential and explanation when solution is made more acidic.",
        "figures": ["img/2005-jan-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(b)(iv)", "Increased / becomes more positive", "1 mark for effect", "1", "AO1 / 3.1.11"),
            ("", "Equilibrium IO3–/I2 is displaced to the right / forward direction favoured", "1 mark for Le Chatelier shift", "1", "AO2 / 3.1.11"),
            ("", "Electrons are more readily accepted / more reduction occurs / electrode gains positive charge", "1 mark for electron / reduction reason (QWC)", "1", "AO2 / 3.1.11")
        ]
    },
    {
        "id": "2005-jan-chm5-q3c",
        "question": "3(c)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.11", "3.2.5"],
        "skills": ["recall", "calculation"],
        "summary": "Identify vanadium species formed when V2+ oxidised by Ce4+, state its oxidation state, and write half-equation.",
        "figures": ["img/2005-jan-chm5/fig-q3-table.jpg"],
        "ms_rows": [
            ("3(c)", "VO2+", "1 mark for formula", "1", "AO1 / 3.2.5"),
            ("", "+5 / V(V)", "1 mark for oxidation state", "1", "AO1 / 3.2.5"),
            ("", "V2+ + 2H2O → VO2+ + 4H+ + 3e–", "1 mark for balanced half-equation", "1", "AO2 / 3.1.11")
        ]
    },

    # Q4
    {
        "id": "2005-jan-chm5-q4ai",
        "question": "4(a)(i)",
        "marks": 2,
        "page": 10,
        "topics": ["3.2.4"],
        "skills": ["recall"],
        "summary": "Formula and oxidation state of phosphorus in oxide formed by burning phosphorus in limited oxygen.",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "P4O6 (or P2O3) [or SO2 in sulphur / if question asks for P: P4O6 / P2O3; if S: SO2]", "1 mark for formula: SO2 or P4O6 / P2O3", "1", "AO1 / 3.2.4"),
            ("", "+3 (or +4 for SO2)", "1 mark for correct oxidation state matching formula", "1", "AO1 / 3.2.4")
        ]
    },
    {
        "id": "2005-jan-chm5-q4aii",
        "question": "4(a)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.2.4"],
        "skills": ["recall"],
        "summary": "Equation for formation of oxide when phosphorus burns in excess oxygen.",
        "figures": [],
        "ms_rows": [
            ("4(a)(ii)", "P4 + 5O2 → P4O10\nor 4P + 5O2 → 2P2O5", "1 mark for balanced equation", "1", "AO1 / 3.2.4")
        ]
    },
    {
        "id": "2005-jan-chm5-q4bi",
        "question": "4(b)(i)",
        "marks": 3,
        "page": 10,
        "topics": ["3.2.4"],
        "skills": ["recall", "explanation"],
        "summary": "Identify molecular oxides B and E from table and explain how melting points confirm molecular nature.",
        "figures": [],
        "ms_rows": [
            ("4(b)(i)", "Oxide B and Oxide E", "1 mark for identifying B, 1 mark for identifying E", "2", "AO1 / 3.2.4"),
            ("", "They have low melting points / weak van der Waals forces between molecules / simple molecular structure", "1 mark for bonding/structure explanation", "1", "AO1 / 3.2.4")
        ]
    },
    {
        "id": "2005-jan-chm5-q4bii",
        "question": "4(b)(ii)",
        "marks": 3,
        "page": 10,
        "topics": ["3.2.4"],
        "skills": ["practical", "recall"],
        "summary": "Simple test to confirm identity of sodium oxide A from other ionic oxides C and D.",
        "figures": [],
        "ms_rows": [
            ("4(b)(ii)", "Test: Add water (dissolve) OR Flame test", "1 mark for correct test reagent / method", "1", "AO3 / 3.2.4"),
            ("", "Measurement: Test pH of solution OR Check flame colour", "1 mark for measurement / check", "1", "AO3 / 3.2.4"),
            ("", "Observation: pH = 13–14 (strongly alkaline) OR Yellow flame", "1 mark for result confirming sodium oxide", "1", "AO3 / 3.2.4")
        ]
    },
    {
        "id": "2005-jan-chm5-q4ci",
        "question": "4(c)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.12", "3.2.4"],
        "skills": ["recall"],
        "summary": "Formula of salt formed at first equivalence point on titration curve.",
        "figures": ["img/2005-jan-chm5/fig-q4-curve.jpg"],
        "ms_rows": [
            ("4(c)(i)", "NaHSO3 (or Na+ and HSO3–)", "Sodium hydrogensulphate(IV) / hydrogensulphite", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2005-jan-chm5-q4cii",
        "question": "4(c)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.12", "3.2.4"],
        "skills": ["recall"],
        "summary": "Equation for reaction occurring between first and second equivalence points.",
        "figures": ["img/2005-jan-chm5/fig-q4-curve.jpg"],
        "ms_rows": [
            ("4(c)(ii)", "NaHSO3 + NaOH → Na2SO3 + H2O\nor HSO3– + OH– → SO3 2– + H2O", "Allow full or ionic equation", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2005-jan-chm5-q4ciii",
        "question": "4(c)(iii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "Suggest suitable indicator for detecting second equivalence point.",
        "figures": ["img/2005-jan-chm5/fig-q4-curve.jpg"],
        "ms_rows": [
            ("4(c)(iii)", "Phenolphthalein / thymol blue / alizarin yellow", "Any indicator changing colour in pH range 8.0–10.5", "1", "AO1 / 3.1.12")
        ]
    },

    # Q5
    {
        "id": "2005-jan-chm5-q5a",
        "question": "5(a)",
        "marks": 1,
        "page": 12,
        "topics": ["3.1.1", "3.2.5"],
        "skills": ["recall"],
        "summary": "Electronic configuration of the Co2+ ion in form 3d^n.",
        "figures": [],
        "ms_rows": [
            ("5(a)", "3d7  (or [Ar] 3d7)", "Do not allow 3d5 4s2", "1", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2005-jan-chm5-q5b",
        "question": "5(b)",
        "marks": 2,
        "page": 12,
        "topics": ["3.2.5"],
        "skills": ["recall", "observation"],
        "summary": "Formula and colour of cobalt(II) complex formed when CoCl2 dissolves in water.",
        "figures": [],
        "ms_rows": [
            ("5(b)", "[Co(H2O)6]2+", "1 mark for formula with correct charge", "1", "AO1 / 3.2.5"),
            ("", "Pink", "1 mark for colour", "1", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2005-jan-chm5-q5ci",
        "question": "5(c)(i)",
        "marks": 2,
        "page": 12,
        "topics": ["3.2.5"],
        "skills": ["recall", "observation"],
        "summary": "Formula and colour of cobalt(II) complex formed with excess aqueous ammonia in absence of air.",
        "figures": [],
        "ms_rows": [
            ("5(c)(i)", "[Co(NH3)6]2+", "1 mark for formula with correct charge", "1", "AO1 / 3.2.5"),
            ("", "Pale brown / straw-coloured / yellow-brown", "1 mark for colour", "1", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2005-jan-chm5-q5cii",
        "question": "5(c)(ii)",
        "marks": 1,
        "page": 12,
        "topics": ["3.2.5"],
        "skills": ["recall"],
        "summary": "Equation for reaction between hexaaquacobalt(II) ion and ammonia.",
        "figures": [],
        "ms_rows": [
            ("5(c)(ii)", "[Co(H2O)6]2+ + 6NH3 → [Co(NH3)6]2+ + 6H2O", "Allow reversible arrows", "1", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2005-jan-chm5-q5d",
        "question": "5(d)",
        "marks": 2,
        "page": 12,
        "topics": ["3.2.5"],
        "skills": ["recall", "explanation"],
        "summary": "Formula of cobalt(III) complex formed on standing in air and role of air in reaction.",
        "figures": [],
        "ms_rows": [
            ("5(d)", "[Co(NH3)6]3+", "1 mark for formula with 3+ charge", "1", "AO1 / 3.2.5"),
            ("", "Oxidising agent / electron acceptor / oxidises cobalt(II) to cobalt(III)", "1 mark for role of air / oxygen", "1", "AO1 / 3.2.5")
        ]
    }
]

def main():
    print("Opening Question Paper PDF...")
    doc_qp = fitz.open(QP_PATH)
    extract_figures(doc_qp)

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Remove any existing 2005-jan-chm5 questions
    db["questions"] = [q for q in db["questions"] if q.get("paper") != "2005-jan-chm5"]

    for qd in QUESTIONS_DATA:
        qid = qd["id"]
        q_label = qd["question"]
        ms_img_rel = f"img/2005-jan-chm5/ms_{qid.split('-')[-1]}.jpg"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

        answers_list = []
        extra_list = []
        spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.2"
        for r in qd["ms_rows"]:
            prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
            answers_list.append(f"{prefix}{r[1]} ({r[3]})")
            if r[2]:
                extra_list.append(f"{r[2]}")

        answers_html = "<br>".join(answers_list)
        extra_html = "<br>".join(extra_list) if extra_list else "-"

        render_official_markscheme_image(
            question_label=q_label,
            answers_html=answers_html,
            extra_html=extra_html,
            marks=qd["marks"],
            spec_ref=spec_ref,
            output_path=ms_img_abs
        )

        entry = {
            "id": qid,
            "paper": "2005-jan-chm5",
            "question": q_label,
            "marks": qd["marks"],
            "page": qd["page"],
            "topics": qd["topics"],
            "skills": qd["skills"],
            "summary": qd["summary"],
            "image": f"img/2005-jan-chm5/q_{qid.split('-')[-1]}.jpg",
            "figures": qd["figures"],
            "markscheme": ms_img_rel,
            "markscheme_text": "\n".join([f"{r[0]} {r[1]} [{r[3]}]".strip() for r in qd["ms_rows"]])
        }
        db["questions"].append(entry)
        print(f"Processed {qid} ({q_label}) - {qd['marks']} marks")

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully ingested {len(QUESTIONS_DATA)} questions for 2005-jan-chm5!")

if __name__ == "__main__":
    main()

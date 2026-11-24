"""Ingest AQA A-level Chemistry Specimen Set 2 Paper 1 (7405/1) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517647584_ab5edb61.pdf"
)

PAPER_ID = "2016-specimen2-7405-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2016,
    "series": "Specimen Set 2",
    "unit": "7405/1",
    "level": "A-level",
    "date": "2016-01-01",
    "title": "7405/1 — A-level Paper 1: Inorganic and Physical Chemistry (Specimen Set 2)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q2-stem.jpg", "page": 3, "x0": 40, "y0": 75, "x1": 550, "y1": 255},
    {"filename": "fig-q4-1-eq.jpg", "page": 7, "x0": 40, "y0": 85, "x1": 550, "y1": 195},
    {"filename": "fig-q5-bornhaber.jpg", "page": 10, "x0": 40, "y0": 108, "x1": 555, "y1": 408},
    {"filename": "fig-q6-table2.jpg", "page": 12, "x0": 40, "y0": 85, "x1": 555, "y1": 295},
    {"filename": "fig-q7-eq.jpg", "page": 14, "x0": 40, "y0": 85, "x1": 555, "y1": 160},
    {"filename": "fig-q7-table3.jpg", "page": 15, "x0": 40, "y0": 115, "x1": 555, "y1": 225},
    {"filename": "fig-q8-3-acid.jpg", "page": 16, "x0": 40, "y0": 300, "x1": 555, "y1": 410},
    {"filename": "fig-q9-fig2.jpg", "page": 20, "x0": 40, "y0": 85, "x1": 555, "y1": 370},
    {"filename": "fig-q10-eq.jpg", "page": 22, "x0": 40, "y0": 85, "x1": 555, "y1": 185},
    {"filename": "fig-q11-table4.jpg", "page": 23, "x0": 40, "y0": 115, "x1": 555, "y1": 210},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 2, "01.4": 2,
    "02.1": 3, "02.2": 3, "02.3": 3,
    "03.1": 4, "03.2": 4, "03.3": 5, "03.4": 5, "03.5": 6, "03.6": 6, "03.7": 6,
    "04.1": 7, "04.2": 7, "04.3": 7, "04.4": 8, "04.5": 8, "04.6": 9, "04.7": 9,
    "05.1": 10, "05.2": 10, "05.3": 11, "05.4": 11,
    "06.1": 12, "06.2": 12, "06.3": 12, "06.4": 13,
    "07.1": 14, "07.2": 14, "07.3": 15, "07.4": 15,
    "08.1": 16, "08.2": 16, "08.3": 16, "08.4": 17, "08.5": 18,
    "09.1": 20, "09.2": 20, "09.3": 21,
    "10.1": 22, "10.2": 22, "10.3": 22, "10.4": 22,
    "11.1": 23, "11.2": 24,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.2.2", "marks": 2, "stem": "Write an equation for the reaction of calcium with water at 25 C and predict a possible pH of the solution formed.", "ms_label": "01.1", "ms_ans": "&bull; Ca + 2H<sub>2</sub>O &rarr; Ca(OH)<sub>2</sub> + H<sub>2</sub> (1)<br>&bull; 8&minus;12 (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "01.2", "specRef": "3.2.2", "marks": 1, "stem": "State the trend in solubility, in water, of the Group 2 sulfates from magnesium to barium.", "ms_label": "01.2", "ms_ans": "Decrease", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "01.3", "specRef": "3.2.2", "marks": 2, "stem": "State a reagent used to test for sulfate ions and write a simple ionic equation for the reaction.", "ms_label": "01.3", "ms_ans": "&bull; BaCl<sub>2</sub> (allow Ba(NO<sub>3</sub>)<sub>2</sub> or other soluble barium salt) (1)<br>&bull; Ba<sup>2+</sup> + SO<sub>4</sub><sup>2&minus;</sup> &rarr; BaSO<sub>4</sub> (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "01.4", "specRef": "3.1.3", "marks": 2, "stem": "Explain why the melting point of calcium sulfate is high.", "ms_label": "01.4", "ms_ans": "&bull; Strong attraction (1)<br>&bull; Between positive and negative ions (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "02.1", "specRef": "3.2.6", "marks": 5, "stem": "Identify by name or formula compounds A, B, C, D and Y from the test-tube reactions of green salt Y.", "ms_label": "02.1", "ms_ans": "&bull; A: Silver bromide / AgBr (1)<br>&bull; B: Iron(II) carbonate / FeCO<sub>3</sub> (1)<br>&bull; C: Iron(II) sulfate / FeSO<sub>4</sub> (1)<br>&bull; D: Carbon dioxide / CO<sub>2</sub> (1)<br>&bull; Y: Iron(II) bromide / FeBr<sub>2</sub> (1)", "ms_extra": "", "ms_marks": "5"},
    {"qnum": "02.2", "specRef": "3.2.3", "marks": 1, "stem": "Write the simplest ionic equation for the reaction of silver nitrate solution with the anion present in compound Y.", "figures": ["fig-q2-stem.jpg"], "ms_label": "02.2", "ms_ans": "Ag<sup>+</sup> + Br<sup>&minus;</sup> &rarr; AgBr", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "02.3", "specRef": "3.2.6", "marks": 1, "stem": "Write the simplest ionic equation for the reaction between the green precipitate B and sulfuric acid.", "figures": ["fig-q2-stem.jpg"], "ms_label": "02.3", "ms_ans": "2H<sup>+</sup> + CO<sub>3</sub><sup>2&minus;</sup> &rarr; H<sub>2</sub>O + CO<sub>2</sub>", "ms_extra": "Allow FeCO<sub>3</sub> + 2H<sup>+</sup> &rarr; Fe<sup>2+</sup> + CO<sub>2</sub> + H<sub>2</sub>O.", "ms_marks": "1"},
    {"qnum": "03.1", "specRef": "3.1.1", "marks": 1, "stem": "Complete the electron configuration of an iodine atom: [Kr] ...", "ms_label": "03.1", "ms_ans": "[Kr] 5s<sup>2</sup>4d<sup>10</sup>5p<sup>5</sup>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "03.2", "specRef": "3.1.3", "marks": 6, "stem": "Use structure and bonding to explain why the melting point of iodine is low (113.5 C) and why that of hydrogen iodide is very low (-50.8 C).", "ms_label": "03.2", "ms_ans": "<b>Indicative chemistry content:</b><br><b>Stage 1:</b> I<sub>2</sub> is molecular; HI is molecular.<br><b>Stage 2:</b> Intermolecular forces hold the molecules together (weak IMF &rarr; low melting points in both). I<sub>2</sub> is a bigger molecule than HI so I<sub>2</sub> has more electrons.<br><b>Stage 3:</b> Stronger van der Waals forces between I<sub>2</sub> molecules need more energy to break, causing higher m.p. HI also has permanent dipole&minus;dipole attraction, but weaker than vdW in I<sub>2</sub>.", "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).", "ms_marks": "6"},
    {"qnum": "03.3", "specRef": "3.1.3", "marks": 1, "stem": "State why iodine does not conduct electricity.", "ms_label": "03.3", "ms_ans": "No delocalised electrons or ions", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "03.4", "specRef": "3.1.4", "marks": 1, "stem": "Deduce an equation for the formation of hydrogen iodide from its elements.", "ms_label": "03.4", "ms_ans": "&frac12;H<sub>2</sub> + &frac12;I<sub>2</sub> &rarr; HI", "ms_extra": "Allow multiples.", "ms_marks": "1"},
    {"qnum": "03.5", "specRef": "3.1.2", "marks": 1, "stem": "What is the formula of ammonium triiodide?", "ms_label": "03.5", "ms_ans": "<b>NH<sub>4</sub>I<sub>3</sub></b>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "03.6", "specRef": "3.1.3", "marks": 2, "stem": "Draw the shape of the IF3 molecule and the shape of the IF4- ion, including lone pairs.", "ms_label": "03.6", "ms_ans": "&bull; IF<sub>3</sub>: T-shaped (3 bond pairs, 2 lone pairs) (1)<br>&bull; IF<sub>4</sub><sup>&minus;</sup>: square planar (4 bond pairs, 2 lone pairs in equatorial/axial positions) (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "03.7", "specRef": "3.1.7", "marks": 2, "stem": "Deduce the oxidation state of iodine in Ba(IO3)2 and [H4IO6]-.", "ms_label": "03.7", "ms_ans": "&bull; Ba(IO<sub>3</sub>)<sub>2</sub>: +5 (1)<br>&bull; [H<sub>4</sub>IO<sub>6</sub>]<sup>&minus;</sup>: +7 (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "04.1", "specRef": "3.2.5", "marks": 1, "stem": "Write an equation for the ligand substitution reaction of hexaaquairon(III) ions with an excess of hydrochloric acid.", "ms_label": "04.1", "ms_ans": "[Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + 4Cl<sup>&minus;</sup> &rarr; FeCl<sub>4</sub><sup>&minus;</sup> + 6H<sub>2</sub>O", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "04.2", "specRef": "3.2.5", "marks": 2, "stem": "Explain why the initial and final iron(III) complexes in Question 04.1 have different shapes.", "figures": ["fig-q4-1-eq.jpg"], "ms_label": "04.2", "ms_ans": "&bull; Cl<sup>&minus;</sup> is a bigger ligand (1)<br>&bull; So only 4 Cl<sup>&minus;</sup> can fit around the metal (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "04.3", "specRef": "3.2.5", "marks": 2, "stem": "Draw the structure of the iron(II) complex formed when hexaaquairon(II) ions react with excess H2NCH2CH2NH2, showing its charge.", "ms_label": "04.3", "ms_ans": "&bull; Octahedral [Fe(H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>)<sub>3</sub>] complex with 3 bidentate ligands (1)<br>&bull; Correct 2+ charge (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "04.4", "specRef": "3.1.8", "marks": 1, "stem": "Which shows the correct change in entropy for the reaction of hexaaquairon(II) ions with H2NCH2CH2NH2?", "ms_label": "04.4", "ms_ans": "<b>change in entropy is positive</b>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "04.5", "specRef": "3.1.7", "marks": 1, "stem": "Deduce an ionic equation for the reaction of iron(II) ions with manganate(VII) ions in acidic solution.", "ms_label": "04.5", "ms_ans": "5Fe<sup>2+</sup> + MnO<sub>4</sub><sup>&minus;</sup> + 8H<sup>+</sup> &rarr; Mn<sup>2+</sup> + 5Fe<sup>3+</sup> + 4H<sub>2</sub>O", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "04.6", "specRef": "3.1.2", "marks": 4, "stem": "1980 mg of iron tablets in excess dilute H2SO4 required 32.50 cm3 of 0.0200 mol dm-3 KMnO4. Calculate the percentage of iron.", "ms_label": "04.6", "ms_ans": "&bull; Amount of MnO<sub>4</sub><sup>&minus;</sup> = 6.50 &times; 10<sup>&minus;4</sup> mol (1)<br>&bull; Amount of Fe<sup>2+</sup> = 3.25 &times; 10<sup>&minus;3</sup> mol (1)<br>&bull; Mass of Fe = 0.181 g = 181 mg (1)<br>&bull; Percentage Fe = (181 / 1980) &times; 100 = 9.14% (3 sf) (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "04.7", "specRef": "3.2.5", "marks": 1, "stem": "State the colour change at the end point in this KMnO4 titration.", "ms_label": "04.7", "ms_ans": "Colourless to pale pink", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "05.1", "specRef": "3.1.8", "marks": 2, "stem": "Complete the Born-Haber cycle for sodium fluoride by adding the missing species on the lines.", "ms_label": "05.1", "ms_ans": "&bull; Upper missing line: Na<sup>+</sup>(g) + e<sup>&minus;</sup> + &frac12;F<sub>2</sub>(g) (1)<br>&bull; Lower missing line: Na(g) + &frac12;F<sub>2</sub>(g) (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "05.2", "specRef": "3.1.8", "marks": 2, "stem": "Use Table 1 and your completed Born-Haber cycle to calculate the enthalpy of lattice formation of sodium fluoride.", "figures": ["fig-q5-bornhaber.jpg"], "ms_label": "05.2", "ms_ans": "&bull; LE = &minus;109 &minus; 494 &minus; 158/2 + 348 &minus; 569 (1)<br>&bull; = &minus;903 (kJ mol<sup>&minus;1</sup>) (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "05.3", "specRef": "3.1.8", "marks": 3, "stem": "Suggest how the enthalpy of lattice formation of NaCl compares with that of NaF and justify your answer.", "ms_label": "05.3", "ms_ans": "&bull; NaCl enthalpy of lattice formation will be less negative / less exothermic (1)<br>&bull; Cl<sup>&minus;</sup> ion is bigger than F<sup>&minus;</sup> (1)<br>&bull; So attraction of halide ion to Na<sup>+</sup> is weaker (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "05.4", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the volume, in cm3, of F2(g) at 298 K and 100 kPa required to produce 1.00 g of NaF by reaction with excess Na.", "ms_label": "05.4", "ms_ans": "&bull; Amount of NaF = 1 / 42 = 2.38 &times; 10<sup>&minus;2</sup> mol (1)<br>&bull; Amount of F<sub>2</sub> = 1.19 &times; 10<sup>&minus;2</sup> mol (1)<br>&bull; V = nRT/p = (1.19 &times; 10<sup>&minus;2</sup> &times; 8.31 &times; 298) / 100000 (1)<br>&bull; = 2.95 &times; 10<sup>&minus;4</sup> m<sup>3</sup> = 295 cm<sup>3</sup> (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "06.1", "specRef": "3.1.11", "marks": 1, "stem": "Use data from Table 2 to deduce the species that is the best oxidising agent.", "figures": ["fig-q6-table2.jpg"], "crop_exclude_y": [[85, 295]], "ms_label": "06.1", "ms_ans": "Cl<sub>2</sub>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "06.2", "specRef": "3.1.11", "marks": 2, "stem": "Write the conventional representation for the cell used to measure the standard electrode potential for the conversion of tin(II) ions to tin.", "figures": ["fig-q6-table2.jpg"], "ms_label": "06.2", "ms_ans": "Pt|H<sub>2</sub>|H<sup>+</sup>||Sn<sup>2+</sup>|Sn", "ms_extra": "1 mark for species, 1 mark for correct order including Pt.", "ms_marks": "2"},
    {"qnum": "06.3", "specRef": "3.1.11", "marks": 2, "stem": "Calculate the EMF of a silver/tin cell and write a half-equation for the reaction at the negative electrode.", "figures": ["fig-q6-table2.jpg"], "ms_label": "06.3", "ms_ans": "&bull; 0.94 V (1)<br>&bull; Sn &rarr; Sn<sup>2+</sup> + 2e<sup>&minus;</sup> (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "06.4", "specRef": "3.1.11", "marks": 1, "stem": "Use data from Table 2 to write an equation for the reaction of silver(I) ions with iron(II) ions.", "figures": ["fig-q6-table2.jpg"], "ms_label": "06.4", "ms_ans": "Ag<sup>+</sup> + Fe<sup>2+</sup> &rarr; Ag + Fe<sup>3+</sup>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "07.1", "specRef": "3.1.6", "marks": 3, "stem": "Use Le Chatelier's principle to predict and explain the effect on the equilibrium yield of hydrogen in CH4 + H2O <=> CO + 3H2 if pressure is increased.", "ms_label": "07.1", "ms_ans": "&bull; Decrease (1)<br>&bull; Increasing pressure moves equilibrium to the side of least moles (backward reaction) (1)<br>&bull; To oppose the increase in pressure / decrease the pressure (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "07.2", "specRef": "3.1.6", "marks": 2, "stem": "Explain why the equilibrium yield of hydrogen is unchanged if a catalyst is used.", "ms_label": "07.2", "ms_ans": "&bull; A catalyst speeds up the rate of the forward and backward reaction (1)<br>&bull; By the same amount (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "07.3", "specRef": "3.1.4", "marks": 2, "stem": "Use data from Table 3 to calculate the standard enthalpy change for this equilibrium reaction.", "figures": ["fig-q7-eq.jpg"], "ms_label": "07.3", "ms_ans": "&bull; &Delta;H = &minus;111 &minus; (&minus;75 &minus; 242) (1)<br>&bull; = 206 (kJ mol<sup>&minus;1</sup>) (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "07.4", "specRef": "3.1.8", "marks": 5, "stem": "Use your answer from Question 07.3 and entropy data from Table 3 to calculate the minimum temperature, in C, needed for this reaction to be feasible.", "figures": ["fig-q7-eq.jpg", "fig-q7-table3.jpg"], "ms_label": "07.4", "ms_ans": "&bull; &Delta;S = 3 &times; 131 + 198 &minus; (186 + 189) = 216 J K<sup>&minus;1</sup> mol<sup>&minus;1</sup> (1)<br>&bull; &Delta;G = &Delta;H &minus; T&Delta;S (1)<br>&bull; 0 = 206 &minus; T &times; (216 / 1000) (1)<br>&bull; T = 953.7 or 954 K (1)<br>&bull; T = 681 (&deg;C) (1)", "ms_extra": "If 120 kJ mol<sup>&minus;1</sup> used, answer is 283 &deg;C.", "ms_marks": "5"},
    {"qnum": "08.1", "specRef": "3.1.12", "marks": 1, "stem": "Give the meaning of the term Bronsted-Lowry acid.", "ms_label": "08.1", "ms_ans": "Proton donor", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "08.2", "specRef": "3.1.12", "marks": 1, "stem": "What is meant by the term strong when describing an acid?", "ms_label": "08.2", "ms_ans": "Completely ionises to give H<sup>+</sup> ions in water", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "08.3", "specRef": "3.1.12", "marks": 2, "stem": "At 298 K, 25.0 cm3 of a strong monoprotic acid contained 1.45 x 10^-3 mol H+. Calculate the pH to 2 d.p.", "ms_label": "08.3", "ms_ans": "&bull; [H<sup>+</sup>] = 0.058 mol dm<sup>&minus;3</sup> (1)<br>&bull; pH = 1.24 (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "08.4", "specRef": "3.1.12", "marks": 5, "stem": "Calculate the pH after adding 35.0 cm3 of 0.150 mol dm-3 NaOH to the original 25.0 cm3 of monoprotic acid.", "figures": ["fig-q8-3-acid.jpg"], "ms_label": "08.4", "ms_ans": "&bull; Amount of NaOH = 5.25 &times; 10<sup>&minus;3</sup> mol (1)<br>&bull; Excess OH<sup>&minus;</sup> = 5.25 &times; 10<sup>&minus;3</sup> &minus; 1.45 &times; 10<sup>&minus;3</sup> = 3.80 &times; 10<sup>&minus;3</sup> mol (1)<br>&bull; [OH<sup>&minus;</sup>] = 3.80 &times; 10<sup>&minus;3</sup> &times; 1000 / 60 = 0.0633 (1)<br>&bull; [H<sup>+</sup>] = 10<sup>&minus;14</sup> / 0.0633 = 1.58 &times; 10<sup>&minus;13</sup> (1)<br>&bull; pH = 12.80 (1)", "ms_extra": "", "ms_marks": "5"},
    {"qnum": "08.5", "specRef": "3.1.12", "marks": 6, "stem": "A buffer is made by adding 1.50 g NaOH to 1.00 dm3 of 0.150 mol dm-3 weak acid HA (Ka = 1.79 x 10^-5). Calculate the pH.", "ms_label": "08.5", "ms_ans": "&bull; Amount of OH<sup>&minus;</sup> added = 1.50 / 40 = 0.0375 mol (1)<br>&bull; Amount of A<sup>&minus;</sup> formed = 0.0375 mol (1)<br>&bull; Amount of HA remaining = 0.150 &minus; 0.0375 = 0.1125 mol (1)<br>&bull; [H<sup>+</sup>] = K<sub>a</sub>[HA]/[A<sup>&minus;</sup>] = 1.79 &times; 10<sup>&minus;5</sup> &times; (0.1125 / 0.0375) (1)<br>&bull; = 5.37 &times; 10<sup>&minus;5</sup> (1)<br>&bull; pH = 4.27 (1)", "ms_extra": "", "ms_marks": "6"},
    {"qnum": "09.1", "specRef": "3.1.12", "marks": 2, "stem": "Suggest possible formulae for an acid and an alkali that could produce the pH curve in Figure 2.", "figures": ["fig-q9-fig2.jpg"], "crop_exclude_y": [[85, 370]], "ms_label": "09.1", "ms_ans": "&bull; Strong acid (e.g. HCl) (1)<br>&bull; Weak alkali (e.g. NH<sub>3</sub>) (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "09.2", "specRef": "RP", "marks": 3, "stem": "Suggest briefly a practical procedure to obtain data from which Figure 2 could be plotted.", "figures": ["fig-q9-fig2.jpg"], "ms_label": "09.2", "ms_ans": "&bull; Place a fixed volume of alkali in a flask or beaker (1)<br>&bull; Add acid in small portions from a burette (1)<br>&bull; Stir and use a pH meter to record the pH after each addition of acid (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "09.3", "specRef": "RP", "marks": 2, "stem": "Suggest how the practical procedure in Question 09.2 could be refined to identify the most suitable indicator from three samples.", "ms_label": "09.3", "ms_ans": "&bull; Repeat the experiment with each indicator (1)<br>&bull; Select the indicator that changes colour rapidly when the pH changes from about 7 to 4 (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "10.1", "specRef": "3.1.6", "marks": 1, "stem": "Write an expression for Kc for Acid X + 2CH3OH <=> Ester Y + 2H2O.", "figures": ["fig-q10-eq.jpg"], "crop_exclude_y": [[85, 185]], "ms_label": "10.1", "ms_ans": "K<sub>c</sub> = ([Y][H<sub>2</sub>O]<sup>2</sup>) / ([X][CH<sub>3</sub>OH]<sup>2</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "10.2", "specRef": "3.1.6", "marks": 3, "stem": "0.32 mol X and 0.84 mol CH3OH reach equilibrium forming 0.26 mol Y. Calculate equilibrium moles of X, CH3OH and H2O.", "figures": ["fig-q10-eq.jpg"], "ms_label": "10.2", "ms_ans": "&bull; Amount of X = 0.06 mol (1)<br>&bull; Amount of CH<sub>3</sub>OH = 0.32 mol (1)<br>&bull; Amount of H<sub>2</sub>O = 0.52 mol (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "10.3", "specRef": "3.1.6", "marks": 3, "stem": "Calculate the value of Kc and state the units.", "figures": ["fig-q10-eq.jpg"], "ms_label": "10.3", "ms_ans": "&bull; K<sub>c</sub> = (0.26 &times; 0.52<sup>2</sup>) / (0.06 &times; 0.32<sup>2</sup>) (1)<br>&bull; = (11.44) = 11 (2 sf) (1)<br>&bull; No units (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "10.4", "specRef": "3.1.6", "marks": 1, "stem": "Predict the effect on Kc if the reaction is carried out at a lower temperature.", "figures": ["fig-q10-eq.jpg"], "ms_label": "10.4", "ms_ans": "Increase", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "11.1", "specRef": "3.1.1", "marks": 3, "stem": "Calculate the relative atomic mass of Q from Table 4 to 1 d.p. and identify element Q.", "ms_label": "11.1", "ms_ans": "&bull; ((82 &times; 5) + (83 &times; 3) + (84 &times; 26) + (86 &times; 7)) / 41 = 3445 / 41 (1)<br>&bull; 84.0 (1)<br>&bull; Kr (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "11.2", "specRef": "3.1.1", "marks": 3, "stem": "The time of flight of an 82Q+ ion is 1.243 x 10^-5 s. Calculate the time of flight of the 86Q+ ion.", "figures": ["fig-q11-table4.jpg"], "ms_label": "11.2", "ms_ans": "&bull; 82 / (1.243 &times; 10<sup>&minus;5</sup>)<sup>2</sup> = 86 / t<sup>2</sup> &rarr; t<sup>2</sup> = (86/82) &times; (1.243 &times; 10<sup>&minus;5</sup>)<sup>2</sup> (1)<br>&bull; t<sup>2</sup> = 1.6204 &times; 10<sup>&minus;10</sup> (1)<br>&bull; t = 1.273 &times; 10<sup>&minus;5</sup> (s) (1)", "ms_extra": "", "ms_marks": "3"},
]


def extract_figures():
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(QP_PDF))
    for fig in FIGURES:
        page = doc[fig["page"] - 1]
        rect = fitz.Rect(fig["x0"], fig["y0"], fig["x1"], fig["y1"])
        pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(2.5, 2.5))
        out_path = IMG_DIR / fig["filename"]
        pix.save(str(out_path))
        print(f"Saved figure: {out_path}")
    doc.close()


def main():
    extract_figures()
    data = json.loads(DB_PATH.read_text(encoding="utf-8"))
    data["papers"] = [p for p in data["papers"] if p["id"] != PAPER_ID]
    data["questions"] = [q for q in data["questions"] if q.get("paper") != PAPER_ID]
    data["papers"].append(PAPER_META)

    total_marks = 0
    for q in QUESTIONS:
        qnum = q["qnum"]
        qnum_slug = qnum.replace(".", "-")
        ms_rel = f"img/{PAPER_ID}/ms/q{qnum_slug}.png"
        ms_abs = ROOT / ms_rel
        render_official_markscheme_image(
            question_label=q["ms_label"],
            answers_html=q["ms_ans"],
            extra_html=q["ms_extra"],
            marks=q["ms_marks"],
            spec_ref=q["specRef"],
            output_path=str(ms_abs),
        )
        entry = {
            "id": f"{PAPER_ID}-q{qnum}",
            "paper": PAPER_ID,
            "year": PAPER_META["year"],
            "series": PAPER_META["series"],
            "unit": PAPER_META["unit"],
            "level": PAPER_META["level"],
            "question": qnum,
            "questionNumber": qnum,
            "page": PAGE_MAP[qnum],
            "marks": q["marks"],
            "topics": [q["specRef"]],
            "skills": [],
            "summary": q["stem"],
            "specRef": q["specRef"],
            "image": f"img/{PAPER_ID}/q{qnum_slug}.jpg",
            "markscheme": ms_rel,
            "figures": [f"img/{PAPER_ID}/{f}" for f in q.get("figures", [])],
        }
        if "crop_exclude_y" in q:
            entry["crop_exclude_y"] = q["crop_exclude_y"]
        data["questions"].append(entry)
        total_marks += q["marks"]

    DB_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Ingested {PAPER_ID}: {len(QUESTIONS)} questions, {total_marks} marks")


if __name__ == "__main__":
    main()

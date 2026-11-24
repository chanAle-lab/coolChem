"""Ingest AQA A-level Chemistry Specimen Set 2 Paper 3 (7405/3) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517647587_21f98d76.pdf"
)

PAPER_ID = "2016-specimen2-7405-3"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2016,
    "series": "Specimen Set 2",
    "unit": "7405/3",
    "level": "A-level",
    "date": "2016-01-01",
    "title": "7405/3 — A-level Paper 3: Practical Skills, Data Analysis & Synopsis (Specimen Set 2)",
    "totalMarks": 90,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-paracetamol.jpg", "page": 2, "x0": 40, "y0": 100, "x1": 555, "y1": 275},
    {"filename": "fig-q3-fig1.jpg", "page": 11, "x0": 40, "y0": 85, "x1": 555, "y1": 320},
    {"filename": "fig-q4-table1.jpg", "page": 14, "x0": 40, "y0": 85, "x1": 555, "y1": 355},
    {"filename": "fig-q4-3.jpg", "page": 15, "x0": 40, "y0": 70, "x1": 555, "y1": 250},
    {"filename": "fig-q13-14-mb.jpg", "page": 22, "x0": 40, "y0": 70, "x1": 555, "y1": 375},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3, "01.3": 4, "01.4": 6, "01.5": 7, "01.6": 7,
    "02.1": 8, "02.2": 8, "02.3": 8, "02.4": 9, "02.5": 10,
    "03.1": 11, "03.2": 12, "03.3": 13,
    "04.1": 14, "04.2": 14, "04.3": 15, "04.4": 16, "04.5": 17, "04.6": 17,
    "05": 18, "06": 18,
    "07": 19, "08": 19, "09": 19,
    "10": 20, "11": 20,
    "12": 21,
    "13": 22, "14": 22,
    "15": 23, "16": 23,
    "17": 24, "18": 24,
    "19": 25, "20": 25, "21": 25,
    "22": 26, "23": 26,
    "24": 27, "25": 27, "26": 27,
    "27": 28, "28": 28,
    "29": 29, "30": 29, "31": 29,
    "32": 30, "33": 30,
    "34": 31,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.9", "marks": 1, "stem": "Write an equation for the preparation of paracetamol from 4-aminophenol and ethanoyl chloride.", "ms_label": "01.1", "ms_ans": "2HO&minus;C<sub>6</sub>H<sub>4</sub>&minus;NH<sub>2</sub> + CH<sub>3</sub>COCl &rarr; HO&minus;C<sub>6</sub>H<sub>4</sub>&minus;NHCOCH<sub>3</sub> + HO&minus;C<sub>6</sub>H<sub>4</sub>&minus;NH<sub>3</sub><sup>+</sup>Cl<sup>&minus;</sup><br>(Allow HO&minus;C<sub>6</sub>H<sub>4</sub>&minus;NH<sub>2</sub> + CH<sub>3</sub>COCl &rarr; HO&minus;C<sub>6</sub>H<sub>4</sub>&minus;NHCOCH<sub>3</sub> + HCl)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "01.2", "specRef": "3.3.9", "marks": 5, "stem": "Name and outline the mechanism for the reaction of 4-aminophenol (RNH2) with ethanoyl chloride.", "figures": ["fig-q1-paracetamol.jpg"], "ms_label": "01.2", "ms_ans": "&bull; (Nucleophilic) Addition-elimination (1)<br>&bull; M2: arrow from lone pair on N to C of C=O (1)<br>&bull; M3: arrow from C=O bond to O (1) + intermediate with + on N and &minus; on O (1)<br>&bull; M4: three arrows and lone pair on O<sup>&minus;</sup> (1)", "ms_extra": "", "ms_marks": "5"},
    {"qnum": "01.3", "specRef": "RP", "marks": 6, "stem": "Outline how to investigate whether a flammable solvent (b.p. 80 C) is suitable for recrystallising impure paracetamol, and how to check purity.", "ms_label": "01.3", "ms_ans": "<b>Indicative chemistry content:</b><br>&bull; Place small amount of pure paracetamol in a test-tube, add small volume (0.5&minus;1.0 cm<sup>3</sup>) of solvent, shake/stir; if it dissolves, solvent unsuitable.<br>&bull; Heat in hot (not boiling) water bath; if it does not dissolve, unsuitable (try adding more solvent if partial).<br>&bull; Place test-tube in ice-water bath; if crystals form = suitable.<br>&bull; Measure melting point: purity indicated by sharp m.p. close to 170 &plusmn; 2 &deg;C.", "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).", "ms_marks": "6"},
    {"qnum": "01.4", "specRef": "3.1.2", "marks": 4, "stem": "Starting with 3.87 g ethanoyl chloride, 4.07 g pure paracetamol was obtained (expected impure yield 65%). Calculate expected impure mass and comment on the student's practical skills.", "ms_label": "01.4", "ms_ans": "&bull; Amount of ethanoyl chloride = 3.87 / 78.5 = 0.0493 mol (1)<br>&bull; Expected impure mass = 0.65 &times; (0.0493 &times; 151) = 4.84 g (1)<br>&bull; Loss in mass = 4.84 &minus; 4.07 = 0.77 g (1)<br>&bull; % loss = (0.77 / 4.84) &times; 100 = 15.9%; less than 20% loss suggests expert practical skills (or sample may not be dry) (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "01.5", "specRef": "RP", "marks": 1, "stem": "Suggest why the student should not use this sample of paracetamol for pain relief.", "ms_label": "01.5", "ms_ans": "There may still be small amounts of impurities", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "01.6", "specRef": "3.3.9", "marks": 2, "stem": "Suggest two reasons why ethanoic anhydride is preferred to ethanoyl chloride industrially in producing paracetamol.", "ms_label": "01.6", "ms_ans": "Any two from:<br>&bull; Less exothermic reaction<br>&bull; Easier to control<br>&bull; Dangerous gas (HCl) not evolved<br>&bull; Ethanoic anhydride is cheaper or more easily recycled", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "02.1", "specRef": "3.3.9", "marks": 1, "stem": "Write an equation for the esterification reaction between ethanoic acid and ethanol.", "ms_label": "02.1", "ms_ans": "CH<sub>3</sub>COOH + CH<sub>3</sub>CH<sub>2</sub>OH &#8652; CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub> + H<sub>2</sub>O", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "02.2", "specRef": "3.3.1", "marks": 1, "stem": "Draw the skeletal formula of ethyl ethanoate.", "ms_label": "02.2", "ms_ans": "Skeletal formula of CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "02.3", "specRef": "3.1.5", "marks": 2, "stem": "State, in general terms, how a catalyst works.", "ms_label": "02.3", "ms_ans": "&bull; Provides an alternative mechanism / pathway for reaction (1)<br>&bull; That has a lower activation energy (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "02.4", "specRef": "3.1.6", "marks": 6, "stem": "0.0435 mol ethanol, 0.0435 mol ethanoic acid and 5.00 x 10^-4 mol H2SO4 reach equilibrium (Kc = 4.07). Calculate the volume of 0.400 mol dm-3 NaOH required to react with the acids.", "ms_label": "02.4", "ms_ans": "&bull; K<sub>c</sub> = [ester][water] / ([acid][alcohol]) (1)<br>&bull; 4.07 = x<sup>2</sup> / (0.0435 &minus; x)<sup>2</sup> (1)<br>&bull; &radic;4.07 = x / (0.0435 &minus; x) &rarr; x = 0.0291 mol (1)<br>&bull; Ethanoic acid left = 0.0435 &minus; 0.0291 = 0.0144 mol (1)<br>&bull; Total H<sup>+</sup> including catalyst = 0.0144 + 2(0.0005) = 0.0154 mol (1)<br>&bull; Volume NaOH = 1000 &times; 0.0154 / 0.400 = 38.5 cm<sup>3</sup> (1)", "ms_extra": "", "ms_marks": "6"},
    {"qnum": "02.5", "specRef": "RP", "marks": 2, "stem": "Suggest how the student could check that the mixture had reached equilibrium after one week.", "ms_label": "02.5", "ms_ans": "&bull; Test several samples &minus; at least one tested after a week (1)<br>&bull; Check that the result has not changed (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "03.1", "specRef": "3.2.5", "marks": 3, "stem": "Explain the terms multidentate and ligand for EDTA4- reacting with [Cu(H2O)6]2+, and circle each bonding atom on Figure 1.", "figures": ["fig-q3-fig1.jpg"], "crop_exclude_y": [[85, 320]], "ms_label": "03.1", "ms_ans": "&bull; Multidentate: EDTA can form many / six dative bonds with central cation (1)<br>&bull; Ligand: lone pair (on N or O of EDTA) can form dative bond with copper(II) ions (1)<br>&bull; 6 circles drawn on EDTA<sup>4&minus;</sup>: 2 &times; N and 4 &times; &minus;O<sup>&minus;</sup> (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "03.2", "specRef": "3.2.5", "marks": 4, "stem": "Outline the practical steps, using colorimetry, to determine the concentration of the copper(II)-EDTA complex in a water sample.", "figures": ["fig-q3-fig1.jpg"], "ms_label": "03.2", "ms_ans": "&bull; Calibrate a colorimeter / produce a calibration curve (1)<br>&bull; By testing the colorimeter with solutions of copper-EDTA complex of known concentration (1)<br>&bull; Add excess EDTA salt to the sample (1)<br>&bull; Measure absorbance of sample and read concentration from calibration curve (1)", "ms_extra": "(3 marks in MS: calibrate/calibration curve, known concentrations, add excess EDTA)", "ms_marks": "4"},
    {"qnum": "03.3", "specRef": "3.2.5", "marks": 5, "stem": "Write an equation for [Cu(H2O)6]2+ + EDTA4-, calculate the volume of 1.00 x 10^-3 mol dm-3 EDTA4- needed for 25.0 cm3 of 7.56 x 10^-5 mol dm-3 Cu2+, and comment on accuracy.", "ms_label": "03.3", "ms_ans": "&bull; [Cu(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + EDTA<sup>4&minus;</sup> &rarr; [Cu(EDTA)]<sup>2&minus;</sup> + 6H<sub>2</sub>O (1)<br>&bull; Amount of Cu(II) = 25.0 &times; 7.56 &times; 10<sup>&minus;5</sup> / 1000 = 1.89 &times; 10<sup>&minus;6</sup> mol (1)<br>&bull; Volume of EDTA<sup>4&minus;</sup> = (1.89 &times; 10<sup>&minus;6</sup> / 0.001) &times; 1000 = 1.89 cm<sup>3</sup> (1)<br>&bull; This is too small to be accurate (1)<br>&bull; Dilute the EDTA<sup>4&minus;</sup> solution / use larger volume of river water (1)", "ms_extra": "", "ms_marks": "5"},
    {"qnum": "04.1", "specRef": "3.1.2", "marks": 2, "stem": "Calculate the initial concentration of propanone in mixture A (Table 1).", "ms_label": "04.1", "ms_ans": "&bull; Amount of propanone = (25.0 &times; 1) / 1000 = 0.025 mol (1)<br>&bull; Concentration in mixture A = 0.025 / (90.0 / 1000) = 0.278 mol dm<sup>&minus;3</sup> (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "04.2", "specRef": "RP", "marks": 2, "stem": "State and explain why different volumes of water are added to mixtures B, C, D and E (Table 1).", "figures": ["fig-q4-table1.jpg"], "ms_label": "04.2", "ms_ans": "&bull; To make volumes constant for all mixtures (1)<br>&bull; So that volume of propanone is proportional to concentration (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "04.3", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the volume of 0.0100 mol dm-3 Na2S2O3 required to react with all the iodine in a 10.0 cm3 sample of mixture E before reaction.", "figures": ["fig-q4-table1.jpg"], "ms_label": "04.3", "ms_ans": "&bull; Amount of I<sub>2</sub> in mixture E = (40.0 &times; 0.02) / 1000 = 8.0 &times; 10<sup>&minus;4</sup> mol (1)<br>&bull; Amount of I<sub>2</sub> in 10 cm<sup>3</sup> sample = 8.0 &times; 10<sup>&minus;4</sup> &times; (10/90) = 8.89 &times; 10<sup>&minus;5</sup> mol (1)<br>&bull; Amount of thiosulfate = 2 &times; 8.89 &times; 10<sup>&minus;5</sup> = 1.78 &times; 10<sup>&minus;4</sup> mol (1)<br>&bull; Volume of thiosulfate = (1.78 &times; 10<sup>&minus;4</sup> / 0.01) &times; 1000 = 17.8 cm<sup>3</sup> (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "04.4", "specRef": "3.1.9", "marks": 5, "stem": "Use Table 2 and Question 04.3 to plot a graph of V against t for mixture E, draw a best-fit straight line, and calculate its gradient.", "figures": ["fig-q4-3.jpg"], "ms_label": "04.4", "ms_ans": "&bull; Scale covering &ge; half the grid in correct orientation (1)<br>&bull; Points plotted within &plusmn;&frac12; small square (1)<br>&bull; Best-fit straight line (1)<br>&bull; Gradient = y / x (1)<br>&bull; = &minus;0.060 (allow &minus;0.059 to &minus;0.061) (1)", "ms_extra": "", "ms_marks": "5"},
    {"qnum": "04.5", "specRef": "3.1.9", "marks": 2, "stem": "Use Table 1 and Table 3 to deduce the order with respect to propanone and explain your answer.", "figures": ["fig-q4-table1.jpg"], "ms_label": "04.5", "ms_ans": "&bull; Gradients/rates are proportional to volumes/concentrations of propanone (or B to D show rate halves when concentration halves) (1)<br>&bull; So first order with regard to propanone (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "04.6", "specRef": "RP", "marks": 2, "stem": "Suggest the purpose of adding each sample to an excess of sodium hydrogencarbonate solution before titration and explain your answer.", "ms_label": "04.6", "ms_ans": "&bull; To stop / quench the reaction at that time (1)<br>&bull; By removing the acid catalyst for the reaction (by neutralisation) (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "05", "specRef": "3.1.1", "marks": 1, "stem": "What are the numbers of neutrons and electrons in the 57Fe2+ ion?", "ms_label": "05", "ms_ans": "<b>A</b> (31 neutrons, 24 electrons)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "06", "specRef": "3.1.2", "marks": 1, "stem": "Which of these contains the most molecules?", "ms_label": "06", "ms_ans": "<b>B</b> (29.6 g of carbon monoxide, CO)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "07", "specRef": "3.1.3", "marks": 1, "stem": "Which of these statements best describes a dative covalent bond?", "ms_label": "07", "ms_ans": "<b>B</b> (A pair of electrons shared between two atoms where one atom has donated two electrons)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "08", "specRef": "3.1.3", "marks": 1, "stem": "Which molecule is the least polar?", "ms_label": "08", "ms_ans": "<b>D</b> (Tetrabromomethane)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "09", "specRef": "3.1.3", "marks": 1, "stem": "Which statement about intermolecular forces is not correct?", "ms_label": "09", "ms_ans": "<b>B</b> (Hydrogen bonding occurs between HBr molecules)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "10", "specRef": "3.1.4", "marks": 1, "stem": "What is the standard enthalpy of formation, in kJ mol-1, for HF(g)?", "ms_label": "10", "ms_ans": "<b>B</b> (&minus;273)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "11", "specRef": "3.1.4", "marks": 1, "stem": "What is the temperature rise, in K, when 504 J of heat energy are absorbed by 0.110 kg of solid iron?", "ms_label": "11", "ms_ans": "<b>B</b> (1.02 &times; 10<sup>1</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "12", "specRef": "3.1.4", "marks": 1, "stem": "Calculate the enthalpy change, in kJ, for this dissociation of 1 mole of propan-1-ol.", "ms_label": "12", "ms_ans": "<b>C</b> (+4403)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "13", "specRef": "3.1.5", "marks": 1, "stem": "Which letter shows the mean energy of the molecules at the higher temperature?", "figures": ["fig-q13-14-mb.jpg"], "crop_exclude_y": [[70, 375]], "ms_label": "13", "ms_ans": "<b>D</b> (S)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "14", "specRef": "3.1.5", "marks": 1, "stem": "Which statement is correct for the higher temperature?", "figures": ["fig-q13-14-mb.jpg"], "ms_label": "14", "ms_ans": "<b>A</b> (The area under the curve to the left of E<sub>a</sub> decreases)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "15", "specRef": "3.1.9", "marks": 1, "stem": "What is the overall order of reaction from the rate investigation table?", "ms_label": "15", "ms_ans": "<b>D</b> (3)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "16", "specRef": "3.1.10", "marks": 1, "stem": "Which statement about Kp is correct for W + X + Y2 <=> WXY + Y (delta H = -46 kJ mol-1)?", "ms_label": "16", "ms_ans": "<b>A</b> (The value of K<sub>p</sub> is independent of pressure)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "17", "specRef": "3.1.12", "marks": 1, "stem": "Which statement about the pKa values of propanoic acid (4.87) and butanoic acid (4.82) is correct?", "ms_label": "17", "ms_ans": "<b>C</b> (The value of K<sub>a</sub> for propanoic acid is 1.35 &times; 10<sup>&minus;5</sup> mol dm<sup>&minus;3</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "18", "specRef": "3.1.1", "marks": 1, "stem": "Which element is in the f-block of the Periodic Table?", "ms_label": "18", "ms_ans": "<b>D</b> (Plutonium)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "19", "specRef": "3.2.1", "marks": 1, "stem": "Which elements are shown in increasing order of the stated property?", "ms_label": "19", "ms_ans": "<b>D</b> (Melting point: argon, chlorine, sulfur)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "20", "specRef": "3.2.3", "marks": 1, "stem": "Which statement is not correct about the addition of chlorine to water?", "ms_label": "20", "ms_ans": "<b>A</b> (Chlorine can react with water to form an alkaline solution)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "21", "specRef": "3.2.4", "marks": 1, "stem": "Which is the formula of the main aluminium-containing species present when aluminium oxide is added to an excess of water?", "ms_label": "21", "ms_ans": "<b>D</b> (Al<sub>2</sub>O<sub>3</sub>(s))", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "22", "specRef": "3.2.5", "marks": 1, "stem": "What is the electron configuration of Cu2+?", "ms_label": "22", "ms_ans": "<b>C</b> ([Ar]3d<sup>9</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "23", "specRef": "3.2.5", "marks": 1, "stem": "What is the increase in energy, in J, for each electron excited in copper(II) ions by 600 nm light?", "ms_label": "23", "ms_ans": "<b>D</b> (3.32 &times; 10<sup>&minus;19</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "24", "specRef": "3.2.5", "marks": 1, "stem": "What is the formula of the vanadium-containing intermediate formed in the Contact process?", "ms_label": "24", "ms_ans": "<b>D</b> (V<sub>2</sub>O<sub>4</sub>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "25", "specRef": "3.3.2", "marks": 1, "stem": "Which catalyst is used in the catalytic cracking of alkanes?", "ms_label": "25", "ms_ans": "<b>D</b> (Zeolite)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "26", "specRef": "3.3.2", "marks": 1, "stem": "Which correctly represents an incomplete combustion of pentane?", "ms_label": "26", "ms_ans": "<b>C</b> (C<sub>5</sub>H<sub>12</sub> + 6O<sub>2</sub> &rarr; 4CO + CO<sub>2</sub> + 6H<sub>2</sub>O)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "27", "specRef": "3.3.2", "marks": 1, "stem": "Which species is produced in a propagation step during the reaction of propane with excess chlorine in UV light?", "ms_label": "27", "ms_ans": "<b>C</b> (C<sub>3</sub>H<sub>6</sub>Cl<sub>2</sub>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "28", "specRef": "3.3.7", "marks": 1, "stem": "Which compound forms a racemic mixture when reacted with KCN followed by dilute acid?", "ms_label": "28", "ms_ans": "<b>B</b> (CH<sub>3</sub>CHO)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "29", "specRef": "3.3.10", "marks": 1, "stem": "Identify the compound that has the most exothermic enthalpy of hydrogenation.", "ms_label": "29", "ms_ans": "<b>A</b> (cyclohexa-1,3,5-triene hypothetical / 3 double bonds — wait MS says A)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "30", "specRef": "3.3.11", "marks": 1, "stem": "Which compound is the strongest base?", "ms_label": "30", "ms_ans": "<b>C</b> (Methylamine)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "31", "specRef": "3.3.11", "marks": 1, "stem": "What type of reaction converts (CH3)3N into the cationic surfactant [(CH3)3N(CH2)15CH3]Cl?", "ms_label": "31", "ms_ans": "<b>D</b> (Nucleophilic substitution)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "32", "specRef": "3.3.12", "marks": 1, "stem": "Which polymer is least likely to be biodegraded after several years in a landfill site?", "ms_label": "32", "ms_ans": "<b>C</b> (Polythene)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "33", "specRef": "3.3.13", "marks": 1, "stem": "Which structure shows 2-aminobutanoic acid as a zwitterion?", "ms_label": "33", "ms_ans": "<b>B</b>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "34", "specRef": "3.3.14", "marks": 1, "stem": "What is the identity of the alkene used to synthesise 2-methylbutylamine?", "ms_label": "34", "ms_ans": "<b>A</b> (But-2-ene)", "ms_extra": "", "ms_marks": "1"},
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

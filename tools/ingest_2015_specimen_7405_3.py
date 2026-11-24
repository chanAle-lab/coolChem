"""Ingest AQA A-level Chemistry Specimen Paper 3 (7405/3) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517607486_27dfbf57.pdf"
)

PAPER_ID = "2015-specimen-7405-3"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2015,
    "series": "Specimen",
    "unit": "7405/3",
    "level": "A-level",
    "date": "2015-01-01",
    "title": "7405/3 — A-level Paper 3: Practical Skills, Data Analysis & Synopsis (Specimen)",
    "totalMarks": 90,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-table1.jpg", "page": 3, "x0": 40, "y0": 115, "x1": 565, "y1": 210},
    {"filename": "fig-q2-table2.jpg", "page": 6, "x0": 25, "y0": 78, "x1": 565, "y1": 275},
    {"filename": "fig-q3-stem.jpg", "page": 8, "x0": 40, "y0": 65, "x1": 565, "y1": 330},
    {"filename": "fig-q4-stem.jpg", "page": 10, "x0": 40, "y0": 78, "x1": 565, "y1": 190},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 4, "01.5": 4,
    "02.1": 5, "02.2": 6, "02.3": 6, "02.4": 6, "02.5": 7, "02.6": 7,
    "03.1": 8, "03.2": 9, "03.3": 9,
    "04.1": 10, "04.2": 11, "04.3": 12,
    "05.1": 13, "05.2": 13,
    "06": 14, "07": 14,
    "08": 15, "09": 15,
    "10": 16, "11": 16, "12": 16,
    "13": 17, "14": 17, "15": 17,
    "16": 18, "17": 18, "18": 18,
    "19": 19, "20": 19, "21": 19,
    "22": 20, "23": 20, "24": 20,
    "25": 21, "26": 21, "27": 21, "28": 21,
    "29": 22, "30": 22, "31": 22, "32": 22,
    "33": 23, "34": 23,
    "35": 24,
}

QUESTIONS = [
    {
        "qnum": "01.1", "specRef": "RP", "marks": 3,
        "stem": "Describe what happens when a reaction mixture is refluxed and why it is necessary for complete oxidation of ethanol to ethanoic acid.",
        "ms_label": "01.1",
        "ms_ans": (
            "&bull; A mixture of liquids is heated to boiling point for a prolonged time (1)<br>"
            "&bull; Vapour is formed which escapes from the liquid mixture, is changed back into liquid and returned to the liquid mixture (1)<br>"
            "&bull; Any ethanal and ethanol that initially evaporates can then be oxidised (1)"
        ),
        "ms_extra": "", "ms_marks": "3",
    },
    {
        "qnum": "01.2", "specRef": "3.1.7", "marks": 1,
        "stem": "Write a half-equation for the overall oxidation of ethanol into ethanoic acid.",
        "ms_label": "01.2",
        "ms_ans": "CH<sub>3</sub>CH<sub>2</sub>OH + H<sub>2</sub>O &rarr; CH<sub>3</sub>COOH + 4H<sup>+</sup> + 4e<sup>&minus;</sup>",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "01.3", "specRef": "RP", "marks": 5,
        "stem": "Use Table 1 to describe how to obtain a sample of ethanal from a mixture of ethanol, ethanal and ethanoic acid, including apparatus and how to minimise loss of ethanal.",
        "ms_label": "01.3",
        "ms_ans": (
            "&bull; Mixture heated in a suitable flask / container (1)<br>"
            "&bull; With still head containing a thermometer (1)<br>"
            "&bull; Water-cooled condenser connected to the still head and suitable cooled collecting vessel (1)<br>"
            "&bull; Collect sample at the boiling point of ethanal (1)<br>"
            "&bull; Cooled collection vessel necessary to reduce evaporation of ethanal (1)"
        ),
        "ms_extra": "A labelled sketch illustrating these points scores the marks.", "ms_marks": "5",
    },
    {
        "qnum": "01.4", "specRef": "3.1.3", "marks": 2,
        "stem": "Use your knowledge of structure and bonding to explain why it is possible to separate ethanal in this way.",
        "figures": ["fig-q1-table1.jpg"],
        "ms_label": "01.4",
        "ms_ans": (
            "&bull; Hydrogen bonding in ethanol and ethanoic acid / no hydrogen bonding in ethanal (1)<br>"
            "&bull; Intermolecular forces / dipole&minus;dipole are weaker than hydrogen bonding (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "01.5", "specRef": "3.3.6", "marks": 5,
        "stem": "Describe how the student could use chemical tests to confirm that the liquid contained ethanal and did not contain ethanoic acid.",
        "ms_label": "01.5",
        "ms_ans": (
            "<b>Confirm presence of ethanal:</b><br>"
            "&bull; Add Tollens' reagent (or Fehling's solution) (1)<br>"
            "&bull; Warm (1)<br>"
            "&bull; Silver mirror / black precipitate (with Tollens') OR red / orange-red precipitate (with Fehling's) (1)<br>"
            "<b>Confirm absence of ethanoic acid:</b><br>"
            "&bull; Add sodium hydrogencarbonate or sodium carbonate (OR add ethanol + conc H<sub>2</sub>SO<sub>4</sub> and warm) (1)<br>"
            "&bull; No effervescence observed; hence no acid present (OR no sweet smell / no oily drops) (1)"
        ),
        "ms_extra": "M2/M3 conditional on M1; M5 conditional on M4.", "ms_marks": "5",
    },
    {
        "qnum": "02.1", "specRef": "3.1.6", "marks": 6,
        "stem": "8.00 x 10^-2 mol ethanoic acid and 1.20 x 10^-1 mol ethanol reach equilibrium at 20 C, made up to 250 cm3. A 10.0 cm3 sample reacts with 3.20 cm3 of 2.00 x 10^-1 mol dm-3 NaOH. Calculate Kc.",
        "ms_label": "02.1",
        "ms_ans": (
            "<b>Stage 1: Moles of acid at equilibrium</b><br>"
            "&bull; Moles NaOH in titration = (3.20 &times; 2.00 &times; 10<sup>&minus;1</sup>) / 1000 = 6.40 &times; 10<sup>&minus;4</sup> (1)<br>"
            "&bull; Moles of acid in 250 cm<sup>3</sup> = 25 &times; 6.40 &times; 10<sup>&minus;4</sup> = 1.60 &times; 10<sup>&minus;2</sup> (1)<br>"
            "<b>Stage 2 &amp; 3: Moles reacted &amp; ethanol remaining</b><br>"
            "&bull; Moles acid reacted = 8.00 &times; 10<sup>&minus;2</sup> &minus; 1.60 &times; 10<sup>&minus;2</sup> = 6.40 &times; 10<sup>&minus;2</sup> (= moles ester &amp; water) (1)<br>"
            "&bull; Moles ethanol remaining = 1.20 &times; 10<sup>&minus;1</sup> &minus; 6.40 &times; 10<sup>&minus;2</sup> = 5.60 &times; 10<sup>&minus;2</sup> (1)<br>"
            "<b>Stage 4: K<sub>c</sub></b><br>"
            "&bull; K<sub>c</sub> = [CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>][H<sub>2</sub>O] / ([CH<sub>3</sub>COOH][CH<sub>3</sub>CH<sub>2</sub>OH]) (1)<br>"
            "&bull; = (6.40 &times; 10<sup>&minus;2</sup>)<sup>2</sup> / (1.60 &times; 10<sup>&minus;2</sup> &times; 5.60 &times; 10<sup>&minus;2</sup>) = 4.5714 = 4.57 (1)"
        ),
        "ms_extra": "Extended response. Answer must be given to 3 significant figures.", "ms_marks": "6",
    },
    {
        "qnum": "02.2", "specRef": "RP", "marks": 1,
        "stem": "Complete Table 2 with the titres.",
        "figures": ["fig-q2-table2.jpg"], "crop_exclude_y": [[78, 275]],
        "ms_label": "02.2",
        "ms_ans": "Rough: 4.50; 1: 4.00; 2: 4.20; 3: 3.95 (cm<sup>3</sup>)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "02.3", "specRef": "RP", "marks": 2,
        "stem": "Calculate the mean titre and justify your choice of titres from Table 2.",
        "figures": ["fig-q2-table2.jpg"],
        "ms_label": "02.3",
        "ms_ans": (
            "&bull; Mean = (4.00 + 3.95) / 2 = 3.98 (cm<sup>3</sup>) (allow 3.975) (1)<br>"
            "&bull; Titres 1 and 3 are concordant (allow titre 2 is not concordant) (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "02.4", "specRef": "3.1.12", "marks": 1,
        "stem": "Select from Table 3 a suitable indicator for the titration of ethanoic acid with sodium hydroxide.",
        "ms_label": "02.4",
        "ms_ans": "Thymol blue",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "02.5", "specRef": "RP", "marks": 1,
        "stem": "The uncertainty in the mean titre is +/- 0.15 cm3. Calculate the percentage uncertainty in this mean titre.",
        "figures": ["fig-q2-table2.jpg"],
        "ms_label": "02.5",
        "ms_ans": "0.15 / 3.98 &times; 100 = 3.77%",
        "ms_extra": "Allow consequential marking on mean titre from 2.3.", "ms_marks": "1",
    },
    {
        "qnum": "02.6", "specRef": "RP", "marks": 2,
        "stem": "Suggest how, using the same mass of ethanoic acid, the experiment could be improved to reduce the percentage uncertainty.",
        "figures": ["fig-q2-table2.jpg"],
        "ms_label": "02.6",
        "ms_ans": (
            "&bull; Use a lower concentration of NaOH (1)<br>"
            "&bull; So that a larger titre is required (reduces percentage uncertainty in titre) (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "03.1", "specRef": "RP", "marks": 4,
        "stem": "For each of the bold parts of the TLC practical procedure, consider whether it is essential and justify your answer.",
        "ms_label": "03.1",
        "ms_ans": (
            "&bull; <b>Wear plastic gloves:</b> Essential &minus; to prevent contamination from the hands to the plate (1)<br>"
            "&bull; <b>Developing solvent depth &le; 1 cm:</b> Essential &minus; if too deep it will dissolve the mixture from the plate (1)<br>"
            "&bull; <b>Solvent rise to the top:</b> Not essential &minus; the R<sub>f</sub> value can be calculated if the solvent front does not reach the top (1)<br>"
            "&bull; <b>Dry in a fume cupboard:</b> Essential &minus; the solvent is toxic / hazardous (1)"
        ),
        "ms_extra": "", "ms_marks": "4",
    },
    {
        "qnum": "03.2", "specRef": "3.3.16", "marks": 4,
        "stem": "Outline the steps needed to locate the positions of the amino acids on the TLC plate and to determine their Rf values.",
        "figures": ["fig-q3-stem.jpg"],
        "ms_label": "03.2",
        "ms_ans": (
            "&bull; Spray with developing agent (ninhydrin) or use UV (1)<br>"
            "&bull; Measure distances from initial pencil line to the spots (x) (1)<br>"
            "&bull; Measure distance from initial pencil line to solvent front line (y) (1)<br>"
            "&bull; R<sub>f</sub> value = x / y (1)"
        ),
        "ms_extra": "", "ms_marks": "4",
    },
    {
        "qnum": "03.3", "specRef": "3.3.16", "marks": 2,
        "stem": "Explain why different amino acids have different Rf values.",
        "figures": ["fig-q3-stem.jpg"],
        "ms_label": "03.3",
        "ms_ans": (
            "&bull; Amino acids have different polarities (1)<br>"
            "&bull; Therefore, have different retention on the stationary phase or different solubility in the developing solvent (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "04.1", "specRef": "3.1.12", "marks": 6,
        "stem": "Use the concept of electronegativity to justify why the acid strengths of ethanedioic acid and ethanoic acid are different.",
        "ms_label": "04.1",
        "ms_ans": (
            "<b>Indicative chemistry content:</b><br>"
            "<b>Stage 1: structure difference</b><br>"
            "&bull; Acids are RCOOH: in ethanoic acid R = CH<sub>3</sub>; in ethanedioic acid R = COOH<br>"
            "<b>Stage 2: inductive effect</b><br>"
            "&bull; Unionised COOH group contains two very electronegative oxygen atoms &rarr; negative inductive (electron-withdrawing) effect<br>"
            "&bull; CH<sub>3</sub> group has a positive inductive (electron-pushing) effect<br>"
            "<b>Stage 3: effect on O&minus;H polarity &amp; strength</b><br>"
            "&bull; O&minus;H bond in ethanedioic acid is more polarised / H becomes more &delta;+<br>"
            "&bull; More dissociation into H<sup>+</sup> ions &rarr; ethanedioic acid is stronger than ethanoic acid"
        ),
        "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).", "ms_marks": "6",
    },
    {
        "qnum": "04.2", "specRef": "3.1.12", "marks": 5,
        "stem": "A buffer is made by adding 6.00 x 10^-2 mol NaOH to 1.00 x 10^-1 mol ethanedioic acid (Ka = 5.89 x 10^-2 mol dm-3). Calculate the pH.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.2",
        "ms_ans": (
            "&bull; Moles NaOH = moles HOOCCOO<sup>&minus;</sup> formed = 6.00 &times; 10<sup>&minus;2</sup> (1)<br>"
            "&bull; Moles HOOCCOOH remaining = 1.00 &times; 10<sup>&minus;1</sup> &minus; 6.00 &times; 10<sup>&minus;2</sup> = 4.00 &times; 10<sup>&minus;2</sup> (1)<br>"
            "&bull; K<sub>a</sub> = [H<sup>+</sup>][A<sup>&minus;</sup>] / [HA] &rarr; [H<sup>+</sup>] = K<sub>a</sub> &times; [HA] / [A<sup>&minus;</sup>] (1)<br>"
            "&bull; [H<sup>+</sup>] = 5.89 &times; 10<sup>&minus;2</sup> &times; (4.00 &times; 10<sup>&minus;2</sup> / V) / (6.00 &times; 10<sup>&minus;2</sup> / V) = 3.927 &times; 10<sup>&minus;2</sup> (1)<br>"
            "&bull; pH = &minus;log<sub>10</sub>(3.927 &times; 10<sup>&minus;2</sup>) = 1.406 = 1.41 (1)"
        ),
        "ms_extra": "Extended response. Answer must be given to 2 decimal places (1.41).", "ms_marks": "5",
    },
    {
        "qnum": "04.3", "specRef": "3.2.5", "marks": 4,
        "stem": "25.0 cm3 of acidified ethanedioic acid reacted with 20.20 cm3 of 2.00 x 10^-2 mol dm-3 KMnO4. Deduce the equation and calculate the original concentration of ethanedioic acid.",
        "ms_label": "04.3",
        "ms_ans": (
            "&bull; 5H<sub>2</sub>C<sub>2</sub>O<sub>4</sub> + 6H<sup>+</sup> + 2MnO<sub>4</sub><sup>&minus;</sup> &rarr; 2Mn<sup>2+</sup> + 10CO<sub>2</sub> + 8H<sub>2</sub>O (OR 5C<sub>2</sub>O<sub>4</sub><sup>2&minus;</sup> + 16H<sup>+</sup> + 2MnO<sub>4</sub><sup>&minus;</sup> &rarr; 2Mn<sup>2+</sup> + 10CO<sub>2</sub> + 8H<sub>2</sub>O) (1)<br>"
            "&bull; Moles KMnO<sub>4</sub> = 20.2 &times; 2.00 &times; 10<sup>&minus;2</sup> / 1000 = 4.04 &times; 10<sup>&minus;4</sup> (1)<br>"
            "&bull; Moles H<sub>2</sub>C<sub>2</sub>O<sub>4</sub> = 5/2 &times; 4.04 &times; 10<sup>&minus;4</sup> = 1.01 &times; 10<sup>&minus;3</sup> (1)<br>"
            "&bull; Concentration = 1.01 &times; 10<sup>&minus;3</sup> &times; 1000 / 25 = 4.04 &times; 10<sup>&minus;2</sup> (mol dm<sup>&minus;3</sup>) (1)"
        ),
        "ms_extra": "", "ms_marks": "4",
    },
    {
        "qnum": "05.1", "specRef": "3.3.9", "marks": 2,
        "stem": "Ethanedioic acid was treated with excess unknown alcohol and strong acid catalyst; TOF MS gave peaks at m/z = 104 and 118. Identify the species responsible.",
        "ms_label": "05.1",
        "ms_ans": (
            "&bull; [CH<sub>3</sub>OCOCOOH]<sup>+</sup> (1)<br>"
            "&bull; [CH<sub>3</sub>OCOCOOCH<sub>3</sub>]<sup>+</sup> (1)"
        ),
        "ms_extra": "Allow names. Do not allow molecular formula.", "ms_marks": "2",
    },
    {
        "qnum": "05.2", "specRef": "3.1.1", "marks": 4,
        "stem": "Outline how the TOF mass spectrometer is able to separate the species at m/z = 104 and 118 to give two peaks.",
        "ms_label": "05.2",
        "ms_ans": (
            "&bull; Positive ions are accelerated by an electric field (1)<br>"
            "&bull; To a constant kinetic energy (1)<br>"
            "&bull; The positive ions with m/z of 104 have the same kinetic energy as those with m/z of 118 and move faster (1)<br>"
            "&bull; Therefore, ions with m/z of 104 arrive at the detector first (1)"
        ),
        "ms_extra": "", "ms_marks": "4",
    },
    {"qnum": "06", "specRef": "3.1.1", "marks": 1, "stem": "Which change requires the largest amount of energy?", "ms_label": "06", "ms_ans": "<b>A</b> (He<sup>+</sup>(g) &rarr; He<sup>2+</sup>(g) + e<sup>&minus;</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "07", "specRef": "3.1.2", "marks": 1, "stem": "A sample of 2.18 g of oxygen gas has a volume of 1870 cm3 at 101 kPa. What is the temperature of the gas?", "ms_label": "07", "ms_ans": "<b>B</b> (334 K)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "08", "specRef": "3.1.2", "marks": 1, "stem": "What is the percentage yield of RCOOH (Mr = 100) when 0.50 g is obtained from 1.0 g of RCOOR' (Mr = 150)?", "ms_label": "08", "ms_ans": "<b>D</b> (75%)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "09", "specRef": "3.1.2", "marks": 1, "stem": "A saturated solution of Mg(OH)2 contains 1.17 x 10^-3 g in 100 cm3. What is [Mg2+(aq)]?", "ms_label": "09", "ms_ans": "<b>D</b> (2.01 &times; 10<sup>&minus;4</sup> mol dm<sup>&minus;3</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "10", "specRef": "3.1.9", "marks": 1, "stem": "For Rate = k[C2H4][H2], if the mixture is compressed to triple the original pressure at fixed T, by what factor does the rate change?", "ms_label": "10", "ms_ans": "<b>B</b> (9)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "11", "specRef": "3.1.10", "marks": 1, "stem": "1 mol NH3 dissociates 50% into 0.5 N2 + 1.5 H2. What is the total number of moles of gas at equilibrium?", "ms_label": "11", "ms_ans": "<b>A</b> (1.5)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "12", "specRef": "3.1.10", "marks": 1, "stem": "Which change would alter the value of Kp for 2SO2(g) + O2(g) <=> 2SO3(g)?", "ms_label": "12", "ms_ans": "<b>D</b> (Increasing the temperature)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "13", "specRef": "3.1.12", "marks": 1, "stem": "What is the pH of a 0.020 mol dm-3 solution of a diprotic acid which is completely dissociated?", "ms_label": "13", "ms_ans": "<b>B</b> (1.40)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "14", "specRef": "3.1.12", "marks": 1, "stem": "Ka of HA is 2.56 x 10^-4 mol dm-3. What is the pH of a 4.25 x 10^-3 mol dm-3 solution of HA?", "ms_label": "14", "ms_ans": "<b>C</b> (2.98)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "15", "specRef": "3.1.2", "marks": 1, "stem": "Which uses correct standard form and significant figures for the minimum volume of 2.56 mol dm-3 HCl to form 5.46 g MgCl2?", "ms_label": "15", "ms_ans": "<b>B</b> (4.48 &times; 10<sup>&minus;2</sup> dm<sup>3</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "16", "specRef": "3.1.7", "marks": 1, "stem": "In which reaction is hydrogen acting as an oxidising agent?", "ms_label": "16", "ms_ans": "<b>D</b> (2Na + H<sub>2</sub> &rarr; 2NaH)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "17", "specRef": "3.1.7", "marks": 1, "stem": "In which reaction is the metal oxidised?", "ms_label": "17", "ms_ans": "<b>D</b> (Mg + S &rarr; MgS)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "18", "specRef": "3.1.11", "marks": 1, "stem": "Which statement is correct about the operation of the cell Cu | Cu2+ || Ag+ | Ag (EMF = +0.46 V)?", "ms_label": "18", "ms_ans": "<b>A</b> (Metallic copper is oxidised by Ag<sup>+</sup> ions)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "19", "specRef": "3.2.2", "marks": 1, "stem": "0.102 g of Group 2 metal X reacts with excess HCl to give 65 cm3 H2 at 99 kPa and 303 K. Which is X?", "ms_label": "19", "ms_ans": "<b>B</b> (Calcium)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "20", "specRef": "3.2.6", "marks": 1, "stem": "What forms when sodium carbonate solution is added to gallium(III) nitrate solution?", "ms_label": "20", "ms_ans": "<b>D</b> (A white precipitate of gallium(III) hydroxide and bubbles of carbon dioxide)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "21", "specRef": "3.2.3", "marks": 1, "stem": "Which compound gives a colourless solution when an excess of dilute aqueous ammonia is added?", "ms_label": "21", "ms_ans": "<b>B</b> (AgCl)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "22", "specRef": "3.2.6", "marks": 1, "stem": "What is the final species produced when an excess of aqueous ammonia is added to aqueous aluminium chloride?", "ms_label": "22", "ms_ans": "<b>B</b> ([Al(OH)<sub>3</sub>(H<sub>2</sub>O)<sub>3</sub>])", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "23", "specRef": "3.2.5", "marks": 1, "stem": "What volume of 0.020 mol dm-3 KMnO4 is required to oxidise 0.010 mol of V4+ ions?", "ms_label": "23", "ms_ans": "<b>D</b> (100 cm<sup>3</sup>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "24", "specRef": "3.3.1", "marks": 1, "stem": "How many isomers have the molecular formula C5H12?", "ms_label": "24", "ms_ans": "<b>B</b> (3)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "25", "specRef": "3.3.2", "marks": 1, "stem": "Which molecule is not produced when ethane reacts with bromine in the presence of UV light?", "ms_label": "25", "ms_ans": "<b>C</b> (H<sub>2</sub>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "26", "specRef": "3.3.1", "marks": 1, "stem": "How many structural isomers have the molecular formula C4H9Br?", "ms_label": "26", "ms_ans": "<b>C</b> (4)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "27", "specRef": "3.3.4", "marks": 1, "stem": "What is the major product of the reaction between but-1-ene and DBr?", "ms_label": "27", "ms_ans": "<b>C</b> (CH<sub>3</sub>CH<sub>2</sub>CHBrCH<sub>2</sub>D)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "28", "specRef": "3.3.3", "marks": 1, "stem": "Why are fluoroalkanes unreactive?", "ms_label": "28", "ms_ans": "<b>D</b> (The C&minus;F bond is very strong)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "29", "specRef": "3.3.8", "marks": 1, "stem": "Which alcohol could not be produced by the reduction of an aldehyde or a ketone?", "ms_label": "29", "ms_ans": "<b>B</b> (2-methylbutan-2-ol)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "30", "specRef": "3.3.7", "marks": 1, "stem": "Which compound forms optically active compounds on reduction?", "ms_label": "30", "ms_ans": "<b>D</b> (CH<sub>3</sub>CH<sub>2</sub>COCH<sub>3</sub>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "31", "specRef": "3.3.11", "marks": 1, "stem": "How many secondary amines have the molecular formula C4H11N?", "ms_label": "31", "ms_ans": "<b>B</b> (3)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "32", "specRef": "3.1.3", "marks": 1, "stem": "Which compound has the highest boiling point?", "ms_label": "32", "ms_ans": "<b>C</b> (CH<sub>3</sub>NH<sub>2</sub>)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "33", "specRef": "3.3.12", "marks": 1, "stem": "Which compound can polymerise by reaction with itself?", "ms_label": "33", "ms_ans": "<b>D</b> (NH<sub>2</sub>CH<sub>2</sub>COCl)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "34", "specRef": "3.3.7", "marks": 1, "stem": "Which molecule requires the design of an optically active drug?", "ms_label": "34", "ms_ans": "<b>C</b> (CH<sub>3</sub>&minus;CH(OH)&minus;COOH)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "35", "specRef": "3.3.15", "marks": 1, "stem": "Which amine has only three peaks in its proton NMR spectrum?", "ms_label": "35", "ms_ans": "<b>C</b> (Diethylamine)", "ms_extra": "", "ms_marks": "1"},
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

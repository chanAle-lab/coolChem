"""Ingest AQA AS Chemistry Specimen Paper 1 (7404/1) into data/questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517590643_dc8971d3.pdf"
)

PAPER_ID = "2015-specimen-7404-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2015,
    "series": "Specimen",
    "unit": "7404/1",
    "level": "AS",
    "date": "2015-01-01",
    "title": "7404/1 — AS Paper 1: Inorganic and Physical Chemistry (Specimen)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {
        "filename": "fig-q4-stem.jpg",
        "page": 8,
        "x0": 40,
        "y0": 64,
        "x1": 560,
        "y1": 218,
    },
]

QUESTIONS = [
    {
        "qnum": "01.1",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "Use the Periodic Table to deduce the full electron configuration of calcium.",
        "ms_label": "01.1",
        "ms_ans": "1s<sup>2</sup>2s<sup>2</sup>2p<sup>6</sup>3s<sup>2</sup>3p<sup>6</sup>4s<sup>2</sup>",
        "ms_extra": "Allow correct numbers that are not superscripted.",
        "ms_marks": "1",
    },
    {
        "qnum": "01.2",
        "specRef": "3.2.2",
        "marks": 1,
        "stem": "Write an ionic equation, with state symbols, to show the reaction of calcium with an excess of water.",
        "ms_label": "01.2",
        "ms_ans": "Ca(s) + 2H<sub>2</sub>O(l) &rarr; Ca<sup>2+</sup>(aq) + 2OH<sup>&minus;</sup>(aq) + H<sub>2</sub>(g)",
        "ms_extra": "State symbols essential.",
        "ms_marks": "1",
    },
    {
        "qnum": "01.3",
        "specRef": "3.1.7",
        "marks": 1,
        "stem": "State the role of water in the reaction with calcium.",
        "ms_label": "01.3",
        "ms_ans": "Oxidising agent",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "01.4",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "Write an equation, including state symbols, to represent the process that occurs when the first ionisation energy of calcium is measured.",
        "ms_label": "01.4",
        "ms_ans": "Ca(g) &rarr; Ca<sup>+</sup>(g) + e<sup>&minus;</sup>",
        "ms_extra": "State symbols essential. Allow 'e' without the negative sign.",
        "ms_marks": "1",
    },
    {
        "qnum": "01.5",
        "specRef": "3.2.1",
        "marks": 3,
        "stem": "State and explain the trend in the first ionisation energies of the elements in Group 2 from magnesium to barium.",
        "ms_label": "01.5",
        "ms_ans": (
            "&bull; Decrease (1)<br>"
            "&bull; Ions get bigger / more (energy) shells (1)<br>"
            "&bull; Weaker attraction of ion to lost electron (1)"
        ),
        "ms_extra": "If answer to 'trend' is not 'decrease', then chemical error = 0/3. Allow atoms instead of ions.",
        "ms_marks": "3",
    },
    {
        "qnum": "02.1",
        "specRef": "3.1.1",
        "marks": 4,
        "stem": "A sample of sulfur consisting of three isotopes has a relative atomic mass of 32.16. Use Table 1 to determine the relative abundance and mass number of the third isotope.",
        "ms_label": "02.1",
        "ms_ans": (
            "&bull; Abundance of third isotope = 100 &minus; 91.0 &minus; 1.8 = 7.2% (1)<br>"
            "&bull; [(32 &times; 91) + (33 &times; 1.8) + (y &times; 7.2)] / 100 = 32.16 (1)<br>"
            "&bull; 7.2y = 3216 &minus; 2912 &minus; 59.4 = 244.6 &rarr; y = 244.6 / 7.2 = 33.97 (1)<br>"
            "&bull; y = 34 (1)"
        ),
        "ms_extra": "Answer must be rounded to the nearest integer.",
        "ms_marks": "4",
    },
    {
        "qnum": "02.2",
        "specRef": "3.1.1",
        "marks": 2,
        "stem": "Describe how ions are formed in a time of flight (TOF) mass spectrometer.",
        "ms_label": "02.2",
        "ms_ans": (
            "<i>(for electrospray ionisation)</i><br>"
            "&bull; A high voltage is applied to a sample in a polar solvent (1)<br>"
            "&bull; The sample molecule, M, gains a proton forming MH<sup>+</sup> (1)<br>"
            "<b>OR</b><br>"
            "<i>(for electron impact ionisation)</i><br>"
            "&bull; The sample is bombarded by high energy electrons (1)<br>"
            "&bull; The sample molecule loses an electron forming M<sup>+</sup> (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "02.3",
        "specRef": "3.1.1",
        "marks": 2,
        "stem": "Explain why it is necessary to ionise molecules when measuring their mass in a TOF mass spectrometer.",
        "ms_label": "02.3",
        "ms_ans": (
            "&bull; Ions, not molecules, will interact with and be accelerated by an electric field (1)<br>"
            "&bull; Only ions will create a current when hitting the detector (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "03.1",
        "specRef": "3.1.4",
        "marks": 1,
        "stem": "Write an equation, including state symbols, for the reaction with enthalpy change equal to the standard enthalpy of formation for CF4(g).",
        "ms_label": "03.1",
        "ms_ans": "C(s) + 2F<sub>2</sub>(g) &rarr; CF<sub>4</sub>(g)",
        "ms_extra": "State symbols essential.",
        "ms_marks": "1",
    },
    {
        "qnum": "03.2",
        "specRef": "3.1.3",
        "marks": 2,
        "stem": "Explain why CF4 has a bond angle of 109.5 degrees.",
        "ms_label": "03.2",
        "ms_ans": (
            "&bull; Around carbon there are 4 bonding pairs of electrons (and no lone pairs) (1)<br>"
            "&bull; Therefore, these repel equally and spread as far apart as possible (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "03.3",
        "specRef": "3.1.4",
        "marks": 3,
        "stem": "Use Table 2 and the enthalpy change (-2889 kJ mol-1) for C2H6(g) + 7F2(g) -> 2CF4(g) + 6HF(g) to calculate the standard enthalpy of formation of C2H6(g).",
        "ms_label": "03.3",
        "ms_ans": (
            "&bull; &Delta;H = &Sigma;&Delta;<sub>f</sub>H products &minus; &Sigma;&Delta;<sub>f</sub>H reactants or a correct cycle (1)<br>"
            "&bull; Hence (2 &times; &minus;680) + (6 &times; &minus;269) &minus; (x) = &minus;2889 (1)<br>"
            "&bull; x = 2889 &minus; 1360 &minus; 1614 = &minus;85 (kJ mol<sup>&minus;1</sup>) (1)"
        ),
        "ms_extra": "Score 1 mark only for +85 (kJ mol<sup>&minus;1</sup>).",
        "ms_marks": "3",
    },
    {
        "qnum": "03.4",
        "specRef": "3.1.4",
        "marks": 4,
        "stem": "Use Table 3 and CH4(g) + 4F2(g) -> CF4(g) + 4HF(g) (delta H = -1904 kJ mol-1) to calculate the F-F bond enthalpy and evaluate the student's suggestion about the reactivity of fluorine.",
        "ms_label": "03.4",
        "ms_ans": (
            "&bull; Bonds broken = 4(C&minus;H) + 4(F&minus;F) = 4 &times; 412 + 4 &times; (F&minus;F); Bonds formed = 4(C&minus;F) + 4(H&minus;F) = 4 &times; 484 + 4 &times; 562 (1)<br>"
            "&bull; &minus;1904 = [4 &times; 412 + 4(F&minus;F)] &minus; [4 &times; 484 + 4 &times; 562] &rarr; 4(F&minus;F) = 632 (1)<br>"
            "&bull; F&minus;F = 632 / 4 = 158 (kJ mol<sup>&minus;1</sup>) (1)<br>"
            "&bull; The student is correct because the F&minus;F bond energy is much less than the C&minus;H or other covalent bonds, therefore the F&minus;F bond is weak / easily broken (1)"
        ),
        "ms_extra": "Both bonds broken and bonds formed required for M1. Relevant comment comparing to other bonds (low activation energy needed to break the F&minus;F bond).",
        "ms_marks": "4",
    },
    {
        "qnum": "04.1",
        "specRef": "3.1.6",
        "marks": 2,
        "stem": "At equilibrium, the mixture contained 0.20 mol of Z(aq). Calculate the amount, in moles, of X(aq) and Y(aq) in this equilibrium mixture.",
        "ms_label": "04.1",
        "ms_ans": (
            "&bull; Amount of X = 0.50 &minus; 0.20 = 0.30 (mol) (1)<br>"
            "&bull; Amount of Y = 0.50 &minus; 2 &times; 0.20 = 0.10 (mol) (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "04.2",
        "specRef": "3.1.6",
        "marks": 3,
        "stem": "On the grid below, draw a graph to show how the amount of Z(aq) changed from the time of initial mixing until 60 seconds had elapsed.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.2",
        "ms_ans": (
            "&bull; Axes labelled with values, units and scales that use over half of each axis (1)<br>"
            "&bull; Curve starts at origin (1)<br>"
            "&bull; Then flattens at 30 seconds at 0.20 mol (1)"
        ),
        "ms_extra": "All three of values, units and scales are required for M1.",
        "ms_marks": "3",
    },
    {
        "qnum": "04.3",
        "specRef": "3.1.6",
        "marks": 3,
        "stem": "At a different temperature, Kc = 2.9 mol-2 dm6, [X] = 0.40 mol dm-3 and [Z] = 0.35 mol dm-3. Calculate [Y] to the appropriate number of significant figures.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.3",
        "ms_ans": (
            "&bull; Expression: K<sub>c</sub> = [Z] / ([X][Y]<sup>2</sup>) (1)<br>"
            "&bull; [Y]<sup>2</sup> = [Z] / ([X] K<sub>c</sub>) (1)<br>"
            "&bull; [Y] = (0.35 / (0.40 &times; 2.9))<sup>0.5</sup> = 0.5493 = 0.55 (mol dm<sup>&minus;3</sup>) (1)"
        ),
        "ms_extra": "Answer must be to 2 significant figures.",
        "ms_marks": "3",
    },
    {
        "qnum": "04.4",
        "specRef": "3.1.6",
        "marks": 3,
        "stem": "A small amount of more Y(aq) was added to the equilibrium mixture in 04.3. Predict and explain any colour change.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.4",
        "ms_ans": (
            "&bull; Darkened / went more orange (1)<br>"
            "&bull; The equilibrium moved to the right (1)<br>"
            "&bull; To oppose the increased concentration of Y (1)"
        ),
        "ms_extra": "",
        "ms_marks": "3",
    },
    {
        "qnum": "04.5",
        "specRef": "3.1.6",
        "marks": 1,
        "stem": "The student warmed the equilibrium mixture from Question 4.3. Predict the colour change, if any, when the equilibrium mixture was warmed.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.5",
        "ms_ans": "The orange colour would fade",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "05.1",
        "specRef": "3.2.3",
        "marks": 3,
        "stem": "Write an equation for the reaction of sodium bromide with concentrated sulfuric acid and explain why bromide ions react differently from chloride ions.",
        "ms_label": "05.1",
        "ms_ans": (
            "&bull; 2NaBr + 2H<sub>2</sub>SO<sub>4</sub> &rarr; Na<sub>2</sub>SO<sub>4</sub> + Br<sub>2</sub> + SO<sub>2</sub> + 2H<sub>2</sub>O (1)<br>"
            "&bull; Br<sup>&minus;</sup> ions are bigger than Cl<sup>&minus;</sup> ions (1)<br>"
            "&bull; Therefore Br<sup>&minus;</sup> ions are more easily oxidised / lose an electron more easily (than Cl<sup>&minus;</sup> ions) (1)"
        ),
        "ms_extra": "Allow ionic equation: 2Br<sup>&minus;</sup> + 2H<sub>2</sub>SO<sub>4</sub> &rarr; Br<sub>2</sub> + SO<sub>4</sub><sup>2&minus;</sup> + SO<sub>2</sub> + 2H<sub>2</sub>O.",
        "ms_marks": "3",
    },
    {
        "qnum": "05.2",
        "specRef": "3.2.3",
        "marks": 6,
        "stem": "Develop a procedure to prepare a pure sample of silver bromide from a mixture of sodium chloride and sodium bromide using aqueous silver nitrate and other reagents, explaining each step with equations.",
        "ms_label": "05.2",
        "ms_ans": (
            "<b>Indicative chemistry content:</b><br>"
            "<b>Stage 1: formation of precipitates</b><br>"
            "&bull; Add silver nitrate to form precipitates of AgCl and AgBr<br>"
            "&bull; AgNO<sub>3</sub> + NaCl &rarr; AgCl + NaNO<sub>3</sub> and AgNO<sub>3</sub> + NaBr &rarr; AgBr + NaNO<sub>3</sub><br>"
            "<b>Stage 2: selective dissolving of AgCl</b><br>"
            "&bull; Add excess of dilute ammonia to the mixture of precipitates<br>"
            "&bull; The silver chloride precipitate dissolves: AgCl + 2NH<sub>3</sub> &rarr; Ag(NH<sub>3</sub>)<sub>2</sub><sup>+</sup> + Cl<sup>&minus;</sup><br>"
            "<b>Stage 3: separation and purification of AgBr</b><br>"
            "&bull; Filter off the remaining silver bromide precipitate<br>"
            "&bull; Wash to remove soluble compounds and dry to remove water"
        ),
        "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).",
        "ms_marks": "6",
    },
    {
        "qnum": "05.3",
        "specRef": "3.2.3",
        "marks": 2,
        "stem": "Write an ionic equation for the reaction between chlorine and cold dilute sodium hydroxide solution, and give the oxidation state of chlorine in each chlorine-containing ion formed.",
        "ms_label": "05.3",
        "ms_ans": (
            "&bull; Cl<sub>2</sub> + 2OH<sup>&minus;</sup> &rarr; OCl<sup>&minus;</sup> + Cl<sup>&minus;</sup> + H<sub>2</sub>O (1)<br>"
            "&bull; OCl<sup>&minus;</sup> is +1 AND Cl<sup>&minus;</sup> is &minus;1 (1)"
        ),
        "ms_extra": "Both oxidation states required for M2.",
        "ms_marks": "2",
    },
    {
        "qnum": "06.1",
        "specRef": "RP",
        "marks": 8,
        "stem": "Outline how to conduct a back titration experiment with 50.0 cm3 of 0.200 mol dm-3 HCl and standard NaOH to determine accurately the relative formula mass of solid calcium hydroxide.",
        "ms_label": "06.1",
        "ms_ans": (
            "<b>Stage 1: excess acid &amp; mass of solid</b><br>"
            "&bull; Statement that there must be an excess of acid (1)<br>"
            "&bull; Moles of acid = 50.0 &times; 0.200 / 1000 = 1.00 &times; 10<sup>&minus;2</sup> mol (1)<br>"
            "&bull; 2 mol acid react with 1 mol Ca(OH)<sub>2</sub>, so moles solid weighed &lt; 5.00 &times; 10<sup>&minus;3</sup> mol (1)<br>"
            "&bull; Mass of solid must be &lt; 5.00 &times; 10<sup>&minus;3</sup> &times; 74.1 = &lt; 0.371 g (1)<br>"
            "<b>Stage 2: experimental method</b><br>"
            "&bull; Measure out 50 cm<sup>3</sup> of acid using a pipette and add the weighed amount of solid in a conical flask (1)<br>"
            "&bull; Titrate against 0.100 (or 0.200) mol dm<sup>&minus;3</sup> NaOH added from a burette and record the volume (v) when an added indicator changes colour (1)<br>"
            "<b>Stage 3: calculation of M<sub>r</sub></b><br>"
            "&bull; Moles of Ca(OH)<sub>2</sub> = 5.00 &times; 10<sup>&minus;3</sup> &minus; (v/2 &times; conc NaOH) / 1000 = z mol (1)<br>"
            "&bull; M<sub>r</sub> = mass of solid / z (1)"
        ),
        "ms_extra": "Extended response: max 7 marks if no sustained, coherent, logically structured line of reasoning.",
        "ms_marks": "8",
    },
    {
        "qnum": "06.2",
        "specRef": "3.1.2",
        "marks": 3,
        "stem": "A 3.56 g sample of CaCl2 reacted with excess H2SO4 with an 83.4% yield of CaSO4. Calculate the mass of CaSO4 formed.",
        "ms_label": "06.2",
        "ms_ans": (
            "&bull; Moles of calcium chloride = 3.56 / 111.1 = 3.204 &times; 10<sup>&minus;2</sup> (1)<br>"
            "&bull; Moles of calcium sulfate = 3.204 &times; 10<sup>&minus;2</sup> &times; 83.4 / 100 = 2.672 &times; 10<sup>&minus;2</sup> (1)<br>"
            "&bull; Mass of calcium sulfate = 2.672 &times; 10<sup>&minus;2</sup> &times; 136.2 = 3.6398 = 3.64 (g) (1)"
        ),
        "ms_extra": "Answer must be to 3 significant figures.",
        "ms_marks": "3",
    },
    {
        "qnum": "07.1",
        "specRef": "3.1.2",
        "marks": 5,
        "stem": "A 3.74 x 10^-2 g sample of Mg(NO3)2 was completely decomposed by heating. Calculate the total volume, in cm3, of gas produced at 60.0 C and 100 kPa.",
        "ms_label": "07.1",
        "ms_ans": (
            "<b>Stage 1:</b><br>"
            "&bull; M<sub>r</sub> for Mg(NO<sub>3</sub>)<sub>2</sub> = 148.3 (1)<br>"
            "&bull; Moles of Mg(NO<sub>3</sub>)<sub>2</sub> = 3.74 &times; 10<sup>&minus;2</sup> / 148.3 = 2.522 &times; 10<sup>&minus;4</sup> mol<br>"
            "<b>Stage 2:</b><br>"
            "&bull; Total moles of gas produced = 5/2 &times; moles of Mg(NO<sub>3</sub>)<sub>2</sub> = 6.305 &times; 10<sup>&minus;4</sup> (1)<br>"
            "<b>Stage 3:</b><br>"
            "&bull; pV = nRT so V = nRT / p (1)<br>"
            "&bull; V = (6.305 &times; 10<sup>&minus;4</sup> &times; 8.31 &times; 333) / (1.00 &times; 10<sup>5</sup>) = 1.745 &times; 10<sup>&minus;5</sup> m<sup>3</sup> (1)<br>"
            "&bull; V = 1.745 &times; 10<sup>&minus;5</sup> &times; 1 &times; 10<sup>6</sup> = 17.45 cm<sup>3</sup> = 17.5 (cm<sup>3</sup>) (1)"
        ),
        "ms_extra": "Extended response calculation. Answer must be to 3 sig figs (17.4 cm<sup>3</sup> also accepted depending on intermediate rounding).",
        "ms_marks": "5",
    },
    {
        "qnum": "07.2",
        "specRef": "RP",
        "marks": 1,
        "stem": "The mass of MgO obtained in this experiment is slightly less than expected. Suggest one practical reason for this.",
        "ms_label": "07.2",
        "ms_ans": "Some of the solid is lost in weighing product / solid is blown away with the gas",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "08",
        "specRef": "3.2.1",
        "marks": 1,
        "stem": "Which of these atoms has the largest atomic radius?",
        "ms_label": "08",
        "ms_ans": "<b>D</b> (Na)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "09",
        "specRef": "3.2.3",
        "marks": 1,
        "stem": "Which of these species is the best reducing agent?",
        "ms_label": "09",
        "ms_ans": "<b>D</b> (I<sup>&minus;</sup>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "10",
        "specRef": "RP",
        "marks": 1,
        "stem": "Which of these pieces of apparatus has the lowest percentage uncertainty in the measurement shown?",
        "ms_label": "10",
        "ms_ans": "<b>A</b> (Volume of 25 cm<sup>3</sup> measured with a burette with an uncertainty of &plusmn;0.1 cm<sup>3</sup>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "11",
        "specRef": "RP",
        "marks": 1,
        "stem": "Which of these is the correct volume of water that should be added to dilute 5.00 cm3 of 1.00 x 10^-2 mol dm-3 HCl to 5.00 x 10^-4 mol dm-3?",
        "ms_label": "11",
        "ms_ans": "<b>B</b> (95.0 cm<sup>3</sup>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "12",
        "specRef": "3.1.3",
        "marks": 1,
        "stem": "Which of these species has a trigonal planar structure?",
        "ms_label": "12",
        "ms_ans": "<b>B</b> (BCl<sub>3</sub>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "13",
        "specRef": "3.1.3",
        "marks": 1,
        "stem": "Which of these compounds has the highest boiling point?",
        "ms_label": "13",
        "ms_ans": "<b>A</b> (HF)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "14",
        "specRef": "3.1.3",
        "marks": 1,
        "stem": "Which type of bond is formed between N and B when a molecule of NH3 reacts with a molecule of BF3?",
        "ms_label": "14",
        "ms_ans": "<b>C</b> (Co-ordinate)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "15",
        "specRef": "3.1.3",
        "marks": 1,
        "stem": "Which of these atoms has the highest electronegativity?",
        "ms_label": "15",
        "ms_ans": "<b>C</b> (Cl)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "16",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "Which of these atoms has the smallest number of neutrons?",
        "ms_label": "16",
        "ms_ans": "<b>D</b> (<sup>4</sup>Li)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "17",
        "specRef": "3.1.3",
        "marks": 1,
        "stem": "Which of these substances does not show hydrogen bonding?",
        "ms_label": "17",
        "ms_ans": "<b>D</b> (CHF<sub>3</sub>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "18",
        "specRef": "3.1.2",
        "marks": 1,
        "stem": "What is the formula of calcium nitrate(V)?",
        "ms_label": "18",
        "ms_ans": "<b>B</b> (Ca(NO<sub>3</sub>)<sub>2</sub>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "19",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "Which of these elements has the highest second ionisation energy?",
        "ms_label": "19",
        "ms_ans": "<b>A</b> (Na)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "20",
        "specRef": "3.1.7",
        "marks": 1,
        "stem": "Which of the following shows chlorine in its correct oxidation states in HCl, KClO3, HClO?",
        "ms_label": "20",
        "ms_ans": "<b>C</b> (&minus;1, +5, +1)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "21",
        "specRef": "3.2.3",
        "marks": 1,
        "stem": "Which substance is not produced in a redox reaction when solid sodium iodide reacts with concentrated sulfuric acid?",
        "ms_label": "21",
        "ms_ans": "<b>B</b> (HI)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "22",
        "specRef": "3.1.2",
        "marks": 1,
        "stem": "Which of the following contains the most chloride ions?",
        "ms_label": "22",
        "ms_ans": "<b>B</b> (20 cm<sup>3</sup> of 5.00 &times; 10<sup>&minus;2</sup> mol dm<sup>&minus;3</sup> calcium chloride solution)",
        "ms_extra": "",
        "ms_marks": "1",
    },
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


PAGE_MAP = {
    "01.1": 3, "01.2": 3, "01.3": 3, "01.4": 3, "01.5": 3,
    "02.1": 4, "02.2": 4, "02.3": 5,
    "03.1": 6, "03.2": 6, "03.3": 6, "03.4": 7,
    "04.1": 8, "04.2": 8, "04.3": 9, "04.4": 9, "04.5": 9,
    "05.1": 10, "05.2": 10, "05.3": 11,
    "06.1": 12, "06.2": 13,
    "07.1": 14, "07.2": 14,
    "08": 15, "09": 15,
    "10": 16, "11": 16, "12": 16,
    "13": 17, "14": 17, "15": 17, "16": 17,
    "17": 18, "18": 18, "19": 18,
    "20": 19, "21": 19, "22": 19,
}

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

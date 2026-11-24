"""Ingest AQA A-level Chemistry Specimen Paper 1 (7405/1) into data/questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517590569_ce237c94.pdf"
)

PAPER_ID = "2015-specimen-7405-1"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2015,
    "series": "Specimen",
    "unit": "7405/1",
    "level": "A-level",
    "date": "2015-01-01",
    "title": "7405/1 — A-level Paper 1: Inorganic and Physical Chemistry (Specimen)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {
        "filename": "fig-q3-table1.jpg",
        "page": 6,
        "x0": 18,
        "y0": 65,
        "x1": 565,
        "y1": 415,
    },
    {
        "filename": "fig-q4-table2.jpg",
        "page": 8,
        "x0": 40,
        "y0": 78,
        "x1": 565,
        "y1": 298,
    },
    {
        "filename": "fig-q5-table3.jpg",
        "page": 12,
        "x0": 40,
        "y0": 78,
        "x1": 565,
        "y1": 260,
    },
    {
        "filename": "fig-q6-fig1.jpg",
        "page": 14,
        "x0": 40,
        "y0": 78,
        "x1": 565,
        "y1": 490,
    },
    {
        "filename": "fig-q7-table4.jpg",
        "page": 18,
        "x0": 40,
        "y0": 65,
        "x1": 565,
        "y1": 265,
    },
    {
        "filename": "fig-q10-table5.jpg",
        "page": 26,
        "x0": 40,
        "y0": 78,
        "x1": 565,
        "y1": 356,
    },
]

QUESTIONS = [
    {
        "qnum": "01.1",
        "specRef": "3.1.3",
        "marks": 6,
        "stem": "Explain how the electron pair repulsion theory can be used to deduce the shape of, and the bond angle in, PF3.",
        "ms_label": "01.1",
        "ms_ans": (
            "<b>Indicative chemistry content:</b><br>"
            "<b>Stage 1: Electrons round P</b><br>"
            "&bull; P has 5 electrons in the outside shell<br>"
            "&bull; With 3 electrons from 3 fluorine, there are a total of 8 electrons in outside shell<br>"
            "&bull; So 3 bond pairs, 1 non-bond pair<br>"
            "<b>Stage 2: Electron pair repulsion theory</b><br>"
            "&bull; Electron pairs repel as far as possible<br>"
            "&bull; Lone pair repels more than bonding pairs<br>"
            "<b>Stage 3: Conclusions</b><br>"
            "&bull; Therefore, tetrahedral / trigonal pyramidal shape<br>"
            "&bull; With angle of 109(.5)&deg; decreased to 107&deg;"
        ),
        "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).",
        "ms_marks": "6",
    },
    {
        "qnum": "01.2",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "State the full electron configuration of a cobalt(II) ion.",
        "ms_label": "01.2",
        "ms_ans": "1s<sup>2</sup>2s<sup>2</sup>2p<sup>6</sup>3s<sup>2</sup>3p<sup>6</sup>3d<sup>7</sup>",
        "ms_extra": "Allow correct numbers that are not superscripted.",
        "ms_marks": "1",
    },
    {
        "qnum": "01.3",
        "specRef": "3.2.5",
        "marks": 1,
        "stem": "Suggest one reason why [Co(NH3)6]^2+ cannot exist.",
        "ms_label": "01.3",
        "ms_ans": "Too many electrons in d sub-shell / orbitals",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "01.4",
        "specRef": "3.1.3",
        "marks": 2,
        "stem": "State the shape of, and the bond angle in, [CoCl4]^2-.",
        "ms_label": "01.4",
        "ms_ans": (
            "&bull; Tetrahedral (shape) (1)<br>"
            "&bull; 109.5&deg; (1)"
        ),
        "ms_extra": "Allow 109&deg;.",
        "ms_marks": "2",
    },
    {
        "qnum": "02.1",
        "specRef": "3.2.1",
        "marks": 2,
        "stem": "Explain why the atomic radii of the elements decrease across Period 3 from sodium to chlorine.",
        "ms_label": "02.1",
        "ms_ans": (
            "&bull; The number of protons increases (across the period) / nuclear charge increases (1)<br>"
            "&bull; Therefore, the attraction between the nucleus and electrons increases (1)"
        ),
        "ms_extra": "Can only score M2 if M1 is correct.",
        "ms_marks": "2",
    },
    {
        "qnum": "02.2",
        "specRef": "3.2.1",
        "marks": 2,
        "stem": "Explain why the melting point of sulfur (S8) is greater than that of phosphorus (P4).",
        "ms_label": "02.2",
        "ms_ans": (
            "&bull; S<sub>8</sub> molecules are bigger than P<sub>4</sub> molecules (1)<br>"
            "&bull; Therefore, van der Waals / dispersion / London forces between molecules are stronger in sulfur (1)"
        ),
        "ms_extra": "Allow sulfur molecules have bigger surface area and sulfur molecules have bigger M<sub>r</sub>.",
        "ms_marks": "2",
    },
    {
        "qnum": "02.3",
        "specRef": "3.2.4",
        "marks": 2,
        "stem": "Explain why sodium oxide forms an alkaline solution when it reacts with water.",
        "ms_label": "02.3",
        "ms_ans": (
            "&bull; Sodium oxide contains O<sup>2&minus;</sup> ions (1)<br>"
            "&bull; These O<sup>2&minus;</sup> ions react with water forming OH<sup>&minus;</sup> ions (1)"
        ),
        "ms_extra": "O<sup>2&minus;</sup> + H<sub>2</sub>O &rarr; 2OH<sup>&minus;</sup> scores M1 and M2.",
        "ms_marks": "2",
    },
    {
        "qnum": "02.4",
        "specRef": "3.2.4",
        "marks": 1,
        "stem": "Write an ionic equation for the reaction of phosphorus(V) oxide with an excess of sodium hydroxide solution.",
        "ms_label": "02.4",
        "ms_ans": "P<sub>4</sub>O<sub>10</sub> + 12OH<sup>&minus;</sup> &rarr; 4PO<sub>4</sub><sup>3&minus;</sup> + 6H<sub>2</sub>O",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "03.1",
        "specRef": "3.1.11",
        "marks": 2,
        "stem": "Explain the function of the salt bridge in a cell used to measure electrode potential.",
        "crop_exclude_y": [[65, 415]],
        "ms_label": "03.1",
        "ms_ans": (
            "&bull; The ions in the ionic substance in the salt bridge move through the salt bridge (1)<br>"
            "&bull; To maintain charge balance / complete the circuit (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "03.2",
        "specRef": "3.1.11",
        "marks": 1,
        "stem": "Use data from Table 1 to deduce the halide ion that is the weakest reducing agent.",
        "figures": ["fig-q3-table1.jpg"],
        "ms_label": "03.2",
        "ms_ans": "F<sup>&minus;</sup>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "03.3",
        "specRef": "3.1.11",
        "marks": 1,
        "stem": "Use data from Table 1 to justify why sulfate ions should not be capable of oxidising bromide ions.",
        "figures": ["fig-q3-table1.jpg"],
        "ms_label": "03.3",
        "ms_ans": "<i>E</i><sup>&ominus;</sup> SO<sub>4</sub><sup>2&minus;</sup>/SO<sub>2</sub> &lt; <i>E</i><sup>&ominus;</sup> Br<sub>2</sub>/Br<sup>&minus;</sup>",
        "ms_extra": "Allow correct answer expressed in words, e.g. electrode potential for sulfate ions / sulfur dioxide is less than that for bromine / bromide.",
        "ms_marks": "1",
    },
    {
        "qnum": "03.4",
        "specRef": "3.1.11",
        "marks": 1,
        "stem": "Use data from Table 1 to calculate a value for the EMF of a hydrogen-oxygen fuel cell operating under alkaline conditions.",
        "figures": ["fig-q3-table1.jpg"],
        "ms_label": "03.4",
        "ms_ans": "1.23 (V)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "03.5",
        "specRef": "3.1.11",
        "marks": 1,
        "stem": "Suggest why a hydrogen-oxygen fuel cell is more efficient than an internal combustion engine burning hydrogen.",
        "ms_label": "03.5",
        "ms_ans": "A fuel cell converts more of the available energy from combustion of hydrogen into kinetic energy of the car / an internal combustion engine wastes more (heat) energy",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "04.1",
        "specRef": "3.1.4",
        "marks": 3,
        "stem": "Use the enthalpy change for CO2(g) + 3H2(g) -> CH3OH(g) + H2O(g) (-49 kJ mol-1) and data from Table 2 to calculate a value for the H-H bond enthalpy.",
        "figures": ["fig-q4-table2.jpg"],
        "crop_exclude_y": [[78, 298]],
        "ms_label": "04.1",
        "ms_ans": (
            "&bull; Bonds broken = 2(C=O) + 3(H&minus;H) = 2 &times; 743 + 3 &times; H&minus;H; Bonds formed = 3(C&minus;H) + (C&minus;O) + 3(O&minus;H) = 3 &times; 412 + 360 + 3 &times; 463 (1)<br>"
            "&bull; &minus;49 = [2 &times; 743 + 3(H&minus;H)] &minus; [3 &times; 412 + 360 + 3 &times; 463] &rarr; 3(H&minus;H) = 1450 (1)<br>"
            "&bull; H&minus;H = 483 (kJ mol<sup>&minus;1</sup>) (1)"
        ),
        "ms_extra": "Both bonds broken and bonds formed required for M1. Allow 483.3(3).",
        "ms_marks": "3",
    },
    {
        "qnum": "04.2",
        "specRef": "3.1.4",
        "marks": 1,
        "stem": "Suggest one reason why the data book value for the H-H bond enthalpy (436 kJ mol-1) is different from your answer to Question 4.1.",
        "figures": ["fig-q4-table2.jpg"],
        "ms_label": "04.2",
        "ms_ans": "Mean bond enthalpies are not the same as the actual bond enthalpies in CO<sub>2</sub> (and/or methanol and/or water)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "04.3",
        "specRef": "3.1.4",
        "marks": 1,
        "stem": "Suggest why using methanol produced by this process as a fuel is said to be carbon neutral.",
        "figures": ["fig-q4-table2.jpg"],
        "ms_label": "04.3",
        "ms_ans": "The carbon dioxide (produced on burning methanol) is used up in this reaction",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "04.4",
        "specRef": "3.1.6",
        "marks": 3,
        "stem": "Explain why a high pressure is used in the industrial synthesis of methanol from carbon dioxide and hydrogen.",
        "figures": ["fig-q4-table2.jpg"],
        "ms_label": "04.4",
        "ms_ans": (
            "&bull; 4 mol of gas form 2 mol (1)<br>"
            "&bull; At high pressure the position of equilibrium moves to the right to lower the pressure / oppose the high pressure (1)<br>"
            "&bull; This increases the yield of methanol (1)"
        ),
        "ms_extra": "",
        "ms_marks": "3",
    },
    {
        "qnum": "04.5",
        "specRef": "3.2.5",
        "marks": 1,
        "stem": "Explain why the solid catalyst used in this process may become less active over time.",
        "figures": ["fig-q4-table2.jpg"],
        "ms_label": "04.5",
        "ms_ans": "Impurities (or sulfur compounds) block the active sites",
        "ms_extra": "Allow catalyst poisoned.",
        "ms_marks": "1",
    },
    {
        "qnum": "04.6",
        "specRef": "3.1.10",
        "marks": 7,
        "stem": "1.0 mol CO2 and 3.0 mol H2 react at 500 kPa until 0.86 mol CH3OH is formed at equilibrium. Calculate Kp and give its units.",
        "figures": ["fig-q4-table2.jpg"],
        "ms_label": "04.6",
        "ms_ans": (
            "<b>Stage 1: equilibrium moles</b><br>"
            "&bull; CO<sub>2</sub> = 1 &minus; 0.86 = 0.14; H<sub>2</sub> = 3 &minus; 3 &times; 0.86 = 0.42; CH<sub>3</sub>OH = 0.86; H<sub>2</sub>O = 0.86 (1)<br>"
            "<b>Stage 2: partial pressures</b><br>"
            "&bull; Total moles of gas = 2.28 (1)<br>"
            "&bull; p(CO<sub>2</sub>) = 0.14 &times; 500/2.28 = 30.7 kPa AND p(H<sub>2</sub>) = 0.42 &times; 500/2.28 = 92.1 kPa (1)<br>"
            "&bull; p(CH<sub>3</sub>OH) = 0.86 &times; 500/2.28 = 188.6 kPa AND p(H<sub>2</sub>O) = 188.6 kPa (1)<br>"
            "<b>Stage 3: K<sub>p</sub></b><br>"
            "&bull; K<sub>p</sub> = (p<sub>CH3OH</sub> &times; p<sub>H2O</sub>) / (p<sub>CO2</sub> &times; p<sub>H2</sub><sup>3</sup>) (1)<br>"
            "&bull; K<sub>p</sub> = (188.6 &times; 188.6) / (30.7 &times; 92.1<sup>3</sup>) = 1.483 &times; 10<sup>&minus;3</sup> = 1.5 &times; 10<sup>&minus;3</sup> (1)<br>"
            "&bull; Units = kPa<sup>&minus;2</sup> (1)"
        ),
        "ms_extra": "Extended response question. Answer must be to 2 significant figures.",
        "ms_marks": "7",
    },
    {
        "qnum": "05.1",
        "specRef": "3.1.8",
        "marks": 4,
        "stem": "Use the enthalpy change (-49 kJ mol-1) and entropy data from Table 3 to calculate the free-energy change (delta G) at 250 C, with units.",
        "figures": ["fig-q5-table3.jpg"],
        "crop_exclude_y": [[78, 260]],
        "ms_label": "05.1",
        "ms_ans": (
            "&bull; &Delta;S = 238 + 189 &minus; 214 &minus; 3 &times; 131 = &minus;180 J K<sup>&minus;1</sup> mol<sup>&minus;1</sup> (1)<br>"
            "&bull; &Delta;G = &Delta;H &minus; T&Delta;S (1)<br>"
            "&bull; = &minus;49 &minus; 523 &times; (&minus;180) / 1000 (1)<br>"
            "&bull; = +45.1 kJ mol<sup>&minus;1</sup> (1)"
        ),
        "ms_extra": "Units essential.",
        "ms_marks": "4",
    },
    {
        "qnum": "05.2",
        "specRef": "3.1.8",
        "marks": 2,
        "stem": "Calculate the temperature at which the reaction becomes feasible.",
        "figures": ["fig-q5-table3.jpg"],
        "ms_label": "05.2",
        "ms_ans": (
            "&bull; When &Delta;G = 0, &Delta;H = T&Delta;S therefore T = &Delta;H / &Delta;S (1)<br>"
            "&bull; = &minus;49 &times; 1000 / &minus;180 = 272 (K) (1)"
        ),
        "ms_extra": "Mark consequentially to &Delta;S in 5.1.",
        "ms_marks": "2",
    },
    {
        "qnum": "05.3",
        "specRef": "3.1.3",
        "marks": 4,
        "stem": "Draw a diagram to show how methanol molecules are attracted to each other in the liquid state, and name the strongest intermolecular force.",
        "ms_label": "05.3",
        "ms_ans": (
            "&bull; Diagram of a molecule showing O&minus;H bond and two lone pairs on each oxygen (1)<br>"
            "&bull; Labels on diagram showing &delta;+ and &delta;&minus; charges (1)<br>"
            "&bull; Diagram showing &delta;+ hydrogen on one molecule attracted to lone pair on a second molecule (1)<br>"
            "&bull; Hydrogen bonding (the name mentioned) is a strong enough force (to hold methanol molecules together in a liquid) (1)"
        ),
        "ms_extra": "Allow explanation of position of &delta;+ and &delta;&minus; charges on H and O.",
        "ms_marks": "4",
    },
    {
        "qnum": "06.1",
        "specRef": "RP",
        "marks": 2,
        "stem": "Suggest a suitable piece of apparatus that could be used to measure out the sodium hydroxide solution and explain why it is suitable.",
        "figures": ["fig-q6-fig1.jpg"],
        "crop_exclude_y": [[78, 490]],
        "ms_label": "06.1",
        "ms_ans": (
            "&bull; Burette (1)<br>"
            "&bull; Because it can deliver variable volumes (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "06.2",
        "specRef": "3.1.12",
        "marks": 2,
        "stem": "Use information from the curve in Figure 1 to explain why the end point of this reaction would be difficult to judge accurately using an indicator.",
        "figures": ["fig-q6-fig1.jpg"],
        "ms_label": "06.2",
        "ms_ans": (
            "&bull; The change in pH is gradual / not rapid at the end point (1)<br>"
            "&bull; An indicator would change colour over a range of volumes of sodium hydroxide (1)"
        ),
        "ms_extra": "Allow indicator would not change colour rapidly / with a few drops of NaOH.",
        "ms_marks": "2",
    },
    {
        "qnum": "06.3",
        "specRef": "3.1.12",
        "marks": 3,
        "stem": "The pH at the end of the experiment was 11.80. Calculate [OH-] at 25 C (Kw = 1.00 x 10^-14 mol2 dm-6).",
        "ms_label": "06.3",
        "ms_ans": (
            "&bull; [H<sup>+</sup>] = 10<sup>&minus;pH</sup> = 1.58 &times; 10<sup>&minus;12</sup> (1)<br>"
            "&bull; K<sub>w</sub> = [H<sup>+</sup>][OH<sup>&minus;</sup>] therefore [OH<sup>&minus;</sup>] = K<sub>w</sub> / [H<sup>+</sup>] (1)<br>"
            "&bull; [OH<sup>&minus;</sup>] = 1 &times; 10<sup>&minus;14</sup> / 1.58 &times; 10<sup>&minus;12</sup> = 6.33 &times; 10<sup>&minus;3</sup> (mol dm<sup>&minus;3</sup>) (1)"
        ),
        "ms_extra": "Allow 6.31&minus;6.33 &times; 10<sup>&minus;3</sup> (mol dm<sup>&minus;3</sup>).",
        "ms_marks": "3",
    },
    {
        "qnum": "06.4",
        "specRef": "3.1.12",
        "marks": 3,
        "stem": "Use the pH of 2.00 mol dm-3 NH4Cl(aq) from Figure 1 to calculate Ka for NH4+.",
        "figures": ["fig-q6-fig1.jpg"],
        "ms_label": "06.4",
        "ms_ans": (
            "&bull; At this point, [NH<sub>3</sub>] = [H<sup>+</sup>] therefore K<sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [NH<sub>4</sub><sup>+</sup>] (1)<br>"
            "&bull; [H<sup>+</sup>] = 10<sup>&minus;4.6</sup> = 2.51 &times; 10<sup>&minus;5</sup> (1)<br>"
            "&bull; K<sub>a</sub> = (2.51 &times; 10<sup>&minus;5</sup>)<sup>2</sup> / 2 = 3.15 &times; 10<sup>&minus;10</sup> (mol dm<sup>&minus;3</sup>) (1)"
        ),
        "ms_extra": "Allow 3.15&minus;3.16 &times; 10<sup>&minus;10</sup> (mol dm<sup>&minus;3</sup>).",
        "ms_marks": "3",
    },
    {
        "qnum": "06.5",
        "specRef": "3.1.12",
        "marks": 2,
        "stem": "A solution contains equal concentrations of ammonia and ammonium ions. Use your value of Ka from Question 6.4 to calculate the pH of this solution and explain your working.",
        "ms_label": "06.5",
        "ms_ans": (
            "&bull; When [NH<sub>3</sub>] = [NH<sub>4</sub><sup>+</sup>], K<sub>a</sub> = [H<sup>+</sup>] therefore &minus;log K<sub>a</sub> = &minus;log [H<sup>+</sup>] (1)<br>"
            "&bull; Therefore pH = &minus;log<sub>10</sub>(3.15 &times; 10<sup>&minus;10</sup>) = 9.50 (1)"
        ),
        "ms_extra": "Allow consequential marking based on answer from 6.4.",
        "ms_marks": "2",
    },
    {
        "qnum": "07.1",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "Which element in Table 4 (X, Y or Z) is calcium?",
        "figures": ["fig-q7-table4.jpg"],
        "crop_exclude_y": [[65, 418]],
        "ms_label": "07.1",
        "ms_ans": "<b>Y</b>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "07.2",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "Which element in Table 4 (X, Y or Z) is vanadium?",
        "figures": ["fig-q7-table4.jpg"],
        "ms_label": "07.2",
        "ms_ans": "<b>X</b>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "07.3",
        "specRef": "3.1.1",
        "marks": 1,
        "stem": "Justify your choice of vanadium in Question 7.2.",
        "figures": ["fig-q7-table4.jpg"],
        "ms_label": "07.3",
        "ms_ans": "Jump in trend of ionisation energies after removal of fifth electron; fits with an element with 5 outer electrons (4s<sup>2</sup>3d<sup>3</sup>) like V",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "07.4",
        "specRef": "3.2.5",
        "marks": 2,
        "stem": "When SO2 is bubbled through acidified NH4VO3, the solution changes colour from yellow to blue. Explain what this observation indicates about vanadium.",
        "ms_label": "07.4",
        "ms_ans": (
            "&bull; Two different colours of solution are observed (1)<br>"
            "&bull; Because each colour is due to vanadium in a different oxidation state (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "07.5",
        "specRef": "3.2.5",
        "marks": 6,
        "stem": "50.0 cm3 of 0.800 mol dm-3 NH4VO3 reacts with 506 cm3 of SO2 at 293 K and 98.0 kPa. Deduce the oxidation state of vanadium in the blue solution.",
        "ms_label": "07.5",
        "ms_ans": (
            "<b>Stage 1: mole calculations</b><br>"
            "&bull; Moles of vanadium = 50.0 &times; 0.800 / 1000 = 4.00 &times; 10<sup>&minus;2</sup> (1)<br>"
            "&bull; Moles of SO<sub>2</sub> = pV / RT = (98 000 &times; 506 &times; 10<sup>&minus;6</sup>) / (8.31 &times; 293) = 2.04 &times; 10<sup>&minus;2</sup> (1)<br>"
            "<b>Stage 2: moles of electrons</b><br>"
            "&bull; SO<sub>2</sub> is oxidised to sulfate(VI) ions so this is a two-electron change (1)<br>"
            "&bull; Moles of electrons released = 2.04 &times; 10<sup>&minus;2</sup> &times; 2 = 4.08 &times; 10<sup>&minus;2</sup> (1)<br>"
            "<b>Stage 3: conclusion</b><br>"
            "&bull; In NH<sub>4</sub>VO<sub>3</sub> vanadium is in oxidation state +5 (1)<br>"
            "&bull; 1 mol V gains 4.08 &times; 10<sup>&minus;2</sup> / 4.00 &times; 10<sup>&minus;2</sup> = 1 mol e<sup>&minus;</sup> (to nearest integer), so new oxidation state is 5 &minus; 1 = 4 (1)"
        ),
        "ms_extra": "Extended response: max 5 marks if no sustained, coherent, logically structured line of reasoning.",
        "ms_marks": "6",
    },
    {
        "qnum": "08.1",
        "specRef": "3.2.5",
        "marks": 2,
        "stem": "Explain how a ligand forms a co-ordinate bond to a central metal ion.",
        "ms_label": "08.1",
        "ms_ans": (
            "&bull; An electron pair on the ligand (1)<br>"
            "&bull; Is donated from the ligand to the central metal ion (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "08.2",
        "specRef": "3.2.6",
        "marks": 4,
        "stem": "Describe what is observed and write equations when aqueous ammonia is added dropwise and then in excess to [Cu(H2O)6]^2+.",
        "ms_label": "08.2",
        "ms_ans": (
            "&bull; Blue precipitate (1)<br>"
            "&bull; Dissolves to give a dark blue solution (1)<br>"
            "&bull; [Cu(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 2NH<sub>3</sub> &rarr; Cu(H<sub>2</sub>O)<sub>4</sub>(OH)<sub>2</sub> + 2NH<sub>4</sub><sup>+</sup> (1)<br>"
            "&bull; Cu(H<sub>2</sub>O)<sub>4</sub>(OH)<sub>2</sub> + 4NH<sub>3</sub> &rarr; [Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup> + 2OH<sup>&minus;</sup> + 2H<sub>2</sub>O (1)"
        ),
        "ms_extra": "",
        "ms_marks": "4",
    },
    {
        "qnum": "08.3",
        "specRef": "3.2.5",
        "marks": 1,
        "stem": "Write an equation for the reaction of [Cu(NH3)4(H2O)2]^2+ with 1,2-diaminoethane (H2NCH2CH2NH2).",
        "ms_label": "08.3",
        "ms_ans": "[Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup> + 2H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> &rarr; [Cu(H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub>)<sub>2</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup> + 4NH<sub>3</sub>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "08.4",
        "specRef": "3.2.5",
        "marks": 2,
        "stem": "Suggest why the enthalpy change for the reaction in Question 8.3 is approximately zero.",
        "ms_label": "08.4",
        "ms_ans": (
            "&bull; Cu&minus;N bonds formed have similar enthalpy / energy to Cu&minus;N bonds broken (1)<br>"
            "&bull; And the same number of bonds broken and made (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "08.5",
        "specRef": "3.1.8",
        "marks": 2,
        "stem": "Explain why the reaction in Question 8.3 occurs despite having an enthalpy change that is approximately zero.",
        "ms_label": "08.5",
        "ms_ans": (
            "&bull; 3 particles form 5 particles / disorder increases because more particles are formed / entropy change is positive (1)<br>"
            "&bull; Therefore, the free-energy change is negative (1)"
        ),
        "ms_extra": "M2 can only be awarded if M1 is correct.",
        "ms_marks": "2",
    },
    {
        "qnum": "09.1",
        "specRef": "RP",
        "marks": 4,
        "stem": "Describe how you would carry out an experiment to determine accurately the temperature change when 5.00 g of KCl dissolves in 50.0 cm3 of water.",
        "ms_label": "09.1",
        "ms_ans": (
            "&bull; Start a clock when KCl is added to water (1)<br>"
            "&bull; Record the temperature every subsequent minute for about 5 minutes (1)<br>"
            "&bull; Plot a graph of temperature vs time (1)<br>"
            "&bull; Extrapolate back to time of mixing = 0 and determine the temperature (1)"
        ),
        "ms_extra": "Allow record the temperature at regular time intervals until some time after all the solid has dissolved for M2.",
        "ms_marks": "4",
    },
    {
        "qnum": "09.2",
        "specRef": "3.1.8",
        "marks": 4,
        "stem": "5.00 g of KCl dissolved in 50.0 g of water caused a temperature fall of 5.4 C. Calculate the enthalpy of solution of KCl in kJ mol-1.",
        "ms_label": "09.2",
        "ms_ans": (
            "&bull; Heat taken in = m &times; c &times; &Delta;T = 50 &times; 4.18 &times; 5.4 = 1128.6 J (1)<br>"
            "&bull; Moles of KCl = 5.00 / 74.6 = 0.0670 (1)<br>"
            "&bull; Enthalpy change per mole = +1128.6 / 0.0670 = 16 839 J mol<sup>&minus;1</sup> (1)<br>"
            "&bull; = +16.8 (kJ mol<sup>&minus;1</sup>) (1)"
        ),
        "ms_extra": "Max 2 if 14.6 &deg;C used as &Delta;T. Answer must be given to 3 significant figures.",
        "ms_marks": "4",
    },
    {
        "qnum": "09.3",
        "specRef": "3.1.8",
        "marks": 2,
        "stem": "Use enthalpy of solution of CaCl2 (-82.9 kJ mol-1) and hydration enthalpies (Ca2+ = -1650, Cl- = -364 kJ mol-1) to calculate the lattice enthalpy of dissociation of CaCl2.",
        "ms_label": "09.3",
        "ms_ans": (
            "&bull; &Delta;H<sub>solution</sub> = &Delta;H<sub>lattice</sub> + &Delta;H<sub>hyd</sub>(Ca<sup>2+</sup>) + 2 &times; &Delta;H<sub>hyd</sub>(Cl<sup>&minus;</sup>) &rarr; &Delta;H<sub>lattice</sub> = &Delta;H<sub>solution</sub> &minus; &Delta;H<sub>hyd</sub>(Ca<sup>2+</sup>) &minus; 2 &times; &Delta;H<sub>hyd</sub>(Cl<sup>&minus;</sup>) (1)<br>"
            "&bull; &Delta;H<sub>lattice</sub> = &minus;82.9 &minus; (&minus;1650 + 2 &times; &minus;364) = +2295 (kJ mol<sup>&minus;1</sup>) (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "09.4",
        "specRef": "3.1.8",
        "marks": 2,
        "stem": "Explain why your answer to Question 9.3 is different from the lattice enthalpy of dissociation for magnesium chloride.",
        "ms_label": "09.4",
        "ms_ans": (
            "&bull; Magnesium ion is smaller than the calcium ion (1)<br>"
            "&bull; Therefore, it attracts the chloride ion more strongly / stronger ionic bonding (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "10.1",
        "specRef": "3.2.6",
        "marks": 6,
        "stem": "Use the observations in Table 5 to identify each of compounds Q, R and S.",
        "figures": ["fig-q10-table5.jpg"],
        "crop_exclude_y": [[78, 353]],
        "ms_label": "10.1",
        "ms_ans": (
            "&bull; Q is calcium or magnesium (1) bromide (1)<br>"
            "&bull; R is aluminium (1) chloride (1)<br>"
            "&bull; S is iron(III) (1) sulfate (1)"
        ),
        "ms_extra": "Mark each cation and anion independently.",
        "ms_marks": "6",
    },
    {
        "qnum": "10.2",
        "specRef": "3.2.6",
        "marks": 4,
        "stem": "Write ionic equations for each of the positive observations with compound S in Table 5.",
        "figures": ["fig-q10-table5.jpg"],
        "ms_label": "10.2",
        "ms_ans": (
            "&bull; Ba<sup>2+</sup> + SO<sub>4</sub><sup>2&minus;</sup> &rarr; BaSO<sub>4</sub> (1)<br>"
            "&bull; [Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + 3OH<sup>&minus;</sup> &rarr; Fe(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub> + 3H<sub>2</sub>O (1)<br>"
            "&bull; 2[Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + 3CO<sub>3</sub><sup>2&minus;</sup> &rarr; 2Fe(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub> + 3H<sub>2</sub>O + 3CO<sub>2</sub> (1)<br>"
            "&bull; [Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + 4Cl<sup>&minus;</sup> &rarr; [FeCl<sub>4</sub>]<sup>&minus;</sup> + 6H<sub>2</sub>O (1)"
        ),
        "ms_extra": "",
        "ms_marks": "4",
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
    "01.1": 2, "01.2": 3, "01.3": 3, "01.4": 3,
    "02.1": 4, "02.2": 4, "02.3": 4, "02.4": 5,
    "03.1": 6, "03.2": 6, "03.3": 7, "03.4": 7, "03.5": 7,
    "04.1": 8, "04.2": 8, "04.3": 9, "04.4": 9, "04.5": 9, "04.6": 10,
    "05.1": 12, "05.2": 13, "05.3": 13,
    "06.1": 14, "06.2": 15, "06.3": 15, "06.4": 16, "06.5": 16,
    "07.1": 18, "07.2": 18, "07.3": 19, "07.4": 19, "07.5": 20,
    "08.1": 22, "08.2": 22, "08.3": 23, "08.4": 23, "08.5": 23,
    "09.1": 24, "09.2": 24, "09.3": 25, "09.4": 25,
    "10.1": 26, "10.2": 27,
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

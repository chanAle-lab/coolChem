"""Ingest AQA AS Chemistry Specimen Paper 2 (7404/2) into data/questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517590689_9a9d9dff.pdf"
)

PAPER_ID = "2015-specimen-7404-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2015,
    "series": "Specimen",
    "unit": "7404/2",
    "level": "AS",
    "date": "2015-01-01",
    "title": "7404/2 — AS Paper 2: Organic and Physical Chemistry (Specimen)",
    "totalMarks": 80,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {
        "filename": "fig-q1-stem.jpg",
        "page": 2,
        "x0": 40,
        "y0": 140,
        "x1": 565,
        "y1": 196,
    },
    {
        "filename": "fig-q2-apparatus.jpg",
        "page": 6,
        "x0": 40,
        "y0": 65,
        "x1": 565,
        "y1": 620,
    },
    {
        "filename": "fig-q6-fig2.jpg",
        "page": 14,
        "x0": 40,
        "y0": 88,
        "x1": 565,
        "y1": 348,
    },
    {
        "filename": "fig-q7-table2.jpg",
        "page": 16,
        "x0": 40,
        "y0": 88,
        "x1": 565,
        "y1": 395,
    },
    {
        "filename": "fig-q17-18-scheme.jpg",
        "page": 21,
        "x0": 40,
        "y0": 264,
        "x1": 565,
        "y1": 415,
    },
    {
        "filename": "fig-q19-20-fig3.jpg",
        "page": 22,
        "x0": 40,
        "y0": 65,
        "x1": 565,
        "y1": 385,
    },
    {
        "filename": "fig-q21-22-fig4.jpg",
        "page": 23,
        "x0": 40,
        "y0": 65,
        "x1": 565,
        "y1": 350,
    },
]

QUESTIONS = [
    {
        "qnum": "01.1",
        "specRef": "3.3.1",
        "marks": 1,
        "stem": "Give the structure of the E isomer of leaf alcohol J (CH3CH2CH=CHCH2CH2OH).",
        "ms_label": "01.1",
        "ms_ans": "<i>trans</i>-alkene structure with CH<sub>3</sub>CH<sub>2</sub> and H on one C=C carbon, and H and CH<sub>2</sub>CH<sub>2</sub>OH on the other C=C carbon (CH<sub>3</sub>CH<sub>2</sub> and CH<sub>2</sub>CH<sub>2</sub>OH on opposite sides)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "01.2",
        "specRef": "3.3.5",
        "marks": 1,
        "stem": "Give the skeletal formula of the organic product formed when J is dehydrated using concentrated sulfuric acid.",
        "figures": ["fig-q1-stem.jpg"],
        "ms_label": "01.2",
        "ms_ans": "Skeletal formula of hexa-1,3-diene (CH<sub>3</sub>CH<sub>2</sub>CH=CHCH=CH<sub>2</sub>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "01.3",
        "specRef": "3.3.1",
        "marks": 6,
        "stem": "Deduce the full IUPAC name of isomer K of leaf alcohol J, including the Z/E prefix deduced using Cahn-Ingold-Prelog priority rules.",
        "figures": ["fig-q1-stem.jpg"],
        "ms_label": "01.3",
        "ms_ans": (
            "<b>Stage 1: right-hand carbon of C=C</b><br>"
            "&bull; Consider the atomic number of the atoms attached (1)<br>"
            "&bull; C has a higher atomic number than H, so CH<sub>2</sub>OH takes priority (1)<br>"
            "<b>Stage 2: left-hand carbon of C=C</b><br>"
            "&bull; Both groups contain C atoms, so consider atoms one bond further away (1)<br>"
            "&bull; C, (H and H) from ethyl group has higher atomic number than H, (H and H) from methyl group, so ethyl takes priority (1)<br>"
            "<b>Stage 3: conclusion</b><br>"
            "&bull; The highest priority groups, ethyl and CH<sub>2</sub>OH, are on same side of the C=C bond so the isomer is <i>Z</i> (1)<br>"
            "&bull; The rest of the IUPAC name is 3-methylpent-2-en-1-ol (1)"
        ),
        "ms_extra": "Extended response: max 5 marks if no sustained, coherent, logically structured line of reasoning. Allow M5 for correct ECF conclusion from wrong priorities.",
        "ms_marks": "6",
    },
    {
        "qnum": "01.4",
        "specRef": "3.1.2",
        "marks": 2,
        "stem": "Determine whether a student was correct to claim a 70% yield when 10.0 g of maleic acid (Mr = 116.0) formed 6.53 g of organic product (Mr = 98.0).",
        "ms_label": "01.4",
        "ms_ans": (
            "&bull; Moles of maleic acid = 10.0 / 116.0 = 8.62 &times; 10<sup>&minus;2</sup> AND expected mass = 8.62 &times; 10<sup>&minus;2</sup> &times; 98.0 = 8.45 g (or moles formed = 6.53 / 98.0 = 6.66 &times; 10<sup>&minus;2</sup>) (1)<br>"
            "&bull; % yield = 100 &times; 6.53 / 8.45 = 77.3% AND statement that the student was NOT correct (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "02.1",
        "specRef": "3.1.4",
        "marks": 1,
        "stem": "Write an equation for the complete combustion of leaf alcohol (CH3CH2CH=CHCH2CH2OH).",
        "figures": ["fig-q2-apparatus.jpg"],
        "crop_exclude_y": [[65, 620]],
        "ms_label": "02.1",
        "ms_ans": "C<sub>6</sub>H<sub>11</sub>OH + 8&frac12;O<sub>2</sub> &rarr; 6CO<sub>2</sub> + 6H<sub>2</sub>O",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "02.2",
        "specRef": "3.1.4",
        "marks": 4,
        "stem": "Use the results from Table 1 to calculate a value for the enthalpy of combustion of leaf alcohol.",
        "figures": ["fig-q2-apparatus.jpg"],
        "ms_label": "02.2",
        "ms_ans": (
            "&bull; Temperature rise = 20.1 &deg;C; q = 50.0 &times; 4.18 &times; 20.1 = 4201 (J) (1)<br>"
            "&bull; Mass of alcohol burned = 0.54 g, M<sub>r</sub> = 100.0 &rarr; mol alcohol n = 0.54 / 100.0 = 0.0054 (1)<br>"
            "&bull; Heat change per mole = q / (1000n) = 778 kJ mol<sup>&minus;1</sup> (or 778 000 J mol<sup>&minus;1</sup>) (1)<br>"
            "&bull; &Delta;H = &minus;778 kJ mol<sup>&minus;1</sup> (or &minus;778 000 J mol<sup>&minus;1</sup>) (1)"
        ),
        "ms_extra": "M4 is for negative sign for exothermic reaction. Units are tied to the final answer and must match.",
        "ms_marks": "4",
    },
    {
        "qnum": "02.3",
        "specRef": "3.1.4",
        "marks": 2,
        "stem": "State how your answer to Question 2.2 is likely to differ from the data book value and give one reason for this difference.",
        "figures": ["fig-q2-apparatus.jpg"],
        "ms_label": "02.3",
        "ms_ans": (
            "&bull; Less negative than the reference (1)<br>"
            "&bull; Heat loss OR incomplete combustion OR evaporation of alcohol OR heat transferred to beaker not taken into account (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "02.4",
        "specRef": "RP",
        "marks": 2,
        "stem": "Explain why the 50.0 g sample of water in the calorimeter did not need to be weighed.",
        "ms_label": "02.4",
        "ms_ans": (
            "&bull; Water has a known density (of 1.0 g cm<sup>&minus;3</sup>) (1)<br>"
            "&bull; Therefore, a volume of 50.0 cm<sup>3</sup> could be measured out (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "03.1",
        "specRef": "3.3.1",
        "marks": 1,
        "stem": "State what is meant by the term structural isomers.",
        "ms_label": "03.1",
        "ms_ans": "(Compounds with the) same molecular formula but different structural / displayed / skeletal formula",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "03.2",
        "specRef": "3.3.3",
        "marks": 5,
        "stem": "Name and outline a mechanism for the reaction of 2-bromopentane with ethanolic potassium hydroxide to form a structural isomer of pent-1-ene.",
        "ms_label": "03.2",
        "ms_ans": (
            "&bull; (Base) elimination (1)<br>"
            "&bull; Curly arrow from lone pair on :OH<sup>&minus;</sup> to H on C adjacent to C&minus;Br (1)<br>"
            "&bull; Curly arrow from C&minus;H bond to C&minus;C (1)<br>"
            "&bull; Curly arrow from C&minus;Br bond to Br (1)<br>"
            "&bull; Structure of chosen product: <i>E</i>-pent-2-ene or <i>Z</i>-pent-2-ene (1)"
        ),
        "ms_extra": "",
        "ms_marks": "5",
    },
    {
        "qnum": "04.1",
        "specRef": "3.1.2",
        "marks": 4,
        "stem": "A compound has 40.9% C, 4.5% H and the remainder oxygen by mass, and Mr = 88.0. Calculate its molecular formula.",
        "ms_label": "04.1",
        "ms_ans": (
            "&bull; % O = 100 &minus; 40.9 &minus; 4.5 = 54.6% (1)<br>"
            "&bull; Moles ratio C : H : O = 40.9/12 : 4.5/1 : 54.6/16 = 3.41 : 4.5 : 3.41 (1)<br>"
            "&bull; Divide by smallest: 1 : 1.32 : 1 &rarr; &times;3 &rarr; 3 : 4 : 3 &rarr; Empirical formula C<sub>3</sub>H<sub>4</sub>O<sub>3</sub> (1)<br>"
            "&bull; Empirical formula mass = 88 = molecular formula mass, so molecular formula is C<sub>3</sub>H<sub>4</sub>O<sub>3</sub> (1)"
        ),
        "ms_extra": "",
        "ms_marks": "4",
    },
    {
        "qnum": "04.2",
        "specRef": "3.3.5",
        "marks": 1,
        "stem": "Write an equation for the fermentation of glucose to form ethanol.",
        "ms_label": "04.2",
        "ms_ans": "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> &rarr; 2C<sub>2</sub>H<sub>5</sub>OH + 2CO<sub>2</sub>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "04.3",
        "specRef": "3.3.5",
        "marks": 2,
        "stem": "Give one advantage and one disadvantage of carrying out fermentation at 40 C rather than 20 C.",
        "ms_label": "04.3",
        "ms_ans": (
            "&bull; Advantage: ethanol is produced at a faster rate (1)<br>"
            "&bull; Disadvantage: more energy is used / required in the reaction (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "04.4",
        "specRef": "3.3.5",
        "marks": 1,
        "stem": "Explain why ethanoic acid was formed when a fermentation mixture was left in an open flask.",
        "ms_label": "04.4",
        "ms_ans": "Air gets in / oxidation occurs",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "04.5",
        "specRef": "3.3.6",
        "marks": 2,
        "stem": "Explain how infrared spectroscopy could be used to show that ethanoic acid was present rather than ethanol, using Table A on the Data Sheet.",
        "ms_label": "04.5",
        "ms_ans": (
            "&bull; Alcohol O&minus;H absorption in different place (3230&minus;3550 cm<sup>&minus;1</sup>) from acid O&minus;H absorption (2500&minus;3000 cm<sup>&minus;1</sup>) (1)<br>"
            "&bull; The C=O in acids has an absorption at 1680&minus;1750 cm<sup>&minus;1</sup> (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "05.1",
        "specRef": "3.3.3",
        "marks": 2,
        "stem": "State the condition and write an equation for the initiation step when tetrachloromethane (CCl4) forms chlorine free radicals in the upper atmosphere.",
        "ms_label": "05.1",
        "ms_ans": (
            "&bull; UV light (1)<br>"
            "&bull; CCl<sub>4</sub> &rarr; CCl<sub>3</sub><sup>&bull;</sup> + <sup>&bull;</sup>Cl (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "05.2",
        "specRef": "3.3.3",
        "marks": 2,
        "stem": "Write equations to show how chlorine free radicals catalyse the decomposition of ozone.",
        "ms_label": "05.2",
        "ms_ans": (
            "&bull; Cl<sup>&bull;</sup> + O<sub>3</sub> &rarr; ClO<sup>&bull;</sup> + O<sub>2</sub> (1)<br>"
            "&bull; ClO<sup>&bull;</sup> + O<sub>3</sub> &rarr; Cl<sup>&bull;</sup> + 2O<sub>2</sub> (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "05.3",
        "specRef": "3.1.2",
        "marks": 3,
        "stem": "100 m3 of air contains 1.78 x 10^-4 kg of CF3Cl. Calculate the number of CF3Cl molecules in a 500 cm3 sample of this air.",
        "ms_label": "05.3",
        "ms_ans": (
            "&bull; M<sub>r</sub> of CF<sub>3</sub>Cl = 104.5; Moles = (1.78 &times; 10<sup>&minus;4</sup> &times; 10<sup>3</sup>) / 104.5 = 1.70 &times; 10<sup>&minus;3</sup> (1)<br>"
            "&bull; Number of molecules in 100 m<sup>3</sup> = 1.70 &times; 10<sup>&minus;3</sup> &times; 6.02 &times; 10<sup>23</sup> = 1.02 &times; 10<sup>21</sup> (1)<br>"
            "&bull; Molecules in 500 cm<sup>3</sup> = (1.02 &times; 10<sup>21</sup> &times; 500 &times; 10<sup>&minus;6</sup>) / 100 = 5.10 &times; 10<sup>15</sup> (1)"
        ),
        "ms_extra": "Allow answer in the range 5.10&minus;5.13 &times; 10<sup>15</sup>. Answer must be given to this precision (3 sig figs).",
        "ms_marks": "3",
    },
    {
        "qnum": "06.1",
        "specRef": "3.3.4",
        "marks": 2,
        "stem": "Name the homologous series that both C2H4 and C4H8 belong to, and draw a functional group isomer of C4H8 that does not belong to this homologous series.",
        "figures": ["fig-q6-fig2.jpg"],
        "crop_exclude_y": [[88, 348]],
        "ms_label": "06.1",
        "ms_ans": (
            "&bull; Alkenes (1)<br>"
            "&bull; Structure of cyclobutane or methylcyclopropane (1)"
        ),
        "ms_extra": "Correctly drawn molecule of cyclobutane or methylcyclopropane; need not be displayed formula.",
        "ms_marks": "2",
    },
    {
        "qnum": "06.2",
        "specRef": "3.3.2",
        "marks": 1,
        "stem": "Identify compound X in Reaction 1 (Figure 2).",
        "figures": ["fig-q6-fig2.jpg"],
        "ms_label": "06.2",
        "ms_ans": "C<sub>6</sub>H<sub>14</sub> (or correct alkane structure with 6 carbons)",
        "ms_extra": "Allow hexane or any other correctly named alkane with 6 carbons.",
        "ms_marks": "1",
    },
    {
        "qnum": "06.3",
        "specRef": "3.3.4",
        "marks": 1,
        "stem": "Name polymer Y in Figure 2.",
        "figures": ["fig-q6-fig2.jpg"],
        "ms_label": "06.3",
        "ms_ans": "Poly(but-2-ene)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "06.4",
        "specRef": "3.3.2",
        "marks": 1,
        "stem": "Reaction 1 is thermal cracking carried out at 750 C. State one other reaction condition needed.",
        "figures": ["fig-q6-fig2.jpg"],
        "ms_label": "06.4",
        "ms_ans": "High pressure",
        "ms_extra": "Allow pressure &ge; 1 MPa. Mention of catalyst loses the mark.",
        "ms_marks": "1",
    },
    {
        "qnum": "06.5",
        "specRef": "3.1.6",
        "marks": 6,
        "stem": "Reaction 2 is exothermic. Explain the effect of a change of temperature on both the position of equilibrium and the rate of reaction, and justify why a compromise temperature of 200 C is used industrially.",
        "figures": ["fig-q6-fig2.jpg"],
        "ms_label": "06.5",
        "ms_ans": (
            "<b>Indicative chemistry content:</b><br>"
            "<b>Stage 1: effect of higher temperature on yield</b> (or vice versa)<br>"
            "&bull; Le Chatelier's principle predicts equilibrium shifts to oppose any increase in temperature<br>"
            "&bull; Exothermic reaction, so equilibrium shifts in endothermic direction / to the left<br>"
            "&bull; Higher T will reduce yield<br>"
            "<b>Stage 2: effect of higher temperature on rate</b> (or vice versa)<br>"
            "&bull; At higher T, more high-energy molecules / more collisions have E &gt; E<sub>a</sub><br>"
            "&bull; So rate of reaction increases / time to reach equilibrium decreases<br>"
            "<b>Stage 3: conclusion</b><br>"
            "&bull; Industrial conditions chosen to achieve (cost-effective) balance of suitable yield at reasonable rate"
        ),
        "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).",
        "ms_marks": "6",
    },
    {
        "qnum": "07.1",
        "specRef": "RP",
        "marks": 2,
        "stem": "In a trial experiment, the gap between the tap and the tip of the burette still contained air. Suggest what effect this would have on the measured volume of bromine water and explain your answer.",
        "figures": ["fig-q7-table2.jpg"],
        "crop_exclude_y": [[88, 395]],
        "ms_label": "07.1",
        "ms_ans": (
            "&bull; Measured volume would be greater (1)<br>"
            "&bull; Level in burette falls as tap is filled before any liquid is delivered (1)"
        ),
        "ms_extra": "",
        "ms_marks": "2",
    },
    {
        "qnum": "07.2",
        "specRef": "RP",
        "marks": 1,
        "stem": "Other than incorrect use of the burette, suggest a reason for the inconsistency in the student's results in Table 2.",
        "figures": ["fig-q7-table2.jpg"],
        "ms_label": "07.2",
        "ms_ans": "Drop sizes vary",
        "ms_extra": "Allow percentage error for amount of oil will be large as the amount used is so small.",
        "ms_marks": "1",
    },
    {
        "qnum": "07.3",
        "specRef": "RP",
        "marks": 4,
        "stem": "Outline how the student could improve this practical procedure so that more consistent results are obtained.",
        "figures": ["fig-q7-table2.jpg"],
        "ms_label": "07.3",
        "ms_ans": (
            "&bull; Use a larger single volume of oil (1)<br>"
            "&bull; Dissolve this oil in the organic solvent (1)<br>"
            "&bull; Transfer to a volumetric/conical flask and make up to 250 cm<sup>3</sup> with more solvent (1)<br>"
            "&bull; Titrate (25 cm<sup>3</sup>) samples from the flask (1)"
        ),
        "ms_extra": "",
        "ms_marks": "4",
    },
    {
        "qnum": "07.4",
        "specRef": "3.1.2",
        "marks": 5,
        "stem": "Use the data (density 0.92 g cm-3, 5 drops of 5.0 x 10^-2 cm3, Mr 885, 2.0 x 10^-2 mol dm-3 Br2(aq), 39.40 cm3) to deduce the number of C=C double bonds in a molecule of the oil.",
        "figures": ["fig-q7-table2.jpg"],
        "ms_label": "07.4",
        "ms_ans": (
            "<b>Stage 1:</b><br>"
            "&bull; Mass of oil = 0.92 &times; (5.0 &times; 10<sup>&minus;2</sup> &times; 5) = 0.23 (g) (1)<br>"
            "&bull; Mol of oil = 0.23 / 885 = 2.6 &times; 10<sup>&minus;4</sup> (1)<br>"
            "<b>Stage 2:</b><br>"
            "&bull; Mol bromine = 2.0 &times; 10<sup>&minus;2</sup> &times; 39.4 / 1000 = 7.9 &times; 10<sup>&minus;4</sup> (1)<br>"
            "<b>Stage 3:</b><br>"
            "&bull; Ratio oil : bromine = 2.6 &times; 10<sup>&minus;4</sup> : 7.9 &times; 10<sup>&minus;4</sup> = 1 : 3 (1)<br>"
            "&bull; Hence, 3 C=C bonds (1)"
        ),
        "ms_extra": "Extended response calculation. M5 cannot be awarded unless working for M4 is shown.",
        "ms_marks": "5",
    },
    {
        "qnum": "08",
        "specRef": "3.1.2",
        "marks": 1,
        "stem": "Which of these samples of gas contains the largest number of molecules?",
        "ms_label": "08",
        "ms_ans": "<b>B</b> (4.0 &times; 10<sup>&minus;3</sup> m<sup>3</sup> at 2.0 &times; 10<sup>5</sup> Pa and 400 K)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "09",
        "specRef": "3.1.3",
        "marks": 1,
        "stem": "Which of these substances has permanent dipole-dipole attractions between molecules?",
        "ms_label": "09",
        "ms_ans": "<b>C</b> ((CH<sub>3</sub>)<sub>2</sub>CO)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "10",
        "specRef": "3.1.2",
        "marks": 1,
        "stem": "What is the total volume of gas remaining after 20 cm3 ethane are burned completely in 100 cm3 oxygen above 100 C?",
        "ms_label": "10",
        "ms_ans": "<b>D</b> (130 cm<sup>3</sup>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "11",
        "specRef": "3.3.4",
        "marks": 1,
        "stem": "Which species is formed in the mechanism of the reaction between propene and hydrogen bromide to form the major product?",
        "ms_label": "11",
        "ms_ans": "<b>C</b> (CH<sub>3</sub>&minus;C<sup>+</sup>H&minus;CH<sub>3</sub>)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "12",
        "specRef": "3.3.3",
        "marks": 1,
        "stem": "Which of these substances reacts most rapidly to produce a silver halide precipitate with acidified silver nitrate?",
        "ms_label": "12",
        "ms_ans": "<b>D</b> (CH<sub>3</sub>I)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "13",
        "specRef": "3.3.4",
        "marks": 1,
        "stem": "Which statement about E-1,2-dichloroethene is correct?",
        "ms_label": "13",
        "ms_ans": "<b>B</b> (It forms a polymer with the same repeating unit as <i>Z</i>-1,2-dichloroethene)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "14",
        "specRef": "3.3.4",
        "marks": 1,
        "stem": "Which statement about ethene is correct?",
        "ms_label": "14",
        "ms_ans": "<b>C</b> (It burns in excess oxygen to produce carbon dioxide and water)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "15",
        "specRef": "3.3.5",
        "marks": 1,
        "stem": "Which statement about ethanal is correct?",
        "ms_label": "15",
        "ms_ans": "<b>A</b> (It reacts with Tollens' reagent to form silver)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "16",
        "specRef": "3.3.2",
        "marks": 1,
        "stem": "Which of these substances does not contribute to the greenhouse effect?",
        "ms_label": "16",
        "ms_ans": "<b>D</b> (Nitrogen)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "17",
        "specRef": "3.3.3",
        "marks": 1,
        "stem": "Which of the curly arrows in the mechanism for preparing ethylamine is not correct?",
        "figures": ["fig-q17-18-scheme.jpg"],
        "crop_exclude_y": [[264, 415]],
        "ms_label": "17",
        "ms_ans": "<b>D</b> (4)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "18",
        "specRef": "3.3.3",
        "marks": 1,
        "stem": "Which statement about the preparation of ethylamine from bromoethane and ammonia is not correct?",
        "figures": ["fig-q17-18-scheme.jpg"],
        "ms_label": "18",
        "ms_ans": "<b>C</b> (Using an excess of bromoethane will prevent further reaction to form a mixture of amine products)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "19",
        "specRef": "3.1.5",
        "marks": 1,
        "stem": "Which letter in Figure 3 best represents the mean energy of the molecules?",
        "figures": ["fig-q19-20-fig3.jpg"],
        "crop_exclude_y": [[65, 385]],
        "ms_label": "19",
        "ms_ans": "<b>C</b>",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "20",
        "specRef": "3.1.5",
        "marks": 1,
        "stem": "What does the area under the curve in Figure 3 represent?",
        "figures": ["fig-q19-20-fig3.jpg"],
        "ms_label": "20",
        "ms_ans": "<b>B</b> (The total number of particles)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "21",
        "specRef": "RP",
        "marks": 1,
        "stem": "What is likely to decrease the accuracy of the sodium thiosulfate + HCl disappearing cross experiment (Figure 4)?",
        "figures": ["fig-q21-22-fig4.jpg"],
        "crop_exclude_y": [[65, 350]],
        "ms_label": "21",
        "ms_ans": "<b>A</b> (Rinsing the flask with acid before each new experiment)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "qnum": "22",
        "specRef": "RP",
        "marks": 1,
        "stem": "Which statement is correct about the time taken for the cross to disappear when repeating the experiment using a larger 250 cm3 conical flask?",
        "figures": ["fig-q21-22-fig4.jpg"],
        "ms_label": "22",
        "ms_ans": "<b>C</b> (The time taken will be increased by using the larger conical flask)",
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
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 4,
    "02.1": 6, "02.2": 7, "02.3": 7, "02.4": 8,
    "03.1": 9, "03.2": 9,
    "04.1": 10, "04.2": 10, "04.3": 10, "04.4": 11, "04.5": 11,
    "05.1": 12, "05.2": 12, "05.3": 12,
    "06.1": 14, "06.2": 14, "06.3": 14, "06.4": 15, "06.5": 15,
    "07.1": 16, "07.2": 16, "07.3": 17, "07.4": 17,
    "08": 18, "09": 18,
    "10": 19, "11": 19, "12": 19,
    "13": 20, "14": 20, "15": 20,
    "16": 21, "17": 21, "18": 21,
    "19": 22, "20": 22,
    "21": 23, "22": 23,
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

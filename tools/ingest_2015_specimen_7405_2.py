"""Ingest AQA A-level Chemistry Specimen Paper 2 (7405/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517607397_bfd48c64.pdf"
)

PAPER_ID = "2015-specimen-7405-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2015,
    "series": "Specimen",
    "unit": "7405/2",
    "level": "A-level",
    "date": "2015-01-01",
    "title": "7405/2 — A-level Paper 2: Organic and Physical Chemistry (Specimen)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q2-fig1.jpg", "page": 6, "x0": 40, "y0": 78, "x1": 565, "y1": 575},
    {"filename": "fig-q3-fig2.jpg", "page": 8, "x0": 40, "y0": 78, "x1": 565, "y1": 240},
    {"filename": "fig-q4-stem.jpg", "page": 12, "x0": 40, "y0": 65, "x1": 565, "y1": 115},
    {"filename": "fig-q5-fig3.jpg", "page": 14, "x0": 40, "y0": 78, "x1": 565, "y1": 365},
    {"filename": "fig-q6-fig4.jpg", "page": 15, "x0": 40, "y0": 78, "x1": 565, "y1": 278},
    {"filename": "fig-q7-fig5.jpg", "page": 16, "x0": 40, "y0": 78, "x1": 565, "y1": 225},
    {"filename": "fig-q8-fig6.jpg", "page": 18, "x0": 40, "y0": 78, "x1": 565, "y1": 445},
    {"filename": "fig-q9-fig8.jpg", "page": 22, "x0": 40, "y0": 75, "x1": 565, "y1": 450},
    {"filename": "fig-q10-spectra.jpg", "page": 26, "x0": 40, "y0": 65, "x1": 565, "y1": 785},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3, "01.3": 3, "01.4": 4, "01.5": 4,
    "02.1": 6, "02.2": 7,
    "03.1": 8, "03.2": 8, "03.3": 9, "03.4": 9, "03.5": 9, "03.6": 9, "03.7": 10, "03.8": 10,
    "04.1": 12, "04.2": 12, "04.3": 12, "04.4": 12, "04.5": 13, "04.6": 13, "04.7": 13, "04.8": 13,
    "05.1": 14, "05.2": 14,
    "06.1": 15, "06.2": 15, "06.3": 15, "06.4": 15, "06.5": 15,
    "07.1": 16, "07.2": 16, "07.3": 17,
    "08.1": 18, "08.2": 19, "08.3": 20, "08.4": 20,
    "09.1": 22, "09.2": 23, "09.3": 24, "09.4": 25, "09.5": 25, "09.6": 25, "09.7": 25, "09.8": 25,
    "10": 27,
    "11.1": 28, "11.2": 28,
    "12.1": 29, "12.2": 29, "12.3": 29,
}

QUESTIONS = [
    {
        "qnum": "01.1", "specRef": "3.1.9", "marks": 3,
        "stem": "Show how the kinetic data in Table 1 can be used to deduce the rate expression for the reaction between A and B.",
        "ms_label": "01.1",
        "ms_ans": (
            "&bull; Consider experiments 1 and 2 ([B] constant): [A] increases &times; 3, rate increases by 3<sup>2</sup> &rarr; 2nd order with respect to A (1)<br>"
            "&bull; Consider experiments 2 and 3: [A] increases &times; 2 (rate should increase &times; 2<sup>2</sup>) but only increases &times; 2; halving [B] halves rate &rarr; 1st order with respect to B (1)<br>"
            "&bull; Rate equation: rate = k[A]<sup>2</sup>[B] (1)"
        ),
        "ms_extra": "", "ms_marks": "3",
    },
    {
        "qnum": "01.2", "specRef": "3.1.9", "marks": 3,
        "stem": "Use the data from experiment 4 in Table 2 and rate = k[C]^2[D] to calculate k and deduce its units.",
        "ms_label": "01.2",
        "ms_ans": (
            "&bull; k = rate / ([C]<sup>2</sup>[D]) (1)<br>"
            "&bull; k = 7.2 &times; 10<sup>&minus;4</sup> / ((1.9 &times; 10<sup>&minus;2</sup>)<sup>2</sup> &times; 3.5 &times; 10<sup>&minus;2</sup>) = 57.0 (1)<br>"
            "&bull; mol<sup>&minus;2</sup> dm<sup>+6</sup> s<sup>&minus;1</sup> (1)"
        ),
        "ms_extra": "Allow consequential marking on incorrect transcription. Units in any order.", "ms_marks": "3",
    },
    {
        "qnum": "01.3", "specRef": "3.1.9", "marks": 1,
        "stem": "Calculate a value for the initial rate in experiment 5.",
        "ms_label": "01.3",
        "ms_ans": "rate = 57.0 &times; (3.6 &times; 10<sup>&minus;2</sup>)<sup>2</sup> &times; 5.4 &times; 10<sup>&minus;2</sup> = 3.99 &times; 10<sup>&minus;3</sup> (mol dm<sup>&minus;3</sup> s<sup>&minus;1</sup>)",
        "ms_extra": "OR their k &times; (3.6 &times; 10<sup>&minus;2</sup>)<sup>2</sup> &times; 5.4 &times; 10<sup>&minus;2</sup>.", "ms_marks": "1",
    },
    {
        "qnum": "01.4", "specRef": "3.1.5", "marks": 3,
        "stem": "For rate = k[E], explain qualitatively why doubling the temperature has a much greater effect on the rate of reaction than doubling [E].",
        "ms_label": "01.4",
        "ms_ans": (
            "&bull; Reaction occurs when molecules have E &ge; E<sub>a</sub> (1)<br>"
            "&bull; Doubling T causes <u>many</u> more molecules to have this E (1)<br>"
            "&bull; Whereas doubling [E] only doubles the number with this E (1)"
        ),
        "ms_extra": "", "ms_marks": "3",
    },
    {
        "qnum": "01.5", "specRef": "3.1.9", "marks": 2,
        "stem": "Use ln k = ln A - Ea/RT with k = 6.51 x 10^-3 and A = 2.57 x 10^10 at 300 K to calculate Ea in kJ mol-1.",
        "ms_label": "01.5",
        "ms_ans": (
            "&bull; E<sub>a</sub> = RT(ln A &minus; ln k) / 1000 (1)<br>"
            "&bull; E<sub>a</sub> = 8.31 &times; 300 &times; (23.97 &minus; (&minus;5.03)) / 1000 = 72.3 (kJ mol<sup>&minus;1</sup>) (1)"
        ),
        "ms_extra": "M1 is for rearrangement of equation and factor of 1000 used correctly to convert J into kJ.", "ms_marks": "2",
    },
    {
        "qnum": "02.1", "specRef": "3.1.9", "marks": 1,
        "stem": "Draw a tangent to the curve in Figure 1 when the concentration of butadiene is 0.0120 mol dm-3.",
        "figures": ["fig-q2-fig1.jpg"], "crop_exclude_y": [[78, 575]],
        "ms_label": "02.1",
        "ms_ans": "Gradient / tangent drawn on graph at [butadiene] = 0.0120 mol dm<sup>&minus;3</sup>",
        "ms_extra": "Line must touch the curve at 0.012 but must not cross the curve.", "ms_marks": "1",
    },
    {
        "qnum": "02.2", "specRef": "3.1.9", "marks": 5,
        "stem": "Use the initial rate (4.57 x 10^-6 mol dm-3 s-1) and the rate from your tangent at 0.0120 mol dm-3 to justify that the order of reaction is 2 with respect to butadiene.",
        "figures": ["fig-q2-fig1.jpg"],
        "ms_label": "02.2",
        "ms_ans": (
            "<b>Stage 1: Rate at 0.0120 mol dm<sup>&minus;3</sup></b><br>"
            "&bull; Gradient = &minus;(0.0160 &minus; 0) / (7800 &minus; 0) = &minus;2.05 &times; 10<sup>&minus;6</sup> (1)<br>"
            "&bull; Rate = 2.05 &times; 10<sup>&minus;6</sup> (mol dm<sup>&minus;3</sup> s<sup>&minus;1</sup>) (1)<br>"
            "<b>Stage 2: Comparison of rates and concentrations</b><br>"
            "&bull; Initial rate / rate at 0.0120 = (4.57 &times; 10<sup>&minus;6</sup>) / (2.05 &times; 10<sup>&minus;6</sup>) = 2.23 (1)<br>"
            "&bull; Initial conc / conc at tangent = 0.018 / 0.012 = 1.5 (1)<br>"
            "<b>Stage 3: Deduction of order</b><br>"
            "&bull; If order is 2, rate should increase by factor of (1.5)<sup>2</sup> = 2.25 &asymp; 2.23, therefore 2nd order with respect to butadiene (1)"
        ),
        "ms_extra": "Extended response. Marking points in stage 2 can be in either order.", "ms_marks": "5",
    },
    {
        "qnum": "03.1", "specRef": "3.3.1", "marks": 1,
        "stem": "Give the IUPAC name for isooctane (Figure 2).",
        "figures": ["fig-q3-fig2.jpg"], "crop_exclude_y": [[78, 240]],
        "ms_label": "03.1",
        "ms_ans": "2,2,4-trimethylpentane",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "03.2", "specRef": "3.3.15", "marks": 1,
        "stem": "Deduce the number of peaks in the 13C NMR spectrum of isooctane.",
        "figures": ["fig-q3-fig2.jpg"],
        "ms_label": "03.2",
        "ms_ans": "<b>A</b> (5)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "03.3", "specRef": "3.3.2", "marks": 1,
        "stem": "Write an equation using molecular formulas for cracking one molecule of a C20 alkane to form isooctane, propene and ethene.",
        "figures": ["fig-q3-fig2.jpg"],
        "ms_label": "03.3",
        "ms_ans": "C<sub>20</sub>H<sub>42</sub> &rarr; C<sub>8</sub>H<sub>18</sub> + 2C<sub>3</sub>H<sub>6</sub> + 3C<sub>2</sub>H<sub>4</sub>",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "03.4", "specRef": "3.3.2", "marks": 1,
        "stem": "How do the products of the reaction in Question 3.3 show that the reaction is an example of thermal cracking?",
        "figures": ["fig-q3-fig2.jpg"],
        "ms_label": "03.4",
        "ms_ans": "Mainly alkenes formed",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "03.5", "specRef": "3.3.7", "marks": 2,
        "stem": "Deduce the number of monochloro isomers formed by isooctane and draw the structure of the monochloro isomer that exists as a pair of optical isomers.",
        "figures": ["fig-q3-fig2.jpg"],
        "ms_label": "03.5",
        "ms_ans": (
            "&bull; 4 (monochloro isomers) (1)<br>"
            "&bull; Structure of 3-chloro-2,2,4-trimethylpentane: (CH<sub>3</sub>)<sub>3</sub>C&minus;CH(Cl)&minus;CH(CH<sub>3</sub>)<sub>2</sub> (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "03.6", "specRef": "3.3.1", "marks": 1,
        "stem": "An isomer of isooctane reacts with chlorine to form only one monochloro compound. Draw the skeletal formula of this monochloro compound.",
        "figures": ["fig-q3-fig2.jpg"],
        "ms_label": "03.6",
        "ms_ans": "Skeletal formula of 1-chloro-2,2,3,3-tetramethylbutane: (CH<sub>3</sub>)<sub>3</sub>C&minus;C(CH<sub>3</sub>)<sub>2</sub>CH<sub>2</sub>Cl",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "03.7", "specRef": "3.1.1", "marks": 2,
        "stem": "A sample of monochlorooctane has 35Cl and 37Cl in the ratio 1.5 : 1.0. Calculate the Mr of this monochlorooctane.",
        "ms_label": "03.7",
        "ms_ans": (
            "&bull; C<sub>8</sub>H<sub>17</sub><sup>35</sup>Cl = 148.0 AND C<sub>8</sub>H<sub>17</sub><sup>37</sup>Cl = 150.0 (1)<br>"
            "&bull; M<sub>r</sub> = (1.5 &times; 148.0)/2.5 + (1.0 &times; 150.0)/2.5 = 148.8 (1)"
        ),
        "ms_extra": "Both M<sub>r</sub> values required for M1.", "ms_marks": "2",
    },
    {
        "qnum": "03.8", "specRef": "3.1.2", "marks": 3,
        "stem": "A chlorinated compound formed from isooctane contains 24.6% C and 2.56% H by mass. Calculate its molecular formula.",
        "ms_label": "03.8",
        "ms_ans": (
            "&bull; 24.6/12 : 2.56/1 : 72.8/35.5 = 2.05 : 2.56 : 2.05 &rarr; 1 : 1.25 : 1 (1)<br>"
            "&bull; Whole number ratio (&times; 4) = 4 : 5 : 4 (1)<br>"
            "&bull; Molecular formula = C<sub>8</sub>H<sub>10</sub>Cl<sub>8</sub> (1)"
        ),
        "ms_extra": "", "ms_marks": "3",
    },
    {
        "qnum": "04.1", "specRef": "3.3.1", "marks": 1,
        "stem": "Deduce the IUPAC name for alcohol A, (CH3)2CHCH(OH)CH3.",
        "ms_label": "04.1",
        "ms_ans": "3-methylbutan-2-ol",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "04.2", "specRef": "3.3.5", "marks": 1,
        "stem": "Draw the structure of the organic product B formed when A is oxidised with acidified potassium dichromate(VI).",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.2",
        "ms_ans": "(CH<sub>3</sub>)<sub>2</sub>CHCOCH<sub>3</sub> (3-methylbutan-2-one)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "04.3", "specRef": "3.3.5", "marks": 1,
        "stem": "Name the mechanism for the dehydration of A with concentrated sulfuric acid.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.3",
        "ms_ans": "Elimination",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "04.4", "specRef": "3.3.5", "marks": 2,
        "stem": "Draw the structures of the two isomeric alkenes C and D formed when A is dehydrated.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.4",
        "ms_ans": (
            "&bull; (CH<sub>3</sub>)<sub>2</sub>C=CHCH<sub>3</sub> (1)<br>"
            "&bull; (CH<sub>3</sub>)<sub>2</sub>CHCH=CH<sub>2</sub> (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "04.5", "specRef": "3.3.1", "marks": 1,
        "stem": "Name the type of structural isomerism shown by C and D.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.5",
        "ms_ans": "Position",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "04.6", "specRef": "3.1.3", "marks": 1,
        "stem": "List alcohol A, product B and isomer C in order of increasing boiling point.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.6",
        "ms_ans": "C B A",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "04.7", "specRef": "3.3.5", "marks": 1,
        "stem": "Draw the structure of the isomer of A that is not oxidised by acidified potassium dichromate(VI).",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.7",
        "ms_ans": "(CH<sub>3</sub>)<sub>2</sub>C(OH)CH<sub>2</sub>CH<sub>3</sub> (2-methylbutan-2-ol)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "04.8", "specRef": "3.3.5", "marks": 1,
        "stem": "Draw the structure of the isomer of A that cannot be dehydrated to form an alkene by reaction with concentrated sulfuric acid.",
        "figures": ["fig-q4-stem.jpg"],
        "ms_label": "04.8",
        "ms_ans": "(CH<sub>3</sub>)<sub>3</sub>CCH<sub>2</sub>OH (2,2-dimethylpropan-1-ol)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "05.1", "specRef": "3.3.13", "marks": 1,
        "stem": "Name the type of protein structure in Figure 3.",
        "figures": ["fig-q5-fig3.jpg"], "crop_exclude_y": [[78, 365]],
        "ms_label": "05.1",
        "ms_ans": "Secondary",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "05.2", "specRef": "3.3.13", "marks": 4,
        "stem": "Explain the origin of the interaction represented by the dotted lines in Figure 3.",
        "figures": ["fig-q5-fig3.jpg"],
        "ms_label": "05.2",
        "ms_ans": (
            "&bull; Nitrogen and oxygen are very electronegative (1)<br>"
            "&bull; Therefore, C=O and N&minus;H are polar (1)<br>"
            "&bull; Which results in the formation of a hydrogen bond between O and H (1)<br>"
            "&bull; In which a lone pair of electrons on an oxygen atom is strongly attracted to the &delta;+ H (1)"
        ),
        "ms_extra": "", "ms_marks": "4",
    },
    {
        "qnum": "06.1", "specRef": "3.3.7", "marks": 1,
        "stem": "Draw a separate circle around each of the asymmetric carbon atoms in the tripeptide in Figure 4.",
        "figures": ["fig-q6-fig4.jpg"], "crop_exclude_y": [[78, 278]],
        "ms_label": "06.1",
        "ms_ans": "Circle the CH(CH(OH)CH<sub>3</sub>) carbon in threonine AND the CH((CH<sub>2</sub>)<sub>4</sub>NH<sub>2</sub>) carbon in lysine (note: also CHOH carbon in threonine side chain? MS shows the two backbone chiral C atoms in threonine and lysine)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "06.2", "specRef": "3.3.13", "marks": 1,
        "stem": "Draw the zwitterion of glycine.",
        "figures": ["fig-q6-fig4.jpg"],
        "ms_label": "06.2",
        "ms_ans": "<sup>+</sup>H<sub>3</sub>N&minus;CH<sub>2</sub>&minus;COO<sup>&minus;</sup>",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "06.3", "specRef": "3.3.11", "marks": 1,
        "stem": "Draw the structure of the species formed when glycine reacts with an excess of bromomethane.",
        "figures": ["fig-q6-fig4.jpg"],
        "ms_label": "06.3",
        "ms_ans": "(CH<sub>3</sub>)<sub>3</sub>N<sup>+</sup>&minus;CH<sub>2</sub>&minus;COOH (Br<sup>&minus;</sup>)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "06.4", "specRef": "3.3.13", "marks": 1,
        "stem": "Deduce the IUPAC name of threonine.",
        "figures": ["fig-q6-fig4.jpg"],
        "ms_label": "06.4",
        "ms_ans": "2-amino-3-hydroxybutanoic acid",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "06.5", "specRef": "3.3.13", "marks": 1,
        "stem": "Draw the structure of the species formed by lysine at low pH.",
        "figures": ["fig-q6-fig4.jpg"],
        "ms_label": "06.5",
        "ms_ans": "<sup>+</sup>H<sub>3</sub>N&minus;CH((CH<sub>2</sub>)<sub>4</sub>NH<sub>3</sub><sup>+</sup>)&minus;COOH",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "07.1", "specRef": "3.3.4", "marks": 2,
        "stem": "Draw the structure of the monomer used to form polymer P (Figure 5) and name the type of polymerisation involved.",
        "figures": ["fig-q7-fig5.jpg"], "crop_exclude_y": [[78, 225]],
        "ms_label": "07.1",
        "ms_ans": (
            "&bull; CH(CH<sub>3</sub>)=C(CH<sub>3</sub>)Cl (1)<br>"
            "&bull; Addition (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "07.2", "specRef": "3.3.12", "marks": 2,
        "stem": "Draw the structures of two compounds that react together to form polymer Q (Figure 5).",
        "figures": ["fig-q7-fig5.jpg"],
        "ms_label": "07.2",
        "ms_ans": (
            "&bull; HO&minus;CH(CH<sub>3</sub>)&minus;CH(CH<sub>3</sub>)&minus;OH (1)<br>"
            "&bull; HOOC&minus;C(CH<sub>3</sub>)<sub>2</sub>&minus;CH<sub>2</sub>&minus;COOH OR ClOC&minus;C(CH<sub>3</sub>)<sub>2</sub>&minus;CH<sub>2</sub>&minus;COCl (1)"
        ),
        "ms_extra": "", "ms_marks": "2",
    },
    {
        "qnum": "07.3", "specRef": "3.3.12", "marks": 3,
        "stem": "Suggest an environmental advantage of polymer Q over polymer P and justify your answer.",
        "figures": ["fig-q7-fig5.jpg"],
        "ms_label": "07.3",
        "ms_ans": (
            "&bull; Q is biodegradable (1)<br>"
            "&bull; Polar C=O group or &delta;+ C in Q (but not in P) (1)<br>"
            "&bull; Therefore, can be attacked by nucleophiles (leading to breakdown) (1)"
        ),
        "ms_extra": "", "ms_marks": "3",
    },
    {
        "qnum": "08.1", "specRef": "3.3.13", "marks": 1,
        "stem": "State the name of the sugar molecule attached to bond X in DNA (Figure 6).",
        "figures": ["fig-q8-fig6.jpg"], "crop_exclude_y": [[78, 445]],
        "ms_label": "08.1",
        "ms_ans": "2-deoxyribose",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "08.2", "specRef": "3.3.13", "marks": 4,
        "stem": "Suggest which of bases A and B (Figure 7) pairs with guanine (Figure 6) when mRNA is synthesised, and explain how it forms a base pair.",
        "figures": ["fig-q8-fig6.jpg"],
        "ms_label": "08.2",
        "ms_ans": (
            "&bull; Base A (1)<br>"
            "&bull; Top N&minus;H forms hydrogen bond to lone pair on O of guanine (1)<br>"
            "&bull; The lone pair of electrons on N bonds to H&minus;N of guanine (1)<br>"
            "&bull; A lone pair of electrons on O bonds to lower H&minus;N of guanine (1)"
        ),
        "ms_extra": "If Base B stated, allow 1 mark only for response including hydrogen bonding. Allow all 4 marks for a correct diagram showing the hydrogen bonding.", "ms_marks": "4",
    },
    {
        "qnum": "08.3", "specRef": "3.3.13", "marks": 1,
        "stem": "On Figure 6, draw a ring round an atom in guanine that is likely to bond to platinum in cisplatin.",
        "figures": ["fig-q8-fig6.jpg"],
        "ms_label": "08.3",
        "ms_ans": "Either of the nitrogen atoms with a lone pair NOT involved in bonding to cytosine (i.e. ring N atoms with shown lone pairs)",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "08.4", "specRef": "3.3.13", "marks": 1,
        "stem": "Suggest one way in which cisplatin can be administered so that its side effect on healthy cells is minimised.",
        "ms_label": "08.4",
        "ms_ans": "Use in very small amounts / target the application to the tumour",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "09.1", "specRef": "3.3.9", "marks": 5,
        "stem": "Name and draw a mechanism for step 1 of Figure 8 using CH3COCl with phenylamine.",
        "figures": ["fig-q9-fig8.jpg"], "crop_exclude_y": [[75, 450]],
        "ms_label": "09.1",
        "ms_ans": (
            "&bull; (Nucleophilic) addition&minus;elimination (1)<br>"
            "&bull; M1: curly arrow from lone pair on N of C<sub>6</sub>H<sub>5</sub>NH<sub>2</sub> to C of C=O (1)<br>"
            "&bull; M2: curly arrow from C=O bond to O (1)<br>"
            "&bull; M3: tetrahedral intermediate with O<sup>&minus;</sup> and N<sup>+</sup>H<sub>2</sub>C<sub>6</sub>H<sub>5</sub> (1)<br>"
            "&bull; M4: curly arrow from lone pair on O<sup>&minus;</sup> back to C=O, curly arrow from C&minus;Cl to Cl, and curly arrow from N&minus;H bond to N (1)"
        ),
        "ms_extra": "Not electrophilic addition-elimination.", "ms_marks": "5",
    },
    {
        "qnum": "09.2", "specRef": "RP", "marks": 4,
        "stem": "Give reasons for each of the four practical steps in the recrystallisation purification of the step 1 product.",
        "ms_label": "09.2",
        "ms_ans": (
            "&bull; Minimum quantity of hot water: to ensure the hot solution would be saturated / crystals would form on cooling (1)<br>"
            "&bull; Cooled to room temperature: yield lower if warm / solubility higher if warm (1)<br>"
            "&bull; Crystals compressed in funnel: air passes through the sample not just round it (1)<br>"
            "&bull; Little cold water poured through: to wash away soluble impurities (1)"
        ),
        "ms_extra": "", "ms_marks": "4",
    },
    {
        "qnum": "09.3", "specRef": "RP", "marks": 2,
        "stem": "The melting point of the sample in Question 9.2 was slightly lower than a data-book value. Suggest the most likely impurity and an improvement to the method.",
        "ms_label": "09.3",
        "ms_ans": (
            "&bull; Water (1)<br>"
            "&bull; Press the sample of crystals between filter papers (or give the sample time to dry in air) (1)"
        ),
        "ms_extra": "Do not allow unreacted reagents for M1.", "ms_marks": "2",
    },
    {
        "qnum": "09.4", "specRef": "3.1.2", "marks": 3,
        "stem": "5.05 g of phenylamine gave 4.82 g of purified product in step 1 (Figure 8). Calculate the percentage yield.",
        "figures": ["fig-q9-fig8.jpg"],
        "ms_label": "09.4",
        "ms_ans": (
            "&bull; M<sub>r</sub> product = 135.0 (1)<br>"
            "&bull; Expected mass = 5.05 &times; (135.0 / 93.0) = 7.33 g (1)<br>"
            "&bull; Percentage yield = (4.82 / 7.33) &times; 100 = 65.75 = 65.8% (1)"
        ),
        "ms_extra": "Answer must be given to 3 significant figures.", "ms_marks": "3",
    },
    {
        "qnum": "09.5", "specRef": "3.3.10", "marks": 1,
        "stem": "Write an equation for the reaction of the nitrating intermediate (NO2+) in step 2 (Figure 8).",
        "figures": ["fig-q9-fig8.jpg"],
        "ms_label": "09.5",
        "ms_ans": "C<sub>6</sub>H<sub>5</sub>NHCOCH<sub>3</sub> + NO<sub>2</sub><sup>+</sup> &rarr; C<sub>6</sub>H<sub>4</sub>(NHCOCH<sub>3</sub>)NO<sub>2</sub> + H<sup>+</sup>",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "09.6", "specRef": "3.3.10", "marks": 1,
        "stem": "Name a mechanism for the reaction in step 2 (Figure 8).",
        "figures": ["fig-q9-fig8.jpg"],
        "ms_label": "09.6",
        "ms_ans": "Electrophilic substitution",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "09.7", "specRef": "3.3.9", "marks": 1,
        "stem": "Suggest the type of reaction occurring in step 3 (Figure 8).",
        "figures": ["fig-q9-fig8.jpg"],
        "ms_label": "09.7",
        "ms_ans": "Hydrolysis",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "09.8", "specRef": "3.3.11", "marks": 1,
        "stem": "Identify the reagents used in step 4 (Figure 8).",
        "figures": ["fig-q9-fig8.jpg"],
        "ms_label": "09.8",
        "ms_ans": "Sn/HCl",
        "ms_extra": "Ignore acid concentration; allow Fe/HCl.", "ms_marks": "1",
    },
    {
        "qnum": "10", "specRef": "3.3.15", "marks": 8,
        "stem": "Deduce the structure of compound R (C6H14O) by analysing the IR spectrum (Figure 9) and 1H NMR spectrum (Figure 10).",
        "figures": ["fig-q10-spectra.jpg"],
        "ms_label": "10",
        "ms_ans": (
            "&bull; M1 (IR): Absorption at 3360 cm<sup>&minus;1</sup> shows O&minus;H alcohol present (1)<br>"
            "&bull; M2 (NMR): 4 peaks indicates 4 different environments of hydrogen (1)<br>"
            "&bull; M3: Integration ratio 1.6 : 0.4 : 1.2 : 2.4 = 4 : 1 : 3 : 6 (1)<br>"
            "&bull; M4: Singlet (integ 1) must be caused by H in O&minus;H alcohol (1)<br>"
            "&bull; M5: Singlet (integ 3) must be due to a CH<sub>3</sub> group with no adjacent H (1)<br>"
            "&bull; M6: Quartet + triplet suggest CH<sub>2</sub>CH<sub>3</sub> group (1)<br>"
            "&bull; M7: Integration 4 and 6 indicates two equivalent CH<sub>2</sub>CH<sub>3</sub> groups (1)<br>"
            "&bull; M8: Structure: CH<sub>3</sub>&minus;C(OH)(CH<sub>2</sub>CH<sub>3</sub>)<sub>2</sub> (3-methylpentan-3-ol) (1)"
        ),
        "ms_extra": "Extended response. Deduction of correct structure without explanation scores max 4 marks.", "ms_marks": "8",
    },
    {
        "qnum": "11.1", "specRef": "3.3.8", "marks": 1,
        "stem": "Write an overall equation for the reduction of butanone using [H] to represent the reductant.",
        "ms_label": "11.1",
        "ms_ans": "CH<sub>3</sub>CH<sub>2</sub>COCH<sub>3</sub> + 2[H] &rarr; CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>3</sub>",
        "ms_extra": "", "ms_marks": "1",
    },
    {
        "qnum": "11.2", "specRef": "3.3.7", "marks": 6,
        "stem": "By considering the mechanism of the reaction of butanone with NaBH4, explain why the product has no effect on plane polarised light.",
        "ms_label": "11.2",
        "ms_ans": (
            "<b>Indicative chemistry content:</b><br>"
            "<b>Stage 1: Formation of product</b><br>"
            "&bull; Nucleophilic attack<br>"
            "&bull; Planar carbonyl group<br>"
            "&bull; H<sup>&minus;</sup> attacks from either side (stated or drawn)<br>"
            "<b>Stage 2: Nature of product</b><br>"
            "&bull; Product of step 1 shown (butan-2-ol)<br>"
            "&bull; Exists in two chiral forms (stated or drawn)<br>"
            "&bull; Equal amounts of each enantiomer / racemic mixture formed<br>"
            "<b>Stage 3: Optical activity</b><br>"
            "&bull; Optical isomers / enantiomers rotate the plane of polarised light equally in opposite directions<br>"
            "&bull; With a racemic / equal mixture the effects cancel"
        ),
        "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).", "ms_marks": "6",
    },
    {
        "qnum": "12.1", "specRef": "3.3.4", "marks": 1,
        "stem": "Suggest a reagent of the form HY which reacts with but-1-ene to form a saturated compound.",
        "ms_label": "12.1",
        "ms_ans": "HBr OR HCl OR H<sub>2</sub>SO<sub>4</sub>",
        "ms_extra": "Allow HI or HY.", "ms_marks": "1",
    },
    {
        "qnum": "12.2", "specRef": "3.3.4", "marks": 5,
        "stem": "Name and draw a mechanism for the reaction in Question 12.1.",
        "ms_label": "12.2",
        "ms_ans": (
            "&bull; Electrophilic addition (1)<br>"
            "&bull; M1: curly arrow from C=C double bond to H<sup>&delta;+</sup> of H&minus;Br (1)<br>"
            "&bull; M2: curly arrow from H&minus;Br bond to Br (1)<br>"
            "&bull; M3: secondary carbocation CH<sub>3</sub>&minus;C<sup>+</sup>H&minus;CH<sub>2</sub>CH<sub>3</sub> (1)<br>"
            "&bull; M4: curly arrow from lone pair on :Br<sup>&minus;</sup> to C<sup>+</sup>, forming CH<sub>3</sub>CHBrCH<sub>2</sub>CH<sub>3</sub> (1)"
        ),
        "ms_extra": "Allow consequential marking on acid in 12.1 and allow use of HY.", "ms_marks": "5",
    },
    {
        "qnum": "12.3", "specRef": "3.3.7", "marks": 3,
        "stem": "Explain how three isomeric products are formed when HY reacts with but-1-ene.",
        "ms_label": "12.3",
        "ms_ans": (
            "&bull; The major product exists as a pair of enantiomers (1)<br>"
            "&bull; The third isomer is 1-bromobutane (minor product) (1)<br>"
            "&bull; Because it is obtained via primary carbocation (1)"
        ),
        "ms_extra": "", "ms_marks": "3",
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

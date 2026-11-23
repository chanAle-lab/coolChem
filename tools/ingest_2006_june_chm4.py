"""
Ingestion script for 2006 June CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q6, Q7).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383083064_6e7b7914.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-june-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

# Extract table for 5(b)
doc = fitz.open(QP_PATH)
page12 = doc[11]
rect_t1 = fitz.Rect(70, 100, 510, 240)
pix_t1 = page12.get_pixmap(clip=rect_t1, dpi=200)
pix_t1.save(os.path.join(IMG_DIR, "fig-q5-table1.jpg"))

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2006-june-chm4-q1a",
        "question": "1(a)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.9"],
        "skills": ["recall"],
        "summary": "Write an equation for the formation of methyl propanoate from methanol and propanoic acid.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "CH<sub>3</sub>OH + CH<sub>3</sub>CH<sub>2</sub>COOH → CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>3</sub> + H<sub>2</sub>O", "Allow C<sub>2</sub>H<sub>5</sub>COOH / C<sub>2</sub>H<sub>5</sub>COOCH<sub>3</sub>", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm4-q1b",
        "question": "1(b)",
        "marks": 5,
        "page": 2,
        "topics": ["3.3.9"],
        "skills": ["mechanism"],
        "summary": "Name and outline a mechanism for the reaction between propanoyl chloride and methanol.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "Name of mechanism: (Nucleophilic) addition-elimination [NOT acylation] (1)<br><br>Mechanism (4):<br>M1: Curly arrow from lone pair on :O of CH<sub>3</sub>OH to carbonyl carbon of CH<sub>3</sub>CH<sub>2</sub>COCl<br>M2: Curly arrow from C=O double bond to oxygen<br>M3: Correct tetrahedral intermediate with O<sup>-</sup> and O<sup>+</sup>H(CH<sub>3</sub>)<br>M4: 3 curly arrows (lone pair on O<sup>-</sup> reforming C=O, loss of :Cl<sup>-</sup>, and loss of H<sup>+</sup> from O<sup>+</sup>-H)", "1 mark for (nucleophilic) addition-elimination<br>4 marks for mechanism:<br>M1: arrow from O of alcohol to C=O carbon<br>M2: arrow from C=O bond to O<br>M3: structure of tetrahedral intermediate<br>M4: 3 arrows for elimination and lone pairs<br>Ignore use of Cl<sup>-</sup> to remove H<sup>+</sup>", "5", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm4-q1c",
        "question": "1(c)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.9"],
        "skills": ["application"],
        "summary": "Draw the structure of propanoic anhydride.",
        "figures": [],
        "ms_rows": [
            ("1(c)", "CH<sub>3</sub>CH<sub>2</sub>COOCOCH<sub>2</sub>CH<sub>3</sub> OR (CH<sub>3</sub>CH<sub>2</sub>CO)<sub>2</sub>O", "Allow C<sub>2</sub>H<sub>5</sub> and -CO<sub>2</sub>-; allow displayed formula showing anhydride linkage", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm4-q1di",
        "question": "1(d)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.9"],
        "skills": ["evaluation"],
        "summary": "State one advantage of using propanoyl chloride rather than propanoic acid in the laboratory preparation of methyl propanoate.",
        "figures": [],
        "ms_rows": [
            ("1(d)(i)", "Faster / not reversible / bigger yield / purer product / no (acid) catalyst required", "Any 1 valid advantage", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm4-q1dii",
        "question": "1(d)(ii)",
        "marks": 1,
        "page": 2,
        "topics": ["3.3.9"],
        "skills": ["evaluation"],
        "summary": "State one advantage of using propanoic anhydride rather than propanoyl chloride.",
        "figures": [],
        "ms_rows": [
            ("1(d)(ii)", "Anhydride less easily hydrolysed OR reaction less violent / exothermic OR no corrosive / toxic HCl fumes formed / safer OR anhydride is cheaper", "Any 1 valid advantage", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm4-q1ei",
        "question": "1(e)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.3.1", "3.3.9"],
        "skills": ["application"],
        "summary": "Deduce the molecular formula of methyl benzoate.",
        "figures": [],
        "ms_rows": [
            ("1(e)(i)", "C<sub>8</sub>H<sub>8</sub>O<sub>2</sub>", "Credit C<sub>8</sub>H<sub>8</sub>O<sub>2</sub> only", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm4-q1eii",
        "question": "1(e)(ii)",
        "marks": 2,
        "page": 5,
        "topics": ["3.3.9", "3.3.10"],
        "skills": ["application"],
        "summary": "Draw the structures of two ester isomers of methyl benzoate that each contain a benzene ring.",
        "figures": [],
        "ms_rows": [
            ("1(e)(ii)", "Any two from:<br>1. Phenyl ethanoate: C<sub>6</sub>H<sub>5</sub>OCOCH<sub>3</sub><br>2. Benzyl methanoate: HCOOCH<sub>2</sub>C<sub>6</sub>H<sub>5</sub><br>3. Methyl 2-, 3- or 4-methylbenzoate: CH<sub>3</sub>C<sub>6</sub>H<sub>4</sub>COOCH<sub>3</sub> (or 2-, 3-, 4-methylphenyl methanoate: HCOOC<sub>6</sub>H<sub>4</sub>CH<sub>3</sub>)", "1 mark each for any two correct ester structures containing a benzene ring (allow -CO<sub>2</sub>- and C<sub>6</sub>H<sub>5</sub>)", "2", "AO1 / 3.3.9")
        ]
    },
    # Q2
    {
        "id": "2006-june-chm4-q2ai",
        "question": "2(a)(i)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "Predict and explain the effect of increasing pressure on the equilibrium yield of hydrogen in the reaction: CH4(g) + H2O(g) <=> CO(g) + 3H2(g).",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "Prediction: Yield decreases (or eqm moves to left)<br><br>Explanation:<br>Higher pressure gives lower yield / eqm opposes increase in pressure<br><br>Eqm shifts to reduce pressure / favours the side with fewer moles of gas (2 moles on left < 4 moles on right)", "M1: Yield decreases (if wrong no further marks in part (i))<br>M2: Higher pressure favours side with fewer moles<br>M3: 2 moles on left < 4 moles on right / eqm shifts to reduce pressure", "3", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm4-q2aii",
        "question": "2(a)(ii)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "Explain whether the reaction is endothermic or exothermic given that yield of hydrogen increases as temperature is raised.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "Prediction: Endothermic<br><br>Explanation:<br>Increase in temperature increases yield / eqm moves to right<br><br>Eqm shifts to reduce temperature / opposes increase in temperature / favours endothermic direction", "M1: Endothermic (if wrong no further marks in part (ii))<br>M2: Increase in temperature shifts eqm in endothermic direction<br>M3: System opposes temperature rise / shifts to right to absorb heat", "3", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm4-q2bi",
        "question": "2(b)(i)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.6"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of iodine and of hydrogen iodide at equilibrium.",
        "figures": [],
        "ms_rows": [
            ("2(b)(i)", "Moles of iodine (I<sub>2</sub>) = 0.023 mol<br><br>Moles of HI = 2 × (0.109 - 0.023) = 0.172 mol", "1 mark for moles of I<sub>2</sub> = 0.023<br>1 mark for moles of HI = 0.172<br>[If × 2 missed, max 1 in part (iv); If wrong no marks in (i)]", "2", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm4-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["recall"],
        "summary": "Write an expression for the equilibrium constant Kc for the reaction: H2(g) + I2(g) <=> 2HI(g).",
        "figures": [],
        "ms_rows": [
            ("2(b)(ii)", "<i>K</i><sub>c</sub> = [HI]<sup>2</sup> / ([H<sub>2</sub>][I<sub>2</sub>])", "Must use square brackets [ ]; penalise once in paper. If round brackets, penalise but mark on in (iv)", "1", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm4-q2biii",
        "question": "2(b)(iii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["explanation"],
        "summary": "Explain why the volume of the reaction container does not need to be known to calculate Kc.",
        "figures": [],
        "ms_rows": [
            ("2(b)(iii)", "Volume <i>V</i> cancels in the <i>K</i><sub>c</sub> expression OR equal number of moles / concentration terms on top and bottom of expression", "1 mark for <i>V</i> cancels / same number of moles on each side", "1", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm4-q2biv",
        "question": "2(b)(iv)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["calculation"],
        "summary": "Calculate the value of Kc for the dissociation of HI (or formation from elements).",
        "figures": [],
        "ms_rows": [
            ("2(b)(iv)", "<i>K</i><sub>c</sub> = (0.023 × 0.023) / (0.172)<sup>2</sup><br>= (0.023)<sup>2</sup> / (0.172)<sup>2</sup><br>= 0.0179 (or 1.79 × 10<sup>-2</sup> / allow 0.018)", "M1: Correct substitution of values<br>M2: 0.0179 or 1.79 × 10<sup>-2</sup> (conseq on (i); allow 0.018)", "2", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2006-june-chm4-q2bv",
        "question": "2(b)(v)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["calculation"],
        "summary": "Deduce the value of Kc for the reverse reaction (synthesis of HI).",
        "figures": [],
        "ms_rows": [
            ("2(b)(v)", "<i>K</i><sub>c</sub>' = 1 / <i>K</i><sub>c</sub> = 1 / 0.0179 = 55.9 (or 56)", "1 mark for 55.9 or 56 (conseq on 1 / answer to (iv))", "1", "AO2 / 3.1.6")
        ]
    },
    # Q3
    {
        "id": "2006-june-chm4-q3a",
        "question": "3(a)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Define pH and calculate the hydrogen ion concentration in an aqueous solution of pH 2.34.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "pH = -log<sub>10</sub>[H<sup>+</sup>]<br><br>[H<sup>+</sup>] = 10<sup>-2.34</sup> = 4.57 × 10<sup>-3</sup> mol dm<sup>-3</sup> (allow 4.6 × 10<sup>-3</sup>)", "1 mark for pH = -log[H<sup>+</sup>]<br>1 mark for 4.57 × 10<sup>-3</sup> [ignore units; ecf if [] wrong]", "2", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "Write an expression for the acid dissociation constant Ka of a weak monoprotic acid HX.",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "<i>K</i><sub>a</sub> = [H<sup>+</sup>][X<sup>-</sup>] / [HX]", "Allow HA; must have charges; do not accept [H<sup>+</sup>]<sup>2</sup>/[HX] for definition", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3bii",
        "question": "3(b)(ii)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the value of Ka for 0.150 mol dm-3 HX and deduce its units.",
        "figures": [],
        "ms_rows": [
            ("3(b)(ii)", "<i>K</i><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [HX] = (4.57 × 10<sup>-3</sup>)<sup>2</sup> / 0.150<br><br>= 1.39 × 10<sup>-4</sup> (allow 1.39 - 1.41 × 10<sup>-4</sup>)<br><br>Units = mol dm<sup>-3</sup>", "M1: Expression [H<sup>+</sup>]<sup>2</sup> / [HX] with numbers substituted<br>M2: 1.39 × 10<sup>-4</sup> (allow 1.39 - 1.41 × 10<sup>-4</sup>)<br>M3: Units = mol dm<sup>-3</sup><br>[If 4.6 × 10<sup>-3</sup> used, <i>K</i><sub>a</sub> = 1.41 × 10<sup>-4</sup>]", "3", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3biii",
        "question": "3(b)(iii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pKa of the acid HX.",
        "figures": [],
        "ms_rows": [
            ("3(b)(iii)", "p<i>K</i><sub>a</sub> = -log<sub>10</sub>(1.39 × 10<sup>-4</sup>) = 3.86", "1 mark for 3.86 (penalise dp < or > 2 in pH/pKa once in paper; 3.85 if 1.41 × 10<sup>-4</sup> used)", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3ci",
        "question": "3(c)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of sodium hydroxide in 30.0 cm3 of 0.480 mol dm-3 NaOH.",
        "figures": [],
        "ms_rows": [
            ("3(c)(i)", "Moles of NaOH = (30 × 0.480) / 1000 = 0.0144 mol (or 1.44 × 10<sup>-2</sup> mol)", "1 mark for 0.0144 / 1.44 × 10<sup>-2</sup>", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3cii",
        "question": "3(c)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of sulphuric acid in 18.0 cm3 of 0.350 mol dm-3 H2SO4.",
        "figures": [],
        "ms_rows": [
            ("3(c)(ii)", "Moles of H<sub>2</sub>SO<sub>4</sub> = (18 × 0.350) / 1000 = 0.0063 mol (or 6.3 × 10<sup>-3</sup> mol)", "1 mark for 0.0063 / 6.3 × 10<sup>-3</sup>", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3ciii",
        "question": "3(c)(iii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of excess sodium hydroxide remaining.",
        "figures": [],
        "ms_rows": [
            ("3(c)(iii)", "Moles of excess OH<sup>-</sup> = 0.0144 - 2(0.0063) = 1.80 × 10<sup>-3</sup> mol", "1 mark for (i) - 2(ii) = 1.80 × 10<sup>-3</sup> [if × 2 missed, CE]", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3civ",
        "question": "3(c)(iv)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the concentration of hydroxide ions in the resulting solution.",
        "figures": [],
        "ms_rows": [
            ("3(c)(iv)", "[OH<sup>-</sup>] = 1.80 × 10<sup>-3</sup> / (48 / 1000) = 0.0375 mol dm<sup>-3</sup> (or 0.038)", "1 mark for 0.0375 (or 0.038)", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2006-june-chm4-q3cv",
        "question": "3(c)(v)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH of the resulting solution at 25°C.",
        "figures": [],
        "ms_rows": [
            ("3(c)(v)", "[H<sup>+</sup>] = <i>K</i><sub>w</sub> / [OH<sup>-</sup>] = 10<sup>-14</sup> / 0.0375 = 2.66 × 10<sup>-13</sup> mol dm<sup>-3</sup> (or pOH = 1.426)<br><br>pH = -log<sub>10</sub>(2.66 × 10<sup>-13</sup>) = 12.57 (or 14 - 1.426 = 12.57 / 12.58)", "M1: <i>K</i><sub>w</sub> / [OH<sup>-</sup>] expression or pOH calculation<br>M2: pH = 12.57 (allow 12.58)<br>[If no attempt to use Kw or pOH lose both M1 and M2]", "2", "AO2 / 3.1.12")
        ]
    },
    # Q4
    {
        "id": "2006-june-chm4-q4ai",
        "question": "4(a)(i)",
        "marks": 2,
        "page": 10,
        "topics": ["3.3.4", "3.3.12"],
        "skills": ["recall"],
        "summary": "State the structure of but-2-ene and type of polymerisation it undergoes.",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "Structure: CH<sub>3</sub>CH=CHCH<sub>3</sub><br><br>Type of polymerisation: Addition (or radical)", "1 mark for CH<sub>3</sub>CH=CHCH<sub>3</sub><br>1 mark for addition / radical", "2", "AO1 / 3.3.4")
        ]
    },
    {
        "id": "2006-june-chm4-q4aii",
        "question": "4(a)(ii)",
        "marks": 5,
        "page": 10,
        "topics": ["3.3.5", "3.3.9", "3.3.12"],
        "skills": ["application"],
        "summary": "Deduce structures and IUPAC names of the diol and dicarboxylic acid forming the polyester, and state type of polymerisation.",
        "figures": [],
        "ms_rows": [
            ("4(a)(ii)", "Diol: CH<sub>3</sub>CH(OH)CH(OH)CH<sub>3</sub> (1)<br>Name: butane-2,3-diol (or 2,3-butanediol) (1)<br><br>Diacid: HOOC-CH(CH<sub>3</sub>)-CH(CH<sub>3</sub>)-COOH (1)<br>Name: 2,3-dimethylbutanedioic acid (1)<br><br>Type of polymerisation: Condensation (1)", "1 mark for diol structure<br>1 mark for butane-2,3-diol<br>1 mark for diacid structure (or 2,3-dimethylbutanodioyl chloride)<br>1 mark for 2,3-dimethylbutanedioic acid<br>1 mark for condensation polymerisation", "5", "AO1 / 3.3.12")
        ]
    },
    {
        "id": "2006-june-chm4-q4aiii",
        "question": "4(a)(iii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.3.9", "3.3.12"],
        "skills": ["recall"],
        "summary": "State a reagent that can be used to hydrolyse the polyester.",
        "figures": [],
        "ms_rows": [
            ("4(a)(iii)", "NaOH (aqueous) OR HCl (aqueous) (or Na<sub>2</sub>CO<sub>3</sub> / conc. H<sub>2</sub>SO<sub>4</sub> / HNO<sub>3</sub>)", "Allow aqueous alkali or aqueous strong acid [NOT pure water nor weak acids]", "1", "AO1 / 3.3.9")
        ]
    },
    {
        "id": "2006-june-chm4-q4b",
        "question": "4(b)",
        "marks": 2,
        "page": 11,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structures of the two isomeric dipeptides formed from alanine and serine.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "Dipeptide 1: H<sub>2</sub>N-CH(CH<sub>3</sub>)-CONH-CH(CH<sub>2</sub>OH)-COOH (alanyl-serine)<br><br>Dipeptide 2: H<sub>2</sub>N-CH(CH<sub>2</sub>OH)-CONH-CH(CH<sub>3</sub>)-COOH (seryl-alanine)", "1 mark for each dipeptide structure showing -CONH- peptide link (allow zwitterions; not repeating units)", "2", "AO1 / 3.3.13")
        ]
    },
    {
        "id": "2006-june-chm4-q4ci",
        "question": "4(c)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.3", "3.3.11"],
        "skills": ["application"],
        "summary": "Identify a halogenoalkane that can react with ammonia to form propylamine.",
        "figures": [],
        "ms_rows": [
            ("4(c)(i)", "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>Br (1-bromopropane) [allow -Cl, -I]", "Credit 1-bromopropane / 1-chloropropane / 1-iodopropane", "1", "AO1 / 3.3.3")
        ]
    },
    {
        "id": "2006-june-chm4-q4cii",
        "question": "4(c)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.3", "3.3.11"],
        "skills": ["application"],
        "summary": "Identify a nitrile that can be reduced to form propylamine.",
        "figures": [],
        "ms_rows": [
            ("4(c)(ii)", "CH<sub>3</sub>CH<sub>2</sub>CN (propanenitrile)", "Credit CH<sub>3</sub>CH<sub>2</sub>CN / propanenitrile (or ethyl cyanide)", "1", "AO1 / 3.3.11")
        ]
    },
    {
        "id": "2006-june-chm4-q4ciii",
        "question": "4(c)(iii)",
        "marks": 3,
        "page": 11,
        "topics": ["3.3.3", "3.3.11"],
        "skills": ["comparison", "explanation"],
        "summary": "Explain why reduction of the nitrile is a better method than reaction of the halogenoalkane with ammonia for preparing a pure sample of propylamine.",
        "figures": [],
        "ms_rows": [
            ("4(c)(iii)", "Reaction of haloalkane undergoes (nucleophilic) substitution (1)<br><br>Further substitution / reaction occurs to give a mixture of products (1)<br><br>One by-product: (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>)<sub>2</sub>NH OR (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>)<sub>3</sub>N OR (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>)<sub>4</sub>N<sup>+</sup>Br<sup>-</sup> (1)<br>(Reduction of nitrile gives only one / pure product)", "1 mark for nucleophilic substitution of haloalkane<br>1 mark for further substitution occurs / mixture formed<br>1 mark for structure of dipropylamine, tripropylamine, or tetrapropylammonium salt", "3", "AO1 / 3.3.11")
        ]
    },
    # Q5
    {
        "id": "2006-june-chm4-q5a",
        "question": "5(a)",
        "marks": 3,
        "page": 12,
        "topics": ["3.1.9"],
        "skills": ["calculation"],
        "summary": "Calculate the value of the rate constant k and deduce its units for the acid hydrolysis of methyl propanoate.",
        "figures": [],
        "ms_rows": [
            ("5(a)", "<i>k</i> = rate / ([CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>3</sub>][H<sup>+</sup>])<br>= (1.15 × 10<sup>-4</sup>) / (0.150 × 0.555)<br><br>= 1.38 × 10<sup>-3</sup> (allow 1.38 - 1.40 × 10<sup>-3</sup>)<br><br>Units: mol<sup>-1</sup> dm<sup>3</sup> s<sup>-1</sup>", "M1: <i>k</i> = rate / ([ester][H<sup>+</sup>])<br>M2: 1.38 × 10<sup>-3</sup> to 1.40 × 10<sup>-3</sup><br>M3: Units: mol<sup>-1</sup> dm<sup>3</sup> s<sup>-1</sup>", "3", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2006-june-chm4-q5b",
        "question": "5(b)",
        "marks": 1,
        "page": 12,
        "topics": ["3.1.9"],
        "skills": ["calculation"],
        "summary": "Calculate the initial rate of reaction when water is added so volume is doubled.",
        "figures": ["img/2006-june-chm4/fig-q5-table1.jpg"],
        "ms_rows": [
            ("5(b)", "Initial rate = <i>k</i> × (½ × 0.150) × (½ × 0.555) = ¼ × original rate<br>= ¼ × (1.15 × 10<sup>-4</sup>) = 2.88 × 10<sup>-5</sup> mol dm<sup>-3</sup> s<sup>-1</sup> (allow 2.87 - 2.91 × 10<sup>-5</sup>)", "1 mark for 2.88 × 10<sup>-5</sup> (allow 2.87 - 2.91 × 10<sup>-5</sup>; ignore units)", "1", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2006-june-chm4-q5c",
        "question": "5(c)",
        "marks": 3,
        "page": 12,
        "topics": ["3.1.9", "3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the initial pH of the reaction mixture in the third experiment at a different temperature.",
        "figures": [],
        "ms_rows": [
            ("5(c)", "[H<sup>+</sup>] = rate / (<i>k</i>[CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>3</sub>])<br>= (4.56 × 10<sup>-5</sup>) / (8.94 × 10<sup>-4</sup> × 0.123)<br>= 0.415 mol dm<sup>-3</sup> (or 0.4146)<br><br>pH = -log<sub>10</sub>(0.415) = 0.38 (or 0.39)", "M1: Rearranged expression [H<sup>+</sup>] = rate / (<i>k</i>[ester])<br>M2: [H<sup>+</sup>] = 0.415 mol dm<sup>-3</sup><br>M3: pH = 0.38 (allow 0.39; mark independently)", "3", "AO2 / 3.1.9")
        ]
    }
]

paper_id = "2006-june-chm4"
new_questions = []

for qd in QUESTIONS_DATA:
    qid = qd["id"]
    q_label = qd["question"]
    ms_img_rel = f"img/{paper_id}/ms_{qid.split('-')[-1]}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

    answers_list = []
    extra_list = []
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.3.9"
    for r in qd["ms_rows"]:
        prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
        answers_list.append(f"{prefix}{r[1]} ({r[3]})")
        if r[2]:
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
        "markscheme": [ms_img_rel]
    }
    new_questions.append(q_obj)

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    db = json.load(f)

db["questions"] = [q for q in db["questions"] if q.get("paper") != paper_id]
db["questions"].extend(new_questions)

with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully ingested {len(new_questions)} questions for {paper_id}. Total marks: {sum(q['marks'] for q in new_questions)}")

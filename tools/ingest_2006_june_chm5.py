"""
Ingestion script for 2006 June CHM5 (Section A only)
Excludes old-spec Section B essay questions (Q6, Q7, Q8, Q9).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383083059_3d319834.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2006-june-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

# Extract figures
doc = fitz.open(QP_PATH)
# fig-q2-graph.jpg on page 6 (index 5)
page6 = doc[5]
rect6 = fitz.Rect(80, 100, 480, 320)
pix6 = page6.get_pixmap(clip=rect6, dpi=200)
pix6.save(os.path.join(IMG_DIR, "fig-q2-graph.jpg"))

# fig-q5-table.jpg on page 11 (index 10)
page11 = doc[10]
rect11 = fitz.Rect(80, 95, 490, 260)
pix11 = page11.get_pixmap(clip=rect11, dpi=200)
pix11.save(os.path.join(IMG_DIR, "fig-q5-table.jpg"))

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2006-june-chm5-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 2,
        "topics": ["3.1.2", "3.2.5"],
        "skills": ["recall"],
        "summary": "Write an equation for the reaction between iron and hydrochloric acid.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "Fe + 2HCl → FeCl<sub>2</sub> + H<sub>2</sub><br>(or Fe + 2H<sup>+</sup> → Fe<sup>2+</sup> + H<sub>2</sub>)", "Allow ionic formulae; ignore state symbols", "1", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2006-june-chm5-q1aii",
        "question": "1(a)(ii)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the moles of hydrogen gas evolved using the ideal gas equation.",
        "figures": [],
        "ms_rows": [
            ("1(a)(ii)", "<i>pV</i> = <i>nRT</i>  =>  <i>n</i> = <i>pV</i> / <i>RT</i><br><br><i>n</i> = (110000 × 102 × 10<sup>-6</sup>) / (8.31 × 298)<br><br>= 4.53 × 10<sup>-3</sup> mol", "M1: <i>pV</i> = <i>nRT</i> or rearranged formula<br>M2: Correct numbers substituted with <i>p</i> in Pa and <i>V</i> in m<sup>3</sup><br>M3: 4.53 × 10<sup>-3</sup> mol (at least 3 sig. figs.; ignore units)", "3", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2006-june-chm5-q1aiii",
        "question": "1(a)(iii)",
        "marks": 2,
        "page": 4,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the mass of iron in the wire sample.",
        "figures": [],
        "ms_rows": [
            ("1(a)(iii)", "Moles of iron = 4.53 × 10<sup>-3</sup> mol<br><br>Mass of iron = 4.53 × 10<sup>-3</sup> × 55.8 = 0.253 g (or 0.254 g with 56)", "1 mark for moles of iron = moles H<sub>2</sub> (conseq on (a)(ii))<br>1 mark for mass = moles × <i>A</i><sub>r</sub> = 0.253 g", "2", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2006-june-chm5-q1aiv",
        "question": "1(a)(iv)",
        "marks": 1,
        "page": 4,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the percentage of iron in the steel wire.",
        "figures": [],
        "ms_rows": [
            ("1(a)(iv)", "% iron = (0.253 / 0.263) × 100 = 96.1% (or 96%)", "1 mark for 96.1% (conseq on mass of iron; do not allow >= 100%)", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2006-june-chm5-q1bi",
        "question": "1(b)(i)",
        "marks": 3,
        "page": 4,
        "topics": ["3.1.7", "3.2.5"],
        "skills": ["recall"],
        "summary": "Write half-equations for Fe2+ oxidation and dichromate reduction, and deduce the overall redox equation.",
        "figures": [],
        "ms_rows": [
            ("1(b)(i)", "Fe<sup>2+</sup> → Fe<sup>3+</sup> + e<sup>-</sup><br><br>Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> + 14H<sup>+</sup> + 6e<sup>-</sup> → 2Cr<sup>3+</sup> + 7H<sub>2</sub>O<br><br>Overall: Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> + 14H<sup>+</sup> + 6Fe<sup>2+</sup> → 2Cr<sup>3+</sup> + 7H<sub>2</sub>O + 6Fe<sup>3+</sup>", "1 mark for Fe<sup>2+</sup> half-equation<br>1 mark for dichromate half-equation<br>1 mark for overall balanced redox equation", "3", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2006-june-chm5-q1bii",
        "question": "1(b)(ii)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.2", "3.1.7"],
        "skills": ["calculation"],
        "summary": "Calculate the volume of 0.0200 mol dm-3 potassium dichromate(VI) required to react with the Fe2+ solution.",
        "figures": [],
        "ms_rows": [
            ("1(b)(ii)", "Moles of dichromate = moles Fe<sup>2+</sup> / 6 = (4.53 × 10<sup>-3</sup>) / 6 = 7.55 × 10<sup>-4</sup> mol<br><br>Volume = (moles / conc) × 1000 = (7.55 × 10<sup>-4</sup> / 0.0200) × 1000<br><br><i>V</i> = 37.75 cm<sup>3</sup> (allow 37.7 to 37.8 cm<sup>3</sup>)", "M1: Moles dichromate = moles Fe<sup>2+</sup> / 6<br>M2: Volume method: moles / conc<br>M3: 37.75 cm<sup>3</sup> (allow 37.7 - 37.8; penalise wrong units)", "3", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2006-june-chm5-q1biii",
        "question": "1(b)(iii)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.7", "3.2.5"],
        "skills": ["evaluation"],
        "summary": "Explain why potassium manganate(VII) cannot be used instead of potassium dichromate(VI) in this titration.",
        "figures": [],
        "ms_rows": [
            ("1(b)(iii)", "KMnO<sub>4</sub> will also oxidise (or react with) Cl<sup>-</sup> (or chloride / HCl)", "1 mark for KMnO<sub>4</sub> oxidises chloride ions", "1", "AO1 / 3.1.7")
        ]
    },
    # Q2
    {
        "id": "2006-june-chm5-q2a",
        "question": "2(a)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.8"],
        "skills": ["recall"],
        "summary": "Suggest why the entropy of water is zero at 0 K.",
        "figures": ["img/2006-june-chm5/fig-q2-graph.jpg"],
        "ms_rows": [
            ("2(a)", "Particles are in a maximum state of order (or perfect order / perfect crystal / minimum disorder / no disorder; entropy is zero at 0 K by definition)", "1 mark for maximum state of order / perfectly ordered crystal", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2006-june-chm5-q2b",
        "question": "2(b)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.8"],
        "skills": ["recall"],
        "summary": "State what change of state occurs at temperature T1.",
        "figures": ["img/2006-june-chm5/fig-q2-graph.jpg"],
        "ms_rows": [
            ("2(b)", "Ice melts (or melting / fusion / changes from solid to liquid)", "1 mark for melting / solid to liquid", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2006-june-chm5-q2c",
        "question": "2(c)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.8"],
        "skills": ["explanation"],
        "summary": "Explain why the entropy change ΔS at temperature T2 is larger than that at T1.",
        "figures": ["img/2006-june-chm5/fig-q2-graph.jpg"],
        "ms_rows": [
            ("2(c)", "Increase in disorder is much greater when boiling / converting liquid to gas than when melting solid to liquid<br><br>Gas has much greater disorder / more random arrangement of particles than liquid", "1 mark for increase in disorder<br>1 mark for much bigger increase at T2 (boiling: liquid to gas) than T1 (melting)", "2", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2006-june-chm5-q2di",
        "question": "2(d)(i)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.8"],
        "skills": ["calculation"],
        "summary": "Calculate the enthalpy change of vaporisation per mole of water.",
        "figures": [],
        "ms_rows": [
            ("2(d)(i)", "Moles of water = 1.53 / 18 = 0.085 mol<br><br>Heat change per mole Δ<i>H</i> = 3.49 / 0.085 = 41.1 kJ mol<sup>-1</sup> (allow 41 to 41.1)", "1 mark for moles of water = 0.085 mol<br>1 mark for Δ<i>H</i> = 41.1 kJ mol<sup>-1</sup> [penalise -41; penalise wrong units]", "2", "AO2 / 3.1.8")
        ]
    },
    {
        "id": "2006-june-chm5-q2dii",
        "question": "2(d)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.8"],
        "skills": ["recall"],
        "summary": "State the relationship between ΔG, ΔH, and ΔS.",
        "figures": [],
        "ms_rows": [
            ("2(d)(ii)", "Δ<i>G</i> = Δ<i>H</i> - <i>T</i>Δ<i>S</i>", "1 mark for Δ<i>G</i> = Δ<i>H</i> - <i>T</i>Δ<i>S</i>", "1", "AO1 / 3.1.8")
        ]
    },
    {
        "id": "2006-june-chm5-q2diii",
        "question": "2(d)(iii)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.8"],
        "skills": ["calculation"],
        "summary": "Calculate the entropy change of vaporisation of water at its boiling point (373 K).",
        "figures": [],
        "ms_rows": [
            ("2(d)(iii)", "At equilibrium (boiling point), Δ<i>G</i> = 0  =>  Δ<i>H</i> = <i>T</i>Δ<i>S</i>  =>  Δ<i>S</i> = Δ<i>H</i> / <i>T</i><br><br>Δ<i>S</i> = 41.1 / 373 = 0.110 kJ K<sup>-1</sup> mol<sup>-1</sup> (or 110 J K<sup>-1</sup> mol<sup>-1</sup>)<br><br>Units: kJ K<sup>-1</sup> mol<sup>-1</sup> (or J K<sup>-1</sup> mol<sup>-1</sup>)", "M1: Δ<i>S</i> = Δ<i>H</i> / <i>T</i><br>M2: 0.110 (or 110)<br>M3: Correct units (kJ K<sup>-1</sup> mol<sup>-1</sup> or J K<sup>-1</sup> mol<sup>-1</sup>)", "3", "AO2 / 3.1.8")
        ]
    },
    # Q3
    {
        "id": "2006-june-chm5-q3a",
        "question": "3(a)",
        "marks": 3,
        "page": 8,
        "topics": ["3.2.5", "3.2.6"],
        "skills": ["recall"],
        "summary": "Identify precipitate A, gas B, and write an equation for the reaction of [Cr(H2O)6]3+ with sodium carbonate.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "Precipitate A: Cr(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub> (or Cr(OH)<sub>3</sub>)<br><br>Gas B: CO<sub>2</sub><br><br>Equation: 2[Cr(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + 3CO<sub>3</sub><sup>2-</sup> → 2[Cr(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub>] + 3CO<sub>2</sub> + 3H<sub>2</sub>O<br>(or gives 2Cr(OH)<sub>3</sub> + 3CO<sub>2</sub> + 9H<sub>2</sub>O)", "1 mark for precipitate A<br>1 mark for gas B (CO<sub>2</sub>)<br>1 mark for balanced equation", "3", "AO1 / 3.2.6")
        ]
    },
    {
        "id": "2006-june-chm5-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 8,
        "topics": ["3.2.5", "3.2.6"],
        "skills": ["recall"],
        "summary": "Identify a reagent to dissolve green precipitate A to form a green solution.",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "NaOH (aqueous) OR KOH (aqueous)", "Credit NaOH / KOH (excess)", "1", "AO1 / 3.2.6")
        ]
    },
    {
        "id": "2006-june-chm5-q3bii",
        "question": "3(b)(ii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.7", "3.2.5"],
        "skills": ["recall"],
        "summary": "State the oxidation state of chromium in chromate(VI) ions.",
        "figures": [],
        "ms_rows": [
            ("3(b)(ii)", "+6 (or +VI / 6)", "Credit +6 or 6 or +VI", "1", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2006-june-chm5-q3biii",
        "question": "3(b)(iii)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.7", "3.2.5", "3.2.6"],
        "skills": ["recall"],
        "summary": "Identify an oxidising agent to convert Cr(III) to chromate(VI) in alkaline solution and write an oxidation half-equation.",
        "figures": [],
        "ms_rows": [
            ("3(b)(iii)", "Oxidising agent: H<sub>2</sub>O<sub>2</sub> (hydrogen peroxide) [or Na<sub>2</sub>O<sub>2</sub> / BaO<sub>2</sub>]<br><br>Half-equation: [Cr(OH)<sub>6</sub>]<sup>3-</sup> + 2OH<sup>-</sup> → CrO<sub>4</sub><sup>2-</sup> + 4H<sub>2</sub>O + 3e<sup>-</sup><br>(or [Cr(OH)<sub>6</sub>]<sup>3-</sup> → CrO<sub>4</sub><sup>2-</sup> + 2H<sub>2</sub>O + 2H<sup>+</sup> + 3e<sup>-</sup>)", "1 mark for H<sub>2</sub>O<sub>2</sub><br>1 mark for balanced half-equation", "2", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2006-june-chm5-q3ci",
        "question": "3(c)(i)",
        "marks": 3,
        "page": 9,
        "topics": ["3.2.5"],
        "skills": ["application"],
        "summary": "Draw the structure of the complex ion formed when [Cr(H2O)6]3+ reacts with 1,2-diaminoethane.",
        "figures": [],
        "ms_rows": [
            ("3(c)(i)", "Structure showing octahedral Cr<sup>3+</sup> coordinated by 3 bidentate H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> (en) ligands through N atoms, with overall 3+ charge", "1 mark for at least one H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> correctly bonded via N<br>1 mark for 6-coordination with 3 en ligands<br>1 mark for 3+ charge [mark independently]", "3", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2006-june-chm5-q3cii",
        "question": "3(c)(ii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.4", "3.2.5"],
        "skills": ["explanation"],
        "summary": "Explain why the enthalpy change for this ligand substitution reaction is close to zero.",
        "figures": [],
        "ms_rows": [
            ("3(c)(ii)", "Same (or similar) type of bonds broken and made (Cr-N vs Cr-O, or coordinate bonds)<br><br>Same number of coordinate bonds broken and made (6 bonds broken and 6 made / coordination number unchanged)", "1 mark for same/similar type of bonds broken and made<br>1 mark for same number of bonds broken and made", "2", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2006-june-chm5-q3ciii",
        "question": "3(c)(iii)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.8", "3.2.5"],
        "skills": ["explanation"],
        "summary": "Explain why this ligand substitution reaction occurs despite ΔH being close to zero.",
        "figures": [],
        "ms_rows": [
            ("3(c)(iii)", "Entropy change (Δ<i>S</i>) is positive / increase in disorder (1)<br><br>Because there are more product particles (4 particles: 1 complex + 3 en -> 1 complex + 6 H<sub>2</sub>O = 7 particles) than reactant particles (chelate effect) (1)", "1 mark for positive entropy change / increase in entropy<br>1 mark for increase in number of moles/particles in solution (chelate effect)", "2", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2006-june-chm5-q3d",
        "question": "3(d)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.7", "3.2.5"],
        "skills": ["recall"],
        "summary": "Identify the chromium-containing complex formed by reduction with zinc/acid and state its role in redox reactions.",
        "figures": [],
        "ms_rows": [
            ("3(d)", "Complex: [Cr(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> (or Cr<sup>2+</sup>(aq))<br><br>Role: Reducing agent (or electron donor)", "1 mark for [Cr(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup><br>1 mark for reducing agent [mark independently]", "2", "AO1 / 3.2.5")
        ]
    },
    {
        "id": "2006-june-chm5-q3ei",
        "question": "3(e)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.2.5", "3.3.5", "3.3.8"],
        "skills": ["recall"],
        "summary": "Identify the organic product formed when acidified potassium dichromate(VI) reacts with ethanol under distillation.",
        "figures": [],
        "ms_rows": [
            ("3(e)(i)", "Ethanal (or CH<sub>3</sub>CHO) [not CH<sub>3</sub>COH]", "Credit ethanal / CH<sub>3</sub>CHO", "1", "AO1 / 3.3.8")
        ]
    },
    {
        "id": "2006-june-chm5-q3eii",
        "question": "3(e)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.2.5", "3.3.5", "3.3.9"],
        "skills": ["recall"],
        "summary": "Identify the organic product formed when acidified potassium dichromate(VI) reacts with ethanol under reflux.",
        "figures": [],
        "ms_rows": [
            ("3(e)(ii)", "Ethanoic acid (or CH<sub>3</sub>COOH)", "Credit ethanoic acid / CH<sub>3</sub>COOH", "1", "AO1 / 3.3.9")
        ]
    },
    # Q4
    {
        "id": "2006-june-chm5-q4ai",
        "question": "4(a)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.10"],
        "skills": ["recall"],
        "summary": "Write an expression for Kp for the equilibrium: X(g) + 3Y(g) <=> 2Z(g).",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "<i>K</i><sub>p</sub> = (<i>p</i><sub>Z</sub>)<sup>2</sup> / ((<i>p</i><sub>X</sub>)(<i>p</i><sub>Y</sub>)<sup>3</sup>)", "Penalise use of square brackets [ ]; allow round brackets ( )", "1", "AO1 / 3.1.10")
        ]
    },
    {
        "id": "2006-june-chm5-q4aii",
        "question": "4(a)(ii)",
        "marks": 3,
        "page": 10,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the partial pressures of X and Y at equilibrium.",
        "figures": [],
        "ms_rows": [
            ("4(a)(ii)", "Partial pressure of X = (22 - 6) / 4 = 4 MPa (or 4.0 MPa)<br><br>Partial pressure of Y = 3 × 4.0 = 12 MPa (or 12.0 MPa)", "1 mark for partial pressure of X = 4 MPa<br>1 mark for Y = 3 × X (method)<br>1 mark for partial pressure of Y = 12 MPa", "3", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2006-june-chm5-q4aiii",
        "question": "4(a)(iii)",
        "marks": 2,
        "page": 10,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the value of Kp and deduce its units.",
        "figures": [],
        "ms_rows": [
            ("4(a)(iii)", "<i>K</i><sub>p</sub> = (6.0)<sup>2</sup> / (4.0 × 12.0<sup>3</sup>) = 36 / 6912 = 5.21 × 10<sup>-3</sup><br><br>Units: MPa<sup>-2</sup> (allow Pa<sup>-2</sup> or kPa<sup>-2</sup> matching pressure unit)", "1 mark for 5.21 × 10<sup>-3</sup> (conseq on (a)(ii))<br>1 mark for MPa<sup>-2</sup>", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2006-june-chm5-q4b",
        "question": "4(b)",
        "marks": 2,
        "page": 10,
        "topics": ["3.1.6", "3.1.10"],
        "skills": ["evaluation"],
        "summary": "State reasons why higher pressures and lower temperatures are not used commercially.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "High pressure is expensive (energy costs to compress gas, high cost of thick-walled plant / safety risk)<br><br>Rate of reaction is too slow at lower temperatures", "1 mark for high pressure expensive / high plant costs<br>1 mark for reaction rate is too slow at low temp", "2", "AO1 / 3.1.6")
        ]
    },
    # Q5
    {
        "id": "2006-june-chm5-q5ai",
        "question": "5(a)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.11"],
        "skills": ["recall"],
        "summary": "Identify the most powerful reducing agent in the table.",
        "figures": ["img/2006-june-chm5/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(a)(i)", "Fe<sup>2+</sup>", "Credit Fe<sup>2+</sup> only", "1", "AO1 / 3.1.11")
        ]
    },
    {
        "id": "2006-june-chm5-q5aii",
        "question": "5(a)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.11"],
        "skills": ["recall"],
        "summary": "Identify the most powerful oxidising agent in the table.",
        "figures": ["img/2006-june-chm5/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(a)(ii)", "F<sub>2</sub>O", "Credit F<sub>2</sub>O only", "1", "AO1 / 3.1.11")
        ]
    },
    {
        "id": "2006-june-chm5-q5aiii",
        "question": "5(a)(iii)",
        "marks": 2,
        "page": 11,
        "topics": ["3.1.11"],
        "skills": ["recall"],
        "summary": "Identify all species in the table that will reduce ozone to oxygen in acidic solution.",
        "figures": ["img/2006-june-chm5/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(a)(iii)", "Fe<sup>2+</sup> AND Cl<sup>-</sup>", "1 mark for Fe<sup>2+</sup><br>1 mark for Cl<sup>-</sup><br>[Apply list principle if more than two answers]", "2", "AO1 / 3.1.11")
        ]
    },
    {
        "id": "2006-june-chm5-q5bi",
        "question": "5(b)(i)",
        "marks": 2,
        "page": 11,
        "topics": ["3.1.11"],
        "skills": ["calculation"],
        "summary": "Deduce the e.m.f. of the cell: Pt|Fe2+,Fe3+||BrO3-,Br2|Pt.",
        "figures": ["img/2006-june-chm5/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(b)(i)", "e.m.f. = <i>E</i>(rhs) - <i>E</i>(lhs) = 1.52 - 0.77 = +0.75 V", "1 mark for formula: <i>E</i>(rhs) - <i>E</i>(lhs)<br>1 mark for +0.75 V (0.75 scores both marks)", "2", "AO2 / 3.1.11")
        ]
    },
    {
        "id": "2006-june-chm5-q5bii",
        "question": "5(b)(ii)",
        "marks": 1,
        "page": 11,
        "topics": ["3.1.11"],
        "skills": ["recall"],
        "summary": "Write a half-equation for the reaction occurring at the negative electrode of this cell.",
        "figures": ["img/2006-june-chm5/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(b)(ii)", "Fe<sup>2+</sup> → Fe<sup>3+</sup> + e<sup>-</sup>", "1 mark for Fe<sup>2+</sup> → Fe<sup>3+</sup> + e<sup>-</sup>", "1", "AO1 / 3.1.11")
        ]
    },
    {
        "id": "2006-june-chm5-q5biii",
        "question": "5(b)(iii)",
        "marks": 3,
        "page": 11,
        "topics": ["3.1.11"],
        "skills": ["explanation"],
        "summary": "Deduce and explain what change in concentration of Fe3+ would cause the e.m.f. to increase.",
        "figures": ["img/2006-june-chm5/fig-q5-table.jpg"],
        "ms_rows": [
            ("5(b)(iii)", "Change in concentration: Decrease [Fe<sup>3+</sup>]<br><br>Explanation:<br>Equilibrium Fe<sup>3+</sup> + e<sup>-</sup> <=> Fe<sup>2+</sup> shifts to the left (or reaction shifts in favour of more Fe<sup>3+</sup> / more electrons)<br><br>Electrode potential for Fe<sup>3+</sup>/Fe<sup>2+</sup> becomes less positive (decreases)", "M1: Decrease (if increase CE = 0)<br>M2: Equilibrium shifts to left to replace Fe<sup>3+</sup> / forms more electrons<br>M3: Electrode potential for Fe<sup>3+</sup>/Fe<sup>2+</sup> becomes less positive / decreases", "3", "AO1 / 3.1.11")
        ]
    }
]

paper_id = "2006-june-chm5"
new_questions = []

for qd in QUESTIONS_DATA:
    qid = qd["id"]
    q_label = qd["question"]
    ms_img_rel = f"img/{paper_id}/ms_{qid.split('-')[-1]}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

    answers_list = []
    extra_list = []
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.8"
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

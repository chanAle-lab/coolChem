import os
import sys
import json
import fitz  # PyMuPDF
from PIL import Image

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-june-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003706_b9ecaf08.pdf"
MS_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003708_687a6c26.pdf"

doc_qp = fitz.open(QP_PATH)

# Extract figures
# 1. Q2 curves on page 6 (0-indexed 5)
p6 = doc_qp[5]
r_curves = fitz.Rect(120, 140, 480, 560)
pix = p6.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=r_curves)
pix.save(os.path.join(IMG_DIR, "fig-q2-curves.jpg"))

# 2. Q3 scheme on page 8 (0-indexed 7)
p8 = doc_qp[7]
r_q3 = fitz.Rect(70, 90, 520, 240)
pix = p8.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=r_q3)
pix.save(os.path.join(IMG_DIR, "fig-q3-scheme.jpg"))

# 3. Q4 IR on page 11 (0-indexed 10)
p11 = doc_qp[10]
r_q4 = fitz.Rect(70, 110, 520, 400)
pix = p11.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=r_q4)
pix.save(os.path.join(IMG_DIR, "fig-q4-ir.jpg"))

# 4. Q5 scheme on page 12 (0-indexed 11)
p12 = doc_qp[11]
r_q5 = fitz.Rect(180, 130, 440, 270)
pix = p12.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=r_q5)
pix.save(os.path.join(IMG_DIR, "fig-q5-scheme.jpg"))

questions_data = [
    # Q1 (15 marks total)
    {
        "id": "2005-june-chm4-q1a",
        "question": "1(a)",
        "marks": 2,
        "page": 2,
        "summary": "Name ester A and write equation for its reaction with aqueous sodium hydroxide.",
        "description": "Name ester A (propyl methanoate) and write equation for its reaction with aqueous sodium hydroxide.",
        "spec_ref": "3.3.10",
        "answers_html": "propyl methanoate<br>HCOOCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> + OH<sup>-</sup> &rarr; HCOO<sup>-</sup> + C<sub>3</sub>H<sub>7</sub>OH<br><em>OR</em><br>HCOOC<sub>3</sub>H<sub>7</sub> + NaOH &rarr; HCOONa + C<sub>3</sub>H<sub>7</sub>OH",
        "extra_html": "1 mark for name<br>1 mark for equation"
    },
    {
        "id": "2005-june-chm4-q1b",
        "question": "1(b)",
        "marks": 3,
        "page": 2,
        "summary": "Deduce orders of reaction with respect to A and NaOH, and calculate initial rate in Experiment 4.",
        "description": "Deduce orders of reaction with respect to A and NaOH from rate data table, and calculate initial rate in Experiment 4.",
        "spec_ref": "3.1.9",
        "answers_html": "Order wrt A = 1<br>Order wrt NaOH = 1<br>Initial rate in Exp 4 = 2.4 &times; 10<sup>-3</sup> (mol dm<sup>-3</sup> s<sup>-1</sup>)",
        "extra_html": "1 mark for order wrt A<br>1 mark for order wrt NaOH<br>1 mark for rate calculation"
    },
    {
        "id": "2005-june-chm4-q1ci",
        "question": "1(c)(i)",
        "marks": 1,
        "page": 2,
        "summary": "Write rate equation under new conditions of high sodium hydroxide concentration.",
        "description": "Write rate equation under new conditions where reaction is first order in A and pseudo-zero order in NaOH.",
        "spec_ref": "3.1.9",
        "answers_html": "Rate = <em>k</em>[A]<br><em>OR</em><br>Rate = <em>k</em>[A][NaOH]<sup>0</sup>",
        "extra_html": "Penalise missing square brackets but mark on.<br>Penalise k<sub>a</sub> or k<sub>w</sub>."
    },
    {
        "id": "2005-june-chm4-q1cii",
        "question": "1(c)(ii)",
        "marks": 3,
        "page": 5,
        "summary": "Calculate value of rate constant k under new conditions and state its units.",
        "description": "Calculate value of rate constant k under new conditions (k = rate / [A]) and state its units.",
        "spec_ref": "3.1.9",
        "answers_html": "<em>k</em> = (9.0 &times; 10<sup>-3</sup>) / 0.020<br>= <strong>0.45</strong><br>Units: <strong>s<sup>-1</sup></strong>",
        "extra_html": "1 mark for expression/working<br>1 mark for 0.45<br>1 mark for s<sup>-1</sup>"
    },
    {
        "id": "2005-june-chm4-q1ciii",
        "question": "1(c)(iii)",
        "marks": 1,
        "page": 5,
        "summary": "Suggest why reaction appears zero order with respect to NaOH under new conditions.",
        "description": "Suggest why order with respect to NaOH appears zero under new conditions (large excess of OH-).",
        "spec_ref": "3.1.9",
        "answers_html": "(Large) excess of OH<sup>-</sup> / [OH<sup>-</sup>] is effectively constant<br><em>OR</em><br>[A] is the limiting factor",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q1di",
        "question": "1(d)(i)",
        "marks": 2,
        "page": 5,
        "summary": "Draw structure and name the product distilled off from alkaline hydrolysis of triester.",
        "description": "Draw structure and name the product distilled off from alkaline hydrolysis of glyceryl tristearate (glycerol).",
        "spec_ref": "3.3.10",
        "answers_html": "Structure: CH<sub>2</sub>OH&ndash;CHOH&ndash;CH<sub>2</sub>OH<br>Name: <strong>propane-1,2,3-triol</strong> <em>or</em> <strong>glycerol</strong>",
        "extra_html": "1 mark for correct structure<br>1 mark for name"
    },
    {
        "id": "2005-june-chm4-q1dii",
        "question": "1(d)(ii)",
        "marks": 2,
        "page": 5,
        "summary": "Give formula of product left in distillation flask and a use for it.",
        "description": "Give formula of product left in distillation flask (sodium stearate) and a use for it.",
        "spec_ref": "3.3.10",
        "answers_html": "Formula: <strong>CH<sub>3</sub>(CH<sub>2</sub>)<sub>16</sub>COONa</strong> (or C<sub>17</sub>H<sub>35</sub>COONa)<br>Use: <strong>soap</strong> (allow with detergent)",
        "extra_html": "1 mark for formula (not just anion, penalise Na shown covalently bonded)<br>1 mark for use"
    },

    # Q2 (13 marks total)
    {
        "id": "2005-june-chm4-q2ai",
        "question": "2(a)(i)",
        "marks": 3,
        "page": 6,
        "figures": ["img/2005-june-chm4/fig-q2-curves.jpg"],
        "summary": "Select titration curve produced by ammonia to HCl, ethanoic acid to NaOH, and NaOH to HCl.",
        "description": "Select titration curves A, B, C, D produced by adding weak base to strong acid, weak acid to strong base, and strong base to strong acid.",
        "spec_ref": "3.1.12",
        "answers_html": "Ammonia to 25 cm<sup>3</sup> HCl: <strong>B</strong><br>Ethanoic acid to 25 cm<sup>3</sup> NaOH: <strong>C</strong><br>Sodium hydroxide to 25 cm<sup>3</sup> HCl: <strong>A</strong>",
        "extra_html": "1 mark each"
    },
    {
        "id": "2005-june-chm4-q2aii",
        "question": "2(a)(ii)",
        "marks": 1,
        "page": 7,
        "figures": ["img/2005-june-chm4/fig-q2-curves.jpg"],
        "summary": "Select indicator suitable for titration of curve A but not curve B.",
        "description": "Select indicator suitable for titration of curve A (strong acid - strong base) but not curve B (strong acid - weak base).",
        "spec_ref": "3.1.12",
        "answers_html": "<strong>cresolphthalein</strong> <em>OR</em> <strong>thymolphthalein</strong>",
        "extra_html": "1 mark (pH range 8.2-9.8 or 9.3-10.5 falls on vertical section of A but not B)"
    },
    {
        "id": "2005-june-chm4-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 7,
        "summary": "Write an expression for the term pH.",
        "description": "Write an expression for the term pH (-log[H+]).",
        "spec_ref": "3.1.12",
        "answers_html": "pH = <strong>&ndash;log[H<sup>+</sup>]</strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q2bii",
        "question": "2(b)(ii)",
        "marks": 3,
        "page": 7,
        "summary": "Calculate concentration of KOH solution of pH 11.90 at 25°C.",
        "description": "Calculate concentration of KOH solution of pH 11.90 at 25°C using Kw.",
        "spec_ref": "3.1.12",
        "answers_html": "[H<sup>+</sup>] = 10<sup>-11.90</sup> = 1.259 &times; 10<sup>-12</sup> mol dm<sup>-3</sup> (or pOH = 14 &ndash; 11.90 = 2.10)<br>[OH<sup>-</sup>] = <em>K</em><sub>w</sub> / [H<sup>+</sup>] = 1.00 &times; 10<sup>-14</sup> / 1.259 &times; 10<sup>-12</sup><br>= <strong>7.94 &times; 10<sup>-3</sup></strong> mol dm<sup>-3</sup> (allow 7.9 &times; 10<sup>-3</sup>)",
        "extra_html": "1 mark for [H<sup>+</sup>] or pOH<br>1 mark for [OH<sup>-</sup>] expression<br>1 mark for answer"
    },
    {
        "id": "2005-june-chm4-q2ci",
        "question": "2(c)(i)",
        "marks": 3,
        "page": 7,
        "summary": "Calculate pH of 0.117 mol dm-3 propanoic acid solution.",
        "description": "Calculate pH of 0.117 mol dm-3 propanoic acid solution using Ka = 1.35 x 10-5 mol dm-3.",
        "spec_ref": "3.1.12",
        "answers_html": "<em>K</em><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [HA]<br>[H<sup>+</sup>] = &radic;(1.35 &times; 10<sup>-5</sup> &times; 0.117) = 1.257 &times; 10<sup>-3</sup> mol dm<sup>-3</sup><br>pH = &ndash;log(1.257 &times; 10<sup>-3</sup>) = <strong>2.90</strong>",
        "extra_html": "1 mark for expression for [H<sup>+</sup>]<br>1 mark for [H<sup>+</sup>] value<br>1 mark for pH to 2 d.p."
    },
    {
        "id": "2005-june-chm4-q2cii",
        "question": "2(c)(ii)",
        "marks": 2,
        "page": 7,
        "summary": "Calculate pH of equimolar propanoate buffer mixture.",
        "description": "Calculate pH of buffer mixture formed by adding equal volumes of 0.117 mol dm-3 sodium propanoate and propanoic acid.",
        "spec_ref": "3.1.12",
        "answers_html": "At half-neutralisation / equimolar buffer, [A<sup>-</sup>] = [HA], so <em>K</em><sub>a</sub> = [H<sup>+</sup>] (or pH = p<em>K</em><sub>a</sub>)<br>pH = &ndash;log(1.35 &times; 10<sup>-5</sup>) = <strong>4.87</strong>",
        "extra_html": "1 mark for recognizing Ka = [H+] / pH = pKa<br>1 mark for 4.87 (penalise 1 d.p. once)"
    },

    # Q3 (14 marks total)
    {
        "id": "2005-june-chm4-q3a",
        "question": "3(a)",
        "marks": 5,
        "page": 8,
        "figures": ["img/2005-june-chm4/fig-q3-scheme.jpg"],
        "summary": "Name and outline mechanism for nucleophilic addition of HCN to propanal in Step 1.",
        "description": "Name and outline mechanism for nucleophilic addition of HCN to propanal in Step 1.",
        "spec_ref": "3.3.8",
        "answers_html": "Name of mechanism: <strong>nucleophilic addition</strong> (1)<br><br>Mechanism (4 marks):<br>&bull; M1: Lone pair on :CN<sup>-</sup> attacks carbonyl carbon of CH<sub>3</sub>CH<sub>2</sub>CHO<br>&bull; M2: Arrow from C=O double bond onto oxygen<br>&bull; M3: Correct intermediate structure CH<sub>3</sub>CH<sub>2</sub>CH(CN)O<sup>-</sup><br>&bull; M4: Lone pair on O<sup>-</sup> attacks H<sup>+</sup> (or H&ndash;CN)",
        "extra_html": "1 mark for name<br>4 marks for mechanism"
    },
    {
        "id": "2005-june-chm4-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 8,
        "figures": ["img/2005-june-chm4/fig-q3-scheme.jpg"],
        "summary": "Name compound Q formed in Step 2.",
        "description": "Name compound Q (2-hydroxybutanoic acid) formed by hydrolysis of hydroxynitrile in Step 2.",
        "spec_ref": "3.3.9",
        "answers_html": "<strong>2-hydroxybutanoic acid</strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q3bii",
        "question": "3(b)(ii)",
        "marks": 3,
        "page": 8,
        "figures": ["img/2005-june-chm4/fig-q3-scheme.jpg"],
        "summary": "Give structures of two stereoisomers formed by dehydration of Q and name type of stereoisomerism.",
        "description": "Give structures of two stereoisomers (E- and Z-but-2-enoic acid) formed by dehydration of Q and name type of stereoisomerism.",
        "spec_ref": "3.3.3",
        "answers_html": "Structures:<br><em>trans / E</em>: CH<sub>3</sub> and COOH on opposite sides across C=C<br><em>cis / Z</em>: CH<sub>3</sub> and COOH on same side across C=C<br><br>Type: <strong>geometric(al)</strong> <em>OR</em> <strong>cis-trans</strong> (allow E-Z)",
        "extra_html": "2 marks for both correct structures<br>1 mark for geometric / cis-trans"
    },
    {
        "id": "2005-june-chm4-q3ci",
        "question": "3(c)(i)",
        "marks": 1,
        "page": 9,
        "summary": "Draw repeating unit of the biodegradable polymer PHB.",
        "description": "Draw repeating unit of biodegradable polyester PHB from 3-hydroxybutanoic acid.",
        "spec_ref": "3.3.12",
        "answers_html": "<strong>&ndash;[O&ndash;CH(CH<sub>3</sub>)&ndash;CH<sub>2</sub>&ndash;CO]&ndash;</strong>",
        "extra_html": "1 mark (trailing bonds needed, ignore brackets or n, one unit only)"
    },
    {
        "id": "2005-june-chm4-q3cii",
        "question": "3(c)(ii)",
        "marks": 1,
        "page": 9,
        "summary": "Suggest why polymer PHB is biodegradable.",
        "description": "Suggest why polyester PHB is biodegradable (ester link can be hydrolysed by acid/base/microorganisms).",
        "spec_ref": "3.3.12",
        "answers_html": "Can be <strong>hydrolysed</strong> (ester bond broken by acid / base / nucleophiles / water / microorganisms)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q3di",
        "question": "3(d)(i)",
        "marks": 1,
        "page": 9,
        "summary": "Draw structure of zwitterion formed by amino acid R.",
        "description": "Draw structure of zwitterion formed by 2-aminobutanoic acid.",
        "spec_ref": "3.3.13",
        "answers_html": "CH<sub>3</sub>CH<sub>2</sub>CH(NH<sub>3</sub><sup>+</sup>)COO<sup>-</sup>",
        "extra_html": "1 mark (allow -NH3+ and -COO-)"
    },
    {
        "id": "2005-june-chm4-q3dii",
        "question": "3(d)(ii)",
        "marks": 1,
        "page": 9,
        "summary": "Draw structure of major organic product when excess R reacts with bromomethane.",
        "description": "Draw structure of major organic product when excess amino acid R reacts with bromomethane (mono-methylation).",
        "spec_ref": "3.3.11",
        "answers_html": "CH<sub>3</sub>CH<sub>2</sub>CH(NHCH<sub>3</sub>)COOH (or zwitterion form)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q3diii",
        "question": "3(d)(iii)",
        "marks": 1,
        "page": 9,
        "summary": "Name mechanism of reaction between R and bromomethane.",
        "description": "Name mechanism of reaction between amine group of R and bromomethane (nucleophilic substitution).",
        "spec_ref": "3.3.11",
        "answers_html": "<strong>nucleophilic substitution</strong>",
        "extra_html": "1 mark"
    },

    # Q4 (9 marks total)
    {
        "id": "2005-june-chm4-q4ai",
        "question": "4(a)(i)",
        "marks": 1,
        "page": 10,
        "summary": "Deduce feature of W from singlet peak at delta = 2.18.",
        "description": "Deduce feature of W from proton NMR singlet peak of area 3 at delta = 2.18 (CH3CO-).",
        "spec_ref": "3.3.15",
        "answers_html": "<strong>CH<sub>3</sub>C=O</strong> (or RCOCH<sub>3</sub> / methyl ketone)",
        "extra_html": "1 mark (or description in words, ignore trailing bonds)"
    },
    {
        "id": "2005-june-chm4-q4aii",
        "question": "4(a)(ii)",
        "marks": 1,
        "page": 10,
        "summary": "Deduce feature of W from singlet peak at delta = 3.33.",
        "description": "Deduce feature of W from proton NMR singlet peak of area 3 at delta = 3.33 (CH3O-).",
        "spec_ref": "3.3.15",
        "answers_html": "<strong>CH<sub>3</sub>&ndash;O</strong> (or ROCH<sub>3</sub> / methoxy group)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q4aiii",
        "question": "4(a)(iii)",
        "marks": 1,
        "page": 10,
        "summary": "Deduce feature of W from two triplet peaks.",
        "description": "Deduce feature of W from two triplet peaks in NMR (-CH2CH2- group).",
        "spec_ref": "3.3.15",
        "answers_html": "<strong>&ndash;CH<sub>2</sub>CH<sub>2</sub>&ndash;</strong> (or two adjacent methylene groups)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q4aiv",
        "question": "4(a)(iv)",
        "marks": 1,
        "page": 10,
        "summary": "Deduce structure of isomer W.",
        "description": "Deduce structure of isomer W from NMR data: 4-methoxybutan-2-one.",
        "spec_ref": "3.3.15",
        "answers_html": "<strong>CH<sub>3</sub>COCH<sub>2</sub>CH<sub>2</sub>OCH<sub>3</sub></strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q4bi",
        "question": "4(b)(i)",
        "marks": 1,
        "page": 11,
        "figures": ["img/2005-june-chm4/fig-q4-ir.jpg"],
        "summary": "Deduce functional group from broad IR absorption centred on 3000 cm-1 in X.",
        "description": "Deduce functional group from broad IR absorption centred on 3000 cm-1 in X (O-H in carboxylic acid).",
        "spec_ref": "3.3.15",
        "answers_html": "<strong>O&ndash;H in carboxylic acids</strong> (or (carboxylic) acid present)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q4bii",
        "question": "4(b)(ii)",
        "marks": 1,
        "page": 11,
        "figures": ["img/2005-june-chm4/fig-q4-ir.jpg"],
        "summary": "Deduce structure of X given NMR spectrum with two peaks in 9:1 ratio.",
        "description": "Deduce structure of X given NMR spectrum with two peaks in 9:1 ratio: 2,2-dimethylpropanoic acid.",
        "spec_ref": "3.3.15",
        "answers_html": "<strong>(CH<sub>3</sub>)<sub>3</sub>CCOOH</strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q4c",
        "question": "4(c)",
        "marks": 3,
        "page": 11,
        "summary": "Identify reagents and observations to distinguish between hydroxy-ketone isomers Y and Z.",
        "description": "Identify reagents and observations to distinguish between secondary and tertiary alcohol isomers Y and Z.",
        "spec_ref": "3.3.4",
        "answers_html": "Reagents: <strong>acidified potassium dichromate(VI)</strong> (K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> / H<sup>+</sup>) <em>OR</em> acidified KMnO<sub>4</sub><br>Observation with Y (tertiary alcohol): <strong>no reaction / remains orange</strong><br>Observation with Z (secondary alcohol): <strong>orange to green</strong> (or purple to colourless with KMnO<sub>4</sub>)",
        "extra_html": "1 mark for reagents<br>1 mark for observation with Y<br>1 mark for observation with Z"
    },

    # Q5 (9 marks total)
    {
        "id": "2005-june-chm4-q5a",
        "question": "5(a)",
        "marks": 3,
        "page": 12,
        "figures": ["img/2005-june-chm4/fig-q5-scheme.jpg"],
        "summary": "Name mechanism and give reagents for nitration of methylbenzene in Step 1.",
        "description": "Name mechanism and give reagents for nitration of methylbenzene to 4-nitromethylbenzene in Step 1.",
        "spec_ref": "3.3.10",
        "answers_html": "Mechanism: <strong>electrophilic substitution</strong><br>Reagents: <strong>conc. HNO<sub>3</sub></strong> and <strong>conc. H<sub>2</sub>SO<sub>4</sub></strong>",
        "extra_html": "1 mark for mechanism<br>1 mark for conc HNO3<br>1 mark for conc H2SO4 (missing 'conc' on either/both scores 1 for acids)"
    },
    {
        "id": "2005-june-chm4-q5b",
        "question": "5(b)",
        "marks": 2,
        "page": 12,
        "figures": ["img/2005-june-chm4/fig-q5-scheme.jpg"],
        "summary": "Give reagents and equation for reduction of nitroarene to aryl amine in Step 2.",
        "description": "Give reagents and equation using [H] for reduction of 4-nitromethylbenzene to 4-methylphenylamine in Step 2.",
        "spec_ref": "3.3.11",
        "answers_html": "Reagent(s): <strong>Sn / HCl</strong> <em>OR</em> <strong>Fe / HCl</strong> (or H<sub>2</sub> / Ni)<br>Equation: CH<sub>3</sub>C<sub>6</sub>H<sub>4</sub>NO<sub>2</sub> + 6[H] &rarr; CH<sub>3</sub>C<sub>6</sub>H<sub>4</sub>NH<sub>2</sub> + 2H<sub>2</sub>O",
        "extra_html": "1 mark for reagent(s)<br>1 mark for balanced equation"
    },
    {
        "id": "2005-june-chm4-q5c",
        "question": "5(c)",
        "marks": 1,
        "page": 12,
        "figures": ["img/2005-june-chm4/fig-q5-scheme.jpg"],
        "summary": "Give m/z value of major peak in methylbenzene mass spectrum not in E or F.",
        "description": "Give m/z value of major peak in methylbenzene mass spectrum (molecular ion 92 or tropylium ion 91 or phenyl 77).",
        "spec_ref": "3.3.14",
        "answers_html": "<strong>92</strong> <em>OR</em> <strong>91</strong> <em>OR</em> <strong>77</strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm4-q5d",
        "question": "5(d)",
        "marks": 1,
        "page": 13,
        "summary": "Draw structure of species formed by 4-methylphenylamine in excess hydrochloric acid.",
        "description": "Draw structure of quaternary/protonated species (CH3C6H4NH3+) formed by F in excess HCl.",
        "spec_ref": "3.3.11",
        "answers_html": "<strong>CH<sub>3</sub>&ndash;C<sub>6</sub>H<sub>4</sub>&ndash;NH<sub>3</sub><sup>+</sup></strong> (or salt with Cl<sup>-</sup>)",
        "extra_html": "1 mark (allow -NH3+)"
    },
    {
        "id": "2005-june-chm4-q5e",
        "question": "5(e)",
        "marks": 2,
        "page": 13,
        "summary": "Draw structures of monosubstituted benzene isomers G and H.",
        "description": "Draw structures of primary amine G (benzylamine) and secondary amine H (N-methylaniline).",
        "spec_ref": "3.3.11",
        "answers_html": "G (primary amine): <strong>C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>NH<sub>2</sub></strong> (phenylmethanamine / benzylamine)<br>H (secondary amine): <strong>C<sub>6</sub>H<sub>5</sub>NHCH<sub>3</sub></strong> (N-methylphenylamine)",
        "extra_html": "1 mark for structure G<br>1 mark for structure H"
    }
]

print(f"Ingesting {len(questions_data)} questions for June 2005 CHM4...")
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Remove any existing 2005-june-chm4 questions
db['questions'] = [q for q in db['questions'] if q['paper'] != '2005-june-chm4']

for item in questions_data:
    q_id = item['id']
    ms_img_rel = f"img/2005-june-chm4/ms_{q_id.split('-')[-1]}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
    q_img_rel = f"img/2005-june-chm4/q_{q_id.split('-')[-1]}.jpg"

    render_official_markscheme_image(
        question_label=item['question'],
        answers_html=item['answers_html'],
        extra_html=item['extra_html'],
        marks=item['marks'],
        spec_ref=item['spec_ref'],
        output_path=ms_img_abs
    )

    q_entry = {
        "id": item["id"],
        "paper": "2005-june-chm4",
        "question": item["question"],
        "marks": item["marks"],
        "summary": item["summary"],
        "description": item["description"],
        "topic": item["spec_ref"],
        "tags": ["CHM4", "AQA", "A-Level"],
        "page": item["page"],
        "image": q_img_rel,
        "markscheme": ms_img_rel
    }
    if "figures" in item:
        q_entry["figures"] = item["figures"]

    db['questions'].append(q_entry)
    print(f"Processed {item['id']} ({item['question']}) - {item['marks']} marks")

with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully ingested {len(questions_data)} questions for 2005-june-chm4!")

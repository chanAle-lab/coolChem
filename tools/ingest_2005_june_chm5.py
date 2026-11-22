import os
import sys
import json
import fitz  # PyMuPDF
from PIL import Image

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-june-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003708_7ca682eb.pdf"
MS_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003705_a67f1479.pdf"

doc_qp = fitz.open(QP_PATH)

# Extract figures
# 1. Q1 scheme on page 2 (0-indexed 1)
p2 = doc_qp[1]
r_q1 = fitz.Rect(100, 160, 500, 480)
pix = p2.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=r_q1)
pix.save(os.path.join(IMG_DIR, "fig-q1-scheme.jpg"))

# 2. Q2 pH curve on page 6 (0-indexed 5)
p6 = doc_qp[5]
r_q2 = fitz.Rect(180, 150, 460, 390)
pix = p6.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=r_q2)
pix.save(os.path.join(IMG_DIR, "fig-q2-curve.jpg"))

# 3. Q4 table on page 10 (0-indexed 9)
p10 = doc_qp[9]
r_q4 = fitz.Rect(120, 130, 480, 330)
pix = p10.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=r_q4)
pix.save(os.path.join(IMG_DIR, "fig-q4-table.jpg"))

questions_data = [
    # Q1 (17 marks total)
    {
        "id": "2005-june-chm5-q1a",
        "question": "1(a)",
        "marks": 3,
        "page": 2,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "Deduce oxidation states of N in Cu(NO3)2 and NO2, and identify oxidation product.",
        "description": "Deduce oxidation states of nitrogen in Cu(NO3)2 and in NO2, and identify product formed by oxidation in thermal decomposition.",
        "spec_ref": "3.1.7",
        "answers_html": "Oxidation state of N in Cu(NO<sub>3</sub>)<sub>2</sub>: <strong>+5</strong><br>Oxidation state of N in NO<sub>2</sub>: <strong>+4</strong><br>Oxidation product: <strong>oxygen</strong> (O<sub>2</sub>)",
        "extra_html": "1 mark each"
    },
    {
        "id": "2005-june-chm5-q1b",
        "question": "1(b)",
        "marks": 2,
        "page": 2,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "Identify copper species in solution A and state its shape.",
        "description": "Identify copper-containing aqua ion present in solution A ([Cu(H2O)6]2+) and state its octahedral shape.",
        "spec_ref": "3.2.5",
        "answers_html": "Copper-containing species: <strong>[Cu(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup></strong><br>Shape: <strong>octahedral</strong>",
        "extra_html": "1 mark for species<br>1 mark for octahedral"
    },
    {
        "id": "2005-june-chm5-q1ci",
        "question": "1(c)(i)",
        "marks": 2,
        "page": 5,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "Identify pale blue precipitate B and write equation for its formation.",
        "description": "Identify pale blue precipitate B (Cu(OH)2 / [Cu(H2O)4(OH)2]) and write equation for reaction with aqueous ammonia.",
        "spec_ref": "3.2.5",
        "answers_html": "Precipitate B: <strong>Cu(H<sub>2</sub>O)<sub>4</sub>(OH)<sub>2</sub></strong> (or Cu(OH)<sub>2</sub> / copper(II) hydroxide)<br>Equation: [Cu(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 2NH<sub>3</sub> &rarr; Cu(H<sub>2</sub>O)<sub>4</sub>(OH)<sub>2</sub> + 2NH<sub>4</sub><sup>+</sup><br><em>OR</em><br>[Cu(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 2OH<sup>-</sup> &rarr; Cu(H<sub>2</sub>O)<sub>4</sub>(OH)<sub>2</sub> + 2H<sub>2</sub>O",
        "extra_html": "1 mark for identity<br>1 mark for equation"
    },
    {
        "id": "2005-june-chm5-q1cii",
        "question": "1(c)(ii)",
        "marks": 1,
        "page": 5,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "State how NH3 behaves as a Brønsted-Lowry base in forming precipitate B.",
        "description": "State how NH3 behaves as a Brønsted-Lowry base (accepts a proton / H+).",
        "spec_ref": "3.1.12",
        "answers_html": "NH<sub>3</sub> <strong>accepts a proton</strong> (H<sup>+</sup>)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q1di",
        "question": "1(d)(i)",
        "marks": 3,
        "page": 5,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "Identify copper species in solution C, its colour, and equation from precipitate B.",
        "description": "Identify deep blue complex [Cu(NH3)4(H2O)2]2+ in solution C and write equation for ligand substitution from precipitate B.",
        "spec_ref": "3.2.5",
        "answers_html": "Identity: <strong>[Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup></strong><br>Colour: <strong>deep blue</strong><br>Equation: Cu(H<sub>2</sub>O)<sub>4</sub>(OH)<sub>2</sub> + 4NH<sub>3</sub> &rarr; [Cu(NH<sub>3</sub>)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub>]<sup>2+</sup> + 2H<sub>2</sub>O + 2OH<sup>-</sup>",
        "extra_html": "1 mark for identity<br>1 mark for colour<br>1 mark for equation"
    },
    {
        "id": "2005-june-chm5-q1dii",
        "question": "1(d)(ii)",
        "marks": 1,
        "page": 5,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "State how NH3 behaves as a Lewis base in forming complex C.",
        "description": "State how NH3 behaves as a Lewis base (donates a lone pair of electrons to Cu2+).",
        "spec_ref": "3.2.5",
        "answers_html": "NH<sub>3</sub> is an <strong>electron pair donor</strong> (forms co-ordinate / dative covalent bonds)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q1e",
        "question": "1(e)",
        "marks": 3,
        "page": 5,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "Identify copper species in solution D, and state its colour and shape.",
        "description": "Identify tetrachlorocuprate(II) complex in solution D ([CuCl4]2-), yellow-green colour, and tetrahedral shape.",
        "spec_ref": "3.2.5",
        "answers_html": "Identity: <strong>[CuCl<sub>4</sub>]<sup>2-</sup></strong><br>Colour: <strong>yellow-green</strong> (or yellow / green)<br>Shape: <strong>tetrahedral</strong>",
        "extra_html": "1 mark each"
    },
    {
        "id": "2005-june-chm5-q1fi",
        "question": "1(f)(i)",
        "marks": 1,
        "page": 5,
        "summary": "Give electron arrangement of Cu+ ion.",
        "description": "Give electronic configuration of copper(I) ion: 1s2 2s2 2p6 3s2 3p6 3d10.",
        "spec_ref": "3.1.1",
        "answers_html": "<strong>1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>6</sup> 3d<sup>10</sup></strong> (or [Ar] 3d<sup>10</sup>)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q1fii",
        "question": "1(f)(ii)",
        "marks": 1,
        "page": 5,
        "figures": ["img/2005-june-chm5/fig-q1-scheme.jpg"],
        "summary": "Deduce role of copper metal in forming [CuCl4]3- from solution D.",
        "description": "Deduce role of copper metal in reducing Cu(II) in [CuCl4]2- to Cu(I) in [CuCl4]3- (reducing agent / reductant).",
        "spec_ref": "3.1.7",
        "answers_html": "Role of Cu: <strong>reducing agent</strong> (or reductant)",
        "extra_html": "1 mark"
    },

    # Q2 (12 marks total)
    {
        "id": "2005-june-chm5-q2a",
        "question": "2(a)",
        "marks": 2,
        "page": 6,
        "figures": ["img/2005-june-chm5/fig-q2-curve.jpg"],
        "summary": "Calculate concentration of weak acid HA from titration curve data.",
        "description": "Calculate concentration of HA from titration endpoint with 18.2 cm3 of 0.150 M NaOH.",
        "spec_ref": "3.1.12",
        "answers_html": "Moles of NaOH = 0.0182 &times; 0.150 = 2.73 &times; 10<sup>-3</sup> mol<br>Moles of HA = 2.73 &times; 10<sup>-3</sup> mol in 25.0 cm<sup>3</sup><br>[HA] = (2.73 &times; 10<sup>-3</sup>) / 0.025 = <strong>0.109</strong> mol dm<sup>-3</sup>",
        "extra_html": "1 mark for moles NaOH<br>1 mark for concentration of HA"
    },
    {
        "id": "2005-june-chm5-q2bi",
        "question": "2(b)(i)",
        "marks": 1,
        "page": 6,
        "summary": "Write an expression for the acid dissociation constant Ka for HA.",
        "description": "Write expression for Ka for weak monoprotic acid HA.",
        "spec_ref": "3.1.12",
        "answers_html": "<em>K</em><sub>a</sub> = <strong>[H<sup>+</sup>][A<sup>-</sup>] / [HA]</strong>",
        "extra_html": "1 mark (not [H+]2/[HA])"
    },
    {
        "id": "2005-june-chm5-q2bii",
        "question": "2(b)(ii)",
        "marks": 1,
        "page": 6,
        "summary": "Write an expression for pKa.",
        "description": "Write expression for pKa: -log Ka.",
        "spec_ref": "3.1.12",
        "answers_html": "p<em>K</em><sub>a</sub> = <strong>&ndash;log <em>K</em><sub>a</sub></strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q2biii",
        "question": "2(b)(iii)",
        "marks": 2,
        "page": 6,
        "summary": "Show that at half-neutralisation pH = pKa for weak acid HA.",
        "description": "Show that when half of HA is neutralised, [A-] = [HA], hence Ka = [H+] and pH = pKa.",
        "spec_ref": "3.1.12",
        "answers_html": "At half-neutralisation, [A<sup>-</sup>] = [HA] (1)<br>Hence <em>K</em><sub>a</sub> = [H<sup>+</sup>][A<sup>-</sup>] / [HA] = [H<sup>+</sup>]<br>Taking &ndash;log of both sides: &ndash;log <em>K</em><sub>a</sub> = &ndash;log [H<sup>+</sup>], so <strong>pH = p<em>K</em><sub>a</sub></strong> (1)",
        "extra_html": "1 mark for [A-] = [HA]<br>1 mark for derivation of pH = pKa"
    },
    {
        "id": "2005-june-chm5-q2c",
        "question": "2(c)",
        "marks": 2,
        "page": 7,
        "summary": "Explain why dilution with a small volume of water does not affect buffer pH.",
        "description": "Explain why dilution does not affect pH of buffer solution: ratio [A-]/[HA] remains constant.",
        "spec_ref": "3.1.12",
        "answers_html": "Ratio [A<sup>-</sup>] : [HA] remains constant (1)<br>Hence as [H<sup>+</sup>] = <em>K</em><sub>a</sub> &times; [HA] / [A<sup>-</sup>], [H<sup>+</sup>] (and pH) remains constant (1)",
        "extra_html": "1 mark for ratio remains constant<br>1 mark for [H+] remains constant"
    },
    {
        "id": "2005-june-chm5-q2di",
        "question": "2(d)(i)",
        "marks": 2,
        "page": 7,
        "summary": "Calculate change in pH when 0.250 mol dm-3 HCl is diluted to 0.150 mol dm-3.",
        "description": "Calculate pH change when 0.250 M HCl (pH 0.60) is diluted to 0.150 M HCl (pH 0.82).",
        "spec_ref": "3.1.12",
        "answers_html": "pH of 0.250 mol dm<sup>-3</sup> HCl = &ndash;log(0.250) = 0.60<br>pH of 0.150 mol dm<sup>-3</sup> HCl = &ndash;log(0.150) = 0.82<br>Change in pH = 0.82 &ndash; 0.60 = <strong>0.22</strong>",
        "extra_html": "1 mark for initial and final pH values<br>1 mark for pH change = 0.22"
    },
    {
        "id": "2005-june-chm5-q2dii",
        "question": "2(d)(ii)",
        "marks": 2,
        "page": 7,
        "summary": "Calculate volume of water needed to dilute 30.0 cm3 of 0.250 M HCl to 0.150 M.",
        "description": "Calculate volume of water added to 30.0 cm3 of 0.250 M HCl to produce 0.150 M solution (V_total = 50 cm3, water added = 20 cm3).",
        "spec_ref": "3.1.2",
        "answers_html": "Moles of HCl = 0.030 &times; 0.250 = 7.50 &times; 10<sup>-3</sup> mol<br>New total volume <em>V</em> = (7.50 &times; 10<sup>-3</sup>) / 0.150 = 0.050 dm<sup>3</sup> = 50 cm<sup>3</sup> (1)<br>Volume of water added = 50 &ndash; 30 = <strong>20 cm<sup>3</sup></strong> (1)",
        "extra_html": "1 mark for total volume 50 cm3<br>1 mark for volume of water added = 20 cm3"
    },

    # Q3 (17 marks total)
    {
        "id": "2005-june-chm5-q3ai",
        "question": "3(a)(i)",
        "marks": 4,
        "page": 8,
        "summary": "Record observations for NaBr and NaI with AgNO3 followed by concentrated NH3.",
        "description": "Record observations when aqueous AgNO3 is added followed by concentrated aqueous ammonia to NaBr and NaI.",
        "spec_ref": "3.2.3",
        "answers_html": "<strong>NaBr(aq)</strong>:<br>&bull; With AgNO<sub>3</sub>: <strong>cream precipitate</strong> (1)<br>&bull; With conc. NH<sub>3</sub>: <strong>precipitate dissolves</strong> (1)<br><br><strong>NaI(aq)</strong>:<br>&bull; With AgNO<sub>3</sub>: <strong>yellow precipitate</strong> (1)<br>&bull; With conc. NH<sub>3</sub>: <strong>precipitate insoluble / no change</strong> (1)",
        "extra_html": "1 mark for each observation"
    },
    {
        "id": "2005-june-chm5-q3aii",
        "question": "3(a)(ii)",
        "marks": 1,
        "page": 8,
        "summary": "Explain why NaNO3 and NaF cannot be distinguished by silver nitrate.",
        "description": "Explain why addition of silver nitrate cannot distinguish between NaNO3 and NaF (AgF is soluble, so no precipitate forms in either).",
        "spec_ref": "3.2.3",
        "answers_html": "<strong>Silver fluoride (AgF) is soluble</strong> (so no precipitate forms with either solution / no visible change in both)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 8,
        "summary": "Identify silver species formed when aqueous thiosulphate dissolves solid silver halide.",
        "description": "Identify dithiosulphatoargentate(I) complex [Ag(S2O3)2]3-.",
        "spec_ref": "3.2.5",
        "answers_html": "<strong>[Ag(S<sub>2</sub>O<sub>3</sub>)<sub>2</sub>]<sup>3-</sup></strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q3bii",
        "question": "3(b)(ii)",
        "marks": 1,
        "page": 8,
        "summary": "Write equation for dissolving AgBr/AgI in aqueous sodium thiosulphate.",
        "description": "Write equation for dissolution of silver halide precipitate by thiosulphate: AgBr + 2S2O3 2- -> [Ag(S2O3)2]3- + Br-.",
        "spec_ref": "3.2.5",
        "answers_html": "<strong>AgBr + 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup> &rarr; [Ag(S<sub>2</sub>O<sub>3</sub>)<sub>2</sub>]<sup>3-</sup> + Br<sup>-</sup></strong><br><em>(or with AgI: AgI + 2S<sub>2</sub>O<sub>3</sub><sup>2-</sup> &rarr; [Ag(S<sub>2</sub>O<sub>3</sub>)<sub>2</sub>]<sup>3-</sup> + I<sup>-</sup>)</em>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q3biii",
        "question": "3(b)(iii)",
        "marks": 1,
        "page": 8,
        "summary": "Give one use of reaction between silver halide and thiosulphate.",
        "description": "Give one use of thiosulphate reaction: photographic fixer / removing unexposed silver halide in photography.",
        "spec_ref": "3.2.5",
        "answers_html": "<strong>Photography / photographic fixer</strong> (fixing unexposed silver halide)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q3ci",
        "question": "3(c)(i)",
        "marks": 2,
        "page": 9,
        "summary": "Draw structure of ethanoyl chloride and predict observation with aqueous silver nitrate.",
        "description": "Draw structure of ethanoyl chloride CH3COCl and state observation with AgNO3(aq) (white precipitate immediately / steamy fumes).",
        "spec_ref": "3.3.10",
        "answers_html": "Structure: <strong>CH<sub>3</sub>COCl</strong><br>Observation: <strong>vigorous / violent / exothermic reaction</strong>, white precipitate formed immediately (or white / steamy fumes)",
        "extra_html": "1 mark for structure<br>1 mark for observation"
    },
    {
        "id": "2005-june-chm5-q3cii",
        "question": "3(c)(ii)",
        "marks": 2,
        "page": 9,
        "summary": "Draw structure of chloroethanoic acid and predict observation with aqueous silver nitrate.",
        "description": "Draw structure of chloroethanoic acid ClCH2COOH and state observation with AgNO3(aq) (no immediate precipitate / very slow reaction).",
        "spec_ref": "3.3.10",
        "answers_html": "Structure: <strong>ClCH<sub>2</sub>COOH</strong><br>Observation: <strong>no immediate reaction / precipitate</strong> (or white precipitate forms very slowly)",
        "extra_html": "1 mark for structure<br>1 mark for observation"
    },
    {
        "id": "2005-june-chm5-q3di",
        "question": "3(d)(i)",
        "marks": 2,
        "page": 9,
        "summary": "Identify silver complex in Tollens' reagent and state its shape.",
        "description": "Identify diamminesilver(I) complex [Ag(NH3)2]+ in Tollens' reagent and its linear shape.",
        "spec_ref": "3.2.5",
        "answers_html": "Silver-containing complex: <strong>[Ag(NH<sub>3</sub>)<sub>2</sub>]<sup>+</sup></strong><br>Shape: <strong>linear</strong>",
        "extra_html": "1 mark for complex<br>1 mark for linear"
    },
    {
        "id": "2005-june-chm5-q3dii",
        "question": "3(d)(ii)",
        "marks": 2,
        "page": 9,
        "summary": "Draw structure of methanoic acid and explain why it gives a silver mirror with Tollens' reagent.",
        "description": "Draw structure of HCOOH and explain that it contains an aldehyde (CHO) group.",
        "spec_ref": "3.3.8",
        "answers_html": "Structure: <strong>HCOOH</strong> (H&ndash;C(=O)&ndash;OH)<br>Explanation: Methanoic acid <strong>contains an aldehyde (&ndash;CHO) group</strong>",
        "extra_html": "1 mark for structure<br>1 mark for aldehyde group explanation"
    },
    {
        "id": "2005-june-chm5-q3diii",
        "question": "3(d)(iii)",
        "marks": 1,
        "page": 9,
        "summary": "Deduce identity of carbon-containing species formed when methanoic acid reacts with Tollens' reagent.",
        "description": "Deduce carbon species formed on oxidation of HCOOH: CO2 / H2CO3 / (NH4)2CO3.",
        "spec_ref": "3.3.8",
        "answers_html": "<strong>CO<sub>2</sub></strong> (carbon dioxide) <em>OR</em> <strong>H<sub>2</sub>CO<sub>3</sub></strong> <em>OR</em> <strong>(NH<sub>4</sub>)<sub>2</sub>CO<sub>3</sub></strong> / HCOONH<sub>4</sub>",
        "extra_html": "1 mark"
    },

    # Q4 (14 marks total)
    {
        "id": "2005-june-chm5-q4a",
        "question": "4(a)",
        "marks": 1,
        "page": 10,
        "figures": ["img/2005-june-chm5/fig-q4-table.jpg"],
        "summary": "Select most powerful reducing agent from electrode potential table.",
        "description": "Select most powerful reducing agent from standard electrode potentials (Zn).",
        "spec_ref": "3.1.11",
        "answers_html": "<strong>Zn</strong> (zinc)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q4bi",
        "question": "4(b)(i)",
        "marks": 1,
        "page": 10,
        "figures": ["img/2005-june-chm5/fig-q4-table.jpg"],
        "summary": "Select species reducing VO2+ to VO2+ but not VO2+ to V3+.",
        "description": "Select Fe2+ which reduces VO2+ (+1.00 V) to VO2+ but cannot reduce VO2+ (+0.34 V).",
        "spec_ref": "3.1.11",
        "answers_html": "<strong>Fe<sup>2+</sup></strong> (or Fe<sup>2+</sup>(aq))",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q4bii",
        "question": "4(b)(ii)",
        "marks": 1,
        "page": 10,
        "figures": ["img/2005-june-chm5/fig-q4-table.jpg"],
        "summary": "Select species oxidising VO2+ to VO2+.",
        "description": "Select Cl2 which oxidises VO2+ (+0.34 V / +1.00 V) to VO2+ (+1.36 V).",
        "spec_ref": "3.1.11",
        "answers_html": "<strong>Cl<sub>2</sub></strong> (chlorine)",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q4ci",
        "question": "4(c)(i)",
        "marks": 1,
        "page": 10,
        "figures": ["img/2005-june-chm5/fig-q4-table.jpg"],
        "summary": "Deduce standard electrode potential for Tl3+/Tl+ half-reaction.",
        "description": "Deduce standard electrode potential for Tl3+ + 2e- -> Tl+ from cell e.m.f. = +0.48 V and Fe3+/Fe2+ = +0.77 V.",
        "spec_ref": "3.1.11",
        "answers_html": "<em>E</em>&deg; = 0.77 + 0.48 = <strong>+1.25 V</strong>",
        "extra_html": "1 mark"
    },
    {
        "id": "2005-june-chm5-q4cii",
        "question": "4(c)(ii)",
        "marks": 2,
        "page": 10,
        "figures": ["img/2005-june-chm5/fig-q4-table.jpg"],
        "summary": "Write equation for spontaneous cell reaction.",
        "description": "Write equation for spontaneous reaction: Tl3+ + 2Fe2+ -> Tl+ + 2Fe3+.",
        "spec_ref": "3.1.11",
        "answers_html": "<strong>Tl<sup>3+</sup> + 2Fe<sup>2+</sup> &rarr; Tl<sup>+</sup> + 2Fe<sup>3+</sup></strong>",
        "extra_html": "1 mark for correct species and direction<br>1 mark for balanced equation"
    },
    {
        "id": "2005-june-chm5-q4di",
        "question": "4(d)(i)",
        "marks": 4,
        "page": 11,
        "summary": "Determine concentration of H2O2 solution in g dm-3 from manganate(VII) titration.",
        "description": "Calculate concentration of H2O2 in g dm-3 from titration with 16.2 cm3 of 0.0200 M KMnO4.",
        "spec_ref": "3.1.2",
        "answers_html": "Moles of KMnO<sub>4</sub> = 0.0162 &times; 0.0200 = 3.24 &times; 10<sup>-4</sup> mol (1)<br>Moles of H<sub>2</sub>O<sub>2</sub> = 3.24 &times; 10<sup>-4</sup> &times; 5/2 = 8.10 &times; 10<sup>-4</sup> mol in 25.0 cm<sup>3</sup> (1)<br>[H<sub>2</sub>O<sub>2</sub>] = (8.10 &times; 10<sup>-4</sup>) / 0.025 = 0.0324 mol dm<sup>-3</sup> (1)<br>Concentration in g dm<sup>-3</sup> = 0.0324 &times; 34.0 = <strong>1.10</strong> g dm<sup>-3</sup> (1)",
        "extra_html": "1 mark for moles of KMnO4<br>1 mark for moles of H2O2 (using 5:2 ratio)<br>1 mark for molarity 0.0324 mol dm-3<br>1 mark for 1.10 g dm-3 (3 sig figs)"
    },
    {
        "id": "2005-june-chm5-q4dii",
        "question": "4(d)(ii)",
        "marks": 4,
        "page": 11,
        "summary": "Calculate volume of oxygen evolved using ideal gas equation pV = nRT.",
        "description": "Calculate volume of O2 evolved in m3 using pV = nRT at 98 kPa and 298 K.",
        "spec_ref": "3.1.2",
        "answers_html": "Moles of O<sub>2</sub> = moles of H<sub>2</sub>O<sub>2</sub> = 8.10 &times; 10<sup>-4</sup> mol<br><em>pV</em> = <em>nRT</em> &rarr; <em>V</em> = <em>nRT</em> / <em>p</em> (1)<br><em>V</em> = (8.10 &times; 10<sup>-4</sup> &times; 8.31 &times; 298) / 98000 (1)<br>= <strong>2.05 &times; 10<sup>-5</sup></strong> (1)<br>Units: <strong>m<sup>3</sup></strong> (1) <em>(or 20.5 cm<sup>3</sup>)</em>",
        "extra_html": "1 mark for pV = nRT rearranged<br>1 mark for numbers substituted<br>1 mark for 2.05 x 10-5 (3 sig figs)<br>1 mark for correct units (m3)"
    }
]

print(f"Ingesting {len(questions_data)} questions for June 2005 CHM5...")
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Remove any existing 2005-june-chm5 questions
db['questions'] = [q for q in db['questions'] if q['paper'] != '2005-june-chm5']

for item in questions_data:
    q_id = item['id']
    ms_img_rel = f"img/2005-june-chm5/ms_{q_id.split('-')[-1]}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
    q_img_rel = f"img/2005-june-chm5/q_{q_id.split('-')[-1]}.jpg"

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
        "paper": "2005-june-chm5",
        "question": item["question"],
        "marks": item["marks"],
        "summary": item["summary"],
        "description": item["description"],
        "topic": item["spec_ref"],
        "tags": ["CHM5", "AQA", "A-Level"],
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

print(f"\nSuccessfully ingested {len(questions_data)} questions for 2005-june-chm5!")

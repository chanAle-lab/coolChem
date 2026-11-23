"""
Ingestion script for 2007 June CHM4 (Section A only: Q1-Q6)
Excludes Section B extended questions (Q7, Q8).
NOTE: PDF page 1 is an Erratum Notice, so 1-based PDF page = printed page + 1.
Renders official AQA modern mark scheme tables and adds paper metadata.
"""
import os
import json
import fitz
import sys
from PIL import Image, ImageDraw
import io

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222468_a1e6a223.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2007-june-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

doc = fitz.open(QP_PATH)
DPI = 200
SCALE = DPI / 72.0

def save_crop(page_idx, rect, filename, mask_pdf_rects=None):
    page = doc[page_idx]
    pix = page.get_pixmap(clip=rect, dpi=DPI)
    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    if mask_pdf_rects:
        draw = ImageDraw.Draw(im)
        for mr in mask_pdf_rects:
            px0 = max(0, int((mr[0] - rect.x0) * SCALE))
            py0 = max(0, int((mr[1] - rect.y0) * SCALE))
            px1 = min(im.width, int((mr[2] - rect.x0) * SCALE))
            py1 = min(im.height, int((mr[3] - rect.y0) * SCALE))
            draw.rectangle([px0, py0, px1, py1], fill=(255, 255, 255))
    im.save(os.path.join(IMG_DIR, filename), format="JPEG", quality=92)

# Q1 figures
save_crop(2, fitz.Rect(55, 145, 530, 282), "fig-q1-eq.jpg")
save_crop(2, fitz.Rect(98, 342, 530, 405), "fig-q1-aii-kp.jpg")
save_crop(5, fitz.Rect(75, 222, 530, 270), "fig-q1-c-data.jpg")
# Q2 figure
save_crop(6, fitz.Rect(105, 265, 480, 520), "fig-q2-curve.jpg")
# Q3 figures
save_crop(8, fitz.Rect(55, 68, 530, 185), "fig-q3-ka.jpg")
save_crop(8, fitz.Rect(72, 366, 530, 408), "fig-q3-b-stem.jpg")
# Q4 figures
save_crop(9, fitz.Rect(55, 68, 530, 178), "fig-q4-a-stem.jpg")
save_crop(9, fitz.Rect(115, 482, 465, 612), "fig-q4-table.jpg")
# Q5 figure
save_crop(10, fitz.Rect(70, 68, 450, 162), "fig-q5-alanine.jpg")
# Q6 figures (mask top-left "6 Consider..." text at x=57..251, y=71..83 and bottom-left "(a)(i)" at y=308.9)
save_crop(
    12,
    fitz.Rect(90, 68, 495, 315),
    "fig-q6-scheme.jpg",
    mask_pdf_rects=[(90, 68, 265, 90), (90, 295, 260, 315)]
)
# Q6 IR spectra (PDF p.16 = doc[15]; widen x0 to 42 for "The infra-red...", mask footer "APW/Jun07/CHM4" at x=47..115, y>=814)
save_crop(
    15,
    fitz.Rect(42, 58, 475, 826),
    "fig-q6-ir-spectra.jpg",
    mask_pdf_rects=[(42, 813, 118, 826)]
)
# Q6 IR Data Sheet Table 2 (PDF p.5 = doc[4])
save_crop(4, fitz.Rect(165, 460, 415, 650), "fig-q6-ir-table.jpg")

PAPER_OBJ = {
    "id": "2007-june-chm4",
    "year": 2007,
    "series": "June",
    "date": "2007-06-18",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 mins"
}

QUESTIONS_DATA = [
    # Q1 (14 marks, PDF p.3 & p.6)
    {
        "id": "2007-june-chm4-q1ai",
        "question": "1(a)(i)",
        "marks": 1,
        "page": 3,
        "topics": ["3.1.10"],
        "skills": ["application"],
        "summary": "Deduce the units of Kp for 2SO2(g) + O2(g) <-> 2SO3(g) when pressures are measured in kPa.",
        "figures": [],
        "ms_rows": [
            ("1(a)(i)", "kPa<sup>−1</sup>", "not 1/kPa", "1", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-june-chm4-q1aii",
        "question": "1(a)(ii)",
        "marks": 3,
        "page": 3,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the partial pressure of oxygen given p(SO2) = 10.6 kPa, p(SO3) = 90.8 kPa, and Kp = 1.42.",
        "figures": ["img/2007-june-chm4/fig-q1-eq.jpg"],
        "ms_rows": [
            ("1(a)(ii)", "<i>p</i><sub>O<sub>2</sub></sub> = (<i>p</i><sub>SO<sub>3</sub></sub>)<sup>2</sup> / ((<i>p</i><sub>SO<sub>2</sub></sub>)<sup>2</sup> × <i>K</i><sub>p</sub>) (1)<br><br>= 90.8<sup>2</sup> / (10.6<sup>2</sup> × 1.42) (1)<br><br>= <b>51.7 kPa</b> (allow 51.6 – 51.9) (1)", "One mark for correct rearrangement and one mark for insertion of correct numbers (can be in either order)", "3", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-june-chm4-q1bi",
        "question": "1(b)(i)",
        "marks": 2,
        "page": 3,
        "topics": ["3.1.10", "3.1.6"],
        "skills": ["explanation"],
        "summary": "State and explain the effect on the mole fraction of SO3 if the container volume is decreased at constant temperature.",
        "figures": ["img/2007-june-chm4/fig-q1-eq.jpg"],
        "ms_rows": [
            ("1(b)(i)", "<b>Effect:</b> increase (1)<br><br><b>Explanation:</b> equilibrium moves to fewer gas moles <i>or</i> fewer moles on RHS (1)", "-", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-june-chm4-q1bii",
        "question": "1(b)(ii)",
        "marks": 1,
        "page": 3,
        "topics": ["3.1.10"],
        "skills": ["recall"],
        "summary": "State the effect on the value of Kp if the container volume is decreased at constant temperature.",
        "figures": ["img/2007-june-chm4/fig-q1-eq.jpg"],
        "ms_rows": [
            ("1(b)(ii)", "None / no effect", "-", "1", "AO1 / 3.1.10")
        ]
    },
    {
        "id": "2007-june-chm4-q1biii",
        "question": "1(b)(iii)",
        "marks": 2,
        "page": 6,
        "topics": ["3.1.10", "3.1.6"],
        "skills": ["explanation"],
        "summary": "Deduce whether T1 or T2 is higher when changing from T1 to T2 decreases p(SO3) (ΔH = -196 kJ mol-1).",
        "figures": ["img/2007-june-chm4/fig-q1-eq.jpg"],
        "ms_rows": [
            ("1(b)(iii)", "<b>Higher temperature:</b> T<sub>2</sub> (1)<br><br><b>Explanation:</b> equilibrium moves in endothermic direction <i>or</i> to LHS (<i>or</i> forward reaction is exothermic) (1)", "-", "2", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-june-chm4-q1ci",
        "question": "1(c)(i)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Calculate the mole fraction of oxygen when the mole fractions of SO3 and SO2 are 0.75 and 0.17.",
        "figures": ["img/2007-june-chm4/fig-q1-eq.jpg"],
        "ms_rows": [
            ("1(c)(i)", "<b>0.08</b>", "NOT 0.085", "1", "AO2 / 3.1.10")
        ]
    },
    {
        "id": "2007-june-chm4-q1cii",
        "question": "1(c)(ii)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["recall"],
        "summary": "Write an expression relating the partial pressure of a gas to its mole fraction and total pressure P.",
        "figures": ["img/2007-june-chm4/fig-q1-eq.jpg"],
        "ms_rows": [
            ("1(c)(ii)", "pp = mole fraction × total pressure", "-", "1", "AO1 / 3.1.10")
        ]
    },
    {
        "id": "2007-june-chm4-q1ciii",
        "question": "1(c)(iii)",
        "marks": 3,
        "page": 6,
        "topics": ["3.1.10"],
        "skills": ["calculation"],
        "summary": "Use the mole fractions and Kp = 1.42 from (a)(ii) to calculate a value for the total pressure P.",
        "figures": [
            "img/2007-june-chm4/fig-q1-eq.jpg",
            "img/2007-june-chm4/fig-q1-aii-kp.jpg",
            "img/2007-june-chm4/fig-q1-c-data.jpg"
        ],
        "ms_rows": [
            ("1(c)(iii)", "<i>K</i><sub>p</sub> = (mol fn SO<sub>3</sub> × <i>P</i>)<sup>2</sup> / [(mol fn SO<sub>2</sub> × <i>P</i>)<sup>2</sup> × (mol fn O<sub>2</sub> × <i>P</i>)] &nbsp;<i>or</i>&nbsp; <i>P</i> = (mol fn SO<sub>3</sub>)<sup>2</sup> / [(mol fn SO<sub>2</sub>)<sup>2</sup> × mol fn O<sub>2</sub> × <i>K</i><sub>p</sub>] (1)<br><br><i>P</i> = 0.75<sup>2</sup> / (0.17<sup>2</sup> × 0.08 × 1.42) (1)<br><br>= <b>171 (kPa)</b> (1)", "Mark consequentially on (i)<br>Must specify substances in expression<br>Steps 1 and 2 can be in either order", "3", "AO2 / 3.1.10")
        ]
    },
    # Q2 (9 marks, PDF p.7-8)
    {
        "id": "2007-june-chm4-q2ai",
        "question": "2(a)(i)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.12"],
        "skills": ["recall"],
        "summary": "Write an expression for the term pH.",
        "figures": [],
        "ms_rows": [
            ("2(a)(i)", "pH = −log[H<sup>+</sup>] &nbsp;<i>or</i>&nbsp; log(1/[H<sup>+</sup>])", "must be [ ]", "1", "AO1 / 3.1.12")
        ]
    },
    {
        "id": "2007-june-chm4-q2aii",
        "question": "2(a)(ii)",
        "marks": 1,
        "page": 7,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the concentration of hydrochloric acid which has a pH value of 0.36.",
        "figures": [],
        "ms_rows": [
            ("2(a)(ii)", "<b>0.437</b> or <b>0.44</b> (mol dm<sup>−3</sup>)", "-", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-june-chm4-q2bi",
        "question": "2(b)(i)",
        "marks": 2,
        "page": 7,
        "topics": ["3.1.12"],
        "skills": ["application"],
        "summary": "Write equations for the reactions occurring before equivalence point A and between equivalence points A and B when HCl is added to Na2CO3(aq).",
        "figures": ["img/2007-june-chm4/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(b)(i)", "<b>Before A:</b> CO<sub>3</sub><sup>2−</sup> + H<sup>+</sup> → HCO<sub>3</sub><sup>−</sup> (1)<br><br><b>Between A and B:</b> HCO<sub>3</sub><sup>−</sup> + H<sup>+</sup> → H<sub>2</sub>O + CO<sub>2</sub> &nbsp;(<i>or</i> → H<sub>2</sub>CO<sub>3</sub>) (1)", "ignore spectator ions", "2", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-june-chm4-q2bii",
        "question": "2(b)(ii)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.12"],
        "skills": ["application"],
        "summary": "Select the best indicator from the list for equivalence point A and for equivalence point B.",
        "figures": ["img/2007-june-chm4/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(b)(ii)", "<b>Equivalence point A:</b> metacresol purple (1)<br><br><b>Equivalence point B:</b> bromophenol blue (1)", "-", "2", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-june-chm4-q2biii",
        "question": "2(b)(iii)",
        "marks": 1,
        "page": 8,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the number of moles of Na2CO3 in a 40.0 cm3 sample of 0.150 mol dm-3 aqueous sodium carbonate.",
        "figures": ["img/2007-june-chm4/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(b)(iii)", "(40 / 10<sup>3</sup>) × 0.150 = <b>6.0 × 10<sup>−3</sup></b>", "-", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-june-chm4-q2biv",
        "question": "2(b)(iv)",
        "marks": 2,
        "page": 8,
        "topics": ["3.1.2"],
        "skills": ["calculation"],
        "summary": "Use the volume of HCl added at equivalence point B to calculate the concentration of the hydrochloric acid used.",
        "figures": ["img/2007-june-chm4/fig-q2-curve.jpg"],
        "ms_rows": [
            ("2(b)(iv)", "mol HCl = <b>12.0 × 10<sup>−3</sup></b> (1)<br><br>conc = (12.0 × 10<sup>−3</sup>) / (50.0 × 10<sup>−3</sup>) = <b>0.24 mol dm<sup>−3</sup></b> (1)", "consequential on (iii); must score first mark to gain 2nd mark", "2", "AO2 / 3.1.2")
        ]
    },
    # Q3 (9 marks, PDF p.9)
    {
        "id": "2007-june-chm4-q3a",
        "question": "3(a)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH at 298 K of a 0.550 mol dm-3 solution of propanoic acid (Ka = 1.35 x 10^-5 mol dm-3).",
        "figures": [],
        "ms_rows": [
            ("3(a)", "<i>K</i><sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [CH<sub>3</sub>CH<sub>2</sub>COOH] (1)<br><br>[H<sup>+</sup>] = √(1.35 × 10<sup>−5</sup> × 0.550) = 2.72 × 10<sup>−3</sup> (1)<br><br>pH = <b>2.56</b> or <b>2.57</b> (1)", "penalise pH with decimal places ≠ 2 once per paper; 5.13 (if miss square root) gets 2", "3", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-june-chm4-q3bi",
        "question": "3(b)(i)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12", "3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the number of moles of propanoic acid originally present in 30.0 cm3 of 0.550 mol dm-3 solution.",
        "figures": [],
        "ms_rows": [
            ("3(b)(i)", "30.0 × 10<sup>−3</sup> × 0.55 = <b>1.65 × 10<sup>−2</sup></b> &nbsp;(or 0.017)", "at least 2 sig figs", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-june-chm4-q3bii",
        "question": "3(b)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12", "3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the number of moles of sodium hydroxide added (10.0 cm3 of 0.230 mol dm-3).",
        "figures": ["img/2007-june-chm4/fig-q3-b-stem.jpg"],
        "ms_rows": [
            ("3(b)(ii)", "10.0 × 10<sup>−3</sup> × 0.23 = <b>2.30 × 10<sup>−3</sup></b> &nbsp;(or 0.0023)", "at least 2 sig figs", "1", "AO2 / 3.1.2")
        ]
    },
    {
        "id": "2007-june-chm4-q3biii",
        "question": "3(b)(iii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.12", "3.1.2"],
        "skills": ["calculation"],
        "summary": "Calculate the number of moles of propanoic acid present in the buffer solution.",
        "figures": ["img/2007-june-chm4/fig-q3-b-stem.jpg"],
        "ms_rows": [
            ("3(b)(iii)", "(1.65 × 10<sup>−2</sup>) − (2.30 × 10<sup>−3</sup>) = <b>1.42 × 10<sup>−2</sup></b>", "i.e. (i) − (ii) above; if addition not subtraction, also penalise first mark gained in (iv)", "1", "AO2 / 3.1.12")
        ]
    },
    {
        "id": "2007-june-chm4-q3biv",
        "question": "3(b)(iv)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.12"],
        "skills": ["calculation"],
        "summary": "Calculate the pH of the propanoic acid / sodium propanoate buffer solution to 2 decimal places.",
        "figures": [
            "img/2007-june-chm4/fig-q3-ka.jpg",
            "img/2007-june-chm4/fig-q3-b-stem.jpg"
        ],
        "ms_rows": [
            ("3(b)(iv)", "mol CH<sub>3</sub>CH<sub>2</sub>COONa = <b>2.30 × 10<sup>−3</sup></b> (may be scored in expression) (1)<br><br>[H<sup>+</sup>] = <i>K</i><sub>a</sub> × [CH<sub>3</sub>CH<sub>2</sub>COOH] / [CH<sub>3</sub>CH<sub>2</sub>COO<sup>−</sup>] = (1.35 × 10<sup>−5</sup>) × (1.42 × 10<sup>−2</sup> / V) / (2.30 × 10<sup>−3</sup> / V) = 8.33 × 10<sup>−5</sup> &nbsp;(or pH = p<i>K</i><sub>a</sub> + log([salt]/[acid])) (1)<br><br>pH = <b>4.08</b> (allow 4.07 if 1.4 × 10<sup>−2</sup> used) (1)", "if any mention of [H<sup>+</sup>]<sup>2</sup>/[HA], max 1 for moles of salt; if addition in (iii), 3.96–3.97 gets 2 in part (iv)", "3", "AO2 / 3.1.12")
        ]
    },
    # Q4 (6 marks, PDF p.10)
    {
        "id": "2007-june-chm4-q4ai",
        "question": "4(a)(i)",
        "marks": 3,
        "page": 10,
        "topics": ["3.1.9"],
        "skills": ["calculation"],
        "summary": "Calculate the rate constant k and deduce its units for rate = k[C][D]^2 when [C] = 0.15, [D] = 0.24 and rate = 0.65 mol dm-3 s-1.",
        "figures": [],
        "ms_rows": [
            ("4(a)(i)", "<i>k</i> = 0.65 / (0.15 × 0.24<sup>2</sup>) (1)<br><br>= <b>75.23</b> (allow 74.7 to 75.23) (1)<br><br>Units: <b>mol<sup>−2</sup> dm<sup>6</sup> s<sup>−1</sup></b> (1)", "if <i>k</i> upside down, max 1 for consequential units (mol<sup>2</sup> dm<sup>−6</sup> s)", "3", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2007-june-chm4-q4aii",
        "question": "4(a)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.9"],
        "skills": ["calculation"],
        "summary": "Calculate the initial rate when the concentrations of both C and D are halved compared to part (a)(i).",
        "figures": ["img/2007-june-chm4/fig-q4-a-stem.jpg"],
        "ms_rows": [
            ("4(a)(ii)", "<b>0.081</b> (mol dm<sup>−3</sup> s<sup>−1</sup>)", "min 2 sig. figs required; ignore wrong units; may be consequential on their <i>k</i> i.e. (1.08 × 10<sup>−3</sup>) × their <i>k</i>", "1", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2007-june-chm4-q4bi",
        "question": "4(b)(i)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.9"],
        "skills": ["application"],
        "summary": "Deduce the order of reaction with respect to E from the initial rate data table.",
        "figures": ["img/2007-june-chm4/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(b)(i)", "<b>2</b>", "-", "1", "AO2 / 3.1.9")
        ]
    },
    {
        "id": "2007-june-chm4-q4bii",
        "question": "4(b)(ii)",
        "marks": 1,
        "page": 10,
        "topics": ["3.1.9"],
        "skills": ["application"],
        "summary": "Deduce the order of reaction with respect to F from the initial rate data table.",
        "figures": ["img/2007-june-chm4/fig-q4-table.jpg"],
        "ms_rows": [
            ("4(b)(ii)", "<b>0</b>", "-", "1", "AO2 / 3.1.9")
        ]
    },
    # Q5 (6 marks, PDF p.11-12)
    {
        "id": "2007-june-chm4-q5ai",
        "question": "5(a)(i)",
        "marks": 1,
        "page": 11,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the zwitterion formed by alanine, H2N-CH(CH3)-COOH.",
        "figures": [],
        "ms_rows": [
            ("5(a)(i)", "<sup>+</sup>H<sub>3</sub>N–CH(CH<sub>3</sub>)–COO<sup>−</sup>", "-", "1", "AO2 / 3.3.13")
        ]
    },
    {
        "id": "2007-june-chm4-q5aii",
        "question": "5(a)(ii)",
        "marks": 3,
        "page": 11,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the organic product formed when alanine reacts with CH3OH/conc. H2SO4, with Na2CO3, and with CH3Cl (1:1).",
        "figures": ["img/2007-june-chm4/fig-q5-alanine.jpg"],
        "ms_rows": [
            ("5(a)(ii)", "<b>With CH<sub>3</sub>OH / conc. H<sub>2</sub>SO<sub>4</sub>:</b> H<sub>2</sub>N–CH(CH<sub>3</sub>)–COOCH<sub>3</sub> (1)<br><br><b>With Na<sub>2</sub>CO<sub>3</sub>:</b> H<sub>2</sub>N–CH(CH<sub>3</sub>)–COO<sup>−</sup> (Na<sup>+</sup>) (1)<br><br><b>With CH<sub>3</sub>Cl (1:1):</b> H<sub>3</sub>C–NH–CH(CH<sub>3</sub>)–COOH (1)", "Not allow covalent O–Na", "3", "AO2 / 3.3.13")
        ]
    },
    {
        "id": "2007-june-chm4-q5b",
        "question": "5(b)",
        "marks": 1,
        "page": 12,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the lysine species present in a solution at low pH.",
        "figures": [],
        "ms_rows": [
            ("5(b)", "<sup>+</sup>H<sub>3</sub>N–(CH<sub>2</sub>)<sub>4</sub>–CH(NH<sub>3</sub><sup>+</sup>)–COOH", "-", "1", "AO2 / 3.3.13")
        ]
    },
    {
        "id": "2007-june-chm4-q5c",
        "question": "5(c)",
        "marks": 1,
        "page": 12,
        "topics": ["3.3.13"],
        "skills": ["application"],
        "summary": "Draw the structure of the dipeptide formed from two proline molecules.",
        "figures": [],
        "ms_rows": [
            ("5(c)", "Dipeptide of two proline pyrrolidine rings joined via tertiary amide bond: free NH ring –C(=O)–N(ring)–COOH", "allow –CON and zwitterions and dipeptide – cyclic(–H<sub>2</sub>O); allow ring CH<sub>2</sub> bonds drawn individually, but not C–H<sub>2</sub> off ring vertex", "1", "AO2 / 3.3.13")
        ]
    },
    # Q6 (16 marks, PDF p.13-14 - Section A!)
    {
        "id": "2007-june-chm4-q6ai",
        "question": "6(a)(i)",
        "marks": 1,
        "page": 13,
        "topics": ["3.3.5", "3.3.1"],
        "skills": ["application"],
        "summary": "Name compound J, CH3CH2CH(CH3)CH2OH.",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(a)(i)", "<b>2-methylbutan-1-ol</b>", "numbers essential", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm4-q6aii",
        "question": "6(a)(ii)",
        "marks": 1,
        "page": 13,
        "topics": ["3.3.7"],
        "skills": ["recall"],
        "summary": "Name the type of stereoisomerism shown by compound J.",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(a)(ii)", "Optical", "-", "1", "AO1 / 3.3.7")
        ]
    },
    {
        "id": "2007-june-chm4-q6bi",
        "question": "6(b)(i)",
        "marks": 1,
        "page": 13,
        "topics": ["3.3.5"],
        "skills": ["recall"],
        "summary": "Name the type of mechanism for Reaction 1 (conversion of alcohol J into alkene K).",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(b)(i)", "Elimination", "not nucleophilic nor any other qualification; not just dehydration", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-june-chm4-q6bii",
        "question": "6(b)(ii)",
        "marks": 2,
        "page": 13,
        "topics": ["3.3.4"],
        "skills": ["application"],
        "summary": "Draw the repeating unit of the polymer formed by alkene K and name the type of polymerisation involved.",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(b)(ii)", "<b>Repeating unit:</b> –C(CH<sub>2</sub>CH<sub>3</sub>)(CH<sub>3</sub>)–CH<sub>2</sub>– with trailing bonds (1)<br><br><b>Type of polymerisation:</b> addition <i>or</i> radical (<b>QoL</b>) (1)", "penalise –CH<sub>3</sub>CH<sub>2</sub> connectivity each time; not \"additional\"", "2", "AO2 / 3.3.4")
        ]
    },
    {
        "id": "2007-june-chm4-q6biii",
        "question": "6(b)(iii)",
        "marks": 1,
        "page": 13,
        "topics": ["3.3.1"],
        "skills": ["application"],
        "summary": "Draw the structure of an isomer of alkene K (C5H10) which shows stereoisomerism.",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(b)(iii)", "Pent-2-ene: cis or trans CH<sub>3</sub>CH<sub>2</sub>(H)C=C(H)CH<sub>3</sub> (allow C<sub>2</sub>H<sub>5</sub>CH=CHCH<sub>3</sub>)<br><i>or</i> 1,2-dimethylcyclopropane", "-", "1", "AO2 / 3.3.1")
        ]
    },
    {
        "id": "2007-june-chm4-q6biv",
        "question": "6(b)(iv)",
        "marks": 1,
        "page": 14,
        "topics": ["3.3.15"],
        "skills": ["application"],
        "summary": "Draw the structure of an isomer of alkene K (C5H10) which has only one peak in its proton n.m.r. spectrum.",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(b)(iv)", "Cyclopentane (five-membered ring of CH<sub>2</sub> groups / skeletal pentagon)", "-", "1", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2007-june-chm4-q6ci",
        "question": "6(c)(i)",
        "marks": 1,
        "page": 14,
        "topics": ["3.3.8", "3.3.15"],
        "skills": ["application"],
        "summary": "Draw the structure of an isomer of aldehyde L (C5H10O) which has no effect on Fehling's or Tollens' reagents and has only two peaks in its 1H n.m.r. spectrum.",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(c)(i)", "CH<sub>3</sub>CH<sub>2</sub>COCH<sub>2</sub>CH<sub>3</sub> (allow C<sub>2</sub>H<sub>5</sub>COC<sub>2</sub>H<sub>5</sub>)", "-", "1", "AO2 / 3.3.15")
        ]
    },
    {
        "id": "2007-june-chm4-q6cii",
        "question": "6(c)(ii)",
        "marks": 1,
        "page": 14,
        "topics": ["3.3.5"],
        "skills": ["practical", "recall"],
        "summary": "State the practical technique used with acidified potassium dichromate(VI) to obtain carboxylic acid M rather than aldehyde L from alcohol J.",
        "figures": ["img/2007-june-chm4/fig-q6-scheme.jpg"],
        "ms_rows": [
            ("6(c)(ii)", "Reflux (<b>QoL</b>)", "-", "1", "AO1 / 3.3.5")
        ]
    },
    {
        "id": "2007-june-chm4-q6d",
        "question": "6(d)",
        "marks": 4,
        "page": 14,
        "topics": ["3.3.6"],
        "skills": ["application"],
        "summary": "Match the four infra-red spectra I, II, III and IV to compounds J, K, L and M using Table 2 on the data sheet.",
        "figures": [
            "img/2007-june-chm4/fig-q6-scheme.jpg",
            "img/2007-june-chm4/fig-q6-ir-spectra.jpg",
            "img/2007-june-chm4/fig-q6-ir-table.jpg"
        ],
        "ms_rows": [
            ("6(d)", "<b>I:</b> M (1)<br><b>II:</b> J (1)<br><b>III:</b> K (1)<br><b>IV:</b> L (1)", "-", "4", "AO2 / 3.3.6")
        ]
    },
    {
        "id": "2007-june-chm4-q6ei",
        "question": "6(e)(i)",
        "marks": 1,
        "page": 14,
        "topics": ["3.3.6"],
        "skills": ["recall"],
        "summary": "Give an approximate range of wavenumbers for the fingerprint region in an infra-red spectrum.",
        "figures": [],
        "ms_rows": [
            ("6(e)(i)", "400 – 1500 cm<sup>−1</sup>", "allow range from [0–600] to [1200–1500]", "1", "AO1 / 3.3.6")
        ]
    },
    {
        "id": "2007-june-chm4-q6eii",
        "question": "6(e)(ii)",
        "marks": 2,
        "page": 14,
        "topics": ["3.3.6"],
        "skills": ["recall"],
        "summary": "Describe how the fingerprint region can be used to identify a compound.",
        "figures": [],
        "ms_rows": [
            ("6(e)(ii)", "<b>M1:</b> compare with spectrum of known compound / database (1)<br><br><b>M2:</b> exact match <i>or</i> fingerprint unique (1)", "M1 must be gained to score M2", "2", "AO1 / 3.3.6")
        ]
    }
]

paper_id = PAPER_OBJ["id"]
new_questions = []

for qd in QUESTIONS_DATA:
    qid = qd["id"]
    q_label = qd["question"]
    ms_img_rel = f"img/{paper_id}/ms_{qid.split('-')[-1]}.jpg"
    ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

    answers_list = []
    extra_list = []
    spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1.10"
    for r in qd["ms_rows"]:
        prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
        answers_list.append(f"{prefix}{r[1]} ({r[3]})" if len(qd["ms_rows"]) > 1 else r[1])
        if r[2] and r[2] != "-":
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
        "markscheme": ms_img_rel
    }
    new_questions.append(q_obj)

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    db = json.load(f)

db["papers"] = [p for p in db["papers"] if p.get("id") != paper_id]
db["papers"].append(PAPER_OBJ)

db["questions"] = [q for q in db["questions"] if q.get("paper") != paper_id]
db["questions"].extend(new_questions)

with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully ingested {len(new_questions)} questions for {paper_id}. Total marks: {sum(q['marks'] for q in new_questions)}")

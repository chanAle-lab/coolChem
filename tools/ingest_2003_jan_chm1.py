"""
Ingestion script for 2003 January CHM1 (Section A only)
Excludes old-spec Section B essay questions (Q6 and Q7).
Renders official AQA modern mark scheme tables and precision cropped question images.
"""
import os
import re
import json
import fitz
from PIL import Image
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463563_9fb5ce0e.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-jan-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-jan-chm1",
    "year": 2003,
    "series": "January",
    "date": "2003-01-14",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour 30 mins"
}

# Crop definitions for Section A questions
# Format: (q_id, q_label, page_num (1-indexed), y0, y1, marks, topics, skills, summary)
QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(d)
    ("2003-jan-chm1-q1a", "1(a)", 2, 145, 330, 3, ["3.1.1"], ["recall"], "Complete table of relative charge and mass for proton, neutron, and electron."),
    ("2003-jan-chm1-q1b", "1(b)", 2, 335, 425, 2, ["3.1.1"], ["recall", "maths"], "Symbol, mass number and atomic number for element Z with two more protons and neutrons than 34S."),
    ("2003-jan-chm1-q1c", "1(c)", 2, 428, 545, 2, ["3.1.1"], ["recall"], "Complete electronic configurations for sulphur atom S and sulphide ion S2-."),
    ("2003-jan-chm1-q1d", "1(d)", 2, 548, 645, 2, ["3.1.1"], ["recall", "analysis"], "State the block in the Periodic Table for sulphur and explain answer."),
    
    # Page 5: Question 1(e)(i)-(iv)
    ("2003-jan-chm1-q1ei", "1(e)(i)", 5, 80, 205, 2, ["3.1.3"], ["recall"], "Deduce the type of bonding present in Na2S and in CS2."),
    ("2003-jan-chm1-q1eii", "1(e)(ii)", 5, 210, 310, 2, ["3.1.3"], ["analysis"], "Explain in terms of electrons how Na2S is formed from its atoms."),
    ("2003-jan-chm1-q1eiii", "1(e)(iii)", 5, 312, 520, 2, ["3.1.3"], ["analysis"], "Draw a diagram representing the bonding in CS2 including outer electrons."),
    ("2003-jan-chm1-q1eiv", "1(e)(iv)", 5, 522, 630, 1, ["3.1.3"], ["recall"], "Equation for reaction of CS2 with steam forming H2S and CO2."),
    
    # Page 6: Question 2(a)-(b)
    ("2003-jan-chm1-q2a", "2(a)", 6, 80, 225, 3, ["3.1.2"], ["calculation"], "Calculate concentration in mol dm-3 of 19.6 g HCl dissolved in 250 cm3."),
    ("2003-jan-chm1-q2bi", "2(b)(i)", 6, 230, 390, 1, ["3.1.2"], ["calculation"], "Calculate moles of HCl used in reaction with M2CO3."),
    ("2003-jan-chm1-q2bii", "2(b)(ii)", 6, 395, 490, 1, ["3.1.2"], ["calculation"], "Calculate moles of M2CO3 in 0.394 g sample."),
    ("2003-jan-chm1-q2biii", "2(b)(iii)", 6, 495, 570, 1, ["3.1.2"], ["calculation"], "Calculate relative molecular mass of M2CO3."),
    ("2003-jan-chm1-q2biv", "2(b)(iv)", 6, 575, 680, 3, ["3.1.2"], ["calculation", "recall"], "Deduce relative atomic mass of M and suggest its identity."),
    
    # Page 7: Question 3(a)-(d)
    ("2003-jan-chm1-q3a", "3(a)", 7, 80, 215, 1, ["3.1.2"], ["recall"], "Name the equation pV = nRT."),
    ("2003-jan-chm1-q3b", "3(b)", 7, 218, 410, 4, ["3.1.2"], ["calculation"], "Calculate moles and relative molecular mass of vaporised liquid X using pV=nRT."),
    ("2003-jan-chm1-q3c", "3(c)", 7, 412, 580, 3, ["3.1.2"], ["calculation"], "Calculate empirical formula of compound X (38.7% C, 9.68% H, 51.6% O)."),
    ("2003-jan-chm1-q3d", "3(d)", 7, 582, 675, 1, ["3.1.2"], ["calculation"], "Deduce molecular formula of X from empirical formula and Mr."),
    
    # Page 8: Question 4(a)-(d)
    ("2003-jan-chm1-q4ai", "4(a)(i)", 8, 80, 175, 1, ["3.1.3"], ["recall"], "Name strongest type of intermolecular attraction present in water."),
    ("2003-jan-chm1-q4aii", "4(a)(ii)", 8, 178, 260, 1, ["3.1.3"], ["recall"], "Name strongest type of intermolecular attraction present in hydrogen sulphide."),
    ("2003-jan-chm1-q4aiii", "4(a)(iii)", 8, 262, 340, 2, ["3.1.3"], ["analysis"], "Explain why boiling point of water is higher than that of hydrogen sulphide."),
    ("2003-jan-chm1-q4b", "4(b)", 8, 342, 435, 2, ["3.1.3"], ["recall"], "Define the term electronegativity."),
    ("2003-jan-chm1-q4c", "4(c)", 8, 438, 595, 3, ["3.2.2"], ["analysis"], "State and explain trend in electronegativity down Group II from Be to Ba."),
    ("2003-jan-chm1-q4di", "4(d)(i)", 8, 598, 650, 1, ["3.1.3"], ["recall"], "Give the type of bonding present in BeCl2."),
    ("2003-jan-chm1-q4dii", "4(d)(ii)", 8, 652, 700, 1, ["3.1.3"], ["recall"], "Give the type of bonding present in BaCl2."),
    ("2003-jan-chm1-q4diii", "4(d)(iii)", 8, 702, 780, 1, ["3.1.3"], ["analysis"], "Explain why the type of bonding is different in BeCl2 and BaCl2."),
    
    # Page 9: Question 4(e)
    ("2003-jan-chm1-q4ei", "4(e)(i)", 9, 80, 230, 3, ["3.2.2"], ["recall"], "Explain what is meant by amphoteric and write two equations with Be(OH)2."),
    ("2003-jan-chm1-q4eii", "4(e)(ii)", 9, 232, 335, 1, ["3.2.2"], ["analysis"], "Explain how Be(OH)2 behaviour is atypical of Group II metal hydroxides."),
    
    # Page 10: Question 5(a)-(c)
    ("2003-jan-chm1-q5a", "5(a)", 10, 80, 210, 2, ["3.1.1"], ["recall"], "Equation with state symbols for first ionisation energy of Na."),
    ("2003-jan-chm1-q5b", "5(b)", 10, 212, 380, 3, ["3.2.1"], ["analysis"], "State and explain general trend in first ionisation energies from Na to Ar."),
    ("2003-jan-chm1-q5c", "5(c)", 10, 382, 620, 5, ["3.2.1"], ["analysis"], "State how and explain why first ionisation energies of Al and S deviate from trend.")
]

MS_DATA = {
    "2003-jan-chm1-q1a": {
        "answers": "• <b>Proton:</b> Relative charge = <b>+1</b> (or 1+); Relative mass = <b>1</b> (1)<br>• <b>Neutron:</b> Relative charge = <b>0</b> (or no charge / neutral / zero); Relative mass = <b>1</b> (1)<br>• <b>Electron:</b> Relative charge = <b>&minus;1</b> (or 1&minus;); Relative mass = <b>1/1800 to 1/2000</b> (or negligible / zero / 5.0 &times; 10<sup>&minus;4</sup> to 5.6 &times; 10<sup>&minus;4</sup>) (1)",
        "extra": "If 'g' in mass column &minus; wrong, penalise once.<br>Neutron relative mass: Not &minus;1.",
        "mark": 3,
        "spec": "3.1.1"
    },
    "2003-jan-chm1-q1b": {
        "answers": "• Mass number: <b>38</b> (1)<br>• Symbol: <b><sub>18</sub>Ar</b> (1)",
        "extra": "Allow numbers before or after Ar.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2003-jan-chm1-q1c": {
        "answers": "• S: <b>1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>4</sup></b> (1)<br>• S<sup>2&minus;</sup>: <b>1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>6</sup></b> (1)",
        "extra": "If use subscripts penalise once.<br>Allow upper case letters.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2003-jan-chm1-q1d": {
        "answers": "• Block: <b>p</b> (1)<br>• Explanation: <b>Highest energy or outer orbital is (3)p</b> OR <b>outer electron / valency electron in (3)p</b> (1)",
        "extra": "NOT 2p etc.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2003-jan-chm1-q1ei": {
        "answers": "• Bonding in Na<sub>2</sub>S: <b>Ionic</b> (1)<br>• Bonding in CS<sub>2</sub>: <b>Covalent</b> (1)",
        "extra": "Ignore other words such as dative / polar / co-ordinate.",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q1eii": {
        "answers": "• <b>Clear indication of electron transfer from Na to S</b> (1)<br>• <b>1e<sup>&minus;</sup> from each (of 2) Na atoms</b> OR <b>2e<sup>&minus;</sup> from 2 Na atoms</b> (1)",
        "extra": "QoL (Correct English).",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q1eiii": {
        "answers": "• <b>Correct covalent double bonds</b> (two shared pairs between each S and C, i.e. S=C=S) (1)<br>• <b>All correct including lone pairs</b> (two lone pairs on each S atom) (1)",
        "extra": "M2 tied to M1.<br>Allow all dots or all crosses.<br>Not separate electrons on S &minus; 2 lone pairs.",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q1eiv": {
        "answers": "<b>CS<sub>2</sub> + 2H<sub>2</sub>O &rarr; CO<sub>2</sub> + 2H<sub>2</sub>S</b> (1)",
        "extra": "Ignore state symbols even if wrong.",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q2a": {
        "answers": "• Moles of HCl = 19.6 / 36.5 = <b>0.537</b> (mol) (1)<br>• Concentration = 0.537 / 0.25 (1)<br>• = <b>2.15</b> (mol dm<sup>&minus;3</sup>) (1)",
        "extra": "Allow 2.14 to 2.15; min 2 d.p.<br>Ignore wrong units.<br>AE: lose 1 mark.<br>Consequential on incorrect M<sub>r</sub>.",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q2bi": {
        "answers": "• Moles HCl = (21.7 / 1000) &times; 0.263 = <b>5.7(1) &times; 10<sup>&minus;3</sup></b> (mol) (1)",
        "extra": "Allow 5.7 to 5.71 &times; 10<sup>&minus;3</sup>.",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q2bii": {
        "answers": "• Moles M<sub>2</sub>CO<sub>3</sub> = (5.71 &times; 10<sup>&minus;3</sup>) / 2 = <b>2.85 &times; 10<sup>&minus;3</sup></b> (mol) (1)",
        "extra": "Consequential on (b)(i).",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q2biii": {
        "answers": "• M<sub>r</sub> = 0.394 / (2.85 &times; 10<sup>&minus;3</sup>) = <b>138</b> (1)",
        "extra": "Allow 138 to 138.2.<br>Consequential on (b)(ii).",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q2biv": {
        "answers": "• 138 &minus; 60 = <b>78</b> (1)<br>• 78 / 2 = <b>39</b> (1)<br>• Identity of M: <b>Potassium</b> OR <b>K</b> OR <b>K<sup>+</sup></b> (1)",
        "extra": "Consequential on M<sub>r</sub>.<br>If 78 = A<sub>r</sub>, M = Selenium.",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q3a": {
        "answers": "<b>Ideal gas equation</b> (or ideal gas law) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q3b": {
        "answers": "• <i>n</i> = <i>pV</i> / <i>RT</i> (1)<br>• = (110 000 &times; 2.34 &times; 10<sup>&minus;4</sup>) / (8.31 &times; 473) (1)<br>• = <b>6.55 &times; 10<sup>&minus;3</sup></b> (mol) (allow 6.5 &times; 10<sup>&minus;3</sup> to 6.6 &times; 10<sup>&minus;3</sup>) (1)<br>• M<sub>r</sub> = <i>m</i> / <i>n</i> = 0.406 / (6.55 &times; 10<sup>&minus;3</sup>) = <b>62</b> (allow 61.5 to 62.5) (1)",
        "extra": "If wrote n = RT/pV zero here, can score M<sub>r</sub>.<br>Ignore units.<br>Min 2 sig figs.<br>Consequential on moles.",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q3c": {
        "answers": "• % Oxygen = 100 &minus; (38.7 + 9.68) = <b>51.6(2)%</b> (1)<br>• Moles: C = 38.7 / 12 = 3.23; H = 9.68 / 1 = 9.68; O = 51.62 / 16 = 3.23 (1)<br>• Ratio = 1 : 3 : 1 &there4; <b>CH<sub>3</sub>O</b> (1)",
        "extra": "Correct empirical formula earns all 3 marks.<br>If no % O or wrong A<sub>r</sub> used then max 1.",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q3d": {
        "answers": "• (62 / 31) &times; CH<sub>3</sub>O = <b>C<sub>2</sub>H<sub>6</sub>O<sub>2</sub></b> (1)",
        "extra": "Consequential on (b) and (c).",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-jan-chm1-q4ai": {
        "answers": "<b>Hydrogen bonding</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q4aii": {
        "answers": "<b>van der Waals</b> OR <b>dipole&minus;dipole</b> (1)",
        "extra": "Allow London forces / dispersion forces / permanent dipole interaction.<br>Must not be '2 dipoles' or 'temporary dipole-dipole'.",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q4aiii": {
        "answers": "• <b>H-bonding is stronger</b> (1)<br>• <b>More energy / higher temperature needed to break</b> (1)",
        "extra": "'H-bonding needs more energy to break' scores (2).",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q4b": {
        "answers": "• <b>Power / tendency / ability of an atom / element to attract / withdraw electron density / electrons</b> (1)<br>• <b>in / from a covalent bond</b> (1)",
        "extra": "To score M2 must have reasonable attempt at M1.<br>Not reference to 'an electron' for M1.<br>'Ability of an atom to gain and retain electrons in a covalent bond' scores 1 mark.",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q4c": {
        "answers": "• Trend: <b>Decreases</b> (1)<br>• Explanation: <b>Any 2 from:</b><br>&nbsp;&nbsp;&ndash; <b>Increased radius / size / number of shells</b> (1)<br>&nbsp;&nbsp;&ndash; <b>Increased shielding</b> (1)<br>&nbsp;&nbsp;&ndash; <b>Weaker attraction between nucleus and bonding pair / electrons</b> (1)",
        "extra": "Max 1 if trend wrong.<br>Any 2 out of 3 in explanation.",
        "mark": 3,
        "spec": "3.2.2"
    },
    "2003-jan-chm1-q4di": {
        "answers": "<b>Covalent</b> (1)",
        "extra": "Ignore other words such as dative, coordinate, polar.<br>Not 'ionic with covalent character'.",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q4dii": {
        "answers": "<b>Ionic</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q4diii": {
        "answers": "<b>Greater electronegativity difference in BaCl<sub>2</sub></b> OR <b>more charge separation</b> OR <b>reduced charge density / polarising power on barium cation (Ba<sup>2+</sup>)</b> OR <b>Be is more electronegative than Ba</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2003-jan-chm1-q4ei": {
        "answers": "• Explanation: <b>Reacts with / dissolves in / neutralises acids and bases / alkalis</b> OR <b>behaves as acid and base</b> (1)<br>• Equation 1: <b>Be(OH)<sub>2</sub> + 2H<sup>+</sup> &rarr; Be<sup>2+</sup> + 2H<sub>2</sub>O</b> (or [Be(H<sub>2</sub>O)<sub>4</sub>]<sup>2+</sup>) (1)<br>• Equation 2: <b>Be(OH)<sub>2</sub> + 2OH<sup>&minus;</sup> &rarr; [Be(OH)<sub>4</sub>]<sup>2&minus;</sup></b> (1)",
        "extra": "Any example must be correct substance.<br>Accept equations with any acid / base.<br>Do not accept coordination number other than 4.",
        "mark": 3,
        "spec": "3.2.2"
    },
    "2003-jan-chm1-q4eii": {
        "answers": "<b>Others do not react with / dissolve in base / alkali</b> OR <b>others not amphoteric</b> OR <b>others only / always basic</b> OR <b>others only react with acids</b> (1)",
        "extra": "'Only' or implied from context.",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2003-jan-chm1-q5a": {
        "answers": "<b>Na(g) &rarr; Na<sup>+</sup>(g) + e<sup>&minus;</sup></b> (or Na(g) + e<sup>&minus;</sup> &rarr; Na<sup>+</sup>(g) + 2e<sup>&minus;</sup>)<br>• Equation (1)<br>• State symbols (1)",
        "extra": "'-' on electron not essential.<br>Ignore state symbols on electrons.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2003-jan-chm1-q5b": {
        "answers": "• Trend: <b>Increases</b> (1)<br>• Explanation:<br>&nbsp;&nbsp;&ndash; <b>Increased nuclear charge / proton number</b> (1)<br>&nbsp;&nbsp;&ndash; <b>Stronger attraction between nucleus and (outer) electron(s)</b> (1)",
        "extra": "If trend wrong: can award M2 and M3 if correct.",
        "mark": 3,
        "spec": "3.2.1"
    },
    "2003-jan-chm1-q5c": {
        "answers": "• Deviation: <b>(Both values) too low / drop in value</b> (1)<br>• Explanation for Al:<br>&nbsp;&nbsp;&ndash; <b>e<sup>&minus;</sup> removed from (3)p orbital</b> (1)<br>&nbsp;&nbsp;&ndash; <b>e<sup>&minus;</sup> / orbital is higher in energy / further away / better shielded (by 3s electrons) than 3s</b> (1)<br>• Explanation for S:<br>&nbsp;&nbsp;&ndash; <b>e<sup>&minus;</sup> removed from (3)p electron pair</b> (1)<br>&nbsp;&nbsp;&ndash; <b>repulsion between paired electrons (reduces energy required)</b> (1)",
        "extra": "If deviation wrong: allow M2 and M4; if M3 and/or M5 right can score.<br>If used 'd' rather than 'p' orbital: lose M2 & M4 but may get M3, M5.",
        "mark": 5,
        "spec": "3.2.1"
    }
}

def crop_question_image(doc, page_num, y0, y1, out_path, x0=35, x1=545, scale=2.0):
    page = doc[page_num - 1]
    rect = fitz.Rect(x0, max(0, y0), x1, min(page.rect.height, y1))
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=rect)
    im = Image.open(fitz.io.BytesIO(pix.tobytes("png")))
    im.convert("RGB").save(out_path, quality=90)
    return out_path

def main():
    print(f"Opening QP: {QP_PATH}")
    doc = fitz.open(QP_PATH)
    
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    # Ensure paper entry exists
    papers = [p for p in db["papers"] if p["id"] != PAPER_INFO["id"]]
    papers.append(PAPER_INFO)
    db["papers"] = papers
    
    # Remove any existing questions for this paper to allow clean update
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
    new_questions = []
    
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        sub_id = q_label.replace("(", "").replace(")", "").replace(" ", "")
        q_img_rel = f"img/2003-jan-chm1/q_q{sub_id}.jpg"
        ms_img_rel = f"img/2003-jan-chm1/ms_q{sub_id}.jpg"
        
        q_img_abs = os.path.join(REPO_DIR, q_img_rel)
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel)
        
        # 1. Crop question image
        crop_question_image(doc, p_num, y0, y1, q_img_abs)
        
        # 2. Render modern official mark scheme table
        ms_item = MS_DATA.get(q_id, {})
        render_official_markscheme_image(
            question_label=q_label,
            answers_html=ms_item.get("answers", ""),
            extra_html=ms_item.get("extra", ""),
            marks=ms_item.get("mark", marks),
            spec_ref=ms_item.get("spec", topics[0] if topics else ""),
            output_path=ms_img_abs
        )
        
        # Format text markscheme for searchability
        ms_text = ms_item.get("answers", "").replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "").replace("&minus;", "-").replace("&times;", "x").replace("&rarr;", "->").replace("&Sigma;", "Sum ").replace("&Delta;", "Delta ").replace("&there4;", "therefore ").replace("&nbsp;", " ")
        if ms_item.get("extra"):
            ms_text += "\n\n[Extra Information]:\n" + ms_item.get("extra", "").replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "").replace("&minus;", "-").replace("&times;", "x").replace("&rarr;", "->")
            
        q_entry = {
            "id": q_id,
            "paper": PAPER_INFO["id"],
            "question": q_label,
            "marks": marks,
            "page": p_num,
            "topics": topics,
            "skills": skills,
            "summary": summary,
            "image": q_img_rel,
            "figures": [],
            "markscheme": ms_img_rel,
            "markscheme_text": ms_text
        }
        new_questions.append(q_entry)
        
    db["questions"].extend(new_questions)
    
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully processed {len(new_questions)} Section A questions for {PAPER_INFO['id']}.")

if __name__ == "__main__":
    main()

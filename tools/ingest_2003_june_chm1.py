"""
Ingestion script for 2003 June CHM1 (Section A only)
Excludes old-spec Section B essay question (Q5).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023200_d1fdd406.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-june-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-june-chm1",
    "year": 2003,
    "series": "June",
    "date": "2003-06-04",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 4 (Exam page 5): Q1
    ("2003-june-chm1-q1ai", "1(a)(i)", 4, 182, 235, 1, ["3.1.1"], ["recall"], "Complete electronic configuration of aluminium."),
    ("2003-june-chm1-q1aii", "1(a)(ii)", 4, 240, 310, 1, ["3.1.1"], ["recall"], "State block in Periodic Table to which aluminium belongs."),
    ("2003-june-chm1-q1b", "1(b)", 4, 335, 470, 2, ["3.1.3"], ["recall"], "Describe bonding in metals."),
    ("2003-june-chm1-q1c", "1(c)", 4, 490, 650, 3, ["3.1.3", "3.2.1"], ["analysis"], "Explain why melting point of magnesium is higher than that of sodium."),
    ("2003-june-chm1-q1d", "1(d)", 4, 670, 785, 2, ["3.1.3"], ["recall", "explanation"], "Explain how metals conduct electricity."),

    # Page 5 (Exam page 6): Q2
    ("2003-june-chm1-q2a", "2(a)", 5, 80, 175, 2, ["3.1.1"], ["recall"], "Give relative charge and relative mass of an electron."),
    ("2003-june-chm1-q2bi", "2(b)(i)", 5, 180, 255, 1, ["3.1.1"], ["recall"], "Give number of protons present in an atom of 54Cr."),
    ("2003-june-chm1-q2bii", "2(b)(ii)", 5, 260, 310, 1, ["3.1.1"], ["recall"], "Deduce number of neutrons present in an atom of 52Cr."),
    ("2003-june-chm1-q2biii", "2(b)(iii)", 5, 315, 395, 1, ["3.1.1"], ["recall"], "Information needed to calculate relative atomic mass of chromium from isotope masses."),
    ("2003-june-chm1-q2ci", "2(c)(i)", 5, 400, 520, 2, ["3.1.1"], ["recall", "explanation"], "Two reasons why it is necessary to ionise chromium atoms in mass spectrometry."),
    ("2003-june-chm1-q2cii", "2(c)(ii)", 5, 525, 580, 1, ["3.1.1"], ["recall"], "What is adjusted so each chromium isotope can be detected in turn."),
    ("2003-june-chm1-q2ciii", "2(c)(iii)", 5, 585, 715, 1, ["3.1.1"], ["explanation"], "Explain how adjustment enables isotopes of chromium to be separated."),

    # Page 6 (Exam page 7): Q2(d)
    ("2003-june-chm1-q2di", "2(d)(i)", 6, 80, 155, 1, ["3.1.2"], ["recall"], "State what is meant by the term empirical formula."),
    ("2003-june-chm1-q2dii", "2(d)(ii)", 6, 160, 330, 3, ["3.1.2"], ["calculation"], "Calculate empirical formula of chromium compound (28.4% Na, 32.1% Cr, remainder O)."),

    # Page 7 (Exam page 8): Q3
    ("2003-june-chm1-q3ai", "3(a)(i)", 7, 80, 195, 1, ["3.1.2"], ["recall"], "State the ideal gas equation."),
    ("2003-june-chm1-q3aii", "3(a)(ii)", 7, 200, 480, 4, ["3.1.2"], ["calculation"], "Calculate volume in cm3 occupied by 1.36 g of ethanol vapour at 100 kPa and 366 K."),
    ("2003-june-chm1-q3bi", "3(b)(i)", 7, 510, 630, 1, ["3.1.2"], ["recall"], "Balance equation for reaction between magnesium nitride and water."),
    ("2003-june-chm1-q3bii", "3(b)(ii)", 7, 635, 785, 3, ["3.1.2"], ["calculation"], "Calculate moles and number of molecules of NH3 in 0.263 g."),

    # Page 8 (Exam page 9): Q3(c)
    ("2003-june-chm1-q3c", "3(c)", 8, 80, 420, 4, ["3.1.2"], ["calculation"], "Calculate maximum mass of sodium carbonate obtained from 800 g of sodium chloride."),

    # Page 9 (Exam page 10): Q4
    ("2003-june-chm1-q4ai", "4(a)(i)", 9, 80, 215, 1, ["3.1.3"], ["recall"], "Property of atoms that causes a bond to be polar."),
    ("2003-june-chm1-q4aii", "4(a)(ii)", 9, 220, 455, 3, ["3.1.3"], ["explanation"], "Explain why HF has a higher boiling point than HCl in terms of intermolecular forces."),
    ("2003-june-chm1-q4b", "4(b)", 9, 465, 660, 2, ["3.1.3"], ["recall", "explanation"], "Explain how coordinate bond is formed when AlCl3 reacts with Cl-."),

    # Page 10 (Exam page 11): Q4(c)
    ("2003-june-chm1-q4c", "4(c)", 10, 80, 450, 4, ["3.1.3"], ["recall", "drawing"], "Draw shapes and state bond angles for PCl5 and PCl4+ ion.")
]

MS_DATA = {
    "2003-june-chm1-q1ai": {
        "answers": "<b>1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>1</sup></b> (1)",
        "extra": "Allow subscripted electron numbers.",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q1aii": {
        "answers": "<b>p (block)</b> (1)",
        "extra": "Allow upper or lower case 's' and 'p' in (a)(i) and (a)(ii).",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q1b": {
        "answers": "• Lattice of metal / +ve ions / cations / atoms (1)<br>• (Surrounded by) <b>delocalised electrons</b> (1)",
        "extra": "Accept regular array / close packed / tightly packed / uniformly arranged.<br>Not: +ve nuclei/centres.<br>Note: Description as a 'giant ionic lattice' = CE.",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-june-chm1-q1c": {
        "answers": "Any three from:<br>• Greater nuclear or ionic charge or more protons (1)<br>• Smaller atoms / ions (1)<br>• More delocalised electrons / e<sup>&minus;</sup> in sea of e<sup>&minus;</sup> / free e<sup>&minus;</sup> (1)<br>• Stronger attraction between ions and delocalised / free electrons etc. (1)",
        "extra": "[Max 3]<br>Accept greater charge density for either M1 or M2.<br>Note: 'intermolecular attraction/forces' or covalent molecules = CE.<br>Accept stronger 'electrostatic attraction' if phrase described elsewhere.<br>Ignore references to m/z values.<br>If Mg or Na compared to Al, rather than each other, max 2.<br>If reference to 'ionic bonding', max 2.<br>Treat description that is effectively one for Ionisation Energy as a 'contradiction'.",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2003-june-chm1-q1d": {
        "answers": "• (Delocalised) electrons (1)<br>• Move / flow in a given direction (idea of moving non-randomly) OR under the influence of applied pd (1)",
        "extra": "QoL mark.<br>Allow 'flow through metal'.<br>Not: 'carry the charge'; 'along the layers'; 'move through the metal'.",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-june-chm1-q2a": {
        "answers": "• Relative charge: <b>&minus;1</b> (1)<br>• Relative mass: <b>&le; 1/1800</b> OR <b>&le; 5.55 &times; 10<sup>&minus;4</sup></b> (1)",
        "extra": "Accept zero / negligible for relative mass.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q2bi": {
        "answers": "Protons = <b>24</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q2bii": {
        "answers": "Neutrons = <b>28</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q2biii": {
        "answers": "Need (relative) <b>abundance</b> OR peak height OR intensity / amount / number / % / fraction of each isotope (1)",
        "extra": "Not: 'ratio of each isotope'.",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q2ci": {
        "answers": "Any two reasons:<br>• Reason 1: To allow particles to be accelerated / deflected / detected or to count (1)<br>• Reason 2: To generate a current in the detector / charged particles (1)",
        "extra": "Not: 'to allow m/z to be measured'.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q2cii": {
        "answers": "<b>Magnetic field</b> OR <b>electric field</b> OR <b>electromagnet</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q2ciii": {
        "answers": "<b>Deflection depends on mass or m/z</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2003-june-chm1-q2di": {
        "answers": "(Simplest) <b>ratio of atoms of each element</b> in compound (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-june-chm1-q2dii": {
        "answers": "• % oxygen = 100 &minus; (28.4 + 32.1) = <b>39.5%</b> (1)<br>• Moles: Na = 28.4/23 = 1.23; Cr = 32.1/52 = 0.617; O = 39.5/16 = 2.47 (1)<br>• Ratio = 2 : 1 : 4 &rArr; empirical formula = <b>Na<sub>2</sub>CrO<sub>4</sub></b> (1)",
        "extra": "If % oxygen not calculated, only M2 available.<br>If A<sub>r</sub> values wrong, only M1 available.",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-june-chm1-q3ai": {
        "answers": "<b>pV = nRT</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-june-chm1-q3aii": {
        "answers": "• Moles ethanol: <i>n</i> = 1.36 / 46 = <b>0.0296 mol</b> (1)<br>• <i>V</i> = <i>nRT / p</i> = (0.0296 &times; 8.31 &times; 366) / 100 000 (1)<br>• <i>V</i> = 8.996 &times; 10<sup>&minus;4</sup> m<sup>3</sup> (1)<br>• Volume = <b>899 cm<sup>3</sup></b> (or 900 cm<sup>3</sup>) (1)",
        "extra": "Range = 895 &minus; 905 cm<sup>3</sup>.<br>If <i>V = p/nRT</i> lose M3 and M4.<br>If final answer = 0.899 award (2 + M1); if = 0.899 dm<sup>3</sup> or 912 award (3 + M1).<br>If 1.36 or 46 or 46/1.36 used as number of moles, M2 and M4 not available.<br>If pressure = 100 then deduct M3 and mark consequentially.",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2003-june-chm1-q3bi": {
        "answers": "<b>Mg<sub>3</sub>N<sub>2</sub> + 6H<sub>2</sub>O &rarr; 3Mg(OH)<sub>2</sub> + 2NH<sub>3</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-june-chm1-q3bii": {
        "answers": "• Moles NH<sub>3</sub> = 0.263 / 17 = <b>0.0155 mol</b> (1)<br>• Number of molecules = 0.0155 &times; 6.02 &times; 10<sup>23</sup> (1)<br>• = <b>9.31 &times; 10<sup>21</sup></b> (1)",
        "extra": "Range 9.2 &times; 10<sup>21</sup> to 9.4 &times; 10<sup>21</sup>.<br>M2 and M3 consequential on M1 (min 2 sig figs).",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-june-chm1-q3c": {
        "answers": "• Moles NaCl = 800 / 58.5 = <b>13.68 mol</b> (1)<br>• Moles NaHCO<sub>3</sub> = 13.68 mol (1)<br>• Moles Na<sub>2</sub>CO<sub>3</sub> = 13.68 / 2 = <b>6.84 mol</b> (1)<br>• Mass Na<sub>2</sub>CO<sub>3</sub> = 6.84 &times; 106 = <b>725 g</b> (1)",
        "extra": "Range = 724 &minus; 727 g.<br>1450 g (range 1448 &minus; 1454) is worth 3 marks.<br>Accept any valid calculation method (e.g. reacting masses, direct 2:1 ratio for NaCl : Na<sub>2</sub>CO<sub>3</sub>).",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2003-june-chm1-q4ai": {
        "answers": "<b>Electronegativity (difference)</b> OR suitable description (1)",
        "extra": "Accept 'F and Cl are highly electronegative'.<br>Not: 'both atoms are highly electronegative'.",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2003-june-chm1-q4aii": {
        "answers": "• HF has <b>hydrogen bonding</b> (1)<br>• HCl has (permanent) <b>dipole-dipole forces</b> OR <b>van der Waals' forces</b> (1)<br>• Hydrogen bonding is <b>stronger</b> than dipole-dipole / van der Waals' forces (1)",
        "extra": "Accept statement that HF must have stronger IMF, even if no IMFs identified.<br>Explanation must be clearly based on intermolecular forces.<br>Note: if explanation is clearly intramolecular = CE.",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2003-june-chm1-q4b": {
        "answers": "• <b>Electron pair</b> OR <b>lone pair</b> donated (1)<br>• From <b>chloride ion</b> to <b>Al</b> (or AlCl<sub>3</sub>) (1)",
        "extra": "Do not accept 'donation of electron(s)'.<br>M1 can be earned by general explanation of coordinate bonding, even if pair said to come from Al.<br>Ignore missing charge.",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-june-chm1-q4c": {
        "answers": "• <b>PCl<sub>5</sub>:</b> Trigonal bipyramidal structure; one solid linear Cl&minus;P&minus;Cl bond (1); Bond angles: <b>90&deg; and 120&deg;</b> (1)<br>• <b>PCl<sub>4</sub><sup>+</sup>:</b> Tetrahedral structure; no solid linear Cl&minus;P&minus;Cl bond, '+' charge (1); Bond angle: <b>109&deg; or 109.5&deg;</b> (1)",
        "extra": "",
        "mark": 4,
        "spec": "3.1.3"
    }
}

def main():
    print("Ingesting 2003 June CHM1...")
    doc = fitz.open(QP_PATH)
    
    # 1. Render markscheme images
    print("Generating official markscheme table images...")
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        ms = MS_DATA.get(q_id)
        if ms:
            out_img = os.path.join(IMG_DIR, f"ms_{q_id.split('-')[-1]}.png")
            render_official_markscheme_image(
                question_label=q_label,
                answers_html=ms["answers"],
                extra_html=ms.get("extra", ""),
                marks=ms["mark"],
                spec_ref=ms.get("spec", ""),
                output_path=out_img
            )
            
    # 2. Crop questions
    print("Cropping question images from QP...")
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        out_jpg = os.path.join(IMG_DIR, f"q_{q_id.split('-')[-1]}.jpg")
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        im.save(out_jpg, format="JPEG", quality=92)
        
    # 3. Update questions.json
    print("Updating questions.json...")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)
        
    # Add paper if not present
    papers = {p["id"]: p for p in db.get("papers", [])}
    papers[PAPER_INFO["id"]] = PAPER_INFO
    db["papers"] = list(papers.values())
    
    # Remove any existing questions for this paper
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
    # Append new questions
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        short_id = q_id.split('-')[-1]
        ms = MS_DATA.get(q_id, {})
        q_obj = {
            "id": q_id,
            "paper": PAPER_INFO["id"],
            "question": q_label,
            "page": p_num,
            "marks": marks,
            "topics": topics,
            "skills": skills,
            "summary": summary,
            "image": f"img/2003-june-chm1/q_{short_id}.jpg",
            "markscheme_image": f"img/2003-june-chm1/ms_{short_id}.png",
            "markscheme_text": ms.get("answers", "").replace("<br>", "\n").replace("<b>", "**").replace("</b>", "**").replace("&minus;", "-").replace("&times;", "x").replace("&le;", "<=").replace("&ge;", ">=").replace("&rArr;", "=>")
        }
        db["questions"].append(q_obj)
        
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully ingested {len(QUESTIONS_DEF)} questions for {PAPER_INFO['id']}!")

if __name__ == "__main__":
    main()

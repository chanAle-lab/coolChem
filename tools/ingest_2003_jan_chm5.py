"""
Ingestion script for 2003 January CHM5 (Section A only)
Excludes old-spec Section B essay questions (Q6 to Q9).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463561_eebd3925.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-jan-chm5")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-jan-chm5",
    "year": 2003,
    "series": "January",
    "date": "2003-01-24",
    "code": "CHM5",
    "unit": "Unit 5: Thermodynamics and Further Inorganic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour 30 mins"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2003-jan-chm5-q1ai", "1(a)(i)", 2, 150, 285, 2, ["3.1.3"], ["recall"], "State the shape and bond angle of the AlCl3 molecule."),
    ("2003-jan-chm5-q1aii", "1(a)(ii)", 2, 288, 415, 2, ["3.1.3"], ["analysis"], "Sketch structure of Al2Cl6 and mark the value of one bond angle."),
    ("2003-jan-chm5-q1aiii", "1(a)(iii)", 2, 418, 515, 2, ["3.1.3"], ["analysis"], "Explain how two AlCl3 molecules bond together to form Al2Cl6."),
    ("2003-jan-chm5-q1bi", "1(b)(i)", 2, 518, 645, 3, ["3.2.6"], ["practical", "recall"], "Observations, major species and pH when anhydrous AlCl3 is added to water."),
    ("2003-jan-chm5-q1bii", "1(b)(ii)", 2, 648, 790, 4, ["3.2.6"], ["practical", "recall"], "Observations and equation when aqueous sodium carbonate is added to aqueous AlCl3."),
    
    # Page 5: Question 2
    ("2003-jan-chm5-q2a", "2(a)", 5, 80, 315, 4, ["3.2.4"], ["recall"], "Equations and pH when Na2O and SO2 are added separately to water."),
    ("2003-jan-chm5-q2bi", "2(b)(i)", 5, 318, 405, 1, ["3.2.4"], ["recall"], "Equation for reaction of SiO2 and carbon in chlorine forming SiCl4 and CO."),
    ("2003-jan-chm5-q2bii", "2(b)(ii)", 5, 408, 525, 3, ["3.2.4"], ["practical", "recall"], "Observations and equation when silicon tetrachloride is added to water."),
    ("2003-jan-chm5-q2biii", "2(b)(iii)", 5, 528, 670, 3, ["3.1.3"], ["analysis"], "Explain in terms of bonding why SiCl4 has a lower melting point than PCl5."),
    
    # Page 6: Question 3(a)
    ("2003-jan-chm5-q3ai", "3(a)(i)", 6, 80, 590, 6, ["3.1.8"], ["calculation"], "Calculate standard enthalpy change and entropy change for extraction of iron."),
    ("2003-jan-chm5-q3aii", "3(a)(ii)", 6, 592, 695, 3, ["3.1.8"], ["analysis"], "Explain why the reaction of Fe2O3 with CO is feasible at all temperatures."),
    
    # Page 7: Question 3(b)-(c)
    ("2003-jan-chm5-q3b", "3(b)", 7, 80, 305, 3, ["3.1.8"], ["calculation"], "Calculate temperature at which Fe2O3 + 3C reaction becomes feasible."),
    ("2003-jan-chm5-q3c", "3(c)", 7, 308, 450, 3, ["3.1.8"], ["calculation"], "Calculate temperature at which standard free-energy change is equal for both reactions."),
    
    # Page 8: Question 4(a)-(b)
    ("2003-jan-chm5-q4a", "4(a)", 8, 80, 395, 1, ["3.1.11"], ["recall"], "Name standard reference electrode against which electrode potentials are measured."),
    ("2003-jan-chm5-q4bi", "4(b)(i)", 8, 398, 485, 1, ["3.1.11"], ["recall"], "Function of platinum electrode when measuring Fe3+/Fe2+ potential."),
    ("2003-jan-chm5-q4bii", "4(b)(ii)", 8, 488, 605, 2, ["3.1.11"], ["recall"], "Standard conditions which apply to Fe3+(aq)/Fe2+(aq) electrode."),
    
    # Page 9: Question 4(c)-(e)
    ("2003-jan-chm5-q4c", "4(c)", 9, 80, 290, 3, ["3.1.11"], ["calculation", "recall"], "Calculate EMF and write spontaneous equation for Pt|H2SO3,SO4 2-||MnO4-,Mn2+|Pt cell."),
    ("2003-jan-chm5-q4di", "4(d)(i)", 9, 292, 345, 1, ["3.1.11"], ["analysis"], "Identify the strongest oxidising agent in the electrode potential table."),
    ("2003-jan-chm5-q4dii", "4(d)(ii)", 9, 348, 435, 2, ["3.1.11"], ["analysis"], "Species in table that could convert Fe2+ to Fe3+ but not Mn2+ to MnO4-."),
    ("2003-jan-chm5-q4e", "4(e)", 9, 438, 520, 2, ["3.1.11"], ["analysis"], "Deduce cell representation that would give standard EMF of 0.93 V."),
    
    # Page 10: Question 5
    ("2003-jan-chm5-q5a", "5(a)", 10, 80, 160, 1, ["3.2.5"], ["recall"], "Give one example of a bidentate ligand."),
    ("2003-jan-chm5-q5b", "5(b)", 10, 162, 240, 1, ["3.2.5"], ["recall"], "Give one example of a linear complex ion formed by a transition metal."),
    ("2003-jan-chm5-q5c", "5(c)", 10, 242, 340, 2, ["3.2.5"], ["recall"], "Equation for ligand substitution changing both coordination number and charge."),
    ("2003-jan-chm5-q5d", "5(d)", 10, 342, 445, 2, ["3.2.5"], ["recall"], "Equation for ligand substitution keeping coordination number and charge constant."),
    ("2003-jan-chm5-q5e", "5(e)", 10, 448, 580, 3, ["3.2.5"], ["recall", "analysis"], "Equation for [Co(H2O)6]2+ with EDTA4- and explain stability in terms of entropy.")
]

MS_DATA = {
    "2003-jan-chm5-q1ai": {
        "answers": "• Shape: <b>Trigonal planar</b> (1)<br>• Bond angle: <b>120&deg;</b> (1)",
        "extra": "Linked to correct shape.",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm5-q1aii": {
        "answers": "• Structure sketch showing two bridging Cl atoms with dative covalent / co-ordinate bonds between Al and Cl (1)<br>• Bond angle: <b>109&deg;28'</b> (allow 104&deg; to 109.5&deg; or correct values) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm5-q1aiii": {
        "answers": "• <b>Lone electron pair on chlorine</b> (1)<br>• <b>Electron deficient Al (accepts lone pair)</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2003-jan-chm5-q1bi": {
        "answers": "• Observation: <b>Dissolves / exothermic reaction</b> (1)<br>• Major species: <b>[Al(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup></b> (1)<br>• pH: <b>2 / 3 / 4</b> (1)",
        "extra": "Mark separately.",
        "mark": 3,
        "spec": "3.2.6"
    },
    "2003-jan-chm5-q1bii": {
        "answers": "• Observations: <b>Gas evolved</b> (1) and <b>white precipitate formed</b> (1)<br>• Equation: <b>2[Al(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + 3CO<sub>3</sub><sup>2&minus;</sup> &rarr; 2[Al(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub>] + 3CO<sub>2</sub> + 3H<sub>2</sub>O</b><br>&nbsp;&nbsp;&ndash; Correct species (1)<br>&nbsp;&nbsp;&ndash; Balanced (1)",
        "extra": "Mark separately.",
        "mark": 4,
        "spec": "3.2.6"
    },
    "2003-jan-chm5-q2a": {
        "answers": "• Sodium oxide:<br>&nbsp;&nbsp;&ndash; Equation: <b>Na<sub>2</sub>O + H<sub>2</sub>O &rarr; 2NaOH</b> (1)<br>&nbsp;&nbsp;&ndash; pH: <b>14</b> (allow 13&ndash;14) (1)<br>• Sulphur dioxide:<br>&nbsp;&nbsp;&ndash; Equation: <b>SO<sub>2</sub> + H<sub>2</sub>O &rarr; H<sub>2</sub>SO<sub>3</sub></b> (1)<br>&nbsp;&nbsp;&ndash; pH: <b>1 &minus; 3</b> (1)",
        "extra": "",
        "mark": 4,
        "spec": "3.2.4"
    },
    "2003-jan-chm5-q2bi": {
        "answers": "<b>SiO<sub>2</sub> + 2C + 2Cl<sub>2</sub> &rarr; SiCl<sub>4</sub> + 2CO</b><br>(or SiO<sub>2</sub> + C + 2Cl<sub>2</sub> &rarr; SiCl<sub>4</sub> + CO<sub>2</sub>) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.4"
    },
    "2003-jan-chm5-q2bii": {
        "answers": "• Observations: <b>(Gelatinous) solid / gel / white precipitate formed</b> (1); <b>Exothermic reaction OR gas evolved</b> (1)<br>• Equation: <b>SiCl<sub>4</sub> + 2H<sub>2</sub>O &rarr; SiO<sub>2</sub> + 4HCl</b> (or SiCl<sub>4</sub> + 4H<sub>2</sub>O &rarr; Si(OH)<sub>4</sub> + 4HCl) (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.4"
    },
    "2003-jan-chm5-q2biii": {
        "answers": "• <b>SiCl<sub>4</sub> is molecular with weak van der Waals forces between molecules</b> (1)<br>• <b>PCl<sub>5</sub> is ionic with ion&minus;ion attractions</b> (1)<br>• <b>Ion&minus;ion attractions are stronger than van der Waals forces</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2003-jan-chm5-q3ai": {
        "answers": "• <b>Standard enthalpy change:</b><br>&nbsp;&nbsp;&ndash; &Delta;<i>H</i><sub>R</sub> = &Sigma;&Delta;<i>H</i><sub>f</sub>(products) &minus; &Sigma;&Delta;<i>H</i><sub>f</sub>(reactants) (or cycle) (1)<br>&nbsp;&nbsp;&ndash; = [2(0) + 3(&minus;393.5)] &minus; [&minus;824.2 + 3(&minus;110.5)] (1)<br>&nbsp;&nbsp;&ndash; = <b>&minus;24.8</b> (kJ mol<sup>&minus;1</sup>) (1) [allow +24.8 max 1]<br><br>• <b>Standard entropy change:</b><br>&nbsp;&nbsp;&ndash; &Delta;<i>S</i> = &Sigma;<i>S</i>(products) &minus; &Sigma;<i>S</i>(reactants) (1)<br>&nbsp;&nbsp;&ndash; = [2(27.3) + 3(213.6)] &minus; [87.4 + 3(197.6)] = 695.4 &minus; 680.2 (1)<br>&nbsp;&nbsp;&ndash; = <b>+15.2</b> (J K<sup>&minus;1</sup> mol<sup>&minus;1</sup>) (1) [allow &minus;15.2 max 1]",
        "extra": "",
        "mark": 6,
        "spec": "3.1.8"
    },
    "2003-jan-chm5-q3aii": {
        "answers": "• <b>&Delta;<i>G</i> = &Delta;<i>H</i> &minus; <i>T</i>&Delta;<i>S</i></b> (1)<br>• <b>&Delta;<i>H</i> is negative and &minus;<i>T</i>&Delta;<i>S</i> is negative (since &Delta;<i>S</i> is positive)</b> (1)<br>• <b>Hence &Delta;<i>G</i> is always negative / feasible when &Delta;<i>G</i> &le; 0</b> (1)",
        "extra": "Consequential on signs in (a)(i).",
        "mark": 3,
        "spec": "3.1.8"
    },
    "2003-jan-chm5-q3b": {
        "answers": "• &Delta;<i>G</i> = 0 = &Delta;<i>H</i> &minus; <i>T</i>&Delta;<i>S</i> &there4; &Delta;<i>H</i> = <i>T</i>&Delta;<i>S</i> (1)<br>• <i>T</i> = &Delta;<i>H</i> / &Delta;<i>S</i> = (492.7 &times; 1000) / 542.6 (1)<br>• = <b>908 K</b> (1)",
        "extra": "Penalise missing 1000 by one mark.",
        "mark": 3,
        "spec": "3.1.8"
    },
    "2003-jan-chm5-q3c": {
        "answers": "• &Delta;<i>G</i>(b) = &Delta;<i>G</i>(a) &rarr; (492.7 &times; 10<sup>3</sup> &minus; <i>T</i> &times; 542.6) = (&minus;24.8 &times; 10<sup>3</sup> &minus; <i>T</i> &times; 15.2) (1)<br>• 517.5 &times; 10<sup>3</sup> = 527.4 <i>T</i> (1)<br>• <i>T</i> = <b>981.2 K</b> (allow 980 to 982 K) (1)",
        "extra": "Penalise missing 1000 by one mark.",
        "mark": 3,
        "spec": "3.1.8"
    },
    "2003-jan-chm5-q4a": {
        "answers": "<b>(Standard) hydrogen (electrode)</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.11"
    },
    "2003-jan-chm5-q4bi": {
        "answers": "<b>To allow transfer of electrons / provide a reaction surface</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.11"
    },
    "2003-jan-chm5-q4bii": {
        "answers": "• Temperature: <b>298 K</b> (1)<br>• Concentration: <b>Both Fe<sup>3+</sup>(aq) and Fe<sup>2+</sup>(aq) have a concentration of 1 mol dm<sup>&minus;3</sup></b> [OR [H<sup>+</sup>] = 1 mol dm<sup>&minus;3</sup>] (1)",
        "extra": "QoL mark for point 2.<br>NOT zero current or 100 kPa.",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2003-jan-chm5-q4c": {
        "answers": "• Cell e.m.f. = 1.51 &minus; (+0.17) = <b>+1.34 V</b> (1)<br>• Equation: <b>2MnO<sub>4</sub><sup>&minus;</sup> + 5H<sub>2</sub>SO<sub>3</sub> &rarr; 2Mn<sup>2+</sup> + 5SO<sub>4</sub><sup>2&minus;</sup> + 3H<sub>2</sub>O + 4H<sup>+</sup></b><br>&nbsp;&nbsp;&ndash; Correct species / order (1)<br>&nbsp;&nbsp;&ndash; Balanced and cancelled (1)",
        "extra": "Allow one mark for 2MnO4- + 5H2SO3 -> 2Mn2+ + 5SO4 2-.",
        "mark": 3,
        "spec": "3.1.11"
    },
    "2003-jan-chm5-q4di": {
        "answers": "<b>Ce<sup>4+</sup>(aq)</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.11"
    },
    "2003-jan-chm5-q4dii": {
        "answers": "• <b>VO<sub>2</sub><sup>+</sup>(aq)</b> (1)<br>• <b>Cl<sub>2</sub></b> (1)",
        "extra": "Penalise additional answers to zero.",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2003-jan-chm5-q4e": {
        "answers": "<b>Pt | Fe<sup>2+</sup>(aq), Fe<sup>3+</sup>(aq) || Ce<sup>4+</sup>(aq), Ce<sup>3+</sup>(aq) | Pt</b><br>• Correct species (1)<br>• Correct order (1)",
        "extra": "Deduct one mark for each error.",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2003-jan-chm5-q5a": {
        "answers": "<b>C<sub>2</sub>O<sub>4</sub><sup>2&minus;</sup></b> (ethanedioate) OR <b>H<sub>2</sub>NCH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub></b> (ethane-1,2-diamine) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2003-jan-chm5-q5b": {
        "answers": "<b>[AgCl<sub>2</sub>]<sup>&minus;</sup></b> OR <b>[Ag(CN)<sub>2</sub>]<sup>&minus;</sup></b> OR <b>[Ag(NH<sub>3</sub>)<sub>2</sub>]<sup>+</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2003-jan-chm5-q5c": {
        "answers": "<b>[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 4Cl<sup>&minus;</sup> &rarr; [CoCl<sub>4</sub>]<sup>2&minus;</sup> + 6H<sub>2</sub>O</b><br>• Correct complex species (1)<br>• Balanced equation (1)",
        "extra": "Only allow if species correct.",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-jan-chm5-q5d": {
        "answers": "<b>[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + 6NH<sub>3</sub> &rarr; [Co(NH<sub>3</sub>)<sub>6</sub>]<sup>2+</sup> + 6H<sub>2</sub>O</b><br>• Correct complex species (1)<br>• Balanced equation (1)",
        "extra": "Only allow if species correct.",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2003-jan-chm5-q5e": {
        "answers": "• Equation: <b>[Co(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup> + EDTA<sup>4&minus;</sup> &rarr; [Co(EDTA)]<sup>2&minus;</sup> + 6H<sub>2</sub>O</b> (1)<br>• Explanation:<br>&nbsp;&nbsp;&ndash; <b>More molecules / particles on right-hand side</b> (1)<br>&nbsp;&nbsp;&ndash; <b>Entropy increases (&Delta;<i>S</i> > 0)</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.5"
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
        
    papers = [p for p in db["papers"] if p["id"] != PAPER_INFO["id"]]
    papers.append(PAPER_INFO)
    db["papers"] = papers
    
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
    new_questions = []
    
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        sub_id = q_label.replace("(", "").replace(")", "").replace(" ", "")
        q_img_rel = f"img/2003-jan-chm5/q_q{sub_id}.jpg"
        ms_img_rel = f"img/2003-jan-chm5/ms_q{sub_id}.jpg"
        
        q_img_abs = os.path.join(REPO_DIR, q_img_rel)
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel)
        
        crop_question_image(doc, p_num, y0, y1, q_img_abs)
        
        ms_item = MS_DATA.get(q_id, {})
        render_official_markscheme_image(
            question_label=q_label,
            answers_html=ms_item.get("answers", ""),
            extra_html=ms_item.get("extra", ""),
            marks=ms_item.get("mark", marks),
            spec_ref=ms_item.get("spec", topics[0] if topics else ""),
            output_path=ms_img_abs
        )
        
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

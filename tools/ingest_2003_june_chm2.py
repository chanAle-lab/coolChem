"""
Ingestion script for 2003 June CHM2 (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023287_2344f672.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-june-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-june-chm2",
    "year": 2003,
    "series": "June",
    "date": "2003-06-04",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2 (Exam page 2): Q1
    ("2003-june-chm2-q1a", "1(a)", 2, 180, 395, 4, ["3.2.3"], ["recall"], "Identify two reducing agents in Blast Furnace and write equations for formation of iron."),
    ("2003-june-chm2-q1b", "1(b)", 2, 400, 520, 4, ["3.2.3"], ["recall"], "Two equations for batch extraction of titanium from TiO2."),
    ("2003-june-chm2-q1c", "1(c)", 2, 525, 785, 4, ["3.2.3"], ["recall", "explanation"], "How metals extracted from sulphide ores and explain pollution problems."),

    # Page 5 (Exam page 5): Q2
    ("2003-june-chm2-q2a", "2(a)", 5, 80, 175, 1, ["3.1.7"], ["recall"], "What happens to oxidising agent during redox reaction in terms of electrons."),
    ("2003-june-chm2-q2bi", "2(b)(i)", 5, 180, 325, 2, ["3.1.7"], ["recall"], "Identify oxidising and reducing agent in reaction of SO2 with Ag+."),
    ("2003-june-chm2-q2bii", "2(b)(ii)", 5, 330, 420, 1, ["3.1.7"], ["recall"], "Half-equation for conversion of sulphur dioxide to sulphate ions."),
    ("2003-june-chm2-q2ci", "2(c)(i)", 5, 425, 535, 1, ["3.1.7"], ["recall"], "Half-equation for oxidation of Fe2+ to Fe3+ by ClO3-."),
    ("2003-june-chm2-q2cii", "2(c)(ii)", 5, 540, 600, 1, ["3.1.7"], ["recall"], "Deduce oxidation state of chlorine in ClO3-."),
    ("2003-june-chm2-q2ciii", "2(c)(iii)", 5, 605, 665, 1, ["3.1.7"], ["recall"], "Half-equation for reduction of ClO3- to Cl- in acidic conditions."),
    ("2003-june-chm2-q2civ", "2(c)(iv)", 5, 670, 735, 1, ["3.1.7"], ["recall"], "Overall equation for oxidation of Fe2+ by ClO3-."),
    ("2003-june-chm2-q2d", "2(d)", 5, 740, 860, 2, ["3.2.3"], ["recall"], "Equation for removal of sulphur from impure iron and identify oxidising agent."),

    # Page 6 (Exam page 6): Q3(a)-(b)
    ("2003-june-chm2-q3ai", "3(a)(i)", 6, 80, 480, 2, ["3.1.5"], ["drawing"], "Sketch Maxwell-Boltzmann curve X for cooled gas sample."),
    ("2003-june-chm2-q3aii", "3(a)(ii)", 6, 485, 565, 2, ["3.1.5"], ["drawing"], "Sketch Maxwell-Boltzmann curve Y for gas sample at higher pressure."),
    ("2003-june-chm2-q3bi", "3(b)(i)", 6, 570, 725, 2, ["3.1.5"], ["recall"], "What must happen between molecules of A before they react to form B and C."),
    ("2003-june-chm2-q3bii", "3(b)(ii)", 6, 730, 850, 2, ["3.1.5"], ["explanation"], "Explain why decomposition of A is faster at higher temperatures."),

    # Page 7 (Exam page 7): Q3(c)
    ("2003-june-chm2-q3ci", "3(c)(i)", 7, 80, 495, 1, ["3.1.6"], ["explanation"], "Suggest why concentration of A remains constant after a time."),
    ("2003-june-chm2-q3cii", "3(c)(ii)", 7, 500, 665, 2, ["3.1.6"], ["explanation"], "Explain why concentration of A falls to a lower value at 320 K."),

    # Page 8 (Exam page 8): Q4(a)-(c)
    ("2003-june-chm2-q4a", "4(a)", 8, 80, 185, 1, ["3.1.4"], ["recall"], "Equation for complete combustion of propanone, C3H6O."),
    ("2003-june-chm2-q4bi", "4(b)(i)", 8, 190, 340, 1, ["3.1.2"], ["calculation"], "Calculate moles of propanone in 1.45 g."),
    ("2003-june-chm2-q4bii", "4(b)(ii)", 8, 345, 520, 2, ["3.1.4"], ["calculation"], "Calculate heat energy required to raise temperature of 100 g water from 293.1 K to 351.2 K."),
    ("2003-june-chm2-q4biii", "4(b)(iii)", 8, 525, 625, 2, ["3.1.4"], ["calculation"], "Calculate enthalpy of combustion of propanone in kJ mol-1."),
    ("2003-june-chm2-q4ci", "4(c)(i)", 8, 630, 755, 1, ["3.1.4"], ["explanation"], "Why experimental enthalpy value is very different from data book value."),
    ("2003-june-chm2-q4cii", "4(c)(ii)", 8, 760, 915, 2, ["3.1.4"], ["explanation"], "How enthalpy value differs if water formed is liquid instead of gas."),

    # Page 9 (Exam page 9): Q4(d)
    ("2003-june-chm2-q4d", "4(d)", 9, 80, 420, 3, ["3.1.4"], ["calculation"], "Calculate standard enthalpy of formation for liquid ethanethiol from combustion data.")
]

MS_DATA = {
    "2003-june-chm2-q1a": {
        "answers": "• Reducing agent 1: <b>C</b> (or coke) (1)<br>• Equation 1: <b>3C + Fe<sub>2</sub>O<sub>3</sub> &rarr; 3CO + 2Fe</b> (1) [or C + O<sub>2</sub> &rarr; CO<sub>2</sub>, C + &frac12;O<sub>2</sub> &rarr; CO, CO<sub>2</sub> + C &rarr; 2CO, 3C + 2Fe<sub>2</sub>O<sub>3</sub> &rarr; 3CO<sub>2</sub> + 4Fe]<br>• Reducing agent 2: <b>CO</b> (1)<br>• Equation 2: <b>3CO + Fe<sub>2</sub>O<sub>3</sub> &rarr; 3CO<sub>2</sub> + 2Fe</b> (1)",
        "extra": "Allow Fe<sub>3</sub>O<sub>4</sub> and FeO.<br>Penalise Fe<sub>2</sub>.<br>Equation mark depends on correct reducing agent, but allow coal.<br>Reducing agent 1: not coal.",
        "mark": 4,
        "spec": "3.2.3"
    },
    "2003-june-chm2-q1b": {
        "answers": "• Equation 1: <b>TiO<sub>2</sub> + 2C + 2Cl<sub>2</sub> &rarr; TiCl<sub>4</sub> + 2CO</b> (or + C &rarr; CO<sub>2</sub>) (2) [1 mark for C + Cl<sub>2</sub>, 1 mark balance with TiCl<sub>4</sub>]<br>• Equation 2: <b>TiCl<sub>4</sub> + 4Na &rarr; 4NaCl + Ti</b> OR <b>TiCl<sub>4</sub> + 2Mg &rarr; 2MgCl<sub>2</sub> + Ti</b> (2) [1 mark for Na or Mg, 1 mark balance]",
        "extra": "",
        "mark": 4,
        "spec": "3.2.3"
    },
    "2003-june-chm2-q1c": {
        "answers": "• <b>Extraction:</b> Form metal oxide (or metal oxide implied) (1);<br>Reduce / react with suitable reducing agent (1)<br>• <b>Pollution problems:</b> <b>SO<sub>2</sub></b> (or oxides of S) (1);<br>Any mention of <b>acid rain</b> / H<sub>2</sub>SO<sub>4</sub> / erosion caused by acid rain (1)",
        "extra": "Second mark consequential on formation of metal oxide.<br>Allow any sensible and correct reducing agent identified.<br>Not SO<sub>3</sub> alone.",
        "mark": 4,
        "spec": "3.2.3"
    },
    "2003-june-chm2-q2a": {
        "answers": "<b>Gains electrons</b> (or accepts / takes electrons) (1)",
        "extra": "Allow 'an electron' or just 'gains' or 'reduction is gain of electrons'.<br>Not: OILRIG even if stated.",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-june-chm2-q2bi": {
        "answers": "• Oxidising agent: <b>Ag<sup>+</sup></b> (or Ag I) (1)<br>• Reducing agent: <b>SO<sub>2</sub></b> (or S IV) (1)",
        "extra": "Do not allow mention of electron pair(s).<br>Reducing agent: not sulphur.",
        "mark": 2,
        "spec": "3.1.7"
    },
    "2003-june-chm2-q2bii": {
        "answers": "<b>SO<sub>2</sub> + 2H<sub>2</sub>O &rarr; SO<sub>4</sub><sup>2&minus;</sup> + 4H<sup>+</sup> + 2e<sup>&minus;</sup></b> (1)",
        "extra": "Or H<sub>2</sub>SO<sub>4</sub> + 2H<sup>+</sup> + 2e<sup>&minus;</sup>.<br>Allow e<sup>&minus;</sup> (i.e. no charge). Allow &minus;e<sup>&minus;</sup> on LHS.<br>Penalise E<sup>&minus;</sup> once only.",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-june-chm2-q2ci": {
        "answers": "<b>Fe<sup>2+</sup> &rarr; Fe<sup>3+</sup> + e<sup>&minus;</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-june-chm2-q2cii": {
        "answers": "<b>5</b> (or +5 or V) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-june-chm2-q2ciii": {
        "answers": "<b>ClO<sub>3</sub><sup>&minus;</sup> + 6H<sup>+</sup> + 6e<sup>&minus;</sup> &rarr; Cl<sup>&minus;</sup> + 3H<sub>2</sub>O</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-june-chm2-q2civ": {
        "answers": "<b>ClO<sub>3</sub><sup>&minus;</sup> + 6H<sup>+</sup> + 6Fe<sup>2+</sup> &rarr; Cl<sup>&minus;</sup> + 3H<sub>2</sub>O + 6Fe<sup>3+</sup></b> (1)",
        "extra": "Mark parts (i) to (iv) independently.",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-june-chm2-q2d": {
        "answers": "• Equation: <b>Mg + S &rarr; MgS</b> (1) [allow Ca; allow FeS + Mg &rarr; MgS + Fe]<br>• Oxidising agent: <b>S</b> (1)",
        "extra": "Only award mark if first answer given unless no first answer then can allow.",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2003-june-chm2-q3ai": {
        "answers": "• Curve X starts at origin, peak higher (1)<br>• Peak displaced to the left, crosses over original curve once (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-june-chm2-q3aii": {
        "answers": "• Curve Y starts at origin, peak higher (1) [CE if not higher]<br>• Peak displaced by same amount (see limits) and does not cross over (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-june-chm2-q3bi": {
        "answers": "• Molecules must <b>collide</b> (1)<br>• With <b>sufficient energy</b> (or <i>E &ge; E<sub>a</sub></i>) / with correct orientation (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-june-chm2-q3bii": {
        "answers": "• Molecules (or particles) have <b>more energy</b> (or move faster) (1)<br>• <b>More molecules</b> (or collisions) have <b><i>E &ge; E<sub>a</sub></i></b> (or sufficient energy / more collisions) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-june-chm2-q3ci": {
        "answers": "<b>Equilibrium reached</b> (or rate of forward reaction = rate of backward reaction) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2003-june-chm2-q3cii": {
        "answers": "• Reaction is <b>endothermic</b> (or &Delta;<i>H</i> is positive / reverse reaction exothermic) (1)<br>• <b>Endothermic reaction is favoured</b> at higher temperature (or reaction shifts to the right / moves forward / more products formed) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2003-june-chm2-q4a": {
        "answers": "<b>C<sub>3</sub>H<sub>6</sub>O + 4O<sub>2</sub> &rarr; 3CO<sub>2</sub> + 3H<sub>2</sub>O</b> (1)",
        "extra": "Allow multiples.",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2003-june-chm2-q4bi": {
        "answers": "Moles propanone = 1.45 / 58 = <b>0.0250 mol</b> (1)",
        "extra": "Allow 0.025.<br>Allow consequential on wrong M<sub>r</sub>.<br>1.45/100 = CE; 1.45/58.1 = CE.",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-june-chm2-q4bii": {
        "answers": "• <i>q</i> = <i>mc</i>&Delta;<i>T</i> = 100 &times; 4.18 &times; 58.1 (1)<br>• = <b>24 300 J</b> (or <b>24.3 kJ</b>) (1)",
        "extra": "Allow 24 200 to 24 300.<br>Ignore decimal places; units tied to answer.<br>If 1.45 used in place of 100 = CE.<br>If use 0.1 &times; 4.18 &times; 58.1 allow &frac12; for 24.3 with no units.",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2003-june-chm2-q4biii": {
        "answers": "• &Delta;<i>H</i> = 24.3 / 0.0250 (1)<br>• = <b>&minus;972 kJ mol<sup>&minus;1</sup></b> (1)",
        "extra": "Allow &minus;968 to &minus;973.<br>Allow +972.<br>Allow no units; penalise wrong units.<br>Allow consequential on (b)(i) and (b)(ii).",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2003-june-chm2-q4ci": {
        "answers": "<b>Heat loss</b> (or energy loss) (1)",
        "extra": "Do not allow incomplete combustion.",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2003-june-chm2-q4cii": {
        "answers": "• Difference: <b>More negative</b> (or more exothermic) (1)<br>• Explanation: <b>Heat (or energy) released when water vapour condenses</b> (or heat/energy required to vaporise water / water molecules have more energy in gaseous state) (1)",
        "extra": "QoL mark.",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2003-june-chm2-q4d": {
        "answers": "• &Delta;<i>H</i> = &Sigma;&Delta;<i>H</i><sub>c</sub>(reactants) &minus; &Sigma;&Delta;<i>H</i><sub>c</sub>(products) (1) [or cycle]<br>• = (2 &times; &minus;394) + (3 &times; &minus;286) + (&minus;297) &minus; (&minus;1170) (1)<br>• = <b>&minus;773 kJ mol<sup>&minus;1</sup></b> (1)",
        "extra": "Allow 1/3 for +773.<br>Ignore units even if wrong.",
        "mark": 3,
        "spec": "3.1.4"
    }
}

def main():
    print("Ingesting 2003 June CHM2...")
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
        
    papers = {p["id"]: p for p in db.get("papers", [])}
    papers[PAPER_INFO["id"]] = PAPER_INFO
    db["papers"] = list(papers.values())
    
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
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
            "image": f"img/2003-june-chm2/q_{short_id}.jpg",
            "markscheme_image": f"img/2003-june-chm2/ms_{short_id}.png",
            "markscheme_text": ms.get("answers", "").replace("<br>", "\n").replace("<b>", "**").replace("</b>", "**").replace("&minus;", "-").replace("&times;", "x").replace("&le;", "<=").replace("&ge;", ">=").replace("&rArr;", "=>")
        }
        db["questions"].append(q_obj)
        
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully ingested {len(QUESTIONS_DEF)} questions for {PAPER_INFO['id']}!")

if __name__ == "__main__":
    main()

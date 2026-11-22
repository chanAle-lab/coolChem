"""
Ingestion script for 2003 June CHM3/W (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023395_abd178d4.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-june-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-june-chm3w",
    "year": 2003,
    "series": "June",
    "date": "2003-06-04",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2 (Exam page 2): Q1(a)-(b)
    ("2003-june-chm3w-q1ai", "1(a)(i)", 2, 180, 295, 1, ["3.3.1"], ["recall"], "Explain what is meant by the term hydrocarbon."),
    ("2003-june-chm3w-q1aii", "1(a)(ii)", 2, 300, 395, 1, ["3.3.2"], ["recall"], "Explain what is meant by the term fuel."),
    ("2003-june-chm3w-q1aiii", "1(a)(iii)", 2, 400, 460, 1, ["3.3.2"], ["recall"], "Equation for complete combustion of butane."),
    ("2003-june-chm3w-q1aiv", "1(a)(iv)", 2, 465, 535, 1, ["3.3.2"], ["recall"], "Equation for incomplete combustion of butane forming CO and water."),
    ("2003-june-chm3w-q1av", "1(a)(v)", 2, 540, 620, 1, ["3.3.2"], ["recall"], "Conditions under which incomplete combustion occurs."),
    ("2003-june-chm3w-q1b", "1(b)", 2, 625, 835, 2, ["3.3.2"], ["recall", "drawing"], "Structures of two other carbocations formed by catalytic cracking of butane."),

    # Page 5 (Exam page 5): Q1(c)
    ("2003-june-chm3w-q1ci", "1(c)(i)", 5, 80, 180, 1, ["3.3.2"], ["recall"], "Equation for cracking ethane to produce ethene and hydrogen."),
    ("2003-june-chm3w-q1cii", "1(c)(ii)", 5, 185, 245, 1, ["3.3.2"], ["recall"], "Suitable catalyst for cracking ethane."),
    ("2003-june-chm3w-q1ciii", "1(c)(iii)", 5, 250, 365, 1, ["3.3.2"], ["recall", "explanation"], "State one reason why cracking is important."),

    # Page 6 (Exam page 7): Q2
    ("2003-june-chm3w-q2ai", "2(a)(i)", 6, 80, 195, 1, ["3.3.3"], ["recall"], "Overall equation for reaction of chlorine with trichloromethane."),
    ("2003-june-chm3w-q2aii", "2(a)(ii)", 6, 200, 275, 1, ["3.3.3"], ["recall"], "Essential condition for reaction between chlorine and trichloromethane."),
    ("2003-june-chm3w-q2b", "2(b)", 6, 280, 610, 4, ["3.3.3"], ["recall"], "Equations for initiation, propagation and termination steps in chlorination of CHCl3."),
    ("2003-june-chm3w-q2ci", "2(c)(i)", 6, 615, 810, 3, ["3.1.2"], ["calculation"], "Empirical formula of chloroalkane W (37.2% C, 55.0% Cl, remainder H)."),
    ("2003-june-chm3w-q2cii", "2(c)(ii)", 6, 815, 915, 1, ["3.1.2"], ["recall"], "Additional information needed to calculate molecular formula of W."),

    # Page 7 (Exam page 8): Q3(a)-(b)(i)
    ("2003-june-chm3w-q3ai", "3(a)(i)", 7, 80, 340, 2, ["3.3.1"], ["drawing"], "Draw structures for two geometrical isomers of 1,2-dichloroethene."),
    ("2003-june-chm3w-q3aii", "3(a)(ii)", 7, 345, 430, 1, ["3.3.1"], ["explanation"], "Feature of double bond preventing isomer 1 changing into isomer 2."),
    ("2003-june-chm3w-q3bi", "3(b)(i)", 7, 435, 905, 4, ["3.3.3"], ["mechanism"], "Outline mechanism for Reaction 1 (nucleophilic substitution) and state role of OH-."),

    # Page 8 (Exam page 9): Q3(b)(ii)
    ("2003-june-chm3w-q3bii", "3(b)(ii)", 8, 80, 395, 4, ["3.3.3"], ["mechanism"], "Outline mechanism for Reaction 2 (elimination) and state role of OH-."),

    # Page 9 (Exam page 10): Q4(a)-(b)
    ("2003-june-chm3w-q4ai", "4(a)(i)", 9, 80, 540, 2, ["3.3.1", "3.3.5"], ["recall"], "Complete naming of isomers of C4H9OH in table."),
    ("2003-june-chm3w-q4aii", "4(a)(ii)", 9, 545, 635, 1, ["3.3.1"], ["recall"], "Name type of isomerism shown by four C4H9OH isomers."),
    ("2003-june-chm3w-q4bi", "4(b)(i)", 9, 640, 745, 1, ["3.3.5"], ["recall"], "Identify C4H9OH isomer resistant to oxidation by acidified potassium dichromate(VI)."),
    ("2003-june-chm3w-q4bii", "4(b)(ii)", 9, 750, 920, 2, ["3.3.5"], ["recall"], "Dehydrating agent and equation for dehydration of 2-methylpropan-2-ol."),

    # Page 10 (Exam page 11): Q4(c)-(d)
    ("2003-june-chm3w-q4ci", "4(c)(i)", 10, 80, 255, 2, ["3.3.5"], ["recall", "drawing"], "Identify isomer oxidised to ketone and give structure of ketone."),
    ("2003-june-chm3w-q4cii", "4(c)(ii)", 10, 260, 420, 2, ["3.3.5"], ["recall", "drawing"], "Identify isomer oxidised to aldehyde and give structure of aldehyde."),
    ("2003-june-chm3w-q4ciii", "4(c)(iii)", 10, 425, 650, 3, ["3.3.5"], ["recall"], "Reagent and observations to distinguish between ketone and aldehyde."),
    ("2003-june-chm3w-q4d", "4(d)", 10, 655, 835, 2, ["3.3.5"], ["recall"], "Equation for oxidation of butan-1-ol to carboxylic acid and name product.")
]

MS_DATA = {
    "2003-june-chm3w-q1ai": {
        "answers": "A molecule / compound / consists of / composed of / made up of <b>hydrogen and carbon only</b> (1)",
        "extra": "QoL mark.",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2003-june-chm3w-q1aii": {
        "answers": "<b>Releases (heat) energy</b> (when burned) OR provides (a useable form of) energy OR is a <b>source of energy</b> (1)",
        "extra": "Accept heat &equiv; energy.<br>Not: 'is energy', 'is heat', 'burns exothermically'.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q1aiii": {
        "answers": "<b>C<sub>4</sub>H<sub>10</sub> + 6&frac12;O<sub>2</sub> &rarr; 4CO<sub>2</sub> + 5H<sub>2</sub>O</b><br>OR <b>2C<sub>4</sub>H<sub>10</sub> + 13O<sub>2</sub> &rarr; 8CO<sub>2</sub> + 10H<sub>2</sub>O</b> (1)",
        "extra": "Ignore state symbols.<br>If not C<sub>4</sub>H<sub>10</sub> = CE.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q1aiv": {
        "answers": "<b>C<sub>4</sub>H<sub>10</sub> + 4&frac12;O<sub>2</sub> &rarr; 4CO + 5H<sub>2</sub>O</b><br>OR <b>2C<sub>4</sub>H<sub>10</sub> + 9O<sub>2</sub> &rarr; 8CO + 10H<sub>2</sub>O</b> (1)",
        "extra": "Ignore state symbols.<br>If not C<sub>4</sub>H<sub>10</sub> = CE.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q1av": {
        "answers": "<b>Limited OR reduced supply of oxygen / air</b> OR low temperature OR poor mixing OR insufficient oxygen / air OR shortage of O<sub>2</sub> (1)",
        "extra": "Not: 'no oxygen', 'lack of oxygen', 'not in excess'.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q1b": {
        "answers": "• Structure 2: <b>CH<sub>3</sub>CH<sup>+</sup>CH<sub>3</sub></b> (1) [not C<sub>2</sub>H<sub>5</sub><sup>+</sup>]<br>• Structure 3: <b><sup>+</sup>CH<sub>3</sub></b> (or CH<sub>3</sub><sup>+</sup>) (1)",
        "extra": "Either order.<br>Allow credit for positive charge around C atom.<br>No alternative carbocations allowed.",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q1ci": {
        "answers": "<b>C<sub>2</sub>H<sub>6</sub> &rarr; C<sub>2</sub>H<sub>4</sub> + H<sub>2</sub></b> (or CH<sub>3</sub>CH<sub>3</sub> &rarr; CH<sub>2</sub>=CH<sub>2</sub> + H<sub>2</sub>) (1)",
        "extra": "Not: CH<sub>2</sub>.CH<sub>2</sub>.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q1cii": {
        "answers": "<b>Al<sub>2</sub>O<sub>3</sub></b> OR <b>zeolite</b> OR <b>aluminosilicate</b> (1)",
        "extra": "Ignore SiO<sub>2</sub>.<br>Not: aluminium silicate, bauxite, porous pot, SiO<sub>2</sub> alone.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q1ciii": {
        "answers": "Any one from:<br>• Produce <b>more useful / valuable products</b> or needed fuels (1)<br>• <b>Demand exceeds supply</b> (qualified) (1)<br>• Produce <b>motor fuels / petrol / alkenes / smaller molecules / branched alkanes / cycloalkanes / aromatics</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-june-chm3w-q2ai": {
        "answers": "<b>CHCl<sub>3</sub> + Cl<sub>2</sub> &rarr; CCl<sub>4</sub> + HCl</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2003-june-chm3w-q2aii": {
        "answers": "<b>uv light</b> OR <b>high T</b> (or T &ge; 500 &deg;C) OR <b>sunlight</b> (1)",
        "extra": "Max T = 1000 &deg;C.<br>Not: heat, light.<br>Ignore pressure.<br>Condition could be on arrow of first equation.",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2003-june-chm3w-q2b": {
        "answers": "• <b>Initiation:</b> Cl<sub>2</sub> &rarr; 2Cl&bull; (1)<br>• <b>First propagation:</b> CHCl<sub>3</sub> + Cl&bull; &rarr; &bull;CCl<sub>3</sub> + HCl (1)<br>• <b>Second propagation:</b> &bull;CCl<sub>3</sub> + Cl<sub>2</sub> &rarr; CCl<sub>4</sub> + Cl&bull; (1)<br>• <b>Termination:</b> &bull;CCl<sub>3</sub> + Cl&bull; &rarr; CCl<sub>4</sub> OR 2 &bull;CCl<sub>3</sub> &rarr; C<sub>2</sub>Cl<sub>6</sub> (1)",
        "extra": "Penalise absence of dot once only.<br>Termination: not 2Cl&bull; &rarr; Cl<sub>2</sub>.<br>Ignore additional termination steps.",
        "mark": 4,
        "spec": "3.3.3"
    },
    "2003-june-chm3w-q2ci": {
        "answers": "• % H = 100 &minus; (37.2 + 55.0) = <b>7.8(0)%</b> (1)<br>• mol C = 37.2/12 = 3.10; mol Cl = 55.0/35.5 = 1.55; mol H = 7.80/1 = 7.80 (1)<br>• Ratio = 2 : 1 : 5 &rArr; Empirical formula = <b>C<sub>2</sub>H<sub>5</sub>Cl</b> (1)",
        "extra": "Not CH<sub>3</sub>CH<sub>2</sub>Cl alone (CH<sub>3</sub>CH<sub>2</sub>Cl alone scores 2 marks).",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-june-chm3w-q2cii": {
        "answers": "<b>M<sub>r</sub></b> OR <b>relative molecular mass</b> OR molar mass OR formula mass OR mass of one mole (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-june-chm3w-q3ai": {
        "answers": "• <b>Isomer 1 (cis-1,2-dichloroethene):</b> C=C with Cl, Cl on same side and H, H on same side (1)<br>• <b>Isomer 2 (trans-1,2-dichloroethene):</b> C=C with Cl, Cl on opposite sides and H, H on opposite sides (1)",
        "extra": "Either order.<br>Credit displayed structures with clear geometry.",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2003-june-chm3w-q3aii": {
        "answers": "<b>Restricted rotation</b> (or no rotation / cannot rotate) of the double bond (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2003-june-chm3w-q3bi": {
        "answers": "• Curly arrow from lone pair on :OH<sup>&minus;</sup> to C atom of C&minus;Cl (1)<br>• Curly arrow from C&minus;Cl bond to Cl atom forming Cl<sup>&minus;</sup> (1)<br>• Correct dipole on C&minus;Cl (C<sup>&delta;+</sup>&minus;Cl<sup>&delta;&minus;</sup>) and correct organic product (1)<br>• Role of hydroxide ion: <b>nucleophile</b> (or electron pair donor / lone pair donor) (1)",
        "extra": "M1 and M2 independent.<br>Curly arrows must be from a bond or a lone pair.<br>Penalise sticks.<br>Penalise M1 if Na&minus;OH precedes (penalise thus once).<br>Credit M1/M2 via carbocation mechanism (SN1).<br>Role: not 'nucleophilic substitution'.",
        "mark": 4,
        "spec": "3.3.3"
    },
    "2003-june-chm3w-q3bii": {
        "answers": "• Curly arrow from lone pair on :OH<sup>&minus;</sup> to H atom on adjacent C (1)<br>• Curly arrow from C&minus;H bond to C&minus;C bond (1)<br>• Curly arrow from C&minus;Cl bond to Cl atom (1)<br>• Role of hydroxide ion: <b>base</b> (or proton acceptor / accepts H<sup>+</sup>) (1)",
        "extra": "M3 independent.<br>M2 must be to correct C&minus;C.<br>M1 must be to correct H atom.<br>Credit M1 and M2 via carbocation mechanism.<br>[No marks after any attack of C+ by OH&minus;].",
        "mark": 4,
        "spec": "3.3.3"
    },
    "2003-june-chm3w-q4ai": {
        "answers": "• CH<sub>3</sub>&minus;CH(CH<sub>3</sub>)&minus;CH<sub>2</sub>OH: <b>2-methylpropan-1-ol</b> (1)<br>• CH<sub>3</sub>CH<sub>2</sub>&minus;CH(OH)&minus;CH<sub>3</sub>: <b>butan-2-ol</b> (or 2-butanol) (1)",
        "extra": "Allow 'e' in names.<br>Not: prop-1-ol, but-2-ol, hydroxy.",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2003-june-chm3w-q4aii": {
        "answers": "<b>Structural</b> (or chain and position / positional) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2003-june-chm3w-q4bi": {
        "answers": "<b>2-methylpropan-2-ol</b> (or the second one) (1)",
        "extra": "If b(i) is blank, b(ii) equation must be full for credit.",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2003-june-chm3w-q4bii": {
        "answers": "• Dehydrating agent: <b>conc. H<sub>2</sub>SO<sub>4</sub></b> OR <b>conc. H<sub>3</sub>PO<sub>4</sub></b> OR <b>Al<sub>2</sub>O<sub>3</sub></b> (1)<br>• Equation: <b>(CH<sub>3</sub>)<sub>3</sub>COH &rarr; (CH<sub>3</sub>)<sub>2</sub>C=CH<sub>2</sub> + H<sub>2</sub>O</b> (1)",
        "extra": "Allow C<sub>4</sub>H<sub>9</sub>OH in equation provided RHS is correct.<br>Mark consequential on b(i).",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2003-june-chm3w-q4ci": {
        "answers": "• Isomer: <b>butan-2-ol</b> (or the fourth one) (1)<br>• Structure of ketone: <b>CH<sub>3</sub>CH<sub>2</sub>COCH<sub>3</sub></b> (1)",
        "extra": "Wrong isomer = CE.<br>Look at name in table.",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2003-june-chm3w-q4cii": {
        "answers": "• Isomer: <b>butan-1-ol</b> OR <b>2-methylpropan-1-ol</b> (1)<br>• Structure of aldehyde: <b>CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CHO</b> OR <b>(CH<sub>3</sub>)<sub>2</sub>CHCHO</b> (1)",
        "extra": "Wrong isomer = CE.<br>Look at name in table.",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2003-june-chm3w-q4ciii": {
        "answers": "• Reagent: <b>Tollens' reagent</b> (or ammoniacal silver nitrate) OR <b>Fehling's solution</b> (or Benedict's) (1)<br>• Ketone: <b>No change / stays colourless</b> (with Tollens') OR <b>stays blue / no change</b> (with Fehling's) (1)<br>• Aldehyde: <b>Silver mirror / black ppt.</b> (with Tollens') OR <b>red solid / ppt.</b> (with Fehling's) (1)",
        "extra": "Others include: acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> (orange to green with aldehyde, no change with ketone); acidified KMnO<sub>4</sub> (purple to colourless/pale pink with aldehyde, no change with ketone).<br>Wrong reagent / no reagent = CE.",
        "mark": 3,
        "spec": "3.3.5"
    },
    "2003-june-chm3w-q4d": {
        "answers": "• Equation: <b>CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH + 2[O] &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOH + H<sub>2</sub>O</b> (1)<br>• Name: <b>butanoic acid</b> (1)",
        "extra": "Allow C<sub>4</sub>H<sub>9</sub>OH + 2[O] &rarr; C<sub>3</sub>H<sub>7</sub>COOH + H<sub>2</sub>O.<br>Accept butanoic acid.",
        "mark": 2,
        "spec": "3.3.5"
    }
}

def main():
    print("Ingesting 2003 June CHM3/W...")
    doc = fitz.open(QP_PATH)
    
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
            
    print("Cropping question images from QP...")
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        out_jpg = os.path.join(IMG_DIR, f"q_{q_id.split('-')[-1]}.jpg")
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        im.save(out_jpg, format="JPEG", quality=92)
        
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
            "image": f"img/2003-june-chm3w/q_{short_id}.jpg",
            "markscheme_image": f"img/2003-june-chm3w/ms_{short_id}.png",
            "markscheme_text": ms.get("answers", "").replace("<br>", "\n").replace("<b>", "**").replace("</b>", "**").replace("&minus;", "-").replace("&times;", "x").replace("&le;", "<=").replace("&ge;", ">=").replace("&rArr;", "=>")
        }
        db["questions"].append(q_obj)
        
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully ingested {len(QUESTIONS_DEF)} questions for {PAPER_INFO['id']}!")

if __name__ == "__main__":
    main()

"""
Ingestion script for 2003 January CHM2 (Section A only)
Excludes old-spec Section B essay questions (Q7).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463338_dbb54824.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-jan-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-jan-chm2",
    "year": 2003,
    "series": "January",
    "date": "2003-01-16",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour 30 mins"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2003-jan-chm2-q1a", "1(a)", 2, 150, 335, 1, ["3.1.4"], ["recall"], "Why standard enthalpy of formation for carbon and nitrogen are zero."),
    ("2003-jan-chm2-q1b", "1(b)", 2, 338, 465, 2, ["3.1.4"], ["recall"], "State Hess's Law."),
    ("2003-jan-chm2-q1c", "1(c)", 2, 468, 645, 3, ["3.1.4"], ["calculation"], "Calculate enthalpy change for NH4NO3 + 1/2 C reaction using standard formation data."),
    
    # Page 5: Question 2
    ("2003-jan-chm2-q2a", "2(a)", 5, 80, 315, 2, ["3.1.4"], ["recall"], "Explain the term mean bond enthalpy."),
    ("2003-jan-chm2-q2bi", "2(b)(i)", 5, 318, 385, 1, ["3.1.4"], ["recall"], "Equation for formation of one mole of ammonia from elements."),
    ("2003-jan-chm2-q2bii", "2(b)(ii)", 5, 388, 535, 3, ["3.1.4"], ["calculation"], "Calculate enthalpy of formation of ammonia from mean bond enthalpy data."),
    ("2003-jan-chm2-q2c", "2(c)", 5, 538, 770, 3, ["3.1.4"], ["calculation"], "Calculate C-H bond enthalpy in ethane from hydrogenation equation and bond data."),
    
    # Page 6: Question 3(a)-(c)
    ("2003-jan-chm2-q3a", "3(a)", 6, 80, 185, 2, ["3.1.5"], ["recall"], "Define the term activation energy for a reaction."),
    ("2003-jan-chm2-q3b", "3(b)", 6, 188, 290, 2, ["3.1.5"], ["recall"], "Give the meaning of the term catalyst."),
    ("2003-jan-chm2-q3c", "3(c)", 6, 292, 420, 2, ["3.1.5"], ["recall", "analysis"], "Explain in general terms how a catalyst works."),
    
    # Page 7: Question 3(d)(i)-(iii)
    ("2003-jan-chm2-q3di", "3(d)(i)", 7, 80, 500, 2, ["3.1.5"], ["analysis"], "Sketch curve W showing concentration of W against time for 2W + Y -> Z."),
    ("2003-jan-chm2-q3dii", "3(d)(ii)", 7, 502, 555, 2, ["3.1.5"], ["analysis"], "Sketch curve Z showing concentration against time in presence of a catalyst."),
    ("2003-jan-chm2-q3diii", "3(d)(iii)", 7, 558, 680, 2, ["3.1.5"], ["analysis"], "Explain in terms of particle behaviour why reaction rate decreases with time."),
    
    # Page 8: Question 4
    ("2003-jan-chm2-q4a", "4(a)", 8, 80, 275, 2, ["3.1.6"], ["recall"], "Explain meaning of dynamic equilibrium in terms of rates and concentrations."),
    ("2003-jan-chm2-q4b", "4(b)", 8, 278, 370, 2, ["3.1.6"], ["analysis"], "Explain why high yield of methanol is favoured by high pressure in CO + 2H2 reaction."),
    ("2003-jan-chm2-q4c", "4(c)", 8, 372, 470, 2, ["3.1.6"], ["analysis"], "Suggest two reasons why operating at pressure much higher than 5 MPa is very expensive."),
    ("2003-jan-chm2-q4d", "4(d)", 8, 472, 630, 3, ["3.1.6"], ["analysis"], "State and explain effect of temperature increase on equilibrium yield of methanol."),
    ("2003-jan-chm2-q4e", "4(e)", 8, 632, 710, 1, ["3.1.5", "3.1.6"], ["analysis"], "Suggest why increased temperature is required if catalyst is not used."),
    
    # Page 9: Question 5
    ("2003-jan-chm2-q5a", "5(a)", 9, 80, 200, 3, ["3.2.3"], ["analysis"], "State and explain trend in electronegativity down Group VII from F to I."),
    ("2003-jan-chm2-q5bi", "5(b)(i)", 9, 202, 305, 2, ["3.2.3"], ["practical", "recall"], "Observations and equation when aqueous bromine is added to aqueous iodide."),
    ("2003-jan-chm2-q5bii", "5(b)(ii)", 9, 308, 395, 1, ["3.2.3"], ["analysis"], "Explain why bromine does not react with aqueous chloride ions."),
    ("2003-jan-chm2-q5c", "5(c)", 9, 398, 500, 2, ["3.2.3"], ["practical"], "Observations when aqueous AgNO3 is added separately to KF(aq) and KBr(aq)."),
    ("2003-jan-chm2-q5d", "5(d)", 9, 502, 575, 1, ["3.2.3"], ["recall"], "Equation for reaction of solid KF with concentrated sulphuric acid."),
    ("2003-jan-chm2-q5e", "5(e)", 9, 578, 655, 2, ["3.2.3"], ["recall"], "Equation for redox reaction of sodium bromide with concentrated sulphuric acid."),
    
    # Page 10: Question 6(a)-(b)
    ("2003-jan-chm2-q6ai", "6(a)(i)", 10, 80, 185, 1, ["3.1.7"], ["recall"], "Half-equation for reduction of hydrogen peroxide to water in acid conditions."),
    ("2003-jan-chm2-q6aii", "6(a)(ii)", 10, 188, 240, 1, ["3.1.7"], ["recall"], "Half-equation for oxidation of iodide ions to iodine."),
    ("2003-jan-chm2-q6aiii", "6(a)(iii)", 10, 242, 315, 1, ["3.1.7"], ["recall"], "Construct overall equation for reaction between H2O2, H+ and I-."),
    ("2003-jan-chm2-q6bi", "6(b)(i)", 10, 318, 420, 1, ["3.1.7"], ["recall"], "Equation for reaction between iodine and thiosulphate ions."),
    ("2003-jan-chm2-q6bii", "6(b)(ii)", 10, 422, 630, 4, ["3.1.2"], ["calculation"], "Calculate concentration of aqueous iodine solution from thiosulphate titration data."),
    
    # Page 11: Question 6(c)
    ("2003-jan-chm2-q6ci", "6(c)(i)", 11, 80, 210, 1, ["3.1.7"], ["recall"], "Half-equation for reduction of chlorine to chloride ions."),
    ("2003-jan-chm2-q6cii", "6(c)(ii)", 11, 212, 265, 1, ["3.1.7"], ["recall"], "Deduce oxidation state of chlorine in HClO."),
    ("2003-jan-chm2-q6ciii", "6(c)(iii)", 11, 268, 330, 1, ["3.1.7"], ["recall"], "Half-equation for oxidation of chlorine in water forming HClO and H+ ions."),
    ("2003-jan-chm2-q6civ", "6(c)(iv)", 11, 332, 420, 1, ["3.2.3"], ["recall"], "Reason why chlorine is used in the water industry.")
]

MS_DATA = {
    "2003-jan-chm2-q1a": {
        "answers": "<b>They are elements</b> (1)",
        "extra": "Ignore irrelevant comments.",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2003-jan-chm2-q1b": {
        "answers": "• <b>Enthalpy change</b> (or heat energy change / heat change / &Delta;<i>H</i> / any named enthalpy change) (1)<br>• <b>independent of route</b> (or depends only on initial and final states) (1)",
        "extra": "CE: if 'change' not mentioned.<br>Only give second mark if first awarded except allow if energy used instead of enthalpy.",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2003-jan-chm2-q1c": {
        "answers": "• &Delta;<i>H</i> = &Sigma;&Delta;<i>H</i><sub>f</sub>(products) &minus; &Sigma;&Delta;<i>H</i><sub>f</sub>(reactants) (or cycle) (1)<br>• = [2 &times; (&minus;242) + 0.5 &times; (&minus;394)] &minus; (&minus;365) (1)<br>• = <b>&minus;316</b> (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "Ignore no units, penalise wrong units.<br>+316 scores 1/3.<br>Working line implies first mark.",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2003-jan-chm2-q2a": {
        "answers": "• <b>Enthalpy / Energy to break a (covalent) bond</b> (or dissociation energy) (1)<br>• <b>varies between compounds so average value used</b> (or average of dissociation energies in a single molecule e.g. CH<sub>4</sub>) (1)",
        "extra": "QoL mark for point 2.<br>Do not allow mention of energy to form bonds (but in this case can allow 2nd mark; otherwise 2nd mark consequential on 1st).",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2003-jan-chm2-q2bi": {
        "answers": "<b>&frac12; N<sub>2</sub> + 1&frac12; H<sub>2</sub> &rarr; NH<sub>3</sub></b> (1)",
        "extra": "Ignore state symbols.",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2003-jan-chm2-q2bii": {
        "answers": "• &Delta;<i>H</i> = (&Sigma;) bonds broken &minus; (&Sigma;) bonds formed (1)<br>• = (&frac12; &times; 944 + 1&frac12; &times; 436) &minus; (3 &times; 388) (1)<br>• = <b>&minus;38</b> (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "Ignore no units, penalise wrong units.<br>Score 2/3 for &minus;76; 1/3 for +38; allow 1/3 for +76.",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2003-jan-chm2-q2c": {
        "answers": "• 4(C&minus;H) + (C=C) + (H&minus;H) &minus; [6(C&minus;H) + (C&minus;C)] = &minus;136<br>&nbsp;&nbsp;OR (C=C) + (H&minus;H) &minus; [(C&minus;C) + 2(C&minus;H)] = &minus;136 (1)<br>• 2(C&minus;H) = 836 (1)<br>• (C&minus;H) = <b>418</b> (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "Note: allow (1) for &minus;836, another (1) for &minus;418.",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2003-jan-chm2-q3a": {
        "answers": "• <b>Minimum energy</b> (1)<br>• <b>required before a reaction can occur</b> (or go / start) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-jan-chm2-q3b": {
        "answers": "• <b>Speeds up (changes) reaction rate</b> (1)<br>• <b>without being (chemically) changed / used up</b> (1)",
        "extra": "Award 4 marks for 4 points wherever found across (b) and (c).",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-jan-chm2-q3c": {
        "answers": "• <b>Provides alternative reaction route</b> (1)<br>• <b>with lower activation energy</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-jan-chm2-q3di": {
        "answers": "• <b>Curve starts between top of axis and 'n' of concentration</b> (or 2 &times; plateau) (1)<br>• <b>Falls to zero when Z curve levels out</b> (1)",
        "extra": "Curve can touch time axis.",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-jan-chm2-q3dii": {
        "answers": "• <b>Curve starts at origin, to left of original</b> (steeper initial gradient) (1)<br>• <b>Reaches same plateau</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-jan-chm2-q3diii": {
        "answers": "• <b>Fewer collisions</b> (1)<br>• <b>W / reactants / reagents used up</b> (or fewer particles) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2003-jan-chm2-q4a": {
        "answers": "• <b>Rate of forward reaction = rate of backward reaction</b> (1)<br>• <b>Concentrations remain constant</b> (1)",
        "extra": "NOT 'equal', allow 'the same' if clear that means 'constant'.",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2003-jan-chm2-q4b": {
        "answers": "• <b>Fewer moles (of gas) on R.H.S.</b> (or converse) (1)<br>• <b>(Methanol favoured) by reducing applied pressure / removes constraint</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2003-jan-chm2-q4c": {
        "answers": "<b>Any two from:</b><br>• <b>Power / energy required to provide high pressure / pumping</b> (1)<br>• <b>Strong pressure vessel / equipment needed</b> (1)<br>• <b>High maintenance costs</b> (1)<br>• <b>High insurance costs</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2003-jan-chm2-q4d": {
        "answers": "• Effect: <b>Decreases</b> (1)<br>• Explanation: <b>Reaction is exothermic</b> (or reverse reaction is endothermic) (1)<br>• <b>System tries to lower T / oppose the change</b> OR <b>endothermic reaction favoured</b> (1)",
        "extra": "If first mark endothermic: allow reverse reaction favoured.",
        "mark": 3,
        "spec": "3.1.6"
    },
    "2003-jan-chm2-q4e": {
        "answers": "<b>To speed up reaction</b> OR <b>otherwise too slow / takes too long</b> OR <b>to give more molecules <i>E</i> &ge; <i>E</i><sub>a</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2003-jan-chm2-q5a": {
        "answers": "• Trend: <b>Decreases</b> (1) (CE if wrong)<br>• Explanation: <b>Number of shells increases</b> (or atomic radius increases) (1)<br>• <b>Increased nuclear shielding</b> OR <b>less attraction for bonding pair / electrons</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.3"
    },
    "2003-jan-chm2-q5bi": {
        "answers": "• Observation: <b>Brown solution</b> OR <b>black solid</b> (1)<br>• Equation: <b>Br<sub>2</sub> + 2I<sup>&minus;</sup> &rarr; I<sub>2</sub> + 2Br<sup>&minus;</sup></b> (1)",
        "extra": "'Purple' wrong for observation.<br>Allow NaI, KI in equation.",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2003-jan-chm2-q5bii": {
        "answers": "<b>Br<sub>2</sub> is a weaker oxidising agent than Cl<sub>2</sub></b> (or converse) OR <b>Br<sub>2</sub> is less reactive than Cl<sub>2</sub></b> (1)",
        "extra": "Penalise Cl, Br, Cl-, Br- etc.",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2003-jan-chm2-q5c": {
        "answers": "• Observation with KF(aq): <b>No change / colourless</b> (1)<br>• Observation with KBr(aq): <b>Cream / off-white precipitate / solid</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2003-jan-chm2-q5d": {
        "answers": "<b>KF + H<sub>2</sub>SO<sub>4</sub> &rarr; KHSO<sub>4</sub> + HF</b> (or 2KF + H<sub>2</sub>SO<sub>4</sub> &rarr; K<sub>2</sub>SO<sub>4</sub> + 2HF) (1)",
        "extra": "Allow ions.",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2003-jan-chm2-q5e": {
        "answers": "<b>2H<sub>2</sub>SO<sub>4</sub> + 2Br<sup>&minus;</sup> &rarr; SO<sub>2</sub> + Br<sub>2</sub> + 2H<sub>2</sub>O + SO<sub>4</sub><sup>2&minus;</sup></b><br>• Correct species (SO<sub>2</sub> + Br<sub>2</sub>) (1)<br>• Balanced equation (1)",
        "extra": "Allow 2H2SO4 + 2NaBr -> SO2 + Br2 + 2H2O + Na2SO4<br>or H2SO4 + 2HBr -> 2H2O + Br2 + SO2 etc.",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2003-jan-chm2-q6ai": {
        "answers": "<b>H<sub>2</sub>O<sub>2</sub> + 2H<sup>+</sup> + 2e<sup>&minus;</sup> &rarr; 2H<sub>2</sub>O</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-jan-chm2-q6aii": {
        "answers": "<b>2I<sup>&minus;</sup> &rarr; I<sub>2</sub> + 2e<sup>&minus;</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-jan-chm2-q6aiii": {
        "answers": "<b>H<sub>2</sub>O<sub>2</sub> + 2H<sup>+</sup> + 2I<sup>&minus;</sup> &rarr; I<sub>2</sub> + 2H<sub>2</sub>O</b> (1)",
        "extra": "Allow 2HI.",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-jan-chm2-q6bi": {
        "answers": "<b>I<sub>2</sub> + 2S<sub>2</sub>O<sub>3</sub><sup>2&minus;</sup> &rarr; 2I<sup>&minus;</sup> + S<sub>4</sub>O<sub>6</sub><sup>2&minus;</sup></b> (1)",
        "extra": "Allow Na+ etc.",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-jan-chm2-q6bii": {
        "answers": "• Moles thiosulphate = (19.5 / 1000) &times; 0.120 = <b>0.00234</b> (mol) (1)<br>• Moles iodine = 0.00234 / 2 = <b>0.00117</b> (mol) (1)<br>• Concentration = (0.00117 &times; 1000) / 25 = <b>0.0468</b> (mol dm<sup>&minus;3</sup>) (1)<br>• Mark for correct final answer in range 0.0468 to 0.047(0) (1)",
        "extra": "Allow consequential on wrong equation in (i).<br>If used 3:1 ratio: moles I2 = 0.000780 (1), conc = 0.0312 (1), allow 0.031(0) - 0.0314.",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2003-jan-chm2-q6ci": {
        "answers": "<b>Cl<sub>2</sub> + 2e<sup>&minus;</sup> &rarr; 2Cl<sup>&minus;</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-jan-chm2-q6cii": {
        "answers": "<b>+1</b> (1)",
        "extra": "Allow 1, 1+, Cl+.",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-jan-chm2-q6ciii": {
        "answers": "<b>Cl<sub>2</sub> + 2H<sub>2</sub>O &rarr; 2HClO + 2H<sup>+</sup> + 2e<sup>&minus;</sup></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2003-jan-chm2-q6civ": {
        "answers": "<b>Kills bacteria / germs / microorganisms / bugs</b> OR <b>sterilise / disinfect</b> (1)",
        "extra": "NOT allow purify, safe to drink.",
        "mark": 1,
        "spec": "3.2.3"
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
        q_img_rel = f"img/2003-jan-chm2/q_q{sub_id}.jpg"
        ms_img_rel = f"img/2003-jan-chm2/ms_q{sub_id}.jpg"
        
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

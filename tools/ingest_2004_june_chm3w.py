"""
Ingestion script for 2004 June CHM3/W (Section A only)
Excludes old-spec Section B essay questions (Q5).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921127_77aaa068.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-june-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-june-chm3w",
    "year": 2004,
    "series": "June",
    "date": "2004-06-10",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(b)
    ("2004-june-chm3w-q1ai", "1(a)(i)", 2, 75, 240, 1, ["3.3.5"], ["recall"], "Write equation to represent fermentation of glucose to ethanol."),
    ("2004-june-chm3w-q1aii", "1(a)(ii)", 2, 242, 310, 1, ["3.3.5"], ["recall"], "Give the name of the process for making ethanol from glucose."),
    ("2004-june-chm3w-q1bi", "1(b)(i)", 2, 312, 455, 1, ["3.3.5"], ["recall"], "Write an equation for the complete combustion of ethanol."),
    ("2004-june-chm3w-q1bii", "1(b)(ii)", 2, 458, 545, 1, ["3.3.2"], ["recall"], "Identify pollutant produced when ethanol is burned in limited air."),
    ("2004-june-chm3w-q1biii", "1(b)(iii)", 2, 548, 775, 1, ["3.3.2"], ["recall"], "Equation for reaction in catalytic converter decreasing nitrogen monoxide."),

    # Page 5: Question 1(c)-(d)
    ("2004-june-chm3w-q1c", "1(c)", 5, 75, 590, 5, ["3.3.5"], ["analysis"], "Name and complete mechanism for dehydration of ethanol using conc sulphuric acid."),
    ("2004-june-chm3w-q1d", "1(d)", 5, 592, 775, 3, ["3.3.4"], ["recall"], "Catalyst and equation with epoxyethane structure for its manufacture."),

    # Page 6: Question 2(a)-(c)
    ("2004-june-chm3w-q2ai", "2(a)(i)", 6, 75, 410, 1, ["3.3.4"], ["recall"], "Name the mechanism for reaction of propene with HBr."),
    ("2004-june-chm3w-q2aii", "2(a)(ii)", 6, 412, 565, 2, ["3.3.4"], ["analysis"], "Explain why 1-bromopropane is only a minor product in Reaction 1."),
    ("2004-june-chm3w-q2b", "2(b)", 6, 568, 680, 2, ["3.3.3"], ["recall"], "Give reagent and conditions for conversion of 2-bromopropane into propan-2-ol."),
    ("2004-june-chm3w-q2c", "2(c)", 6, 682, 775, 1, ["3.3.3"], ["recall"], "State different conditions needed to convert 2-bromopropane into propene."),

    # Page 7: Question 2(d)
    ("2004-june-chm3w-q2di", "2(d)(i)", 7, 75, 260, 1, ["3.3.5"], ["recall"], "Name the class of alcohols to which propan-2-ol belongs."),
    ("2004-june-chm3w-q2dii", "2(d)(ii)", 7, 262, 590, 4, ["3.3.4"], ["analysis"], "Outline mechanism for Reaction 2 Stage 1 (propene with conc H2SO4)."),
    ("2004-june-chm3w-q2diii", "2(d)(iii)", 7, 592, 775, 1, ["3.3.4"], ["recall"], "State the overall role of sulphuric acid in Reaction 2."),

    # Page 8: Question 3
    ("2004-june-chm3w-q3ai", "3(a)(i)", 8, 75, 255, 3, ["3.3.5"], ["recall"], "Reagent, conditions and reaction type for propan-2-ol into propanone."),
    ("2004-june-chm3w-q3aii", "3(a)(ii)", 8, 258, 465, 2, ["3.3.9"], ["recall"], "Reagent and equation with [H] for reduction of propanone to propan-2-ol."),
    ("2004-june-chm3w-q3bi", "3(b)(i)", 8, 468, 565, 1, ["3.3.9"], ["recall"], "Draw the structure of propanal."),
    ("2004-june-chm3w-q3bii", "3(b)(ii)", 8, 568, 775, 3, ["3.3.9"], ["analysis"], "Chemical test, reagent and observations to distinguish propanone and propanal."),

    # Page 10: Question 4(a)
    ("2004-june-chm3w-q4ai", "4(a)(i)", 10, 75, 220, 1, ["3.3.2"], ["recall"], "Name the mechanism for reaction between bromine and methane."),
    ("2004-june-chm3w-q4aii", "4(a)(ii)", 10, 222, 335, 2, ["3.3.2"], ["recall"], "Name and state essential condition for first step (initiation)."),
    ("2004-june-chm3w-q4aiii", "4(a)(iii)", 10, 338, 460, 1, ["3.3.2"], ["recall"], "Write equation for termination step which gives ethane as product."),
    ("2004-june-chm3w-q4aiv", "4(a)(iv)", 10, 462, 775, 1, ["3.3.2"], ["recall"], "Write overall equation for further substitution forming dibromomethane."),

    # Page 11: Question 4(b)
    ("2004-june-chm3w-q4bi", "4(b)(i)", 11, 75, 280, 1, ["3.3.3"], ["recall"], "Explain what is meant by the term nucleophile."),
    ("2004-june-chm3w-q4bii", "4(b)(ii)", 11, 282, 355, 1, ["3.3.3"], ["recall"], "Name the organic product of reaction of bromomethane with ammonia."),
    ("2004-june-chm3w-q4biii", "4(b)(iii)", 11, 358, 775, 4, ["3.3.3"], ["analysis"], "Outline a mechanism for reaction of bromomethane with ammonia.")
]

MS_DATA = {
    "2004-june-chm3w-q1ai": {
        "answers": "C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> &rarr; 2C<sub>2</sub>H<sub>5</sub>OH + 2CO<sub>2</sub> (1)",
        "extra": "allow CH3CH2OH; ignore state symbols",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2004-june-chm3w-q1aii": {
        "answers": "Fermentation (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2004-june-chm3w-q1bi": {
        "answers": "C<sub>2</sub>H<sub>5</sub>OH + 3O<sub>2</sub> &rarr; 2CO<sub>2</sub> + 3H<sub>2</sub>O (1)",
        "extra": "allow C2H6O or CH3CH2OH",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2004-june-chm3w-q1bii": {
        "answers": "CO or carbon monoxide or C or carbon ONLY (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-june-chm3w-q1biii": {
        "answers": "2CO + 2NO &rarr; 2CO<sub>2</sub> + N<sub>2</sub> (1)",
        "extra": "or 2NO -> N2 + O2 / 2NO + C -> N2 + CO2 / C8H18 + 25NO -> 8CO2 + 12½N2 + 9H2O",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-june-chm3w-q1c": {
        "answers": "• Name: Elimination (1)<br>• M1 structure of protonated alcohol CH<sub>3</sub>CH<sub>2</sub>OH<sub>2</sub><sup>+</sup> (1)<br>• M2 arrow to show breakage of C&minus;O bond on protonated alcohol (1)<br>• M3 structure of carbocation CH<sub>3</sub>CH<sub>2</sub><sup>+</sup> (1)<br>• M4 arrow from correct C&minus;H bond on carbocation (1)",
        "extra": "penalise 'electrophilic elimination'<br>synchronous mechanism using correct structure required for M1, loses M3",
        "mark": 5,
        "spec": "3.3.5"
    },
    "2004-june-chm3w-q1d": {
        "answers": "• Catalyst: Silver OR silver-based (1)<br>• Equation: H<sub>2</sub>C=CH<sub>2</sub> + &frac12;O<sub>2</sub> &rarr; C<sub>2</sub>H<sub>4</sub>O (1)<br>• Structure: Epoxyethane cyclic three-membered ring (1)",
        "extra": "catalyst: NOT silver oxide; credit structure independently",
        "mark": 3,
        "spec": "3.3.4"
    },
    "2004-june-chm3w-q2ai": {
        "answers": "Electrophilic addition (1)",
        "extra": "both words required",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2004-june-chm3w-q2aii": {
        "answers": "• Reaction to form 1-bromopropane goes via primary carbocation CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub><sup>+</sup> (1)<br>• Primary carbocations are less stable than secondary carbocations (1)",
        "extra": "or converse argument for 2-bromopropane via more stable secondary carbocation",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2004-june-chm3w-q2b": {
        "answers": "• Reagent: NaOH OR KOH (1)<br>• Conditions: Aqueous or solution in water (1)",
        "extra": "penalise OH- alone for M1; NaOH(aq) scores both marks",
        "mark": 2,
        "spec": "3.3.3"
    },
    "2004-june-chm3w-q2c": {
        "answers": "Ethanolic OR alcoholic OR aqueous ethanol/alcohol solvent OR higher temperature (1)",
        "extra": "penalise 'ethanoic'",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-june-chm3w-q2di": {
        "answers": "Secondary OR 2&deg; (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2004-june-chm3w-q2dii": {
        "answers": "• M1 arrow from double bond to H of H&minus;OSO<sub>2</sub>OH (1)<br>• M2 arrow from bond to oxygen atom showing H&minus;O bond breakage (1)<br>• M3 structure of carbocation CH<sub>3</sub>CH<sup>+</sup>CH<sub>3</sub> (1)<br>• M4 arrow from lone pair of electrons on :OSO<sub>2</sub>OH<sup>&minus;</sup> to carbon atom of carbocation (1)",
        "extra": "penalise M1 if arrow goes to H2SO4; accept negative charge anywhere on HSO4- ion",
        "mark": 4,
        "spec": "3.3.4"
    },
    "2004-june-chm3w-q2diii": {
        "answers": "Catalyst ONLY (1)",
        "extra": "ignore homogeneous, heterogeneous",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2004-june-chm3w-q3ai": {
        "answers": "• Reagent: Potassium (or sodium) dichromate(VI) / K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> (1)<br>• Conditions: Acidified (or H<sub>2</sub>SO<sub>4</sub>) (1)<br>• Type of reaction: Oxidation or redox (1)",
        "extra": "allow potassium manganate(VII)",
        "mark": 3,
        "spec": "3.3.5"
    },
    "2004-june-chm3w-q3aii": {
        "answers": "• Reagent: NaBH<sub>4</sub> OR LiAlH<sub>4</sub> OR H<sub>2</sub>/Ni (1)<br>• Equation: CH<sub>3</sub>COCH<sub>3</sub> + 2[H] &rarr; CH<sub>3</sub>CH(OH)CH<sub>3</sub> (1)",
        "extra": "credit H2 in equation if H2/Ni chosen",
        "mark": 2,
        "spec": "3.3.9"
    },
    "2004-june-chm3w-q3bi": {
        "answers": "CH<sub>3</sub>CH<sub>2</sub>CHO (structure showing aldehyde C=O with H attached) (1)",
        "extra": "must clearly show aldehyde group",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2004-june-chm3w-q3bii": {
        "answers": "• Reagent: Tollens' reagent OR Fehling's solution OR acidified potassium dichromate (1)<br>• Observation with propanone: Stays colourless / stays blue / stays orange (no reaction) (1)<br>• Observation with propanal: Silver mirror (black ppt) / red-brown ppt / goes green (1)",
        "extra": "credit other correct reagents with appropriate observations",
        "mark": 3,
        "spec": "3.3.9"
    },
    "2004-june-chm3w-q4ai": {
        "answers": "(Free) radical substitution (1)",
        "extra": "both words needed",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-june-chm3w-q4aii": {
        "answers": "• Name: Initiation (1)<br>• Essential condition: Ultra-violet light OR sunlight OR high temperature (&ge; 450 &deg;C) (1)",
        "extra": "penalise 'high temperature' without value for M2",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2004-june-chm3w-q4aiii": {
        "answers": "2&bull;CH<sub>3</sub> &rarr; C<sub>2</sub>H<sub>6</sub> (1)",
        "extra": "allow CH3CH3",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-june-chm3w-q4aiv": {
        "answers": "CH<sub>3</sub>Br + Br<sub>2</sub> &rarr; CH<sub>2</sub>Br<sub>2</sub> + HBr (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2004-june-chm3w-q4bi": {
        "answers": "Electron pair donor OR species with an electron pair able to form a covalent bond (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-june-chm3w-q4bii": {
        "answers": "Methylamine (1)",
        "extra": "credit 'aminomethane'",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2004-june-chm3w-q4biii": {
        "answers": "• M1 arrow to show breakage of C&minus;Br bond (1)<br>• M2 arrow from lone pair on N of :NH<sub>3</sub> to form bond with C (1)<br>• M3 structure of intermediate CH<sub>3</sub>NH<sub>3</sub><sup>+</sup> (1)<br>• M4 arrow from N&minus;H bond to N atom of CH<sub>3</sub>NH<sub>3</sub><sup>+</sup> (1)",
        "extra": "ignore partial charges on haloalkane; full credit for SN1 carbocation mechanism",
        "mark": 4,
        "spec": "3.3.3"
    }
}

def main():
    doc = fitz.open(QP_PATH)
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    if not any(p["id"] == PAPER_INFO["id"] for p in db.get("papers", [])):
        db.setdefault("papers", []).append(PAPER_INFO)

    existing_ids = {q["id"] for q in db["questions"]}
    added = 0

    for qid, q_label, p_num, y0, y1, mark, spec_topics, skills, prompt in QUESTIONS_DEF:
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-june-chm3w/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-june-chm3w/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-june-chm3w",
            "year": 2004,
            "series": "June",
            "code": "CHM3/W",
            "unit": "Unit 3(a): Introduction to Organic Chemistry",
            "question": q_label,
            "page": p_num,
            "marks": mark,
            "topics": spec_topics,
            "skills": skills,
            "description": prompt,
            "image": q_img_rel,
            "markscheme": ms_img_rel
        }

        if qid not in existing_ids:
            db["questions"].append(q_obj)
            existing_ids.add(qid)
            added += 1
        else:
            for idx, item in enumerate(db["questions"]):
                if item["id"] == qid:
                    db["questions"][idx] = q_obj
                    break

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-june-chm3w ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

"""
Ingestion script for 2005 January CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q7, Q8).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382904753_27df4626.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-jan-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-jan-chm4",
    "year": 2005,
    "series": "January",
    "date": "2005-01-21",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A2",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 minutes"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(b)
    ("2005-jan-chm4-q1ai", "1(a)(i)", 2, 80, 480, 2, ["3.3.10"], ["recall"], "Give reagents for Step 1 (formation of NO2+) and write equation.", ["img/2005-jan-chm4/fig-q1-scheme.jpg"]),
    ("2005-jan-chm4-q1aii", "1(a)(ii)", 2, 485, 820, 4, ["3.3.10"], ["recall"], "Name and outline mechanism for reaction of NO2+ with methylbenzene.", ["img/2005-jan-chm4/fig-q1-scheme.jpg"]),
    ("2005-jan-chm4-q1b", "1(b)", 2, 825, 930, 1, ["3.3.10", "3.3.11"], ["recall"], "Give suitable reagent or combination for Step 2 (reduction of nitroarene to amine K).", ["img/2005-jan-chm4/fig-q1-scheme.jpg"]),

    # Page 5: Question 1(c)-(f)
    ("2005-jan-chm4-q1ci", "1(c)(i)", 5, 80, 260, 2, ["3.3.11"], ["recall"], "Give reagent for Step 4 and condition to ensure primary amine is major product.", None),
    ("2005-jan-chm4-q1cii", "1(c)(ii)", 5, 265, 520, 5, ["3.3.11"], ["recall"], "Name and outline mechanism for Step 4 (nucleophilic substitution with NH3).", None),
    ("2005-jan-chm4-q1d", "1(d)", 5, 525, 650, 2, ["3.3.11"], ["explanation"], "Explain why amine K (phenylamine derivative) is a weaker base than ammonia.", None),
    ("2005-jan-chm4-q1e", "1(e)", 5, 655, 765, 1, ["3.3.11"], ["recall"], "Draw structure of organic compound formed when large excess of bromomethane reacts with amine L.", None),
    ("2005-jan-chm4-q1f", "1(f)", 5, 770, 890, 1, ["3.3.9", "3.3.11"], ["recall"], "Draw structure of organic compound formed when ethanoyl chloride reacts with amine L.", None),

    # Page 6: Question 2(a)-(b)
    ("2005-jan-chm4-q2ai", "2(a)(i)", 6, 80, 395, 2, ["3.3.13"], ["recall"], "Draw structure of main alanine species in aqueous solution and give name of type of species.", None),
    ("2005-jan-chm4-q2aii", "2(a)(ii)", 6, 400, 560, 1, ["3.3.13"], ["recall"], "Draw structure of alanine species formed when excess hydrochloric acid is added.", None),
    ("2005-jan-chm4-q2b", "2(b)", 6, 565, 850, 2, ["3.3.12", "3.3.13"], ["recall"], "Give repeating unit of alanine polypeptide and name type of polymerisation.", None),

    # Page 7: Question 2(c)
    ("2005-jan-chm4-q2c", "2(c)", 7, 80, 340, 1, ["3.3.12"], ["recall"], "Give name of alkene used to form given polyalkene.", None),

    # Page 8: Question 3(a)-(c)
    ("2005-jan-chm4-q3a", "3(a)", 8, 80, 370, 2, ["3.3.1"], ["recall"], "Draw one possible structure each for isomers A and B (C5H10).", None),
    ("2005-jan-chm4-q3b", "3(b)", 8, 375, 580, 2, ["3.3.6"], ["recall"], "Draw one possible structure each for isomers C and D (C2H4O2).", None),
    ("2005-jan-chm4-q3c", "3(c)", 8, 585, 850, 2, ["3.3.6"], ["recall"], "Draw one possible structure each for esters E and F (C5H10O2).", None),

    # Page 9: Question 3(d)-(e)
    ("2005-jan-chm4-q3d", "3(d)", 9, 80, 320, 2, ["3.3.7"], ["recall"], "Draw one possible structure each for isomers G and H (C3H6Cl2).", None),
    ("2005-jan-chm4-q3e", "3(e)", 9, 325, 680, 2, ["3.3.6"], ["recall"], "Draw one possible structure each for isomers I and J (C6H12).", None),

    # Page 10: Question 4
    ("2005-jan-chm4-q4a", "4(a)", 10, 80, 385, 2, ["3.1.9"], ["calculation"], "Deduce order of reaction with respect to P and with respect to Q.", ["img/2005-jan-chm4/fig-q4-table.jpg"]),
    ("2005-jan-chm4-q4bi", "4(b)(i)", 10, 390, 590, 3, ["3.1.9"], ["calculation"], "Write rate equation for reaction between R and S, and calculate initial rate.", None),
    ("2005-jan-chm4-q4bii", "4(b)(ii)", 10, 595, 780, 2, ["3.1.9"], ["calculation"], "Calculate value of rate constant at temperature T2.", None),
    ("2005-jan-chm4-q4biii", "4(b)(iii)", 10, 785, 900, 1, ["3.1.9"], ["explanation"], "Deduce which of T1 and T2 is the higher temperature.", None),

    # Page 11: Question 5
    ("2005-jan-chm4-q5ai", "5(a)(i)", 11, 80, 310, 2, ["3.1.6"], ["calculation"], "Calculate moles of C2F4 and moles of HCl at equilibrium.", None),
    ("2005-jan-chm4-q5aii", "5(a)(ii)", 11, 315, 430, 1, ["3.1.6"], ["recall"], "Write an expression for Kc for the equilibrium.", None),
    ("2005-jan-chm4-q5aiii", "5(a)(iii)", 11, 435, 650, 3, ["3.1.6"], ["calculation"], "Calculate value for Kc and give its units.", None),
    ("2005-jan-chm4-q5bi", "5(b)(i)", 11, 655, 740, 1, ["3.1.6"], ["explanation"], "State how temperature should be changed at constant pressure to increase yield of C2F4.", None),
    ("2005-jan-chm4-q5bii", "5(b)(ii)", 11, 745, 830, 1, ["3.1.6"], ["explanation"], "State how total pressure should be changed at constant temperature to increase yield of C2F4.", None),
    ("2005-jan-chm4-q5c", "5(c)", 11, 835, 930, 1, ["3.3.2", "3.3.12"], ["recall"], "Name type of polymerisation involved in formation of PTFE.", None),

    # Page 12: Question 6
    ("2005-jan-chm4-q6a", "6(a)", 12, 80, 270, 1, ["3.3.9"], ["recall"], "Name compound U (CH3CH2CH2COCl).", None),
    ("2005-jan-chm4-q6bi", "6(b)(i)", 12, 275, 360, 1, ["3.1.1", "3.3.6"], ["explanation"], "State why mass spectrum of U contains two molecular ion peaks.", None),
    ("2005-jan-chm4-q6bii", "6(b)(ii)", 12, 365, 470, 1, ["3.1.1", "3.3.6"], ["calculation"], "Give m/z values of these two peaks.", None),
    ("2005-jan-chm4-q6c", "6(c)", 12, 475, 850, 5, ["3.3.9"], ["recall"], "Name and outline mechanism for reaction of U with CH3OH.", None)
]

MS_DEF = {
    "2005-jan-chm4-q1ai": {
        "answers": "conc HNO<sub>3</sub> (1)<br>conc H<sub>2</sub>SO<sub>4</sub> (1)<br>HNO<sub>3</sub> + 2H<sub>2</sub>SO<sub>4</sub> → NO<sub>2</sub><sup>+</sup> + H<sub>3</sub>O<sup>+</sup> + 2HSO<sub>4</sub><sup>–</sup><br><b>OR</b> HNO<sub>3</sub> + H<sub>2</sub>SO<sub>4</sub> → NO<sub>2</sub><sup>+</sup> + H<sub>2</sub>O + HSO<sub>4</sub><sup>–</sup> (1)",
        "extra": "allow 1 for both acids if either conc missing",
        "mark": 2,
        "spec": "3.3.10"
    },
    "2005-jan-chm4-q1aii": {
        "answers": "electrophilic substitution (1)<br>M1: curly arrow from delocalised pi ring of methylbenzene to NO<sub>2</sub><sup>+</sup> (1)<br>M2: correct structure of intermediate carbocation (horseshoe facing C with H and NO<sub>2</sub>, + charge in ring) (1)<br>M3: curly arrow from C-H bond to reform aromatic ring (1)",
        "extra": "horseshoe must not extend beyond C2 to C6 but can be smaller; + must not be too close to C1",
        "mark": 4,
        "spec": "3.3.10"
    },
    "2005-jan-chm4-q1b": {
        "answers": "Sn or Fe / HCl (conc or dil or neither)<br><b>OR</b> Ni / H<sub>2</sub>",
        "extra": "not NaBH<sub>4</sub> / LiAlH<sub>4</sub>",
        "mark": 1,
        "spec": "3.3.10 / 3.3.11"
    },
    "2005-jan-chm4-q1ci": {
        "answers": "Reagent: NH<sub>3</sub> (1)<br>Condition: Use an excess of ammonia (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.11"
    },
    "2005-jan-chm4-q1cii": {
        "answers": "nucleophilic substitution (1)<br>M1: curly arrow from lone pair on N of NH<sub>3</sub> to C attached to Cl (1)<br>M2: curly arrow from C-Cl bond to Cl atom (1)<br>M3: structure of intermediate C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>N<sup>+</sup>H<sub>3</sub> (1)<br>M4: curly arrow from N-H bond to N atom (or attack by another NH<sub>3</sub>) (1)",
        "extra": "",
        "mark": 5,
        "spec": "3.3.11"
    },
    "2005-jan-chm4-q1d": {
        "answers": "lone pair on N less available (in correct context) (1)<br>delocalised into the ring (1)",
        "extra": "(Q of L)",
        "mark": 2,
        "spec": "3.3.11"
    },
    "2005-jan-chm4-q1e": {
        "answers": "[C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>N(CH<sub>3</sub>)<sub>3</sub>]<sup>+</sup> Br<sup>–</sup> (quaternary ammonium salt)",
        "extra": "ignore Br<sup>–</sup>; + must be on N or outside square bracket",
        "mark": 1,
        "spec": "3.3.11"
    },
    "2005-jan-chm4-q1f": {
        "answers": "C<sub>6</sub>H<sub>5</sub>CH<sub>2</sub>NHCOCH<sub>3</sub> (N-benzylacetamide)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.9 / 3.3.11"
    },
    "2005-jan-chm4-q2ai": {
        "answers": "Structure: H<sub>3</sub>N<sup>+</sup>–CH(CH<sub>3</sub>)–COO<sup>–</sup> (1)<br>Type of species: zwitterion (1)",
        "extra": "penalise <sup>+</sup>NH<sub>3</sub>– or + on H once per paper",
        "mark": 2,
        "spec": "3.3.13"
    },
    "2005-jan-chm4-q2aii": {
        "answers": "H<sub>3</sub>N<sup>+</sup>–CH(CH<sub>3</sub>)–COOH",
        "extra": "",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2005-jan-chm4-q2b": {
        "answers": "Repeating unit: –[NH–CH(CH<sub>3</sub>)–CO]– (1)<br>Type of polymerisation: condensation or (nucleophilic) addition-elimination (1)",
        "extra": "ignore n, but allow one drawn out repeating unit only",
        "mark": 2,
        "spec": "3.3.12 / 3.3.13"
    },
    "2005-jan-chm4-q2c": {
        "answers": "3-methylpent-2-ene",
        "extra": "",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2005-jan-chm4-q3a": {
        "answers": "A: any C<sub>5</sub> alkene (e.g. pent-1-ene, pent-2-ene, 2-methylbut-1-ene) (1)<br>B: cyclopentane or methylcyclobutane etc (1)",
        "extra": "penalise non-cyclic structures for B",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2005-jan-chm4-q3b": {
        "answers": "C: CH<sub>3</sub>COOH (ethanoic acid) or HCOOCH<sub>3</sub> (methyl methanoate) (1)<br>D: HOCH<sub>2</sub>CHO (hydroxyethanal) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.6"
    },
    "2005-jan-chm4-q3c": {
        "answers": "E: HCOOC(CH<sub>3</sub>)<sub>3</sub> (tert-butyl methanoate) (1)<br>F: CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub> (ethyl propanoate) (1)",
        "extra": "(allow C<sub>2</sub>H<sub>5</sub>)",
        "mark": 2,
        "spec": "3.3.6"
    },
    "2005-jan-chm4-q3d": {
        "answers": "G: CH<sub>3</sub>CH(Cl)CH<sub>2</sub>Cl (1,2-dichloropropane) (1)<br>H: CH<sub>3</sub>CH<sub>2</sub>CHCl<sub>2</sub> or ClCH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>Cl or CH<sub>3</sub>CCl<sub>2</sub>CH<sub>3</sub> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.7"
    },
    "2005-jan-chm4-q3e": {
        "answers": "I: (CH<sub>3</sub>)<sub>2</sub>C=C(CH<sub>3</sub>)<sub>2</sub> (2,3-dimethylbut-2-ene) (1)<br>J: (C<sub>2</sub>H<sub>5</sub>)<sub>2</sub>C=CH<sub>2</sub> (2-ethylbut-1-ene) (1)",
        "extra": "NOT hex-3-ene",
        "mark": 2,
        "spec": "3.3.6"
    },
    "2005-jan-chm4-q4a": {
        "answers": "order with respect to P is 2 (1)<br>order with respect to Q is 1 (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2005-jan-chm4-q4bi": {
        "answers": "rate = k[R][S]<sup>2</sup> (1)<br>rate = (4.2 × 10<sup>–4</sup>) × 0.16 × 0.84<sup>2</sup> (1)<br>= 4.7 × 10<sup>–5</sup> (mol dm<sup>–3</sup> s<sup>–1</sup>) (1)",
        "extra": "if wrong expression, no further marks; ignore units even if wrong",
        "mark": 3,
        "spec": "3.1.9"
    },
    "2005-jan-chm4-q4bii": {
        "answers": "k = rate / ([R][S]<sup>2</sup>) = (8.1 × 10<sup>–5</sup>) / (0.76 × 0.98<sup>2</sup>) (1)<br>= 1.1 × 10<sup>–4</sup> (mol<sup>–2</sup> dm<sup>6</sup> s<sup>–1</sup>) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2005-jan-chm4-q4biii": {
        "answers": "T<sub>1</sub>",
        "extra": "* If calculated value for k > 4.2 × 10<sup>–4</sup>, then answer is T<sub>2</sub>",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2005-jan-chm4-q5ai": {
        "answers": "moles of C<sub>2</sub>F<sub>4</sub> = 0.40 (1)<br>moles of HCl = 0.80 (1)",
        "extra": "mark independently; not consequential",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2005-jan-chm4-q5aii": {
        "answers": "K<sub>c</sub> = [C<sub>2</sub>F<sub>4</sub>][HCl]<sup>2</sup> / [CHClF<sub>2</sub>]<sup>2</sup>",
        "extra": "wrong Kc means they can only score for units in (iii) consequ on their Kc",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2005-jan-chm4-q5aiii": {
        "answers": "K<sub>c</sub> = [(0.40/18.5)(0.80/18.5)<sup>2</sup>] / (0.20/18.5)<sup>2</sup> (1)<br>= 0.35 (1)<br>Units: mol dm<sup>–3</sup> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.6"
    },
    "2005-jan-chm4-q5bi": {
        "answers": "increase",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2005-jan-chm4-q5bii": {
        "answers": "decrease",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2005-jan-chm4-q5c": {
        "answers": "addition or radical",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2 / 3.3.12"
    },
    "2005-jan-chm4-q6a": {
        "answers": "butanoyl chloride",
        "extra": "",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2005-jan-chm4-q6bi": {
        "answers": "Cl has (two) isotopes or <sup>35</sup>Cl and <sup>37</sup>Cl",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1 / 3.3.6"
    },
    "2005-jan-chm4-q6bii": {
        "answers": "106 and 108",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1 / 3.3.6"
    },
    "2005-jan-chm4-q6c": {
        "answers": "(nucleophilic) addition-elimination (1)<br>M1: curly arrow from lone pair on O of CH<sub>3</sub>OH to carbonyl C (1)<br>M2: curly arrow from C=O bond to O atom (1)<br>M3: tetrahedral intermediate with O<sup>–</sup>, Cl, O<sup>+</sup>H(CH<sub>3</sub>) (1)<br>M4: 3 arrows (lone pair on O<sup>–</sup> reforms C=O, C-Cl bond breaks to Cl, loss of H<sup>+</sup>) (1)",
        "extra": "penalise electrophilic ... not esterification",
        "mark": 5,
        "spec": "3.3.9"
    }
}

def main():
    print("Opening Question Paper PDF...")
    doc = fitz.open(QP_PATH)

    new_questions = []

    for qid, q_label, p_num, y0, y1, marks, spec, skills, desc, figs in QUESTIONS_DEF:
        # Render initial crop image
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        
        subpart_name = qid.split("-")[-1]
        img_filename = f"q_{subpart_name}.jpg"
        img_rel = f"img/2005-jan-chm4/{img_filename}"
        img_abs = os.path.join(REPO_DIR, img_rel.replace("/", os.sep))
        
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        im.save(img_abs, format="JPEG", quality=92)
        
        # Render official mark scheme image
        ms_data = MS_DEF[qid]
        ms_filename = f"ms_{subpart_name}.png"
        ms_img_rel = f"img/2005-jan-chm4/{ms_filename}"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        
        render_official_markscheme_image(
            q_label,
            ms_data["answers"],
            ms_data["extra"],
            ms_data["mark"],
            ms_data["spec"],
            ms_img_abs
        )

        q_entry = {
            "id": qid,
            "paper": PAPER_INFO["id"],
            "year": PAPER_INFO["year"],
            "series": PAPER_INFO["series"],
            "unit": PAPER_INFO["unit"],
            "date": PAPER_INFO["date"],
            "question": q_label,
            "description": desc,
            "marks": marks,
            "topics": spec,
            "skills": skills,
            "image": img_rel,
            "markscheme": {
                "image": ms_img_rel
            },
            "page": p_num
        }
        if figs:
            q_entry["figures"] = figs
            
        new_questions.append(q_entry)
        print(f"Processed {qid} ({q_label}) - {marks} marks")

    # Load questions.json and update
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Ensure paper metadata exists in papers
    if not any(p["id"] == PAPER_INFO["id"] for p in db.get("papers", [])):
        db.setdefault("papers", []).append(PAPER_INFO)

    # Filter out existing entries for this paper if any
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    db["questions"].extend(new_questions)

    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully ingested {len(new_questions)} questions for {PAPER_INFO['id']}!")

if __name__ == "__main__":
    main()

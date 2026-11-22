"""
Ingestion script for 2004 June CHM4 (Section A only)
Excludes old-spec Section B essay questions (Q7 and Q8).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921129_89796597.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-june-chm4")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-june-chm4",
    "year": 2004,
    "series": "June",
    "date": "2004-06-24",
    "code": "CHM4",
    "unit": "Unit 4: Further Physical and Organic Chemistry",
    "level": "A",
    "spec": "AQA Chemistry",
    "totalMarks": 90,
    "duration": "1 hour 30 minutes"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2004-june-chm4-q1ai", "1(a)(i)", 2, 75, 520, 3, ["3.1.9"], ["calculation"], "Complete table of initial rate data for reaction between A and B."),
    ("2004-june-chm4-q1aii", "1(a)(ii)", 2, 522, 690, 3, ["3.1.9"], ["calculation"], "Calculate rate constant k and state its units using experiment 1 data."),
    ("2004-june-chm4-q1b", "1(b)", 2, 692, 775, 1, ["3.1.9"], ["recall"], "State how value of rate constant k changes if concentration of A increased."),

    # Page 5: Question 2
    ("2004-june-chm4-q2a", "2(a)", 5, 75, 255, 1, ["3.1.12"], ["recall"], "Write an expression for Ka for weak acid HA."),
    ("2004-june-chm4-q2b", "2(b)", 5, 258, 455, 4, ["3.1.12"], ["calculation"], "Calculate pH of 0.250 mol dm-3 solution of HA at 298 K."),
    ("2004-june-chm4-q2ci", "2(c)(i)", 5, 458, 640, 2, ["3.1.12"], ["recall"], "State and explain effect on pH of buffer when small amount of HCl is added."),
    ("2004-june-chm4-q2cii", "2(c)(ii)", 5, 642, 775, 4, ["3.1.12"], ["calculation"], "Calculate concentration of A- in buffer solution when pH is 3.59."),

    # Page 6: Question 3(a)-(d)
    ("2004-june-chm4-q3a", "3(a)", 6, 75, 395, 3, ["3.1.10"], ["calculation"], "Deduce partial pressure of oxygen and mole fraction in equilibrium mixture."),
    ("2004-june-chm4-q3b", "3(b)", 6, 398, 475, 1, ["3.1.10"], ["calculation"], "Calculate partial pressure of sulphur trioxide in equilibrium mixture."),
    ("2004-june-chm4-q3c", "3(c)", 6, 478, 715, 4, ["3.1.10"], ["calculation"], "Write expression for Kp, calculate its value at T1 and state units."),
    ("2004-june-chm4-q3d", "3(d)", 6, 718, 775, 3, ["3.1.10"], ["analysis"], "State which of T1 and T2 is lower temperature when Kp increases and explain."),

    # Page 7: Question 3(e)
    ("2004-june-chm4-q3e", "3(e)", 7, 75, 775, 2, ["3.1.10"], ["recall"], "Deduce effect of smaller flask volume on yield of SO3 and on Kp."),

    # Page 8: Question 4(a)-(c)
    ("2004-june-chm4-q4a", "4(a)", 8, 75, 505, 5, ["3.3.11"], ["analysis"], "Name and outline mechanism for formation of butylamine from 1-bromobutane and ammonia."),
    ("2004-june-chm4-q4b", "4(b)", 8, 508, 690, 3, ["3.3.11", "3.3.3"], ["recall"], "Equations for two-step synthesis of butylamine from 1-bromopropane via nitrile."),
    ("2004-june-chm4-q4ci", "4(c)(i)", 8, 692, 810, 2, ["3.3.11"], ["recall"], "Explain why butylamine is a stronger base than ammonia."),
    ("2004-june-chm4-q4cii", "4(c)(ii)", 8, 812, 850, 1, ["3.1.12", "3.3.11"], ["recall"], "Identify substance added to aqueous butylamine to produce basic buffer."),

    # Page 9: Question 4(d)
    ("2004-june-chm4-q4d", "4(d)", 9, 75, 775, 1, ["3.3.11"], ["recall"], "Draw the structure of a tertiary amine which is an isomer of butylamine."),

    # Page 10: Question 5(a)-(b)
    ("2004-june-chm4-q5ai", "5(a)(i)", 10, 75, 275, 1, ["3.3.12"], ["recall"], "Draw repeating unit of polymer formed from H2C=CHCN."),
    ("2004-june-chm4-q5aii", "5(a)(ii)", 10, 278, 355, 1, ["3.3.12"], ["recall"], "Name type of polymerisation involved in forming poly(propenenitrile)."),
    ("2004-june-chm4-q5bi", "5(b)(i)", 10, 358, 560, 1, ["3.3.13"], ["recall"], "Name the amino acid produced when dipeptide is hydrolysed under acidic conditions."),
    ("2004-june-chm4-q5bii", "5(b)(ii)", 10, 562, 775, 1, ["3.3.13"], ["recall"], "Draw structure of amino acid species present in acidic solution."),

    # Page 11: Question 5(c)
    ("2004-june-chm4-q5ci", "5(c)(i)", 11, 75, 270, 1, ["3.3.12"], ["calculation"], "Deduce empirical formula of repeating unit of polyester."),
    ("2004-june-chm4-q5cii", "5(c)(ii)", 11, 272, 440, 2, ["3.3.12"], ["recall"], "Draw structure and give name of dicarboxylic acid used to prepare polyester."),
    ("2004-june-chm4-q5ciii", "5(c)(iii)", 11, 442, 775, 1, ["3.3.12"], ["recall"], "Give one reason why the polyester is biodegradable."),

    # Page 12: Question 6
    ("2004-june-chm4-q6a", "6(a)", 12, 75, 335, 1, ["3.3.9"], ["recall"], "Name compound C (C5H10O)."),
    ("2004-june-chm4-q6bi", "6(b)(i)", 12, 338, 445, 1, ["3.3.16"], ["analysis"], "Suggest wavenumber in IR of C but not D."),
    ("2004-june-chm4-q6bii", "6(b)(ii)", 12, 448, 545, 1, ["3.3.16"], ["analysis"], "Suggest wavenumber in IR of D but not C."),
    ("2004-june-chm4-q6c", "6(c)", 12, 548, 620, 1, ["3.3.15"], ["analysis"], "Deduce number of peaks in proton NMR spectrum of C."),
    ("2004-june-chm4-q6d", "6(d)", 12, 622, 770, 3, ["3.3.5", "3.3.9"], ["practical"], "Reagent and observations to distinguish ketone C and secondary alcohol D."),
    ("2004-june-chm4-q6e", "6(e)", 12, 772, 850, 2, ["3.3.9"], ["practical"], "Reagent and observation reacting with aldehyde E but not C or D.")
]

MS_DATA = {
    "2004-june-chm4-q1ai": {
        "answers": "• Experiment 2: 2.60 &times; 10<sup>&minus;3</sup> (1)<br>• Experiment 3: 0.60 &times; 10<sup>&minus;2</sup> (1)<br>• Experiment 4: 11.4 &times; 10<sup>&minus;2</sup> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.9"
    },
    "2004-june-chm4-q1aii": {
        "answers": "• k = (10.4 &times; 10<sup>&minus;3</sup>) / ((4.80 &times; 10<sup>&minus;2</sup>)(6.60 &times; 10<sup>&minus;2</sup>)<sup>2</sup>) (1)<br>• = 49.7 (1) (allow 49.8 and 50)<br>• Units: mol<sup>&minus;2</sup> dm<sup>6</sup> s<sup>&minus;1</sup> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.9"
    },
    "2004-june-chm4-q1b": {
        "answers": "No change (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2004-june-chm4-q2a": {
        "answers": "K<sub>a</sub> = [H<sup>+</sup>][A<sup>&minus;</sup>] / [HA] (1)",
        "extra": "all three sets of square brackets needed; penalise missing brackets or charges once; don't penalise extra [H+]^2/[HA]",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2004-june-chm4-q2b": {
        "answers": "• K<sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [HA] or [H<sup>+</sup>] = [A<sup>&minus;</sup>] (1)<br>• [H<sup>+</sup>] = &radic;(1.45 &times; 10<sup>&minus;4</sup> &times; 0.250) (1)<br>• = 6.02 &times; 10<sup>&minus;3</sup> (mol dm<sup>&minus;3</sup>) (1)<br>• pH = 2.22 (1) (must be to 2 dp)",
        "extra": "allow 4th mark consequential on [H+]",
        "mark": 4,
        "spec": "3.1.12"
    },
    "2004-june-chm4-q2ci": {
        "answers": "• pH (almost) unchanged (1)<br>• H<sup>+</sup> removed by A<sup>&minus;</sup> forming HA (or acid reacts with salt / more HA formed) (1)",
        "extra": "must be correct to score explanation",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2004-june-chm4-q2cii": {
        "answers": "• [H<sup>+</sup>] = 10<sup>&minus;3.59</sup> = 2.57 &times; 10<sup>&minus;4</sup> (1)<br>• [A<sup>&minus;</sup>] = K<sub>a</sub>[HA] / [H<sup>+</sup>] (1)<br>• = (1.45 &times; 10<sup>&minus;4</sup> &times; 0.250) / (2.57 &times; 10<sup>&minus;4</sup>) (1)<br>• = 0.141 (mol dm<sup>&minus;3</sup>) (1) (allow 0.139 to 0.141, allow 0.14)",
        "extra": "alternative using Henderson-Hasselbalch: pH = pKa - log([HA]/[A-]), pKa = 3.84, [A-] = 0.141",
        "mark": 4,
        "spec": "3.1.12"
    },
    "2004-june-chm4-q3a": {
        "answers": "• Partial pressure of O<sub>2</sub> = 12 (kPa) (1)<br>• pp = mole fraction &times; total pressure or mole fraction = 12 / 104 (1)<br>• = 0.115 (allow 0.12) (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.10"
    },
    "2004-june-chm4-q3b": {
        "answers": "p(SO<sub>3</sub>) = 104 &minus; 24 &minus; 12 = 68 (kPa) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2004-june-chm4-q3c": {
        "answers": "• K<sub>p</sub> = (pSO<sub>3</sub>)<sup>2</sup> / ((pSO<sub>2</sub>)<sup>2</sup> &times; pO<sub>2</sub>) (1)<br>• = 68<sup>2</sup> / (24<sup>2</sup> &times; 12) (1)<br>• = 0.669 (allow 0.67) (1)<br>• Units: kPa<sup>&minus;1</sup> (1)",
        "extra": "allow full marks consequential on values in (a) and (b)",
        "mark": 4,
        "spec": "3.1.10"
    },
    "2004-june-chm4-q3d": {
        "answers": "• Lower temperature: T<sub>2</sub> (1)<br>• Exothermic (1)<br>• Reduce T to shift equilibrium to the right / forward reaction favoured by low T / Kp increases for low T (1)",
        "extra": "T2 must be correct to score any marks in this section",
        "mark": 3,
        "spec": "3.1.10"
    },
    "2004-june-chm4-q3e": {
        "answers": "• Effect on yield of SO<sub>3</sub>: Increase (1)<br>• Effect on K<sub>p</sub>: None (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.10"
    },
    "2004-june-chm4-q4a": {
        "answers": "• Name: Nucleophilic substitution (1)<br>• M1 arrow from lone pair on N of :NH<sub>3</sub> to C (1)<br>• M2 arrow from C&minus;Br bond to Br (1)<br>• M3 structure of intermediate cation CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>3</sub><sup>+</sup> (1)<br>• M4 arrow from N&minus;H bond to N atom (with second NH<sub>3</sub> removing H<sup>+</sup>) (1)",
        "extra": "allow SN1 mechanism; penalise M4 if Br- used to remove H+",
        "mark": 5,
        "spec": "3.3.11"
    },
    "2004-june-chm4-q4b": {
        "answers": "• Step 1: CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>Br + KCN &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CN + KBr (or CN<sup>&minus;</sup>) (2)<br>• Step 2: CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CN + 2H<sub>2</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub> (or 4[H]) (1)",
        "extra": "not HCN for Step 1",
        "mark": 3,
        "spec": "3.3.11"
    },
    "2004-june-chm4-q4ci": {
        "answers": "• Lone pair (on N) (1)<br>• R group increases electron density / donates electrons / pushes electrons / has positive inductive effect (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.11"
    },
    "2004-june-chm4-q4cii": {
        "answers": "Any strong acid (not concentrated) OR any amine salt / ammonium salt of a strong acid (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2004-june-chm4-q4d": {
        "answers": "CH<sub>3</sub>CH<sub>2</sub>N(CH<sub>3</sub>)<sub>2</sub> (dimethylethylamine) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.11"
    },
    "2004-june-chm4-q5ai": {
        "answers": "–[–CH<sub>2</sub>–CH(CN)–]– (1)",
        "extra": "ignore n or brackets, but trailing bonds essential",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2004-june-chm4-q5aii": {
        "answers": "Addition or radical (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2004-june-chm4-q5bi": {
        "answers": "2-aminobutanoic (acid) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2004-june-chm4-q5bii": {
        "answers": "H<sub>3</sub>N<sup>+</sup>–CH(CH<sub>2</sub>CH<sub>3</sub>)–COOH (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2004-june-chm4-q5ci": {
        "answers": "C<sub>3</sub>H<sub>4</sub>O<sub>2</sub> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2004-june-chm4-q5cii": {
        "answers": "• Structure: HOOC–CH<sub>2</sub>CH<sub>2</sub>–COOH (1)<br>• Name: (1,4-)butan(e)dioic (acid) (1)",
        "extra": "allow succinic, but not dibutanoic nor butanedicarboxylic acid",
        "mark": 2,
        "spec": "3.3.12"
    },
    "2004-june-chm4-q5ciii": {
        "answers": "Can be hydrolysed / can react with acid or base or water / can react with nucleophiles (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2004-june-chm4-q6a": {
        "answers": "Pentan-2-one (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2004-june-chm4-q6bi": {
        "answers": "1680 &minus; 1750 (cm<sup>&minus;1</sup>) (C=O) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.16"
    },
    "2004-june-chm4-q6bii": {
        "answers": "3230 &minus; 3550 (O&minus;H alcohol) or 1000 &minus; 1300 (C&minus;O) (cm<sup>&minus;1</sup>) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.16"
    },
    "2004-june-chm4-q6c": {
        "answers": "4 (peaks) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2004-june-chm4-q6d": {
        "answers": "• Reagent: Acidified K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> (or Na / CH<sub>3</sub>COOH+H<sub>2</sub>SO<sub>4</sub>) (1)<br>• Observation with C: No reaction (1)<br>• Observation with D: Goes green (or effervescence / fruity smell) (1)",
        "extra": "penalise incomplete reagent (e.g. unacidified dichromate)",
        "mark": 3,
        "spec": "3.3.5"
    },
    "2004-june-chm4-q6e": {
        "answers": "• Reagent: Tollens' reagent OR Fehling's / Benedict's solution (1)<br>• Observation with E: Silver mirror OR red precipitate / goes red (1)",
        "extra": "not red solution for Fehling's",
        "mark": 2,
        "spec": "3.3.9"
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
        q_img_rel = f"img/2004-june-chm4/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        ms_img_rel = f"img/2004-june-chm4/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        q_obj = {
            "id": qid,
            "paper": "2004-june-chm4",
            "year": 2004,
            "series": "June",
            "code": "CHM4",
            "unit": "Unit 4: Further Physical and Organic Chemistry",
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

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-june-chm4 ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

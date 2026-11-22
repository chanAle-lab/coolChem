"""
Ingestion script for 2005 January CHM3/W (Section A only)
Excludes old-spec Section B essay questions (Q6).
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382849486_6024c1f3.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-jan-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-jan-chm3w",
    "year": 2005,
    "series": "January",
    "date": "2005-01-11",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry (CHM3/W)",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2005-jan-chm3w-q1ai", "1(a)(i)", 2, 80, 215, 1, ["3.3.1"], ["recall"], "Name the process used to separate petroleum into fractions.", None),
    ("2005-jan-chm3w-q1aii", "1(a)(ii)", 2, 220, 290, 1, ["3.3.1"], ["recall"], "Give the molecular formula for an alkane with nine carbon atoms.", None),
    ("2005-jan-chm3w-q1aiii", "1(a)(iii)", 2, 295, 365, 1, ["3.3.1"], ["recall"], "Write an equation for the complete combustion of alkane C11H24.", None),
    ("2005-jan-chm3w-q1aiv", "1(a)(iv)", 2, 370, 480, 1, ["3.3.1"], ["recall"], "Write an equation for the incomplete combustion of C11H24 to produce carbon and water only.", None),
    ("2005-jan-chm3w-q1bi", "1(b)(i)", 2, 485, 590, 1, ["3.3.1"], ["recall"], "Write an equation for thermal cracking of C10H22 to propene and an alkane only.", None),
    ("2005-jan-chm3w-q1bii", "1(b)(ii)", 2, 595, 680, 1, ["3.3.1"], ["recall"], "Draw the structure of the chain isomer of but-1-ene.", None),
    ("2005-jan-chm3w-q1c", "1(c)", 2, 685, 870, 2, ["3.3.1"], ["recall"], "State two other general features of an homologous series of compounds.", None),

    # Page 5: Question 2
    ("2005-jan-chm3w-q2a", "2(a)", 5, 80, 470, 4, ["3.3.1"], ["recall"], "Outline initiation, two propagation, and a termination step for methane with fluorine.", None),
    ("2005-jan-chm3w-q2b", "2(b)", 5, 475, 610, 1, ["3.3.1"], ["recall"], "Write an overall equation for reaction of fluorine with fluoromethane to form CF4.", None),

    # Page 6: Question 3(a)-(b)
    ("2005-jan-chm3w-q3a", "3(a)", 6, 80, 430, 2, ["3.3.1"], ["recall"], "State what is meant by the term position isomers.", ["img/2005-jan-chm3w/fig-q3-scheme.jpg"]),
    ("2005-jan-chm3w-q3b", "3(b)", 6, 435, 570, 2, ["3.3.1"], ["recall"], "Name compound A and compound C from reaction schemes.", ["img/2005-jan-chm3w/fig-q3-scheme.jpg"]),

    # Page 7: Question 3(c)-(d)
    ("2005-jan-chm3w-q3ci", "3(c)(i)", 7, 80, 185, 1, ["3.3.3"], ["recall"], "State the type of reaction in reaction schemes.", None),
    ("2005-jan-chm3w-q3cii", "3(c)(ii)", 7, 190, 290, 2, ["3.3.3"], ["recall"], "Identify a suitable combination of reagents for oxidation of alcohols.", None),
    ("2005-jan-chm3w-q3ciii", "3(c)(iii)", 7, 295, 400, 1, ["3.3.3"], ["recall"], "State how to ensure compound A is converted into butanoic acid rather than butanal.", None),
    ("2005-jan-chm3w-q3civ", "3(c)(iv)", 7, 405, 520, 1, ["3.3.3"], ["recall"], "Draw structure of isomer of compound A which does not react with these reagents.", None),
    ("2005-jan-chm3w-q3cv", "3(c)(v)", 7, 525, 675, 1, ["3.3.3"], ["recall"], "Draw structure of carboxylic acid formed by reaction of methanol with these reagents.", None),
    ("2005-jan-chm3w-q3di", "3(d)(i)", 7, 680, 770, 1, ["3.3.3"], ["recall"], "State a reagent which could be used to distinguish between butanal and compound C.", None),
    ("2005-jan-chm3w-q3dii", "3(d)(ii)", 7, 775, 870, 1, ["3.3.1"], ["recall"], "Draw structure of another aldehyde which is an isomer of butanal.", None),

    # Page 8: Question 4(a)-(b)
    ("2005-jan-chm3w-q4a", "4(a)", 8, 80, 310, 3, ["3.3.2"], ["recall"], "Complete mechanism by drawing curly arrows for 2-bromopentane to pent-2-ene.", None),
    ("2005-jan-chm3w-q4b", "4(b)", 8, 315, 600, 2, ["3.3.1"], ["recall"], "Draw and name the geometrical isomers of pent-2-ene.", None),

    # Page 9: Question 4(c)
    ("2005-jan-chm3w-q4ci", "4(c)(i)", 9, 80, 410, 4, ["3.3.2"], ["recall"], "Outline mechanism for reaction of pent-1-ene with hydrogen bromide.", None),
    ("2005-jan-chm3w-q4cii", "4(c)(ii)", 9, 415, 510, 1, ["3.3.2"], ["recall"], "Identify the minor product formed in reaction of pent-1-ene with HBr.", None),
    ("2005-jan-chm3w-q4ciii", "4(c)(iii)", 9, 515, 660, 2, ["3.3.2"], ["explanation"], "Explain why 2-bromopentane is the major product of this reaction.", None),

    # Page 10: Question 5
    ("2005-jan-chm3w-q5a", "5(a)", 10, 80, 310, 2, ["3.3.3"], ["recall"], "Name types of reaction: glucose to ethanol, ethanol to ethene.", None),
    ("2005-jan-chm3w-q5bi", "5(b)(i)", 10, 315, 410, 1, ["3.3.3"], ["recall"], "State what must be added to aqueous glucose so ethanol is formed.", None),
    ("2005-jan-chm3w-q5bii", "5(b)(ii)", 10, 415, 500, 1, ["3.3.3"], ["recall"], "Identify a suitable catalyst for conversion of ethanol into ethene.", None),
    ("2005-jan-chm3w-q5ci", "5(c)(i)", 10, 505, 575, 1, ["3.3.3"], ["recall"], "State the class of alcohols to which ethanol belongs.", None),
    ("2005-jan-chm3w-q5cii", "5(c)(ii)", 10, 580, 680, 1, ["3.3.3"], ["recall"], "Give one advantage of using ethanol as fuel compared with petroleum fraction.", None),
    ("2005-jan-chm3w-q5d", "5(d)", 10, 685, 765, 1, ["3.3.1"], ["recall"], "Write equation for production of ethene by heating ethane to 900°C.", None),
    ("2005-jan-chm3w-q5e", "5(e)", 10, 770, 850, 1, ["3.3.2"], ["recall"], "Name type of polymerisation when ethene is converted into poly(ethene).", None)
]

MS_DEF = {
    "2005-jan-chm3w-q1ai": {
        "answers": "fractional distillation or fractionation",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q1aii": {
        "answers": "C<sub>9</sub>H<sub>20</sub> only",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q1aiii": {
        "answers": "C<sub>11</sub>H<sub>24</sub> + 17O<sub>2</sub> → 11CO<sub>2</sub> + 12H<sub>2</sub>O",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q1aiv": {
        "answers": "C<sub>11</sub>H<sub>24</sub> + 6O<sub>2</sub> → 11C + 12H<sub>2</sub>O",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q1bi": {
        "answers": "C<sub>10</sub>H<sub>22</sub> → C<sub>3</sub>H<sub>6</sub> + C<sub>7</sub>H<sub>16</sub>",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q1bii": {
        "answers": "correctly drawn structure of methylpropene (CH<sub>2</sub>=C(CH<sub>3</sub>)<sub>2</sub>)",
        "extra": "(insist on clearly drawn C-C and C=C bonds)",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q1c": {
        "answers": "Any two from:<br>• chemically similar or chemically the same or react in the same way<br>• same functional group<br>• same general formula<br>• differ by CH<sub>2</sub> (2)",
        "extra": "(penalise same molecular formula or same empirical formula)",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q2a": {
        "answers": "F<sub>2</sub> → 2F• (1)<br>CH<sub>4</sub> + F• → •CH<sub>3</sub> + HF (1)<br>•CH<sub>3</sub> + F<sub>2</sub> → CH<sub>3</sub>F + F• (1)<br>•CH<sub>3</sub> + F• → CH<sub>3</sub>F<br>OR 2•CH<sub>3</sub> → C<sub>2</sub>H<sub>6</sub> (1)",
        "extra": "(allow credit on this occasion for 2F• → F<sub>2</sub>)<br>(penalise incorrect symbol Fl, once only)<br>(penalise absence of radical dot once only)",
        "mark": 4,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q2b": {
        "answers": "CH<sub>3</sub>F + 3F<sub>2</sub> → CF<sub>4</sub> + 3HF",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q3a": {
        "answers": "Compounds with the same molecular formula (1)<br>but different structures due to different positions of the same functional group on the same carbon skeleton/chain (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q3b": {
        "answers": "Compound A is butan-1-ol only (1)<br>Compound C is butanone or butan-2-one (1)",
        "extra": "(penalise but-1-ol, but allow repeat error for but-2-one)<br>(credit butane-1-ol)",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q3ci": {
        "answers": "oxidation or redox",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q3cii": {
        "answers": "K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> or potassium dichromate(VI) (1)<br>acidified or H<sub>2</sub>SO<sub>4</sub> (or other identified strong acid) (1)",
        "extra": "(penalise the dichromate ion or incorrect oxidation state, but mark on)<br>(penalise H<sup>+</sup>)<br>(do not credit the acid unless M1 has been correctly attempted)",
        "mark": 2,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q3ciii": {
        "answers": "(heat under) reflux<br>OR use excess oxidising agent",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q3civ": {
        "answers": "correctly drawn structure of 2-methylpropan-2-ol ((CH<sub>3</sub>)<sub>3</sub>COH)",
        "extra": "(insist on clearly drawn C-C and C-O bonds)",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q3cv": {
        "answers": "correctly drawn structure of methanoic acid (HCOOH)",
        "extra": "(insist on C-O and C=O displayed in the formula)",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q3di": {
        "answers": "Tollens' reagent or this whole reagent specified (ammoniacal silver nitrate)<br>OR Fehling's solution<br>OR acidified potassium dichromate(VI)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q3dii": {
        "answers": "correctly drawn structure of methylpropanal ((CH<sub>3</sub>)<sub>2</sub>CHCHO)",
        "extra": "(insist on C-H and C=O of aldehyde displayed in the formula)",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q4a": {
        "answers": "M1 curly arrow from lone pair on oxygen of hydroxide ion to H atom on C-H adjacent to C-Br (1)<br>M2 curly arrow from single bond of adjacent C-H to adjacent single bond C-C (1)<br>M3 curly arrow from C-Br bond to side of Br atom (1)",
        "extra": "(only credit M2 if M1 is being attempted to correct H atom)<br>(credit M3 independently)",
        "mark": 3,
        "spec": "3.3.2"
    },
    "2005-jan-chm3w-q4b": {
        "answers": "M1 credit a correct structure for either geometrical isomer and its designation as either cis or trans (1)<br>M2 credit a second mark if all four parts of the required structures and names are correct (1)",
        "extra": "(credit 'linear' structures)<br>(insist on the alkyl groups being attached clearly by C-C bonds)",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q4ci": {
        "answers": "M1 curly arrow from middle of C=C bond to H atom on H-Br (1)<br>M2 curly arrow from H-Br bond to side of Br atom (1)<br>M3 correct structure for correct secondary carbocation (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>C<sup>+</sup>HCH<sub>3</sub>) (1)<br>M4 curly arrow from lone pair on bromide ion to the positive carbon of carbocation (1)",
        "extra": "(penalise M1 if partial negative charge or formal positive charge on H)<br>(penalise M1 if pent-2-ene is used)<br>(with exception of pent-2-ene, if wrong alkene used, only penalise structure M3)<br>(penalise use of two dots in addition to covalent bond, once only)",
        "mark": 4,
        "spec": "3.3.2"
    },
    "2005-jan-chm3w-q4cii": {
        "answers": "1-bromopentane",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2005-jan-chm3w-q4ciii": {
        "answers": "M1 2-bromopentane is formed via the secondary (or 2°) carbocation<br>OR 1-bromopentane is formed via the primary (or 1°) carbocation (1)<br>M2 a secondary carbocation is more stable than a primary carbocation (1)",
        "extra": "(the argument must involve clear statements about carbocations)",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2005-jan-chm3w-q5a": {
        "answers": "Glucose to ethanol: fermentation (1)<br>Ethanol to ethene: dehydration or elimination (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q5bi": {
        "answers": "yeast OR zymase OR an enzyme",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q5bii": {
        "answers": "concentrated sulphuric or phosphoric acid",
        "extra": "(penalise aqueous or dilute as a contradiction)",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q5ci": {
        "answers": "primary or 1°",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q5cii": {
        "answers": "sugar or glucose or ethanol is renewable<br>OR ethanol does not contain sulphur-containing impurities<br>OR ethanol produces less pollution or is less smoky or less CO/C",
        "extra": "(the objective is a positive statement about ethanol)<br>(penalise the idea that ethanol is an infinite source or vague statements that ethanol has less impurities)<br>(penalise the idea that ethanol produces no pollution)",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2005-jan-chm3w-q5d": {
        "answers": "C<sub>2</sub>H<sub>6</sub> → C<sub>2</sub>H<sub>4</sub> + H<sub>2</sub>",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2005-jan-chm3w-q5e": {
        "answers": "Addition",
        "extra": "(ignore self or chain as a preface to 'addition')<br>(penalise additional)",
        "mark": 1,
        "spec": "3.3.2"
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
        img_rel = f"img/2005-jan-chm3w/{img_filename}"
        img_abs = os.path.join(REPO_DIR, img_rel.replace("/", os.sep))
        
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        im.save(img_abs, format="JPEG", quality=92)
        
        # Render official mark scheme image
        ms_data = MS_DEF[qid]
        ms_filename = f"ms_{subpart_name}.png"
        ms_img_rel = f"img/2005-jan-chm3w/{ms_filename}"
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

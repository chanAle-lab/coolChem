"""
Ingestion script for 2005 January CHM2 (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382849428_1c35b8c8.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-jan-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-jan-chm2",
    "year": 2005,
    "series": "January",
    "date": "2005-01-11",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2005-jan-chm2-q1a", "1(a)", 2, 80, 275, 4, ["3.1.3", "3.2.3"], ["explanation"], "State the trend in boiling points of halogens from fluorine to iodine and explain this trend.", None),
    ("2005-jan-chm2-q1bi", "1(b)(i)", 2, 280, 420, 2, ["3.2.3"], ["recall"], "Observation and equation for reaction of aqueous bromide ions with chlorine gas.", None),
    ("2005-jan-chm2-q1bii", "1(b)(ii)", 2, 425, 600, 3, ["3.2.3"], ["recall"], "Observations and equation for bromide with silver nitrate followed by concentrated ammonia.", None),
    ("2005-jan-chm2-q1biii", "1(b)(iii)", 2, 605, 725, 2, ["3.2.3"], ["recall"], "State two observations for reaction of solid KBr with concentrated sulphuric acid.", None),
    ("2005-jan-chm2-q1c", "1(c)", 2, 730, 840, 2, ["3.1.7", "3.2.3"], ["recall"], "Write equation for redox reaction of potassium bromide with concentrated sulphuric acid.", None),

    # Page 5: Question 2
    ("2005-jan-chm2-q2a", "2(a)", 5, 80, 185, 1, ["3.1.7"], ["recall"], "Explain the meaning of oxidising agent in terms of electrons.", None),
    ("2005-jan-chm2-q2b", "2(b)", 5, 190, 280, 1, ["3.1.7"], ["recall"], "Explain meaning of oxidation state for element X in ionic compound MX.", None),
    ("2005-jan-chm2-q2c", "2(c)", 5, 285, 490, 3, ["3.1.7"], ["recall"], "Deduce oxidation states of C in CO3(2-), P in PCl4(+), and N in Mg3N2.", None),
    ("2005-jan-chm2-q2di", "2(d)(i)", 5, 495, 620, 1, ["3.1.7"], ["recall"], "Write half-equation for oxidation of copper to copper(II) ions.", None),
    ("2005-jan-chm2-q2dii", "2(d)(ii)", 5, 625, 715, 1, ["3.1.7"], ["recall"], "Write half-equation for reduction of nitrate ions to nitrogen monoxide in acidified solution.", None),
    ("2005-jan-chm2-q2diii", "2(d)(iii)", 5, 720, 820, 1, ["3.1.7"], ["recall"], "Write overall equation for reaction of copper with acidified nitrate ions.", None),

    # Page 6: Question 3
    ("2005-jan-chm2-q3a", "3(a)", 6, 80, 565, 1, ["3.1.5"], ["explanation"], "State how the curve could be used to find rate of reaction at point A.", ["img/2005-jan-chm2/fig-q3-curve.jpg"]),
    ("2005-jan-chm2-q3bi", "3(b)(i)", 6, 570, 660, 2, ["3.1.5"], ["explanation"], "Sketch curve X on axes for 100 cm3 of 1.0 mol dm-3 H2O2.", ["img/2005-jan-chm2/fig-q3-curve.jpg"]),
    ("2005-jan-chm2-q3bii", "3(b)(ii)", 6, 665, 780, 2, ["3.1.5"], ["explanation"], "Sketch curve Y on axes for 25 cm3 of 2.0 mol dm-3 H2O2 with catalyst.", ["img/2005-jan-chm2/fig-q3-curve.jpg"]),

    # Page 7: Question 3(c)
    ("2005-jan-chm2-q3ci", "3(c)(i)", 7, 80, 240, 1, ["3.1.5"], ["recall"], "Write overall equation for decomposition of hydrogen peroxide.", None),
    ("2005-jan-chm2-q3cii", "3(c)(ii)", 7, 245, 360, 2, ["3.1.5"], ["recall"], "Define the term catalyst.", None),
    ("2005-jan-chm2-q3ciii", "3(c)(iii)", 7, 365, 520, 2, ["3.1.5"], ["explanation"], "Give two reasons suggesting hydrogen bromide behaves as a catalyst in given equations.", None),

    # Page 8: Question 4
    ("2005-jan-chm2-q4ai", "4(a)(i)", 8, 80, 215, 1, ["3.1.2", "3.2.2"], ["recall"], "Write equation to illustrate how carbon monoxide is formed in Blast Furnace.", None),
    ("2005-jan-chm2-q4aii", "4(a)(ii)", 8, 220, 290, 1, ["3.2.2"], ["recall"], "Write equation to illustrate how carbon monoxide reduces iron(III) oxide.", None),
    ("2005-jan-chm2-q4aiii", "4(a)(iii)", 8, 295, 410, 2, ["3.1.5", "3.2.2"], ["explanation"], "Suggest in terms of collisions why CO reacts more rapidly with Fe2O3 than does C.", None),
    ("2005-jan-chm2-q4b", "4(b)", 8, 415, 490, 1, ["3.2.2"], ["recall"], "State why carbon is not used to reduce oxide of titanium to metal.", None),
    ("2005-jan-chm2-q4ci", "4(c)(i)", 8, 495, 570, 1, ["3.2.2"], ["recall"], "Name the converter used to remove impurities from iron obtained from Blast Furnace.", None),
    ("2005-jan-chm2-q4cii", "4(c)(ii)", 8, 575, 640, 1, ["3.2.2"], ["recall"], "Write equation to illustrate how sulphur impurity is removed from iron.", None),
    ("2005-jan-chm2-q4ciii", "4(c)(iii)", 8, 645, 725, 2, ["3.2.2"], ["recall"], "State how phosphorus impurity is removed from iron in this converter.", None),
    ("2005-jan-chm2-q4civ", "4(c)(iv)", 8, 730, 830, 2, ["3.2.2"], ["explanation"], "Explain two major benefits of using some scrap iron in this converter.", None),
    ("2005-jan-chm2-q4d", "4(d)", 8, 835, 930, 2, ["3.2.2"], ["recall"], "Give two reasons why titanium is a more expensive metal than iron.", None)
]

MS_DEF = {
    "2005-jan-chm2-q1a": {
        "answers": "Increase (1)<br>Van der Waals forces between molecules (1)<br>Increase with size (or Mr or surface area etc) (1)<br>More energy needed to break (overcome) these forces (1)",
        "extra": "(Note max 2 from last three marks if no mention of molecules or 'molecular')",
        "mark": 4,
        "spec": "3.1.3 / 3.2.3"
    },
    "2005-jan-chm2-q1bi": {
        "answers": "Observation: Brown solution (or yellow or orange) (1)<br>Equation: Cl<sub>2</sub> + 2Br<sup>–</sup> → 2Cl<sup>–</sup> + Br<sub>2</sub> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2005-jan-chm2-q1bii": {
        "answers": "Observation with AgNO<sub>3</sub>: cream precipitate (1)<br>Equation: Br<sup>–</sup> + Ag<sup>+</sup> → AgBr (1)<br>Observation with conc. NH<sub>3</sub>: Precipitate dissolves (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.3"
    },
    "2005-jan-chm2-q1biii": {
        "answers": "Any two from:<br>• orange (brown) fumes (gas)<br>• white fumes (or misty fumes)<br>• choking gas (2)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2005-jan-chm2-q1c": {
        "answers": "2H<sup>+</sup> + H<sub>2</sub>SO<sub>4</sub> + 2Br<sup>–</sup> → SO<sub>2</sub> + Br<sub>2</sub> + 2H<sub>2</sub>O<br><b>OR</b> 2KBr + 2H<sub>2</sub>SO<sub>4</sub> → K<sub>2</sub>SO<sub>4</sub> + SO<sub>2</sub> + Br<sub>2</sub> + 2H<sub>2</sub>O",
        "extra": "(SO<sub>2</sub> and Br<sub>2</sub> (1), balanced equation (1))",
        "mark": 2,
        "spec": "3.1.7 / 3.2.3"
    },
    "2005-jan-chm2-q2a": {
        "answers": "Accepts electrons",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2005-jan-chm2-q2b": {
        "answers": "Charge on the ion (or element or atom)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2005-jan-chm2-q2c": {
        "answers": "Carbon in CO<sub>3</sub><sup>2–</sup>: +4 (1)<br>Phosphorus in PCl<sub>4</sub><sup>+</sup>: +5 (1)<br>Nitrogen in Mg<sub>3</sub>N<sub>2</sub>: –3 (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.7"
    },
    "2005-jan-chm2-q2di": {
        "answers": "Cu → Cu<sup>2+</sup> + 2e<sup>–</sup>",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2005-jan-chm2-q2dii": {
        "answers": "NO<sub>3</sub><sup>–</sup> + 4H<sup>+</sup> + 3e<sup>–</sup> → NO + 2H<sub>2</sub>O",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2005-jan-chm2-q2diii": {
        "answers": "3Cu + 2NO<sub>3</sub><sup>–</sup> + 8H<sup>+</sup> → 3Cu<sup>2+</sup> + 2NO + 4H<sub>2</sub>O",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2005-jan-chm2-q3a": {
        "answers": "Gradient (or slope) (or draw a tangent)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2005-jan-chm2-q3bi": {
        "answers": "Curve X is lower and starts at origin (1)<br>And levels out at same volume as original curve (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2005-jan-chm2-q3bii": {
        "answers": "Curve Y is steeper than original and starts at origin (1)<br>Then levels out at half the volume of the original (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2005-jan-chm2-q3ci": {
        "answers": "2H<sub>2</sub>O<sub>2</sub> → 2H<sub>2</sub>O + O<sub>2</sub>",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2005-jan-chm2-q3cii": {
        "answers": "Speeds up (alters the rate of) a chemical reaction (1)<br>Remains unchanged (or not used up) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2005-jan-chm2-q3ciii": {
        "answers": "Remains unchanged (or not used up or not in the overall reaction equation) (1)<br>Offers alternative reaction route (or acts as an intermediate) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2005-jan-chm2-q4ai": {
        "answers": "C + CO<sub>2</sub> → 2CO (or 2C + O<sub>2</sub> → 2CO, or carbon reduction of an iron oxide)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2 / 3.2.2"
    },
    "2005-jan-chm2-q4aii": {
        "answers": "3CO + Fe<sub>2</sub>O<sub>3</sub> → 3CO<sub>2</sub> + 2Fe",
        "extra": "",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2005-jan-chm2-q4aiii": {
        "answers": "CO is gaseous (or C is solid) (1)<br>CO has more collisions (or C has very few collisions) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5 / 3.2.2"
    },
    "2005-jan-chm2-q4b": {
        "answers": "Titanium carbide is stable.",
        "extra": "",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2005-jan-chm2-q4ci": {
        "answers": "Basic oxygen process (or BOS)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2005-jan-chm2-q4cii": {
        "answers": "Mg + S → MgS",
        "extra": "",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2005-jan-chm2-q4ciii": {
        "answers": "React with oxygen (1)<br>Forms phosphorus oxide (or P<sub>4</sub>O<sub>10</sub>) and removed as slag (or phosphate) (with CaO) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.2"
    },
    "2005-jan-chm2-q4civ": {
        "answers": "Any two from:<br>• saves energy<br>• removes scrap from environment<br>• uses fewer raw materials<br>• fewer greenhouse gases released<br>• less CO released / less SO<sub>2</sub> released<br>• less mining<br>• has greater % of iron / correct economic argument (2)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.2"
    },
    "2005-jan-chm2-q4d": {
        "answers": "Cost of chlorine or sodium (or Mg) or argon or batch process (1)<br>Mention of another of these factors (1)",
        "extra": "(cost is QL mark)",
        "mark": 2,
        "spec": "3.2.2"
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
        img_rel = f"img/2005-jan-chm2/{img_filename}"
        img_abs = os.path.join(REPO_DIR, img_rel.replace("/", os.sep))
        
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        im.save(img_abs, format="JPEG", quality=92)
        
        # Render official mark scheme image
        ms_data = MS_DEF[qid]
        ms_filename = f"ms_{subpart_name}.png"
        ms_img_rel = f"img/2005-jan-chm2/{ms_filename}"
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

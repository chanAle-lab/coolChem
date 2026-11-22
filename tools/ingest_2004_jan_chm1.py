"""
Ingestion script for 2004 January CHM1 (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960711_d83e0ad2.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2004-jan-chm1")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2004-jan-chm1",
    "year": 2004,
    "series": "January",
    "date": "2004-01-09",
    "code": "CHM1",
    "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour"
}

QUESTIONS_DEF = [
    # Page 2: Question 1
    ("2004-jan-chm1-q1ai", "1(a)(i)", 2, 75, 230, 2, ["3.1.1"], ["recall"], "Define the term isotopes in terms of fundamental particles present."),
    ("2004-jan-chm1-q1aii", "1(a)(ii)", 2, 232, 335, 1, ["3.1.1"], ["recall"], "Explain why isotopes of the same element have the same chemical properties."),
    ("2004-jan-chm1-q1aiii", "1(a)(iii)", 2, 338, 480, 2, ["3.1.2"], ["calculation"], "Calculate the mass in grams of a single atom of 23Na using Avogadro constant."),
    ("2004-jan-chm1-q1b", "1(b)", 2, 482, 570, 1, ["3.1.1"], ["recall"], "Give electronic configuration showing all sub-levels for a sodium atom."),
    ("2004-jan-chm1-q1c", "1(c)", 2, 572, 675, 1, ["3.1.1", "3.2.1"], ["recall"], "Explain why chromium is placed in the d block in the Periodic Table."),
    ("2004-jan-chm1-q1d", "1(d)", 2, 678, 775, 2, ["3.1.1"], ["recall"], "Give symbol including mass number and atomic number for atom derived from 28Si."),

    # Page 5: Question 2
    ("2004-jan-chm1-q2a", "2(a)", 5, 75, 230, 2, ["3.1.1"], ["recall"], "Describe how positive ions are formed from gaseous chromium atoms in mass spectrometer."),
    ("2004-jan-chm1-q2b", "2(b)", 5, 232, 320, 1, ["3.1.1"], ["recall"], "What is used in a mass spectrometer to accelerate the positive ions?"),
    ("2004-jan-chm1-q2c", "2(c)", 5, 322, 410, 1, ["3.1.1"], ["recall"], "What is used in a mass spectrometer to deflect the positive ions?"),
    ("2004-jan-chm1-q2d", "2(d)", 5, 412, 775, 2, ["3.1.1"], ["calculation"], "Calculate relative atomic mass of chromium from isotopic abundance data."),

    # Page 6: Question 3(a)
    ("2004-jan-chm1-q3ai", "3(a)(i)", 6, 75, 290, 1, ["3.1.2"], ["calculation"], "Calculate moles of HCl in 75.0 cm3 of 0.500 mol dm-3 hydrochloric acid."),
    ("2004-jan-chm1-q3aii", "3(a)(ii)", 6, 292, 375, 1, ["3.1.2"], ["calculation"], "Calculate moles of NaOH used to neutralise unreacted HCl."),
    ("2004-jan-chm1-q3aiii", "3(a)(iii)", 6, 378, 460, 1, ["3.1.2"], ["calculation"], "Show that moles of HCl reacting with MgCO3 was 0.0267 mol."),
    ("2004-jan-chm1-q3aiv", "3(a)(iv)", 6, 462, 775, 4, ["3.1.2"], ["calculation"], "Calculate moles, mass and percentage by mass of MgCO3 in sample."),

    # Page 7: Question 3(b)
    ("2004-jan-chm1-q3bi", "3(b)(i)", 7, 75, 340, 3, ["3.1.2"], ["calculation"], "Show that empirical formula of compound (36.5% Na, 25.5% S) is Na2SO3."),
    ("2004-jan-chm1-q3bii", "3(b)(ii)", 7, 342, 520, 1, ["3.1.2"], ["recall"], "Write equation for reaction of Na2SO3 with excess hydrochloric acid."),

    # Page 8: Question 4
    ("2004-jan-chm1-q4a", "4(a)", 8, 75, 385, 5, ["3.1.2"], ["calculation"], "State ideal gas equation and calculate moles and Mr of oxide A."),
    ("2004-jan-chm1-q4bi", "4(b)(i)", 8, 388, 485, 1, ["3.2.2"], ["recall"], "Identify reagent used to test for sulphate ions in aqueous solution."),
    ("2004-jan-chm1-q4bii", "4(b)(ii)", 8, 488, 570, 1, ["3.2.2"], ["recall"], "State observation if sulphate ion test is positive."),
    ("2004-jan-chm1-q4biii", "4(b)(iii)", 8, 572, 775, 1, ["3.2.2"], ["recall"], "Write ionic equation for positive sulphate ion test."),

    # Page 9: Question 5
    ("2004-jan-chm1-q5a", "5(a)", 9, 75, 420, 3, ["3.1.1"], ["analysis"], "Mark approximate positions of first IE for Na, P, S on Period 3 diagram."),
    ("2004-jan-chm1-q5b", "5(b)", 9, 422, 595, 3, ["3.1.1"], ["recall"], "Explain general increase in first ionisation energies from Na to Ar."),
    ("2004-jan-chm1-q5c", "5(c)", 9, 598, 775, 4, ["3.1.1"], ["recall"], "Explain position of aluminium and sulphur in terms of electron sub-levels.")
]

MS_DATA = {
    "2004-jan-chm1-q1ai": {
        "answers": "• Atoms with the same number of protons / proton number (1)<br>• with different numbers of neutrons (1)",
        "extra": "NOT same atomic number.<br>NOT different mass number / fewer neutrons.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q1aii": {
        "answers": "Chemical properties depend on the <u>number or amount of (outer) electrons</u><br><i>OR</i> isotopes have the same <u>electron configuration</u> / same number of e<sup>&minus;</sup> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q1aiii": {
        "answers": "• 23 / (6.023 &times; 10<sup>23</sup>) (1)<br>• = <b>3.8(2) &times; 10<sup>&minus;23</sup> (g)</b> (1)",
        "extra": "CE = 0 if inverted or multiplied.<br>[2-5 sig figs]. Tied to M1.",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q1b": {
        "answers": "<b>1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>1</sup></b> (1)",
        "extra": "Accept subscripted figures.",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q1c": {
        "answers": "Highest energy e<sup>&minus;</sup> / outer e<sup>&minus;</sup>s / last e<sup>&minus;</sup> in <b>(3)d sub-shell</b> <i>OR</i> d sub-shell being filled / is incomplete<br><i>OR</i> highest energy sub-shell is (3)d (1)",
        "extra": "NOT transition element / e configuration ends at 3d.",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q1d": {
        "answers": "• <b><sup>15</sup><sub>7</sub>N</b> (1) [correct symbol]<br>• Mass number = <b>15</b> <u>AND</u> atomic number = <b>7</b> (1)",
        "extra": "Allow N<sup>15</sup><sub>7</sub>.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q2a": {
        "answers": "• High speed electrons <i>OR</i> electrons from an electron gun (1)<br>• Knocks out an (outer-shell) electron (on the chromium atom) (1)<br>[Accept Cr(g) + e<sup>&minus;</sup> &rarr; Cr<sup>+</sup>(g) + 2e<sup>&minus;</sup>]",
        "extra": "NOT e gun alone / beam of e / bombardment with e.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q2b": {
        "answers": "Electric field <i>OR</i> (attraction to) &minus;ve plate <i>OR</i> electrostatic attraction <i>OR</i> (repelled by) +ve plate <i>OR</i> charged plate (1)",
        "extra": "NOT high p.d. / electromagnetic field / electric plates.",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q2c": {
        "answers": "Magnet <i>OR</i> magnetic field <i>OR</i> electromagnet (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q2d": {
        "answers": "• <i>A</i><sub>r</sub> = (50 &times; 0.043) + (52 &times; 0.838) + (53 &times; 0.095) + (54 &times; 0.024) (1)<br>• = <b>52.06</b> <i>OR</i> <b>52.05</b> (1)",
        "extra": "Mark consequentially on transcription or addition of % error.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q3ai": {
        "answers": "75.0 &times; 10<sup>&minus;3</sup> &times; 0.500 = <b>0.0375 (mol)</b> (1)",
        "extra": "Accept 0.037 or 0.038.",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q3aii": {
        "answers": "21.6 &times; 10<sup>&minus;3</sup> &times; 0.500 = <b>0.0108 (mol)</b> (1)",
        "extra": "Accept 0.011.<br>[If both (i) and (ii) answers wrong, allow ONE process mark for both correct processes].",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q3aiii": {
        "answers": "0.0375 &minus; 0.0108 = <b>0.0267 (mol)</b> (1)",
        "extra": "NOT conseq &ndash; must use figures shown.",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q3aiv": {
        "answers": "• Moles of MgCO<sub>3</sub> = 0.0267 / 2 = <b>0.01335 (mol)</b> (1) [allow 0.0134 &ndash; 0.0133]<br>• Mass of MgCO<sub>3</sub> = 0.01335 &times; 84.3 [allow 84] (1) = <b>1.125 g</b> (1) [accept 1.13 g]<br>• Percentage of MgCO<sub>3</sub> = (1.125 / 1.25) &times; 100 (1) = <b>90%</b> (1) [range = 89.5 &ndash; 90.5%]",
        "extra": "Mark conseq on moles of MgCO3 and check for inversion. If % expression inverted, lose M4 and M5.",
        "mark": 4,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q3bi": {
        "answers": "• % oxygen = <b>38.0</b> (1)<br>• Na = 36.5/23 = 1.587, S = 25.5/32(.1) = 0.794, O = 38.0/16 = 2.375 (1)<br>• Ratio = <b>2 : 1 : 3</b> &rarr; Na<sub>2</sub>SO<sub>3</sub> (1)",
        "extra": "[If no % of oxygen Max 1 (allow M2 only)]<br>[If % for Na and S transposed or atomic numbers used, M1 only available].",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q3bii": {
        "answers": "<b>Na<sub>2</sub>SO<sub>3</sub> + 2HCl &rarr; 2NaCl + H<sub>2</sub>O + SO<sub>2</sub></b> (1)",
        "extra": "Allow multiples.<br>Allow SO<sub>3</sub><sup>2&minus;</sup> + 2H<sup>+</sup> &rarr; H<sub>2</sub>O + SO<sub>2</sub>.",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q4a": {
        "answers": "• Ideal gas equation: <b><i>pV</i> = <i>nRT</i></b> (1)<br>• Calculation: <i>n</i> = <i>pV</i>/<i>RT</i> = (103000 &times; 127 &times; 10<sup>&minus;6</sup>) / (8.31 &times; 415) (1) = <b>3.79 &times; 10<sup>&minus;3</sup> (mol)</b> (1) [range 3.79 &times; 10<sup>&minus;3</sup> to 3.8 &times; 10<sup>&minus;3</sup>]<br>• <i>M</i><sub>r</sub> = <i>m</i>/<i>n</i> = 0.304 / (3.79 &times; 10<sup>&minus;3</sup>) = <b>80.1</b> (1) [range 80 &ndash; 80.3] min 2+ s.f.",
        "extra": "[If 'V' wrong lose M2; 'p' wrong lose M3; 'inverted' lose M3 and M4].",
        "mark": 5,
        "spec": "3.1.2"
    },
    "2004-jan-chm1-q4bi": {
        "answers": "<b>BaCl<sub>2</sub></b> <i>OR</i> <b>barium chloride</b> (1)",
        "extra": "Allow barium nitrate / hydroxide / ethanoate.<br>Not Ba2+ but allow M2 and M3 as conseq. [If reagent wrong, CE = 0].",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm1-q4bii": {
        "answers": "<b>White precipitate</b> / solid / suspension (1)",
        "extra": "NOT cloudy / milky.",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm1-q4biii": {
        "answers": "<b>Ba<sup>2+</sup> + SO<sub>4</sub><sup>2&minus;</sup> &rarr; BaSO<sub>4</sub></b> (1)",
        "extra": "Do not allow spectator ions.",
        "mark": 1,
        "spec": "3.2.2"
    },
    "2004-jan-chm1-q5a": {
        "answers": "• Na point marked below Al (1)<br>• P point marked above Si but below Cl (1)<br>• S point marked below P and Cl but above Si (1)<br>Crosses joined with straight lines.",
        "extra": "",
        "mark": 3,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q5b": {
        "answers": "• Increased nuclear charge / proton number (1)<br>• Electrons enter same shell / energy level <i>OR</i> atoms get smaller <i>OR</i> same shielding (1)<br>• Stronger attraction between nucleus and (outer) electrons (1)",
        "extra": "NOT increased atomic number.",
        "mark": 3,
        "spec": "3.1.1"
    },
    "2004-jan-chm1-q5c": {
        "answers": "<u>Explanation for aluminium:</u><br>• (third) electron in <b>(3)p sub-shell</b> (1)<br>• Sub-shell further away from nucleus <i>OR</i> of higher energy <i>OR</i> extra shielding from (3)s (1)<br><br><u>Explanation for sulphur:</u><br>• Pair of electrons in (3)p orbital (1)<br>• Repulsion between electrons (1)",
        "extra": "[Penalise '2p' once only].",
        "mark": 4,
        "spec": "3.1.1"
    }
}

def main():
    doc = fitz.open(QP_PATH)
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    existing_ids = {q["id"] for q in db["questions"]}
    added = 0

    for qid, q_label, p_num, y0, y1, mark, spec_topics, skills, prompt in QUESTIONS_DEF:
        # 1. Question image
        page = doc[p_num - 1]
        rect = fitz.Rect(35, y0, 545, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
        im = Image.open(fitz.io.BytesIO(pix.tobytes("png"))).convert("RGB")
        q_img_rel = f"img/2004-jan-chm1/q_{qid.split('-')[-1]}.jpg"
        q_img_abs = os.path.join(REPO_DIR, q_img_rel.replace("/", os.sep))
        im.save(q_img_abs, format="JPEG", quality=92)

        # 2. Markscheme image
        ms_img_rel = f"img/2004-jan-chm1/ms_{qid.split('-')[-1]}.png"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))
        ms = MS_DATA[qid]
        render_official_markscheme_image(q_label, ms["answers"], ms["extra"], ms["mark"], ms["spec"], ms_img_abs)

        # 3. DB object
        q_obj = {
            "id": qid,
            "paper": "2004-jan-chm1",
            "year": 2004,
            "series": "January",
            "code": "CHM1",
            "unit": "Unit 1: Atomic Structure, Bonding and Periodicity",
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

    print(f"Ingested {len(QUESTIONS_DEF)} questions for 2004-jan-chm1 ({added} newly added).")
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Saved questions.json successfully.")

if __name__ == "__main__":
    main()

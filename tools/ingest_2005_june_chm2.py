"""
Ingestion script for 2005 June CHM2 (Section A only)
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

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382980221_a694d6cb.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2005-june-chm2")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2005-june-chm2",
    "year": 2005,
    "series": "June",
    "date": "2005-06-08",
    "code": "CHM2",
    "unit": "Unit 2: Foundation Physical and Inorganic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry"
}

def extract_figures(doc):
    p6 = doc[5]
    rect = fitz.Rect(70, 240, 520, 530)
    pix = p6.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    fig_path = os.path.join(IMG_DIR, "fig-q2-curves.jpg")
    im.save(fig_path, format="JPEG", quality=92)
    print("Saved fig-q2-curves.jpg")

QUESTIONS_DATA = [
    # Q1
    {
        "id": "2005-june-chm2-q1a",
        "question": "1(a)",
        "marks": 5,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "Explain the meaning of the terms mean bond enthalpy and standard enthalpy of formation.",
        "figures": [],
        "ms_rows": [
            ("1(a)", "Mean bond enthalpy: Enthalpy (or energy) to break (or dissociate) a bond", "1 mark for bond breaking energy", "1", "AO1 / 3.1.4"),
            ("", "Averaged over different molecules / environments", "1 mark for average across environments", "1", "AO1 / 3.1.4"),
            ("", "Standard enthalpy of formation: Enthalpy change when one mole of a compound", "1 mark for 1 mole of compound", "1", "AO1 / 3.1.4"),
            ("", "Is formed from its constituent elements", "1 mark for from elements", "1", "AO1 / 3.1.4"),
            ("", "In their standard states (under standard conditions)", "1 mark for standard states", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2005-june-chm2-q1b",
        "question": "1(b)",
        "marks": 3,
        "page": 2,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Calculate enthalpy change for reaction of hydrazine with hydrogen peroxide using bond enthalpies.",
        "figures": [],
        "ms_rows": [
            ("1(b)", "Delta H = sum(bonds broken) – sum(bonds formed)", "1 mark for method / cycle", "1", "AO1 / 3.1.4"),
            ("", "= [4(N–H) + (N–N) + 2(O–O) + 4(O–H)] – [(N≡N) + 8(O–H)]\n= 4(388) + 163 + 2(146) + 4(463) – [944 + 8(463)]", "1 mark for correct numerical substitution", "1", "AO2 / 3.1.4"),
            ("", "= –789 kJ mol–1", "1 mark for –789 (+789 scores 1 only)", "1", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2005-june-chm2-q1ci",
        "question": "1(c)(i)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["recall"],
        "summary": "State the value of Delta Hf for N2(g).",
        "figures": [],
        "ms_rows": [
            ("1(c)(i)", "Zero / 0 (kJ mol–1)", "By definition enthalpy of formation of an element is zero", "1", "AO1 / 3.1.4")
        ]
    },
    {
        "id": "2005-june-chm2-q1cii",
        "question": "1(c)(ii)",
        "marks": 3,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["calculation"],
        "summary": "Calculate enthalpy change for reaction using Delta Hf values from table.",
        "figures": [],
        "ms_rows": [
            ("1(c)(ii)", "Delta H = sum(Delta Hf products) – sum(Delta Hf reactants)", "1 mark for method expression", "1", "AO1 / 3.1.4"),
            ("", "= [0 + 4(–242)] – [75 + 2(–133)]", "1 mark for correct numbers", "1", "AO2 / 3.1.4"),
            ("", "= –777 kJ mol–1", "1 mark for –777 (+777 scores 1 mark only)", "1", "AO2 / 3.1.4")
        ]
    },
    {
        "id": "2005-june-chm2-q1d",
        "question": "1(d)",
        "marks": 1,
        "page": 5,
        "topics": ["3.1.4"],
        "skills": ["explanation"],
        "summary": "Explain why value obtained in part (b) is different from that obtained in part (c)(ii).",
        "figures": [],
        "ms_rows": [
            ("1(d)", "Mean bond enthalpies are not exact / are average values from various molecules\n(whereas Delta Hf values are specific to the actual compounds)", "Allow mean bond enthalpies are approximations", "1", "AO1 / 3.1.4")
        ]
    },

    # Q2
    {
        "id": "2005-june-chm2-q2a",
        "question": "2(a)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.6"],
        "skills": ["analysis"],
        "summary": "Mark point X on curve A representing time equilibrium is first reached.",
        "figures": ["img/2005-june-chm2/fig-q2-curves.jpg"],
        "ms_rows": [
            ("2(a)", "Mark labelled X on curve A where curve becomes flat / horizontal (where curve C joins A)", "Point at start of plateau of curve A", "1", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2005-june-chm2-q2b",
        "question": "2(b)",
        "marks": 1,
        "page": 6,
        "topics": ["3.1.6"],
        "skills": ["recall"],
        "summary": "State Le Chatelier's principle.",
        "figures": ["img/2005-june-chm2/fig-q2-curves.jpg"],
        "ms_rows": [
            ("2(b)", "An equilibrium opposes any change (imposed upon it)", "Allow: if a system at equilibrium is disturbed, the equilibrium moves in the direction that tends to reduce the disturbance", "1", "AO1 / 3.1.6")
        ]
    },
    {
        "id": "2005-june-chm2-q2c",
        "question": "2(c)",
        "marks": 4,
        "page": 7,
        "topics": ["3.1.6"],
        "skills": ["analysis", "explanation"],
        "summary": "Identify curve representing higher pressure at same temperature and explain difference from curve A.",
        "figures": ["img/2005-june-chm2/fig-q2-curves.jpg"],
        "ms_rows": [
            ("2(c)", "Curve: B", "1 mark for curve B", "1", "AO3 / 3.1.6"),
            ("", "More ammonia is produced / yield of ammonia increases", "1 mark for higher yield", "1", "AO2 / 3.1.6"),
            ("", "Fewer moles of gas on the right (4 mol goes to 2 mol)", "1 mark for mole comparison", "1", "AO2 / 3.1.6"),
            ("", "Equilibrium shifts to the right to oppose increase in pressure", "1 mark for Le Chatelier explanation", "1", "AO2 / 3.1.6")
        ]
    },
    {
        "id": "2005-june-chm2-q2d",
        "question": "2(d)",
        "marks": 3,
        "page": 7,
        "topics": ["3.1.5", "3.1.6"],
        "skills": ["analysis", "explanation"],
        "summary": "Identify curve when catalyst added under same conditions as A and explain choice.",
        "figures": ["img/2005-june-chm2/fig-q2-curves.jpg"],
        "ms_rows": [
            ("2(d)", "Curve: C", "1 mark for curve C", "1", "AO3 / 3.1.6"),
            ("", "Amount of ammonia / yield / equilibrium position is unchanged", "1 mark for same equilibrium yield", "1", "AO2 / 3.1.6"),
            ("", "Reaction is faster / equilibrium reached sooner / catalyst increases rate equally in both directions", "1 mark for rate reason", "1", "AO2 / 3.1.5")
        ]
    },

    # Q3
    {
        "id": "2005-june-chm2-q3a",
        "question": "3(a)",
        "marks": 3,
        "page": 8,
        "topics": ["3.1.3", "3.2.3"],
        "skills": ["explanation"],
        "summary": "State and explain trend in electronegativity down Group VII from fluorine to iodine.",
        "figures": [],
        "ms_rows": [
            ("3(a)", "Trend: Decreases", "1 mark for trend", "1", "AO1 / 3.2.3"),
            ("", "Increase in shielding / larger atomic radius", "1 mark for shielding or atomic radius", "1", "AO1 / 3.2.3"),
            ("", "Less attraction for bonding / shared pair of electrons", "1 mark for weaker attraction for pair of electrons", "1", "AO1 / 3.1.3")
        ]
    },
    {
        "id": "2005-june-chm2-q3b",
        "question": "3(b)",
        "marks": 2,
        "page": 8,
        "topics": ["3.2.3"],
        "skills": ["observation", "recall"],
        "summary": "Observation and equation when chlorine gas is bubbled into aqueous potassium iodide.",
        "figures": [],
        "ms_rows": [
            ("3(b)", "Observation: Brown solution (or black solid / purple vapour)", "1 mark for observation", "1", "AO1 / 3.2.3"),
            ("", "Equation: Cl2 + 2KI → 2KCl + I2\n(OR Cl2 + 2I– → 2Cl– + I2)", "1 mark for balanced equation", "1", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2005-june-chm2-q3c",
        "question": "3(c)",
        "marks": 4,
        "page": 8,
        "topics": ["3.2.3"],
        "skills": ["recall"],
        "summary": "Identify two sulphur-containing reduction products from H2SO4 with iodide and write half-equations.",
        "figures": [],
        "ms_rows": [
            ("3(c)", "Reduction product 1: SO2", "1 mark for formula or name", "1", "AO1 / 3.2.3"),
            ("", "Half-equation: SO4 2– + 4H+ + 2e– → SO2 + 2H2O", "1 mark for balanced half-equation", "1", "AO1 / 3.2.3"),
            ("", "Reduction product 2: S (or H2S)", "1 mark for sulphur or hydrogen sulphide", "1", "AO1 / 3.2.3"),
            ("", "Half-equation: SO4 2– + 8H+ + 6e– → S + 4H2O\n(or SO4 2– + 10H+ + 8e– → H2S + 4H2O)", "1 mark for balanced half-equation matching product", "1", "AO1 / 3.2.3")
        ]
    },
    {
        "id": "2005-june-chm2-q3d",
        "question": "3(d)",
        "marks": 5,
        "page": 8,
        "topics": ["3.1.7", "3.2.3"],
        "skills": ["recall"],
        "summary": "Equation for chlorine with dilute NaOH, names of chlorine products, and their oxidation states.",
        "figures": [],
        "ms_rows": [
            ("3(d)", "Cl2 + 2NaOH → NaCl + NaOCl + H2O", "1 mark for balanced equation", "1", "AO1 / 3.2.3"),
            ("", "Product 1: Sodium chloride", "1 mark for name", "1", "AO1 / 3.2.3"),
            ("", "Oxidation state: –1", "1 mark for oxidation state", "1", "AO1 / 3.1.7"),
            ("", "Product 2: Sodium chlorate(I) (or sodium hypochlorite / bleach)", "1 mark for name", "1", "AO1 / 3.2.3"),
            ("", "Oxidation state: +1", "1 mark for oxidation state", "1", "AO1 / 3.1.7")
        ]
    },

    # Q4
    {
        "id": "2005-june-chm2-q4a",
        "question": "4(a)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.7"],
        "skills": ["recall"],
        "summary": "Function of a reducing agent in terms of electrons.",
        "figures": [],
        "ms_rows": [
            ("4(a)", "Electron donor / donates electrons / loses electrons", "Insist on donor of electrons", "1", "AO1 / 3.1.7")
        ]
    },
    {
        "id": "2005-june-chm2-q4b",
        "question": "4(b)",
        "marks": 2,
        "page": 9,
        "topics": ["3.1.7", "3.2.2"],
        "skills": ["recall"],
        "summary": "Reducing agent in iron extraction and redox equation for formation of iron from Fe2O3.",
        "figures": [],
        "ms_rows": [
            ("4(b)", "Reducing agent: CO (or C)", "1 mark for carbon monoxide or carbon", "1", "AO1 / 3.2.2"),
            ("", "Equation: 3CO + Fe2O3 → 3CO2 + 2Fe\n(or 3C + 2Fe2O3 → 3CO2 + 4Fe / 3C + Fe2O3 → 3CO + 2Fe)", "1 mark for balanced equation", "1", "AO1 / 3.2.2")
        ]
    },
    {
        "id": "2005-june-chm2-q4c",
        "question": "4(c)",
        "marks": 3,
        "page": 9,
        "topics": ["3.1.7", "3.2.2"],
        "skills": ["recall", "explanation"],
        "summary": "Reducing agent for titanium extraction from TiCl4, condition used and reason.",
        "figures": [],
        "ms_rows": [
            ("4(c)", "Reducing agent: Na (or Mg)", "1 mark for sodium or magnesium", "1", "AO1 / 3.2.2"),
            ("", "Condition: Argon atmosphere / inert atmosphere", "1 mark for argon / inert gas", "1", "AO1 / 3.2.2"),
            ("", "Explanation: Na / Mg / Ti / TiCl4 reacts with air (oxygen / water / nitrogen) forming brittle oxide/nitride impurities", "1 mark for preventing reaction with air/O2/N2/H2O", "1", "AO1 / 3.2.2")
        ]
    },
    {
        "id": "2005-june-chm2-q4di",
        "question": "4(d)(i)",
        "marks": 2,
        "page": 9,
        "topics": ["3.2.2"],
        "skills": ["recall"],
        "summary": "State two essential conditions for electrolytic extraction of aluminium from Al2O3.",
        "figures": [],
        "ms_rows": [
            ("4(d)(i)", "Condition 1: Dissolved in (molten) cryolite / Na3AlF6", "1 mark for cryolite", "1", "AO1 / 3.2.2"),
            ("", "Condition 2: Molten / high temperature (liquid state to allow ions to move)", "1 mark for molten / liquid", "1", "AO1 / 3.2.2")
        ]
    },
    {
        "id": "2005-june-chm2-q4dii",
        "question": "4(d)(ii)",
        "marks": 1,
        "page": 9,
        "topics": ["3.1.7", "3.2.2"],
        "skills": ["recall"],
        "summary": "Equation illustrating formation of aluminium from aluminium ions.",
        "figures": [],
        "ms_rows": [
            ("4(d)(ii)", "Al3+ + 3e– → Al", "Allow multiples", "1", "AO1 / 3.2.2")
        ]
    }
]

def main():
    print("Opening Question Paper PDF...")
    doc_qp = fitz.open(QP_PATH)
    extract_figures(doc_qp)

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Remove existing
    db["questions"] = [q for q in db["questions"] if q.get("paper") != "2005-june-chm2"]

    for qd in QUESTIONS_DATA:
        qid = qd["id"]
        q_label = qd["question"]
        ms_img_rel = f"img/2005-june-chm2/ms_{qid.split('-')[-1]}.jpg"
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel.replace("/", os.sep))

        answers_list = []
        extra_list = []
        spec_ref = qd["ms_rows"][0][4] if qd["ms_rows"] else "AO1 / 3.1"
        for r in qd["ms_rows"]:
            prefix = f"<strong>{r[0]}</strong> " if r[0] else ""
            answers_list.append(f"{prefix}{r[1]} ({r[3]})")
            if r[2]:
                extra_list.append(f"{r[2]}")

        answers_html = "<br>".join(answers_list)
        extra_html = "<br>".join(extra_list) if extra_list else "-"

        render_official_markscheme_image(
            question_label=q_label,
            answers_html=answers_html,
            extra_html=extra_html,
            marks=qd["marks"],
            spec_ref=spec_ref,
            output_path=ms_img_abs
        )

        entry = {
            "id": qid,
            "paper": "2005-june-chm2",
            "question": q_label,
            "marks": qd["marks"],
            "page": qd["page"],
            "topics": qd["topics"],
            "skills": qd["skills"],
            "summary": qd["summary"],
            "image": f"img/2005-june-chm2/q_{qid.split('-')[-1]}.jpg",
            "figures": qd["figures"],
            "markscheme": ms_img_rel,
            "markscheme_text": "\n".join([f"{r[0]} {r[1]} [{r[3]}]".strip() for r in qd["ms_rows"]])
        }
        db["questions"].append(entry)
        print(f"Processed {qid} ({q_label}) - {qd['marks']} marks")

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully ingested {len(QUESTIONS_DATA)} questions for 2005-june-chm2!")

if __name__ == "__main__":
    main()

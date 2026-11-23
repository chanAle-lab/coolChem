import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2008-june-chm1"
MS_DIR = os.path.join(ROOT, "img", PAPER_ID, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2008,
    "series": "June",
    "unit": "CHM1",
    "level": "AS",
    "title": "CHM1 – Atomic Structure, Bonding and Periodicity",
    "date": "2008-06-04",
    "totalMarks": 60,
    "duration": "1 hour",
}

QUESTIONS = [
    # Q1 (11 marks)
    {
        "id": f"{PAPER_ID}-q1a",
        "questionNumber": "1(a)",
        "marks": 1,
        "topics": ["Atomic Structure"],
        "skills": ["Knowledge & Recall"],
        "summary": "Define isotopes in terms of protons and neutrons.",
        "specRef": "3.1.1",
        "ms_label": "1(a)",
        "ms_ans": "(Atoms/isotopes/particles/species with the) same (number of) protons and different (number of) neutrons",
        "ms_extra": "[Not same atomic number/mass number/molecules/element/ions/diff electrons]<br>[allow &lsquo;different versions of the same element with&hellip;&rsquo;]",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1b",
        "questionNumber": "1(b)",
        "marks": 2,
        "topics": ["Atomic Structure", "Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate relative atomic mass of lead from mass spectrum isotopic abundances.",
        "specRef": "3.1.1",
        "ms_label": "1(b)",
        "ms_ans": "<i>A</i><sub>r</sub> = [(204 &times; 1.5) + (206 &times; 23.6) + (207 &times; 21.4) + (208 &times; 53.5)] / 100<br><br>207.3",
        "ms_extra": "[Wrong approach or not dividing by 100 = CE = 0]<br><br>[Answer to 1 d.p.]<br>[Mark conseq on transcription error]",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1ci",
        "questionNumber": "1(c)(i)",
        "marks": 1,
        "topics": ["Amount of Substance"],
        "skills": ["Chemical Equations"],
        "summary": "Balance the overall equation for a lead-acid car battery.",
        "specRef": "3.1.2",
        "ms_label": "1(c)(i)",
        "ms_ans": "PbO<sub>2</sub> + Pb + <b>2</b>H<sub>2</sub>SO<sub>4</sub> &rarr; <b>2</b>PbSO<sub>4</sub> + <b>2</b>H<sub>2</sub>O",
        "ms_extra": "[fractions/multiples]",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q1cii",
        "questionNumber": "1(c)(ii)",
        "marks": 2,
        "topics": ["Atomic Structure"],
        "skills": ["Knowledge & Recall", "Explanation"],
        "summary": "State and explain any chemical difference between 204Pb and 206Pb.",
        "specRef": "3.1.1",
        "ms_label": "1(c)(ii)",
        "ms_ans": "No difference in reaction/chemistry / chemical properties identical/same<br><br>They have same electron arrangement / number of electrons<br>or chemistry determined by electrons / electron arrangement",
        "ms_extra": "[Not &lsquo;similar&rsquo; etc.]<br><br>Tied to M2: [Not just same protons]<br>[allow if near-miss for M2]<br>[accept &lsquo;same protons and electrons&rsquo;]<br>[If M2 = blank or wrong, CE = 0 for M3]",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1d",
        "questionNumber": "1(d)",
        "marks": 2,
        "topics": ["Atomic Structure"],
        "skills": ["Application"],
        "summary": "Deduce the symbol and mass number of an atom from proton and neutron ratios relative to 7Li.",
        "specRef": "3.1.1",
        "ms_label": "1(d)",
        "ms_ans": "<sup>24</sup>Mg<br>&bull; mass number anywhere (1)<br>&bull; element name/symbol (1)",
        "ms_extra": "[If wrong atomic number given, &lsquo;con&rsquo; Mg mark]<br>[Not 24.3 or 24.0]",
        "ms_marks": "1<br>1",
    },
    {
        "id": f"{PAPER_ID}-q1ei",
        "questionNumber": "1(e)(i)",
        "marks": 2,
        "topics": ["Atomic Structure"],
        "skills": ["Knowledge & Recall"],
        "summary": "Explain how gaseous atoms are ionised in a mass spectrometer.",
        "specRef": "3.1.1",
        "ms_label": "1(e)(i)",
        "ms_ans": "High energy/speed electron / electron from electron gun<br><br>Knock off / made to lose (one) e<sup>&minus;</sup> (from the atom) / electron displaced from atom",
        "ms_extra": "[Not just &lsquo;bombarded with electrons&rsquo;]<br><br>Ind<br>[Not equations here]",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q1eii",
        "questionNumber": "1(e)(ii)",
        "marks": 1,
        "topics": ["Atomic Structure"],
        "skills": ["Knowledge & Recall"],
        "summary": "Identify another process in a mass spectrometer that depends on ionisation.",
        "specRef": "3.1.1",
        "ms_label": "1(e)(ii)",
        "ms_ans": "Acceleration",
        "ms_extra": "",
        "ms_marks": "1",
    },
    # Q2 (11 marks)
    {
        "id": f"{PAPER_ID}-q2a",
        "questionNumber": "2(a)",
        "marks": 3,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate moles of H2O2 in solution and moles of O2 produced on decomposition.",
        "specRef": "3.1.2",
        "ms_label": "2(a)",
        "ms_ans": "Moles H<sub>2</sub>O<sub>2</sub> = 150 &times; 10<sup>&minus;3</sup> &times; 2.72<br>= 0.408 / 0.41<br><br>Moles O<sub>2</sub> = 0.408 &divide; 2 = 0.20 &ndash; 0.21 (mol)",
        "ms_extra": "[if &times; 10<sup>&minus;3</sup> missing, lose M1 and M2]<br><br>[mark conseq on error in moles H<sub>2</sub>O<sub>2</sub>]<br>Sig. figs: min 2 s.f. (penalise once in Q2)",
        "ms_marks": "1<br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2bi",
        "questionNumber": "2(b)(i)",
        "marks": 1,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the number of moles of PH3 in 1.43 g.",
        "specRef": "3.1.2",
        "ms_label": "2(b)(i)",
        "ms_ans": "Moles PH<sub>3</sub> = 1.43 &divide; 34.0 = 0.0421 / 0.042 (mol)",
        "ms_extra": "",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2bii",
        "questionNumber": "2(b)(ii)",
        "marks": 1,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the number of moles of oxygen reacted with PH3.",
        "specRef": "3.1.2",
        "ms_label": "2(b)(ii)",
        "ms_ans": "Moles of oxygen reacted = 0.0421 &times; 2 = 0.084 &ndash; 0.0842 (mol)",
        "ms_extra": "[mark conseq on error in moles PH<sub>3</sub>]",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q2biii",
        "questionNumber": "2(b)(iii)",
        "marks": 2,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations"],
        "summary": "Calculate the mass of phosphoric acid formed from 1.43 g of phosphine.",
        "specRef": "3.1.2",
        "ms_label": "2(b)(iii)",
        "ms_ans": "<i>M</i><sub>r</sub> of H<sub>3</sub>PO<sub>4</sub> = 98(.0)<br><br>Mass of H<sub>3</sub>PO<sub>4</sub> = 0.0421 &times; 98(.0) = 4.1 &ndash; 4.13 g",
        "ms_extra": "<br><br>[mark conseq on error in moles PH<sub>3</sub>]",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q2c",
        "questionNumber": "2(c)",
        "marks": 4,
        "topics": ["Amount of Substance"],
        "skills": ["Maths & Calculations", "Knowledge & Recall"],
        "summary": "State the ideal gas equation and calculate the pressure of unreacted oxygen.",
        "specRef": "3.1.2",
        "ms_label": "2(c)",
        "ms_ans": "<i>pV</i> = <i>nRT</i><br><br><i>p</i> = <i>nRT</i> / <i>V</i> = (0.166 &times; 8.31 &times; 300) / (1725 &times; 10<sup>&minus;6</sup>)<br>&bull; volume conversion 1725 &times; 10<sup>&minus;6</sup> (1)<br>&bull; all other numbers correct (1)<br><br>= 239906 Pa / 2.40 &times; 10<sup>5</sup> Pa / 240 kPa",
        "ms_extra": "[accept correctly rearranged formula; letters in wrong case]<br><br>[if number missing, e.g. omitted 300, lose M3 and M4]<br>[If 1725 &times; 10<sup>&minus;3</sup> / 1.725 used AND units = kPa allow all marks]<br>[If units = Pa, treat 1725 &times; 10<sup>&minus;3</sup> / 1.725 as error in volume conversion]<br>[If equation incorrectly rearranged, CE = 0 for M3 and M4 but can still earn M2 for 1725 &times; 10<sup>&minus;6</sup>]",
        "ms_marks": "1<br><br>1<br>1<br><br>1",
    },
    # Q3 (12 marks)
    {
        "id": f"{PAPER_ID}-q3a",
        "questionNumber": "3(a)",
        "marks": 2,
        "topics": ["Atomic Structure"],
        "skills": ["Knowledge & Recall"],
        "summary": "Define the term first ionisation energy of an atom.",
        "specRef": "3.1.1",
        "ms_label": "3(a)",
        "ms_ans": "Energy / enthalpy required/change to remove one electron<br><br>From a gaseous atom",
        "ms_extra": "[Accept &lsquo;enthalpy change for the process M(g) &rarr; M<sup>+</sup>(g) + e<sup>&minus;</sup>&rsquo; for 2 marks]<br>[allow &lsquo;gaseous&rsquo; from equation]<br>&ldquo;Enthalpy change when one mole of gaseous atoms forms one mole of (gaseous) unipositive ions.&rdquo; scores 2 marks",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3b",
        "questionNumber": "3(b)",
        "marks": 2,
        "topics": ["Atomic Structure", "Periodicity"],
        "skills": ["Explanation"],
        "summary": "Explain the general increase in first ionisation energies across Period 3 (Na to Ar).",
        "specRef": "3.1.1",
        "ms_label": "3(b)",
        "ms_ans": "Increase in number of protons / nuclear charge<br><br>Decrease in size / same shielding / same shells / similar shielding / increased attraction between nucleus and outer electrons",
        "ms_extra": "",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3c",
        "questionNumber": "3(c)",
        "marks": 3,
        "topics": ["Atomic Structure", "Periodicity"],
        "skills": ["Explanation"],
        "summary": "State and explain how the first ionisation energy of sulphur deviates from the Period 3 trend.",
        "specRef": "3.1.1",
        "ms_label": "3(c)",
        "ms_ans": "S has a lower than expected 1st IE value / is low / &lt; P / decreases<br><br>e<sup>&minus;</sup> pair in 3p (sub-level)<br><br>(Easier to remove e<sup>&minus;</sup> due to) repulsion between these paired e<sup>&minus;</sup> (wtte)",
        "ms_extra": "[if IE said to be higher, CE = 0 for M3 but allow M2]<br><br>[allow following error in 3p orbital &ndash; e.g. 2p]<br>QoL: [not just diagram/electron arrangement]",
        "ms_marks": "1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3di",
        "questionNumber": "3(d)(i)",
        "marks": 2,
        "topics": ["Bonding"],
        "skills": ["Structure & Bonding"],
        "summary": "Draw the shapes of BF3 and H2S molecules showing any lone pairs.",
        "specRef": "3.1.3",
        "ms_label": "3(d)(i)",
        "ms_ans": "BF<sub>3</sub> shown as trigonal planar with no lone pairs<br><br>H<sub>2</sub>S shown as bent / V shaped with 2 lone pairs",
        "ms_extra": "Ignore errors in dots-and-wedges as long as shape is right; Not &lsquo;T&rsquo; shape / pyramidal; Not dot-and-cross; Allow : for bond.<br><br>Not S=H; Not empty orbital envelopes; Allow two dots without envelope.",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3dii",
        "questionNumber": "3(d)(ii)",
        "marks": 2,
        "topics": ["Bonding"],
        "skills": ["Explanation"],
        "summary": "Explain why a BF3 molecule has a trigonal planar shape.",
        "specRef": "3.1.3",
        "ms_label": "3(d)(ii)",
        "ms_ans": "(Because there are 3) bonding pairs / electron pairs<br><br>with equal repulsion between them",
        "ms_extra": "[&lsquo;T&rsquo; shape/pyramidal &ndash; allow M3 but not M4]<br>[allow &lsquo;equal repulsion between three bonds&rsquo; for M4 but don&rsquo;t award M3]<br>[M4 only available if correct diagram given; not &lsquo;equal repulsion between atoms&rsquo;]<br>[If NOT just 3 bonding pairs (e.g. shows a lone pair), CE = 0 for M3 and M4]",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q3e",
        "questionNumber": "3(e)",
        "marks": 1,
        "topics": ["Bonding"],
        "skills": ["Application"],
        "summary": "Predict the H-S-H bond angle in the H2S-BF3 adduct (compound A).",
        "specRef": "3.1.3",
        "ms_label": "3(e)",
        "ms_ans": "H-S-H bond angle = 107.5 down to 95&deg;",
        "ms_extra": "",
        "ms_marks": "1",
    },
    # Q4 (11 marks)
    {
        "id": f"{PAPER_ID}-q4a",
        "questionNumber": "4(a)",
        "marks": 4,
        "topics": ["Periodicity"],
        "skills": ["Explanation"],
        "summary": "State and explain whether a sodium atom or a chlorine atom has a larger atomic radius.",
        "specRef": "3.1.4",
        "ms_label": "4(a)",
        "ms_ans": "Na larger than Cl<br><br>Na has fewer protons / lower nuclear charge than Cl<br><br>Both Na and Cl have the same shielding / shells / similar shielding<br><br>Weaker attraction between nucleus and electrons of Na",
        "ms_extra": "[allow contra argument; allow correct trend across the Period]<br><br>Ind<br><br>Ind<br><br>Tied to M1 [allow contra arguments]",
        "ms_marks": "1<br><br>1<br><br>1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4bi",
        "questionNumber": "4(b)(i)",
        "marks": 1,
        "topics": ["Atomic Structure"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give the electron arrangement of a sodium atom.",
        "specRef": "3.1.1",
        "ms_label": "4(b)(i)",
        "ms_ans": "1s<sup>2</sup>2s<sup>2</sup>2p<sup>6</sup>3s<sup>1</sup>",
        "ms_extra": "[accept caps and subscripted numbers]<br>(Not [Ne] 3s<sup>1</sup>)",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4bii",
        "questionNumber": "4(b)(ii)",
        "marks": 2,
        "topics": ["Atomic Structure", "Periodicity"],
        "skills": ["Explanation"],
        "summary": "State and explain whether a sodium atom or Na+ ion has a larger radius.",
        "specRef": "3.1.4",
        "ms_label": "4(b)(ii)",
        "ms_ans": "Na / sodium (atom) (larger than Na<sup>+</sup> / sodium ion)<br><br>Ion has one less shell / energy level than atom",
        "ms_extra": "<br>Tied: [accept correct references to 2p and 3s sub-levels]<br>[Not &lsquo;less electrons, so more attraction&rsquo;]",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4biii",
        "questionNumber": "4(b)(iii)",
        "marks": 2,
        "topics": ["Atomic Structure", "Periodicity"],
        "skills": ["Explanation"],
        "summary": "Suggest why a chloride ion (Cl-) has a larger radius than a chlorine atom.",
        "specRef": "3.1.4",
        "ms_label": "4(b)(iii)",
        "ms_ans": "1s<sup>2</sup>2s<sup>2</sup>2p<sup>6</sup>3s<sup>2</sup>3p<sup>5</sup> &rarr; 1s<sup>2</sup>2s<sup>2</sup>2p<sup>6</sup>3s<sup>2</sup>3p<sup>6</sup> / ion has more electrons / fills its outer shell<br><br>Ion has more e<sup>&minus;</sup>&ndash;e<sup>&minus;</sup> repulsion",
        "ms_extra": "[Accept argument that this is not a fair comparison as: Cl value is &frac12; covalent radius (1); Cl<sup>&minus;</sup> value is determined from lattice measurements (1)]",
        "ms_marks": "1<br><br>1",
    },
    {
        "id": f"{PAPER_ID}-q4ci",
        "questionNumber": "4(c)(i)",
        "marks": 1,
        "topics": ["Group 2"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give the formula of the least soluble Group 2 sulphate (Mg to Ba).",
        "specRef": "3.2.2",
        "ms_label": "4(c)(i)",
        "ms_ans": "Least soluble sulphate = BaSO<sub>4</sub>",
        "ms_extra": "not name only<br>[Allow, for 1 mark across (c)(i)-(ii), correct identification of Ba/barium in both; RaSO<sub>4</sub> penalised, Ra(OH)<sub>2</sub> allowed as RE]",
        "ms_marks": "1",
    },
    {
        "id": f"{PAPER_ID}-q4cii",
        "questionNumber": "4(c)(ii)",
        "marks": 1,
        "topics": ["Group 2"],
        "skills": ["Knowledge & Recall"],
        "summary": "Give the formula of the most soluble Group 2 hydroxide (Mg to Ba).",
        "specRef": "3.2.2",
        "ms_label": "4(c)(ii)",
        "ms_ans": "Most soluble hydroxide = Ba(OH)<sub>2</sub>",
        "ms_extra": "not name only",
        "ms_marks": "1",
    },
]


def main():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Upsert paper
    papers = [p for p in db["papers"] if p["id"] != PAPER_ID]
    papers.append(PAPER_OBJ)
    db["papers"] = papers

    # Remove existing questions for this paper
    questions = [q for q in db["questions"] if q.get("paper") != PAPER_ID]

    for q in QUESTIONS:
        q_slug = q["id"].split("-")[-1]
        ms_rel = f"img/{PAPER_ID}/ms/{q_slug}.png"
        ms_abs = os.path.join(ROOT, ms_rel)
        render_official_markscheme_image(
            question_label=q["ms_label"],
            answers_html=q["ms_ans"],
            extra_html=q["ms_extra"],
            marks=q["ms_marks"],
            spec_ref=q["specRef"],
            output_path=ms_abs,
        )
        questions.append({
            "id": q["id"],
            "paper": PAPER_ID,
            "year": PAPER_OBJ["year"],
            "series": PAPER_OBJ["series"],
            "unit": PAPER_OBJ["unit"],
            "level": PAPER_OBJ["level"],
            "questionNumber": q["questionNumber"],
            "marks": q["marks"],
            "topics": q["topics"],
            "skills": q["skills"],
            "summary": q["summary"],
            "specRef": q["specRef"],
            "image": f"img/{PAPER_ID}/{q_slug}.jpg",
            "markscheme": ms_rel,
            "figures": [],
        })

    db["questions"] = questions
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    total_m = sum(q["marks"] for q in QUESTIONS)
    print(f"Ingested {PAPER_ID}: {len(QUESTIONS)} questions, {total_m} marks.")


if __name__ == "__main__":
    main()

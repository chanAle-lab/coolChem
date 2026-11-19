"""
Convert 2002-jan-chm1 markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-jan-chm1-q1a": {
        "answers": "number of protons in one atom (or nucleus) (1)",
        "extra": "allow protons & electrons<br>do <b>not</b> allow protons + electrons or electrons",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1b": {
        "answers": "• Mass number: 23 (1)<br>• Atomic number: 11 (1)<br>(Symbol: <sup>23</sup><sub>11</sub>Na)",
        "extra": "or Na + unambiguous statement of mass no. & at. no.",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1c": {
        "answers": "1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>1</sup> (1)",
        "extra": "allow [Ne] 3s<sup>2</sup> 3p<sup>1</sup>",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1d": {
        "answers": "14 (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1e": {
        "answers": "(average mass of an atom (or isotope) / mass of 1 atom of <sup>12</sup>C) &times; 12 (2 marks)",
        "extra": "or stated in moles<br>or compared with 1/12th of a <sup>12</sup>C atom<br>or relative to <sup>12</sup>C taken as 12<br>reference to mass number (not mass) CE = 0",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1fi": {
        "answers": "electron gun (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1fii": {
        "answers": "(particles must be charged / ions) before attraction to a charged plate (or electric field) (1)",
        "extra": "or only ions can be attracted / accelerated by an electric field<br>or converse: if not charged, not attracted to electric field",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1fiii": {
        "answers": "magnetic field (or magnet) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1fiv": {
        "answers": "magnetic field (or accelerating potential / strength of magnet / allow magnet) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1gi": {
        "answers": "• (24.0 &times; 64.2 + 25.0 &times; 20.3 + 26.0 &times; 15.5) / 100 (1)<br>• = 24.5 (1)",
        "extra": "allow 24.5 to 24.52<br>ignore units<br>if numerator is correct but 100 has AE, conseq AE-1<br>if AE on 100, allow conseq correct answer provided numerator is correct",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1gii": {
        "answers": "magnesium (or Mg) (1)",
        "extra": "allow conseq on wrong A<sub>r</sub>",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q1giii": {
        "answers": "abundance of isotopes is different (1)",
        "extra": "or different isotopes present in meteorite vs terrestrial sample",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q2ai": {
        "answers": "Negative signs (−) marked on the four chloride ion positions alternating with the positive ion (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q2aii": {
        "answers": "vibrate faster (or with bigger amplitude / vibrate more) (1)",
        "extra": "<b>not</b> start to vibrate<br>or other type of motion esp. translation<br>ignore rotation",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q2bi": {
        "answers": "Na + &frac12;Cl<sub>2</sub> &rarr; NaCl (or 2Na + Cl<sub>2</sub> &rarr; 2NaCl) (1)",
        "extra": "allow Na<sup>+</sup>Cl<sup>−</sup><br>ignore state symbols even if wrong",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q2bii": {
        "answers": "from sodium (or sodium atom / sodium metal) (1)",
        "extra": "allow from sodium ion",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q2ci": {
        "answers": "not spherical / distorted / charge uneven (or diagram showing distorted electron cloud) (1)",
        "extra": "do <b>not</b> allow if describe Cl<sup>−</sup> in a polarised covalent compound",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q2cii": {
        "answers": "high charge / size ratio (or high charge density / high charge / small size) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q2di": {
        "answers": "shared (1) electron pair (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q2dii": {
        "answers": "difference in electronegativity (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q3ai": {
        "answers": "• 3 (bonding) pairs of electrons (allow 3 bonds) (1)<br>• repel equally (or as much as possible / get as far apart as possible) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q3aii": {
        "answers": "• Predicted bond angle: 118° (allow 117–119°) (1)<br>• Explanation: lone pair (1)<br>• repels more than bonding pair (1)",
        "extra": "allow explanation if angle < 118°<br>CE = 0 if angle &ge; 120°",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q3b": {
        "answers": "• Name: tetrahedral (1)<br>• Example: CH<sub>4</sub> (1)",
        "extra": "allow correct ion e.g. NH<sub>4</sub><sup>+</sup>, SO<sub>4</sub><sup>2−</sup>",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q3ci": {
        "answers": "90° (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q3cii": {
        "answers": "• lone pairs (or they) repel more than bonding pairs (or repel most) (1)<br>• (so are) as far apart as possible (1)",
        "extra": "mark independently",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q3ciii": {
        "answers": "square planar (allow square) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q3d": {
        "answers": "• 3 bonds and 1 lone pair shown on nitrogen (1)<br>• correct 3D pyramidal shape drawn (e.g. wedges / dashed bonds) (1)",
        "extra": "only give second mark if first mark also given<br>penalise sticks (i.e. N−) once but N must be shown",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q4a": {
        "answers": "• {ability / power} (of an atom) to attract {electron density / electrons / negative charge} (1)<br>• in a covalent bond (or shared pair) (1)",
        "extra": "if 'remove an electron' lose first mark",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q4b": {
        "answers": "• Trend: increases (1)<br>• Explanation: nuclear charge (number of protons) increases (1)<br>• electrons in same shell / similar shielding / smaller atomic radius (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.3, 3.2.1"
    },
    "2002-jan-chm1-q4c": {
        "answers": "• {enthalpy / energy} for removal of one electron (or 1 mol of e<sup>−</sup>) (1)<br>• from a gaseous atom (or 1 mol of gaseous atoms) (1)<br>(Equation: X(g) &rarr; X<sup>+</sup>(g) + e<sup>−</sup> scores both marks)",
        "extra": "must have first mark to score second mark",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q4di": {
        "answers": "2 (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q4dii": {
        "answers": "Two elements (or Na and Mg) before the drop (in energy) to Al (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q4diii": {
        "answers": "ionisation energy of Al &lt; that for Mg (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q4div": {
        "answers": "• fall in energy from P to S (or discontinuity in trend) (1)<br>• from Al to P there are 3 additional electrons (or 3 elements) (1)",
        "extra": "for second mark: idea of block of 3 elements",
        "mark": 2,
        "spec": "3.1.1"
    },
    "2002-jan-chm1-q5ai": {
        "answers": "• positive ions (1)<br>• (attract) delocalised electrons (or sea of / free / mobile electrons) (1)",
        "extra": "confusion with −ve ions or ionic lattice CE = 0",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q5aii": {
        "answers": "• more protons (or Mg<sup>2+</sup> has higher charge than Na<sup>+</sup>) (1)<br>• attracts delocalised (or bonding) electrons more strongly (or attracts positive ions more / more delocalised electrons) (1)",
        "extra": "can be brought forward from (a)(i)<br>'metallic bonding stronger' scores 1 mark (only given if no other marks awarded)",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q5b": {
        "answers": "• macromolecular (or giant molecule / giant covalent lattice) (1)<br>• covalent (1)<br>• strong covalent bonds (or bonds require much energy to break) (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q5c": {
        "answers": "delocalised electrons (or free / mobile / sea of electrons) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-jan-chm1-q5d": {
        "answers": "• planes (or layers) of atoms / carbon rings (1)<br>• weak forces (or van der Waals' forces / weak bonds) between planes (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    }
}

def main():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    updated_count = 0
    for q in db["questions"]:
        qid = q.get("id")
        if qid in MS_DATA:
            data = MS_DATA[qid]
            q_num = q.get("question", "")
            img_rel = q.get("markscheme", f"img/2002-jan-chm1/ms_{qid.split('-')[-1]}.jpg")
            img_path = os.path.join(SCRATCH_DIR, img_rel.replace("/", os.sep))
            
            print(f"Generating MS for {qid} ({q_num}) -> {img_path}")
            render_official_markscheme_image(
                question_label=q_num,
                answers_html=data["answers"],
                extra_html=data["extra"],
                marks=data["mark"],
                spec_ref=data["spec"],
                output_path=img_path
            )
            
            clean_ans = data["answers"].replace("<br>", "\n").replace("&rarr;", "->").replace("&frac12;", "1/2").replace("•", "-")
            clean_ext = data["extra"].replace("<br>", "\n")
            q["markscheme_text"] = f"{clean_ans}\n\n[Extra Information]:\n{clean_ext}" if clean_ext else clean_ans
            updated_count += 1

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {updated_count} questions for 2002-jan-chm1!")

if __name__ == "__main__":
    main()

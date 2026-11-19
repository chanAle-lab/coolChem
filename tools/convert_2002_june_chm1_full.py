"""
Convert 2002-june-chm1 markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-june-chm1-q1a": {
        "answers": "• L = mass of 1 mol / mass of 1 atom = 1.0078 / (1.6734 &times; 10<sup>&minus;24</sup>) (1)<br>• = 6.0225 &times; 10<sup>23</sup> (1)",
        "extra": "must show working<br>ignore wrong units<br>answer only scores 1 mark",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2002-june-chm1-q1b": {
        "answers": "equal (or same / 1 : 1) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2002-june-chm1-q1c": {
        "answers": "• PV = nRT &rArr; n = PV / RT (1)<br>• n = (98000 &times; 0.0352) / (8.31 &times; 298) (1)<br>• n = 1.39 (mol) (1)",
        "extra": "allow 1.390 to 1.395<br>ignore units even if incorrect<br>answer = 1.4 loses last mark",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2002-june-chm1-q1d": {
        "answers": "• Concentration = (0.732 &times; 1000) / 250 = 2.93 (1)<br>• Units: mol dm<sup>&minus;3</sup> (or M / mol/dm<sup>3</sup> / mol l<sup>&minus;1</sup>) (1)",
        "extra": "allow 2.928 to 2.93<br>unit mark tied to correct answer, but allow unit mark only if answer = 2.9 or 3",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2002-june-chm1-q1ei": {
        "answers": "• moles H<sub>2</sub>SO<sub>4</sub> = (25.0 / 1000) &times; 1.24 = 0.0310 (1)<br>• moles NH<sub>3</sub> in 30.8 cm<sup>3</sup> = 0.0310 &times; 2 = 0.0620 (1)<br>• moles NH<sub>3</sub> in 1 dm<sup>3</sup> = (0.0620 &times; 1000) / 30.8 = 2.01 (mol dm<sup>&minus;3</sup>) (1)",
        "extra": "allow 2.010 to 2.015<br>mark 2 is for &times; 2; CE if &times; 2 not used<br>if use m<sub>1</sub>v<sub>1</sub> = m<sub>2</sub>v<sub>2</sub>, scores 3 if ans correct else zero<br>'no units' OK, wrong units lose last mark",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2002-june-chm1-q1eii": {
        "answers": "• moles (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub> = moles H<sub>2</sub>SO<sub>4</sub> = 0.0310 (1)<br>• M<sub>r</sub>((NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub>) = 132.1 (allow 132) (1)<br>• mass = 0.0310 &times; 132.1 = 4.10 g (1)",
        "extra": "allow 4.09 to 4.11<br>allow conseq on wrong moles in part 1 if clear H<sub>2</sub>SO<sub>4</sub> = (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub><br>wrong formula for (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub> CE = 0<br>if moles of (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub> not clear CE<br>wrong units loses mark",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2002-june-chm1-q1f": {
        "answers": "Mg<sub>3</sub>N<sub>2</sub> + 6H<sub>2</sub>O &rarr; 3Mg(OH)<sub>2</sub> + 2NH<sub>3</sub><br>• Correct formulae (1)<br>• Balanced equation (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2002-june-chm1-q2ai": {
        "answers": "covalent (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q2aii": {
        "answers": "co-ordinate (or dative) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q2aiii": {
        "answers": "both electrons (or electron pair) come from nitrogen (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q2aiv": {
        "answers": "• 4 (bonding) electron pairs (1)<br>• repel equally / are identical (1)<br>• as far apart as possible / to position of minimum repulsion (1)<br>• tetrahedron (1)",
        "extra": "",
        "mark": 4,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q2b": {
        "answers": "• power (ability) of an atom / element to attract electron density / electrons / electron pair (1)<br>• in a covalent bond (1)",
        "extra": "allow attract from / withdraw in / withdraw from<br>do not allow remove from",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q2ci": {
        "answers": "electron-deficient / small (slight / partial) positive charge (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q2cii": {
        "answers": "H &lt; N (hydrogen has lower electronegativity than nitrogen) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3a": {
        "answers": "• van der Waals' forces (or London / dispersion / temporary dipole forces) (1)<br>• dipole&minus;dipole forces (1)<br>• hydrogen bonding (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3bi": {
        "answers": "• covalent between atoms (or within a molecule) (1)<br>• van der Waals' between molecules (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3bii": {
        "answers": "molecular (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3biii": {
        "answers": "forces (or bonds / v.d.W. forces / intermolecular forces) between molecules must be broken / loosened (1)",
        "extra": "mention of ions CE = 0",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3ci": {
        "answers": "• hydrogen bonding in HF (1)<br>• dipole&minus;dipole forces (or v.d.W.) in HCl (1)<br>• hydrogen bonding is stronger than dipole&minus;dipole forces (or H-bonding is strongest intermolecular force) (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3cii": {
        "answers": "• HI is a bigger molecule than HCl (or heavier / has more electrons / more electron shells / larger M<sub>r</sub> / more polarisable) (1)<br>• Therefore the (van der Waals') forces between HI molecules are stronger (1)",
        "extra": "Q of L mark (look for unambiguous statement using correct terminology)",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3di": {
        "answers": "• ionic (1)<br>• strong forces between ions / lots of energy required to break ionic bonds (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3dii": {
        "answers": "all bonds must be broken (1)",
        "extra": "mention of molecules etc. CE = 0",
        "mark": 1,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q3e": {
        "answers": "• macromolecular (or giant molecule / giant covalent lattice) (1)<br>• strong covalent bonds / lots of energy required to break bonds (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-june-chm1-q4a": {
        "answers": "• Trend: increases (1)<br>• Reason: more electron shells (or more shells / subshells / energy levels) (1)",
        "extra": "wrong trend CE = 0 and in (b)",
        "mark": 2,
        "spec": "3.2.2"
    },
    "2002-june-chm1-q4b": {
        "answers": "• Trend: decreases (1)<br>• Explanation: metallic bonds weaker / weaker attraction between positive ions and delocalised electrons (or nuclei) (1)<br>• atoms (or ions) are larger (1)",
        "extra": "third mark only scored if previous mark given<br>CE if mention molecules, intermolecular forces, ionic bonding",
        "mark": 3,
        "spec": "3.2.2"
    },
    "2002-june-chm1-q4c": {
        "answers": "• Trend: increases (1)<br>• Equation for Mg: Mg + H<sub>2</sub>O &rarr; MgO + H<sub>2</sub> (1)<br>• Equation for Sr: Sr + 2H<sub>2</sub>O &rarr; Sr(OH)<sub>2</sub> + H<sub>2</sub> (1)",
        "extra": "ignore state symbols",
        "mark": 3,
        "spec": "3.2.2"
    },
    "2002-june-chm1-q4d": {
        "answers": "• Formula: BaSO<sub>4</sub> (1)<br>• Use: test for sulphate ions (or pigment / for X-rays / barium meal / paint) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.2"
    },
    "2002-june-chm1-q4e": {
        "answers": "• Identity of M: Be (allow Be<sup>2+</sup>) (1)<br>• Equation 1: Be<sup>2+</sup> + 2OH<sup>&minus;</sup> &rarr; Be(OH)<sub>2</sub> (1)<br>&nbsp;&nbsp;(allow + 2NaOH &rarr; ... + 2Na<sup>+</sup>)<br>• Equation 2: Be(OH)<sub>2</sub> + 2OH<sup>&minus;</sup> &rarr; [Be(OH)<sub>4</sub>]<sup>2&minus;</sup> (1)<br>&nbsp;&nbsp;(allow + 2NaOH &rarr; ... + 2Na<sup>+</sup>)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.2"
    },
    "2002-june-chm1-q4f": {
        "answers": "• Be<sup>2+</sup> ion has high charge / size ratio (or high charge density / Be<sup>2+</sup> is very small) (1)<br>• polarises chloride ion (Cl<sup>&minus;</sup>) (1)<br>• causes covalency / sharing of electrons (1)",
        "extra": "penalise Be; do not allow if BeCl<sub>2</sub> ionic<br>can score mark 2 from diagram",
        "mark": 3,
        "spec": "3.2.2"
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
            img_rel = q.get("markscheme", f"img/2002-june-chm1/ms_{qid.split('-')[-1]}.jpg")
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

    print(f"Successfully updated {updated_count} questions for 2002-june-chm1!")

if __name__ == "__main__":
    main()

"""
Convert 2001-june-chm3w markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

# Data dictionary for 2001-june-chm3w
MS_DATA = {
    "2001-june-chm3w-q1ai": {
        "answers": "• Isomer 3: CH<sub>3</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>Br (or (CH<sub>3</sub>)<sub>2</sub>CHCH<sub>2</sub>Br) (1)<br>• Isomer 4: CH<sub>3</sub>CH<sub>2</sub>CH(Br)CH<sub>3</sub> (1)",
        "extra": "if 'B' used in place of 'Br', allow M2",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2001-june-chm3w-q1aii": {
        "answers": "2-bromo(-2-)methylpropane (1)",
        "extra": "allow (2-)methyl-2-bromopropane",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2001-june-chm3w-q1bi": {
        "answers": "• Structural formula: CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CN (1)<br>• Name: Pentanenitrile (1)",
        "extra": "formula: <b>not</b> C<sub>4</sub>H<sub>9</sub>CN<br>name: allow pentanonitrile, ignore numbers",
        "mark": 2,
        "spec": "3.3.3"
    },
    "2001-june-chm3w-q1bii": {
        "answers": "• Name: Nucleophilic substitution (1)<br>• Mechanism (2 marks):<br>&nbsp;&nbsp;M1: curly arrow from C–Br bond to Br (or C–Br dipole C<sup>δ+</sup>–Br<sup>δ−</sup>) (1)<br>&nbsp;&nbsp;M2: curly arrow from lone pair on :CN<sup>−</sup> to C (1)",
        "extra": "S<sub>N</sub>1 mechanism:<br>M1: formation of carbocation including C–Br<br>M2: attack by :CN<sup>−</sup><br>allow mechanism showing 'Cl'<br>if + on C lose M1, if δ− on C and δ+ on Br lose M1<br>if K–CN shown lose M2",
        "mark": 3,
        "spec": "3.3.3"
    },
    "2001-june-chm3w-q1biii": {
        "answers": "C–F bond is strong(er) (than C–Br bond) (1)",
        "extra": "must imply C–F is stronger than C–Br bond<br>ignore references to electronegativity, bond polarity etc.",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2001-june-chm3w-q1ci": {
        "answers": "Idea of 'splitting by water' or reaction with water (in which OH bonds are broken) (1)",
        "extra": "allow adding water to break bond<br><b>not</b> addition of water",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2001-june-chm3w-q1cii": {
        "answers": "Heat (under reflux) or hot or warm or high temperature (1)",
        "extra": "<b>not</b> T > 100 °C<br>penalise any catalyst, high pressure but ignore 'acid catalyst'<br>if list, wrong answer cancels correct one",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2001-june-chm3w-q1ciii": {
        "answers": "CH<sub>3</sub>CH<sub>2</sub>COOH or propanoic acid (1)",
        "extra": "allow C<sub>2</sub>H<sub>5</sub>COOH, CH<sub>3</sub>CH<sub>2</sub>CO<sub>2</sub>H, C<sub>2</sub>H<sub>5</sub>CO<sub>2</sub>H<br>or propanamide, CH<sub>3</sub>CH<sub>2</sub>CONH<sub>2</sub>, C<sub>2</sub>H<sub>5</sub>CONH<sub>2</sub>",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2001-june-chm3w-q2ai": {
        "answers": "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH + [O] &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CHO + H<sub>2</sub>O<br>• Product: CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>CHO (1)<br>• Balance: + [O] &rarr; ... + H<sub>2</sub>O (1)",
        "extra": "allow C<sub>4</sub>H<sub>9</sub>CH<sub>2</sub>OH or C<sub>5</sub>H<sub>11</sub>OH for reactant<br>product must show aldehyde group e.g. C<sub>4</sub>H<sub>9</sub>CHO<br>if ketone shown here, allow balance mark<br>if wrong alcohol used, allow balance mark",
        "mark": 2,
        "spec": "3.3.5, 3.3.8"
    },
    "2001-june-chm3w-q2aii": {
        "answers": "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH(OH)CH<sub>3</sub> + [O] &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COCH<sub>3</sub> + H<sub>2</sub>O<br>• Product: CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COCH<sub>3</sub> (1)<br>• Balance: + [O] &rarr; ... + H<sub>2</sub>O (1)",
        "extra": "allow C<sub>3</sub>H<sub>7</sub>CH(OH)CH<sub>3</sub> or C<sub>5</sub>H<sub>11</sub>OH for reactant<br>product must show C=O in ketone e.g. C<sub>3</sub>H<sub>7</sub>COCH<sub>3</sub><br>if aldehyde shown here, allow balance mark<br>if wrong alcohol used, allow balance mark",
        "mark": 2,
        "spec": "3.3.5, 3.3.8"
    },
    "2001-june-chm3w-q2b": {
        "answers": "<b>Any one test from:</b><br><br><b>Option 1: Fehling's solution</b><br>• Reagent: Fehling's solution (1)<br>• Conditions: boil / heat / warm (1)<br>• Observation (a)(i): orange or brown or red precipitate / solid (1)<br>• Observation (a)(ii): no precipitate / no reaction (1)<br><br><b>Option 2: Tollens' reagent</b><br>• Reagent: Tollens' reagent (ammoniacal silver nitrate) (1)<br>• Conditions: boil / heat / warm (1)<br>• Observation (a)(i): silver mirror / grey or black precipitate (1)<br>• Observation (a)(ii): no silver mirror / no reaction (1)<br><br><b>Option 3: Acidified potassium dichromate</b><br>• Reagent: potassium dichromate (1)<br>• Conditions: acidified (1)<br>• Observation (a)(i): (orange) turns green or blue (1)<br>• Observation (a)(ii): no colour change / no reaction (1)",
        "extra": "conditions tied to reagent<br>observation tied to reagent<br><b>not</b> 'nothing'<br>if no reagent or wrong reagent quoted, mark as CE<br>any appropriate reagent e.g. Benedict's, but if Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> or [Ag(NH<sub>3</sub>)<sub>2</sub>]<sup>+</sup> or MnO<sub>4</sub><sup>−</sup> given without cation, do <b>not</b> allow reagent mark",
        "mark": 4,
        "spec": "3.3.8"
    },
    "2001-june-chm3w-q3a": {
        "answers": "• Catalyst: (conc) phosphoric acid OR (conc) sulphuric acid (1)<br>• Conditions (2 marks):<br>&nbsp;&nbsp;Temp = High or 200–500 °C (1)<br>&nbsp;&nbsp;Pressure = High or 5–20 MPa / 50–200 atm (1)<br>&nbsp;&nbsp;(for H<sub>2</sub>SO<sub>4</sub>: 50–100 °C, 2–4 MPa / 20–40 atm)<br>• Equation: CH<sub>2</sub>=CH<sub>2</sub> + H<sub>2</sub>O &rarr; CH<sub>3</sub>CH<sub>2</sub>OH (1)",
        "extra": "catalyst: accept correct formula, <b>not</b> dilute<br>if no or wrong catalyst given, allow phosphoric acid conditions<br>equation: allow C<sub>2</sub>H<sub>4</sub>, allow C<sub>2</sub>H<sub>5</sub>OH, <b>not</b> CH<sub>2</sub>CH<sub>2</sub>",
        "mark": 4,
        "spec": "3.3.4, 3.3.5"
    },
    "2001-june-chm3w-q3bi": {
        "answers": "• Catalyst: Silver or Ag (1)<br>• Equation: CH<sub>2</sub>=CH<sub>2</sub> + &frac12;O<sub>2</sub> &rarr; C<sub>2</sub>H<sub>4</sub>O (oxirane / epoxyethane) (1)",
        "extra": "accept doubled equation<br>allow C<sub>2</sub>H<sub>4</sub>, <b>not</b> [O], allow (CH<sub>2</sub>CH<sub>2</sub>)O",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2001-june-chm3w-q3bii": {
        "answers": "• Name: Epoxyethane or ethylene oxide (1)<br>• Explanation: (3-membered) ring or molecule (very) strained or 60° bond angle (making molecule highly reactive) (1)",
        "extra": "explanation: <b>not</b> 'stressed'",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2001-june-chm3w-q3biii": {
        "answers": "antifreeze or polyesters (1)",
        "extra": "<b>not</b> de-icers, plastics, polymers, surfactants",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2001-june-chm3w-q4ai": {
        "answers": "• Initiation: Cl<sub>2</sub> &rarr; 2 Cl• (1)<br>• Propagation 1: CH<sub>4</sub> + Cl• &rarr; CH<sub>3</sub>• + HCl (1)<br>• Propagation 2: CH<sub>3</sub>• + Cl<sub>2</sub> &rarr; CH<sub>3</sub>Cl + Cl• (1)",
        "extra": "equations must be balanced<br>missing dots '•': penalise once<br>dot can be anywhere on species<br>if written explanation given, must be as clear and detailed as equations<br>allow termination step: Cl• + Cl• &rarr; Cl<sub>2</sub>, CH<sub>3</sub>• + CH<sub>3</sub>• &rarr; C<sub>2</sub>H<sub>6</sub>, or CH<sub>3</sub>• + Cl• &rarr; CH<sub>3</sub>Cl<br>chlorine atoms or chlorine radicals, <b>not</b> just 'radicals'",
        "mark": 3,
        "spec": "3.3.2"
    },
    "2001-june-chm3w-q4aii": {
        "answers": "Initiation (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2001-june-chm3w-q4aiii": {
        "answers": "• Suggestion: Use excess methane or limit the amount of Cl<sub>2</sub> (1)<br>• Reason (2 marks):<br>&nbsp;&nbsp;Idea of to minimise multiple substitutions (1)<br>&nbsp;&nbsp;OR to minimise / prevent further reaction or substitution (of CH<sub>3</sub>Cl) / more chance of Cl• colliding with CH<sub>4</sub> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.3.2"
    },
    "2001-june-chm3w-q4bi": {
        "answers": "• Idea that but-2-ene has different substituents / groups / atoms on each carbon of C=C (1)<br>• Idea that but-1-ene has 2 H atoms (or same atoms/groups) on one carbon of C=C (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2001-june-chm3w-q4bii": {
        "answers": "• Any correct structure for 1-bromobut-1-ene (1)<br>• Both correct cis/trans (Z/E) isomers drawn: (Z)-1-bromobut-1-ene and (E)-1-bromobut-1-ene (1)",
        "extra": "consequential: allow M2 if wrong bromoalkene used",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2001-june-chm3w-q5a": {
        "answers": "• C = 87.8 / 12 = 7.32 and H = 12.2 / 1 = 12.2 (1)<br>• Ratio C : H = 3 : 5 (or 1 : 1.67) &rArr; empirical formula C<sub>3</sub>H<sub>5</sub> (1)<br>• Molecular mass of empirical formula = 41; 82 / 41 = 2 &rArr; molecular formula C<sub>6</sub>H<sub>10</sub> (1)<br><br><b>OR:</b><br>• C = (87.8 / 100) &times; 82 = 72 (1)<br>• H = (12.2 / 100) &times; 82 = 10 (1)<br>• 72 / 12 = 6 (C<sub>6</sub>) and 10 / 1 = 10 (H<sub>10</sub>) &rArr; C<sub>6</sub>H<sub>10</sub> (1)",
        "extra": "if (12 &times; 6) + (1 &times; 10) = 82 used to deduce C<sub>6</sub>H<sub>10</sub>, M3 may be awarded",
        "mark": 3,
        "spec": "3.1.2, 3.3.1"
    },
    "2001-june-chm3w-q5bi": {
        "answers": "Ni or Pt or Pd (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2001-june-chm3w-q5bii": {
        "answers": "One / a C=C bond or double bond (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2001-june-chm3w-q5biii": {
        "answers": "B is saturated or is an alkane or has no C=C (1)",
        "extra": "or not unsaturated or not an alkene or has only C–C single bonds",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2001-june-chm3w-q5biv": {
        "answers": "• Recognises that B is saturated / has no C=C (1)<br>• but has too few H atoms for chain alkane (C<sub>n</sub>H<sub>2n+2</sub>) / cyclic alkane formula = C<sub>n</sub>H<sub>2n</sub> / ring needs fewer H atoms (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.1"
    },
    "2001-june-chm3w-q5bv": {
        "answers": "• Name: Cyclohexene (1)<br>• Structural formula: drawn structure of cyclohexene (six-membered carbon ring with one double bond) (1)",
        "extra": "name: accept cyclichexene<br>structural formula: not tied to name<br><b>not</b> -H<sub>2</sub> structures",
        "mark": 3,
        "spec": "3.3.1, 3.3.4"
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
            img_rel = q.get("markscheme_image", f"img/2001-june-chm3w/ms_{qid.split('-')[-1]}.jpg")
            img_path = os.path.join(SCRATCH_DIR, img_rel.replace("/", os.sep))
            
            print(f"Generating MS for {qid} ({q_num}) -> {img_path}")
            generate_markscheme_image = render_official_markscheme_image
            render_official_markscheme_image(
                question_label=q_num,
                answers_html=data["answers"],
                extra_html=data["extra"],
                marks=data["mark"],
                spec_ref=data["spec"],
                output_path=img_path
            )
            
            # Format text for markscheme_text
            clean_ans = data["answers"].replace("<br>", "\n").replace("&rarr;", "->").replace("&frac12;", "1/2").replace("•", "-")
            clean_ext = data["extra"].replace("<br>", "\n")
            q["markscheme_text"] = f"{clean_ans}\n\n[Extra Information]:\n{clean_ext}" if clean_ext else clean_ans
            updated_count += 1

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {updated_count} questions for 2001-june-chm3w!")

if __name__ == "__main__":
    main()

"""
Convert 2002-june-chm2 markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-june-chm2-q1a": {
        "answers": "• Heat energy change (1)<br>• Measured at constant pressure (1)",
        "extra": "heat energy: <b>not</b> energy on its own<br>mark separately<br>ignore constant temperature statements",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q1bi": {
        "answers": "• (Enthalpy change when) 1 mol of a compound / substance / product is formed (1)<br>• from its constituent elements (1)<br>• in their standard states under standard conditions (1)",
        "extra": "mark separately",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q1bii": {
        "answers": "2Na(s) + S(s) + 2O<sub>2</sub>(g) &rarr; Na<sub>2</sub>SO<sub>4</sub>(s)<br>• Balanced equation (1)<br>• State symbols (1)",
        "extra": "allow &frac18;S<sub>8</sub>(s)<br>state symbols mark only if all species correct",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q1c": {
        "answers": "Enthalpy change is independent of reaction route (1)",
        "extra": "penalise incorrect additional statements",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q1d": {
        "answers": "• Cycle or equation (1)<br>• &Delta;H<sub>f</sub> = 4(&minus;393.5) + 2(&minus;285.8) &minus; (&minus;1356) (1)<br>• = &minus;789.6 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "if answer incorrect: score +789.6 two marks<br>score (&times;1), (&times;2) and (&times;4) for species: one mark<br>if incorrect negative answer given, check for AE for loss of one mark",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q2a": {
        "answers": "2AgNO<sub>3</sub> + Zn &rarr; Zn(NO<sub>3</sub>)<sub>2</sub> + 2Ag (1)<br>(or ionic: 2Ag<sup>+</sup> + Zn &rarr; 2Ag + Zn<sup>2+</sup>)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.4, 3.1.7"
    },
    "2002-june-chm2-q2b": {
        "answers": "• Moles = mv / 1000 = (0.20 &times; 50) / 1000 (1)<br>• = 1.00 &times; 10<sup>&minus;2</sup> (mol) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2002-june-chm2-q2c": {
        "answers": "• Heat energy change = mc&Delta;T = 50 &times; 4.18 &times; 3.20 (1)<br>• = 669 J (or 668.8 J / 0.669 kJ) (1)",
        "extra": "ignore signs<br>penalise wrong units if given",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q2d": {
        "answers": "• Dividing 2 &times; (c) by (b): (2 &times; 669) / 0.010 (1)<br>• = 134 kJ mol<sup>&minus;1</sup> (allow 133&ndash;134) (1)",
        "extra": "mark conseq to equation in (a) for full marks<br>penalise incorrect units; if no working shown and answer incorrect: zero",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q2e": {
        "answers": "Incomplete reaction OR heat loss (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2002-june-chm2-q3ai": {
        "answers": "&minus;2 (or 2&minus;) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q3aii": {
        "answers": "NaI or NaAt (or I<sup>&minus;</sup> / iodide / At<sup>&minus;</sup> / astatide) (1)",
        "extra": "<b>not</b> atoms or molecules",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q3aiii": {
        "answers": "Smell of bad eggs (1)",
        "extra": "allow: PbAc<sub>2</sub> paper goes black / K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub>/H<sup>+</sup> goes cloudy green",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q3aiv": {
        "answers": "8e<sup>&minus;</sup> + 8H<sup>+</sup> + H<sub>2</sub>SO<sub>4</sub> &rarr; H<sub>2</sub>S + 4H<sub>2</sub>O (1)<br>(or 8e<sup>&minus;</sup> + 10H<sup>+</sup> + SO<sub>4</sub><sup>2&minus;</sup> &rarr; H<sub>2</sub>S + 4H<sub>2</sub>O)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.3, 3.1.7"
    },
    "2002-june-chm2-q3bi": {
        "answers": "HF or HCl (1)",
        "extra": "CE = 0 if redox answer given<br>if NaF, NaCl, F<sup>&minus;</sup> or Cl<sup>&minus;</sup> given, lose mark in (i) but mark on",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q3bii": {
        "answers": "NaF or NaCl (or F<sup>&minus;</sup> / Cl<sup>&minus;</sup> / sodium fluoride / sodium chloride) (1)",
        "extra": "if wrong halide given, allow max 1 in b(iii)",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q3biii": {
        "answers": "A proton donor or an acid (1)",
        "extra": "allow if X is a hydrogen halide in (i)",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q3biv": {
        "answers": "H<sup>+</sup> + F<sup>&minus;</sup> &rarr; HF (1)<br>(or H<sub>2</sub>SO<sub>4</sub> + NaF &rarr; NaHSO<sub>4</sub> + HF / H<sub>2</sub>SO<sub>4</sub> + 2NaF &rarr; Na<sub>2</sub>SO<sub>4</sub> + 2HF / or corresponding chloride equations)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q4ai": {
        "answers": "HNO<sub>3</sub> (nitric acid) or CH<sub>3</sub>COOH (ethanoic acid) (1)",
        "extra": "CE in (a) if incorrect acid given (e.g. HCl or H<sub>2</sub>SO<sub>4</sub>)",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q4aii": {
        "answers": "2HNO<sub>3</sub> + Na<sub>2</sub>CO<sub>3</sub> &rarr; 2NaNO<sub>3</sub> + CO<sub>2</sub> + H<sub>2</sub>O (1)<br>(or ionic: 2H<sup>+</sup> + CO<sub>3</sub><sup>2&minus;</sup> &rarr; H<sub>2</sub>O + CO<sub>2</sub>)",
        "extra": "<b>not</b> H<sub>2</sub>CO<sub>3</sub>",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q4bi": {
        "answers": "I<sup>&minus;</sup> or At<sup>&minus;</sup> (iodide or astatide) (1)",
        "extra": "<b>not</b> elements, atoms or molecules",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q4bii": {
        "answers": "F<sup>&minus;</sup> (fluoride) (1)",
        "extra": "<b>not</b> element, atoms or molecules",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q4ci": {
        "answers": "Cl<sup>&minus;</sup> (chloride) (1)",
        "extra": "allow AgCl<br><b>not</b> element, atoms or molecules",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q4cii": {
        "answers": "Br<sup>&minus;</sup> (bromide) (1)",
        "extra": "allow AgBr<br><b>not</b> element, atoms or molecules",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q5ai": {
        "answers": "• y-axis: Number of molecules (or particles) (1)<br>• x-axis: (Molecular) Energy (1)",
        "extra": "y-axis: <b>not</b> moles/mols, <b>not</b> atoms, <b>not</b> fraction/proportion<br>x-axis: <b>not</b> velocity",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2002-june-chm2-q5aii": {
        "answers": "The total number of molecules / particles in the sample (or number of molecules present) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2002-june-chm2-q5aiii": {
        "answers": "No molecules have no energy (OR All molecules have some energy) (1)",
        "extra": "do <b>not</b> allow 'If there are no molecules there is no energy'",
        "mark": 1,
        "spec": "3.1.5"
    },
    "2002-june-chm2-q5bi": {
        "answers": "• The minimum energy required (1)<br>• for a reaction to occur / to start reaction / for a successful collision (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.5"
    },
    "2002-june-chm2-q5bii": {
        "answers": "• Change: Catalyst (1)<br>• Explanation: Provides an alternative reaction route / pathway (1)<br>• with a lower activation energy (1)",
        "extra": "if change incorrect CE = 0<br>allow lower activation energy (1) so more molecules have enough energy to react (1)",
        "mark": 3,
        "spec": "3.1.5"
    },
    "2002-june-chm2-q6a": {
        "answers": "A reducing agent gives electrons (or loses electrons) (1)",
        "extra": "<b>not</b> electron pairs",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q6b": {
        "answers": "Zero (0) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q6ci": {
        "answers": "(+)3 (1)",
        "extra": "allow answers in roman (III)",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q6cii": {
        "answers": "&minus;3 (or 3&minus;) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q6ciii": {
        "answers": "&minus;1 (or 1&minus;) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q6di": {
        "answers": "PbO<sub>2</sub> + 4H<sup>+</sup> + 2e<sup>&minus;</sup> &rarr; Pb<sup>2+</sup> + 2H<sub>2</sub>O (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q6dii": {
        "answers": "2Cl<sup>&minus;</sup> &rarr; Cl<sub>2</sub> + 2e<sup>&minus;</sup> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q6diii": {
        "answers": "PbO<sub>2</sub> + 4H<sup>+</sup> + 2Cl<sup>&minus;</sup> &rarr; Pb<sup>2+</sup> + Cl<sub>2</sub> + 2H<sub>2</sub>O (1)<br>(or molecular: PbO<sub>2</sub> + 4HCl &rarr; PbCl<sub>2</sub> + Cl<sub>2</sub> + 2H<sub>2</sub>O)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q7a": {
        "answers": "To kill bacteria / micro-organisms / microbes / germs OR to sterilize / disinfect water (as a germicide) (1)",
        "extra": "<b>not</b> to purify water; <b>not</b> to kill organisms",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q7b": {
        "answers": "• Equation: Cl<sub>2</sub> + H<sub>2</sub>O &rlarr; HClO + HCl (1)<br>• Substance: (Free) chlorine or Cl<sub>2</sub> (1)",
        "extra": "allow ionic products (H<sup>+</sup> + Cl<sup>&minus;</sup> + HClO)",
        "mark": 2,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q7c": {
        "answers": "2NaOH + Cl<sub>2</sub> &rarr; NaCl + NaClO + H<sub>2</sub>O (1)<br>(or ionic: 2OH<sup>&minus;</sup> + Cl<sub>2</sub> &rarr; Cl<sup>&minus;</sup> + ClO<sup>&minus;</sup> + H<sub>2</sub>O)",
        "extra": "both products must be salts / allow OCl<sup>&minus;</sup>",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q7di": {
        "answers": "Cl<sub>2</sub> + 2KI &rarr; 2KCl + I<sub>2</sub> (1)<br>(or ionic: Cl<sub>2</sub> + 2I<sup>&minus;</sup> &rarr; 2Cl<sup>&minus;</sup> + I<sub>2</sub>)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.3"
    },
    "2002-june-chm2-q7dii": {
        "answers": "I<sub>2</sub> + 2Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub> &rarr; 2NaI + Na<sub>2</sub>S<sub>4</sub>O<sub>6</sub> (1)<br>(or ionic: I<sub>2</sub> + 2S<sub>2</sub>O<sub>3</sub><sup>2&minus;</sup> &rarr; 2I<sup>&minus;</sup> + S<sub>4</sub>O<sub>6</sub><sup>2&minus;</sup>)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-june-chm2-q7diii": {
        "answers": "• Moles thiosulphate = mv / 1000 = (0.0150 &times; 7.20) / 1000 = 1.08 &times; 10<sup>&minus;4</sup> mol (1)<br>• Moles Cl<sub>2</sub> = Moles I<sub>2</sub> = (1.08 &times; 10<sup>&minus;4</sup>) / 2 = 5.40 &times; 10<sup>&minus;5</sup> mol (1)<br>• Mass Cl<sub>2</sub> = (5.40 &times; 10<sup>&minus;5</sup>) &times; 71.0 (1)<br>• = 3.83 &times; 10<sup>&minus;3</sup> g dm<sup>&minus;3</sup> (1)",
        "extra": "penalise missing 1000 as AE &minus;1<br>allow 3.80&ndash;3.85 &times; 10<sup>&minus;3</sup> g dm<sup>&minus;3</sup>",
        "mark": 4,
        "spec": "3.1.2"
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
            img_rel = q.get("markscheme", f"img/2002-june-chm2/ms_{qid.split('-')[-1]}.jpg")
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
            
            clean_ans = data["answers"].replace("<br>", "\n").replace("&rarr;", "->").replace("&rlarr;", "<=>").replace("&frac18;", "1/8").replace("&minus;", "-").replace("•", "-")
            clean_ext = data["extra"].replace("<br>", "\n").replace("&minus;", "-")
            q["markscheme_text"] = f"{clean_ans}\n\n[Extra Information]:\n{clean_ext}" if clean_ext else clean_ans
            updated_count += 1

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {updated_count} questions for 2002-june-chm2!")

if __name__ == "__main__":
    main()

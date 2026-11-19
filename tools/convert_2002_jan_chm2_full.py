"""
Convert 2002-jan-chm2 markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-jan-chm2-q1a": {
        "answers": "• (Enthalpy change) when 1 mol of a compound is formed (1)<br>• from its constituent elements (1)<br>• in their standard states (1)",
        "extra": "mark each point independently<br>allow energy or heat<br>ignore 'evolved or absorbed'",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2002-jan-chm2-q1b": {
        "answers": "(The enthalpy change for a reaction is) independent of the route (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2002-jan-chm2-q1c": {
        "answers": "• &Delta;H<sub>c</sub> = &Sigma;&Delta;H<sub>f</sub>(products) &minus; &Sigma;&Delta;H<sub>f</sub>(reactants) (1)<br>• = [(3 &times; &minus;286) + (3 &times; &minus;394)] &minus; (&minus;248) (1)<br>• = &minus;1792 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "deduct one mark for each error to zero",
        "mark": 3,
        "spec": "3.1.4"
    },
    "2002-jan-chm2-q2a": {
        "answers": "• (Energy required) to break a given covalent bond (1)<br>• averaged over a range of compounds (1)",
        "extra": "penalise first mark if 'energy/enthalpy evolved'",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2002-jan-chm2-q2bi": {
        "answers": "• 4 &times; (C&minus;H) = 4 &times; 413 = +1652<br>&nbsp;&nbsp;1 &times; (C&minus;C) = 1 &times; 347 = 347<br>&nbsp;&nbsp;1 &times; (C=O) = 1 &times; 736 = 736<br>&nbsp;&nbsp;2&frac12; &times; (O=O) = 2.5 &times; 498 = 1245<br>• Reactants bonds broken: 2735 + 1245 = +3980 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "first mark for 4 : 1 : 1 or 2735 (1) [ignore sign]",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2002-jan-chm2-q2bii": {
        "answers": "• 4 &times; (H&minus;O) = &minus;4 &times; 464 = &minus;1856<br>&nbsp;&nbsp;4 &times; (C=O) = &minus;4 &times; 736 = &minus;2944<br>• Products bonds formed = &minus;4800 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "first mark for 4 : 4 (1)",
        "mark": 2,
        "spec": "3.1.4"
    },
    "2002-jan-chm2-q2biii": {
        "answers": "&Delta;H = &Sigma;(Bonds broken) &minus; &Sigma;(Bonds made)<br>= +3980 &minus; 4800 = &minus;820 (kJ mol<sup>&minus;1</sup>) (1)",
        "extra": "consequential mark for incorrect answers in (i) and (ii) as (i) Answer + (ii) Answer",
        "mark": 1,
        "spec": "3.1.4"
    },
    "2002-jan-chm2-q3ai": {
        "answers": "• Rates: Rates are equal, forward and backward (1)<br>• Concentrations: Concentrations are constant (1)",
        "extra": "Q of L mark",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2002-jan-chm2-q3aii": {
        "answers": "• Equilibrium yield: Decreases (1)<br>• Explanation: More moles / molecules of product (or 2 &rarr; 4) (1)<br>• Reaction / equilibrium moves to the left / to reduce constraint (1)",
        "extra": "if wrong, allow max 1 for a correct moles statement<br><b>not</b> 'volume' answers<br>allow one for 'Reaction favours fewer molecules'",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2002-jan-chm2-q3aiii": {
        "answers": "positive / endothermic (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6"
    },
    "2002-jan-chm2-q3aiv": {
        "answers": "• Both forward and backward rates increase / are changed (1)<br>• by equal amount / same proportion (1)",
        "extra": "allow one mark for 'Ea of forward and backward reactions reduced by an equal amount'",
        "mark": 2,
        "spec": "3.1.6"
    },
    "2002-jan-chm2-q3bi": {
        "answers": "• The reaction is exothermic (1)<br>• High temperature gives a low equilibrium yield (or low temp favours the reaction) (1)<br>• Rate of reaction is higher at higher temperature (1)",
        "extra": "do <b>not</b> allow answers based on cost of higher temp etc.",
        "mark": 3,
        "spec": "3.1.6"
    },
    "2002-jan-chm2-q3bii": {
        "answers": "• Higher pressure gives a higher yield (1)<br>• 4 moles of gaseous reactant form 2 moles of gaseous product (1)<br>• Higher pressure increases rate of reaction (1)<br>• High pressure is expensive to produce (generation / equipment / compression cost factor) (1)",
        "extra": "NB <b>not</b> a safety answer<br>equilibrium statement required for mark 2",
        "mark": 4,
        "spec": "3.1.6"
    },
    "2002-jan-chm2-q4ai": {
        "answers": "loss (of electrons) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-jan-chm2-q4aii": {
        "answers": "• Oxidation state of nitrogen in NO: (+)2 (1)<br>• Oxidation state of nitrogen in NH<sub>4</sub><sup>+</sup>: &minus;3 (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.7"
    },
    "2002-jan-chm2-q4aiii": {
        "answers": "I<sub>2</sub> (or iodine) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-jan-chm2-q4bi": {
        "answers": "Cl<sub>2</sub> + 2e<sup>&minus;</sup> &rarr; 2Cl<sup>&minus;</sup> (1)",
        "extra": "ignore state symbols in equations<br>allow multiples",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-jan-chm2-q4bii": {
        "answers": "SO<sub>2</sub> + 2H<sub>2</sub>O &rarr; SO<sub>4</sub><sup>2&minus;</sup> + 4H<sup>+</sup> + 2e<sup>&minus;</sup> (1)",
        "extra": "ignore state symbols in equations<br>allow multiples",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-jan-chm2-q4biii": {
        "answers": "SO<sub>2</sub> + 2H<sub>2</sub>O + Cl<sub>2</sub> &rarr; SO<sub>4</sub><sup>2&minus;</sup> + 2Cl<sup>&minus;</sup> + 4H<sup>+</sup> (1)",
        "extra": "or SO<sub>2</sub> + 2H<sub>2</sub>O + Cl<sub>2</sub> &rarr; H<sub>2</sub>SO<sub>4</sub> + 2HCl<br>ignore state symbols in equations<br>allow multiples",
        "mark": 1,
        "spec": "3.1.7"
    },
    "2002-jan-chm2-q5a": {
        "answers": "• Moles = mv / 1000 (1)<br>• = 0.36 &times; 28.2 / 1000 = 0.010(2) (1)",
        "extra": "NB An answer of 0.01 scores one",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2002-jan-chm2-q5b": {
        "answers": "I<sub>2</sub> + 2S<sub>2</sub>O<sub>3</sub><sup>2&minus;</sup> &rarr; S<sub>4</sub>O<sub>6</sub><sup>2&minus;</sup> + 2I<sup>&minus;</sup> (1)",
        "extra": "allow multiples",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2002-jan-chm2-q5c": {
        "answers": "(Mole ratio = 1 : 2)<br>Moles of I<sub>2</sub> = Answer from (a) / 2 = 0.005(1) mol (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2002-jan-chm2-q5d": {
        "answers": "2KI + Cl<sub>2</sub> &rarr; 2KCl + I<sub>2</sub> (1)<br>(or ionic: 2I<sup>&minus;</sup> + Cl<sub>2</sub> &rarr; 2Cl<sup>&minus;</sup> + I<sub>2</sub>)",
        "extra": "or a multiple<br>ignore state symbols and incorrect use of caps",
        "mark": 1,
        "spec": "3.1.2, 3.2.3"
    },
    "2002-jan-chm2-q5e": {
        "answers": "• Moles Cl<sub>2</sub> = Moles I<sub>2</sub> = 0.0051 (1)<br>• M<sub>r</sub>(Cl<sub>2</sub>) = 35.5 &times; 2 = 71 (1)<br>• Mass Cl<sub>2</sub> = 0.0051 &times; 71 = 0.360 g (1)",
        "extra": "allow 0.36 &plusmn; 0.005<br>if moles not from (c), max 1 mark if M<sub>r</sub> of chlorine given as 71<br>if A<sub>r</sub> of chlorine used, score max 1<br>if M<sub>r</sub>(chlorine) = 70, penalise as AE",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2002-jan-chm2-q5f": {
        "answers": "• Indicator: Starch (1)<br>• Colour change: Blue (or black or blue/black) to colourless (1)",
        "extra": "not straw coloured<br>if an indicator given, it must be correct for second mark to be awarded",
        "mark": 2,
        "spec": "3.1.2"
    },
    "2002-jan-chm2-q6ai": {
        "answers": "C + O<sub>2</sub> &rarr; CO<sub>2</sub> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.1"
    },
    "2002-jan-chm2-q6aii": {
        "answers": "Fe<sub>2</sub>O<sub>3</sub> + 3CO &rarr; 2Fe + 3CO<sub>2</sub> (1)<br>(or Fe<sub>2</sub>O<sub>3</sub> + 3C &rarr; 2Fe + 3CO)",
        "extra": "allow oxides FeO, Fe<sub>2</sub>O<sub>3</sub>, Fe<sub>3</sub>O<sub>4</sub>",
        "mark": 1,
        "spec": "3.2.1"
    },
    "2002-jan-chm2-q6aiii": {
        "answers": "Mg + S &rarr; MgS (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.1"
    },
    "2002-jan-chm2-q6aiv": {
        "answers": "• Removal: Oxygen (1)<br>• blown through molten iron (or liquid iron / bubbled through) (1)<br>• Reason: Carbon makes iron brittle (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.2.1"
    },
    "2002-jan-chm2-q6bi": {
        "answers": "(Titanium) carbide is formed (1)",
        "extra": "allow C bonds / reacts with Ti",
        "mark": 1,
        "spec": "3.2.1"
    },
    "2002-jan-chm2-q6bii": {
        "answers": "• Equation: TiO<sub>2</sub> + 2C + 2Cl<sub>2</sub> &rarr; TiCl<sub>4</sub> + 2CO (or with C &rarr; TiCl<sub>4</sub> + CO<sub>2</sub>)<br>&nbsp;&nbsp;All species correct (1)<br>&nbsp;&nbsp;Balanced equation (1)<br>• Condition: High temperature (or 700&ndash;1100 °C) (1)",
        "extra": "mark independently<br>condition: <b>not</b> 'heat'",
        "mark": 3,
        "spec": "3.2.1"
    },
    "2002-jan-chm2-q6c": {
        "answers": "• Use of carbon: As electrodes (or cathode / anode) (1)<br>• Half-equation: Al<sup>3+</sup> + 3e<sup>&minus;</sup> &rarr; Al (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.1"
    },
    "2002-jan-chm2-q6d": {
        "answers": "<b>Any three factors from:</b><br>• Cost of reductant (1)<br>• Cost of energy (1)<br>• Purity of metal (1)<br>• Reactivity of metal (1)",
        "extra": "Max 3 marks",
        "mark": 3,
        "spec": "3.2.1"
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
            img_rel = q.get("markscheme", f"img/2002-jan-chm2/ms_{qid.split('-')[-1]}.jpg")
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

    print(f"Successfully updated {updated_count} questions for 2002-jan-chm2!")

if __name__ == "__main__":
    main()

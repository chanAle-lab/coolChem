"""
Convert 2002-june-chm3w markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-june-chm3w-q1a": {
        "answers": "<b>Any three from:</b><br>• Crude oil heated to vaporise it / oil is vaporised (1)<br>• (Vapour passed into) fractionating tower / column (1)<br>• Top of tower cooler than bottom / negative temperature gradient (1)<br>• Fractions separated by boiling points / condense at different temperatures or levels (1)",
        "extra": "Max 3 marks<br>allow low boiling fractions / small molecules / light components at the top",
        "mark": 3,
        "spec": "3.3.2"
    },
    "2002-june-chm3w-q1bi": {
        "answers": "• Identifies shortfall in supply &ndash; e.g. petrol / smaller molecules (1)<br>• Produces higher value / more useful products / more of required material (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2002-june-chm3w-q1bii": {
        "answers": "<b>Any two from:</b><br>• Motor fuels (1)<br>• Aromatic hydrocarbons (1)<br>• Branched alkanes / hydrocarbons (1)<br>• Cycloalkanes (1)",
        "extra": "ignore specific fractions, alkanes, shorter alkanes<br>penalise alkenes, hydrogen",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2002-june-chm3w-q1c": {
        "answers": "• Catalyst: Zeolite / aluminosilicate (1)<br>• Mechanism: Carbocation / heterolytic fission (1)<br>• Conditions (2 marks):<br>&nbsp;&nbsp;High temp / around 450 °C [300&ndash;600 °C] (1)<br>&nbsp;&nbsp;Slight pressure [&gt; 1 atm &le; 10 atm / 1 MPa / 1000 kPa] (1)",
        "extra": "conditions: <b>not</b> heat/warm<br>pressure: <b>not</b> high pressure",
        "mark": 4,
        "spec": "3.3.2"
    },
    "2002-june-chm3w-q2ai": {
        "answers": "Cl<sub>2</sub> &rarr; 2Cl• (1)",
        "extra": "penalise missing dot '•' once only",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2002-june-chm3w-q2aii": {
        "answers": "CH<sub>2</sub>Cl<sub>2</sub> + Cl<sub>2</sub> &rarr; CHCl<sub>3</sub> + HCl (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2002-june-chm3w-q2aiii": {
        "answers": "• Equation 1: CH<sub>2</sub>Cl<sub>2</sub> + Cl• &rarr; CHCl<sub>2</sub>• + HCl (1)<br>• Equation 2: CHCl<sub>2</sub>• + Cl<sub>2</sub> &rarr; CHCl<sub>3</sub> + Cl• (1)",
        "extra": "can reverse order<br>penalise missing dot '•' once only",
        "mark": 2,
        "spec": "3.3.3"
    },
    "2002-june-chm3w-q2aiv": {
        "answers": "• Effect on rate: Increases (1)<br>• Explanation: More Cl• radicals formed / more Cl&minus;Cl bonds broken (1)",
        "extra": "allow more Cl atoms / more Cl<sub>2</sub> have E<sub>a</sub> / increased rate of Cl• production<br>if decrease given, CE zero marks",
        "mark": 2,
        "spec": "3.3.3"
    },
    "2002-june-chm3w-q2bi": {
        "answers": "C<sub>15</sub>H<sub>32</sub> + 23O<sub>2</sub> &rarr; 15CO<sub>2</sub> + 16H<sub>2</sub>O<br>• Products: 15CO<sub>2</sub> + 16H<sub>2</sub>O (1)<br>• Balance: + 23O<sub>2</sub> (1)",
        "extra": "if wrong reactant, CE",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2002-june-chm3w-q2bii": {
        "answers": "• Identity: CO (carbon monoxide) (1)<br>• Equation: CH<sub>4</sub> + 1&frac12;O<sub>2</sub> &rarr; CO + 2H<sub>2</sub>O (1)",
        "extra": "any balanced equation using CH<sub>4</sub> producing CO (could make C &amp; CO<sub>2</sub> also)",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2002-june-chm3w-q3a": {
        "answers": "The four carbon atoms associated with the double bond: the 2 carbons of C=C and the 2 carbon atoms directly bonded to them (C of CH<sub>3</sub> and C of CH<sub>2</sub>) (1)",
        "extra": "may circle 4 Cs separately",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2002-june-chm3w-q3b": {
        "answers": "• Mechanism (4 marks):<br>&nbsp;&nbsp;M1: curly arrow from C=C bond to H of H&minus;OSO<sub>2</sub>OH (or H<sup>+</sup>) (1)<br>&nbsp;&nbsp;M2: curly arrow from H&minus;O bond to O of H<sub>2</sub>SO<sub>4</sub> (1)<br>&nbsp;&nbsp;M3: tertiary carbocation intermediate (CH<sub>3</sub>)<sub>2</sub>C<sup>+</sup>&minus;CH<sub>2</sub>CH<sub>3</sub> (1)<br>&nbsp;&nbsp;M4: curly arrow from lone pair on :O<sup>&minus;</sup> of &minus;OSO<sub>2</sub>OH to C<sup>+</sup> (1)",
        "extra": "must show :O<sup>&minus;</sup> in HSO<sub>4</sub><sup>&minus;</sup><br>ignore &delta;+, &delta;&minus; unless wrong",
        "mark": 4,
        "spec": "3.3.4"
    },
    "2002-june-chm3w-q3c": {
        "answers": "• Reagent: H<sub>2</sub>O / water / steam / dilute sulphuric acid (1)<br>• Condition: Heat / warm / boil / reflux [50&ndash;100 °C] (1)<br>• Name: 2-methylbutan-2-ol (1)",
        "extra": "name: allow 2-methylbutane-2-ol<br>penalise hydroxy 2-methylbutane once only / paper<br>ignore pressure",
        "mark": 3,
        "spec": "3.3.5"
    },
    "2002-june-chm3w-q3d": {
        "answers": "• Identity: 2-methylbutan-1-ol (or structure) (1)<br>• Explanation (2 marks):<br>&nbsp;&nbsp;C formed via tertiary carbocation, D via primary carbocation (1)<br>&nbsp;&nbsp;tertiary carbocation is more stable than primary carbocation (1)",
        "extra": "if wrong carbocations shown, can still score stability mark",
        "mark": 3,
        "spec": "3.3.4"
    },
    "2002-june-chm3w-q4a": {
        "answers": "• % O = 100 &minus; (64.9 + 13.5) = 21.6% (1)<br>• Moles: C = 64.9 / 12 = 5.41; H = 13.5 / 1 = 13.5; O = 21.6 / 16 = 1.35 (1)<br>• Ratio: 4 : 10 : 1 &rArr; Empirical formula = C<sub>4</sub>H<sub>10</sub>O (1)",
        "extra": "if no % O calculated, only M2 available<br>if arithmetic error in any result, lose M3<br>if percentage composition calculation done: zero",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2002-june-chm3w-q4bi": {
        "answers": "• Type: Tertiary (1)<br>• Reason: No hydrogen atom on central carbon (the carbon bonded to &minus;OH) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2002-june-chm3w-q4bii": {
        "answers": "• Isomer 3: CH<sub>3</sub>&minus;CH(OH)&minus;CH<sub>2</sub>CH<sub>3</sub> (butan-2-ol) (1)<br>• Isomer 4: (CH<sub>3</sub>)<sub>2</sub>CH&minus;CH<sub>2</sub>OH (2-methylpropan-1-ol) (1)",
        "extra": "penalise missing bonds / incorrect bonds once per paper",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2002-june-chm3w-q4ci": {
        "answers": "Aldehyde (1)",
        "extra": "ignore named aldehydes or structures<br>penalise wrong named compound",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2002-june-chm3w-q4cii": {
        "answers": "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CH<sub>2</sub>OH + [O] &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CHO + H<sub>2</sub>O<br>• Product: CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CHO (1)<br>• Balanced equation (1)",
        "extra": "product: <b>not</b> C<sub>3</sub>H<sub>7</sub>CHO, but C<sub>2</sub>H<sub>5</sub>CH<sub>2</sub>CHO is OK<br>[O] can be over arrow; C<sub>4</sub>H<sub>10</sub>O is OK as reactant<br>if use C<sub>3</sub> or C<sub>5</sub> compds no marks in (ii); CE if wrong alcohol",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2002-june-chm3w-q4ciii": {
        "answers": "• Name: Butanoic acid (1)<br>• Structure: CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOH (1)",
        "extra": "mark consequential on (ii) or as stated",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2002-june-chm3w-q4d": {
        "answers": "• Advantage: Fast reaction OR pure product OR continuous process / high yield / 100% alcohol / low manpower (1)<br>• Disadvantage: High technology required OR ethene from non-renewable source / expensive equipment (1)",
        "extra": "<b>not</b> answers based on fermentation",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2002-june-chm3w-q4e": {
        "answers": "• M1: curly arrow from lone pair on :O of OH to H<sup>+</sup> (or H<sub>2</sub>SO<sub>4</sub>) (1)<br>• M2: curly arrow from C&minus;O bond to O<sup>+</sup>H<sub>2</sub> (1)<br>• M3: carbocation intermediate CH<sub>3</sub>&minus;CH<sub>2</sub><sup>+</sup> (1)<br>• M4: curly arrow from C&minus;H bond to C&minus;C bond forming CH<sub>2</sub>=CH<sub>2</sub> + H<sup>+</sup> (1)",
        "extra": "scores M2 &amp; M4 if no carbocation intermediate shown, but lose M3",
        "mark": 4,
        "spec": "3.3.5"
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
            img_rel = q.get("markscheme", f"img/2002-june-chm3w/ms_{qid.split('-')[-1]}.jpg")
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
            
            clean_ans = data["answers"].replace("<br>", "\n").replace("&rarr;", "->").replace("&frac12;", "1/2").replace("&minus;", "-").replace("&le;", "<=").replace("&gt;", ">").replace("•", "-")
            clean_ext = data["extra"].replace("<br>", "\n").replace("&minus;", "-")
            q["markscheme_text"] = f"{clean_ans}\n\n[Extra Information]:\n{clean_ext}" if clean_ext else clean_ans
            updated_count += 1

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {updated_count} questions for 2002-june-chm3w!")

if __name__ == "__main__":
    main()

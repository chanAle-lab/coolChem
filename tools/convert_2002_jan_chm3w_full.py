"""
Convert 2002-jan-chm3w markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-jan-chm3w-q1a": {
        "answers": "• Condition: uv light or sunlight or 450 °C or high temp (1)<br>• Explanation: uv light provides energy to break Cl&minus;Cl bond (1)",
        "extra": "do not accept ref. to E<sub>a</sub> or wrong bond or 'to make Cl radicals'",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2002-jan-chm3w-q1bi": {
        "answers": "(Free) radical substitution (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2002-jan-chm3w-q1bii": {
        "answers": "• Step 1: initiation (1)<br>• Step 2: propagation (1)<br>• Step 3: termination (1)",
        "extra": "any order<br>don't be too harsh on spelling",
        "mark": 3,
        "spec": "3.3.2"
    },
    "2002-jan-chm3w-q1ci": {
        "answers": "• Equation 1: CH<sub>3</sub>Cl + Cl• &rarr; CH<sub>2</sub>Cl• + HCl (1)<br>• Equation 2: CH<sub>2</sub>Cl• + Cl<sub>2</sub> &rarr; CH<sub>2</sub>Cl<sub>2</sub> + Cl• (1)<br>(or CH<sub>2</sub>Cl• + Cl• &rarr; CH<sub>2</sub>Cl<sub>2</sub>)",
        "extra": "mark equations independently, any order<br>penalise absence of dot '•' once only",
        "mark": 2,
        "spec": "3.3.2"
    },
    "2002-jan-chm3w-q1cii": {
        "answers": "CH<sub>2</sub>Cl• + CH<sub>3</sub>• &rarr; CH<sub>3</sub>CH<sub>2</sub>Cl (1)<br>(or CH<sub>3</sub>CH<sub>2</sub>• + Cl<sub>2</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub>Cl + Cl• / CH<sub>3</sub>CH<sub>2</sub>• + Cl• &rarr; CH<sub>3</sub>CH<sub>2</sub>Cl)",
        "extra": "equation must have CH<sub>3</sub>CH<sub>2</sub>Cl as product<br>accept C<sub>2</sub>H<sub>5</sub>Cl<br>penalise absence of dot '•' once only",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2002-jan-chm3w-q2ai": {
        "answers": "• Reagent: Hydrogen or H<sub>2</sub> (1)<br>• Conditions: Ni (catalyst) and 100&ndash;200 °C / heat (1)",
        "extra": "conditions: ignore (Pt)<br>not 'high temp', not 'warm'",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2002-jan-chm3w-q2aii": {
        "answers": "• Difference in structure: soft margarine is less hydrogenated / has more C=C bonds / is more unsaturated than hard margarine (1)<br>• Difference in melting point: soft margarine has lower melting point (1)",
        "extra": "must be a comparison",
        "mark": 3,
        "spec": "3.3.4"
    },
    "2002-jan-chm3w-q2bi": {
        "answers": "3-methylbutan-2-ol (1)",
        "extra": "no alternatives",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2002-jan-chm3w-q2bii": {
        "answers": "elimination or dehydration (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2002-jan-chm3w-q2biii": {
        "answers": "(conc) H<sub>2</sub>SO<sub>4</sub> or (conc) H<sub>3</sub>PO<sub>4</sub> (1)",
        "extra": "name or correct formula",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2002-jan-chm3w-q2biv": {
        "answers": "• Alkene 1: CH<sub>2</sub>=CH&minus;CH(CH<sub>3</sub>)<sub>2</sub> (3-methylbut-1-ene) (1)<br>• Alkene 2: CH<sub>3</sub>&minus;CH=C(CH<sub>3</sub>)<sub>2</sub> (2-methylbut-2-ene) (1)",
        "extra": "double bond must be shown<br>accept any correct unambiguous structures<br>if but-1-ene and but-2-ene offered, allow M2",
        "mark": 2,
        "spec": "3.3.4, 3.3.5"
    },
    "2002-jan-chm3w-q3a": {
        "answers": "• Electrophile: electron-pair acceptor / electron-deficient species / electron-seeking species (1)<br>• Addition: reaction which increases number of substituents / converts double bond to single bond / where two molecules form one molecule (1)",
        "extra": "for species accept atom, molecule, ion<br>not '+' ion, not 'attracted to − charge'",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2002-jan-chm3w-q3b": {
        "answers": "• (high) electron-dense / electron-rich C=C bond (or &pi; bond / 4e<sup>&minus;</sup> between carbons) (1)<br>• causes induced dipole in Br<sub>2</sub> (1)",
        "extra": "not just 'C=C'<br>ignore refs to 'temporary'<br>can score M2 from &delta;+/&delta;&minus; on Br<sub>2</sub> in (c) unless contradicting error in (b)",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2002-jan-chm3w-q3c": {
        "answers": "• Mechanism (4 marks):<br>&nbsp;&nbsp;M1: curly arrow from C=C bond to Br (1)<br>&nbsp;&nbsp;M2: curly arrow from Br&minus;Br bond to Br (1)<br>&nbsp;&nbsp;M3: structure of secondary carbocation H<sub>2</sub>C(Br)&minus;CH<sup>+</sup>&minus;CH<sub>3</sub> (1)<br>&nbsp;&nbsp;M4: curly arrow from lone pair on :Br<sup>&minus;</sup> to C<sup>+</sup> (1)<br>• Name of product: 1,2-dibromopropane (1)",
        "extra": "if incorrect alkene, lose M3 (wrong cation)<br>mark M4 consequentially on M3",
        "mark": 5,
        "spec": "3.3.4"
    },
    "2002-jan-chm3w-q3d": {
        "answers": "addition (1)",
        "extra": "not 'additional'",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2002-jan-chm3w-q4ai": {
        "answers": "• Type of reaction: reduction / (nucleophilic) addition / hydrogenation (1)<br>• Reagent Y: sodium borohydride / NaBH<sub>4</sub> / H<sub>2</sub> (1)",
        "extra": "not NaBH<sub>4</sub> for hydrogenation",
        "mark": 2,
        "spec": "3.3.8, 3.3.5"
    },
    "2002-jan-chm3w-q4aii": {
        "answers": "CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CHO + [O] &rarr; CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOH (1)",
        "extra": "accept [O] over arrow<br>accept C<sub>3</sub>H<sub>7</sub>CHO &rarr; C<sub>3</sub>H<sub>7</sub>COOH",
        "mark": 1,
        "spec": "3.3.8, 3.3.9"
    },
    "2002-jan-chm3w-q4bi": {
        "answers": "• (compounds) with same molecular formula (or same number & type of atoms) (1)<br>• with atoms arranged in different functional groups (or in different classes of compounds) (1)",
        "extra": "second mark tied to first",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2002-jan-chm3w-q4bii": {
        "answers": "butanone or CH<sub>3</sub>COCH<sub>2</sub>CH<sub>3</sub> (1)",
        "extra": "or tetrahydrofuran / cyclic ether or other acceptable structure",
        "mark": 1,
        "spec": "3.3.1, 3.3.8"
    },
    "2002-jan-chm3w-q4ci": {
        "answers": "• Empirical formula: simplest ratio of atoms of each element in the compound or molecule (1)<br>• Molecular formula: (actual) number of atoms of each element present in a compound or molecule (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.2, 3.3.1"
    },
    "2002-jan-chm3w-q4cii": {
        "answers": "• C: 62.07 / 12 = 5.17, H: 10.34 / 1 = 10.34, O: 27.59 / 16 = 1.72 (1)<br>• ratio C : H : O = 3 : 6 : 1 &rArr; Empirical formula = C<sub>3</sub>H<sub>6</sub>O (1)<br>• Molecular formula = (116 / 58 &times; C<sub>3</sub>H<sub>6</sub>O) = C<sub>6</sub>H<sub>12</sub>O<sub>2</sub> (1)",
        "extra": "if correct answer, working not essential",
        "mark": 3,
        "spec": "3.1.2, 3.3.1"
    },
    "2002-jan-chm3w-q5a": {
        "answers": "• Name of mechanism: nucleophilic substitution (1)<br>• Mechanism (4 marks):<br>&nbsp;&nbsp;M1: curly arrow from lone pair on :NH<sub>3</sub> to C (1)<br>&nbsp;&nbsp;M2: curly arrow from C&minus;Br bond to Br (1)<br>&nbsp;&nbsp;M3: intermediate structure showing + charge on N (1)<br>&nbsp;&nbsp;M4: curly arrow from N&minus;H bond to N<sup>+</sup> (or loss of H<sup>+</sup> by attack of :NH<sub>3</sub>) (1)",
        "extra": "M3 is for correct intermediate - if used wrong halogenoalkane lose M3<br>wrong dipole loses C&minus;Br mark<br>mark S<sub>N</sub>1 using same points",
        "mark": 5,
        "spec": "3.3.3, 3.3.11"
    },
    "2002-jan-chm3w-q5b": {
        "answers": "• Role of potassium hydroxide: Base (1)<br>• Mechanism (4 marks):<br>&nbsp;&nbsp;M1: curly arrow from lone pair on :OH<sup>&minus;</sup> to H on adjacent carbon (1)<br>&nbsp;&nbsp;M2: curly arrow from C&minus;H bond to C&minus;C bond (1)<br>&nbsp;&nbsp;M3: curly arrow from C&minus;Br bond to Br (1)<br>&nbsp;&nbsp;M4: structure of propene CH<sub>3</sub>CH=CH<sub>2</sub> (1)",
        "extra": "mark E1 using same points",
        "mark": 5,
        "spec": "3.3.3"
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
            img_rel = q.get("markscheme", f"img/2002-jan-chm3w/ms_{qid.split('-')[-1]}.jpg")
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

    print(f"Successfully updated {updated_count} questions for 2002-jan-chm3w!")

if __name__ == "__main__":
    main()

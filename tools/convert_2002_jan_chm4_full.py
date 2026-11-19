"""
Convert 2002-jan-chm4 markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-jan-chm4-q1ai": {
        "answers": "Comparing Experiments 1 and 2: [A] doubles whilst [B] is kept constant, and the rate doubles (1)",
        "extra": "stated or shown numerically",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2002-jan-chm4-q1aii": {
        "answers": "2 (or [B]<sup>2</sup>) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.9"
    },
    "2002-jan-chm4-q1bi": {
        "answers": "• k = rate / ([C]<sup>2</sup>[D]) = (9.30 &times; 10<sup>&minus;5</sup>) / ((0.75)<sup>2</sup> &times; 1.50) (1)<br>• = 1.10 &times; 10<sup>&minus;4</sup> (1)<br>• Units: mol<sup>&minus;2</sup> dm<sup>6</sup> s<sup>&minus;1</sup> (1)",
        "extra": "upside-down expression for k scores zero in (i) for 9073",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2002-jan-chm4-q1bii": {
        "answers": "• rate = k[C]<sup>2</sup>[D] = (1.10 &times; 10<sup>&minus;4</sup>) &times; (0.20)<sup>2</sup> &times; (0.10) (1)<br>• = 4.41 &times; 10<sup>&minus;7</sup> (mol dm<sup>&minus;3</sup> s<sup>&minus;1</sup>) (1)",
        "extra": "consequential on (i)<br>ignore units<br>if k = 9073 used, rate = 9073 &times; (0.20)<sup>2</sup> &times; 0.10 = 36.3 scores (1) in (ii)",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2002-jan-chm4-q2ai": {
        "answers": "0.86 (mol) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.6, 3.1.10"
    },
    "2002-jan-chm4-q2aii": {
        "answers": "• total moles = 0.86 + 0.430 + 0.0850 = 1.375 (1)<br>• mole fraction of H<sub>2</sub> = 0.86 / 1.375 = 0.625 (1)",
        "extra": "consequential on (i)<br>allow 0.62&ndash;0.63",
        "mark": 2,
        "spec": "3.1.10"
    },
    "2002-jan-chm4-q2aiii": {
        "answers": "• pp = mole fraction &times; total P (1)<br>• = 0.625 &times; (1.75 &times; 10<sup>4</sup>) = 1.09 &times; 10<sup>4</sup> (kPa) (or 1.10 &times; 10<sup>4</sup>) (1)",
        "extra": "consequential on (ii)<br>ignore units",
        "mark": 2,
        "spec": "3.1.10"
    },
    "2002-jan-chm4-q2bi": {
        "answers": "K<sub>p</sub> = p(CH<sub>3</sub>OH) / [p(H<sub>2</sub>)<sup>2</sup> &times; p(CO)] (1)",
        "extra": "penalize square brackets [ ]",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2002-jan-chm4-q2bii": {
        "answers": "• K<sub>p</sub> = 2710 / ((12300)<sup>2</sup> &times; 7550) = 2.37 &times; 10<sup>&minus;9</sup> (or 2.4 &times; 10<sup>&minus;9</sup>) (1)<br>• Units: kPa<sup>&minus;2</sup> (1)<br>(or 2.37 &times; 10<sup>&minus;15</sup> Pa<sup>&minus;2</sup>)",
        "extra": "not consequential to wrong K<sub>p</sub> expression",
        "mark": 2,
        "spec": "3.1.10"
    },
    "2002-jan-chm4-q2c": {
        "answers": "• Isomer E: (CH<sub>3</sub>)<sub>3</sub>CCOOCH<sub>3</sub> (methyl 2,2-dimethylpropanoate) (1)<br>• Isomer F: CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)COOCH<sub>3</sub> (methyl 2-methylbutanoate) (1)",
        "extra": "allow CO<sub>2</sub>CH<sub>3</sub>",
        "mark": 2,
        "spec": "3.3.9, 3.3.15, 3.3.7"
    },
    "2002-jan-chm4-q3ai": {
        "answers": "K<sub>a</sub> = [H<sup>+</sup>][CH<sub>3</sub>COO<sup>&minus;</sup>] / [CH<sub>3</sub>COOH] (1)<br>(allow [H<sub>3</sub>O<sup>+</sup>])",
        "extra": "",
        "mark": 1,
        "spec": "3.1.12"
    },
    "2002-jan-chm4-q3aii": {
        "answers": "• K<sub>a</sub> = [H<sup>+</sup>]<sup>2</sup> / [CH<sub>3</sub>COOH] (1)<br>• [H<sup>+</sup>] = &radic;(1.74 &times; 10<sup>&minus;5</sup> &times; 0.220) = 1.96 &times; 10<sup>&minus;3</sup> (1)<br>• pH = &minus;log<sub>10</sub>[H<sup>+</sup>] (1)<br>• pH = 2.71 (1)",
        "extra": "pH expression can score independently<br>2 decimal places essential<br>if forget &radic;, can score marks 1 and 3 for pH = 5.42",
        "mark": 4,
        "spec": "3.1.12"
    },
    "2002-jan-chm4-q3bi": {
        "answers": "• moles acid = (25.0 / 1000) &times; 0.220 = 5.50 &times; 10<sup>&minus;3</sup> mol (1)<br>• volume NaOH = (5.50 &times; 10<sup>&minus;3</sup> / 0.150) &times; 1000 (1)<br>• = 36.7 cm<sup>3</sup> (or 36.6 / 37) (1)",
        "extra": "units must match<br><b>not</b> 36, <b>not</b> 37.0",
        "mark": 3,
        "spec": "3.1.12"
    },
    "2002-jan-chm4-q3bii": {
        "answers": "• Indicator: thymol blue (1)<br>• Explanation: weak acid &ndash; strong base titration, equivalence point at pH &gt; 7 / high pH (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2002-jan-chm4-q3c": {
        "answers": "• (1) mol NaOH added = 2.0 / 40.0 = 0.050 (1)<br>• (2) mol CH<sub>3</sub>COOH left = 0.220 &minus; 0.050 = 0.170 (1)<br>• (3) mol CH<sub>3</sub>COO<sup>&minus;</sup> formed = 0.050 (1)<br>• (4) [H<sup>+</sup>] = K<sub>a</sub> [acid] / [salt] OR pH = pK<sub>a</sub> + log([salt]/[acid]) (1)<br>• (5) [H<sup>+</sup>] = (1.74 &times; 10<sup>&minus;5</sup>) &times; (0.170 / 0.050) = 5.916 &times; 10<sup>&minus;5</sup> (1)<br>• (6) pH = 4.23 (1)",
        "extra": "if wrong M<sub>r</sub>: CE, lose marks 1 and 2, then mark consequentially (max 4)<br>if expression wrong, no marks 4, 5, 6<br>correct answer gets 6 marks<br>if forgets subtraction in step 2, scores max 4 (pH = 4.12)<br>if [acid]/[salt] upside down, answer 5.29 scores 3 marks (for 1, 2, 3)",
        "mark": 6,
        "spec": "3.1.12"
    },
    "2002-jan-chm4-q4a": {
        "answers": "• R: O&minus;H (alcohols) (1)<br>• S: C=O (carbonyl) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.6"
    },
    "2002-jan-chm4-q4b": {
        "answers": "aldehyde (or &minus;CHO / RCHO) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.8"
    },
    "2002-jan-chm4-q4ci": {
        "answers": "<b>Any two reasons from:</b><br>• TMS is inert / non-toxic (1)<br>• volatile / easily removed (low boiling point) (1)<br>• gives a single intense peak (12 equivalent protons in identical environment) (1)<br>• signal is upfield of other proton peaks / highly shielded / at &delta; = 0 (1)",
        "extra": "not solvent, not cheap",
        "mark": 2,
        "spec": "3.3.15"
    },
    "2002-jan-chm4-q4cii": {
        "answers": "• Solvent: CDCl<sub>3</sub> or CCl<sub>4</sub> (1)<br>• Reason: proton-free / contains no hydrogen atoms (1)",
        "extra": "solvent: <b>not</b> D<sub>2</sub>O<br>reason: allow no hydrogens; <b>not</b> H<sup>+</sup> / hydrogen ions",
        "mark": 2,
        "spec": "3.3.15"
    },
    "2002-jan-chm4-q4di": {
        "answers": "CH<sub>3</sub>&minus;C(=O)&minus; (methyl ketone / acetyl group) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2002-jan-chm4-q4dii": {
        "answers": "&minus;OH (alcohol group) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2002-jan-chm4-q4diii": {
        "answers": "&minus;CH<sub>2</sub>&minus;CH<sub>2</sub>&minus; (adjacent CH<sub>2</sub> groups) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2002-jan-chm4-q4e": {
        "answers": "CH<sub>3</sub>&minus;C(=O)&minus;CH<sub>2</sub>&minus;CH<sub>2</sub>&minus;OH (4-hydroxybutan-2-one) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15, 3.3.6"
    },
    "2002-jan-chm4-q5ai": {
        "answers": "hexane-1,6-diamine or 1,6-diaminohexane (1)",
        "extra": "allow 1,6-hexan(e)diamine; allow amine",
        "mark": 1,
        "spec": "3.3.11"
    },
    "2002-jan-chm4-q5aii": {
        "answers": "&minus;CO&minus;(CH<sub>2</sub>)<sub>4</sub>&minus;CO&minus;NH&minus;(CH<sub>2</sub>)<sub>6</sub>&minus;NH&minus; (1)",
        "extra": "allow &minus;CONH&minus;",
        "mark": 1,
        "spec": "3.3.12"
    },
    "2002-jan-chm4-q5bi": {
        "answers": "H<sub>2</sub>N&minus;CH(CH<sub>3</sub>)&minus;COOH (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2002-jan-chm4-q5bii": {
        "answers": "H<sub>2</sub>N&minus;CH(CH<sub>3</sub>)&minus;CO&minus;NH&minus;CH(CH<sub>3</sub>)&minus;COOH (1)",
        "extra": "peptide link essential; the rest is consequential on b(i)<br>allow &minus;CONH&minus;; allow anhydride",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2002-jan-chm4-q5ci": {
        "answers": "quaternary ammonium salt (or quaternary ammonium bromide) (1)",
        "extra": "allow quarternary<br><b>not</b> ion, <b>not</b> compound",
        "mark": 1,
        "spec": "3.3.11"
    },
    "2002-jan-chm4-q5cii": {
        "answers": "• Reagent: CH<sub>3</sub>Br or bromomethane (1)<br>• Condition: excess (CH<sub>3</sub>Br) (1)",
        "extra": "penalise CH<sub>3</sub>Cl, but allow excess for any halomethane",
        "mark": 2,
        "spec": "3.3.11"
    },
    "2002-jan-chm4-q5ciii": {
        "answers": "nucleophilic substitution (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.11, 3.3.3"
    },
    "2002-jan-chm4-q6ai": {
        "answers": "CH<sub>3</sub>COCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> + 2[H] &rarr; CH<sub>3</sub>CH(OH)CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub> (1)",
        "extra": "allow C<sub>5</sub>H<sub>10</sub>O + 2[H] &rarr; C<sub>5</sub>H<sub>11</sub>OH",
        "mark": 1,
        "spec": "3.3.8, 3.3.5"
    },
    "2002-jan-chm4-q6aii": {
        "answers": "• Name: nucleophilic addition (1)<br>• Mechanism (3 marks):<br>&nbsp;&nbsp;M1: curly arrow from lone pair on :H<sup>&minus;</sup> to carbonyl carbon (1)<br>&nbsp;&nbsp;M2: curly arrow from C=O bond to oxygen (1)<br>&nbsp;&nbsp;M3: intermediate alkoxide ion and curly arrow from lone pair on :O<sup>&minus;</sup> to H<sup>+</sup> (1)",
        "extra": "QoL mark<br>curly arrow from C=O alone loses M2",
        "mark": 4,
        "spec": "3.3.8"
    },
    "2002-jan-chm4-q6aiii": {
        "answers": "• Racemic mixture / racemate is formed (1)<br>• Two enantiomers formed in equal amounts / equal probability of attack by :H<sup>&minus;</sup> from either side of planar carbonyl group (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.7"
    },
    "2002-jan-chm4-q6b": {
        "answers": "<b>Any two from:</b><br>• m/z = 43 (CH<sub>3</sub>CO<sup>+</sup>) (1)<br>• m/z = 71 (CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CO<sup>+</sup>) (1)<br>• m/z = 15 (CH<sub>3</sub><sup>+</sup>) (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.6"
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
            img_rel = q.get("markscheme", f"img/2002-jan-chm4/ms_{qid.split('-')[-1]}.jpg")
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

    print(f"Successfully updated {updated_count} questions for 2002-jan-chm4!")

if __name__ == "__main__":
    main()

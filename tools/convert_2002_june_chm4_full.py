"""
Convert 2002-june-chm4 markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-june-chm4-q1a": {
        "answers": "• Order with respect to iodine: <b>0</b> (1)<br>• Overall order: <b>2</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2002-june-chm4-q1b": {
        "answers": "• <i>k</i> = <span style=\"font-family:serif;\">2 × 10<sup>&minus;5</sup> / (1.50 × 3.00 × 10<sup>&minus;2</sup>)</span> (1)<br>• = <b>4.4(4) × 10<sup>&minus;4</sup></b> (1)<br>• Units: <b>mol<sup>&minus;1</sup> dm<sup>3</sup> s<sup>&minus;1</sup></b> (1)",
        "extra": "Can score all 3 consequential on rate equation from (a)<br>If wrong rate equation, allow units consequential",
        "mark": 3,
        "spec": "3.1.9"
    },
    "2002-june-chm4-q1c": {
        "answers": "• Appears in rate equation (or implied by mention of concentration / order) (1)<br>• Does not appear in (stoichiometric / overall) equation (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.9"
    },
    "2002-june-chm4-q1d": {
        "answers": "• pH = &minus;log<sub>10</sub>[H<sup>+</sup>] = 1.25 &rArr; [H<sup>+</sup>] = <b>0.056(2)</b> (mol dm<sup>&minus;3</sup>) (1)<br>• rate = (4.44 × 10<sup>&minus;4</sup>) × (1.50) × (0.0562) (1)<br>• = <b>3.75 × 10<sup>&minus;5</sup></b> (mol dm<sup>&minus;3</sup> s<sup>&minus;1</sup>) (1)",
        "extra": "allow 3.7 &minus; 3.8 × 10<sup>&minus;5</sup><br>can score all 3 consequential on <i>k</i> from part (b)",
        "mark": 3,
        "spec": "3.1.12"
    },
    "2002-june-chm4-q2a": {
        "answers": "<b>(1,4-)butane(ne)dioic acid</b> (1)",
        "extra": "NOT dibutanedioic / dibutanic<br>allow butane dicarboxylic / ethane dicarboxylic<br>penalise wrong numbers",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2002-june-chm4-q2b": {
        "answers": "<i>K</i><sub>c</sub> = <span style=\"font-family:serif;\">[<b>Y</b>][<b>H<sub>2</sub>O</b>]<sup>2</sup> / ([<b>X</b>][<b>CH<sub>3</sub>OH</b>]<sup>2</sup>)</span> (1)",
        "extra": "must be square brackets [ ]<br>if <i>K</i><sub>c</sub> expression wrong, lose units mark in (e) also",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2002-june-chm4-q2c": {
        "answers": "• Moles of <b>X</b> = 0.25 &minus; 0.13 = <b>0.12</b> (1)<br>• Moles of methanol = 0.34 &minus; 0.26 = <b>0.08</b> (1)<br>• Moles of water = <b>0.26</b> (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.1.10"
    },
    "2002-june-chm4-q2d": {
        "answers": "• Equal number of moles on each side of equation (1)<br><b>OR</b> <i>V</i> cancels (1)",
        "extra": "provided not incorrectly qualified",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2002-june-chm4-q2e": {
        "answers": "• <i>K</i><sub>c</sub> = <span style=\"font-family:serif;\">(0.13/<i>V</i>) × (0.26/<i>V</i>)<sup>2</sup> / [(0.12/<i>V</i>) × (0.08/<i>V</i>)<sup>2</sup>]</span> (1)<br>• = <b>11(.4)</b> (1)<br>• Units: <b>none</b> (1)",
        "extra": "Can score all 3 consequential on (b) and (c)<br>If different values from (c) used, allow units only (consequential on correct <i>K</i><sub>c</sub>)<br>Lose units mark if <i>K</i><sub>c</sub> wrong even if none given",
        "mark": 3,
        "spec": "3.1.10"
    },
    "2002-june-chm4-q2f": {
        "answers": "<b>decrease</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.1.10"
    },
    "2002-june-chm4-q3a": {
        "answers": "• Substance 1: <b>HCl</b> or <b>HBr</b> (1)<br>• Substance 2: <b>AlCl<sub>3</sub></b> / <b>AlBr<sub>3</sub></b> / <b>FeCl<sub>3</sub></b> / <b>FeBr<sub>3</sub></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.10"
    },
    "2002-june-chm4-q3b": {
        "answers": "<b>H<sub>2</sub>C=CH<sub>2</sub> + HCl + AlCl<sub>3</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub><sup>+</sup> + AlCl<sub>4</sub><sup>&minus;</sup></b> (1)",
        "extra": "allow 2 equations:<br>H<sub>2</sub>C=CH<sub>2</sub> + HCl &rarr; CH<sub>3</sub>CH<sub>2</sub>Cl<br>CH<sub>3</sub>CH<sub>2</sub>Cl + AlCl<sub>3</sub> &rarr; CH<sub>3</sub>CH<sub>2</sub><sup>+</sup> + AlCl<sub>4</sub><sup>&minus;</sup>",
        "mark": 1,
        "spec": "3.3.10"
    },
    "2002-june-chm4-q3c": {
        "answers": "• Name of mechanism: <b>electrophilic substitution</b> (1)<br>• Mechanism:<br>&nbsp;&nbsp;&ndash; Curly arrow from benzene ring to <sup>+</sup>CH<sub>2</sub>CH<sub>3</sub> (1)<br>&nbsp;&nbsp;&ndash; Correct structure of intermediate (horseshoe with + inside, pointing towards sp<sup>3</sup> C with H and CH<sub>2</sub>CH<sub>3</sub>) (1)<br>&nbsp;&nbsp;&ndash; Curly arrow from C&minus;H bond back into ring (1)",
        "extra": "horseshoe must extend over 5 carbons and open towards tetrahedral carbon; charge must be inside horseshoe",
        "mark": 4,
        "spec": "3.3.10"
    },
    "2002-june-chm4-q3d": {
        "answers": "Structure of <b>cyclohexylbenzene</b>: (C<sub>6</sub>H<sub>5</sub>&minus;C<sub>6</sub>H<sub>11</sub>) (1)<br><div style=\"margin-top:4px;\"><svg width=\"160\" height=\"55\" viewBox=\"0 0 160 55\"><polygon points=\"20,10 40,10 50,27 40,45 20,45 10,27\" fill=\"none\" stroke=\"black\" stroke-width=\"1.5\"/><circle cx=\"30\" cy=\"27\" r=\"11\" fill=\"none\" stroke=\"black\" stroke-width=\"1.5\"/><line x1=\"50\" y1=\"27\" x2=\"75\" y2=\"27\" stroke=\"black\" stroke-width=\"1.5\"/><polygon points=\"85,10 105,10 115,27 105,45 85,45 75,27\" fill=\"none\" stroke=\"black\" stroke-width=\"1.5\"/></svg></div>",
        "extra": "benzene ring directly bonded to cyclohexane ring",
        "mark": 1,
        "spec": "3.3.10"
    },
    "2002-june-chm4-q3e": {
        "answers": "• Type of polymerisation: <b>addition</b> (1)<br>• Repeating unit: <b>&minus;[CH<sub>2</sub>&minus;CH(C<sub>6</sub>H<sub>5</sub>)]&minus;</b> (1)<br><div style=\"margin-top:4px;\"><svg width=\"140\" height=\"75\" viewBox=\"0 0 140 75\"><line x1=\"10\" y1=\"18\" x2=\"100\" y2=\"18\" stroke=\"black\" stroke-width=\"1.5\"/><text x=\"18\" y=\"22\" font-family=\"Arial\" font-size=\"13\">CH</text><text x=\"38\" y=\"26\" font-family=\"Arial\" font-size=\"10\">2</text><text x=\"56\" y=\"22\" font-family=\"Arial\" font-size=\"13\">CH</text><line x1=\"66\" y1=\"25\" x2=\"66\" y2=\"36\" stroke=\"black\" stroke-width=\"1.5\"/><polygon points=\"58,38 74,38 82,49 74,60 58,60 50,49\" fill=\"none\" stroke=\"black\" stroke-width=\"1.5\"/><circle cx=\"66\" cy=\"49\" r=\"6.5\" fill=\"none\" stroke=\"black\" stroke-width=\"1.5\"/></svg></div>",
        "extra": "open bonds at ends required",
        "mark": 2,
        "spec": "3.3.12"
    },
    "2002-june-chm4-q4a": {
        "answers": "<b>2-chloropropanoic acid</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2002-june-chm4-q4b": {
        "answers": "• &delta; 1.72: <b>Doublet</b> &ndash; (adjacent / next to) <b>CH</b> (1)<br>• &delta; 4.44: <b>Quartet</b> &ndash; (adjacent / next to) <b>CH<sub>3</sub></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.3.15"
    },
    "2002-june-chm4-q4c": {
        "answers": "<b>Two triplets</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.15"
    },
    "2002-june-chm4-q4d": {
        "answers": "• Nucleophilic substitution mechanism:<br>&nbsp;&nbsp;&ndash; Curly arrow from lone pair on :NH<sub>3</sub> to C(2) (1)<br>&nbsp;&nbsp;&ndash; Curly arrow from C&minus;Cl bond to Cl (1)<br>&nbsp;&nbsp;&ndash; Correct intermediate: CH<sub>3</sub>&minus;CH(COOH)&minus;N<sup>+</sup>H<sub>3</sub> (or &minus;N<sup>+</sup>H<sub>2</sub>&minus;H) (1)<br>&nbsp;&nbsp;&ndash; Curly arrow from N&minus;H bond to N<sup>+</sup> (or attack of 2nd :NH<sub>3</sub> on H) (1)<br>• Structure of alanine: <b>CH<sub>3</sub>&minus;CH(NH<sub>2</sub>)&minus;COOH</b> (1)",
        "extra": "allow S<sub>N</sub>1 mechanism",
        "mark": 5,
        "spec": "3.3.13"
    },
    "2002-june-chm4-q4ei": {
        "answers": "Structure of product with excess aqueous HCl:<br><b>H<sub>3</sub>N<sup>+</sup>&minus;(CH<sub>2</sub>)<sub>4</sub>&minus;CH(N<sup>+</sup>H<sub>3</sub>)&minus;COOH</b> (with 2Cl<sup>&minus;</sup>) (1)",
        "extra": "both amine groups protonated; allow without Cl<sup>&minus;</sup>",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2002-june-chm4-q4eii": {
        "answers": "Structure of product with excess aqueous NaOH:<br><b>H<sub>2</sub>N&minus;(CH<sub>2</sub>)<sub>4</sub>&minus;CH(NH<sub>2</sub>)&minus;COO<sup>&minus;</sup></b> (Na<sup>+</sup>) (1)",
        "extra": "carboxylic acid group deprotonated; allow without Na<sup>+</sup>",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2002-june-chm4-q4eiii": {
        "answers": "Structure showing peptide / amide link (<b>&minus;CONH&minus;</b>): (1)<br>• e.g. <b>H<sub>2</sub>N&minus;(CH<sub>2</sub>)<sub>4</sub>&minus;CH(NH<sub>2</sub>)&minus;CO&minus;NH&minus;(CH<sub>2</sub>)<sub>4</sub>&minus;CH(NH<sub>2</sub>)&minus;COOH</b><br>• or <b>H<sub>2</sub>N&minus;CH(COOH)&minus;(CH<sub>2</sub>)<sub>4</sub>&minus;NH&minus;CO&minus;CH(NH<sub>2</sub>)&minus;(CH<sub>2</sub>)<sub>4</sub>&minus;NH<sub>2</sub></b><br>• or cyclic anhydride",
        "extra": "must clearly show the &minus;CONH&minus; link (or anhydride)",
        "mark": 1,
        "spec": "3.3.13"
    },
    "2002-june-chm4-q5a": {
        "answers": "• Structure of <b>P</b>: <b>CH<sub>3</sub>&minus;CH(CH<sub>2</sub>CH<sub>3</sub>)&minus;CH=CH<sub>2</sub></b> (or 3-methylpent-1-ene) (1)<br>• Structure of <b>Q</b>: <b>CH<sub>3</sub>&minus;CH=C(CH<sub>3</sub>)&minus;CH<sub>2</sub>CH<sub>3</sub></b> (or 3-methylpent-2-ene) (1)<br>• Structure of <b>R</b>: <b>CH<sub>3</sub>&minus;CH=CH&minus;CH(CH<sub>3</sub>)<sub>2</sub></b> (or 4-methylpent-2-ene) (1)",
        "extra": "Q and R are interchangeable<br>NOT C<sub>3</sub>H<sub>7</sub> &ndash; must show branching",
        "mark": 3,
        "spec": "3.3.1"
    },
    "2002-june-chm4-q5bi": {
        "answers": "• Racemic mixture: <b>equal mixture</b> / equimolar mixture of <b>optical isomers</b> / enantiomers (1)<br>• Explanation:<br>&nbsp;&nbsp;&ndash; <b>Planar carbonyl group</b> / C=O is planar (1)<br>&nbsp;&nbsp;&ndash; Attack from either side / above and below is <b>equally likely</b> (1)",
        "extra": "'equal mixture of' can be stated in explanation",
        "mark": 3,
        "spec": "3.3.8"
    },
    "2002-june-chm4-q5bii": {
        "answers": "• Reagent S: <b>HCN</b> OR <b>KCN / HCl</b> (or KCN / H<sub>2</sub>SO<sub>4</sub>) (1)<br>• Compound T: <b>CH<sub>3</sub>CH<sub>2</sub>&minus;C(OH)(CN)&minus;CH<sub>3</sub></b> (2-hydroxy-2-methylbutanenitrile) (1)<br>• Compound U: <b>CH<sub>3</sub>&minus;CH=C(CN)&minus;CH<sub>3</sub></b> (2-methylbut-2-enenitrile) (1)",
        "extra": "",
        "mark": 3,
        "spec": "3.3.8"
    },
    "2002-june-chm4-q6a": {
        "answers": "<b>CH<sub>3</sub>CH<sub>2</sub>&minus;COOCH<sub>2</sub>CH<sub>3</sub></b> (or CH<sub>3</sub>CH<sub>2</sub>C(=O)OCH<sub>2</sub>CH<sub>3</sub>) (1)",
        "extra": "allow &minus;COO&minus;",
        "mark": 1,
        "spec": "3.3.9"
    },
    "2002-june-chm4-q6b": {
        "answers": "• Name of mechanism: <b>(nucleophilic) addition-elimination</b> (1)<br>• Mechanism:<br>&nbsp;&nbsp;&ndash; Curly arrow from :O of ethanol to carbonyl C of propanoyl chloride (1)<br>&nbsp;&nbsp;&ndash; Curly arrow from C=O double bond to oxygen atom (1)<br>&nbsp;&nbsp;&ndash; Correct tetrahedral intermediate structure including charges: CH<sub>3</sub>CH<sub>2</sub>&minus;C(O<sup>&minus;</sup>)(Cl)&minus;O<sup>+</sup>H(CH<sub>2</sub>CH<sub>3</sub>) (1)<br>&nbsp;&nbsp;&ndash; 3 arrows: lone pair on O<sup>&minus;</sup> reforming C=O, C&minus;Cl bond breaking to form Cl<sup>&minus;</sup>, and O&minus;H bond breaking to O<sup>+</sup> (1)",
        "extra": "",
        "mark": 5,
        "spec": "3.3.9"
    },
    "2002-june-chm4-q6c": {
        "answers": "• Fragmentation equation:<br><b>CH<sub>3</sub>CH<sub>2</sub>COOCH<sub>2</sub>CH<sub>3</sub><sup>+&bull;</sup> &rarr; CH<sub>3</sub>CH<sub>2</sub>C<sup>+</sup>=O + CH<sub>3</sub>CH<sub>2</sub>O<sup>&bull;</sup></b> (1)<br>• Structure of species at <i>m/z</i> = 57: <b>CH<sub>3</sub>CH<sub>2</sub>C<sup>+</sup>=O</b> (or CH<sub>3</sub>CH<sub>2</sub>CO<sup>+</sup>) (1)",
        "extra": "equation (1), structure (1)",
        "mark": 2,
        "spec": "3.3.15"
    },
    "2002-june-chm4-q6d": {
        "answers": "<b>CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>COOCH<sub>3</sub></b> OR <b>(CH<sub>3</sub>)<sub>2</sub>CHCOOCH<sub>3</sub></b> (1)",
        "extra": "allow C<sub>3</sub>H<sub>7</sub>COOCH<sub>3</sub><br><i>m/z</i> = 71 is [C<sub>3</sub>H<sub>7</sub>CO]<sup>+</sup>",
        "mark": 1,
        "spec": "3.3.9"
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
            img_rel = q.get("markscheme", f"img/2002-june-chm4/ms_{qid.split('-')[-1]}.jpg")
            img_path = os.path.join(SCRATCH_DIR, img_rel.replace("/", os.sep))

            print(f"Generating MS for {qid} ({q_num}) -> {img_path}")
            render_official_markscheme_image(
                question_label=q_num,
                answers_html=data["answers"],
                extra_html=data["extra"],
                marks=data["mark"],
                spec_ref=data.get("spec", ""),
                output_path=img_path
            )

            clean_ans = data["answers"].replace("<br>", "\n").replace("&rarr;", "->").replace("&frac12;", "1/2").replace("&minus;", "-").replace("&le;", "<=").replace("&gt;", ">").replace("•", "-")
            clean_ext = data["extra"].replace("<br>", "\n").replace("&minus;", "-")
            q["markscheme_text"] = f"{clean_ans}\n\n[Extra Information]:\n{clean_ext}" if clean_ext else clean_ans
            updated_count += 1

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {updated_count} questions for 2002-june-chm4!")

if __name__ == "__main__":
    main()

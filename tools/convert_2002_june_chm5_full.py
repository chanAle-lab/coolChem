"""
Convert 2002-june-chm5 markschemes to official AQA modern mark scheme format.
"""
import os
import json
import sys

SCRATCH_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(SCRATCH_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QUESTIONS_FILE = os.path.join(SCRATCH_DIR, "questions.json")

MS_DATA = {
    "2002-june-chm5-q1ai": {
        "answers": "<b>Standard enthalpy change:</b><br>• &Delta;<i>H</i><sub>R</sub> = &Sigma;&Delta;<i>H</i><sub>f</sub>(products) &minus; &Sigma;&Delta;<i>H</i><sub>f</sub>(reactants) (1)<br>• &Delta;<i>H</i><sub>R</sub> = (&minus;804 &minus; 394) &minus; (&minus;940) (1)<br>• = <b>&minus;258</b> (kJ mol<sup>&minus;1</sup>; ignore units completely) (1)<br><br><b>Standard entropy change:</b><br>• &Delta;<i>S</i> = &Sigma;<i>S</i>(products) &minus; &Sigma;<i>S</i>(reactants) (1)<br>• &Delta;<i>S</i> = (252 + 214) &minus; (49.9 + 5.7 + [2 &times; 223]) (1)<br>• = <b>&minus;35.6</b> (J K<sup>&minus;1</sup> mol<sup>&minus;1</sup>; ignore units completely) (1)",
        "extra": "For &Delta;<i>H</i>: allow +258 (2 marks); formula statement worth (2) if answer wrong.<br>For &Delta;<i>S</i>: allow +35.6 (2 marks); &minus;36 AE &minus;1; allow max 1 for +187; statement worth (2) if answer wrong.",
        "mark": 6,
        "spec": "3.1.8"
    },
    "2002-june-chm5-q1aii": {
        "answers": "• <i>T</i> = &Delta;<i>H</i> / &Delta;<i>S</i> (or &Delta;<i>H</i> value / &Delta;<i>S</i> value from (a)(i)) (1)<br>• <i>T</i> = (&minus;258 &times; 1000) / (&minus;35.6) (1)<br>• = <b>7245 to 7250</b> (K) (1)",
        "extra": "penalise wrong sign in formula<br>consequential to &Delta;<i>H</i> and &Delta;<i>S</i> values from above<br>if negative temperature given max 2<br>if &deg;C used incorrectly max 2<br>ignore letter after value",
        "mark": 3,
        "spec": "3.1.8"
    },
    "2002-june-chm5-q1bi": {
        "answers": "<b>TiCl<sub>4</sub> + 4Na &rarr; 4NaCl + Ti</b><br><b>OR</b> <b>TiCl<sub>4</sub> + 2Mg &rarr; 2MgCl<sub>2</sub> + Ti</b><br>(1 mark for correct species, 1 mark for balanced)",
        "extra": "penalise (aq) by one mark<br>ignore other state symbols<br>CE if species incorrect",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q1bii": {
        "answers": "<b>Any one from:</b><br>• Ti reacts with oxygen / air <b>OR</b> Ti is oxidised / an oxide formed (allow any oxide) (1)<br>• Ti reacts with nitrogen <b>OR</b> nitride formed (allow formula of any nitride) (1)<br>• Na or Mg reacts with oxygen, nitrogen or air (1)",
        "extra": "do not allow hydrolysis<br>penalise if other products given, e.g. carbide",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q1c": {
        "answers": "<b>TiCl<sub>4</sub> + 2H<sub>2</sub>O &rarr; TiO<sub>2</sub> + 4HCl</b> (1)",
        "extra": "ignore state symbols<br>allow Ti(OH)<sub>4</sub> when 4H<sub>2</sub>O used<br>or Ti(OH)<sub>4</sub>(H<sub>2</sub>O)<sub>2</sub> when 6H<sub>2</sub>O used<br>or TiO<sub>2</sub>&middot;<i>x</i>H<sub>2</sub>O where <i>x</i> &le; 6, but must be balanced",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q2a": {
        "answers": "• Cell e.m.f.: <b>1.93 (V)</b> (1)<br>• Half-equation: <b>Mg &rarr; Mg<sup>2+</sup> + 2e<sup>&minus;</sup></b> (or &rightleftharpoons;) (1)",
        "extra": "CE if a negative value given for e.m.f.<br>ignore state symbols<br>mark on after an AE",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2002-june-chm5-q2b": {
        "answers": "• Change in e.m.f.: <b>Increases</b> (1)<br>• Explanation:<br>&nbsp;&nbsp;&ndash; Equilibrium displaced to Mg<sup>2+</sup> / to the left (or cell / overall reaction goes to right) (1)<br>&nbsp;&nbsp;&ndash; Electrode is more negative <b>OR</b> <i>E</i> decreases / gives more electrons / forms more Mg<sup>2+</sup> ions (1)",
        "extra": "mark on even if direction incorrect<br>mark points separately",
        "mark": 3,
        "spec": "3.1.11"
    },
    "2002-june-chm5-q2c": {
        "answers": "• Cell e.m.f.: <b>&minus;0.84 (V)</b> (1)<br>• Explanation: <b>Fe gives electrons</b> OR <b>forms Fe<sup>2+</sup></b> OR <b>reaction goes in reverse direction</b> (1)",
        "extra": "CE if positive value given for e.m.f.<br>mark on after an AE<br>NB in (a) and (c) mark on if no value given, but CE if emf = 0",
        "mark": 2,
        "spec": "3.1.11"
    },
    "2002-june-chm5-q3a": {
        "answers": "• (Electrons excited /) <b>Electron transitions in d shell / d-d transition</b> (1)<br>• (Energy absorbed in) <b>visible range</b> (1)",
        "extra": "do not allow charge transfer<br>do not accept 'emits in visible region'",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q3b": {
        "answers": "• Change 1: (Different) <b>oxidation states</b> (1)<br>• Change 2: (Different) <b>ligands</b> (1)<br>• Change 3: (Different) <b>co-ordination number</b> (1)",
        "extra": "do not allow 'shape' as an answer",
        "mark": 3,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q3c": {
        "answers": "• Add an appropriate (or given correct) ligand to intensify colour [e.g. thiocyanate (CNS<sup>&minus;</sup>) or bipyridyl] (1)<br>• Make up solutions of known concentration (1)<br>• Measure absorption(s) OR transmission (1)<br>• Plot graph of results OR calibration curve (1)<br>• Measure absorption of unknown and compare / read concentration from curve (1)",
        "extra": "Allow concentration statement if included in graph statement<br>allow adsorption but circle d<br>sketch graph of Absorption vs Concentration scores 3 marks",
        "mark": 5,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q4a": {
        "answers": "• Species: <b>[Ag(NH<sub>3</sub>)<sub>2</sub>]<sup>+</sup></b> (1)<br>• Shape: <b>Linear</b> (1)<br>• Use: To distinguish between (or identify) <b>aldehydes and ketones</b> OR <b>Tollens' reagent</b> OR in <b>silver mirror test</b> (1)",
        "extra": "allow name for species but penalise contradictions<br>mark species, shape and use separately",
        "mark": 3,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q4bi": {
        "answers": "• Precipitate B: <b>AgBr</b> (or silver bromide) (1)<br>• Silver-containing species in C: <b>[Ag(S<sub>2</sub>O<sub>3</sub>)<sub>2</sub>]<sup>3&minus;</sup></b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q4bii": {
        "answers": "• Equation: <b>AgBr + 2S<sub>2</sub>O<sub>3</sub><sup>2&minus;</sup> &rarr; [Ag(S<sub>2</sub>O<sub>3</sub>)<sub>2</sub>]<sup>3&minus;</sup> + Br<sup>&minus;</sup></b> (1)<br>• Explanation: <b>Removes AgBr</b> (or Ag<sup>+</sup>) OR <b>\"fixer\"</b> OR <b>prevents AgX darkening / reacting with light</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q4c": {
        "answers": "• Species: <b>[Ag(CN)<sub>2</sub>]<sup>&minus;</sup></b> (1)<br>• Use: <b>Electroplating</b> (1)",
        "extra": "mark use separately",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q4d": {
        "answers": "<b>It has a full d shell</b> OR <b>does not have a partially filled d shell</b> (1)",
        "extra": "ignore 3d / 4d stated<br>NOT 'it has a full outer shell'",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q5ai": {
        "answers": "<b>[Cr(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> + H<sub>2</sub>O &rarr; [Cr(H<sub>2</sub>O)<sub>5</sub>(OH)]<sup>2+</sup> + H<sub>3</sub>O<sup>+</sup></b><br><b>OR</b> <b>[Cr(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> &rarr; [Cr(H<sub>2</sub>O)<sub>5</sub>(OH)]<sup>2+</sup> + H<sup>+</sup></b> (1)",
        "extra": "allow loss of up to 2H<sup>+</sup><br>do NOT allow reactions with bases other than water",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q5aii": {
        "answers": "<b>Any two from:</b><br>• Cr<sup>3+</sup> is smaller than Cr<sup>2+</sup> <b>OR</b> Cr<sup>3+</sup> has a greater charge density / greater charge-to-size ratio / surface density of charge (1)<br>• Cr<sup>3+</sup> is more polarising (or draws electron density from oxygen) (1)<br>• O&minus;H bonds weakened / break more easily (1)",
        "extra": "Max 2 from 3",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q5bi": {
        "answers": "<b>Cr(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub></b> <b>OR</b> <b>Cr(OH)<sub>3</sub></b> <b>OR</b> <b>Cr(OH)<sub>3</sub>&middot;<i>x</i>H<sub>2</sub>O</b> (where <i>x</i> = 1, 2 or 3)<br><b>OR</b> name: <b>chromium(III) hydroxide</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q5bii": {
        "answers": "<b>Base</b> <b>OR</b> <b>electron pair donor</b> <b>OR</b> <b>proton acceptor</b> (1)",
        "extra": "NOT alkali; ignore nucleophile but penalise 'ligand'",
        "mark": 1,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q5biii": {
        "answers": "• Gas evolved: <b>CO<sub>2</sub></b> (or carbon dioxide) (1)<br>• Equation: <b>3CO<sub>3</sub><sup>2&minus;</sup> + 2[Cr(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> &rarr; 2[Cr(H<sub>2</sub>O)<sub>3</sub>(OH)<sub>3</sub>] + 3CO<sub>2</sub> + 3H<sub>2</sub>O</b> (1)",
        "extra": "If separate equations for CO<sub>3</sub><sup>2&minus;</sup> and Cr<sup>3+</sup>(aq) given, an overall equation must be deduced",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q5c": {
        "answers": "• <b>H<sub>2</sub>O<sub>2</sub> + NaOH</b> (or KOH) (scores 2 marks)<br>• <i>Alternative:</i> <b>Na<sub>2</sub>O<sub>2</sub></b> (scores 2 marks)<br>• H<sub>2</sub>O<sub>2</sub> alone or with anything else (scores 1 mark)",
        "extra": "NaOH alone scores 0<br>Do not allow 'alkaline' or OH<sup>&minus;</sup> or NH<sub>3</sub>",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q6a": {
        "answers": "• <b>A shared electron pair</b> OR covalent bond (1)<br>• <b>Both electrons from one atom</b> OR when a Lewis base reacts with a Lewis acid (1)",
        "extra": "mark points separately",
        "mark": 2,
        "spec": "3.1.3"
    },
    "2002-june-chm5-q6b": {
        "answers": "• Br&oslash;nsted&ndash;Lowry acid: <b>A proton OR H<sup>+</sup> donor</b> (1) (NOT H<sub>3</sub>O<sup>+</sup>)<br>• Lewis acid: <b>A lone OR electron pair acceptor</b> (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.1.12"
    },
    "2002-june-chm5-q6c": {
        "answers": "• <b>Two atoms</b> OR <b>two points of attachment</b> (1)<br>• <b>Each donating a lone electron pair</b> OR forms 2 co-ordinate bonds OR donates two pairs of electrons (1)",
        "extra": "",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q6d": {
        "answers": "• Change in co-ordination number: <b>6 to 4</b> (1)<br>• Reason for change: <b>Chloride ligands are larger than water ligands</b> OR <b>greater repulsion between chloride ligands</b> (1)",
        "extra": "do not allow 'chlorine' or 'Cl'",
        "mark": 2,
        "spec": "3.2.5"
    },
    "2002-june-chm5-q6e": {
        "answers": "• <b>Same number</b> (1)<br>• and <b>same type of bonds</b> (1)<br>broken and made",
        "extra": "1 mark for same number of bonds, 1 mark for same type of bonds",
        "mark": 2,
        "spec": "3.1.8"
    },
    "2002-june-chm5-q6f": {
        "answers": "<b>Cl<sup>&minus;</sup> H<sub>3</sub>N<sup>+</sup>CH<sub>2</sub>CH<sub>2</sub>N<sup>+</sup>H<sub>3</sub> Cl<sup>&minus;</sup></b><br><b>OR</b> <b>(NH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>3</sub>)<sup>2+</sup> 2Cl<sup>&minus;</sup></b><br><b>OR</b> <b>C<sub>2</sub>H<sub>10</sub>N<sub>2</sub>Cl<sub>2</sub></b><br><b>OR</b> <b>NH<sub>3</sub>Cl CH<sub>2</sub>CH<sub>2</sub> NH<sub>3</sub>Cl</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.11"
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
            img_rel = q.get("markscheme", f"img/2002-june-chm5/ms_{qid.split('-')[-1]}.jpg")
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

    print(f"Successfully updated {updated_count} questions for 2002-june-chm5!")

if __name__ == "__main__":
    main()

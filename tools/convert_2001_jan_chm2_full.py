import os
import json
from generate_official_markscheme import render_official_markscheme_image

repo = "C:/Users/Alexander/.gemini/antigravity/scratch/coolChem"
out_dir = os.path.join(repo, "img/2001-jan-chm2")

items = [
    # Q1
    {
        "id": "2001-jan-chm2-q1a",
        "sub_id": "q1a",
        "lbl": "1(a)",
        "ans": "<b>decreases</b> (down group / from chlorine to iodine) (1)",
        "extra": "<p>allow: Cl<sub>2</sub> &gt; Br<sub>2</sub> &gt; I<sub>2</sub></p>",
        "marks": 1,
        "spec": "3.2.3"
    },
    {
        "id": "2001-jan-chm2-q1b",
        "sub_id": "q1b",
        "lbl": "1(b)",
        "ans": "• <b>KCl:</b> yellow solution / no reaction (1)<br>• <b>KI:</b> brown solution / black precipitate (1)<br>• <b>Ionic equation:</b> 2I<sup>-</sup> + Br<sub>2</sub> &rarr; 2Br<sup>-</sup> + I<sub>2</sub> (1)",
        "extra": "<p>allow: orange / reddish solution for KCl</p><p>allow: purple / brown for KI</p>",
        "marks": 3,
        "spec": "3.2.3"
    },
    {
        "id": "2001-jan-chm2-q1ci",
        "sub_id": "q1ci",
        "lbl": "1(c)(i)",
        "ans": "<b>Cl<sub>2</sub></b> (1)",
        "extra": "<p>allow: chlorine / Cl<sub>2</sub>(aq)</p>",
        "marks": 1,
        "spec": "3.2.3"
    },
    {
        "id": "2001-jan-chm2-q1cii",
        "sub_id": "q1cii",
        "lbl": "1(c)(ii)",
        "ans": "<b>Cl<sub>2</sub> + H<sub>2</sub>O &rightleftharpoons; HCl + HClO</b> (1)",
        "extra": "<p>allow: &rarr; instead of &rightleftharpoons;</p><p>allow: H<sup>+</sup> + Cl<sup>-</sup> + HClO</p>",
        "marks": 1,
        "spec": "3.2.3"
    },
    {
        "id": "2001-jan-chm2-q1ciii",
        "sub_id": "q1ciii",
        "lbl": "1(c)(iii)",
        "ans": "• <b>Red colour:</b> due to presence of acid / H<sup>+</sup> ions (1)<br>• <b>White:</b> due to bleaching by HClO / chloric(I) acid (1)",
        "extra": "<p>allow: ClO<sup>-</sup> for bleaching agent</p>",
        "marks": 2,
        "spec": "3.2.3"
    },
    {
        "id": "2001-jan-chm2-q1d",
        "sub_id": "q1d",
        "lbl": "1(d)",
        "ans": "<b>2NaOH + Cl<sub>2</sub> &rarr; NaCl + NaClO + H<sub>2</sub>O</b> (1)",
        "extra": "<p>allow ionic equation:<br>2OH<sup>-</sup> + Cl<sub>2</sub> &rarr; Cl<sup>-</sup> + ClO<sup>-</sup> + H<sub>2</sub>O</p>",
        "marks": 1,
        "spec": "3.2.3"
    },

    # Q2
    {
        "id": "2001-jan-chm2-q2ai",
        "sub_id": "q2ai",
        "lbl": "2(a)(i)",
        "ans": "<b>loss</b> of electron(s) (1)",
        "extra": "<p>do <b>not</b> accept: gain of oxygen without electron mention</p>",
        "marks": 1,
        "spec": "3.1.7"
    },
    {
        "id": "2001-jan-chm2-q2aii",
        "sub_id": "q2aii",
        "lbl": "2(a)(ii)",
        "ans": "<b>+1</b> (1)",
        "extra": "<p>allow: 1 or 1+ or +I</p>",
        "marks": 1,
        "spec": "3.1.7"
    },
    {
        "id": "2001-jan-chm2-q2b",
        "sub_id": "q2b",
        "lbl": "2(b)",
        "ans": "<b>2S<sub>2</sub>O<sub>3</sub><sup>2-</sup> + I<sub>2</sub> &rarr; S<sub>4</sub>O<sub>6</sub><sup>2-</sup> + 2I<sup>-</sup></b><br><br>• correct species (1)<br>• correctly balanced (1)",
        "extra": "<p>allow full equation with sodium salts:<br>2Na<sub>2</sub>S<sub>2</sub>O<sub>3</sub> + I<sub>2</sub> &rarr; Na<sub>2</sub>S<sub>4</sub>O<sub>6</sub> + 2NaI</p>",
        "marks": 2,
        "spec": "3.1.7"
    },
    {
        "id": "2001-jan-chm2-q2ci",
        "sub_id": "q2ci",
        "lbl": "2(c)(i)",
        "ans": "• moles = 0.100 &times; (24.4 / 1000) (1)<br>• = <b>2.44 &times; 10<sup>-3</sup></b> (mol)",
        "extra": "<p>allow: 0.00244 mol</p>",
        "marks": 1,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm2-q2cii",
        "sub_id": "q2cii",
        "lbl": "2(c)(ii)",
        "ans": "• moles of I<sub>2</sub> = 2.44 &times; 10<sup>-3</sup> / 2 (1)<br>• = <b>1.22 &times; 10<sup>-3</sup></b> (mol)",
        "extra": "<p>consequential on 2(c)(i) &divide; 2</p>",
        "marks": 1,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm2-q2ciii",
        "sub_id": "q2ciii",
        "lbl": "2(c)(iii)",
        "ans": "<b>ClO<sup>-</sup> + 2I<sup>-</sup> + 2H<sup>+</sup> &rarr; Cl<sup>-</sup> + I<sub>2</sub> + H<sub>2</sub>O</b><br><br>• correct species (1)<br>• correctly balanced (1)",
        "extra": "<p>allow: full equation</p>",
        "marks": 2,
        "spec": "3.1.7"
    },
    {
        "id": "2001-jan-chm2-q2civ",
        "sub_id": "q2civ",
        "lbl": "2(c)(iv)",
        "ans": "• moles of ClO<sup>-</sup> in 25 cm<sup>3</sup> = 1.22 &times; 10<sup>-3</sup> (1)<br>• concentration = (1.22 &times; 10<sup>-3</sup> &times; 1000) / 25.0 (1)<br>• = <b>0.0488</b> mol dm<sup>-3</sup> (1)",
        "extra": "<p>allow: 0.049 mol dm<sup>-3</sup></p><p>consequential marking from (c)(ii)</p>",
        "marks": 3,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm2-q2cv",
        "sub_id": "q2cv",
        "lbl": "2(c)(v)",
        "ans": "• <b>Indicator:</b> starch (1)<br>• <b>Colour change:</b> blue(-black) to colourless (1)",
        "extra": "<p>do <b>not</b> accept: clear for colourless</p>",
        "marks": 2,
        "spec": "3.1.2"
    },

    # Q3
    {
        "id": "2001-jan-chm2-q3a",
        "sub_id": "q3a",
        "lbl": "3(a)",
        "ans": "<i>Standard enthalpy of formation:</i><br>• enthalpy change when <b>one mole</b> of a compound (1)<br>• is formed from its constituent <b>elements</b> (1)<br>• with all substances in their standard states under standard conditions (1)<br><br><i>Standard enthalpy of combustion:</i><br>• enthalpy change when <b>one mole</b> of a substance (1)<br>• is <b>completely burned</b> in oxygen (1)<br>• under standard conditions (298 K, 100 kPa) (1)",
        "extra": "<p>allow: standard state conditions of 100 kPa and 298 K</p>",
        "marks": 6,
        "spec": "3.1.4"
    },
    {
        "id": "2001-jan-chm2-q3b",
        "sub_id": "q3b",
        "lbl": "3(b)",
        "ans": "• &Delta;<i>H</i> = &Sigma;&Delta;<i>H</i><sub>f</sub>(products) &minus; &Sigma;&Delta;<i>H</i><sub>f</sub>(reactants) (1)<br>• = [3(&minus;394) + 4(&minus;286)] &minus; [&minus;304] (1)<br>• = <b>&minus;2022 kJ mol<sup>-1</sup></b> (1)",
        "extra": "<p>correct answer with negative sign scores 3 marks</p><p>allow +2022 for 2 marks</p>",
        "marks": 3,
        "spec": "3.1.4"
    },
    {
        "id": "2001-jan-chm2-q3ci",
        "sub_id": "q3ci",
        "lbl": "3(c)(i)",
        "ans": "• <i>q</i> = <i>mc</i>&Delta;<i>T</i> = 200 &times; 4.2 &times; 15 (1)<br>• = <b>12.6 kJ</b> (or <b>12600 J</b>) (1)",
        "extra": "<p>allow: 12.6 without unit if working shown</p>",
        "marks": 2,
        "spec": "3.1.4"
    },
    {
        "id": "2001-jan-chm2-q3cii",
        "sub_id": "q3cii",
        "lbl": "3(c)(ii)",
        "ans": "• moles of C<sub>3</sub>H<sub>7</sub>OH = 0.90 / 60.0 (1)<br>• = <b>0.015</b> (mol) (1)",
        "extra": "<p>allow: 0.0150 mol</p>",
        "marks": 2,
        "spec": "3.1.4"
    },
    {
        "id": "2001-jan-chm2-q3ciii",
        "sub_id": "q3ciii",
        "lbl": "3(c)(iii)",
        "ans": "• &Delta;<i>H</i><sub>c</sub> = &minus;12.6 / 0.015 (1)<br>• = <b>&minus;840 kJ mol<sup>-1</sup></b> (1)",
        "extra": "<p>negative sign required for second mark</p><p>consequential from 3(c)(i) &divide; 3(c)(ii)</p>",
        "marks": 2,
        "spec": "3.1.4"
    },
    {
        "id": "2001-jan-chm2-q3civ",
        "sub_id": "q3civ",
        "lbl": "3(c)(iv)",
        "ans": "any <b>two</b> from:<br>• heat loss to surroundings / air / calorimeter (1)<br>• incomplete combustion (1)<br>• heat capacity of the calorimeter not included (1)<br>• evaporation of alcohol from wick (1)",
        "extra": "<p>allow: experiment not done under standard conditions</p>",
        "marks": 2,
        "spec": "3.1.4"
    },

    # Q4
    {
        "id": "2001-jan-chm2-q4ai",
        "sub_id": "q4ai",
        "lbl": "4(a)(i)",
        "ans": "• <b>Stage 1:</b> C + O<sub>2</sub> &rarr; CO<sub>2</sub> (1)<br>• <b>Stage 2:</b> CO<sub>2</sub> + C &rarr; 2CO (1)",
        "extra": "<p>allow: 2C + O<sub>2</sub> &rarr; 2CO for 1 mark if neither 2-stage given</p>",
        "marks": 2,
        "spec": "3.2.1"
    },
    {
        "id": "2001-jan-chm2-q4aii",
        "sub_id": "q4aii",
        "lbl": "4(a)(ii)",
        "ans": "• <b>By carbon:</b> Fe<sub>2</sub>O<sub>3</sub> + 3C &rarr; 2Fe + 3CO (1)<br>&nbsp;&nbsp;<i>(or 2Fe<sub>2</sub>O<sub>3</sub> + 3C &rarr; 4Fe + 3CO<sub>2</sub>)</i><br>• <b>By CO:</b> Fe<sub>2</sub>O<sub>3</sub> + 3CO &rarr; 2Fe + 3CO<sub>2</sub> (1)",
        "extra": "<p>equations must be correctly balanced</p>",
        "marks": 2,
        "spec": "3.2.1"
    },
    {
        "id": "2001-jan-chm2-q4aiii",
        "sub_id": "q4aiii",
        "lbl": "4(a)(iii)",
        "ans": "• <b>Impurity:</b> SiO<sub>2</sub> / silicon dioxide / sand (1)<br>• CaCO<sub>3</sub> &rarr; CaO + CO<sub>2</sub> (1)<br>• CaO + SiO<sub>2</sub> &rarr; CaSiO<sub>3</sub> (1)",
        "extra": "<p>allow: CaCO<sub>3</sub> + SiO<sub>2</sub> &rarr; CaSiO<sub>3</sub> + CO<sub>2</sub> (scores both equation marks)</p>",
        "marks": 3,
        "spec": "3.2.1"
    },
    {
        "id": "2001-jan-chm2-q4b",
        "sub_id": "q4b",
        "lbl": "4(b)",
        "ans": "• <b>Main impurity:</b> carbon (1)<br>• <b>Explanation:</b> oxygen blown / injected into molten iron (1)<br>• carbon oxidised to CO / CO<sub>2</sub> (gases escape) (1)",
        "extra": "<p>allow: basic oxygen process</p>",
        "marks": 3,
        "spec": "3.2.1"
    },
    {
        "id": "2001-jan-chm2-q4c",
        "sub_id": "q4c",
        "lbl": "4(c)",
        "ans": "• <b>Gas:</b> CO<sub>2</sub> / carbon dioxide (1)<br>• <b>Environmental problem:</b> global warming / greenhouse effect (1)<br><br><i>OR</i><br><br>• <b>Gas:</b> CO / carbon monoxide (1)<br>• <b>Environmental problem:</b> toxic / poisonous (1)",
        "extra": "<p>environmental problem must match named gas</p>",
        "marks": 2,
        "spec": "3.2.1"
    },
    {
        "id": "2001-jan-chm2-q4d",
        "sub_id": "q4d",
        "lbl": "4(d)",
        "ans": "• <b>Gas:</b> SO<sub>2</sub> / sulfur dioxide (1)<br>• <b>Environmental problem:</b> acid rain (1)",
        "extra": "<p>allow: respiratory problems</p>",
        "marks": 2,
        "spec": "3.2.1"
    },

    # Q5
    {
        "id": "2001-jan-chm2-q5a",
        "sub_id": "q5a",
        "lbl": "5(a)",
        "ans": "<b>TiO<sub>2</sub> + 2C + 2Cl<sub>2</sub> &rarr; TiCl<sub>4</sub> + 2CO</b><br><br>• correct species (1)<br>• correctly balanced (1)",
        "extra": "<p>allow: TiO<sub>2</sub> + C + 2Cl<sub>2</sub> &rarr; TiCl<sub>4</sub> + CO<sub>2</sub></p>",
        "marks": 2,
        "spec": "3.2.1"
    },
    {
        "id": "2001-jan-chm2-q5b",
        "sub_id": "q5b",
        "lbl": "5(b)",
        "ans": "• <b>Reducing agent:</b> Na or Mg (1)<br>• <b>Conditions:</b> high temperature / heat (1)<br>• argon atmosphere / inert atmosphere (1)<br>• <b>Equation:</b> TiCl<sub>4</sub> + 4Na &rarr; Ti + 4NaCl (1)<br>&nbsp;&nbsp;<i>(or TiCl<sub>4</sub> + 2Mg &rarr; Ti + 2MgCl<sub>2</sub>)</i>",
        "extra": "<p>equation must match chosen reducing agent</p>",
        "marks": 4,
        "spec": "3.2.1"
    },
    {
        "id": "2001-jan-chm2-q5c",
        "sub_id": "q5c",
        "lbl": "5(c)",
        "ans": "<b>titanium carbide</b> is formed (1)",
        "extra": "<p>allow: TiC formed</p><p>allow: makes the titanium brittle</p>",
        "marks": 1,
        "spec": "3.2.1"
    }
]

# 1. Render all official tables
for item in items:
    out_path = os.path.join(out_dir, f"ms_{item['sub_id']}.jpg")
    render_official_markscheme_image(
        question_label=item['lbl'],
        answers_html=item['ans'],
        extra_html=item['extra'],
        marks=item['marks'],
        spec_ref=item['spec'],
        output_path=out_path
    )
    print(f"Rendered: {item['id']} -> {out_path}")

# 2. Update questions.json with text
q_json_path = os.path.join(repo, "questions.json")
with open(q_json_path, "r", encoding="utf-8") as f:
    db = json.load(f)

item_map = {item["id"]: item for item in items}
updated_count = 0
for q in db["questions"]:
    if q["id"] in item_map:
        it = item_map[q["id"]]
        text_clean = it["ans"].replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("&rarr;", "->").replace("&rightleftharpoons;", "<=>").replace("&minus;", "-").replace("&Sigma;", "sum ").replace("&Delta;", "delta ").replace("&times;", "x").replace("<sup>", "^").replace("</sup>", "").replace("<sub>", "_").replace("</sub>", "").replace("&nbsp;", " ").replace("<i>", "").replace("</i>", "")
        q["markscheme_text"] = text_clean
        updated_count += 1

with open(q_json_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {updated_count} questions for 2001-jan-chm2 in questions.json!")

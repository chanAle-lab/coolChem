import os
import json
from generate_official_markscheme import render_official_markscheme_image

repo = "C:/Users/Alexander/.gemini/antigravity/scratch/coolChem"
out_dir = os.path.join(repo, "img/2001-june-chm2")

items = [
    # Q1
    {
        "id": "2001-june-chm2-q1a",
        "sub_id": "q1a",
        "lbl": "1(a)",
        "ans": "• enthalpy change / heat change when <b>one mole</b> (of a substance) (1)<br>• is <b>completely burned</b> in oxygen (1)<br>• under <b>standard conditions</b> (100 kPa and 298 K) (1)",
        "extra": "<p>penalise first mark if heat absorbed or just 'energy change'</p>",
        "marks": 3,
        "spec": "3.1.4"
    },
    {
        "id": "2001-june-chm2-q1b",
        "sub_id": "q1b",
        "lbl": "1(b)",
        "ans": "• &Delta;<i>H</i> = &Sigma;&Delta;<i>H</i><sub>f</sub>(products) &minus; &Sigma;&Delta;<i>H</i><sub>f</sub>(reactants) (1)<br>&nbsp;&nbsp;= &Delta;<i>H</i><sub>f</sub>(CO<sub>2</sub>) + 2&Delta;<i>H</i><sub>f</sub>(H<sub>2</sub>O) &minus; &Delta;<i>H</i><sub>f</sub>(CH<sub>4</sub>)<br>• = (&minus;394) + 2(&minus;286) &minus; (&minus;75) (1)<br>• = <b>&minus;891 kJ mol<sup>-1</sup></b> (1)",
        "extra": "<p>allow: +891 scores max 1</p>",
        "marks": 3,
        "spec": "3.1.4"
    },
    {
        "id": "2001-june-chm2-q1ci",
        "sub_id": "q1ci",
        "lbl": "1(c)(i)",
        "ans": "• enthalpy required to <b>break a covalent bond</b> (1)<br>• <b>averaged</b> over many compounds (1)",
        "extra": "<p>do <b>not</b> allow energy instead of enthalpy for mark 1</p>",
        "marks": 2,
        "spec": "3.1.4"
    },
    {
        "id": "2001-june-chm2-q1cii",
        "sub_id": "q1cii",
        "lbl": "1(c)(ii)",
        "ans": "• 4 &times; <i>BE</i>(C&minus;H) = 715 + 2(436) &minus; (&minus;75) = 1662 (1)<br>• <i>BE</i>(C&minus;H) = 1662 / 4 = <b>+415.5 kJ mol<sup>-1</sup></b> (1)",
        "extra": "<p>allow: 415 &ndash; 416</p><p>allow: &minus;415.5 scores max 1</p>",
        "marks": 2,
        "spec": "3.1.4"
    },
    {
        "id": "2001-june-chm2-q1ciii",
        "sub_id": "q1ciii",
        "lbl": "1(c)(iii)",
        "ans": "• 4020 = 2 &times; <i>BE</i>(C&minus;C) + 8 &times; <i>BE</i>(C&minus;H) (1)<br>• <i>BE</i>(C&minus;C) = [4020 &minus; 8(415.5)] / 2 (1)<br>• = <b>+348 kJ mol<sup>-1</sup></b> (1)",
        "extra": "<p>allow: 346 &ndash; 350</p><p>allow consequential marking from (c)(ii): if 390 used, <i>BE</i>(C&minus;C) = 450 (2 marks)</p>",
        "marks": 3,
        "spec": "3.1.4"
    },

    # Q2
    {
        "id": "2001-june-chm2-q2a",
        "sub_id": "q2a",
        "lbl": "2(a)",
        "ans": "<b>H<sup>+</sup> + OH<sup>-</sup> &rarr; H<sub>2</sub>O</b> (1)",
        "extra": "<p>allow: H<sub>3</sub>O<sup>+</sup> + OH<sup>-</sup> &rarr; 2H<sub>2</sub>O</p><p>ignore state symbols; ignore spectator ions</p>",
        "marks": 1,
        "spec": "3.1.4"
    },
    {
        "id": "2001-june-chm2-q2b",
        "sub_id": "q2b",
        "lbl": "2(b)",
        "ans": "• moles of H<sup>+</sup> = (50.0 &times; 1.00) / 1000<br>• = <b>0.050 mol</b> (or 5.0 &times; 10<sup>-2</sup>) (1)",
        "extra": "<p>allow: 0.05 mol</p>",
        "marks": 1,
        "spec": "3.1.4"
    },
    {
        "id": "2001-june-chm2-q2c",
        "sub_id": "q2c",
        "lbl": "2(c)",
        "ans": "• <i>q</i> = <i>mc</i>&Delta;<i>T</i> = 100 &times; 4.18 &times; 6.5 (1)<br>• = <b>2717 J</b> (or <b>2.717 kJ</b>) (1)",
        "extra": "<p>allow: 2700 &ndash; 2717 J (or 2.7 &ndash; 2.717 kJ)</p><p>allow: 2730 J if 4.2 used for c</p>",
        "marks": 2,
        "spec": "3.1.4"
    },
    {
        "id": "2001-june-chm2-q2d",
        "sub_id": "q2d",
        "lbl": "2(d)",
        "ans": "• &Delta;<i>H</i> = &minus;2.717 / 0.050 (1)<br>• = <b>&minus;54.3 kJ mol<sup>-1</sup></b> (1)",
        "extra": "<p>negative sign required</p><p>allow consequential marking on (b) and (c)</p>",
        "marks": 2,
        "spec": "3.1.4"
    },

    # Q3
    {
        "id": "2001-june-chm2-q3a",
        "sub_id": "q3a",
        "lbl": "3(a)",
        "ans": "• <b>Rate of reaction:</b> change in concentration (1) per unit time (or per second / per minute) (1)<br>• <b>Activation energy:</b> minimum energy (1) required for a reaction to occur / for successful collisions (1)",
        "extra": "<p>allow: 1 / time for rate (scores 1 mark)</p>",
        "marks": 4,
        "spec": "3.1.5"
    },
    {
        "id": "2001-june-chm2-q3bi",
        "sub_id": "q3bi",
        "lbl": "3(b)(i)",
        "ans": "<i>Sketch of curve at higher temperature:</i><br>• peak lower and shifted to the right (1)<br>• curve crosses once only and stays above original curve at high energy (1)",
        "extra": "<p>penalise curves that do not start at the origin or that cross more than once</p>",
        "marks": 2,
        "spec": "3.1.5"
    },
    {
        "id": "2001-june-chm2-q3bii",
        "sub_id": "q3bii",
        "lbl": "3(b)(ii)",
        "ans": "• <b>Effect:</b> (rate of reaction) <b>increases</b> (1)<br>• <b>Explanation:</b> many more molecules / particles (1)<br>• have energy &ge; <i>E</i><sub>a</sub> / have activation energy (1)",
        "extra": "<p>allow: greater frequency of successful collisions</p><p>mark CE if incorrect effect given</p>",
        "marks": 3,
        "spec": "3.1.5"
    },
    {
        "id": "2001-june-chm2-q3biii",
        "sub_id": "q3biii",
        "lbl": "3(b)(iii)",
        "ans": "• <b>Effect:</b> (rate of reaction) <b>increases</b> (1)<br>• <b>Explanation:</b> catalyst provides an <b>alternative reaction route / mechanism</b> (1)<br>• with a <b>lower activation energy</b> (1)<br>• so more molecules have enough energy to react / have energy &ge; <i>E</i><sub>a</sub> (1)",
        "extra": "<p>if effect incorrect, allow max 2 for alternative route with lower Ea</p>",
        "marks": 4,
        "spec": "3.1.5"
    },

    # Q4
    {
        "id": "2001-june-chm2-q4ai",
        "sub_id": "q4ai",
        "lbl": "4(a)(i)",
        "ans": "all reactants and products are in the <b>same phase / state</b> (or are all gases) (1)",
        "extra": "<p>allow: all species in single phase</p>",
        "marks": 1,
        "spec": "3.1.6"
    },
    {
        "id": "2001-june-chm2-q4aii",
        "sub_id": "q4aii",
        "lbl": "4(a)(ii)",
        "ans": "• forward and reverse reactions proceed at <b>equal rates</b> (1)<br>• <b>concentrations</b> of reactants and products remain constant (1)",
        "extra": "<p>do <b>not</b> accept: concentrations are equal</p>",
        "marks": 2,
        "spec": "3.1.6"
    },
    {
        "id": "2001-june-chm2-q4bi",
        "sub_id": "q4bi",
        "lbl": "4(b)(i)",
        "ans": "• <b>Effect:</b> (concentration of hydrogen) <b>increases</b> (1)<br>• <b>Explanation:</b> equilibrium shifts to the <b>right</b> / forward reaction favoured (1)<br>• to oppose the addition of steam / remove added water (1)",
        "extra": "<p>do not allow rate answers</p>",
        "marks": 3,
        "spec": "3.1.6"
    },
    {
        "id": "2001-june-chm2-q4bii",
        "sub_id": "q4bii",
        "lbl": "4(b)(ii)",
        "ans": "• <b>Effect:</b> (concentration of hydrogen) <b>increases</b> (1)<br>• <b>Explanation:</b> equilibrium shifts to the <b>right</b> / forward reaction favoured (1)<br>• forward reaction is <b>exothermic</b> / produces heat to oppose temperature decrease (1)",
        "extra": "<p>allow max 1 for exothermic if other answers incorrect</p>",
        "marks": 3,
        "spec": "3.1.6"
    },
    {
        "id": "2001-june-chm2-q4c",
        "sub_id": "q4c",
        "lbl": "4(c)",
        "ans": "• <b>Effect:</b> <b>none</b> / no effect (1)<br>• <b>Explanation:</b> rates of forward and reverse reactions (1)<br>• are increased by the <b>same amount / equally</b> (1)",
        "extra": "<p>allow: activation energy of both forward and reverse reactions lowered by same amount</p>",
        "marks": 3,
        "spec": "3.1.6"
    },

    # Q5
    {
        "id": "2001-june-chm2-q5a",
        "sub_id": "q5a",
        "lbl": "5(a)",
        "ans": "<b>gain</b> of electron(s) (1)",
        "extra": "<p>do <b>not</b> accept: loss of oxygen without electron mention</p>",
        "marks": 1,
        "spec": "3.1.7"
    },
    {
        "id": "2001-june-chm2-q5bi",
        "sub_id": "q5bi",
        "lbl": "5(b)(i)",
        "ans": "• <b>NO<sub>3</sub><sup>-</sup>:</b> +5 (1)<br>• <b>NO<sub>2</sub>:</b> +4 (1)<br>• <b>NO:</b> +2 (1)",
        "extra": "<p>allow: V, IV, II</p>",
        "marks": 3,
        "spec": "3.1.7"
    },
    {
        "id": "2001-june-chm2-q5bii",
        "sub_id": "q5bii",
        "lbl": "5(b)(ii)",
        "ans": "• <b>Process:</b> <b>reduction</b> (1)<br>• <b>Half-equation:</b> 4H<sup>+</sup> + NO<sub>3</sub><sup>-</sup> + 3e<sup>-</sup> &rarr; NO + 2H<sub>2</sub>O (1)",
        "extra": "<p>half-equation must be correctly balanced</p>",
        "marks": 2,
        "spec": "3.1.7"
    },
    {
        "id": "2001-june-chm2-q5biii",
        "sub_id": "q5biii",
        "lbl": "5(b)(iii)",
        "ans": "<b>2H<sup>+</sup> + NO<sub>3</sub><sup>-</sup> + e<sup>-</sup> &rarr; NO<sub>2</sub> + H<sub>2</sub>O</b> (1)",
        "extra": "<p>allow: multiples</p>",
        "marks": 1,
        "spec": "3.1.7"
    },
    {
        "id": "2001-june-chm2-q5biv",
        "sub_id": "q5biv",
        "lbl": "5(b)(iv)",
        "ans": "<b>Cu + 4H<sup>+</sup> + 2NO<sub>3</sub><sup>-</sup> &rarr; Cu<sup>2+</sup> + 2NO<sub>2</sub> + 2H<sub>2</sub>O</b><br><br>• correct species (1)<br>• correctly balanced (1)",
        "extra": "<p>CE if electrons included and unbalanced</p>",
        "marks": 2,
        "spec": "3.1.7"
    },

    # Q6
    {
        "id": "2001-june-chm2-q6a",
        "sub_id": "q6a",
        "lbl": "6(a)",
        "ans": "• <b>Trend:</b> <b>decreases</b> (down group) (1)<br>• <b>Explanation:</b> atomic radius / size increases / more electron shells (1)<br>• more shielding (from inner shells) (1)<br>• weaker attraction for shared electron pair / electron density in covalent bond (1)",
        "extra": "<p>if wrong trend given, allow max 2 for explanation points</p>",
        "marks": 4,
        "spec": "3.2.3"
    },
    {
        "id": "2001-june-chm2-q6b",
        "sub_id": "q6b",
        "lbl": "6(b)",
        "ans": "• <b>Trend:</b> <b>increases</b> (down group) (1)<br>• <b>Explanation:</b> molecular size / <i>M</i><sub>r</sub> increases / more electrons (1)<br>• stronger van der Waals' / intermolecular forces (between molecules) (1)",
        "extra": "<p>mark CE if incorrect trend given</p>",
        "marks": 3,
        "spec": "3.2.3"
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
        text_clean = it["ans"].replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("&rarr;", "->").replace("&rightleftharpoons;", "<=>").replace("&minus;", "-").replace("&Sigma;", "sum ").replace("&Delta;", "delta ").replace("&times;", "x").replace("<sup>", "^").replace("</sup>", "").replace("<sub>", "_").replace("</sub>", "").replace("&nbsp;", " ").replace("<i>", "").replace("</i>", "").replace("&divide;", "/").replace("&delta;", "delta ").replace("&deg;", " deg ").replace("&ndash;", "-").replace("&ge;", ">=").replace("&minus;", "-")
        q["markscheme_text"] = text_clean
        updated_count += 1

with open(q_json_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {updated_count} questions for 2001-june-chm2 in questions.json!")

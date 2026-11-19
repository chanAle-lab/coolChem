import os
import json
from generate_official_markscheme import render_official_markscheme_image

repo = "C:/Users/Alexander/.gemini/antigravity/scratch/coolChem"
out_dir = os.path.join(repo, "img/2001-june-chm1")

items = [
    # Q1
    {
        "id": "2001-june-chm1-q1a",
        "sub_id": "q1a",
        "lbl": "1(a)",
        "ans": "• <b>Mass number:</b> (number of) protons + (number of) neutrons (1)<br>• <b>Atomic number:</b> (number of) protons (1)",
        "extra": "<p>allow: atomic number = number of electrons if qualified for neutral atom</p><p>penalise: '+ electrons' for mass number</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "id": "2001-june-chm1-q1b",
        "sub_id": "q1b",
        "lbl": "1(b)",
        "ans": "<sup>9</sup><sub>5</sub>B<br><br>• <b>B</b> (or Boron) (1)<br>• <b>9</b> (mass number) and <b>5</b> (atomic number) (1)",
        "extra": "<p>penalise 9.0</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "id": "2001-june-chm1-q1c",
        "sub_id": "q1c",
        "lbl": "1(c)",
        "ans": "• <b>N:</b> 1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>3</sup> (1)<br>• <b>N<sup>3-</sup>:</b> 1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> (1)",
        "extra": "<p>allow: 2p<sub>x</sub><sup>1</sup> 2p<sub>y</sub><sup>1</sup> 2p<sub>z</sub><sup>1</sup></p><p>if omit 2 in 2p penalise once</p><p>if [He] used penalise once</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "id": "2001-june-chm1-q1d",
        "sub_id": "q1d",
        "lbl": "1(d)",
        "ans": "• (mean / average) mass of an atom (of an element) (1)<br>• &divide; 1/12th of the mass of an atom of <sup>12</sup>C (1)<br><br><i>OR</i><br><br>• [mass of 1 mole of atoms (1)<br>• &divide; 1/12th of the mass of 1 mole of <sup>12</sup>C atoms (1)]",
        "extra": "<p>allow: &times; 12 &divide; mass of 1 atom of <sup>12</sup>C</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "id": "2001-june-chm1-q1ei",
        "sub_id": "q1ei",
        "lbl": "1(e)(i)",
        "ans": "• high speed / beam of electrons from an electron gun (1)<br>• knock out an electron from X / forms X<sup>+</sup> (1)",
        "extra": "<p>allow: X(g) + e<sup>-</sup> &rarr; X<sup>+</sup>(g) + 2e<sup>-</sup></p><p>do <b>not</b> accept: electric gun</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "id": "2001-june-chm1-q1eii",
        "sub_id": "q1eii",
        "lbl": "1(e)(ii)",
        "ans": "<b>alter / change / vary</b> magnetic field (or electric field / accelerating potential) (1)",
        "extra": "<p>allow: electromagnet strength changed</p>",
        "marks": 1,
        "spec": "3.1.1"
    },
    {
        "id": "2001-june-chm1-q1eiii",
        "sub_id": "q1eiii",
        "lbl": "1(e)(iii)",
        "ans": "• [(1 &times; 82) + (1 &times; 83) + (6 &times; 84) + (2 &times; 86)] / 10 (1)<br>• = <b>84.1</b> (1)",
        "extra": "<p>ignore units</p><p>treat 1 arithmetic error as -1 mark</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "id": "2001-june-chm1-q1eiv",
        "sub_id": "q1eiv",
        "lbl": "1(e)(iv)",
        "ans": "<b>Kr</b> / krypton (2)",
        "extra": "<p>allow consequential on answer to 1(e)(iii)</p>",
        "marks": 2,
        "spec": "3.1.1"
    },

    # Q2
    {
        "id": "2001-june-chm1-q2a",
        "sub_id": "q2a",
        "lbl": "2(a)",
        "ans": "<b>Avogadro's</b> (constant / number) (1)",
        "extra": "<p>allow phonetic spelling</p>",
        "marks": 1,
        "spec": "3.1.2"
    },
    {
        "id": "2001-june-chm1-q2bi",
        "sub_id": "q2bi",
        "lbl": "2(b)(i)",
        "ans": "<i>pV</i> = <i>nRT</i> (1)",
        "extra": "<p>allow: <i>V</i> = <i>nRT</i> / <i>p</i></p>",
        "marks": 1,
        "spec": "3.1.2"
    },
    {
        "id": "2001-june-chm1-q2bii",
        "sub_id": "q2bii",
        "lbl": "2(b)(ii)",
        "ans": "• <i>V</i> = <i>nRT</i> / <i>p</i> = (1.00 &times; 8.31 &times; 298) / 100000 (1)<br>• = <b>0.0248</b> (1)<br>• <b>m<sup>3</sup></b> (1)",
        "extra": "<p>allow: 24.8 dm<sup>3</sup> (with units) scores 3 marks</p><p>allow range: 0.0247 to 0.025 m<sup>3</sup></p>",
        "marks": 3,
        "spec": "3.1.2"
    },
    {
        "id": "2001-june-chm1-q2biii",
        "sub_id": "q2biii",
        "lbl": "2(b)(iii)",
        "ans": "• <i>n</i> = <i>pV</i> / <i>RT</i> = (500000 &times; 0.00500) / (8.31 &times; 273) = 1.10 mol (1)<br>• <i>M</i><sub>r</sub>(CO<sub>2</sub>) = 44.0 (1)<br>• mass = 44.0 &times; 1.10 = <b>48.5 g</b> (1)",
        "extra": "<p>allow range: 48 &ndash; 49 g</p><p>consequential marking on calculation of moles</p>",
        "marks": 3,
        "spec": "3.1.2"
    },
    {
        "id": "2001-june-chm1-q2c",
        "sub_id": "q2c",
        "lbl": "2(c)",
        "ans": "• moles of HCl = (100 / 1000) &times; 5.0 = 0.50 mol (1)<br>• moles of H<sub>2</sub> = 0.50 / 2 = 0.25 mol (1)<br>• mass of H<sub>2</sub> = 0.25 &times; 2.0 = <b>0.50 g</b> (1)",
        "extra": "<p>if no factor of 2 used for 1:2 ratio, CE = 0 for remaining marks</p>",
        "marks": 3,
        "spec": "3.1.2"
    },
    {
        "id": "2001-june-chm1-q2di",
        "sub_id": "q2di",
        "lbl": "2(d)(i)",
        "ans": "• %O = 100 &minus; (38.9 + 16.7) = <b>44.4%</b> (1)<br>• ratio Fe : C : O = (38.9 / 55.8) : (16.7 / 12.0) : (44.4 / 16.0) (1)<br>&nbsp;&nbsp;= 0.697 : 1.39 : 2.78 = 1 : 2 : 4<br>• empirical formula = <b>FeC<sub>2</sub>O<sub>4</sub></b> (1)",
        "extra": "<p>if incorrect %O calculated, allow consequential ratio marking</p>",
        "marks": 3,
        "spec": "3.1.2"
    },
    {
        "id": "2001-june-chm1-q2dii",
        "sub_id": "q2dii",
        "lbl": "2(d)(ii)",
        "ans": "<b>CO</b> / carbon monoxide (1)",
        "extra": "<p>allow: consequential on (d)(i)</p>",
        "marks": 1,
        "spec": "3.1.2"
    },

    # Q3
    {
        "id": "2001-june-chm1-q3a",
        "sub_id": "q3a",
        "lbl": "3(a)",
        "ans": "<b>electrostatic</b> (attraction between oppositely charged ions) (1)",
        "extra": "<p>allow: ionic</p>",
        "marks": 1,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3b",
        "sub_id": "q3b",
        "lbl": "3(b)",
        "ans": "<b>shared pair of electrons</b> (1)",
        "extra": "<p>allow: shared electron pair</p>",
        "marks": 1,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3c",
        "sub_id": "q3c",
        "lbl": "3(c)",
        "ans": "• <b>both electrons / electron pair</b> (1)<br>• (donated) from the <b>same atom</b> / molecule / species (1)",
        "extra": "<p>allow: dative covalent description</p>",
        "marks": 2,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3d",
        "sub_id": "q3d",
        "lbl": "3(d)",
        "ans": "• <b>positive ions</b> / cations / lattice of metal ions (1)<br>• attracted to <b>delocalised electrons</b> / sea of electrons (1)",
        "extra": "<p>mention of ionic or covalent bonding or molecules CE = 0</p>",
        "marks": 2,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3ei",
        "sub_id": "q3ei",
        "lbl": "3(e)(i)",
        "ans": "• <b>charge separation</b> / unequal sharing of electrons (1)<br>• leading to &delta;+ and &delta;&minus; ends (1)",
        "extra": "<p>allow: diagram showing &delta;+ and &delta;&minus; on HCl</p>",
        "marks": 2,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3eii",
        "sub_id": "q3eii",
        "lbl": "3(e)(ii)",
        "ans": "• chlorine is <b>more electronegative</b> than hydrogen (1)<br>• attracts electron density / bonding pair towards chlorine (1)",
        "extra": "<p>allow: difference in electronegativity between H and Cl</p>",
        "marks": 2,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3eiii",
        "sub_id": "q3eiii",
        "lbl": "3(e)(iii)",
        "ans": "<b>van der Waals'</b> forces (1)",
        "extra": "<p>allow: dispersion forces / London forces / temporary dipole-dipole</p>",
        "marks": 1,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3f",
        "sub_id": "q3f",
        "lbl": "3(f)",
        "ans": "<i>Diagram showing two HF molecules:</i><br>• 3 lone pairs on each F atom (1)<br>• partial charges &delta;+ on H and &delta;&minus; on F (1)<br>• hydrogen bond from lone pair on F to &delta;+ H of adjacent molecule (1)",
        "extra": "<p>penalise full charges H<sup>+</sup> &minus; F<sup>-</sup></p>",
        "marks": 3,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q3g",
        "sub_id": "q3g",
        "lbl": "3(g)",
        "ans": "bromine is <b>not sufficiently electronegative</b> (1)",
        "extra": "<p>allow: lone pair on Br too diffuse</p><p>allow: bond not polar enough / small electronegativity difference</p>",
        "marks": 1,
        "spec": "3.1.3"
    },

    # Q4
    {
        "id": "2001-june-chm1-q4a",
        "sub_id": "q4a",
        "lbl": "4(a)",
        "ans": "• <b>Solid iodine:</b> vibration (1) about a fixed position (1)<br>• <b>Iodine vapour:</b> random motion / free to move (1)",
        "extra": "<p>allow: rapid / straight line motion for vapour</p>",
        "marks": 3,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q4b",
        "sub_id": "q4b",
        "lbl": "4(b)",
        "ans": "• <b>weak intermolecular forces</b> / van der Waals' forces (1)<br>• easily overcome / require little energy to break (1)",
        "extra": "<p>do <b>not</b> accept: covalent bonds break</p>",
        "marks": 2,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q4c",
        "sub_id": "q4c",
        "lbl": "4(c)",
        "ans": "• <b>Property 1:</b> silver conducts electricity (1)<br>• <b>Reason:</b> delocalised electrons (1) <i>[NaCl has no mobile ions in solid]</i><br>• <b>Property 2:</b> silver is malleable / ductile (1)<br>• <b>Reason:</b> layers / planes of atoms / ions can slide over each other (1) <i>[NaCl is brittle]</i>",
        "extra": "<p>allow: silver insoluble in water (1) / NaCl soluble (1)</p>",
        "marks": 4,
        "spec": "3.1.3"
    },
    {
        "id": "2001-june-chm1-q4d",
        "sub_id": "q4d",
        "lbl": "4(d)",
        "ans": "• <b>BeCl<sub>2</sub>:</b> linear shape Cl&minus;Be&minus;Cl (1), bond angle <b>180&deg;</b> (1)<br>• <b>NCl<sub>3</sub>:</b> pyramidal shape with 1 lone pair on N (1), bond angle <b>106&deg; &ndash; 108&deg;</b> (1)<br>• <b>BeCl<sub>4</sub><sup>2-</sup>:</b> tetrahedral shape [BeCl<sub>4</sub>]<sup>2-</sup> (1), bond angle <b>109&deg; &ndash; 109.5&deg;</b> (1)",
        "extra": "<p>shape and angle marked independently for each species</p>",
        "marks": 6,
        "spec": "3.1.3"
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
        text_clean = it["ans"].replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("&rarr;", "->").replace("&rightleftharpoons;", "<=>").replace("&minus;", "-").replace("&Sigma;", "sum ").replace("&Delta;", "delta ").replace("&times;", "x").replace("<sup>", "^").replace("</sup>", "").replace("<sub>", "_").replace("</sub>", "").replace("&nbsp;", " ").replace("<i>", "").replace("</i>", "").replace("&divide;", "/").replace("&delta;", "delta ").replace("&deg;", " deg ").replace("&ndash;", "-")
        q["markscheme_text"] = text_clean
        updated_count += 1

with open(q_json_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {updated_count} questions for 2001-june-chm1 in questions.json!")

import os
import json
from generate_official_markscheme import render_official_markscheme_image

repo = "C:/Users/Alexander/.gemini/antigravity/scratch/coolChem"
out_dir = os.path.join(repo, "img/2001-jan-chm1")

items = [
    # Q2
    {
        "id": "2001-jan-chm1-q2a",
        "sub_id": "q2a",
        "lbl": "2(a)",
        "ans": "• 12 / (1.99 × 10<sup>-23</sup>) (1)<br>• = <b>6.03 × 10<sup>23</sup></b> (1)",
        "extra": "<p>allow: 6.030 × 10<sup>23</sup></p><p>allow: correct expression without calculating final value for 1 mark</p>",
        "marks": 2,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm1-q2b",
        "sub_id": "q2b",
        "lbl": "2(b)",
        "ans": "<b>simplest ratio</b> of atoms of each element in a compound (1)",
        "extra": "<p>allow: simplest whole number ratio of elements in a compound</p>",
        "marks": 1,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm1-q2c",
        "sub_id": "q2c",
        "lbl": "2(c)",
        "ans": "• (average) mass of an entity / molecule (1)<br>• ÷ 1/12th of the mass of an atom of <sup>12</sup>C (1)<br><br><i>OR</i><br><br>• [mass of 1 mole of molecules (1)<br>• ÷ 1/12th of mass of 1 mole of <sup>12</sup>C (1)]",
        "extra": "<p>allow: (average mass of one molecule × 12) ÷ mass of one atom of <sup>12</sup>C</p>",
        "marks": 2,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm1-q2d",
        "sub_id": "q2d",
        "lbl": "2(d)",
        "ans": "• CHO = 29<br>&nbsp;&nbsp;174 / 29 = <b>6</b> (1)<br>• (therefore) <b>C<sub>6</sub>H<sub>6</sub>O<sub>6</sub></b> (1)",
        "extra": "<p>allow: working showing 6 empirical units</p>",
        "marks": 2,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm1-q2e",
        "sub_id": "q2e",
        "lbl": "2(e)",
        "ans": "<b>CH<sub>4</sub>O + 1&frac12; O<sub>2</sub> &rarr; CO<sub>2</sub> + 2H<sub>2</sub>O</b> (1)",
        "extra": "<p>allow multiples e.g.:<br>2CH<sub>4</sub>O + 3O<sub>2</sub> &rarr; 2CO<sub>2</sub> + 4H<sub>2</sub>O</p><p>ignore state symbols</p>",
        "marks": 1,
        "spec": "3.1.2"
    },

    # Q3
    {
        "id": "2001-jan-chm1-q3a",
        "sub_id": "q3a",
        "lbl": "3(a)",
        "ans": "• moles of NH<sub>3</sub> = 20.0 / 17.0 = <b>1.18</b> (mol) (1)<br>• moles of HNO<sub>3</sub> = moles of NH<sub>3</sub> = 1.18 (mol)<br>• volume = 1.18 / 2.00 (1)<br>• = <b>0.588</b> (1) <b>dm<sup>3</sup></b> (1)",
        "extra": "<p>allow: 588 cm<sup>3</sup> (with correct unit)</p><p>consequential marking from calculation of moles</p>",
        "marks": 4,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm1-q3bi",
        "sub_id": "q3bi",
        "lbl": "3(b)(i)",
        "ans": "• <i>pV</i> = <i>nRT</i> (1)<br>• <i>n</i> = <i>pV</i> / <i>RT</i> = (95000 &times; 0.0500) / (8.31 &times; 298) (1)<br>• = <b>1.92</b> (1)<br>• <b>mol</b> (1)",
        "extra": "<p>allow: 1.918 mol</p><p>mark independently: equation (1), substitution with unit conversion (1), value (1), unit (1)</p>",
        "marks": 4,
        "spec": "3.1.2"
    },
    {
        "id": "2001-jan-chm1-q3bii",
        "sub_id": "q3bii",
        "lbl": "3(b)(ii)",
        "ans": "• moles of NH<sub>4</sub>NO<sub>3</sub> = 1.92 / 1.5 = <b>1.28 mol</b> (1)<br>• mass = 1.28 &times; 80.0 (1) = <b>102 g</b> (or <b>102.4 g</b>) (1)",
        "extra": "<p>consequential marking from 3(b)(i) answer</p>",
        "marks": 2,
        "spec": "3.1.2"
    },

    # Q4
    {
        "id": "2001-jan-chm1-q4a",
        "sub_id": "q4a",
        "lbl": "4(a)",
        "ans": "• Cross for <b>Si</b> higher than Al (1)<br>• Cross for <b>P</b> higher than Si (1)<br>• Cross for <b>S</b> lower than P (and higher than Al) (1)",
        "extra": "<p>allow: general trend of Si &gt; Al, P &gt; Si, S &lt; P</p>",
        "marks": 3,
        "spec": "3.1.1"
    },
    {
        "id": "2001-jan-chm1-q4b",
        "sub_id": "q4b",
        "lbl": "4(b)",
        "ans": "<b>Ne(g) &rarr; Ne<sup>+</sup>(g) + e<sup>-</sup></b> (1)",
        "extra": "<p>allow: Ne &rarr; Ne<sup>+</sup> + e</p><p>do <b>not</b> accept: missing charges</p>",
        "marks": 1,
        "spec": "3.1.1"
    },
    {
        "id": "2001-jan-chm1-q4c",
        "sub_id": "q4c",
        "lbl": "4(c)",
        "ans": "<i>Explanation for neon:</i><br>• Neon's electron is in a lower (2p) shell / closer to nucleus (1)<br>• attracted more strongly to (or less shielded from) the nucleus (1)<br><br><i>Explanation for magnesium:</i><br>• magnesium has more protons / greater nuclear charge (1)<br>• electrons in same (3rd) shell / similar shielding (1)",
        "extra": "<p>do <b>not</b> accept: vague references to full octet / stability</p>",
        "marks": 4,
        "spec": "3.1.1"
    },
    {
        "id": "2001-jan-chm1-q4d",
        "sub_id": "q4d",
        "lbl": "4(d)",
        "ans": "• Al's outer electron is in a <b>3p</b> sub-shell (1)<br>• 3p electron is higher in energy / further from nucleus / shielded by 3s electrons (1)",
        "extra": "<p>do <b>not</b> accept: aluminium has more shielding without naming sub-shell</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "id": "2001-jan-chm1-q4e",
        "sub_id": "q4e",
        "lbl": "4(e)",
        "ans": "• Element: <b>neon</b> (1)<br>• exists as individual / free atoms (1)<br>• (very) weak van der Waals forces (between atoms) (1)",
        "extra": "<p>allow: monoatomic</p><p>allow: dispersion forces / London forces</p>",
        "marks": 3,
        "spec": "3.1.3"
    },
    {
        "id": "2001-jan-chm1-q4f",
        "sub_id": "q4f",
        "lbl": "4(f)",
        "ans": "• Element: <b>silicon</b> (1)<br>• macromolecular / giant covalent lattice (1)<br>• (many strong) covalent bonds must be broken (1)",
        "extra": "<p>require: mention of large amount of energy needed to break covalent bonds</p>",
        "marks": 3,
        "spec": "3.1.3"
    },

    # Q5
    {
        "id": "2001-jan-chm1-q5a",
        "sub_id": "q5a",
        "lbl": "5(a)",
        "ans": "• ability / power of an atom to attract electron density / shared pair of electrons (1)<br>• from a covalent bond (1)",
        "extra": "<p>do <b>not</b> accept: attract an electron (without mention of bond / shared pair)</p>",
        "marks": 2,
        "spec": "3.1.3"
    },
    {
        "id": "2001-jan-chm1-q5b",
        "sub_id": "q5b",
        "lbl": "5(b)",
        "ans": "• <b>Trend:</b> decreases (1)<br>• <b>Explanation:</b> outer electrons further from nucleus / atomic radius increases (1)<br>• more shielding (from inner electron shells) (1)",
        "extra": "<p>mark trend independently</p>",
        "marks": 3,
        "spec": "3.2.2"
    },
    {
        "id": "2001-jan-chm1-q5c",
        "sub_id": "q5c",
        "lbl": "5(c)",
        "ans": "• <b>Equation:</b> Sr + 2H<sub>2</sub>O &rarr; Sr(OH)<sub>2</sub> + H<sub>2</sub> (1)<br>• <b>pH:</b> 12 &ndash; 14 (1)",
        "extra": "<p>allow: pH in range 10 &ndash; 14</p>",
        "marks": 2,
        "spec": "3.2.2"
    },
    {
        "id": "2001-jan-chm1-q5d",
        "sub_id": "q5d",
        "lbl": "5(d)",
        "ans": "• <b>Observation:</b> white precipitate (1)<br>• <b>Equation:</b> Ba<sup>2+</sup> + SO<sub>4</sub><sup>2-</sup> &rarr; BaSO<sub>4</sub> (1)",
        "extra": "<p>allow: BaCl<sub>2</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; BaSO<sub>4</sub> + 2HCl</p><p>allow: white solid</p>",
        "marks": 2,
        "spec": "3.2.2"
    },
    {
        "id": "2001-jan-chm1-q5e",
        "sub_id": "q5e",
        "lbl": "5(e)",
        "ans": "any <b>two</b> from:<br>• BeCl<sub>2</sub> is covalent (1)<br>• Be(OH)<sub>2</sub> is amphoteric (1)<br>• Be forms complex ions (1)",
        "extra": "<p>allow: hydrolyses in water</p>",
        "marks": 2,
        "spec": "3.2.2"
    },
    {
        "id": "2001-jan-chm1-q5f",
        "sub_id": "q5f",
        "lbl": "5(f)",
        "ans": "high charge / size ratio (1)",
        "extra": "<p>allow: high charge density / small ionic radius / highly polarising</p>",
        "marks": 1,
        "spec": "3.2.2"
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
        # Clean text representation for markscheme_text
        text_clean = it["ans"].replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("&rarr;", "->").replace("&times;", "x").replace("&frac12;", "1/2").replace("<sup>", "^").replace("</sup>", "").replace("<sub>", "_").replace("</sub>", "").replace("&ndash;", "-").replace("&nbsp;", " ")
        q["markscheme_text"] = text_clean
        updated_count += 1

with open(q_json_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {updated_count} questions in questions.json!")

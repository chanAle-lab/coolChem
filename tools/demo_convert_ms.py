import os
from tools.generate_official_markscheme import render_official_markscheme_image

repo = "C:/Users/Alexander/.gemini/antigravity/scratch/coolChem"
out_dir = os.path.join(repo, "img/2001-jan-chm1")

q1_ms = [
    {
        "sub_id": "q1a",
        "lbl": "1(a)",
        "ans": "• <b>Relative mass:</b> 1 (1)<br>• <b>Relative charge:</b> 0 / neutral (1)",
        "extra": "<p>allow: 1.0</p><p>allow: zero / none / no charge</p><p>do <b>not</b> accept: -1 or +1</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "sub_id": "q1b",
        "lbl": "1(b)",
        "ans": "• <b>In common:</b> (same) number of protons (or electrons) (1)<br>• <b>Difference:</b> (different) number of neutrons (1)",
        "extra": "<p>allow: same atomic number / different mass number</p><p>do <b>not</b> accept: vague mass differences without mentioning neutrons</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "sub_id": "q1c",
        "lbl": "1(c)",
        "ans": "<sup>41</sup><sub>19</sub>K<br><br>• <b>K</b> symbol (1)<br>• <b>41</b> (mass number) and <b>19</b> (atomic number) (1)",
        "extra": "<p>atomic number 19 must match K symbol</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "sub_id": "q1di",
        "lbl": "1(d)(i)",
        "ans": "• <b>Measurement 1:</b> <i>m/z</i> (ratio) (1)<br>• <b>Measurement 2:</b> relative abundance (1)",
        "extra": "<p>allow: mass (or <i>m/e</i>)</p><p>allow: percentage abundance / intensity / current</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "sub_id": "q1dii",
        "lbl": "1(d)(ii)",
        "ans": "any <b>two</b> from:<br>• (ions hit a) charged (or negative) plate (1)<br>• creates a current (when hit by ions) (1)<br>• sends a signal to a computer (or chart recorder) (1)",
        "extra": "<p>allow: ions gain electrons from the detector plate</p><p>allow: current is proportional to abundance</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "sub_id": "q1diii",
        "lbl": "1(d)(iii)",
        "ans": "(they have the) same <i>m/z</i> (ratio) (1)",
        "extra": "<p>allow: both have <i>m/z</i> = 14</p><p>(14/1 = 28/2 = 14)</p>",
        "marks": 1,
        "spec": "3.1.1"
    },
    {
        "sub_id": "q1e",
        "lbl": "1(e)",
        "ans": "• 6 electrons in total (1)<br>• correct orbital arrangement: 1s: ↑↓, 2s: ↑↓, 2p: ↑, ↑, _ (1)",
        "extra": "<p>2p electrons must be in separate orbitals with parallel spins (Hund's rule)</p>",
        "marks": 2,
        "spec": "3.1.1"
    },
    {
        "sub_id": "q1f",
        "lbl": "1(f)",
        "ans": "1s<sup>2</sup> 2s<sup>2</sup> (1)",
        "extra": "<p>allow subscripts or large numbers if clearly meant as powers</p>",
        "marks": 1,
        "spec": "3.1.1"
    }
]

for item in q1_ms:
    out_path = os.path.join(out_dir, f"ms_{item['sub_id']}.jpg")
    render_official_markscheme_image(
        question_label=item['lbl'],
        answers_html=item['ans'],
        extra_html=item['extra'],
        marks=item['marks'],
        spec_ref=item['spec'],
        output_path=out_path
    )
    print(f"Generated official MS table for {item['lbl']} -> {out_path}")

"""
coolChem Official Mark Scheme Table Generator
----------------------------------------------
Renders structured mark scheme entries into official AQA-style table images
matching the exact typography, borders, and column alignment of modern AQA mark schemes:
  Columns: [Question | Answers | Extra information | Mark | AO / Spec Ref.]
"""

import fitz
from PIL import Image
import numpy as np
import os
import html

def render_official_markscheme_image(
    question_label: str,
    answers_html: str,
    extra_html: str,
    marks: int,
    spec_ref: str,
    output_path: str,
    width_pt: int = 700,
    dpi: int = 150
):
    """
    Renders an official AQA markscheme table to an image file at output_path.
    """
    html_code = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 8px;
    background: #ffffff;
    font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    color: #000000;
  }}
  table.ms-table {{
    border-collapse: collapse;
    width: 100%;
    border: 1.5pt solid #000000;
  }}
  table.ms-table th, table.ms-table td {{
    border: 1pt solid #000000;
    padding: 6pt 8pt;
    vertical-align: top;
    font-size: 10pt;
    line-height: 1.4;
  }}
  table.ms-table th {{
    font-weight: bold;
    text-align: center;
    border-bottom: 1.5pt solid #000000;
    font-size: 10.5pt;
    padding: 6pt 4pt;
  }}
  .col-q {{
    width: 12%;
    text-align: center;
    font-weight: bold;
    font-size: 11pt;
  }}
  .col-ans {{
    width: 38%;
    text-align: left;
  }}
  .col-extra {{
    width: 32%;
    text-align: left;
    font-size: 9.5pt;
    color: #111111;
  }}
  .col-mark {{
    width: 8%;
    text-align: center;
    font-size: 11pt;
  }}
  .col-spec {{
    width: 10%;
    text-align: center;
    font-size: 9.5pt;
  }}
  ul {{
    margin: 2pt 0;
    padding-left: 14pt;
  }}
  li {{
    margin-bottom: 2pt;
  }}
  p {{
    margin: 0 0 4pt 0;
  }}
  p:last-child {{
    margin-bottom: 0;
  }}
</style>
</head>
<body>
<table class="ms-table">
  <thead>
    <tr>
      <th class="col-q">Question</th>
      <th class="col-ans">Answers</th>
      <th class="col-extra">Extra information</th>
      <th class="col-mark">Mark</th>
      <th class="col-spec">AO /<br>Spec Ref.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="col-q">{html.escape(question_label)}</td>
      <td class="col-ans">{answers_html}</td>
      <td class="col-extra">{extra_html}</td>
      <td class="col-mark">{marks}</td>
      <td class="col-spec">{html.escape(spec_ref)}</td>
    </tr>
  </tbody>
</table>
</body>
</html>"""

    # Open with PyMuPDF as HTML
    doc = fitz.open("html", html_code.encode("utf-8"))
    doc.layout(rect=fitz.Rect(0, 0, width_pt, 600))
    page = doc[0]
    pix = page.get_pixmap(dpi=dpi)
    
    import io
    raw_im = Image.open(io.BytesIO(pix.tobytes("png")))
    arr = np.array(raw_im.convert("L"))
    non_white = np.where(arr < 250)
    if len(non_white[0]) > 0:
        y0, y1 = max(0, non_white[0].min() - 4), min(raw_im.height, non_white[0].max() + 4)
        x0, x1 = max(0, non_white[1].min() - 4), min(raw_im.width, non_white[1].max() + 4)
        cropped = raw_im.crop((x0, y0, x1, y1))
    else:
        cropped = raw_im

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    if output_path.lower().endswith(('.jpg', '.jpeg')):
        cropped.convert("RGB").save(output_path, quality=95)
    else:
        cropped.save(output_path)
    return output_path

if __name__ == "__main__":
    # Test sample
    out = "C:/Users/Alexander/.gemini/antigravity/scratch/coolChem/test_sample_ms.jpg"
    render_official_markscheme_image(
        question_label="1(a)",
        answers_html="<ul><li><b>Relative mass:</b> 1</li><li><b>Relative charge:</b> 0 / neutral</li></ul>",
        extra_html="<p>allow: 1.0</p><p>allow: zero / none</p><p>do <b>not</b> accept -1 or +1</p>",
        marks=2,
        spec_ref="3.1.1",
        output_path=out
    )
    print("Rendered test sample to:", out)

"""
Ingestion script for 2003 January CHM3/W (Section A only)
Excludes old-spec Section B essay questions (Q5 and Q6).
Renders official AQA modern mark scheme tables and precision cropped question images.
"""
import os
import re
import json
import fitz
from PIL import Image
import sys

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.append(os.path.join(REPO_DIR, "tools"))
from generate_official_markscheme import render_official_markscheme_image

QP_PATH = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463606_01130d35.pdf"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")
IMG_DIR = os.path.join(REPO_DIR, "img", "2003-jan-chm3w")
os.makedirs(IMG_DIR, exist_ok=True)

PAPER_INFO = {
    "id": "2003-jan-chm3w",
    "year": 2003,
    "series": "January",
    "date": "2003-01-20",
    "code": "CHM3/W",
    "unit": "Unit 3(a): Introduction to Organic Chemistry",
    "level": "AS",
    "spec": "AQA Chemistry",
    "totalMarks": 60,
    "duration": "1 hour 15 mins"
}

QUESTIONS_DEF = [
    # Page 2: Question 1(a)-(c)(i)
    ("2003-jan-chm3w-q1ai", "1(a)(i)", 2, 150, 315, 1, ["3.3.2"], ["recall"], "State what is meant by the term hydrocarbon."),
    ("2003-jan-chm3w-q1aii", "1(a)(ii)", 2, 318, 385, 1, ["3.3.2"], ["recall"], "Give the general formula for the alkanes."),
    ("2003-jan-chm3w-q1aiii", "1(a)(iii)", 2, 388, 465, 1, ["3.3.2"], ["recall"], "Give the molecular formula for hexane."),
    ("2003-jan-chm3w-q1b", "1(b)", 2, 468, 605, 2, ["3.3.1"], ["recall"], "State two other characteristics of an homologous series."),
    ("2003-jan-chm3w-q1ci", "1(c)(i)", 2, 608, 770, 2, ["3.3.1"], ["recall"], "State what is meant by the term structural isomers."),
    
    # Page 5: Question 1(c)(ii)-(iii), (d)(i)-(ii)
    ("2003-jan-chm3w-q1cii", "1(c)(ii)", 5, 80, 400, 2, ["3.3.1"], ["recall"], "Name the two isomers of hexane shown (2-methylpentane, 2,2-dimethylbutane)."),
    ("2003-jan-chm3w-q1ciii", "1(c)(iii)", 5, 402, 520, 2, ["3.3.1"], ["recall"], "Give structures of two other branched-chain isomers of hexane."),
    ("2003-jan-chm3w-q1di", "1(d)(i)", 5, 522, 685, 3, ["3.1.2"], ["calculation"], "Calculate empirical formula of hydrocarbon W (92.3% C, Mr 78.0)."),
    ("2003-jan-chm3w-q1dii", "1(d)(ii)", 5, 688, 775, 1, ["3.1.2"], ["calculation"], "Calculate molecular formula of W from empirical formula and Mr."),
    
    # Page 6: Question 2(a)
    ("2003-jan-chm3w-q2ai", "2(a)(i)", 6, 80, 515, 4, ["3.3.4"], ["analysis"], "Mechanism for electrophilic addition of HBr to propene forming major product."),
    ("2003-jan-chm3w-q2aii", "2(a)(ii)", 6, 518, 680, 1, ["3.3.4"], ["recall"], "Structure of alternative carbocation formed between propene and HBr."),
    
    # Page 7: Question 2(b)-(c)
    ("2003-jan-chm3w-q2bi", "2(b)(i)", 7, 80, 345, 2, ["3.3.3"], ["recall"], "Structure and name of organic product of 2-bromopropane with aqueous NaOH."),
    ("2003-jan-chm3w-q2bii", "2(b)(ii)", 7, 348, 610, 3, ["3.3.3"], ["analysis"], "Name and mechanism for substitution of 2-bromopropane with OH-."),
    ("2003-jan-chm3w-q2ci", "2(c)(i)", 7, 612, 700, 1, ["3.3.3"], ["recall"], "Name mechanism for reaction of 2-bromopropane with NaOH forming propene."),
    ("2003-jan-chm3w-q2cii", "2(c)(ii)", 7, 702, 770, 1, ["3.3.3"], ["recall"], "State the role of sodium hydroxide in elimination to propene."),
    
    # Page 8: Question 3(a)-(b)
    ("2003-jan-chm3w-q3ai", "3(a)(i)", 8, 80, 165, 1, ["3.3.5"], ["recall"], "State what is meant by the term hydration."),
    ("2003-jan-chm3w-q3aii", "3(a)(ii)", 8, 168, 335, 2, ["3.3.5"], ["analysis"], "One advantage and one disadvantage of manufacturing ethanol by fermentation."),
    ("2003-jan-chm3w-q3bi", "3(b)(i)", 8, 338, 595, 2, ["3.3.5"], ["recall"], "Draw structures of aldehyde and carboxylic acid formed by oxidising ethanol."),
    ("2003-jan-chm3w-q3bii", "3(b)(ii)", 8, 598, 750, 3, ["3.3.5"], ["recall"], "Reagents and conditions for oxidation of ethanol to carboxylic acid."),
    
    # Page 9: Question 3(c)-(d)
    ("2003-jan-chm3w-q3ci", "3(c)(i)", 9, 80, 215, 1, ["3.3.5"], ["recall"], "Structure of 4-carbon alcohol resistant to oxidation."),
    ("2003-jan-chm3w-q3cii", "3(c)(ii)", 9, 218, 385, 1, ["3.3.5"], ["recall"], "Structure of 4-carbon alcohol oxidised to a ketone."),
    ("2003-jan-chm3w-q3di", "3(d)(i)", 9, 388, 465, 1, ["3.3.5"], ["recall"], "Catalyst for dehydration of ethanol to ethene."),
    ("2003-jan-chm3w-q3dii", "3(d)(ii)", 9, 468, 755, 4, ["3.3.5"], ["analysis"], "Complete mechanism for acid-catalysed dehydration of ethanol to ethene."),
    
    # Page 10: Question 4
    ("2003-jan-chm3w-q4ai", "4(a)(i)", 10, 80, 205, 2, ["3.3.4"], ["recall"], "Equation for formation of epoxyethane from ethene showing structure."),
    ("2003-jan-chm3w-q4aii", "4(a)(ii)", 10, 208, 255, 1, ["3.3.4"], ["analysis"], "Explain why epoxyethane molecule is highly reactive."),
    ("2003-jan-chm3w-q4aiii", "4(a)(iii)", 10, 258, 475, 2, ["3.3.5"], ["recall"], "Structure and one use of product formed by epoxyethane and water."),
    ("2003-jan-chm3w-q4b", "4(b)", 10, 478, 755, 3, ["3.3.1"], ["recall"], "Structures of the two isomers of but-2-ene and name type of isomerism.")
]

MS_DATA = {
    "2003-jan-chm3w-q1ai": {
        "answers": "<b>Molecule / compound / consists / composed / made up of hydrogen and carbon only</b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-jan-chm3w-q1aii": {
        "answers": "<b>C<sub><i>n</i></sub>H<sub>2<i>n</i>+2</sub></b> (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-jan-chm3w-q1aiii": {
        "answers": "<b>C<sub>6</sub>H<sub>14</sub> only</b> (1)",
        "extra": "Do not credit structures alone or in addition.",
        "mark": 1,
        "spec": "3.3.2"
    },
    "2003-jan-chm3w-q1b": {
        "answers": "<b>Any two from:</b><br>• <b>Chemically similar / react in same way / same chemistry</b> (1)<br>• <b>Differ by CH<sub>2</sub></b> (1)<br>• <b>Gradation in physical properties</b> (OR specified trend e.g. b.p.) (1)<br>• <b>Same functional group</b> (1)",
        "extra": "NOT same molecular formula.",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2003-jan-chm3w-q1ci": {
        "answers": "• M1: <b>Same molecular formula</b> (1)<br>• M2: <b>Different structural formula / structures / atoms arranged in different ways</b> (1)",
        "extra": "NOT same Mr for M1.<br>NOT different spatial arrangements for M2.<br>Only credit M2 if M1 is correct.",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2003-jan-chm3w-q1cii": {
        "answers": "• Isomer 1: <b>2-methylpentane</b> (1)<br>• Isomer 2: <b>2,2-dimethylbutane</b> (1)",
        "extra": "Penalise 'meth' etc. on first occasion.<br>Ignore commas and dashes in names.",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2003-jan-chm3w-q1ciii": {
        "answers": "• Isomer 3: <b>CH<sub>3</sub>CH<sub>2</sub>CH(CH<sub>3</sub>)CH<sub>2</sub>CH<sub>3</sub></b> (3-methylpentane) (1)<br>• Isomer 4: <b>CH<sub>3</sub>CH(CH<sub>3</sub>)CH(CH<sub>3</sub>)CH<sub>3</sub></b> (2,3-dimethylbutane) (1)",
        "extra": "Either order.<br>Penalise 'sticks' once.<br>Penalise absence of vertical bonds once.<br>Penalise badly drawn bonds once.<br>Accept correct condensed formula or structural formula.",
        "mark": 2,
        "spec": "3.3.1"
    },
    "2003-jan-chm3w-q1di": {
        "answers": "• M1: % by mass of H = 100 &minus; 92.3 = <b>7.7(0)%</b> (1)<br>• M2: Moles: mol H = 7.70 / 1 = 7.70; mol C = 92.3 / 12 = 7.69 (1)<br>• M3: Ratio 1 : 1 &there4; <b>CH</b> (1)",
        "extra": "Correct answer = 3 marks.<br>Credit variations for M2 e.g. (78 &times; 7.7 / 100 = 6) and (78 &times; 92.3 / 12 &times; 100 = 6).",
        "mark": 3,
        "spec": "3.1.2"
    },
    "2003-jan-chm3w-q1dii": {
        "answers": "• (CH has empirical mass of 13; 78 / 13 = 6) &there4; <b>C<sub>6</sub>H<sub>6</sub></b> (1)",
        "extra": "Correct answer = 1 mark.",
        "mark": 1,
        "spec": "3.1.2"
    },
    "2003-jan-chm3w-q2ai": {
        "answers": "• M1: Curly arrow from C=C bond to H of H&minus;Br (1)<br>• M2: Curly arrow from H&minus;Br bond to Br (1)<br>• M3: Structure of secondary carbocation: <b>H<sub>3</sub>C&minus;C<sup>+</sup>H&minus;CH<sub>3</sub></b> (1)<br>• M4: Curly arrow from lone pair on :Br<sup>&minus;</sup> to C<sup>+</sup> (1)",
        "extra": "If wrong carbocation: lose structure mark (M3) but can still score 3/4.<br>If wrong alkene: lose structure mark.<br>Penalise M2 if polarity is included incorrectly, if no bond between H and Br, or if bond shown as dots.",
        "mark": 4,
        "spec": "3.3.4"
    },
    "2003-jan-chm3w-q2aii": {
        "answers": "<b>CH<sub>3</sub>CH<sub>2</sub>C<sup>+</sup>H<sub>2</sub></b> (primary carbocation) (1)",
        "extra": "Credit secondary carbocation here if primary carbocation was used in (i).<br>Ignore attack on this carbocation by Br-.",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2003-jan-chm3w-q2bi": {
        "answers": "• Structure: <b>H<sub>3</sub>C&minus;CH(OH)&minus;CH<sub>3</sub></b> (1)<br>• Name: <b>propan-2-ol</b> (1)",
        "extra": "Insist on C&minus;OH bond.<br>No credit for propan-1-ol even when named correctly.<br>Credit propane-2-ol.<br>NOT 2-hydroxypropane.",
        "mark": 2,
        "spec": "3.3.3"
    },
    "2003-jan-chm3w-q2bii": {
        "answers": "• Name of mechanism: <b>nucleophilic substitution</b> (1) (both words; NOT S<sub>N</sub>1 or S<sub>N</sub>2)<br>• Mechanism:<br>&nbsp;&nbsp;&ndash; Curly arrow from lone pair on :OH<sup>&minus;</sup> to C atom attached to Br (1)<br>&nbsp;&nbsp;&ndash; Curly arrow from C&minus;Br bond to Br atom (1)",
        "extra": "Penalise incorrect polarity on C&minus;Br.<br>If SN1 mechanism given, both marks possible (M1: arrow from C-Br to Br; M2: arrow from :OH- to carbocation).<br>Credit the arrows even if incorrect haloalkane.",
        "mark": 3,
        "spec": "3.3.3"
    },
    "2003-jan-chm3w-q2ci": {
        "answers": "<b>elimination</b> (1)",
        "extra": "Ignore 'nucleophilic elimination'.<br>Penalise 'electrophilic elimination'.",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2003-jan-chm3w-q2cii": {
        "answers": "<b>Base</b> OR <b>proton acceptor</b> (1)",
        "extra": "NOT nucleophile (base).",
        "mark": 1,
        "spec": "3.3.3"
    },
    "2003-jan-chm3w-q3ai": {
        "answers": "<b>Addition of water / steam</b> (1)",
        "extra": "Ignore 'to the reaction'.",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q3aii": {
        "answers": "• <b>Advantage (any one):</b> Low technology / renewable feedstock or resource / allowed for use in drinks, perfumes / considered to be green (1)<br>• <b>Disadvantage (any one):</b> Slow / low yield / significant land use / has to be distilled / labour intensive (1)",
        "extra": "Do not credit negative statements.<br>NOT 'infinite resource', 'non-finite'.<br>Ignore yeast.<br>NOT (unqualified) batch process.<br>NOT impure product.",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q3bi": {
        "answers": "• Structure of aldehyde: <b>CH<sub>3</sub>&minus;C(=O)H</b> (1)<br>• Structure of carboxylic acid: <b>CH<sub>3</sub>&minus;C(=O)OH</b> (1)",
        "extra": "Penalise incorrect R group once.<br>NOT CH3CHO, NOT CH3COOH (must draw structural formula showing carbonyl group).",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q3bii": {
        "answers": "• Reagent: <b>Potassium dichromate(VI)</b> OR <b>sodium dichromate(VI)</b> (1)<br>• Conditions:<br>&nbsp;&nbsp;&ndash; <b>Acidified</b> OR <b>sulphuric acid</b> (1)<br>&nbsp;&nbsp;&ndash; <b>(Heat under) reflux</b> (1)",
        "extra": "Correct formulae accepted: K2Cr2O7 / Na2Cr2O7.<br>'(VI)' not essential.<br>Credit KMnO4 for M1.<br>M2 depends on M1 (but mark M2 correct from Cr2O7 2-).<br>M3 is independent.<br>Ignore T and P for M2.",
        "mark": 3,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q3ci": {
        "answers": "<b>(CH<sub>3</sub>)<sub>3</sub>C&minus;OH</b> (2-methylpropan-2-ol) (1)",
        "extra": "Possible repeat error for C-OH bond.",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q3cii": {
        "answers": "<b>CH<sub>3</sub>CH<sub>2</sub>CH(OH)CH<sub>3</sub></b> (butan-2-ol) (1)",
        "extra": "",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q3di": {
        "answers": "<b>Al<sub>2</sub>O<sub>3</sub></b> OR <b>H<sub>2</sub>SO<sub>4</sub></b> OR <b>H<sub>3</sub>PO<sub>4</sub></b> (name or formula) (1)",
        "extra": "Ignore aqueous.",
        "mark": 1,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q3dii": {
        "answers": "• M1: Protonated intermediate formula: <b>CH<sub>3</sub>CH<sub>2</sub>O<sup>+</sup>H<sub>2</sub></b> (1)<br>• M2: Curly arrow from C&minus;O bond to O<sup>+</sup> (loss of H<sub>2</sub>O) (1)<br>• M3: Carbocation formula: <b>CH<sub>3</sub>C<sup>+</sup>H<sub>2</sub></b> (1)<br>• M4: Curly arrow from C&minus;H bond to form C=C double bond (reforming H<sup>+</sup>) (1)",
        "extra": "For M1 '+' can be on O or H if -OH2 used.<br>For M2 arrow must go to the '+' or to oxygen.<br>Synchronous loss without carbocation loses carbocation structure mark (can score 3/4).",
        "mark": 4,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q4ai": {
        "answers": "<b>H<sub>2</sub>C=CH<sub>2</sub> + &frac12; O<sub>2</sub> &rarr; epoxyethane (cyclic C<sub>2</sub>H<sub>4</sub>O ring)</b><br>• Product structure (oxirane 3-membered ring) (1)<br>• Balanced equation (1)",
        "extra": "Penalise CH2.CH2 and CH2:CH2.<br>NOT [O].<br>For M2 allow credit when C2H4O or CH2CH2O are used.",
        "mark": 2,
        "spec": "3.3.4"
    },
    "2003-jan-chm3w-q4aii": {
        "answers": "<b>Strained (ring)</b> (or stressed) (1)",
        "extra": "NOT weak bonds.<br>NOT unstable.",
        "mark": 1,
        "spec": "3.3.4"
    },
    "2003-jan-chm3w-q4aiii": {
        "answers": "• Structure: <b>CH<sub>2</sub>(OH)&minus;CH<sub>2</sub>(OH)</b> (ethane-1,2-diol) (1)<br>• Use: <b>Antifreeze</b> OR <b>production of Terylene</b> OR <b>feedstock for polyester or PET</b> (1)",
        "extra": "NOT plasticiser, NOT solvent, NOT de-icer, NOT alcohol.",
        "mark": 2,
        "spec": "3.3.5"
    },
    "2003-jan-chm3w-q4b": {
        "answers": "• Structures of both isomers: <b><i>cis</i>-but-2-ene</b> and <b><i>trans</i>-but-2-ene</b> (showing C=C double bond with H and CH<sub>3</sub> groups) (2 marks; 1 mark for each)<br>• Type of isomerism: <b>Geometric(al)</b> OR <b><i>cis&minus;trans</i></b> OR <b>diastereoisomerism</b> (1)",
        "extra": "Ignore names.<br>Accept CH3-CH=CH-CH3 displayed geometry.<br>NOT stereoisomerism (must be specific).",
        "mark": 3,
        "spec": "3.3.1"
    }
}

def crop_question_image(doc, page_num, y0, y1, out_path, x0=35, x1=545, scale=2.0):
    page = doc[page_num - 1]
    rect = fitz.Rect(x0, max(0, y0), x1, min(page.rect.height, y1))
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=rect)
    im = Image.open(fitz.io.BytesIO(pix.tobytes("png")))
    im.convert("RGB").save(out_path, quality=90)
    return out_path

def main():
    print(f"Opening QP: {QP_PATH}")
    doc = fitz.open(QP_PATH)
    
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    papers = [p for p in db["papers"] if p["id"] != PAPER_INFO["id"]]
    papers.append(PAPER_INFO)
    db["papers"] = papers
    
    db["questions"] = [q for q in db["questions"] if q["paper"] != PAPER_INFO["id"]]
    
    new_questions = []
    
    for q_id, q_label, p_num, y0, y1, marks, topics, skills, summary in QUESTIONS_DEF:
        sub_id = q_label.replace("(", "").replace(")", "").replace(" ", "")
        q_img_rel = f"img/2003-jan-chm3w/q_q{sub_id}.jpg"
        ms_img_rel = f"img/2003-jan-chm3w/ms_q{sub_id}.jpg"
        
        q_img_abs = os.path.join(REPO_DIR, q_img_rel)
        ms_img_abs = os.path.join(REPO_DIR, ms_img_rel)
        
        crop_question_image(doc, p_num, y0, y1, q_img_abs)
        
        ms_item = MS_DATA.get(q_id, {})
        render_official_markscheme_image(
            question_label=q_label,
            answers_html=ms_item.get("answers", ""),
            extra_html=ms_item.get("extra", ""),
            marks=ms_item.get("mark", marks),
            spec_ref=ms_item.get("spec", topics[0] if topics else ""),
            output_path=ms_img_abs
        )
        
        ms_text = ms_item.get("answers", "").replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "").replace("&minus;", "-").replace("&times;", "x").replace("&rarr;", "->").replace("&Sigma;", "Sum ").replace("&Delta;", "Delta ").replace("&there4;", "therefore ").replace("&nbsp;", " ")
        if ms_item.get("extra"):
            ms_text += "\n\n[Extra Information]:\n" + ms_item.get("extra", "").replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "").replace("&minus;", "-").replace("&times;", "x").replace("&rarr;", "->")
            
        q_entry = {
            "id": q_id,
            "paper": PAPER_INFO["id"],
            "question": q_label,
            "marks": marks,
            "page": p_num,
            "topics": topics,
            "skills": skills,
            "summary": summary,
            "image": q_img_rel,
            "figures": [],
            "markscheme": ms_img_rel,
            "markscheme_text": ms_text
        }
        new_questions.append(q_entry)
        
    db["questions"].extend(new_questions)
    
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully processed {len(new_questions)} Section A questions for {PAPER_INFO['id']}.")

if __name__ == "__main__":
    main()

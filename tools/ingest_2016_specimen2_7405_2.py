"""Ingest AQA A-level Chemistry Specimen Set 2 Paper 2 (7405/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_official_markscheme import render_official_markscheme_image

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795517647635_4437b334.pdf"
)

PAPER_ID = "2016-specimen2-7405-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2016,
    "series": "Specimen Set 2",
    "unit": "7405/2",
    "level": "A-level",
    "date": "2016-01-01",
    "title": "7405/2 — A-level Paper 2: Organic and Physical Chemistry (Specimen Set 2)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q1-table1.jpg", "page": 2, "x0": 40, "y0": 130, "x1": 555, "y1": 412},
    {"filename": "fig-q1-grid.jpg", "page": 3, "x0": 120, "y0": 65, "x1": 510, "y1": 408},
    {"filename": "fig-q4-fig1.jpg", "page": 12, "x0": 40, "y0": 85, "x1": 555, "y1": 245},
    {"filename": "fig-q4-fg.jpg", "page": 14, "x0": 40, "y0": 85, "x1": 555, "y1": 195},
    {"filename": "fig-q5-scheme.jpg", "page": 18, "x0": 40, "y0": 85, "x1": 555, "y1": 270},
    {"filename": "fig-q8-fig4.jpg", "page": 25, "x0": 40, "y0": 75, "x1": 555, "y1": 728},
    {"filename": "fig-q8-fig5.jpg", "page": 26, "x0": 40, "y0": 75, "x1": 555, "y1": 765},
    {"filename": "fig-q8-table3.jpg", "page": 28, "x0": 40, "y0": 85, "x1": 555, "y1": 250},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 3, "01.3": 4,
    "02.1": 6, "02.2": 6, "02.3": 7, "02.4": 7, "02.5": 8,
    "03.1": 10, "03.2": 10, "03.3": 10, "03.4": 10, "03.5": 11,
    "04.1": 12, "04.2": 12, "04.3": 14, "04.4": 14, "04.5": 15, "04.6": 16,
    "05.1": 18, "05.2": 18, "05.3": 19,
    "06.1": 20, "06.2": 21,
    "07.1": 22, "07.2": 22, "07.3": 23, "07.4": 23,
    "08.1": 24, "08.2": 24, "08.3": 27, "08.4": 28, "08.5": 28, "08.6": 29,
    "09.1": 30,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.1.9", "marks": 4, "stem": "Calculate [C6H5CHO]^2 for each experiment in Table 1 and plot a graph of initial rate against [C6H5CHO]^2 on the grid opposite.", "figures": ["fig-q1-table1.jpg", "fig-q1-grid.jpg"], "crop_exclude_y": [[130, 412]], "ms_label": "01.1", "ms_ans": "&bull; Stage 1: [C<sub>6</sub>H<sub>5</sub>CHO]<sup>2</sup> = 0, 0.0625, 0.25, 0.56, 1 (1)<br>&bull; Stage 2: Graph labels with units and sensible scales covering &ge; half the grid (1)<br>&bull; Plotting of 5 points (1)<br>&bull; Stage 3: Line of best fit (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "01.2", "specRef": "3.1.9", "marks": 2, "stem": "Deduce the order of the reaction with respect to C6H5CHO from the graph and explain your answer.", "figures": ["fig-q1-table1.jpg"], "crop_exclude_y": [[65, 408]], "ms_label": "01.2", "ms_ans": "&bull; 2<sup>nd</sup> order (1)<br>&bull; Since [C<sub>6</sub>H<sub>5</sub>CHO]<sup>2</sup> plotted against rate is a straight line / directly proportional (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "01.3", "specRef": "3.1.9", "marks": 2, "stem": "Suggest the role of the cyanide ion in the benzaldehyde dimerisation reaction and explain your answer.", "ms_label": "01.3", "ms_ans": "&bull; Catalyst (1)<br>&bull; CN<sup>&minus;</sup> appears in the rate equation but is not in the reaction equation (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "02.1", "specRef": "3.3.3", "marks": 2, "stem": "Write two equations to show how chlorine atoms catalyse the decomposition of ozone.", "ms_label": "02.1", "ms_ans": "&bull; Cl<sup>&bull;</sup> + O<sub>3</sub> &rarr; ClO<sup>&bull;</sup> + O<sub>2</sub> (1)<br>&bull; ClO<sup>&bull;</sup> + O<sub>3</sub> &rarr; 2O<sub>2</sub> + Cl<sup>&bull;</sup> (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "02.2", "specRef": "3.3.3", "marks": 2, "stem": "State the role of potassium hydroxide and the role of propan-1-ol when chloroethane reacts to form ethene.", "ms_label": "02.2", "ms_ans": "&bull; KOH acts as a base (1)<br>&bull; Propan-1-ol acts as a solvent (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "02.3", "specRef": "3.3.3", "marks": 4, "stem": "Name and outline a mechanism for the reaction in Question 02.2 between chloroethane and potassium hydroxide to produce ethene.", "ms_label": "02.3", "ms_ans": "&bull; Elimination (1)<br>&bull; 3 curly arrows: lone pair on :OH<sup>&minus;</sup> to H; C&minus;H bond to C&minus;C; C&minus;Cl bond to Cl (3)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "02.4", "specRef": "3.3.4", "marks": 1, "stem": "Draw the structure of the monomer used to form polymer A.", "ms_label": "02.4", "ms_ans": "CF<sub>2</sub>=CFCl (1-chloro-1,2,2-trifluoroethene)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "02.5", "specRef": "3.1.1", "marks": 6, "stem": "Determine the formula of each of the three molecular ions (m/z = 220, 222, 224) of chlorofluoroalkane B (51.6% F, 32.1% Cl) and predict and explain their relative abundance ratio.", "ms_label": "02.5", "ms_ans": "<b>Indicative chemistry content:</b><br><b>Stage 1:</b> 16.3% C; moles C:Cl:F = 16.3/12 : 32.1/35.5 : 51.6/19 = 1.358 : 0.904 : 2.716 = 3 : 2 : 6 &rarr; empirical formula C<sub>3</sub>Cl<sub>2</sub>F<sub>6</sub>.<br><b>Stage 2:</b> M<sub>r</sub> = 221 lies within 220&minus;224, so molecular formula = C<sub>3</sub>Cl<sub>2</sub>F<sub>6</sub>. Ions: C<sub>3</sub><sup>35</sup>Cl<sub>2</sub>F<sub>6</sub><sup>+</sup> (220), C<sub>3</sub><sup>35</sup>Cl<sup>37</sup>ClF<sub>6</sub><sup>+</sup> (222), C<sub>3</sub><sup>37</sup>Cl<sub>2</sub>F<sub>6</sub><sup>+</sup> (224).<br><b>Stage 3:</b> Ratio = (3/4)<sup>2</sup> : 2&times;(3/4)&times;(1/4) : (1/4)<sup>2</sup> = 9 : 6 : 1.", "ms_extra": "Marked using levels of response (Level 3: 5–6 marks; Level 2: 3–4 marks; Level 1: 1–2 marks).", "ms_marks": "6"},
    {"qnum": "03.1", "specRef": "3.3.1", "marks": 1, "stem": "How many isomers are represented by the formula C5H12?", "ms_label": "03.1", "ms_ans": "<b>3</b>", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "03.2", "specRef": "3.3.1", "marks": 1, "stem": "Name the type of structural isomerism shown by the isomers of C5H12.", "ms_label": "03.2", "ms_ans": "Chain", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "03.3", "specRef": "3.3.7", "marks": 2, "stem": "Draw 3D representations of the two enantiomers of 2-hydroxypropanenitrile, showing how they are related.", "ms_label": "03.3", "ms_ans": "&bull; One 3D enantiomer of CH<sub>3</sub>CH(OH)CN (1)<br>&bull; Second enantiomer correctly drawn as 3D mirror image of first (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "03.4", "specRef": "3.3.7", "marks": 2, "stem": "Describe how separate samples of each of these enantiomers could be distinguished.", "ms_label": "03.4", "ms_ans": "&bull; Plane-polarised light (1)<br>&bull; Rotated in opposite directions (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "03.5", "specRef": "3.3.5", "marks": 8, "stem": "Butan-2-ol reacts with concentrated sulfuric acid to produce three isomeric alkenes. Name and outline a mechanism for one alkene and explain how all three are formed.", "ms_label": "03.5", "ms_ans": "&bull; Elimination (1)<br>&bull; Mechanism (3 marks): M2 arrow from lone pair on O to H<sup>+</sup>; M3 protonated alcohol intermediate + arrow C&minus;O<sup>+</sup>H<sub>2</sub> to O; M4 carbocation + arrow C&minus;H to C&minus;C forming C=C.<br>&bull; Explanation (4 marks): M5 loss of H<sup>+</sup> from C adjacent to C<sup>+</sup>; M6 loss from C1 gives but-1-ene; M7 loss from C3 gives but-2-ene; M8 but-2-ene formed as mixture of <i>E</i>-<i>Z</i> isomers.", "ms_extra": "Extended response question.", "ms_marks": "8"},
    {"qnum": "04.1", "specRef": "3.3.1", "marks": 1, "stem": "State the IUPAC name of compound F (Figure 1).", "figures": ["fig-q4-fig1.jpg"], "crop_exclude_y": [[85, 245]], "ms_label": "04.1", "ms_ans": "2,3-dimethylbutane(-1,4-)dioic acid", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "04.2", "specRef": "3.3.14", "marks": 6, "stem": "Deduce the structure of D, suggest reagents and mechanisms for steps 1 and 2, and suggest the type of reaction in step 3 (Figure 1).", "figures": ["fig-q4-fig1.jpg"], "ms_label": "04.2", "ms_ans": "&bull; D = CH<sub>3</sub>CH(Br)CH(Br)CH<sub>3</sub> (1)<br>&bull; Step 1: HBr (1), electrophilic addition (1)<br>&bull; Step 2: KCN (1), nucleophilic substitution (1)<br>&bull; Step 3: Hydrolysis (1)", "ms_extra": "", "ms_marks": "6"},
    {"qnum": "04.3", "specRef": "3.3.6", "marks": 3, "stem": "State a reagent to distinguish between F and G and describe what is observed with each.", "ms_label": "04.3", "ms_ans": "&bull; K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> &amp; H<sub>2</sub>SO<sub>4</sub> (F: no change, G: orange to green) OR Mg / Na<sub>2</sub>CO<sub>3</sub> / NaHCO<sub>3</sub> (F: effervescence, G: no change) (3)", "ms_extra": "1 mark reagent, 1 mark observation with F, 1 mark observation with G.", "ms_marks": "3"},
    {"qnum": "04.4", "specRef": "3.3.12", "marks": 2, "stem": "Compounds F and G react to form a polymer. Draw the repeating unit of the polymer.", "figures": ["fig-q4-fg.jpg"], "ms_label": "04.4", "ms_ans": "&minus;CO&minus;CH(CH<sub>3</sub>)&minus;CH(CH<sub>3</sub>)&minus;CO&minus;O&minus;CH<sub>2</sub>&minus;CH(CH<sub>3</sub>)&minus;CH(CH<sub>3</sub>)&minus;CH<sub>2</sub>&minus;O&minus;<br>&bull; Two ester groups (1); one unit only with trailing bonds (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "04.5", "specRef": "3.1.2", "marks": 4, "stem": "0.930 kg of purified F were obtained from 1.11 dm3 of G (density 1.04 g cm-3). Calculate the percentage yield.", "figures": ["fig-q4-fg.jpg"], "ms_label": "04.5", "ms_ans": "&bull; Mass of G = 1.11 &times; 10<sup>3</sup> &times; 1.04 = 1154 g (1)<br>&bull; Amount of G = 1154 / 118 = 9.78 mol (1)<br>&bull; Expected mass of F = 9.78 &times; 146 = 1428 g (or actual mol F = 930/146 = 6.37 mol) (1)<br>&bull; % yield = 930/1428 &times; 100 = 65.1% (3 sf) (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "04.6", "specRef": "RP", "marks": 4, "stem": "Name the technique used to separate and collect the liquid by-products from the reaction mixture and describe the apparatus.", "ms_label": "04.6", "ms_ans": "&bull; Fractional distillation (1)<br>&bull; Apparatus with fractionating column (1)<br>&bull; Fractionating column and thermometer (1)<br>&bull; Condenser / water jacket (1)", "ms_extra": "A rough labelled sketch illustrating these points scores the marks.", "ms_marks": "4"},
    {"qnum": "05.1", "specRef": "3.3.1", "marks": 1, "stem": "Deduce the molecular formula of H.", "figures": ["fig-q5-scheme.jpg"], "crop_exclude_y": [[85, 270]], "ms_label": "05.1", "ms_ans": "C<sub>9</sub>H<sub>10</sub>O", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "05.2", "specRef": "3.3.1", "marks": 2, "stem": "Draw the structure of one of the other two isomers produced in the reaction and name the type of structural isomerism.", "figures": ["fig-q5-scheme.jpg"], "ms_label": "05.2", "ms_ans": "&bull; 2-methyl or 3-methyl isomer of methylphenylethanone (1)<br>&bull; Position (isomerism) (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "05.3", "specRef": "3.3.10", "marks": 5, "stem": "Name and outline the mechanism for the reaction of ethanoyl chloride with methylbenzene to produce H, including the equation for forming the reactive intermediate.", "figures": ["fig-q5-scheme.jpg"], "ms_label": "05.3", "ms_ans": "&bull; Electrophilic substitution (1)<br>&bull; CH<sub>3</sub>COCl + AlCl<sub>3</sub> &rarr; CH<sub>3</sub>CO<sup>+</sup> + AlCl<sub>4</sub><sup>&minus;</sup> (1)<br>&bull; Mechanism (3 marks): M1 arrow from benzene ring to C of CH<sub>3</sub>C<sup>+</sup>O; M2 4-isomer Wheland intermediate; M3 arrow from C&minus;H bond into hexagon with loss of H<sup>+</sup>.", "ms_extra": "", "ms_marks": "5"},
    {"qnum": "06.1", "specRef": "3.3.16", "marks": 4, "stem": "Explain why dipeptides J and K can be separated by gas chromatography and why mass spectrometry using electrospray ionisation does not enable you to identify them.", "ms_label": "06.1", "ms_ans": "&bull; <b>GC:</b> Different retention times / appear at different times (1); different balance between solubility in moving gas phase and retention by stationary phase (1)<br>&bull; <b>MS:</b> Same m/z values (1); both J and K have same molecular formula / M<sub>r</sub> (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "06.2", "specRef": "3.3.16", "marks": 3, "stem": "Use Figure 2 and Table 2 to identify the dipeptides in spots M and N and deduce the order of amino acids in tripeptide L.", "ms_label": "06.2", "ms_ans": "&bull; Spot M: ser-ala (1)<br>&bull; Spot N: ala-lys (1)<br>&bull; Tripeptide L: ser-ala-lys (1)", "ms_extra": "This order only.", "ms_marks": "3"},
    {"qnum": "07.1", "specRef": "3.3.13", "marks": 3, "stem": "Draw the structure of the DNA nucleotide that contains guanine, showing clearly the bonding between the components.", "ms_label": "07.1", "ms_ans": "&bull; Correct phosphate-sugar link on C3 (or C5) (1)<br>&bull; Correct sugar-guanine link on C1 (1)<br>&bull; Remainder of molecule correct (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "07.2", "specRef": "3.3.13", "marks": 2, "stem": "Complete the base pair diagram showing the interactions between guanine and its complementary base.", "ms_label": "07.2", "ms_ans": "&bull; Correct diagram of cytosine (base pair with guanine) (1)<br>&bull; Three hydrogen bonds drawn (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "07.3", "specRef": "3.3.13", "marks": 1, "stem": "State how the interactions in the adenine-thymine base pair differ from those identified in Question 07.2.", "ms_label": "07.3", "ms_ans": "There are only two H-bonds in the adenine-thymine base pair", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "07.4", "specRef": "3.3.13", "marks": 2, "stem": "Suggest why urea is effective at separating the complementary strands in DNA.", "ms_label": "07.4", "ms_ans": "&bull; The amino / &minus;NH<sub>2</sub> groups in urea (1)<br>&bull; Are able to substitute for the H-bonds in the double helix (1)", "ms_extra": "", "ms_marks": "2"},
    {"qnum": "08.1", "specRef": "3.3.15", "marks": 1, "stem": "Give the skeletal formula of the compound used as the standard when recording a 13C NMR spectrum.", "ms_label": "08.1", "ms_ans": "Skeletal formula of tetramethylsilane: Si(CH<sub>3</sub>)<sub>4</sub> (a central Si with four single bonds to methyl groups)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "08.2", "specRef": "3.3.15", "marks": 3, "stem": "Match the 13C NMR spectra in Figure 4 to three of the isomers P, Q, R and S in Figure 3.", "figures": ["fig-q8-fig4.jpg"], "ms_label": "08.2", "ms_ans": "&bull; Top spectrum: <b>S</b> (1)<br>&bull; Middle spectrum: <b>R</b> (1)<br>&bull; Bottom spectrum: <b>Q</b> (1)", "ms_extra": "", "ms_marks": "3"},
    {"qnum": "08.3", "specRef": "3.3.15", "marks": 6, "stem": "Identify the functional group(s) present in each isomer T, U and V (Figure 5) using Table A in the Data Booklet and explain your answer.", "figures": ["fig-q8-fig5.jpg"], "ms_label": "08.3", "ms_ans": "&bull; <b>Isomer T:</b> signals due to O&minus;H (alcohol) at 3230&minus;3350 and C=O at 1680&minus;1750 (1); O&minus;H and C=O separated in molecule (not a carboxylic acid) (1)<br>&bull; <b>Isomer U:</b> only signal for O&minus;H (alcohol) at 3230&minus;3350 (1); 2 &times; OH groups / diol / OH &amp; cyclo(ether) (1)<br>&bull; <b>Isomer V:</b> signals due to O&minus;H (acid) at 2500&minus;3000 and C=O at 1680&minus;1750 (1); carboxylic acid group / &minus;COOH present (1)", "ms_extra": "", "ms_marks": "6"},
    {"qnum": "08.4", "specRef": "3.3.15", "marks": 1, "stem": "Deduce the simplest ratio of the relative numbers of protons in each environment in compound X (Table 3).", "ms_label": "08.4", "ms_ans": "2 : 2 : 2 : 3 : 3 (any order)", "ms_extra": "", "ms_marks": "1"},
    {"qnum": "08.5", "specRef": "3.3.15", "marks": 4, "stem": "Deduce the parts of X causing the signals at delta = 3.5 and 2.2 in Table 3 and explain their splitting patterns.", "figures": ["fig-q8-table3.jpg"], "ms_label": "08.5", "ms_ans": "&bull; Signal at &delta;=3.5: CH<sub>2</sub> next to / shifted downfield by electronegative O (1); quartet because of adjacent CH<sub>3</sub> group / 3 adjacent protons (1)<br>&bull; Signal at &delta;=2.2: CH<sub>3</sub> attached to / shifted downfield by electronegative C=O (1); singlet because there are no adjacent protons / no coupling (1)", "ms_extra": "", "ms_marks": "4"},
    {"qnum": "08.6", "specRef": "3.3.15", "marks": 2, "stem": "Deduce the structure of compound X, C6H12O2.", "figures": ["fig-q8-table3.jpg"], "ms_label": "08.6", "ms_ans": "CH<sub>3</sub>&minus;CH<sub>2</sub>&minus;O&minus;CH<sub>2</sub>&minus;CH<sub>2</sub>&minus;CO&minus;CH<sub>3</sub> (2)", "ms_extra": "Allow 1 mark for CH<sub>3</sub>&minus;O&minus;CH<sub>2</sub>&minus;CH<sub>2</sub>&minus;CO&minus;CH<sub>2</sub>&minus;CH<sub>3</sub>.", "ms_marks": "2"},
    {"qnum": "09.1", "specRef": "3.1.9", "marks": 8, "stem": "Complete Table 4 with ln k and 1/T, plot ln k against 1/T on the grid opposite, and calculate Ea in kJ mol-1.", "ms_label": "09.1", "ms_ans": "<b>Stage 1:</b> 1/T = 1.43&times;10<sup>&minus;3</sup>, 1.38&times;10<sup>&minus;3</sup>, 1.34&times;10<sup>&minus;3</sup>, 1.26&times;10<sup>&minus;3</sup> (1); ln k = &minus;9.7(0), &minus;8.2(0), &minus;7.1(0), &minus;4.8(0) (1); plot points (1); line of best fit (1).<br><b>Stage 2:</b> gradient working &Delta;y/&Delta;x (1); gradient = &minus;2.88 &times; 10<sup>4</sup> (1).<br><b>Stage 3:</b> E<sub>a</sub> = 2.88 &times; 10<sup>4</sup> &times; 8.314 (1); (&divide;1000 =) E<sub>a</sub> = 239 kJ mol<sup>&minus;1</sup> (3 sf) (1).", "ms_extra": "Extended response question.", "ms_marks": "8"},
]


def extract_figures():
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(QP_PDF))
    for fig in FIGURES:
        page = doc[fig["page"] - 1]
        rect = fitz.Rect(fig["x0"], fig["y0"], fig["x1"], fig["y1"])
        pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(2.5, 2.5))
        out_path = IMG_DIR / fig["filename"]
        pix.save(str(out_path))
        print(f"Saved figure: {out_path}")
    doc.close()


def main():
    extract_figures()
    data = json.loads(DB_PATH.read_text(encoding="utf-8"))
    data["papers"] = [p for p in data["papers"] if p["id"] != PAPER_ID]
    data["questions"] = [q for q in data["questions"] if q.get("paper") != PAPER_ID]
    data["papers"].append(PAPER_META)

    total_marks = 0
    for q in QUESTIONS:
        qnum = q["qnum"]
        qnum_slug = qnum.replace(".", "-")
        ms_rel = f"img/{PAPER_ID}/ms/q{qnum_slug}.png"
        ms_abs = ROOT / ms_rel
        render_official_markscheme_image(
            question_label=q["ms_label"],
            answers_html=q["ms_ans"],
            extra_html=q["ms_extra"],
            marks=q["ms_marks"],
            spec_ref=q["specRef"],
            output_path=str(ms_abs),
        )
        entry = {
            "id": f"{PAPER_ID}-q{qnum}",
            "paper": PAPER_ID,
            "year": PAPER_META["year"],
            "series": PAPER_META["series"],
            "unit": PAPER_META["unit"],
            "level": PAPER_META["level"],
            "question": qnum,
            "questionNumber": qnum,
            "page": PAGE_MAP[qnum],
            "marks": q["marks"],
            "topics": [q["specRef"]],
            "skills": [],
            "summary": q["stem"],
            "specRef": q["specRef"],
            "image": f"img/{PAPER_ID}/q{qnum_slug}.jpg",
            "markscheme": ms_rel,
            "figures": [f"img/{PAPER_ID}/{f}" for f in q.get("figures", [])],
        }
        if "crop_exclude_y" in q:
            entry["crop_exclude_y"] = q["crop_exclude_y"]
        data["questions"].append(entry)
        total_marks += q["marks"]

    DB_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Ingested {PAPER_ID}: {len(QUESTIONS)} questions, {total_marks} marks")


if __name__ == "__main__":
    main()

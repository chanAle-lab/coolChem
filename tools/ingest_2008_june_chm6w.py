import json
import os
import sys
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_official_markscheme import render_official_markscheme_image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")

PAPER_ID = "2008-june-chm6w"
QP_PDF = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471967992_a0217e33.pdf"
IMG_DIR = os.path.join(ROOT, "img", PAPER_ID)
MS_DIR = os.path.join(IMG_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

PAPER_OBJ = {
    "id": PAPER_ID,
    "year": 2008,
    "series": "June",
    "unit": "CHM6/W",
    "level": "A",
    "title": "CHM6/W – Synoptic Assessment",
    "date": "2008-06-19",
    "totalMarks": 40,
    "duration": "1 hour",
}

FIG_4_6 = f"img/{PAPER_ID}/fig-q4-6.jpg"
FIG_24_25 = f"img/{PAPER_ID}/fig-q24-25.jpg"
FIG_DIR = f"img/{PAPER_ID}/fig-directions.jpg"

# (qnum, page, ans, topics, skills, specRef, summary, note)
RAW_QS = [
    (1, 2, "A", ["Bonding"], ["Knowledge & Recall"], "3.1.3", "Identify the solid containing covalent bonds but not ionic bonds (C6H5COOH).", "Benzoic acid is molecular covalent; CuSO4, NH4Br, CH3NH3Cl are ionic."),
    (2, 2, "B", ["Atomic Structure"], ["Knowledge & Recall"], "3.1.1", "Identify the species with the same electronic arrangement as Li+ (Be2+).", "Li+ and Be2+ both have 2 electrons (1s2)."),
    (3, 2, "B", ["Acids & Bases"], ["Maths & Calculations"], "3.1.12", "Calculate the pH of a propanoic acid / sodium propanoate buffer (5.19).", "[H+] = Ka * 0.100 / 0.200 = 6.5e-6; pH = 5.19."),
    (4, 5, "B", ["Acids & Bases"], ["Application"], "3.1.12", "Identify the diagram representing a strong acid solution (B).", "Strong acid HX is completely dissociated into H3O+ and X-."),
    (5, 5, "D", ["Acids & Bases"], ["Application"], "3.1.12", "Identify the diagram representing a salt from a strong acid and NaOH (D).", "Contains Na+ and X- ions only (plus H2O)."),
    (6, 5, "C", ["Acids & Bases"], ["Application"], "3.1.12", "Identify the diagram representing a weak acid partially neutralised by NaOH (C).", "Buffer mixture containing HX, X-, and Na+."),
    (7, 6, "D", ["Amount of Substance"], ["Maths & Calculations"], "3.1.2", "Find which chloride solution precipitates the largest mass of AgCl.", "Moles Cl-: A=0.020, B=0.025, C=0.020, D=0.030*0.300*3=0.027 mol."),
    (8, 6, "C", ["Amount of Substance"], ["Maths & Calculations"], "3.1.2", "Calculate percentage by mass of Ti in a 95% TiO2 concentrate (57%).", "95 * 47.9 / 79.9 = 57.0%."),
    (9, 6, "A", ["Amount of Substance"], ["Maths & Calculations"], "3.1.2", "Find which N2O5 decomposition gives the largest mole fraction of O2.", "O2 mole fractions: A=1/2, B=0.5/1.5=1/3, C=0.5/2.5=1/5, D=1/3."),
    (10, 6, "C", ["Carboxylic Acids & Esters", "Alkenes"], ["Application"], "3.3.7", "Identify the correct statement about isopropyl ethanoate.", "Hydrolysis gives propan-2-ol, also formed by acid-catalysed hydration of propene."),
    (11, 7, "D", ["Polymers", "Haloalkanes"], ["Application"], "3.3.4", "Identify the reaction forming a chloroalkene monomer for addition polymerisation.", "Elimination of HCl from 1,2-dichloroethane gives chloroethene (vinyl chloride)."),
    (12, 7, "A", ["Polymers"], ["Application"], "3.3.10", "Identify which product reacts with butanedioic acid to form a condensation polymer.", "Epoxyethane + H2O gives ethane-1,2-diol, which forms a polyester with butanedioic acid."),
    (13, 7, "D", ["Amines"], ["Application"], "3.3.9", "Identify the product when excess bromomethane reacts with diethylamine.", "Exhaustive methylation forms the quaternary ammonium salt [CH3CH2N(CH3)2CH2CH3]+ Br-? Wait: diethylamine (CH3CH2)2NH + excess CH3Br -> [(CH3CH2)2N(CH3)2]+ Br- (D)."),
    (14, 8, "D", ["Aromatic Chemistry", "Synthesis"], ["Application"], "3.3.6", "Identify the reagents for the 4-step synthesis from 3-phenylpropanoyl chloride.", "1: AlCl3 (Friedel-Crafts); 2: NaBH4; 3: conc H2SO4; 4: Cl2."),
    (15, 8, "B", ["Amount of Substance"], ["Maths & Calculations"], "3.1.2", "Calculate volume of O2 at 295 K and 100 kPa for incomplete combustion of 0.10 mol butane (11 dm3).", "n(O2) = 0.45 mol; V = 0.45 * 8.31 * 295 / 100000 = 0.0110 m3 = 11 dm3."),
    (16, 9, "A", ["Amount of Substance"], ["Maths & Calculations"], "3.1.2", "Calculate percentage yield of phenyl benzoate from 1.20 g benzoyl chloride (47.3%).", "Theoretical = (1.20/140.5)*198 = 1.691 g; yield = 0.800/1.691 = 47.3%."),
    (17, 9, "C", ["Nomenclature & Isomerism", "Haloalkanes"], ["Application"], "3.3.1", "Count structural isomers of C2HBrClF3 including halothane (4).", "CF3CHBrCl, CF2BrCHFCl, CF2ClCHFBr, CFBrClCHF2 (4 structural isomers)."),
    (18, 9, "C", ["Group 7"], ["Knowledge & Recall"], "3.2.3", "Identify the correct trend statement (reducing ability of halide ions increases down Group 7).", "Larger halide ions lose an outer electron more easily."),
    (19, 9, "C", ["Group 7", "Transition Metals"], ["Knowledge & Recall"], "3.2.3", "Identify the correct inorganic statement (AgBr dissolves in conc NH3 to form [Ag(NH3)2]+).", "AgBr dissolves in concentrated NH3(aq) to form [Ag(NH3)2]+."),
    (20, 10, "D", ["Electrode Potentials"], ["Application"], "3.1.11", "Identify the incorrect statement from E0 values for V, Cr, and Co half-cells.", "E0(VO2+/VO2+) = +1.00 V < E0(Co3+/Co2+) = +1.82 V, so VO2+ cannot oxidise Co2+."),
    (21, 11, "B", ["Transition Metals", "Haloalkanes"], ["Knowledge & Recall"], "3.2.8", "Identify reactions of NH3 that are substitution reactions (1 and 3 only).", "1: ligand substitution with [Cu(H2O)6]2+; 3: nucleophilic substitution with CH3Br."),
    (22, 11, "B", ["Amount of Substance", "Alkanes"], ["Maths & Calculations"], "3.1.2", "Identify hydrocarbons with 85.7% C by mass (empirical formula CH2: 1 and 3 only).", "1 (cyclopentane, C5H10) and 3 (methylcyclohexane, C7H14) have formula CnH2n."),
    (23, 12, "B", ["Kinetics"], ["Application"], "3.1.9", "Identify true statements for rate = k[X][Y]^2 (1 and 3 only).", "1: 2*1^2 = 2; 3: 3*3^2 = 27."),
    (24, 13, "D", ["Kinetics"], ["Data Analysis"], "3.1.9", "Identify true statements about Maxwell-Boltzmann curves P, Q, R, S (4 only).", "Only S (lower pressure/fewer molecules at same T -> lower peak at same energy) matches statement 4."),
    (25, 13, "B", ["Kinetics"], ["Application"], "3.1.9", "Identify diagrams showing changes that alter the rate constant k (1 and 3 only).", "Only temperature changes (P and R) alter k; catalyst and pressure/conc do not."),
    (26, 14, "A", ["Periodicity", "Acyl Derivatives"], ["Knowledge & Recall"], "3.2.5", "Identify substances forming acidic solutions in water (1, 2, and 3 only).", "AlCl3, Cl2, and CH3COCl form acidic solutions; NaCl is neutral."),
    (27, 14, "A", ["Bonding", "Transition Metals"], ["Knowledge & Recall"], "3.1.3", "Identify species with at least one 90 degree bond angle (1, 2, and 3 only).", "XeF4 (square planar, 90), PF5 (trigonal bipyramidal, 90), [Co(NH3)6]3+ (octahedral, 90)."),
    (28, 14, "C", ["Acids & Bases", "Transition Metals"], ["Knowledge & Recall"], "3.2.8", "Identify solutions that effervesce with solid Na2CO3 (2 and 4 only).", "HCOOH (carboxylic acid) and [Cr(H2O)6]3+ (strongly acidic 3+ aqua ion) liberate CO2."),
    (29, 14, "B", ["Equilibria", "Thermodynamics"], ["Application"], "3.1.10", "Identify true statements about endothermic decomposition of ClF3(g) (1 and 3 only).", "1: redox (Cl +3->0, F -1->0); 3: lower P shifts to more gas moles (RHS)."),
    (30, 15, "C", ["Aromatic Chemistry", "Acyl Derivatives"], ["Application"], "3.3.6", "Identify mechanism types in the 5-step aromatic synthesis (2 and 4 only).", "Nitration is electrophilic substitution (2); N-acylation of amine is nucleophilic addition-elimination (4)."),
    (31, 16, "D", ["Bonding"], ["Knowledge & Recall"], "3.1.3", "Identify substances where covalent bonds break on melting (4 only).", "Silicon dioxide is giant covalent; poly(ethene), Br2, and SO2 have intermolecular forces."),
    (32, 16, "A", ["Amino Acids & Proteins"], ["Application"], "3.3.11", "Identify true statements about aspartame (1, 2, and 3 only).", "Has NH2 & COOH (zwitterion), ester & amide links (alkaline hydrolysis), and 2 chiral centres."),
    (33, 16, "B", ["Redox", "Transition Metals"], ["Application"], "3.1.6", "Identify species that can act as both oxidising and reducing agents (1 and 3 only).", "CH3CHO (reduced to alcohol, oxidised to acid) and Fe2+ (reduced to Fe, oxidised to Fe3+)."),
    (34, 16, "B", ["Nomenclature & Isomerism"], ["Application"], "3.3.1", "Identify reactions forming a chiral product (1 and 3 only).", "1 gives CH3CHBrCH2CH3; 3 gives CH3CH2CH(OH)CN."),
    (35, 17, "C", ["Spectroscopy"], ["Application"], "3.3.12", "Identify compounds matching IR ~1700 cm-1, 2 NMR peaks, m/z 57 (2 and 4 only).", "Pentan-3-one (2 peaks, CH3CH2CO+ m/z 57) and 2,2-dimethylpropanal (2 peaks, (CH3)3C+ m/z 57)."),
    (36, 17, "A", ["Alkenes", "Aromatic Chemistry"], ["Application"], "3.3.4", "Identify true statements about tamoxifen (1, 2, and 3 only).", "Has C=C (addition, E/Z isomers) and benzene rings (Friedel-Crafts acylation); basic amine dissolves in HCl."),
    (37, 18, "B", ["Alkenes", "Carbonyls"], ["Application"], "3.3.4", "Identify mechanisms involved in reactions of ionone (1 and 3 only).", "C=C undergoes electrophilic addition (1); C=O undergoes nucleophilic addition (3)."),
    (38, 18, "C", ["Nomenclature & Isomerism"], ["Application"], "3.3.1", "Identify pairs of functional group isomers (2 and 4 only).", "2: carboxylic acid & ester; 4: ether & alcohol. 1 and 3 are position isomers."),
    (39, 18, "A", ["Periodicity"], ["Knowledge & Recall"], "3.2.5", "Identify correct statements about Period 3 chlorides and elements (1, 2, and 3 only).", "1: SiO2 ppt; 2: S8 > P4 VdW; 3: [Al(H2O)5(OH)]2+ formed; 4 false (SO2 + Br2 also formed)."),
    (40, 19, "B", ["Thermodynamics"], ["Application"], "3.1.8", "Identify true statements for N2O4(g) -> 2NO2(g) (1 and 3 only).", "Bond breaking -> Delta H > 0 (1); 1 mol gas -> 2 mol gas -> Delta S > 0 (3)."),
]


def extract_figures():
    doc = fitz.open(QP_PDF)
    crops = [
        (4, fitz.Rect(42, 65, 555, 520), FIG_4_6),      # Page 5: Q4-6 diagrams
        (12, fitz.Rect(42, 155, 555, 515), FIG_24_25),  # Page 13: Q24-25 M-B curves
        (11, fitz.Rect(140, 68, 460, 148), FIG_DIR),    # Page 12: Directions summarised
    ]
    for pno, rect, rel in crops:
        pix = doc[pno].get_pixmap(clip=rect, dpi=200)
        pix.save(os.path.join(ROOT, rel))
        print(f"Saved figure {rel}")


def main():
    extract_figures()
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    papers = [p for p in db["papers"] if p["id"] != PAPER_ID]
    papers.append(PAPER_OBJ)
    db["papers"] = papers

    questions = [q for q in db["questions"] if q.get("paper") != PAPER_ID]

    for qnum, page, ans, topics, skills, spec_ref, summary, note in RAW_QS:
        q_slug = f"q{qnum}"
        ms_rel = f"img/{PAPER_ID}/ms/{q_slug}.png"
        ms_abs = os.path.join(ROOT, ms_rel)
        render_official_markscheme_image(
            question_label=str(qnum),
            answers_html=f"<b>{ans}</b>",
            extra_html=note,
            marks="1",
            spec_ref=spec_ref,
            output_path=ms_abs,
        )
        figs = []
        if qnum in (4, 5, 6):
            figs.append(FIG_4_6)
        if qnum in (24, 25):
            figs.append(FIG_24_25)
        if qnum >= 21:
            figs.append(FIG_DIR)

        questions.append({
            "id": f"{PAPER_ID}-{q_slug}",
            "paper": PAPER_ID,
            "year": PAPER_OBJ["year"],
            "series": PAPER_OBJ["series"],
            "unit": PAPER_OBJ["unit"],
            "level": PAPER_OBJ["level"],
            "question": str(qnum),
            "questionNumber": str(qnum),
            "page": page,
            "marks": 1,
            "topics": topics,
            "skills": skills,
            "summary": summary,
            "specRef": spec_ref,
            "image": f"img/{PAPER_ID}/{q_slug}.jpg",
            "markscheme": ms_rel,
            "figures": figs,
        })

    db["questions"] = questions
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Ingested {PAPER_ID}: {len(RAW_QS)} questions, {len(RAW_QS)} marks.")


if __name__ == "__main__":
    main()

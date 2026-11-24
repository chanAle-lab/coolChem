"""Ingest AQA A-level Chemistry June 2019 Paper 2 (7405/2) into questions.json."""

import json
from pathlib import Path
import sys

import pymupdf as fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crop_official_markscheme import crop_official_markschemes

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "questions.json"
QP_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521544918_50b72016.pdf"
)
MS_PDF = Path(
    r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795521544932_f02c0ca8.pdf"
)

PAPER_ID = "2019-june-7405-2"
IMG_DIR = ROOT / "img" / PAPER_ID

PAPER_META = {
    "id": PAPER_ID,
    "year": 2019,
    "series": "June",
    "unit": "7405/2",
    "level": "A-level",
    "date": "2019-06-11",
    "title": "7405/2 — A-level Paper 2: Organic and Physical Chemistry (June 2019)",
    "totalMarks": 105,
    "pdf": None,
    "ms": None,
}

FIGURES = [
    {"filename": "fig-q4-table1.jpg", "page": 10, "x0": 40, "y0": 65, "x1": 555, "y1": 390},
    {"filename": "fig-q8-scheme.jpg", "page": 18, "x0": 40, "y0": 65, "x1": 555, "y1": 270},
    {"filename": "fig-q8-6-eq.jpg", "page": 20, "x0": 40, "y0": 245, "x1": 555, "y1": 565},
    {"filename": "fig-q9-fig2.jpg", "page": 22, "x0": 40, "y0": 65, "x1": 555, "y1": 525},
    {"filename": "fig-q12-fig4.jpg", "page": 29, "x0": 40, "y0": 65, "x1": 555, "y1": 435},
]

PAGE_MAP = {
    "01.1": 2, "01.2": 2, "01.3": 3, "01.4": 3, "01.5": 3,
    "02.1": 4, "02.2": 4, "02.3": 5, "02.4": 5, "02.5": 6,
    "03.1": 7, "03.2": 8, "03.3": 9, "03.4": 9,
    "04.1": 10, "04.2": 11, "04.3": 11,
    "05": 12,
    "06.1": 13, "06.2": 13, "06.3": 14, "06.4": 15,
    "07.1": 16, "07.2": 16,
    "08.1": 18, "08.2": 18, "08.3": 19, "08.4": 19, "08.5": 20, "08.6": 20, "08.7": 21,
    "09.1": 22, "09.2": 23, "09.3": 23, "09.4": 23,
    "10.1": 24, "10.2": 24, "10.3": 25, "10.4": 25, "10.5": 25,
    "11.1": 26, "11.2": 26, "11.3": 27, "11.4": 27, "11.5": 28, "11.6": 28,
    "12.1": 29, "12.2": 29, "12.3": 29,
    "13.1": 30, "13.2": 30,
}

QUESTIONS = [
    {"qnum": "01.1", "specRef": "3.3.11", "marks": 2, "stem": "Give an equation for the preparation of 1,6-diaminohexane from 1,6-dibromohexane and excess ammonia."},
    {"qnum": "01.2", "specRef": "3.3.11", "marks": 4, "stem": "Complete the mechanism for ammonia + 6-bromohexylamine and suggest a cyclic secondary amine by-product."},
    {"qnum": "01.3", "specRef": "3.3.11", "marks": 3, "stem": "Suggest reagents and conditions for the two-stage synthesis of 1,6-diaminohexane from 1,4-dibromobutane."},
    {"qnum": "01.4", "specRef": "3.3.11", "marks": 2, "stem": "Explain why 3-aminopentane is a stronger base than ammonia."},
    {"qnum": "01.5", "specRef": "3.3.7", "marks": 1, "stem": "Justify the statement that there are no chiral centres in 3-aminopentane."},
    {"qnum": "02.1", "specRef": "RP", "marks": 2, "stem": "Complete the diagram of the apparatus used to distil cyclohexene at 83 C."},
    {"qnum": "02.2", "specRef": "RP", "marks": 1, "stem": "State why cyclohexene can be separated from the aqueous solution using a separating funnel."},
    {"qnum": "02.3", "specRef": "RP", "marks": 1, "stem": "Give one observation to confirm that the cyclohexene dried with anhydrous CaCl2 was dry."},
    {"qnum": "02.4", "specRef": "3.1.2", "marks": 5, "stem": "Calculate the percentage yield of cyclohexene (4.15 cm3, d=0.810) from 14.4 g of cyclohexanol."},
    {"qnum": "02.5", "specRef": "3.3.4", "marks": 3, "stem": "Complete the mechanism for the reaction of cyclohexene with bromine."},
    {"qnum": "03.1", "specRef": "3.1.2", "marks": 4, "stem": "Deduce the molecular formula of isoprene (88.2% C by mass) and suggest a possible branched structure."},
    {"qnum": "03.2", "specRef": "3.3.4", "marks": 2, "stem": "Draw the skeletal formula and give the IUPAC name of the monomer for the repeating unit shown."},
    {"qnum": "03.3", "specRef": "3.3.1", "marks": 2, "stem": "Draw the stereoisomeric repeating unit of the third polymer and explain why stereoisomerism arises."},
    {"qnum": "03.4", "specRef": "3.3.12", "marks": 1, "stem": "Explain why polyalkene golf balls do not biodegrade."},
    {"qnum": "04.1", "specRef": "3.1.9", "marks": 1, "stem": "Complete Table 2 to show the initial rate of reaction of P in experiments 2 and 3."},
    {"qnum": "04.2", "specRef": "3.1.9", "marks": 2, "stem": "Determine the order of reaction with respect to P and with respect to Q.", "figures": ["fig-q4-table1.jpg"]},
    {"qnum": "04.3", "specRef": "3.1.9", "marks": 3, "stem": "Calculate the rate constant k and give its units for a reaction second order in R and second order in S."},
    {"qnum": "05", "specRef": "3.1.9", "marks": 4, "stem": "Calculate the Arrhenius constant A and its units from k = 3.46 x 10^-8 s^-1 at 25 C and Ea = 96.2 kJ mol^-1."},
    {"qnum": "06.1", "specRef": "3.3.5", "marks": 3, "stem": "Give a reagent and observations to distinguish between 2-methylbutan-1-ol and 2-methylbutan-2-ol."},
    {"qnum": "06.2", "specRef": "3.3.15", "marks": 2, "stem": "Draw structures for C4H8Br2 isomers A (singlet, triplet, quartet) and B (two singlets) from 1H NMR."},
    {"qnum": "06.3", "specRef": "3.3.15", "marks": 2, "stem": "Draw structures for C6H3Br3 isomers C (2 13C NMR peaks) and D (4 13C NMR peaks)."},
    {"qnum": "06.4", "specRef": "3.3.14", "marks": 1, "stem": "Label each IR spectrum in Figure 1 with the correct isomer E, F or G."},
    {"qnum": "07.1", "specRef": "3.3.1", "marks": 1, "stem": "Give the IUPAC name for isomer X (cyclopentanone)."},
    {"qnum": "07.2", "specRef": "3.3.15", "marks": 6, "stem": "Explain how and why isomers X and Y can be distinguished by boiling points, 13C NMR spectra and IR spectra."},
    {"qnum": "08.1", "specRef": "3.3.10", "marks": 1, "stem": "Name the mechanism of the reaction in Step 1 (phenol to 4-nitrophenol)."},
    {"qnum": "08.2", "specRef": "3.3.11", "marks": 1, "stem": "Complete the equation for the reduction of 4-nitrophenol to 4-aminophenol in Step 2.", "figures": ["fig-q8-scheme.jpg"]},
    {"qnum": "08.3", "specRef": "3.3.9", "marks": 2, "stem": "Complete the mechanism for the reaction of 4-aminophenol with ethanoyl chloride."},
    {"qnum": "08.4", "specRef": "3.3.9", "marks": 1, "stem": "Give one reason why ethanoyl chloride is not used in the industrial synthesis of paracetamol."},
    {"qnum": "08.5", "specRef": "3.3.9", "marks": 1, "stem": "Draw the structure of one other aromatic product formed in Step 3.", "figures": ["fig-q8-scheme.jpg"]},
    {"qnum": "08.6", "specRef": "3.3.9", "marks": 1, "stem": "Complete the equation for the reaction of hydroquinone with ammonium ethanoate to form paracetamol."},
    {"qnum": "08.7", "specRef": "3.1.2", "marks": 3, "stem": "Calculate the mass, in kg, of hydroquinone (Mr = 110.0) needed to produce 250 kg of paracetamol.", "figures": ["fig-q8-6-eq.jpg"]},
    {"qnum": "09.1", "specRef": "3.3.13", "marks": 1, "stem": "Suggest a suitable reagent for the hydrolysis of a protein."},
    {"qnum": "09.2", "specRef": "RP", "marks": 1, "stem": "Suggest how the positions of the amino acids on the TLC plate were located.", "figures": ["fig-q9-fig2.jpg"]},
    {"qnum": "09.3", "specRef": "3.3.16", "marks": 1, "stem": "Deduce the minimum number of amino acids present in the original mixture from Figure 2.", "figures": ["fig-q9-fig2.jpg"]},
    {"qnum": "09.4", "specRef": "3.3.16", "marks": 1, "stem": "Suggest why it was necessary to use two different solvents in the TLC.", "figures": ["fig-q9-fig2.jpg"]},
    {"qnum": "10.1", "specRef": "3.3.9", "marks": 3, "stem": "Deduce the molecular formula of a dicarboxylic acid with Mr = 118."},
    {"qnum": "10.2", "specRef": "3.1.2", "marks": 4, "stem": "Calculate the mass, in g, of the dicarboxylic acid used from the NaOH titration data."},
    {"qnum": "10.3", "specRef": "3.3.15", "marks": 1, "stem": "Deduce the number of peaks in the 1H NMR spectrum of hexane-2,5-diol."},
    {"qnum": "10.4", "specRef": "3.3.15", "marks": 1, "stem": "Draw the structure of a C6H14O2 diol whose 1H NMR spectrum consists of two singlet peaks."},
    {"qnum": "10.5", "specRef": "3.1.1", "marks": 1, "stem": "State why the dicarboxylic acid can be distinguished from the diols by high resolution ESI-MS."},
    {"qnum": "11.1", "specRef": "3.3.9", "marks": 3, "stem": "Complete the equation for propanoic anhydride + ethanol and give the IUPAC name of the ester."},
    {"qnum": "11.2", "specRef": "3.3.9", "marks": 2, "stem": "Draw the structure of the vegetable oil that reacts with methanol to form 2 mol C19H34O2 and 1 mol C19H36O2."},
    {"qnum": "11.3", "specRef": "3.3.1", "marks": 2, "stem": "Complete the skeletal formula of Z,Z-octadeca-9,12-dienoic acid to C14 showing Z stereochemistry."},
    {"qnum": "11.4", "specRef": "3.3.2", "marks": 1, "stem": "Give an equation for the complete combustion of the ester C19H34O2."},
    {"qnum": "11.5", "specRef": "3.3.14", "marks": 1, "stem": "State how the IR spectrum of CO2 in Figure 3 differs from what Table A predicts."},
    {"qnum": "11.6", "specRef": "3.3.14", "marks": 2, "stem": "Explain how carbon dioxide causes global warming."},
    {"qnum": "12.1", "specRef": "3.3.13", "marks": 2, "stem": "Draw all the hydrogen bonds between the complementary DNA strands in Figure 4."},
    {"qnum": "12.2", "specRef": "3.3.13", "marks": 2, "stem": "Draw a ring around each of the component parts of the cytosine nucleotide in Figure 4.", "figures": ["fig-q12-fig4.jpg"]},
    {"qnum": "12.3", "specRef": "3.3.13", "marks": 1, "stem": "State the meaning of the term complementary when referring to DNA strands."},
    {"qnum": "13.1", "specRef": "3.3.8", "marks": 5, "stem": "Show the first step of the mechanism of NaBH4 + 2-methylbutanal and explain why NaBH4 does not reduce 2-methylbut-1-ene."},
    {"qnum": "13.2", "specRef": "3.3.8", "marks": 2, "stem": "Give a reagent and observation to confirm incomplete reduction of 2-methylbutanal."},
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
    ms_map = crop_official_markschemes(
        MS_PDF,
        [q["qnum"] for q in QUESTIONS],
        IMG_DIR / "ms",
    )

    data = json.loads(DB_PATH.read_text(encoding="utf-8"))
    data["papers"] = [p for p in data["papers"] if p["id"] != PAPER_ID]
    data["questions"] = [q for q in data["questions"] if q.get("paper") != PAPER_ID]
    data["papers"].append(PAPER_META)

    total_marks = 0
    for q in QUESTIONS:
        qnum = q["qnum"]
        qnum_slug = qnum.replace(".", "-")
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
            "markscheme": f"img/{PAPER_ID}/ms/{ms_map[qnum]}",
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

"""
coolChem Streamlined Past Paper Ingestion Tool
---------------------------------------------
Automates the extraction, cropping, mark scheme alignment,
specification topic mapping, and questions.json indexing for AQA Chemistry past papers.
Automatically excludes old-spec Section B essay questions.
"""

import fitz  # PyMuPDF
from PIL import Image
import numpy as np
import os
import io
import re
import json
import argparse
import glob

# Specification Topic Mapping Rules
TOPIC_KEYWORDS = [
    # 3.1 Physical Chemistry
    ("3.1.1", ["mass number", "atomic number", "isotope", "relative atomic mass", "mass spectrometer", "mass spectrometry", "electronic configuration", "first ionisation energy", "ionisation energy", "electron gun", "accelerated", "deflected"]),
    ("3.1.2", ["avogadro", "ideal gas", "pv = nrt", "pv=nrt", "empirical formula", "molecular formula", "moles of", "mole of", "atom economy", "percentage yield", "titration", "standard solution", "hydrochloric acid of concentration"]),
    ("3.1.3", ["ionic crystal", "covalent bond", "co-ordinate bond", "dative", "metallic", "electronegativity", "permanent dipole", "van der waals", "hydrogen bond", "hydrogen bonding", "shape of", "shapes of", "vsepr", "bond angle", "sublimation", "melting point", "crystal structure", "intermolecular"]),
    ("3.1.4", ["standard enthalpy", "enthalpy of combustion", "enthalpy of formation", "mean bond enthalpy", "bond enthalpy", "calorimeter", "calorimetry", "heat energy evolved", "q = mc", "molar enthalpy change", "hess's law"]),
    ("3.1.5", ["rate of reaction", "activation energy", "maxwell–boltzmann", "maxwell-boltzmann", "collision theory", "catalyst", "higher temperature"]),
    ("3.1.6", ["dynamic equilibrium", "homogeneous", "le chatelier", "position of equilibrium", "equilibrium mixture", "kc", "kp"]),
    ("3.1.7", ["reduction in terms of electrons", "oxidation state", "half-equation", "redox", "oxidising agent", "reducing agent"]),
    ("3.1.8", ["lattice enthalpy", "born-haber", "entropy", "gibbs free energy", "free-energy"]),
    ("3.1.9", ["order of reaction", "rate equation", "arrhenius"]),
    ("3.1.10", ["equilibrium constant kp", "partial pressure"]),
    ("3.1.11", ["electrode potential", "electrochemical", "emf", "standard hydrogen electrode", "lithium ion"]),
    ("3.1.12", ["ph", "weak acid", "bronsted-lowry", "buffer", "ka", "kw", "neutralisation"]),

    # 3.2 Inorganic Chemistry
    ("3.2.1", ["period 3", "periodicity", "melting points of the period 3", "electrical conductivities of the elements", "extraction of aluminium", "extraction of titanium", "hall-heroult", "kroll"]),
    ("3.2.2", ["group 2", "group ii", "beryllium", "magnesium", "calcium", "barium", "solubility of hydroxides", "solubility of sulphates", "solubility of sulfates", "react with water"]),
    ("3.2.3", ["halogens", "group 7", "group vii", "electronegativity of the halogens", "chlorine", "bromine", "iodine", "concentrated sulphuric acid to separate solid", "aqueous chlorine to separate"]),
    ("3.2.4", ["period 3 oxides", "sodium oxide", "magnesium oxide", "aluminium oxide", "phosphorus(v) oxide", "sulfur dioxide"]),
    ("3.2.5", ["transition metal", "complex ion", "ligand", "ligand substitution", "octahedral", "tetrahedral", "variable oxidation state", "coloured ions", "catalytic properties of transition"]),
    ("3.2.6", ["aqueous metal ions", "precipitation with sodium hydroxide", "acidity of metal aqua ions", "chelate effect"]),

    # 3.3 Organic Chemistry
    ("3.3.1", ["structural isomers", "iupac", "nomenclature", "chain isomer", "position isomer", "functional group isomer", "geometrical isomer", "stereoisomerism", "e-z", "e/z", "but-2-ene"]),
    ("3.3.2", ["alkane", "cracking", "fractional distillation", "zeolite", "free-radical", "chloromethane can be prepared", "combustion of alkanes", "catalytic cracking"]),
    ("3.3.3", ["halogenoalkane", "nucleophilic substitution", "elimination", "potassium cyanide", "nitrile", "reacts less rapidly than", "1-bromobutane", "ozone"]),
    ("3.3.4", ["alkene", "electrophilic addition", "carbocation", "markovnikov", "hydrogen bromide to", "addition polymer", "ethene", "cyclohexene"]),
    ("3.3.5", ["alcohol", "pentan-1-ol", "pentan-2-ol", "ethanol", "fermentation", "hydration of ethene", "ethane-1,2-diol", "epoxyethane", "biofuel"]),
    ("3.3.6", ["infrared", "fingerprint region", "high resolution mass spectrometry"]),
    ("3.3.7", ["chiral", "enantiomer", "optical isomer", "non-superimposable", "plane-polarized"]),
    ("3.3.8", ["aldehyde", "ketone", "tollens", "fehling", "nucleophilic addition", "distinguish between the two oxidation products"]),
    ("3.3.9", ["carboxylic acid", "ester", "esterification", "hydrolysis", "propanoic acid", "biodiesel", "acyl chloride", "acid anhydride"]),
    ("3.3.10", ["benzene", "electrophilic substitution", "nitration", "friedel-crafts", "delocalisation energy"]),
    ("3.3.11", ["amine", "base strength of amines", "nucleophilic substitution of haloalkane with ammonia"]),
    ("3.3.12", ["condensation polymer", "polyester", "polyamide", "nylon", "kevlar", "terylene"]),
    ("3.3.13", ["amino acid", "zwitterion", "peptide link", "protein", "dna", "cisplatin"]),
    ("3.3.14", ["organic synthesis", "synthetic route", "target molecule"]),
    ("3.3.15", ["1h nmr", "13c nmr", "chemical shift", "splitting pattern", "integration factor", "tms"]),
    ("3.3.16", ["thin layer chromatography", "gas chromatography", "retention time", "rf value"])
]

def map_topics(text):
    text_lower = text.lower()
    matched = []
    for code, keywords in TOPIC_KEYWORDS:
        for kw in keywords:
            if kw in text_lower:
                matched.append(code)
                break
    if not matched:
        # Fallback to general physical or organic if undetected
        matched = ["3.1.1"]
    return matched[:3]

def infer_skills(text):
    text_lower = text.lower()
    skills = []
    if any(k in text_lower for k in ["calculate", "determine", "deduce", "volume", "mass", "empirical formula", "percentage", "moles", "pv=nrt", "equation"]):
        skills.append("maths")
    if any(k in text_lower for k in ["experiment", "apparatus", "describe the process", "detector", "calorimeter", "distinguish", "reagents", "observations", "observe", "test"]):
        skills.append("practical")
    if any(k in text_lower for k in ["explain", "suggest", "why", "difference", "compare", "justify", "trend", "mechanism", "reason", "outline"]):
        skills.append("analysis")
    if not skills or any(k in text_lower for k in ["define", "what is meant", "state", "name", "give the symbol", "write"]):
        skills.append("recall")
    return list(set(skills))

def detect_metadata(qp_doc):
    text = qp_doc[0].get_text()
    # Find year
    year_match = re.search(r'\b(19\d\d|20\d\d)\b', text)
    year = int(year_match.group(1)) if year_match else 2001

    # Find series
    series = "June" if "june" in text.lower() else "January" if "january" in text.lower() else "Summer"

    # Find unit code
    code_match = re.search(r'\b(CHM[1-9](?:/W)?)\b', text, re.IGNORECASE)
    code = code_match.group(1).upper() if code_match else "CHM1"

    # Find unit title
    unit_title = ""
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, l in enumerate(lines):
        if "unit" in l.lower() and i + 1 < len(lines):
            unit_title = lines[i+1]
            break

    clean_code_id = code.lower().replace('/', '')
    paper_id = f"{year}-{series.lower()}-{clean_code_id}"

    return {
        "id": paper_id,
        "year": year,
        "series": series,
        "date": f"{year}-06-12" if series == "June" else f"{year}-01-12",
        "code": code,
        "unit": f"Unit {code}: {unit_title}" if unit_title else f"Unit {code}",
        "level": "AS" if code in ["CHM1", "CHM2", "CHM3", "CHM3/W"] else "A",
        "spec": "AQA Chemistry",
        "duration": "1 hour 30 mins" if code in ["CHM1", "CHM2"] else "1 hour 15 mins"
    }

def crop_box(page, y0, y1, x0=25, x1=555, scale=2.0):
    rect = fitz.Rect(x0, max(0, y0), x1, min(page.rect.height, y1))
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=rect)
    im = Image.open(io.BytesIO(pix.tobytes("png")))
    return im.convert("RGB")

def find_ms_valleys(ms_page, num_valleys):
    pix = ms_page.get_pixmap(dpi=150)
    im = Image.open(io.BytesIO(pix.tobytes('png'))).convert('L')
    arr = np.array(im)
    # Count dark pixels per horizontal row in middle 80%
    dark_rows = np.sum(arr[:, int(im.width*0.1):int(im.width*0.9)] < 200, axis=1)
    return dark_rows

def parse_paper_section_a(qp_doc, ms_doc, paper_id, base_dir):
    img_dir = os.path.join(base_dir, "img", paper_id)
    os.makedirs(img_dir, exist_ok=True)

    questions = []
    current_q_num = None

    # Iterate over Question Paper pages (start from page 2, 0-indexed page 1)
    for p_idx in range(1, len(qp_doc)):
        qp_page = qp_doc[p_idx]
        text = qp_page.get_text()

        # Stop at SECTION B
        if "SECTION B" in text or "SECTION   B" in text:
            print(f"  [Info] Reached Section B at Page {p_idx+1}. Excluding Section B as requested.")
            break

        blocks = qp_page.get_text("blocks")
        # Filter headers/footers
        content_blocks = [b for b in blocks if 65 <= b[1] <= 780 and b[4].strip() and not b[4].strip().startswith("APW/") and not b[4].strip().startswith("LEAVE") and not b[4].strip().startswith("MARGIN")]
        if not content_blocks:
            continue

        sorted_blocks = sorted(content_blocks, key=lambda x: x[1])

        # Identify sub-question labels on this page
        subq_indices = []
        for idx, b in enumerate(sorted_blocks):
            b_txt = b[4].strip().replace('\n', ' ')
            # Match patterns like: "1 (a)", "(a)", "(b)(i)", "(i)", etc.
            match = re.match(r'^(?:(\d+)\s*)?(\([a-z\d]+\)(?:\([a-z\d]+\))?)\b', b_txt)
            if match:
                q_lead = match.group(1)
                sub_label = match.group(2)
                if q_lead:
                    current_q_num = q_lead
                subq_indices.append((idx, current_q_num, sub_label, b[1], b[3], b_txt))

        # Check for shared resource figure at the top of the page (before first sub-question)
        page_figures = []
        if subq_indices and subq_indices[0][0] > 0:
            first_sub_idx = subq_indices[0][0]
            pre_blocks = sorted_blocks[:first_sub_idx]
            pre_text = " ".join([b[4].strip() for b in pre_blocks])
            # Check if there's diagram or significant preamble (>40 chars or has visual/diagram)
            if len(pre_text) > 30 and ("SECTION" not in pre_text or len(pre_blocks) > 1):
                fig_y0 = max(70, pre_blocks[0][1] - 5)
                fig_y1 = pre_blocks[-1][3] + 10
                q_lead = subq_indices[0][1] or "res"
                fig_name = f"fig-p{p_idx+1}-q{q_lead}.jpg"
                fig_rel = f"img/{paper_id}/{fig_name}"
                fig_im = crop_box(qp_page, fig_y0, fig_y1, x0=35, x1=545)
                fig_im.save(os.path.join(base_dir, fig_rel), quality=85)
                page_figures.append(fig_rel)

        # Build individual sub-question crops
        if not subq_indices:
            continue

        ms_page = ms_doc[p_idx] if p_idx < len(ms_doc) else None

        for s_i, (b_idx, q_num, sub_lbl, y0, y1, txt) in enumerate(subq_indices):
            # Compute QP vertical bounds
            crop_y0 = max(70, y0 - 8)
            if s_i + 1 < len(subq_indices):
                crop_y1 = subq_indices[s_i + 1][3] - 6
            else:
                crop_y1 = min(qp_page.rect.height - 40, sorted_blocks[-1][3] + 15)

            # Combined question label, e.g. "1(a)" or "1(b)(i)"
            full_label = f"{q_num}{sub_lbl}" if q_num and not sub_lbl.startswith(q_num) else sub_lbl
            sub_id = full_label.replace('(', '').replace(')', '').replace(' ', '')
            q_id = f"{paper_id}-q{sub_id}"

            # Extract marks
            # Look forward through blocks belonging to this sub-question
            end_idx = subq_indices[s_i + 1][0] if s_i + 1 < len(subq_indices) else len(sorted_blocks)
            sub_blocks_text = " ".join([b[4].strip() for b in sorted_blocks[b_idx:end_idx]])
            mark_match = re.search(r'\((\d+)\s*marks?\)', sub_blocks_text, re.IGNORECASE)
            marks = int(mark_match.group(1)) if mark_match else 2

            # Summary
            first_sentence = re.sub(r'^(?:\d+\s*)?\([a-z\d]+\)(?:\([a-z\d]+\))?\s*', '', txt)
            first_sentence = first_sentence.replace('..', '').strip()
            summary = first_sentence[:95] if first_sentence else f"Question {full_label} response."

            # Topics and skills
            topics = map_topics(sub_blocks_text)
            skills = infer_skills(sub_blocks_text)

            # Crop Question
            q_rel = f"img/{paper_id}/q_q{sub_id}.jpg"
            q_im = crop_box(qp_page, crop_y0, crop_y1, x0=35, x1=545)
            q_im.save(os.path.join(base_dir, q_rel), quality=85)

            # Crop Mark Scheme
            ms_rel = f"img/{paper_id}/ms_q{sub_id}.jpg"
            if ms_page:
                # MS in old AQA has handwritten content on same page coordinates with slight buffer
                ms_y0 = max(60, crop_y0 - 5)
                ms_y1 = min(ms_page.rect.height, crop_y1 + 10)
                ms_im = crop_box(ms_page, ms_y0, ms_y1, x0=20, x1=560)
                ms_im.save(os.path.join(base_dir, ms_rel), quality=85)
            else:
                q_im.save(os.path.join(base_dir, ms_rel), quality=85)

            item = {
                "id": q_id,
                "paper": paper_id,
                "question": full_label,
                "marks": marks,
                "page": p_idx + 1,
                "topics": topics,
                "skills": skills,
                "summary": summary,
                "image": q_rel,
                "figures": list(page_figures),
                "markscheme": ms_rel
            }
            questions.append(item)

    return questions

def ingest_paper_pair(qp_path, ms_path, base_dir=r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"):
    print(f"\n=======================================================")
    print(f"Ingesting: {os.path.basename(qp_path)} & {os.path.basename(ms_path)}")
    print(f"=======================================================")

    doc_qp = fitz.open(qp_path)
    doc_ms = fitz.open(ms_path)

    meta = detect_metadata(doc_qp)
    paper_id = meta["id"]
    print(f"Detected Paper: {paper_id} ({meta['code']}, {meta['series']} {meta['year']})")

    questions = parse_paper_section_a(doc_qp, doc_ms, paper_id, base_dir)
    total_marks = sum(q["marks"] for q in questions)
    meta["totalMarks"] = total_marks

    print(f"Extracted {len(questions)} Section A questions (Total marks: {total_marks})")

    # Update questions.json
    q_json_path = os.path.join(base_dir, "questions.json")
    with open(q_json_path, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    # Replace or add paper meta
    data["papers"] = [p for p in data["papers"] if p["id"] != paper_id]
    data["papers"].append(meta)

    # Replace or add questions
    existing_ids = {q["id"] for q in questions}
    data["questions"] = [q for q in data["questions"] if q["id"] not in existing_ids]
    data["questions"].extend(questions)

    with open(q_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Successfully updated questions.json for {paper_id}!")
    return paper_id, len(questions), total_marks

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="coolChem Past Paper Ingestion Tool")
    parser.add_argument("--qp", help="Path to Question Paper PDF")
    parser.add_argument("--ms", help="Path to Mark Scheme PDF")
    parser.add_argument("--scan", help="Scan a directory for QP and MS pairs")
    args = parser.parse_args()

    if args.qp and args.ms:
        ingest_paper_pair(args.qp, args.ms)
    elif args.scan:
        pdf_files = glob.glob(os.path.join(args.scan, "*.pdf"))
        qp_files = [f for f in pdf_files if "-QP-" in os.path.basename(f) or "QP" in os.path.basename(f)]
        for qp in qp_files:
            ms_cand = qp.replace("-QP-", "-MS-").replace("QP", "MS")
            if os.path.exists(ms_cand):
                ingest_paper_pair(qp, ms_cand)
            else:
                print(f"[Warning] No matching MS for {qp}")
    else:
        print("Please provide --qp and --ms or --scan <folder>")

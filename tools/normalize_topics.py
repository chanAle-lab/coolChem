import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "questions.json")


def map_topic(t, q):
    unit = (q.get("unit") or "").upper()
    spec = q.get("specRef") or ""
    summ = (q.get("summary") or "").lower()

    if re.match(r"^3\.[123]\.\d+$", t) or t == "RP":
        return [t]

    if t in ("3.1", "3.2", "3.3"):
        # Drop bare section prefixes if the question already has specific 3.x.y topics,
        # otherwise map to the first topic in that section.
        return []

    if t == "Atomic Structure":
        return ["3.1.1"]
    if t == "Amount of Substance":
        return ["3.1.2"]
    if t == "Bonding":
        return ["3.1.3"]
    if t == "Energetics":
        return ["3.1.4"]
    if t in ("Kinetics", "Kinetics & Rate Equations"):
        if t == "Kinetics & Rate Equations" or unit in ("CHEM4", "CHM4") or spec.startswith("3.4.1"):
            if "rate constant" in summ or "rate equation" in summ or "order" in summ or "arrhenius" in summ or "initial rate" in summ or unit in ("CHEM4", "CHM4"):
                return ["3.1.9"]
        return ["3.1.5"]
    if t in ("Equilibria", "Equilibria & Kc"):
        if "kp" in summ or "partial pressure" in summ:
            return ["3.1.10"]
        return ["3.1.6"]
    if t in ("Redox", "Extraction of Metals"):
        return ["3.1.7"]
    if t == "Thermodynamics":
        return ["3.1.8"]
    if t in ("Electrode Potentials", "Redox & Electrode Potentials"):
        return ["3.1.11"]
    if t in ("Acids & Bases", "Acids, Bases & pH"):
        return ["3.1.12"]
    if t == "Periodicity":
        return ["3.2.1"]
    if t in ("Group 2", "Group 2 (Alkaline Earth Metals)"):
        return ["3.2.2"]
    if t in ("Group 7", "Group 7 (Halogens)", "Halogens"):
        return ["3.2.3"]
    if t in ("Periodicity (Period 3)", "Period 3 Oxides"):
        return ["3.2.4"]
    if t == "Transition Metals":
        return ["3.2.5"]
    if t in ("Aqueous Metal Ions", "Reactions of Ions in Aqueous Solution"):
        return ["3.2.6"]
    if t in ("Introduction to Organic Chemistry", "Nomenclature & Isomerism", "Nomenclature", "Isomerism", "Organic Chemistry"):
        if "optical" in summ or "enantiomer" in summ or "chiral" in summ or "stereoisomer" in summ and unit in ("CHEM4", "CHM4"):
            return ["3.3.7"]
        return ["3.3.1"]
    if t == "Alkanes":
        return ["3.3.2"]
    if t == "Haloalkanes":
        return ["3.3.3"]
    if t == "Alkenes":
        return ["3.3.4"]
    if t == "Alcohols":
        return ["3.3.5"]
    if t in ("Analytical Techniques", "Spectroscopy", "Infrared Spectroscopy", "Mass Spectrometry"):
        if "nmr" in summ or "chemical shift" in summ or "singlet" in summ or "doublet" in summ or "triplet" in summ or "quartet" in summ or "tms" in summ:
            return ["3.3.15"]
        if "chromatography" in summ or "retention" in summ or "rf" in summ:
            return ["3.3.16"]
        return ["3.3.6"]
    if t == "NMR Spectroscopy":
        return ["3.3.15"]
    if t == "Chromatography":
        return ["3.3.16"]
    if t == "Optical Isomerism":
        return ["3.3.7"]
    if t in ("Carbonyl Compounds", "Carbonyls"):
        return ["3.3.8"]
    if t == "Carbonyls & Carboxylic Acids":
        if "carboxylic" in summ or "ester" in summ or "acyl" in summ or "acid" in summ:
            return ["3.3.9"]
        return ["3.3.8"]
    if t in ("Carboxylic Acids & Esters", "Acylation", "Acyl Derivatives", "Acyl Chlorides"):
        return ["3.3.9"]
    if t == "Aromatic Chemistry":
        return ["3.3.10"]
    if t == "Amines":
        return ["3.3.11"]
    if t == "Polymers":
        return ["3.3.12"]
    if t == "Amino Acids & Proteins":
        return ["3.3.13"]
    if t == "Amino Acids & Polymers":
        if "polymer" in summ or "polyamide" in summ or "polyester" in summ:
            return ["3.3.13", "3.3.12"]
        return ["3.3.13"]
    if t in ("Organic Synthesis & Mechanisms", "Organic Synthesis", "Synthesis", "Reaction Mechanisms"):
        return ["3.3.14"]

    raise ValueError(f"Unmapped topic: {t!r} in {q.get('id')}")


def main():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    valid = {t["id"] for t in db["topics"]}
    changed = 0
    for q in db["questions"]:
        orig = q.get("topics", [])
        mapped = []
        for t in orig:
            for m in map_topic(t, q):
                if m not in mapped:
                    mapped.append(m)
        if not mapped and orig:
            # Fallback if only bare '3.1'/'3.2'/'3.3' was present
            for t in orig:
                if t in ("3.1", "3.2", "3.3"):
                    mapped.append(f"{t}.1")
        if mapped != orig:
            q["topics"] = mapped
            changed += 1
        for m in mapped:
            assert m in valid, f"Invalid mapped topic {m} on {q.get('id')}"

    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Normalized topics on {changed} questions across {len(db['questions'])} total questions.")


if __name__ == "__main__":
    main()

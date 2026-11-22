import json
import os

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")

def verify():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    questions = db["questions"]
    print(f"Total questions in database: {len(questions)}")

    missing_images = []
    missing_ms = []
    invalid_ms_key = []
    section_b_questions = []

    paper_counts = {}

    for q in questions:
        paper = q.get("paper", "unknown")
        paper_counts[paper] = paper_counts.get(paper, 0) + 1

        # Check image
        img_rel = q.get("image")
        if not img_rel:
            missing_images.append((q["id"], "No image field"))
        else:
            img_abs = os.path.join(REPO_DIR, img_rel.replace("/", os.sep))
            if not os.path.exists(img_abs) or os.path.getsize(img_abs) == 0:
                missing_images.append((q["id"], img_rel))

        # Check markscheme
        ms_rel = q.get("markscheme")
        if not ms_rel:
            invalid_ms_key.append(q["id"])
        else:
            ms_abs = os.path.join(REPO_DIR, ms_rel.replace("/", os.sep))
            if not os.path.exists(ms_abs) or os.path.getsize(ms_abs) == 0:
                missing_ms.append((q["id"], ms_rel))

        # Check Section B
        q_label = q.get("question", "")
        if "SECTION B" in q.get("description", "").upper():
            section_b_questions.append(q["id"])

    print("\n--- Summary per Paper ---")
    for paper in sorted(paper_counts.keys()):
        print(f"  {paper}: {paper_counts[paper]} questions")

    print("\n--- Integrity Results ---")
    print(f"Missing or empty question images: {len(missing_images)}")
    if missing_images:
        for item in missing_images[:10]:
            print("  ", item)

    print(f"Missing markscheme key in q: {len(invalid_ms_key)}")
    if invalid_ms_key:
        for item in invalid_ms_key[:10]:
            print("  ", item)

    print(f"Missing or empty markscheme images: {len(missing_ms)}")
    if missing_ms:
        for item in missing_ms[:10]:
            print("  ", item)

    print(f"Flagged Section B questions: {len(section_b_questions)}")
    if section_b_questions:
        for item in section_b_questions:
            print("  ", item)

    if not missing_images and not invalid_ms_key and not missing_ms and not section_b_questions:
        print("\nALL INTEGRITY CHECKS PASSED PERFECTLY!")

if __name__ == "__main__":
    verify()

import json
import os

repo = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
with open(os.path.join(repo, "questions.json"), "r", encoding="utf-8") as f:
    db = json.load(f)

papers = [
    "2003-june-chm1",
    "2003-june-chm2",
    "2003-june-chm3w",
    "2003-june-chm4",
    "2003-june-chm5",
    "2003-june-chm6w"
]

all_ok = True
total_june_questions = 0

for p in papers:
    qs = [q for q in db["questions"] if q["paper"] == p]
    total_june_questions += len(qs)
    print(f"\nPaper {p}: {len(qs)} questions")
    if not qs:
        print(f"  ERROR: No questions found for {p}!")
        all_ok = False
        continue
    missing_q_img = 0
    missing_ms_img = 0
    section_b_found = 0
    for q in qs:
        q_path = os.path.join(repo, q.get("image", "").replace("/", os.sep))
        ms_path = os.path.join(repo, q.get("markscheme", "").replace("/", os.sep))
        if not os.path.exists(q_path) or os.path.getsize(q_path) == 0:
            missing_q_img += 1
            print(f"  Missing question image: {q_path}")
        if not os.path.exists(ms_path) or os.path.getsize(ms_path) == 0:
            missing_ms_img += 1
            print(f"  Missing markscheme image: {ms_path}")
        # Check Section B
        if p != "2003-june-chm6w":
            m = q["question"]
            if (p == "2003-june-chm1" and m.startswith("5")) or \
               (p == "2003-june-chm2" and m.startswith("5")) or \
               (p == "2003-june-chm3w" and m.startswith("5")) or \
               (p == "2003-june-chm4" and (m.startswith("6") or m.startswith("7"))) or \
               (p == "2003-june-chm5" and (m.startswith("6") or m.startswith("7") or m.startswith("8") or m.startswith("9"))):
                section_b_found += 1
                print(f"  Section B question included: {q['id']} ({m})")

    print(f"  Missing question images: {missing_q_img}")
    print(f"  Missing mark scheme images: {missing_ms_img}")
    print(f"  Section B questions found: {section_b_found}")
    if missing_q_img > 0 or missing_ms_img > 0 or section_b_found > 0:
        all_ok = False

print(f"\nTotal June 2003 questions: {total_june_questions}")
print(f"Overall verification status: {'SUCCESS - ALL OK' if all_ok else 'FAILED'}")

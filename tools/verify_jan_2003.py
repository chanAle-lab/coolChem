import json
import os

repo_dir = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
questions_file = os.path.join(repo_dir, "questions.json")

with open(questions_file, "r", encoding="utf-8") as f:
    db = json.load(f)

jan03_papers = ["2003-jan-chm1", "2003-jan-chm2", "2003-jan-chm3w", "2003-jan-chm4", "2003-jan-chm5", "2003-jan-chm6w"]

print(f"Total papers in db: {len(db['papers'])}")
print(f"Total questions in db: {len(db['questions'])}")

total_jan03_q = 0
for pid in jan03_papers:
    p_obj = next((p for p in db["papers"] if p["id"] == pid), None)
    qs = [q for q in db["questions"] if q["paper"] == pid]
    total_jan03_q += len(qs)
    print(f"\nPaper {pid}: {p_obj['code']} - {p_obj['unit']} ({len(qs)} questions)")
    missing_q_img = 0
    missing_ms_img = 0
    missing_ms_txt = 0
    for q in qs:
        q_path = os.path.join(repo_dir, q["image"])
        ms_path = os.path.join(repo_dir, q["markscheme"])
        if not os.path.exists(q_path) or os.path.getsize(q_path) == 0:
            missing_q_img += 1
        if not os.path.exists(ms_path) or os.path.getsize(ms_path) == 0:
            missing_ms_img += 1
        if not q.get("markscheme_text"):
            missing_ms_txt += 1
    print(f"  Images check: missing_q_img={missing_q_img}, missing_ms_img={missing_ms_img}, missing_ms_txt={missing_ms_txt}")

print(f"\nTotal January 2003 questions: {total_jan03_q}")

sec_b_count = 0
for q in db["questions"]:
    if "section b" in q.get("summary", "").lower() or "section b" in q.get("question", "").lower() or "section b" in q.get("id", "").lower():
        sec_b_count += 1
print(f"Section B questions check across entire database: {sec_b_count} found.")

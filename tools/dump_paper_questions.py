import json
import sys

paper_id = sys.argv[1] if len(sys.argv) > 1 else "2001-jan-chm1"
with open("C:/Users/Alexander/.gemini/antigravity/scratch/coolChem/questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

qs = [q for q in data["questions"] if q.get("paper") == paper_id]
print(f"Total questions for {paper_id}: {len(qs)}")
for q in qs:
    print(f"{q['id']} | {q['question']} | {q['marks']}m | {q['topics']} | {q['markscheme']}")

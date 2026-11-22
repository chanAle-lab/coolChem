import os
import sys
import json
import re
import fitz

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.insert(0, REPO_DIR)
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")

with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

from tools.recrop_all_questions import PDF_MAP, extract_lines

targets = [
    ('2002-jan-chm1', 10),
    ('2002-june-chm5', 4),
    ('2003-jan-chm1', 5),
    ('2003-jan-chm1', 7),
    ('2003-jan-chm1', 8),
    ('2003-jan-chm3w', 5),
    ('2003-jan-chm4', 9),
]

for p, pg in targets:
    qs = [q for q in db['questions'] if q['paper'] == p and q['page'] == pg]
    print(f"\n==================== {p} Page {pg} ({len(qs)} questions in DB) ====================")
    for q in qs:
        print(f"  ID: {q['id']} | Q: {q['question']} | Marks: {q.get('marks')} | Desc: {q.get('description', '')[:50]}")

    # Now simulate recrop_all_questions
    doc = fitz.open(PDF_MAP[p])
    page = doc[pg - 1]
    q_list = qs
    lines = extract_lines(page)

    main_q_top = None
    for bbox, txt in lines:
        if bbox[0] < 70 and re.match(r'^\d+$', txt.strip()):
            main_q_top = (int(txt.strip()), bbox[1])
            break

    curr_y = 60.0
    located = []
    for q_idx, q in enumerate(q_list):
        q_label = q['question']
        m = re.match(r'^(\d+)?(?:\(([a-z\d]+)\))?(?:\(([a-z\d]+)\))?', q_label)
        main_q, sub1, sub2 = m.groups() if m else (None, None, None)

        parent_sub_y0 = None
        if sub2 and (q_idx == 0 or not q_list[q_idx-1]['question'].startswith(f"{main_q}({sub1})")):
            for bbox, txt in lines:
                if bbox[1] >= curr_y - 5 and bbox[0] < 120:
                    words = txt.split()
                    if words and words[0] == f"({sub1})":
                        parent_sub_y0 = bbox[1]
                        break

        candidates = []
        if sub2:
            candidates.append(f"({sub2})")
            if sub1:
                candidates.append(f"({sub1})({sub2})")
                candidates.append(f"({sub1}) ({sub2})")
        elif sub1:
            candidates.append(f"({sub1})")
            if main_q:
                candidates.append(f"{main_q} ({sub1})")
                candidates.append(f"{main_q}({sub1})")
        elif main_q:
            candidates.append(main_q)

        found_y0 = None
        search_start = parent_sub_y0 if parent_sub_y0 is not None else curr_y
        for bbox, txt in lines:
            if bbox[1] >= search_start - 5:
                for cand in candidates:
                    if bbox[0] < 140:
                        words = txt.split()
                        if (words and (words[0] == cand or txt.startswith(cand))) or txt == cand:
                            found_y0 = bbox[1]
                            break
                if found_y0 is not None:
                    break

        actual_y0 = parent_sub_y0 if parent_sub_y0 is not None else found_y0
        located.append((q, found_y0, actual_y0))
        if found_y0 is not None:
            curr_y = found_y0 + 10.0

    print("  --- Calculated y0, y1 ---")
    for i, (q, ly0, start_y0) in enumerate(located):
        if ly0 is None:
            print(f"    ERROR: Could not locate {q['id']}")
            continue
        if i == 0:
            m = re.match(r'^(\d+)', q['question'])
            q_num = int(m.group(1)) if m else None
            if main_q_top and q_num and main_q_top[0] == q_num and main_q_top[1] < start_y0:
                y0 = max(68.0, main_q_top[1] - 8.0)
            else:
                y0 = max(68.0, start_y0 - 8.0)
        else:
            y0 = max(68.0, start_y0 - 8.0)

        if i + 1 < len(located) and located[i+1][2] is not None:
            y1 = located[i+1][2] - 6.0
        else:
            after_lines = [
                l for l in lines 
                if l[0][1] >= ly0 and l[0][3] < 785 
                and 'Turn over' not in l[1] 
                and 'APW/' not in l[1] 
                and not re.match(r'^\d+$', l[1].strip())
            ]
            if after_lines:
                last_y = max(l[0][3] for l in after_lines)
                y1 = min(775.0, last_y + 18.0)
            else:
                y1 = min(775.0, ly0 + 120.0)
        print(f"    {q['id']} ({q['question']}): ly0={ly0:.1f}, start_y0={start_y0:.1f} => y0={y0:.1f}, y1={y1:.1f}")


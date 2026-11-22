import os
import sys
import json
import fitz

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
sys.path.insert(0, REPO_DIR)
from tools.recrop_all_questions import PDF_MAP, extract_lines

cases = [
    {
        "name": "Case 1 & 2: 2002-jan-chm1 page 10 (Q5(b), Q5(d))",
        "paper": "2002-jan-chm1",
        "page": 10,
        "questions": ["2002-jan-chm1-q5ai", "2002-jan-chm1-q5aii", "2002-jan-chm1-q5b", "2002-jan-chm1-q5c", "2002-jan-chm1-q5d"]
    },
    {
        "name": "Case 3: 2002-june-chm5 page 4 (Q2(c))",
        "paper": "2002-june-chm5",
        "page": 4,
        "questions": ["2002-june-chm5-q2a", "2002-june-chm5-q2b", "2002-june-chm5-q2c"]
    },
    {
        "name": "Case 4: 2003-jan-chm1 page 5 (Q1(e)(iii))",
        "paper": "2003-jan-chm1",
        "page": 5,
        "questions": ["2003-jan-chm1-q1ei", "2003-jan-chm1-q1eii", "2003-jan-chm1-q1eiii", "2003-jan-chm1-q1eiv"]
    },
    {
        "name": "Case 5: 2003-jan-chm1 page 7 (Q3(b))",
        "paper": "2003-jan-chm1",
        "page": 7,
        "questions": ["2003-jan-chm1-q3a", "2003-jan-chm1-q3b", "2003-jan-chm1-q3c", "2003-jan-chm1-q3d"]
    },
    {
        "name": "Case 6: 2003-jan-chm1 page 8 (Q4(a)(iii))",
        "paper": "2003-jan-chm1",
        "page": 8,
        "questions": ["2003-jan-chm1-q4ai", "2003-jan-chm1-q4aii", "2003-jan-chm1-q4aiii", "2003-jan-chm1-q4b", "2003-jan-chm1-q4c", "2003-jan-chm1-q4di", "2003-jan-chm1-q4dii", "2003-jan-chm1-q4diii"]
    },
    {
        "name": "Case 7: 2003-jan-chm3w page 5 (Q1(c)(iii))",
        "paper": "2003-jan-chm3w",
        "page": 5,
        "questions": ["2003-jan-chm3w-q1cii", "2003-jan-chm3w-q1ciii", "2003-jan-chm3w-q1di", "2003-jan-chm3w-q1dii"]
    },
    {
        "name": "Case 8: 2003-jan-chm4 page 9 (Q4(b)(ii))",
        "paper": "2003-jan-chm4",
        "page": 9,
        "questions": ["2003-jan-chm4-q4a", "2003-jan-chm4-q4bi", "2003-jan-chm4-q4bii", "2003-jan-chm4-q4c"]
    }
]

for c in cases:
    print(f"\n=======================================================")
    print(f"=== {c['name']} ===")
    doc = fitz.open(PDF_MAP[c['paper']])
    page = doc[c['page'] - 1]
    lines = extract_lines(page)
    print(f"Total lines extracted: {len(lines)}")
    for bbox, txt in lines:
        if any(term in txt for term in ['(a)', '(b)', '(c)', '(d)', '(e)', '(i)', '(ii)', '(iii)', '(iv)', 'marks']):
            print(f"  [{bbox[0]:.1f}, {bbox[1]:.1f}, {bbox[2]:.1f}, {bbox[3]:.1f}] : {txt}")

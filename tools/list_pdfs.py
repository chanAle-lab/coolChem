import os, glob, fitz

user_dir = r"C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded"
files = [
    "media_1795377960848_e3a53879.pdf",
    "media_1795377960711_d83e0ad2.pdf",
    "media_1795377960748_db71a865.pdf",
    "media_1795377960738_8da10bc5.pdf",
    "media_1795377960796_2ea4f9d8.pdf",
    "media_1795377960886_d6991030.pdf",
    "media_1795377960892_cf20d3cb.pdf",
    "media_1795377960916_d1c191c7.pdf",
    "media_1795377961025_154c822a.pdf",
    "media_1795377960895_e3fc9c52.pdf",
    "media_1795377960893_0b31f8c4.pdf",
    "media_1795377961015_0dd0a392.pdf"
]

for fname in files:
    fpath = os.path.join(user_dir, fname)
    doc = fitz.open(fpath)
    found = []
    for p in range(min(3, len(doc))):
        t = doc[p].get_text()
        for u in ["CHM1", "CHM2", "CHM3", "CHM4", "CHM5", "CHM6"]:
            if u in t:
                found.append(f"{u}(p{p+1})")
        if "Mark scheme" in t or "Mark Scheme" in t:
            found.append("MS")
        if "SECTION A" in t:
            found.append("SecA")
    print(f"{fname} ({len(doc)}p): {', '.join(set(found))}")

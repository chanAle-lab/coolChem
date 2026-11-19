import fitz
import glob
import os

pdf_dir = "C:/Users/Alexander/.gemini/antigravity/brain/8512efd8-03d2-4069-bf73-26ca25b72d40/.user_uploaded"
for pdf in sorted(glob.glob(os.path.join(pdf_dir, "*.pdf"))):
    try:
        doc = fitz.open(pdf)
        first_page = doc[0].get_text() if len(doc) > 0 else ""
        lines = [line.strip() for line in first_page.split("\n") if line.strip()][:5]
        print(f"{os.path.basename(pdf)} ({len(doc)} pages): {' | '.join(lines)}")
    except Exception as e:
        print(f"{os.path.basename(pdf)}: {e}")

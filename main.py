import os
import json
import fitz  # PyMuPDF

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    font_sizes = {}
    heading_candidates = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        size = round(span["size"], 1)

                        if len(text) == 0:
                            continue

                        font_sizes[size] = font_sizes.get(size, 0) + 1

                        heading_candidates.append({
                            "text": text,
                            "font_size": size,
                            "page": page_num,
                            "flags": span["flags"],
                            "bbox": span["bbox"],
                        })

    sorted_sizes = sorted(font_sizes.items(), key=lambda x: -x[0])
    size_to_level = {}
    for i, (size, _) in enumerate(sorted_sizes[:3]):
        size_to_level[size] = f"H{i+1}"

    def is_heading_candidate(item):
        """Decide whether a text span is likely a heading."""
        size = item["font_size"]
        text = item["text"]
        flags = item["flags"]
        y_pos = item["bbox"][1]  

        is_bold = bool(flags & 2)
        is_upper = text.isupper()
        is_top = y_pos < 200  
        size_ranked = size in size_to_level

        score = 0
        if size_ranked: score += 1
        if is_bold: score += 1
        if is_upper: score += 1
        if is_top: score += 1

        return score >= 2 

    outline = []
    title = None
    for item in heading_candidates:
        if is_heading_candidate(item):
            level = size_to_level.get(item["font_size"])
            if level:
                if level == "H1" and title is None:
                    title = item["text"]
                outline.append({
                    "level": level,
                    "text": item["text"],
                    "page": item["page"]
                })

    return {
        "title": title if title else "Untitled Document",
        "outline": outline
    }

def process_pdfs():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            print(f"Processing {filename}...")
            result = extract_headings(input_path)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    process_pdfs()

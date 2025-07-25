# 📄 PDF Outline Extractor – Adobe India Hackathon 2025 (Round 1A)

## 🧠 Challenge: Connecting the Dots Through Docs

This solution extracts a structured outline from a given PDF — including the **document title**, and **headings (H1, H2, H3)** along with their **page numbers** — using font-size–based logic. It's lightweight, offline-ready, and fully Dockerized.

---

## 👥 Team Members

- DharmaReddy Polam  
- Sathvika Nellutla  
- Vaishnavi Pingili  

---

## ✅ Features

- 🔍 Extracts:
  - `title` (first H1)
  - Headings: `H1`, `H2`, `H3` with `text` and `page` number
- 🔠 Supports multilingual documents (e.g., Japanese, Hindi, Chinese)
- 🐳 Dockerized and runs on `linux/amd64` architecture
- 🧠 Font-size–based logic (not hardcoded rules)
- ⚡ Fast and offline (≤10s for a 50-page PDF)
- ❌ No API/web calls, no GPU required

---

## 📦 Dependencies

All dependencies are installed inside the Docker container via:

```txt
PyMuPDF

🛠️ How to Build and Run (Documentation Only)
Adobe’s evaluation system will build and run the container as per their automated pipeline.

🔨 Build Docker Image
docker build --platform linux/amd64 -t pdf-outline:abc123 .

▶️ Run Docker Container
Linux/Mac:
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-outline:abc123

Windows CMD/PowerShell:
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output --network none pdf-outline:abc123
🧪 Sample Output Format
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
💡 Approach
We use PyMuPDF to extract all text spans from each page.

Each span includes font size, text, and position info.

The 3 most frequently used largest font sizes are mapped to H1, H2, and H3.

The first H1 becomes the document title.

All headings are structured into an output JSON with level and page info.

🈺 Multilingual Support
Thanks to Unicode support in PyMuPDF, the solution extracts and processes text in:

Japanese (日本語)

Hindi (हिंदी)

Chinese (中文)

Arabic, Russian, and other languages.

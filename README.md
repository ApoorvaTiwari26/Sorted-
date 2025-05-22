# Sorted!
An OCR-based question extraction system using Tesseract and PDF2Image in Python. Converts PDFs to images, preprocesses them, and uses Tesseract OCR to extract and identify questions chapter-wise using regex. Built with libraries like OpenCV, NumPy, and PIL for image handling.

---

## Tech Stack

- **Language:** Python 3
- **OCR Engine:** Tesseract OCR
- **PDF to Image Conversion:** PDF2Image
- **Image Processing:** OpenCV, NumPy, PIL
- **Regex Matching:** re (Regular Expressions)
- **Environment:** Google Colab

---

## Working

- Converts PDF pages into high-resolution images
- Applies image preprocessing for better OCR accuracy
- Extracts text using Tesseract OCR
- Uses regex to identify and group questions chapter-wise
- Displays debug output for verification and refinement

---

## How to Use

## Clone the Repository

```bash
git clone https://github.com/your-username/ocr-question-extractor.git
cd ocr-question-extractor
```

## Install Dependencies

Make sure Python is installed, then install the required libraries:

```bash
pip install pytesseract pdf2image opencv-python pillow numpy
sudo apt-get install -y tesseract-ocr poppler-utils
```

## Run the Extractor

1. **Place your PDF file** in the root directory of the project.

2. **Run the script:**

```bash
python main.py
```

(Ensure your script is saved as `main.py` or modify accordingly.)

3. **Follow the prompts to input your PDF file name.**

## PDF Requirements

The uploaded PDF should:

- Contain scanned or printed question papers
- Have clear, high-resolution text (preferably 300 DPI)
- Use English language content

## Output

The system will:

- Convert each PDF page to an image
- Apply OCR to extract text
- Use regex to group questions by chapter (e.g., `1a)`, `b)`, `c)`)
- Display structured output in the terminal

---

## Example Match Patterns

- `1a)`
- `1. a)`
- `2 a)`
- Follow-up questions: `b)`, `c)`, `d)`

---

## Notes

- Accuracy depends on the quality of the scanned PDF.
- For best results, use clean, high-resolution documents.

---


Built by Apoorva Tiwari (https://github.com/ApoorvaTiwari26)

# Sorted!
An OCR-based question extraction system using Tesseract and PDF2Image in Python. Converts PDFs to images, preprocesses them, and uses Tesseract OCR to extract and identify questions chapter-wise using regex. Built with libraries like OpenCV, NumPy, and PIL for image handling.

---

## 🔧 Tech Stack

- **Language:** Python 3
- **OCR Engine:** Tesseract OCR
- **PDF to Image Conversion:** PDF2Image
- **Image Processing:** OpenCV, NumPy, PIL
- **Regex Matching:** re (Regular Expressions)
- **Environment:** Google Colab

---

## 🚀 Features

- Converts PDF pages into high-resolution images
- Applies image preprocessing for better OCR accuracy
- Extracts text using Tesseract OCR
- Uses regex to identify and group questions chapter-wise
- Displays debug output for verification and refinement

---

## 📂 How to Use

1. **Setup Environment** (on Google Colab):

```bash
!pip install pytesseract pdf2image
!apt-get install -y tesseract-ocr poppler-utils
```

2. **Upload PDF:**

```python
from google.colab import files
uploaded = files.upload()
pdf_path = next(iter(uploaded))
```

3. **Run OCR Pipeline:**

```python
ocr_text = extract_text_from_pdf(pdf_path)
process_questions(ocr_text)
```

4. **Functions Overview:**

- `preprocess_image(image)`: Converts image to grayscale, applies blur and thresholding.
- `extract_text_from_pdf(pdf_path)`: Converts PDF to images, performs OCR.
- `process_questions(text)`: Uses regex to group questions by chapter.

---

## 📝 Output

The output will show:
- Total number of pages processed
- First 300 characters of OCR'd text per page
- Grouped questions by chapter numbers (like Chapter 1, 2, etc.)

---

## ✅ Example Match Patterns

- `1a)`
- `1. a)`
- `2 a)`
- Follow-up questions: `b)`, `c)`, `d)`

---

## 📌 Notes

- Accuracy depends on the quality of the scanned PDF.
- For best results, use clean, high-resolution documents.
- If no text is detected, verify preprocessing steps or consider tuning OCR parameters.

---

## 📬 Contact

For questions or contributions, feel free to reach out!

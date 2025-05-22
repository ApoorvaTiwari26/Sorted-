!pip install pytesseract pdf2image
!my-get install -y tesseract-ocr
!apt-get install -y poppler-utils
import pytesseract
from pdf2image import convert_from_path
import re
from collections import defaultdict
import numpy as np
import cv2
from PIL import Image
from google.colab import files


def preprocess_image(image):
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Image.fromarray(binary)


def extract_text_from_pdf(pdf_path):
    print("Converting PDF to images...")
    images = convert_from_path(pdf_path, dpi=300)  
    print(f"Converted {len(images)} pages into images.")

    full_text = ""


    print("Running OCR on each image...")
    for i, image in enumerate(images):
        enhanced_image = preprocess_image(image)
        text = pytesseract.image_to_string(enhanced_image, lang="eng", config="--psm 6")
        full_text += text
        print(f"Processed page {i + 1}: {text[:300]}...")  

    if not full_text.strip():
        print("OCR failed to extract text. Check the PDF or preprocessing.")
    return full_text


def process_questions(text):
    chapter_questions = defaultdict(list)
    current_chapter = None

    
    start_pattern = re.compile(r"^(\d+)\.?\s*a\)", re.IGNORECASE)  
    subpart_pattern = re.compile(r"^[b-d]\)", re.IGNORECASE) 
    print("Processing questions using regex...")

       for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        print(f"Processing line: {line}") 

       
        start_match = start_pattern.match(line)
        if start_match:
            current_chapter = start_match.group(1) 
            chapter_questions[current_chapter].append(line)  

       
        elif current_chapter and subpart_pattern.match(line):
            chapter_questions[current_chapter].append(line) 

    if chapter_questions:
        print("Questions grouped by chapters:")
        for chapter, questions in chapter_questions.items():
            print(f"Chapter {chapter}:")
            for question in questions:
                print(f"  - {question}")
    else:
        print("No questions identified. Check OCR output or adjust regex.")


uploaded = files.upload()
pdf_path = next(iter(uploaded))  

ocr_text = extract_text_from_pdf(pdf_path)
process_questions(ocr_text)

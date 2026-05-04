import easyocr
import cv2
import os
import re

INPUT_FOLDER = "images"
OUTPUT_FILE = "extracted_numbers.txt"

# Initialize OCR reader
reader = easyocr.Reader(['en'], gpu=False)

def extract_numbers(text):
    results = []

    # Fix common OCR mistakes
    text = text.replace("O", "0").replace("I", "1").replace("l", "1")

    # Match +91 XXXXX XXXXX and variations
    matches = re.findall(r'\+?\s*9\s*1[\s\-]?\d{5}[\s\-]?\d{5}', text)

    for m in matches:
        digits = re.sub(r'\D', '', m)

        if len(digits) == 12 and digits.startswith("91"):
            results.append("+91 " + digits[2:7] + " " + digits[7:])

    return results


def process_image(path):
    img = cv2.imread(path)

    if img is None:
        print(f"Skipping: {path}")
        return []

    # Run OCR
    result = reader.readtext(img, detail=0)

    full_text = " ".join(result)

    return extract_numbers(full_text)


def main():
    all_numbers = set()

    files = [f for f in os.listdir(INPUT_FOLDER)
             if f.lower().endswith((".jpg", ".png", ".jpeg"))]

    for file in files:
        print(f"Processing: {file}")
        path = os.path.join(INPUT_FOLDER, file)

        nums = process_image(path)
        all_numbers.update(nums)

    with open(OUTPUT_FILE, "w") as f:
        for num in sorted(all_numbers):
            f.write(num + "\n")

    print(f"\n✅ Done. Extracted {len(all_numbers)} numbers.")


if __name__ == "__main__":
    main()
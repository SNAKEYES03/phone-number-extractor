import easyocr
import cv2
import os
import re
import argparse

def extract_numbers(text, output_format):
    results = []

    # Fix common OCR issues
    text = text.replace("O", "0").replace("I", "1").replace("l", "1")

    matches = re.findall(r'\+?\s*9\s*1[\s\-]?\d{5}[\s\-]?\d{5}', text)

    for m in matches:
        digits = re.sub(r'\D', '', m)

        if len(digits) == 12 and digits.startswith("91"):
            if output_format == "compact":
                results.append("+" + digits)
            else:  # spaced
                results.append("+91 " + digits[2:7] + " " + digits[7:])

    return results


def process_image(path, reader, output_format, debug):
    img = cv2.imread(path)
    if img is None:
        print(f"Skipping: {path}")
        return []

    # Optional upscale
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    result = reader.readtext(img, detail=0)
    text = " ".join(result)

    if debug:
        print(f"\n--- OCR ({path}) ---\n{text[:500]}\n")

    return extract_numbers(text, output_format)


def main():
    parser = argparse.ArgumentParser(description="Extract +91 phone numbers from images")

    parser.add_argument("--input", required=True, help="Folder containing images")
    parser.add_argument("--output", default="output.txt", help="Output file")
    parser.add_argument("--format", choices=["spaced", "compact"], default="spaced")
    parser.add_argument("--dedupe", choices=["true", "false"], default="true")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    reader = easyocr.Reader(['en'], gpu=False)

    all_numbers = set() if args.dedupe == "true" else []

    files = [f for f in os.listdir(args.input)
             if f.lower().endswith((".jpg", ".png", ".jpeg"))]

    for file in files:
        print(f"Processing: {file}")
        path = os.path.join(args.input, file)

        nums = process_image(path, reader, args.format, args.debug)

        if args.dedupe == "true":
            all_numbers.update(nums)
        else:
            all_numbers.extend(nums)

    # Save output
    with open(args.output, "w") as f:
        for num in sorted(all_numbers):
            f.write(num + "\n")

    print(f"\n✅ Done. Extracted {len(all_numbers)} numbers.")


if __name__ == "__main__":
    main()

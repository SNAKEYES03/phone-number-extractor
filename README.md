# Phone Number Extractor

A Python CLI tool to extract Indian phone numbers (`+91 XXXXX XXXXX`) from images using OCR.

---

## Features

* Batch processing of multiple images
* OCR-based extraction using EasyOCR
* 🇮🇳 Detects Indian phone numbers (+91 format)
* Supports multiple output formats:

  * `+91 XXXXX XXXXX` (spaced)
  * `+911234567890` (compact)
* Optional duplicate removal
* Debug mode for OCR inspection

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/phone-number-extractor.git
cd phone-number-extractor
```

### 2. (Optional but recommended) Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / WSL
# OR
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
phone-number-extractor/
│── tool.py
│── images/              # input images
│── output.txt           # generated output
│── requirements.txt
```

---

## Usage

Basic usage:

```bash
python tool.py --input images
```

---

## Available Options

### Input folder

```bash
--input images
```

### Output file

```bash
--output output.txt
```

### Format options

```bash
--format spaced     # +91 98765 43210 (default)
--format compact    # +911234567890
```

### Remove duplicates

```bash
--dedupe true       # default
--dedupe false      # keep duplicates
```

### Debug mode (shows OCR output)

```bash
--debug
```

---

## Examples

### Default extraction

```bash
python tool.py --input images
```

### Compact format

```bash
python tool.py --input images --format compact
```

### Keep duplicates

```bash
python tool.py --input images --dedupe false
```

### Debug OCR output

```bash
python tool.py --input images --debug
```

---

## Example Output

```
+91 12345 67890
+91 12345 67890
```

---

## Notes

* Works best with **clear screenshots (e.g. WhatsApp chat lists)**
* OCR accuracy depends on image quality
* First run may download EasyOCR models (~100MB)

---

## Built With

* Python
* EasyOCR
* OpenCV
* Regex

---

## Future Improvements

* GUI interface
* Export to CSV / Excel
* Contact name extraction
* WhatsApp-specific layout parsing

---

## Contributing

Pull requests are welcome. For major changes, open an issue first.



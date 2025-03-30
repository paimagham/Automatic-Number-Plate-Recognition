# Automatic Number Plate Recognition (ANPR)

## Description
This project implements an **Automatic Number Plate Recognition (ANPR)** system using OpenCV and Tesseract OCR. It processes car images to detect, segment, and extract number plates.

## Installation

1. Install **Python** (version 3.6+ recommended).
2. Install required libraries:
   ```bash
   pip install opencv-python imutils pytesseract
   ```
3. Download and install **Tesseract OCR**:
   - [Tesseract Download Link](https://github.com/UB-Mannheim/tesseract/wiki)
   - After installation, set the path in the script:
     ```python
     pytesseract.pytesseract.tesseract_cmd = 'path/to/tesseract.exe'
     ```
4. Install **PyCharm** (optional but recommended):
   - [Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=linux)

## Usage

1. Place an image of a car (`car.jpg`) in the project folder.
2. Run the script:
   ```bash
   python anpr.py
   ```
3. The script will:
   - Load and resize the image
   - Convert it to grayscale
   - Reduce noise
   - Detect edges
   - Identify the number plate region
   - Extract and recognize text from the plate using Tesseract OCR

## Code Breakdown

### **Assignment 1: Preprocessing**
- Load and resize the image
- Convert to grayscale
- Reduce noise
- Detect edges

### **Assignment 2: Contour Detection**
- Find and draw contours to identify possible plate regions.

### **Assignment 3: Sorting Contours**
- Sort contours based on size.
- Select the most prominent ones.

### **Assignment 4: Locating the Number Plate**
- Detect four-sided contours that match the shape of a number plate.

## Example Output
*(Screenshots or sample output here)*

## Contributors
- **Bhavitha**

## License
This project is licensed under the **MIT License**.


from PIL import Image
import pytesseract

# Set path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ✅ Function to detect Hindi script in text
def detect_language(text):
    return "hi" if any('\u0900' <= c <= '\u097F' for c in text) else "en"

# ✅ Function to extract text from an image using specified language
def extract_text_from_image(image, lang_code="eng"):
    try:
        # Extract text
        text = pytesseract.image_to_string(image, lang=lang_code).strip()

        # Detect actual language in extracted text
        actual_lang = detect_language(text)
        return text if text else ("No text detected.")
    except Exception as e:
        return f"OCR Error: {e}"

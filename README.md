# Seeing beyond Sight: An AI-based Assistive System for the Visually Impaired 🤖👁️

An AI-based assistive system designed to help visually impaired individuals understand their surroundings through image analysis, object detection, text reading, and personalized assistance.

## 📁 Project Structure 

```
├── app.py                              # Main Streamlit application UI entry point  
├── image_to_text_using_langchain.py    # Alternative scene understanding implementation using LangChain  
├── requirements.txt                    # Python dependencies list   
│   
├── utils/
│   ├── __init__.py                     # Package initialization    
│   ├── scene_understanding.py          # Generates scene descriptions using Gemini    
│   ├── object_detection.py             # YOLO-based object detection     
│   ├── ocr_processing.py               # Extracts text from images (OCR)       
│   ├── text_to_speech.py               # Converts text to audio files        
│   └── personalized_assistance.py     # Provides conversational assistance via voice query
   
└── keys/
    └── gemini_key.txt                  # Stores Google Gemini API key  

```

## 🌟 Features

- **📸 Image Input**: Upload images or capture from webcam
- **🖼️ Scene Understanding**: Generate detailed descriptions of images using Gemini AI
- **🔍 Object Detection**: Detect and identify objects in real-time using YOLO
- **📝 OCR & Text Reading**: Extract and read text from images (supports English and Hindi)
- **🎤 Voice Commands**: Interact with the system using voice queries via speech recognition  
- **🤖 Personalized Assistance**: Get contextual answers about uploaded images using Gemini AI with natural language responses

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Frontend/UI | Streamlit |
| Computer Vision | OpenCV, PIL, Ultralytics (YOLO) |
| OCR | Tesseract (pytesseract) |
| Speech Recognition | SpeechRecognition, pyaudio |
| Text-to-Speech | pyttsx3, gTTS |
| AI/LLM | Google GenerativeAI (Gemini) |

## 📋 Prerequisites

### 1. Install Python Dependencies
   
```
bash
pip install -r requirements.txt
```

### 2. Additional Setup Required

#### Tesseract OCR Engine ⚠️ IMPORTANT FOR WINDOWS USERS:
Download and install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki). Update the path in `utils/ocr_processing.py` if needed:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesserakt\tesseract.exe"
```

#### API Key Configuration:
Add your Google Gemini API key in `keys/gemini_key.txt`

```
# keys/gemini_key.txt format:
YOUR_API_KEY_HERE


```

## 🚀 How to Run the Application

```
bash
streamlit run app.py --server.port 8501 --server.address localhost --server.headless true 
```

Or simply:

```
bash  
streamlit run app.py 
```

Then open your browser at `http://localhost:8501`


## 💻 Usage Examples

### Example 1: Scene Understanding
```
Input: Upload an image of a busy street scene
Output: "A busy city street with multiple vehicles including cars, buses, and motorcycles. 
         There are pedestrians walking on sidewalks on both sides. Traffic lights are visible 
         at an intersection nearby."
```

### Example 2: Object Detection  
```
Input: Upload an image containing various objects
Output: Detected Objects:
        - 3 person(s)
        - 2 car(s)
        - 1 bus(es)
        Positions shown with bounding boxes and confidence scores"
```

### Example 3: Text Reading (OCR)
```
Input: Upload an image with printed text (e.g., a signboard)
Output: Extracted text displayed on screen AND spoken aloud via TTS
        
Example Hindi text from image:
"दिल्ली मेट्रो रेल कॉर्पोरेशन लिमिटेड"
(Delhi Metro Rail Corporation Limited)"
```

### Example 4: Personalized Assistance via Voice Command
```
User speaks into microphone: "What is in this picture?"
System responds verbally:
"You asked: What is in this picture?
AI Response based on uploaded image content..."
```

---

## 🖥️ Installation for Other Operating Systems

### Linux (Ubuntu/Debian)

```
bash
# Install Python dependencies
pip install -r requirements.txt

# Install Tesseract OCR
sudo apt-get update && sudo apt-get install tesseract-ocr tesseract-ocr-hin

# Update path if needed in utils/ocr_processing.py:
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Run the application  
streamlit run app.py --server.port 8501 --server.address localhost --server.headless true 
```

For Hindi OCR support:
```
bash  
sudo apt-get install tesseract-ocr-hin  
```
  

---

### macOS  

```
bash  
# Install Python dependencies  
pip install -r requirements.txt  

# Install Tesseract OCR using Homebrew  
brew install tesseract tesseract-lang  

# Update path if needed in utils/ocr_processing.py:
pytesserract.pytesseraction.tesseraction_cmd = '/usr/local/bin/tesseraction'  

For Hindi language support may require additional configuration.
```
---

## ⚠️ Limitations

- **Internet Dependency**: Requires active internet connection for Gemini AI features
- **Language Support**: Primarily supports English and Hindi; other languages have limited OCR accuracy
- **Webcam Access**: Requires proper camera permissions and drivers installed
- **Audio Output Quality**: Text-to-speech quality depends on system audio drivers
- **Processing Time**: Large images may take longer to process with YOLO object detection

---

## 🔮 Future Work

- [ ] Add more language support for OCR (Hindi, Bengali, Tamil, etc.)
- [ ] Implement real-time video analysis for continuous assistance  
- [ ] Add GPS integration for location-based contextual information
- [ ] Improve voice command recognition with custom wake words
- [ ] Integrate with smart assistive devices (smart glasses, wearables)
- [ ] Add multi-modal output (Braille display support)
- [ ] Implement offline mode using local ML models where possible

---

###  Acknowledgements

1. **Google** - For providing the Gemini AI API that powers our scene understanding and personalized assistance features
   
2. **Ultralytics** - For developing YOLO which enables real-time object detection
   
3. **Tesseract OCR Team** - For the open-source optical character recognition engine


*🌍 Designed to make the world more accessible — because technology should empower everyone.*

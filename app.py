import streamlit as st
from PIL import Image
import os
import io
import pyttsx3
import tempfile
import speech_recognition as sr
import cv2

# ---------- Page Config ----------
st.set_page_config(page_title="Seeing Beyond Sight", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
    body, .stApp {background-color: #E8DAEF !important; color: #111 !important;}
    .main-title {font-size: 80px; text-align:center; font-weight:bold; font-family:'Brush Script MT', cursive; color:#8E44AD; margin-top:20px;}
    .subtitle {text-align:center; font-size:30px; font-weight:bold; font-family:'Alex Brush', cursive; color:#9B5986; margin-bottom:20px;}
    .feature-box {background:#FBEDED; border-radius:15px; padding:20px; margin:20px auto; width:95%; color:#6C3483; font-size:18px; font-family:'Pinyon Script', cursive; box-shadow:0 4px 12px rgba(0,0,0,0.1);}
    .feature-box:hover {background:#F9EBEA; transform:scale(1.01);}
    .stButton>button {background-color:#D98880; color:white; font-weight:bold; padding:10px 18px; border-radius:8px; margin-top:5px; margin-bottom:5px;}
    .stButton>button:hover {background-color:#B03A2E;}
</style>
""", unsafe_allow_html=True)

# ---------- Utilities ----------
from utils.scene_understanding import generate_scene_description
from utils.text_to_speech import text_to_speech
from utils.object_detection import detect_objects
from utils.personalized_assistance import provide_personalized_assistance
from utils.ocr_processing import extract_text_from_image

# ---------- Helper: Text-to-Speech ----------
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ---------- Header ----------
st.markdown("<div class='main-title'>Seeing Beyond Sight</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-Based Assistive System for the Visually Impaired</div>", unsafe_allow_html=True)

st.markdown("""
<div class='feature-box'>
<b>🌟 Features:</b>
<ul>
    <li>📸 Upload or Capture Images</li>
    <li>🔍 Object Detection</li>
    <li>📝 OCR & Text Reading</li>
    <li>🖼️ Scene Understanding</li>
    <li>🎤 Voice Commands</li>
    <li>🤖 Personalized Assistance</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------- Image Input ----------
input_method = st.radio("Select Input Method", ["Upload Image", "Use Webcam"])

image = None
if input_method == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
elif input_method == "Use Webcam":
    if st.button("Capture from Webcam"):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg").name
            cv2.imwrite(path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            image = Image.open(path)
        cap.release()

# ---------- Display Selected Image ----------
if image:
    st.image(image, caption="Selected Image", use_column_width=True)

    # ---------- Action Buttons ----------
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Scene Understanding"):
            img_bytes = io.BytesIO()
            image.save(img_bytes, format=image.format)
            result = generate_scene_description(img_bytes.getvalue())
            st.subheader("🖼️ Scene Description")
            st.write(result)
            speak_text(result)
    with col2:
        if st.button("Text Reading"):
            text = extract_text_from_image(image)
            st.subheader("📝 Extracted Text")
            st.write(text or "No text found")
            speak_text(text or "No text found")
            text_to_speech(text, "audio/output.mp3")
            st.audio("audio/output.mp3")
    with col3:
        if st.button("Object Detection"):
            det_img, objects, positions = detect_objects(image)
            st.subheader("🔍 Object Detection")
            st.image(det_img, caption="Objects Detected")
            if objects:
                summary = ", ".join([f"{v} {k}(s)" for k, v in objects.items()])
                st.success(f"Detected: {summary}")
                speak_text("Detected: " + summary)
            else:
                st.warning("No objects detected.")
                speak_text("No objects detected.")
    with col4:
        if st.button("Personalized Assistance"):
            st.subheader("🧐 Personalized Assistance")
            response = provide_personalized_assistance(image)
            st.write(response)

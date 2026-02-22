import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os

# ✅ Speak text in English
def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech Error: {e}")

# ✅ Get voice query from user (English only)
def listen_to_user_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak_text("Please ask your question.")
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            query = recognizer.recognize_google(audio, language="en-IN")
            return query
        except sr.UnknownValueError:
            return "Sorry, I could not understand."
        except sr.RequestError:
            return "Could not connect to the speech service."

# ✅ Gemini Integration for personalized assistance
def provide_personalized_assistance(image):
    try:
        with open("keys/gemini_key.txt", "r") as f:
            api_key = f.read().strip()
        genai.configure(api_key=api_key)

        query = listen_to_user_query()
        if "sorry" in query.lower():
            speak_text(query)
            return query

        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        prompt = f"The user asked: {query}. Please assist based on the uploaded image."

        response = model.generate_content([image, prompt])
        if response and response.text:
            answer = response.text.strip()
            speak_text("You asked: " + query)
            speak_text(answer)
            return f"User: {query}\n\nAI: {answer}"
        else:
            msg = "I couldn't generate a helpful response."
            speak_text(msg)
            return msg

    except Exception as e:
        msg = f"Error: {str(e)}"
        speak_text(msg)
        return msg

from gtts import gTTS
import os
import time

def text_to_speech(text, output_audio_path="audio/output_audio.mp3", lang="en"):
    try:
        if not text.strip():
            text = "No text detected in the image." if lang == "en" else "छवि में कोई पाठ नहीं मिला।"

        # gTTS works reliably for both English and Hindi
        lang_code = 'hi' if lang == 'hi' else 'en'
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(output_audio_path)

        time.sleep(0.3)  # Give it time to save
    except Exception as e:
        raise RuntimeError(f"Error generating speech: {e}")

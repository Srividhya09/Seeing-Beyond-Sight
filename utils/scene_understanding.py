# import google.generativeai as genai
# from PIL import Image
# import io

# def generate_scene_description(image_bytes, language="en"):
#     # Read API key
#     with open("keys/gemini_key.txt", "r") as f:
#         key = f.read().strip()

#     # Configure generative AI
#     genai.configure(api_key=key)

#     # Load image from bytes
#     image = Image.open(io.BytesIO(image_bytes))

#     # Initialize Gemini model
#     model = genai.GenerativeModel(model_name="gemini-1.5-flash")

#     # Use specific prompts based on language
#     if language == "hi":
#         prompt = "कृपया इस छवि में जो कुछ भी हो रहा है उसका एक सरल, स्पष्ट और विस्तृत हिंदी वर्णन करें।"
#     else:
#         prompt = "Describe clearly what is happening in this image."

#     # Generate description
#     response = model.generate_content([prompt, image])

#     # Safety: fall back if Gemini returns nothing
#     description = response.text.strip() if hasattr(response, "text") else "No description generated."

#     return description

import google.generativeai as genai
from PIL import Image
import io

def generate_scene_description(image_bytes, language="en"):
    """
    Generates a description for an image using a valid Gemini model.
    Automatically selects a model that supports generate_content.
    """
    # Load API key
    with open("keys/gemini_key.txt", "r") as f:
        key = f.read().strip()
    genai.configure(api_key=key)

    # List all models and pick one that supports generate_content
    models = genai.list_models()
    valid_model_name = None
    for m in models:
        if "generateContent" in m.supported_generation_methods:
            # Optional: check if model supports image input
            valid_model_name = m.name
            break

    if not valid_model_name:
        raise RuntimeError("No suitable model found that supports generate_content.")

    # Initialize the model
    model = genai.GenerativeModel(model_name=valid_model_name)

    # Load image
    image = Image.open(io.BytesIO(image_bytes))

    # Prepare prompt
    if language == "hi":
        prompt = "कृपया इस छवि में जो कुछ भी हो रहा है उसका एक सरल, स्पष्ट और विस्तृत हिंदी वर्णन करें।"
    else:
        prompt = "Describe clearly what is happening in this image."

    # Generate description safely
    try:
        response = model.generate_content([prompt, image])
        description = response.text.strip() if hasattr(response, "text") else "No description generated."
    except Exception as e:
        description = f"Error generating description: {e}"

    return description


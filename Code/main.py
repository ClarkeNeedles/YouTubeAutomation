import os
import google.generativeai as genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Load API Key from .env file
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

def generate_script(topic):
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"Write a short, engaging video script under 60 seconds for: '{topic}'. Focus on being snappy and interesting."

    response = model.generate_content(prompt)

    return response.text.strip()

with open("output.txt", "w") as f:
  f.write(generate_script("The Science of Sleep"))

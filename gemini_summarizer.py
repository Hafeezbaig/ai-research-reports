import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_summary(topic):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Generate a concise research summary on the topic: {topic}. Use real-world examples, statistics, and make it suitable for a professional report."
    response = model.generate_content(prompt)
    return response.text.strip()

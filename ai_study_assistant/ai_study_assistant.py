# AI Study Assistant

import os
from google import genai

print("===== AI Study Assistant =====")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found.")
    print("Please set the GEMINI_API_KEY environment variable.")
else:
    client = genai.Client(api_key=api_key)

    topic = input("Enter a study topic: ")

    prompt = f"""
    You are a helpful study assistant.

    For the topic "{topic}", provide:

    1. A simple explanation
    2. Five important key points
    3. Three practice questions
    4. A short study plan

    Use simple language suitable for a beginner.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n===== AI Study Assistant Response =====")
    print(response.text)

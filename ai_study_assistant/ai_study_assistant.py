import os
from google import genai

print("===== AI STUDY ASSISTANT =====")

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    print("Please set your Gemini API key and try again.")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Get topic from user
topic = input("Enter a study topic: ")

# Create prompt
prompt = f"""
You are a helpful AI Study Assistant.

Explain the topic "{topic}" in simple words.

Provide:
1. A simple explanation
2. 5 important key points
3. 3 practice questions

Keep the explanation suitable for a college student.
"""

try:
    # Generate AI response
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    print("\n===== AI RESPONSE =====\n")
    print(response.text)

except Exception as e:
    print("\nError while connecting to Gemini API.")
    print("Please check your internet connection or API configuration.")
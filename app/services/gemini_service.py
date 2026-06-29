from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_ai_response(history):

    prompt = f"""
    You are Chat Nexus, an AI assistant.

    Rules:
    - Keep responses under 500 words.
    - Answer clearly and concisely.
    - For programming questions, give short explanations with small examples.
    - Do not give very lengthy answers.

    Conversation:
        {history}

    Assistant:
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        return (
            "Sorry, the AI service is currently busy. "
            "Please try again in a few moments."
        )
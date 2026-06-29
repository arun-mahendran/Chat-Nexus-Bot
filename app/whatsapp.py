from fastapi import APIRouter
import os
import requests
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


@router.get("/send")
def send_message():

    url = (
        f"https://graph.facebook.com/v23.0/"
        f"{PHONE_NUMBER_ID}/messages"
    )

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": "919629133841",
        "type": "text",
        "text": {
            "body": "Hello from FastAPI 🚀"
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return response.json()
from fastapi import APIRouter, Request, Query
import json
import requests
import os
from dotenv import load_dotenv
from app.services.gemini_service import get_ai_response

load_dotenv()

router = APIRouter()

VERIFY_TOKEN = "chat_nexus_verify"

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

def send_message(to, message):

    print("Sending to:", to)
    print("Message:", message)

    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }

    print(payload)

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("\n=== SEND MESSAGE RESPONSE ===")
    print("Status Code:", response.status_code)
    print("Response:", response.text)


@router.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge")
):

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)

    return {"error": "Verification failed"}


@router.post("/webhook")
async def receive_message(request: Request):

    data = await request.json()

    print(json.dumps(data, indent=4))

    try:
        message = (
            data["entry"][0]["changes"][0]
            ["value"]["messages"][0]["text"]["body"]
        )

        sender = (
            data["entry"][0]["changes"][0]
            ["value"]["messages"][0]["from"]
        )

        print("Message:", message)
        print("Sender:", sender)

        ai_reply = get_ai_response(message)

        # Limit response to 4000 characters
        ai_reply = ai_reply[:4000]

        send_message(
            "919629133841",
            ai_reply
        )

    except Exception as e:
        print("Error:", e)

    return {"status": "ok"}
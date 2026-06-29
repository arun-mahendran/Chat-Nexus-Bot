from app.services.gemini_service import get_ai_response

from app.services.memory_service import (
    save_message,
    get_history,
    clear_history
)

USER_ID = "arun"

while True:

    user_message = input("You: ")

    # Clear memory
    if user_message.lower() == "/clear":
        clear_history(USER_ID)
        print("\nBot: Conversation history cleared successfully.\n")
        continue

    save_message(
        USER_ID,
        "user",
        user_message
    )

    history = get_history(USER_ID)

    conversation = ""

    for role, msg in history:
        conversation += f"{role}: {msg}\n"

    print("\n=== Conversation Sent to Gemini ===")
    print(conversation)
    print("===================================\n")

    ai_reply = get_ai_response(conversation)

    print("\nBot:", ai_reply)

    save_message(
        USER_ID,
        "assistant",
        ai_reply
    )

    print("\n" + "-" * 50 + "\n")
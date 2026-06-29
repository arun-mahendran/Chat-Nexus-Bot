from app.services.memory_service import (
    save_message,
    get_history
)

save_message(
    "arun",
    "user",
    "My name is Arun"
)

history = get_history("arun")

print(history)
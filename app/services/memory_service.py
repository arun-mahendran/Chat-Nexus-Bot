import sqlite3

# Create database connection
conn = sqlite3.connect(
    "chat_memory.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    role TEXT,
    message TEXT
)
""")

conn.commit()


# Save message
def save_message(user_id, role, message):

    cursor.execute(
        """
        INSERT INTO chat_history
        (user_id, role, message)
        VALUES (?, ?, ?)
        """,
        (user_id, role, message)
    )

    conn.commit()


# Get chat history
def get_history(user_id):

    cursor.execute(
        """
        SELECT role, message
        FROM chat_history
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT 10
        """,
        (user_id,)
    )

    history = cursor.fetchall()

    return history[::-1]


# Clear chat history
def clear_history(user_id):

    cursor.execute(
        """
        DELETE FROM chat_history
        WHERE user_id = ?
        """,
        (user_id,)
    )

    conn.commit()
import os
import json
from groq import Groq
from dotenv import load_dotenv
from tools import get_time, get_date, say_hello

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Load chat history
try:
    with open("chat_history.json", "r") as file:
        messages = json.load(file)
except FileNotFoundError:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

print("AI Chatbot Started")
print("Type '/help' for commands\n")

while True:
    user_input = input("You: ")

    # Exit command
    if user_input.lower() in ["exit", "/exit"]:
        print("Goodbye!")
        break

    # Help command
    if user_input.lower() == "/help":
        print("""
Available Commands:
------------------
/help     - Show commands
/history  - Show stored messages
/clear    - Clear chat memory
/hello    - Say hello
/time     - Show current time
/date     - Show current date
/exit     - Exit chatbot
""")
        continue

    # History command
    if user_input.lower() == "/history":
        print(f"Total messages stored: {len(messages)}")
        continue

    # Clear command
    if user_input.lower() == "/clear":
        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]

        with open("chat_history.json", "w") as file:
            json.dump(messages, file, indent=4)

        print("Chat history cleared.")
        continue

    # Hello command
    if user_input.lower() == "/hello":
        print(say_hello())
        continue

    # Time command
    if user_input.lower() == "/time":
        print("Current Time:", get_time())
        continue

    # Date command
    if user_input.lower() == "/date":
        print("Today's Date:", get_date())
        continue

    # Add user message
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Send conversation history
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    bot_reply = response.choices[0].message.content

    print("Bot:", bot_reply)
    print()

    # Save assistant reply
    messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    # Save chat history
    with open("chat_history.json", "w") as file:
        json.dump(messages, file, indent=4)
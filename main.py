import os
from groq import Groq
from dotenv import load_dotenv

from tools import get_time, get_date, say_hello
from memory import load_messages, save_messages, clear_messages
from tool_selector import select_tool

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Load previous chat history
messages = load_messages()

# Available tools
tools = {
    "get_time": get_time,
    "get_date": get_date,
    "say_hello": say_hello
}

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
        messages = clear_messages()
        print("Chat history cleared.")
        continue

    # Manual commands
    if user_input.lower() == "/hello":
        print("Bot:", say_hello())
        continue

    if user_input.lower() == "/time":
        print("Bot:", get_time())
        continue

    if user_input.lower() == "/date":
        print("Bot:", get_date())
        continue

    # -----------------------
    # AI Tool Calling
    # -----------------------

    tool_name = select_tool(client, user_input)

    if tool_name in tools:
        result = tools[tool_name]()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"Tool result: {result}"
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        bot_reply = response.choices[0].message.content

        print("Bot:", bot_reply)
        print()

        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        messages.append(
            {
                "role": "assistant",
                "content": bot_reply
            }
        )

        save_messages(messages)

        continue

    # -----------------------
    # Normal Chat
    # -----------------------

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    bot_reply = response.choices[0].message.content

    print("Bot:", bot_reply)
    print()

    messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    save_messages(messages)
import json


def load_messages():
    try:
        with open("chat_history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]


def save_messages(messages):
    with open("chat_history.json", "w") as file:
        json.dump(messages, file, indent=4)


def clear_messages():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

    save_messages(messages)

    return messages
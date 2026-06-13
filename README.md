# AI Chatbot

A simple AI chatbot built with Python and the Groq API.

## Features

* LLM-powered conversations
* Persistent chat memory using JSON
* Modular code structure
* Custom commands:

  * /help
  * /history
  * /clear
  * /hello
  * /time
  * /date
  * /exit

## Technologies Used

* Python
* Groq API
* JSON
* python-dotenv

## Project Structure

AI Chatbot/
├── main.py
├── memory.py
├── tools.py
├── chat_history.json
├── .env
└── requirements.txt

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Create a `.env` file:

GROQ_API_KEY=your_api_key

3. Run:

python main.py

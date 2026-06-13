from groq import Groq
from dotenv import load_dotenv
import os

from pdf_reader import read_pdf
from chunker import chunk_text

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Read PDF
text = read_pdf("AI.pdf")

# Create chunks
chunks = chunk_text(text)

question = input("Ask a question: ")

# Find relevant chunk
relevant_chunk = ""

for chunk in chunks:
    if any(word.lower() in chunk.lower() for word in question.split()):
        relevant_chunk = chunk
        break

if relevant_chunk == "":
    relevant_chunk = chunks[0]

prompt = f"""
Answer the question using the context below.

Context:
{relevant_chunk}

Question:
{question}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nAnswer:")
print(response.choices[0].message.content)
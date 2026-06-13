from pdf_reader import read_pdf
from chunker import chunk_text

text = read_pdf("AI.pdf")

chunks = chunk_text(text)

print("Total Chunks:", len(chunks))
print()
print(chunks[0])
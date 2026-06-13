from pdf_reader import read_pdf

text = read_pdf("AI.pdf")

print(text[:1000])
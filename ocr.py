from bangla_pdf_ocr import process_pdf
path = "./data/book1.pdf"
output_file = "output.txt"
extracted_text = process_pdf(path, output_file)
print(extracted_text)

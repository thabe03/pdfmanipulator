import PyPDF2

pdf_file = open('0.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_reader.decrypt('')
pdf_writer = PyPDF2.PdfWriter()

pages = range(0,79)

for page_num in pages:
    pdf_writer.add_page(pdf_reader.pages[page_num])

with open('0_decrypt.pdf', 'wb') as new_file:
    pdf_writer.write(new_file)
pdf_file.close()

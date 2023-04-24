from PyPDF2 import PdfReader, PdfWriter

pdf_file_path = 'samp.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfReader(pdf_file_path)

pages = range(10,18)
pdfWriter = PdfWriter()

for page_num in pages:
    pdfWriter.add_page(pdf.pages[page_num])

with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
    pdfWriter.write(f)
    f.close()
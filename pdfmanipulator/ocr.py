import subprocess
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def ocr(chemin_fichier):
    chemin_sortie = '{0}_ocr.pdf'.format(chemin_fichier)
    arguments = ["ocrmypdf", "--skip-text", chemin_fichier, chemin_sortie]
    subprocess.run(arguments)

def merge(start_page,end_page):
    pdfs = [str(i)+'.pdf' for i in range(start_page, end_page)]
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result_merge.pdf")
    merger.close()

def extract(start_page,end_page,chemin_fichier):
    pdf_file_path = chemin_fichier
    file_base_name = pdf_file_path.replace('.pdf', '')
    pdf = PdfReader(pdf_file_path)
    pages = range(start_page,end_page)
    pdfWriter = PdfWriter()
    for page_num in pages:
        pdfWriter.add_page(pdf.pages[page_num])
    with open('{0}_extract.pdf'.format(file_base_name), 'wb') as f:
        pdfWriter.write(f)
        f.close()

def decrypt(chemin_fichier):
    pdf_file = open(chemin_fichier, 'rb')
    pdf_reader = PdfReader(pdf_file)
    pdf_reader.decrypt('')
    pdf_writer = PdfWriter()
    pages = range(len(pdf_writer.pages))
    for page_num in pages:
        pdf_writer.add_page(pdf_reader.pages[page_num])
    with open('{0}_decrypt.pdf', 'wb') as new_file:
        pdf_writer.write(new_file)
    pdf_file.close()

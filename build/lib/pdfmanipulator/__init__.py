import subprocess
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def ocr(chemin_fichier):
    """
    This Python function performs OCR (optical character recognition) on a given file and saves the
    output as a PDF file.
    
    :param chemin_fichier: The path to the input file that needs to be OCR'd (Optical Character
    Recognition)
    """
    chemin_sortie = '{0}_ocr.pdf'.format(chemin_fichier)
    arguments = ["ocrmypdf", "--skip-text", chemin_fichier, chemin_sortie]
    subprocess.run(arguments)

def merge(start_page,end_page):
    """
    This function merges multiple PDF files into a single PDF file.
    
    :param start_page: The starting page number of the PDF files to be merged
    :param end_page: The end page parameter specifies the last page number of the PDF files that need to
    be merged
    """
    pdfs = [str(i)+'.pdf' for i in range(start_page, end_page)]
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result_merge.pdf")
    merger.close()

def extract(start_page,end_page,chemin_fichier):
    """
    This function extracts a range of pages from a PDF file and saves them as a new PDF file.
    
    :param start_page: The starting page number from where the extraction should begin
    :param end_page: The end page parameter specifies the page number up to which the PDF file needs to
    be extracted
    :param chemin_fichier: The file path of the PDF file that needs to be extracted
    """
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
    """
    This function decrypts a PDF file and saves the decrypted version as a new file.
    
    :param chemin_fichier: The parameter "chemin_fichier" is a string that represents the file path of
    the PDF file that needs to be decrypted
    """
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

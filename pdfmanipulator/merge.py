from PyPDF2 import PdfMerger

pdfs = [str(i)+'.pdf' for i in range(0, 2)]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()


# import PyPDF2
# pdfFiles=["1.pdf","2.pdf"]
# merger=PyPDF2.PdfWriter()
# for pdf in pdfFiles:
#   merger.append(pdf)
  
# merger.write("merged-pdf.pdf")
# merger.close()
  
import PyPDF2
pdfFiles=["1.pdf","2.pdf"]
merger=PyPDF2.PdfWriter ()#*Pdfwriter to create new pdf file 
for file in pdfFiles:#*this loop will merge and append the pdf 
  merger.append(file)
  
merger.write("new-pdf.pdf")#*The write method creates a new PDF file named new-pdf.pdf containing all the appended pages from the original PDF files.
merger.close()


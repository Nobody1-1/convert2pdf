from docx2pdf import convert
from pdf2docx import Converter
import glob

# word file to pdf file converter
def docx_to_pdf(wordfile):
    pdffile = f"{wordfile.split('.')[0]}.pdf"
    convert(wordfile,pdffile)

# pdf file to word file converter
def pdf_to_word(pdffile):
    wordfile = f"{pdffile.split('.')[0]}.docx"
    cv = Converter(pdffile)
    cv.convert(wordfile)
    cv.close()

# docx_to_pdf("makalah_mulillalbab.docx") #your word/docx filename directory
pdf_to_word("LAPORAN KEGIATAN PAMERAN SENI RUPA.pdf") #your pdf filename directory

def all_docxtopdf():
    all_docx = glob.glob("*.docx")

    for filename in all_docx:
        pdffile = f"{filename.split('.')[0]}.pdf"
        convert(filename,pdffile)
    
# all_docxtopdf()
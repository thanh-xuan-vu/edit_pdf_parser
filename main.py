''' Use pdfminer or fitz to extract texts and images in an editable pdf file'''

import fitz
print(fitz.__doc__)
# from pathlib import Path


def parse_edit_pdf(f_path):

    # TODO: Normalize the f_path into pathlib path 
    print('================\nFile: {} is processing ...'.format(f_path))

    # Open the file with fitz
    doc = fitz.open(f_path)

    # Read the table of contents
    ToC = doc.get_toc()
    print('\nTable of contents (extracted): \n', ToC[:5])

    # Reading one page (numbering from 0)
    pageCount = doc.pageCount
    page_no = 35
    print('\nReading page {}/{}:'.format(page_no, pageCount))

    page = doc[page_no]
    textBlocks = page.getTextBlocks()   # contains all texts and images with bbox
    # print(textBlocks)
    text = page.getText()   # contains all the texts, header & footer are all on top
    print(text)
    pass


if __name__=='__main__':
    f_path = 'data/WorkCentre_5019-5021.pdf'
    parse_edit_pdf(f_path)
    pass 

import PyPDF2

with open('dummy.pdf', 'rb') as file: 
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.getNumPages())
    # rotate page - will need page number first. 
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    # instantiate a writer object.
    writer = PyPDF2.PdfFileWriter()
    # add the page to the write object.
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)


## MERGE TWO PDFs using the ARGS from the terminal. ###

import sys

inputs = sys.argv[1:] #grabs the first argument and the rest.

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')

pdf_combiner(inputs)


## ADD THE WATERMARK to all page of a document ###

template = PyPDF2.PdfFileReader(open('merged.pdf', 'rb')) # openinf file and saving it in a variable
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()): # range in getNumPage() to get the number of pages in the merged pdf and loop through each. 
    page = (template.getPage(i))
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as new_file:
        output.write(new_file)
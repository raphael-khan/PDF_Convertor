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
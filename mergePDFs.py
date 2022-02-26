# It creates a new pdf of containing the pages of all the pdfs of folder\
# in alphabetical order of the file names.
# The result file is named after the origin folder.

import os
from pikepdf import Pdf

# input origin, saveLocation, pdf_pass
origin = "C:/Users/<User>/Desktop/pdfs/" # Don't forget '/' at the end
saveLocation = origin
pdf_pass = "" # empty string if no pass


pdf = Pdf.new()
for file in os.listdir(os.fsencode(origin)):
   filename = os.fsdecode(file)

   pdfFile = Pdf.open(origin + filename, password=pdf_pass)
   pdf.pages.extend(pdfFile.pages)


name = origin.split('/')[-2]
pdf.save(saveLocation + name + "Merged.pdf")


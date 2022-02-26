# Works with folder containing pdfs that all use the same password. (You need to know the password!)
# Saves unprotected version of PDFs to specified location.

import os
import pikepdf  

# inputs: origin, saveLocation, pdf_pass
origin = "C:/Users/<user>/Desktop/" # end with '/'
saveLocation = "C:/Users/<user>/Desktop/"
pdf_pass = ""  # empty string if no password


for file in os.listdir(os.fsencode(origin)):
    filename = os.fsdecode(file)

    pdf = pikepdf.open(origin + filename, password=pdf_pass)
    pdf.save(saveLocation + filename)

    
# pip install pypdf2

from PyPDF2 import PdfFileMerger
import os

pdfs1 = ["1.pdf", "2.pdf"]
pdfs2 = ["1_1.pdf", "2_1.pdf"]
pdfsS = ["r/s1.pdf", "r/s2.pdf"]

os.mkdir("r")

for i in range(len(pdfs1)):
    fusionador = PdfFileMerger()
    nombre_archivo_salida = pdfsS[i]
    fusionador.append(open(pdfs1[i], 'rb'))
    fusionador.append(open(pdfs2[i], 'rb'))
    
    with open(nombre_archivo_salida, 'wb') as salida:
        fusionador.write(salida)
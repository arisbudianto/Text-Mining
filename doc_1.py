import docx
from docx import Document

# Buatlah sebuah file doc yang akan kita baca dan letakkan di D:\Project\Latihan
# Path bisa berubah
doc = open("latihan_baca.docx","rb")

# membuat word reader object
document = docx.Document(doc)

#membuat variabel yang kosong untuk temporary
docu=""
for para in document.paragraphs:
       docu += para.text
# Cetak dokumen
print(docu.encode("utf-8"))

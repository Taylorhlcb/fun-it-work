from pdfrw import PdfReader
pdf = PdfReader('setup.pdf')
print(pdf.Root.AcroForm.Fields)
print(len(pdf.Root.AcroForm.Fields))
for a in range(0,16):
    print(pdf.Root.AcroForm.Fields[a].T)
print(pdf.Root.AcroForm.Fields[1].T)
print('PDF has {} pages'.format(len(pdf.pages)))
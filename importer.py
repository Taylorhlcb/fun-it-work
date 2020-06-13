import json
import os
import pdfrw

with open('exported-csv.json', 'r') as f:
    dataset = json.load(f)

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def write_fillable_pdf(data_dict, row, input_pdf_path='setup.pdf', output_pdf_path='formatted{}.pdf'):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for a in range(0,len(template_pdf.pages)):
        annotations = template_pdf.pages[a][ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict[str(a)].keys():
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[str(a)][key]))
                        )
        pdfrw.PdfWriter().write(output_pdf_path.format(row), template_pdf)

for row_number, data in enumerate(dataset):
    with open('fields.json', 'r') as f:
        vals = json.load(f)
    vals["0"]["0"] = data[0]
    vals["1"]["1"] = data[0]
    write_fillable_pdf(vals, row_number)
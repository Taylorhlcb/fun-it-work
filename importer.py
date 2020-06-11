import json
import os

with open('exported-csv.json', 'r') as f:
    dataset = json.load(f)

# from shutil import copyfile
# for row in range(1,23):
#     if not os.path.isfile('formatted{}.pdf'.format(row)):
#         copyfile('setup.pdf', 'formatted{}.pdf'.format(row))
#     with open

import pdfrw


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def write_fillable_pdf(data_dict, row, input_pdf_path='setup.pdf', output_pdf_path='formatted{}.pdf'):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(output_pdf_path.format(row), template_pdf)

for row_number, data in enumerate(dataset):
    vals = {
        'Given Name Text Box': data[0],
        'Family Name Text Box': data[1],
        'House nr Text Box': data[2],
        'Postcode Text Box': data[3],
        'Address 1 Text Box': data[4],
        'Address 2 Text Box': data[5],
        'Postcode Text Box': data[6],
        'City Text Box': data[7],
    }
    write_fillable_pdf(vals, row_number)
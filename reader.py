import json
import pdfrw

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def get_fucking_weird_annotations(input_pdf_path='setup.pdf'):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    pages = {}
    for a in range(0,len(template_pdf.pages)):
        keyss = {}
        annotations = template_pdf.pages[a][ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    keyss[key] = '/data/'
        pages[a] = keyss
    with open('fields.json', 'w') as f:
        json.dump(pages, f, indent=2)
get_fucking_weird_annotations()
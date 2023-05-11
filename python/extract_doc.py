#!/usr/local/bin/python

'''
This script synchronously extracts structured data from the specified PDF and is limited to
PDFs of ~4.5MB or less with an extraction runtime under 30s (extractions rarely take
longer than 30s unless they require OCR). For more information
see https://docs.sensible.so/docs/api-tutorial-sync.
'''

import json
import requests

# The name of a document type in Sensible, e.g., auto_insurance_quote
DOCUMENT_TYPE = "YOUR_DOCUMENT_TYPE"
# The path to the PDF you'd like to extract from
# If the PDF is over ~4.5MB use an async example script in this repo instead
DOCUMENT_PATH = "YOUR_PDF.pdf"
# Your Sensible API key
API_KEY = "YOUR_API_KEY"


def extract_doc():
    headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),
        'Content-Type': 'application/pdf'
    }
    with open(DOCUMENT_PATH, 'rb') as pdf_file:
        body = pdf_file.read()
    response = requests.request(
        "POST",
        "https://api.sensible.so/v0/extract/{}".format(DOCUMENT_TYPE),
        headers=headers,
        data=body)
    try:
        response.raise_for_status()
    except requests.RequestException:
        print(response.text)
    else:
        print(json.dumps(response.json(), indent=2))


if __name__ == '__main__':
    extract_doc()

#!/usr/local/bin/python

'''
This script asynchronously extracts structured data from the specified PDF.
For more information, see https://docs.sensible.so/docs/api-tutorial-async-1.
'''

import time
import json
import requests

# The name of a document type in Sensible, e.g., auto_insurance_quote
DOCUMENT_TYPE = "YOUR_DOCUMENT_TYPE"
# The URL of the PDF you'd like to extract from
DOCUMENT_URL = "YOUR_PDF_URL"
# Your Sensible API key
API_KEY = "YOUR_API_KEY"


def extract_from_doc_url():
    headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),  'Content-Type': 'application/json'
    }
    body = json.dumps({"document_url": DOCUMENT_URL})
    response = requests.request(
        "POST",
        "https://api.sensible.so/v0/extract_from_url/{}".format(
            DOCUMENT_TYPE),
        headers=headers,
        data=body)
    try:
        response.raise_for_status()
    except requests.RequestException:
        print(response.text)
    else:
        document_extraction = response.json()
        poll_count = 0
        # In production you'd use a webhook to avoid polling
        while document_extraction["status"] == "WAITING":
            # Wait a few seconds for the extraction to complete on each iteration
            time.sleep(3)
            poll_count += 1
            response = requests.request(
                "GET",
                "https://api.sensible.so/v0/documents/{}".format(document_extraction['id']),
                headers=headers)
            try:
                response.raise_for_status()
            except requests.RequestException:
                print(response.text)
                break
            else:
                document_extraction = response.json()
                print("Poll attempt: {}, status: {}".format(
                    poll_count, document_extraction["status"]))
        print(json.dumps(document_extraction, indent=2))


if __name__ == '__main__':
    extract_from_doc_url()

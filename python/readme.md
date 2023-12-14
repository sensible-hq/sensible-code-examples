This starter code calls Sensible [extraction APIs](https://docs.sensible.so/reference#extract-data-from-a-document) and returns structured data from a PDF. You'll need an [API key](https://app.sensible.so/account/?t=api_keys).


Run
---
To run the code:

- Clone this repo.
- Open a command promt at this cloned directory:
  - To install dependencies, run `python -m pip install requests`.
- Open extract_docs.py in a text editor and specify:
  - your API key. Be sure to secure this key before committing.
  - the local path to your PDF.
  - the name of the doc type that you created in the [Sensible app](https://app.sensible.so/).
- Run `python extract_doc.py`. 

Run with examples
----

To see example data in a response quickly, run extract_doc.py with an example PDF and config:

- Clone this directory, install dependencies, and add your API key (see previous steps).
- Download an example [auto insurance quote PDF](https://github.com/sensible-hq/sensible-docs/blob/main/readme-sync/assets/v0/pdfs/auto_insurance_anyco.pdf).
- In the [Sensible app](https://app.sensible.so/):
    - Create a doc type, for example, `test_auto_insurance_quote`.
    - Create a config in the doc type, for example `anyco`.
    - Paste the [example JSON](https://github.com/sensible-hq/sensible-docs/raw/main/readme-sync/assets/v0/json/anyco.json) into the left pane of the config editor.
    - Publish the config: **Publish configuration** > **Production**.
- Open extract_doc.py in a text editor and specify:
  - the path to the example PDF you downloaded.
  - the name of the doc type you created.
- Run `python extract_doc.py`. 


 

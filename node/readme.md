This starter code calls Sensible [extraction APIs](https://docs.sensible.so/reference#extract-data-from-a-document) and returns structured data from a PDF. You'll need an [API key]([https://www.sensible.so/get-early-access](https://app.sensible.so/account/?t=api_keys)).


Run
---
To run the code:

- Clone this repo.
- To install dependencies, open a command prompt at this cloned directory and run `npm install`.
- Open extract-doc.js in a text editor and specify:
  - your API key. Be sure to secure this key before committing.
  - the local path to your PDF.
  - the name of the doc type that you created in the [Sensible app](https://app.sensible.so/).
- Run `node extract-docs.js`. 

Run with examples
----

To see example data in a response quickly, run extract-doc.js with an example PDF and config:

- Clone this directory, install dependencies, and add your API key (see previous steps).
- Download an example [auto insurance quote PDF](https://github.com/sensible-hq/sensible-docs/blob/main/readme-sync/assets/v0/pdfs/auto_insurance_anyco.pdf).
- In the [Sensible app](https://app.sensible.so/):
    - Create a doc type, for example, `test_auto_insurance_quote`.
    - Create a config in the doc type, for example `anyco`.
    - Paste the [example JSON](https://github.com/sensible-hq/sensible-docs/raw/main/readme-sync/assets/v0/json/anyco.json) into the left pane of the config editor.
    - Publish the config: **Publish** > **Production**. 
- Open extract-doc.js in a text editor and specify:
  - the path to the example PDF you downloaded.
  - the name of the doc type you created.
- Run `node extract-docs.js`. 


 

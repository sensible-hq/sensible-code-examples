#!/usr/bin/env node

// This script synchronously extracts structured data from the specified PDF and is limited to
// PDFs of ~4.5MB or less with an extraction runtime under 30s (extractions rarely take
// longer than 30s unless they require OCR). For more information
// see https://docs.sensible.so/docs/api-tutorial-sync.

import fs from "fs";
import fetch from "node-fetch"; 
import { Headers } from "node-fetch"; 

// The name of a document type in Sensible, e.g., auto_insurance_quote
const DOCUMENT_TYPE = "YOUR_DOCUMENT_TYPE";

// The path to the PDF you'd like to extract from
// If the PDF is over ~4.5MB use the extract-doc-async.js script
const DOCUMENT_PATH = "YOUR_PDF.pdf";

// Your Sensible API key
const API_KEY = "YOUR_API_KEY";

async function main() {
  const headers = new Headers();
  headers.append("Authorization", `Bearer ${API_KEY}`);
  headers.append("Content-Type", "application/pdf");

  const body = fs.readFileSync(DOCUMENT_PATH);

  const response = await fetch(
    `https://api.sensible.so/v0/extract/${DOCUMENT_TYPE}`,
    {
      method: "POST",
      headers,
      body,
    }
  );

  if (!response.ok) {
    console.log(await response.text());
  } else {
    console.log(JSON.stringify(await response.json(), null, 2));
  }
}

main();

🧾 JSON-LD Schema Validator with jsonschema
📌 Problem Statement
Structured data in the form of application/ld+json (JSON-LD) is widely used for SEO, but errors in the data or schema can cause Google or other parsers to reject it. This tool fetches JSON-LD from a webpage and validates it against its own schema using Python.

💡 Scenario: Fetch and Validate JSON-LD from a Live Webpage
This script:
- Fetches a webpage
- Extracts all <script type="application/ld+json"> blocks
- Tries to validate each block using jsonschema.validate()

✅ Use Case
- Verify that structured data returned by a webpage is well-formed
- Start building an automated structured data audit tool
- Learn how to use jsonschema to validate web data

🛠️ Modules Used
requests - To fetch the raw HTML of the webpage
BeautifulSoup	- To parse and extract JSON-LD <script> blocks
json - To convert raw script strings into Python dictionaries
jsonschema - To validate JSON structure and data types

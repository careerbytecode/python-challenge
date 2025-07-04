## Scenario 1: File Processing and Automation
**Problem Statement:** Automating the process of reading and writing files for data extraction and storage.

**Detailed Scenario:** A project requires automating the task of reading large data files (e.g., CSV or JSON), extracting useful information, and writing the extracted data into new files for further processing.

**Use Case Approach:** Use Python’s file handling functions to read the data, process it, and write the output to new files.

**Tools and Modules:** os, sys, json, csv

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:

- Ask for the input and output files  
- Verify if the file extension ends with `.csv` or `.json` and filter the data  
- Open the file and read the data  
- Filter the required data  
- Write the output to a new file  

Python Modules Used:  
- os and sys: for file system and system-level operations  
- json: for working with JSON files  
- csv: for working with CSV files  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Reference:  
For the csv module, read and write:  
https://docs.python.org/3/library/csv.html#csv.DictReader  
https://docs.python.org/3/library/csv.html#csv.DictWriter  

For the json module, read and write:  
https://docs.python.org/3/library/json.html#json.loads  
https://docs.python.org/3/library/json.html#json.dumps  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

## Scenario 2: Batch File Data Processing

**Problem Statement:** Process a batch of text files to clean and format data.

**Detailed Scenario:** A system receives a batch of unstructured text files. The goal is to clean the data by removing unwanted characters and reformatting it into a standard structure.

**Use Case Approach:** Open and process each file using Python’s file handling and string manipulation methods to clean the content.

**Tools and Modules:** `os`, `re`, `sys`

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

**Approach:**

- Prompt the user to enter the path to the input folder containing the text files.
- Check if the specified folder exists and contains files to process.
- Iterate through each text file in the folder, reading its contents.
- Use regular expressions to remove all characters except letters, numbers, spaces, and newlines from each file.
- Overwrite each file with the cleaned content.

**Python Modules Used:**

- `os`: For navigating directories and handling file paths.
- `sys`: For command-line argument handling and exiting on errors.
- `re`: For pattern matching and cleaning file contents.

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Reference:  
https://docs.python.org/3/library/re.html#re.sub

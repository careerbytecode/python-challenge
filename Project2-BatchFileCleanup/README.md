## Scenario 2: Batch File Data Processing

**Problem Statement:** Process a batch of text files to clean and format data.

**Detailed Scenario:** A system receives a batch of unstructured text files. The goal is to clean the data by removing unwanted characters and reformatting it into a standard structure.

**Use Case Approach:** Open and process each file using Python’s file handling and string manipulation methods to clean the content.

**Tools and Modules:** `os`, `re`, `sys`

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

**Approach:**

- Ask for the input folder where all files are located.  
- Verify that the folder exists and is not empty.  
- Create a backup of the folder as a tar file in case any file needs to be restored.  
- Remove all content from the files except alphanumeric characters, spaces, and newlines.  

**Python Modules Used:**

- `os` and `sys`: For file system and system-level operations.  
- `re`: For regex search and removal of unwanted characters.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Reference:  
https://docs.python.org/3/library/re.html#re.sub

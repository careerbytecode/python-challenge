## Scenario 17: Parsing and Analyzing Log Files
**Problem Statement: Parsing server log files for error detection.**

**Detailed Scenario: A system needs to parse large log files, looking for specific error messages and generating a report.**

**Usecase Approach: Use Python to read log files, search for specific strings, and generate reports.**

**Tools and Modules: os, re, sys**

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

### Approach

- **Open the Log File:** Use Python to open and read the log file line by line.
- **Find Errors:** Look for lines that contain error messages using simple string search or regular expressions.
- **Collect Information:** When an error is found, save important details like the time and error message.
- **Summarize Results:** Count how many errors were found and list them in a simple report.
- **Use Command-line Arguments:** Allow the user to provide the log file path when running the script.




══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

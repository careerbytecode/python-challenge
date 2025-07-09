**Scenario: Age Verification with Logging**

📌 Problem Statement
Design a simple terminal-based system that collects a user’s name and age, validates the age input, and determines if the user is eligible for registration. If an invalid input is entered (e.g., a non-numeric age), the system should handle it gracefully and log the error for future reference.

💡 Detailed Scenario
This script simulates a basic eligibility verification process. It repeatedly prompts the user for their name and age. If the user enters a valid age above the eligibility threshold (greater than 18), the program acknowledges successful registration. If the user is underage, it politely informs them and exits the loop.

In case of invalid input (like entering a string instead of a number for age), the system doesn't crash. Instead, it logs the issue to an error file and allows the user to try again.

✅ Use Case Approach
The program is designed with the following considerations:

- Input validation is performed using a try...except block.
- Eligibility is checked with a simple age condition.
- Errors from invalid inputs are captured and recorded in a log file.
- User experience is kept clean and interactive using terminal prompts and clear messages.

🛠️ Tools and Modules Used
- Module	Purpose
- input()	Accepts user input for name and age.
- print()	Displays real-time feedback to guide the user.
- logging	Logs incorrect inputs (like non-numeric values) into a .log file.

🚦 Approach Summary
- Start a loop that continuously collects user input.
- Wrap the input for age inside a try...except block to catch any invalid formats.
- If the age is valid and over 18, inform the user of their eligibility.
- If the user is underage, display a message and exit the loop.
- On any input error, log a message to an error log file and ask the user to try again.


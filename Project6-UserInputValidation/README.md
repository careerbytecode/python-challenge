-------------------------------------------------
**Scenario : User Input Validation and Authentication**

Problem Statement:
Create an interactive form that collects and validates user input (name, age, email, and password) in a loop, and allows the user to authenticate with a password and decide whether to continue or exit.

**Detailed Scenario:**

A system requires basic user information for registration or login. The program must:
Prompt the user to enter their first name, last name, age, email, and password.
Validate that age is a number and email is in correct format.
Authenticate the user with a preset password.
Inform users about eligibility based on age.
Ask if the user wants to continue or exit the loop.

**Use Case Approach:**
Use pyinputplus to:
Validate user input (strings, numbers, emails).
Handle incorrect input gracefully without crashing.
Create a clean, user-friendly terminal-based form.

**Tools and Modules:**
pyinputplus: for robust and automatic input validation.
input(): for custom password input.
print(): for user messaging and feedback.

**Approach:**
Use a while True loop to keep asking for user details.
Use pyip.inputStr(), inputNum(), and inputEmail() for validation.
Store and display the user's full name, age, and email.
Use a password field to match a preset password (123456789).
Add eligibility logic (e.g., age must be ≥ 18).
Ask the user if they want to continue using inputYesNo().
Break the loop if the user says “no”.

**Python Modules Used:**
Module	Purpose
pyinputplus	Validates string, numeric, and email input
input()	Accepts unvalidated user input (for password)
print()	Outputs information to the user

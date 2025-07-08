**Unique ID Generator with User Input Validation**

**🔍 Project Objective**
Create a terminal-based Python application that:
- Collects user data interactively (first name, last name, age, email, password)
- Validates user input to ensure data integrity
- Generates a custom unique ID for each user based on timestamp and randomness
- Stores all entries in a structured CSV file
- Continues or exits based on user preference

🎯 Main Purpose: Build a clean system that generates unique, timestamp-based IDs for users and logs them for further processing or identification.

**Features**
✅ Validates name, age, and email inputs using pyinputplus
🔐 Accepts password input via input() (no validation logic here — just collection)
🆔 Generates a unique ID using:
    - Current timestamp (seconds since epoch)
    - Random 6-character alphanumeric string
🧾 Stores data persistently in user_data.csv
🔁 Runs in a loop until the user opts to exit

**Tools & Modules Used:**
- pyinputplus: Handles validated inputs like strings, numbers, and emails
- uuid:	Used initially to create a default Customer ID column header
- time:	Gets current timestamp to ensure ID uniqueness
- random & string:	Generates random uppercase letters and digits
- csv:	Writes user data to a CSV file for persistence

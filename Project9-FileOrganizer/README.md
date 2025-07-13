Problem Statement
Managing a cluttered Downloads folder can be time-consuming. This script automates the organization of files into categorized folders based on their file extensions (e.g., Images, Documents, Videos, Music).

💡 Scenario: Automatic File Organization
This script scans the Downloads directory, checks the extension of each file, and then moves it into the appropriate folder (Images, Documents, Videos, Music, or Others). If the folder doesn’t exist, it is automatically created.

✅ Use Case Approach
- Categorize files based on extension using a dictionary (file_types).
- Automatically create target folders if they don’t exist.
- Move each file to its corresponding category folder.
- Unrecognized extensions are moved to a default Others folder.

🛠️ Tools and Modules
- Module	Purpose
- pathlib	Handle file system paths and access user directories easily
- shutil	Move files across directories
- print()	Show user-friendly messages in terminal

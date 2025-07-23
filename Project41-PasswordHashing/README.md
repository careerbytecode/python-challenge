## Scenario 41: Generating Password Hashes for Security  
**Problem Statement: Storing passwords securely by generating hash values.**  

**Detailed Scenario: A Python application needs to generate and store password hashes instead of plain text passwords to enhance security.**  

**Usecase Approach: Use Python’s bcrypt to hash passwords before storing them.**  

**Tools and Modules: bcrypt**  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════  

Approach:   
- Use bcrypt to hash passwords before storing them   
- Store the hashed value in your database (not the plain password)  
- When a user logs in, hash their input and compare with stored hash using checkpw  

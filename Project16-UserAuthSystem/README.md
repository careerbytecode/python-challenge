## Scenario 16: User Authentication System  
**Problem Statement:** Implement user authentication in an application.

**Detailed Scenario:** The system must authenticate users using a username and password, with passwords stored as hashes for security.

**Use Case Approach:** Use Python’s `hashlib` for password hashing and compare the stored hash with the entered password.

**Tools and Modules:** `hashlib`, `os`

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

**Approach:**  
- When a user registers, their password is hashed using Python’s `hashlib` module before storage.
- During login, the entered password is hashed and compared to the stored hash to authenticate the user.
- The `os` module generates a random salt for each password, enhancing security.
- Password hashes and salts are stored securely, not the plain text passwords.

**Python Modules Used:**  
- `hashlib` – Provides secure hash functions for password hashing (e.g., SHA-256).
- `os` – Generates cryptographically secure random salts for password hashing.

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════


## Scenario 55: API Availability Monitor with Retry  
**Problem Statement: Ensure reliability of APIs by continuously checking their availability and handling failures gracefully**  

**Detailed Scenario: A DevOps engineer needs to monitor multiple API endpoints. The script should retry on failure using exponential backoff and log persistent failures for alerting.**  

**Use Case Approach: Read API URLs from a file. Send GET requests to each. If a request fails, retry with backoff. Log final failures with timestamp.**  

**Tools and Modules: requests**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Reads API URLs from a text file  
- Retries 3 times with exponential backoff on failure  
- Logs unavailable URLs with timestamp  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════



## Scenario 58: SSL Certificate Expiry Monitor  
**Problem Statement: Monitor SSL certificates for internal and external services and alert before they expire to prevent downtime.**  

**Detailed Scenario: As an SRE, ensuring SSL certificates are valid is critical. Expired certs lead to broken services and customer impact. Need to check certificate expiry dates across a list of domains and report those expiring soon**  

**Use Case Approach: Parse the expiry date and calculate days left domain mentioned in a text file**  

**Tools and Modules: ssl, socket, datetime**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Read list of domain names (and optional ports) from a file.  
- Connect via ssl and socket to retrieve the certificate.  
- Parse the expiry date and calculate days left.  
- Print results in terminal and optionally export to CSV.  
- Optional: send email or Slack alert if any cert is near expiry.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════


<img width="1612" height="335" alt="image" src="https://github.com/user-attachments/assets/b77b5fa1-8a32-4a13-91bf-811c514f3d92" />

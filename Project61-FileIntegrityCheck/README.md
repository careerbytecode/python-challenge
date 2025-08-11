## Scenario 61: File Integrity & Tamper Detection  
**Problem Statement: Critical system or application files can change unexpectedly (misconfig, accidental edits, compromise). A simple way to record known-good file hashes and later detect any drift.**  

**Detailed Scenario: Maintain a Linux server with a few important files (e.g., /etc/passwd, /etc/ssh/sshd_config, app configs). On day 1, you create a baseline of SHA-256 hashes for these files. Each subsequent run compares current hashes against the baseline and reports**  

**Use Case Approach: Keep a simple files.txt with one absolute path per line, Compute SHA-256 and compare to baseline and report**  

**Tools and Modules: hashlib**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Keep a simple files.txt with one absolute path per line.  
- Compute SHA-256 for each file and save to baseline.json.  
- Recompute hashes, compare to baseline, and print a clear report.  
- Investigate differences; update baseline only when changes are intended.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Day 1 (baseline):
sudo python3 file_integrity.py --init files.txt

Daily check (cron):
sudo python3 file_integrity.py --check files.txt

Investigate any reported drift; if legitimate changes were made, re-baseline.


## Scenario 56: Zombie Process Detector and Cleaner  
**Problem Statement: Identify and optionally clean up zombie or defunct processes that waste system resources**  

**Detailed Scenario: Zombie processes occur when a child process finishes execution but still has an entry in the process table. If not cleaned, they clutter the system and may indicate an issue with the parent process. This tool can help automate detection, logging, and optional cleanup.**  

**Use Case Approach: Use psutil or subprocess to list all processes. Identify processes in Z (zombie) state. Log details: PID, PPID, name, age. Optionally attempt to kill parent or notify via email/logging.**  

**Tools and Modules: psutil, argparse**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Use psutil to list all system processes.  
- Check each process's status for 'zombie'.  
- Print or log details: PID, parent PID, name.  
- Optionally kill the parent process to clean up the zombie (if --clean is passed).  
- Handle permission errors gracefully.  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════


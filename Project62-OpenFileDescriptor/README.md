## Scenario 62: Open File Descriptor Leak Detector  
**Problem Statement: Detect and alert when a process is using an unusually high number of file descriptors (FDs), which can cause "Too many open files" errors and service crashes.**  

**Detailed Scenario: On Linux, processes can leak file descriptors over time if they don't close files, sockets, or pipes properly. This can lead to service outages. As an SRE, you need a quick way to periodically check FD usage and alert if a process is approaching system limits.**  

**Use Case Approach: Use /proc/<pid>/fd to count open file descriptor, compare against ulimit and alert**  

**Tools and Modules: subprocess, psutil**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Use /proc/<pid>/fd or lsof to count open file descriptors.  
- Compare against the process's soft and hard limit "ulimit -n".  
- If FD usage exceeds a threshold, log the event and alert.  
- Optionally store historical data for trend analysis.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════



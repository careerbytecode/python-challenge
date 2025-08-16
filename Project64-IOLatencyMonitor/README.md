## Scenario 64: Disk I/O & Latency Monitor  
**Problem Statement: Disk performance issues like high I/O wait times or latency can severely affect application performance. Many teams only detect this when applications start failing, rather than proactively monitoring it.**  

**Detailed Scenario: A lightweight Python tool that periodically checks disk I/O stats and latency using iostat or /proc/diskstats. If latency or utilization exceeds a threshold, the tool should log the event and optionally send an alert.**  

**Use Case Approach: Collect disk I/O statistics from iostat, comprae with threshold, log and alert.**  

**Tools and Modules: shutil**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- 

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Usage
./diskio_monitor.py --interval 2 --iterations 0 --util-threshold 80 --await-threshold 50
  --interval : seconds between samples (default 2)  
  --iterations: number of updates, 0 = run forever  
  --util-threshold: mark devices with util >= this %  
  --await-threshold: mark devices with await >= this ms  

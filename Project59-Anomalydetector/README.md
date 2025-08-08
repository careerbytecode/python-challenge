## Scenario 59: System Resource Anomaly Detector  
**Problem Statement: SRE teams often face sudden spikes in CPU, memory, or disk usage. Without early detection, this can lead to outages or degraded performance.**  

**Detailed Scenario: The script monitors system metrics at regular intervals and compares them against a moving average. If usage exceeds a defined threshold, it logs the event or triggers an alert.**  

**Use Case Approach: Collect metrics, maintain a rolling history, detect deviations.**  

**Tools and Modules: psutil, collections.deque**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Collect metrics using psutil  
- Maintain a rolling history of past N readings  
- Detect deviations above a percentage threshold from the average  
- Output anomalies to a log or send alerts  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

<img width="1428" height="556" alt="image" src="https://github.com/user-attachments/assets/5d11bd84-a034-4da8-b727-48b58827c19b" />

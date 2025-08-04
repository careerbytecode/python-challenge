## Scenario 54: OpenShift Pod restart count reporter  
**Problem Statement: OpenShift workloads can suffer from issues such as frequent container restarts due to crashes, memory pressure, or configuration errors. These restart loops can silently impact application reliability and performance if left unnoticed.**  

**Detailed Scenario: After infrastructure updates, deployments, or image changes in an OpenShift cluster, some pods may go into frequent restart loops. These issues often go unnoticed unless monitored manually or with external tooling. There is a need to automate the detection of such pods across namespaces and notify operators.**  

**Use Case Approach:  Use the oc CLI to parse restart counts from container status. Generate an HTML or CSV report with thresholds clearly highlighted.**  

**Tools and Modules: Python subprocess, jinja2**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Use the oc CLI to fetch all pods in all namespaces.  
- Parse the container status and filter by restart count.  
- Render the results into a readable HTML report.  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

<img width="1543" height="585" alt="image" src="https://github.com/user-attachments/assets/cf3ec345-19ac-4a21-bc01-0096a070ea5e" />

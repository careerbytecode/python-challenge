## Scenario 52: OpenShift PVC Usage Reporter  
**Problem Statement: OpenShift clusters can experience node disk pressure or pod eviction if PVC usage is left unchecked. This tool proactively monitors PVC usage.**  

**Detailed Scenario: Cluster administrators need a utility to fetch PersistentVolumeClaim (PVC) usage across namespaces, compare against defined thresholds, and report violations in a readable HTML/CSV format.**  

**Use Case Approach:  Use the oc CLI to list PVCs and their associated volumes. Query actual usage. Generate an HTML or CSV report with thresholds clearly highlighted.**  

**Tools and Modules: Python subprocess, csv, jinja2**


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Use Python▒~@~Ys subprocess to call oc get pvc and oc describe pvc  
- Parse PVC size (spec.resources.requests.storage) and usage (Used By or volume metrics if available)  
- Compare against a threshold (e.g., 80%)  
- Output results as HTML and CSV  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

<img width="1457" height="257" alt="image" src="https://github.com/user-attachments/assets/778d02cc-03bc-403a-b848-97ec09e091ef" />

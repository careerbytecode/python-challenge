## Scenario 66: OpenShift route TLS audit  
**Problem Statement: Some OpenShift Routes are accidentally left insecure (plain HTTP, weak TLS, or no redirect). That can expose users to sniffing or downgrade attacks.**  

**Detailed Scenario: Across many namespaces, you want to quickly find Routes which are insecure (plain HTTP, weak TLS, or no redirect).**  

**Use Case Approach: Use oc get routes -A -o json to fetch every Route. Validate and Output in a file**  

**Tools and Modules: is, csv, time**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
Use oc get routes -A -o json to fetch every Route.  
For each Route, inspect:  
  .spec.tls.termination (edge/reencrypt/passthrough/None)  
  .spec.tls.insecureEdgeTerminationPolicy (Redirect vs Allow)  
optional TLS annotations (e.g., allowed versions/ciphers)  
Classify each Route as Secure, Needs Redirect, or Insecure.  
Output a simple HTML (and CSV) report with color coding and quick fix hints.  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════


<img width="1145" height="880" alt="image" src="https://github.com/user-attachments/assets/29a807dc-a85b-4519-872b-1981d0159a02" />

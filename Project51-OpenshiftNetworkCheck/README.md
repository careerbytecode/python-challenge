## Scenario 1: File Processing and Automation
**Problem Statement:** You want to automate the detection of Pod-level networking issues inside an OpenShift cluster from a remote or bastion host.  

**Detailed Scenario:** In complex OpenShift setups, Pods may experience intermittent connectivity issues due to CNI problems, misconfigured NetworkPolicies, or DNS failures.  

**Use Case Approach:** Use Python’s subprocess or openshift-client to run oc exec into pods.  

**Tools and Modules:** subprocess, json, os

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Select a namespace and test pod using oc get pods.  
- Run network tests inside the pod using oc exec:  
   - Resolve a DNS name.  
   - Check outbound internet connectivity.  
- Summarize results in a readable format (PASS/FAIL).  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════



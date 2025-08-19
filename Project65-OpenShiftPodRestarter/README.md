## Scenario 65: OpenShift Pod Restarter  
**Problem Statement: Sometimes application pods get stuck in CrashLoopBackOff or fail due to transient issues. As an SRE, we need a simple tool that can detect such pods and restart them automatically.**  

**Detailed Scenario: In a large OpenShift cluster, developers may report that their pods are stuck or not recovering automatically. Instead of manually running oc delete pod, you can build a Python utility that scans all namespaces, identifies unhealthy pods (e.g., status CrashLoopBackOff, Error, ImagePullBackOff), and restarts them by deleting the pod (so the ReplicaSet/Deployment brings it back).**  

**Use Case Approach: oc client to fetch pod statues, execute oc delete pod command**  

**Tools and Modules: subprocess**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Use the oc CLI or Kubernetes Python client to fetch pod statuses.  
- Filter pods that are in bad states.  
- Restart them by running oc delete pod <pod> -n <namespace>.  
- Log all restarts and generate a small HTML/CSV report for visibility.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

- Uses `oc get pods -o json` to list pods (all namespaces or a single namespace)
- Detects unhealthy pods (CrashLoopBackOff, ImagePullBackOff, ErrImagePull, etc.)
- Restarts them by deleting the pod (Deployment/ReplicaSet/StatefulSet will recreate)
- Supports --dry-run to preview actions

 # Restart unhealthy pods in ALL namespaces
  python oc_pod_restarter.py

  # Only a specific namespace
  python oc_pod_restarter.py -n my-namespace

  # Filter by label (e.g., only app=myapp)
  python oc_pod_restarter.py -n my-namespace --selector app=myapp

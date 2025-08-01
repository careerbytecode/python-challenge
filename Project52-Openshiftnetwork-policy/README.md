## Scenario 52: OpenShift Network Policy Visualizer  
**Problem Statement: Network policies across namespaces are hard to audit and understand visually. Admins need clarity on which namespaces are allowed to communicate with others.**  

**Detailed Scenario: Teams want a visual report showing which namespaces are allowed to send traffic to others via ingress rules. This helps in verifying connectivity, isolating issues, and security audits.Detailed Scenario.**  

**Use Case Approach: Use oc CLI to fetch all network policies in JSON format. Parse ingress rules to identify namespace-to-namespace relationships. Visualize relationships as a graph with Graphviz.**  

**Tools and Modules: oc, json, graphviz**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Use oc get networkpolicy -A -o json to extract all namespace-level policies.  
- Parse the JSON to identify namespaceSelector-based ingress rules.  
- Visualize namespace communication using graphviz.Digraph.  
- Style each namespace as a node; draw directional edges with policy names as labels.  
- Generate an HTML report embedding the SVG graph with timestamp for review in any browser.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

<img width="1301" height="267" alt="image" src="https://github.com/user-attachments/assets/2e9a7452-2753-47c1-8d8a-d7c177f72a91" />

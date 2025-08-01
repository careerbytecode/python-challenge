import subprocess
import json
from graphviz import Digraph
from datetime import datetime

def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd, shell=True, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return ""

def fetch_network_policies():
    output = run_cmd("oc get networkpolicy -A -o json")
    if not output:
        return []
    try:
        return json.loads(output).get("items", [])
    except json.JSONDecodeError:
        print("Failed to parse JSON from oc output.")
        return []

def build_policy_graph(policies):
    graph = Digraph("NetworkPolicyGraph", format="svg")
    graph.attr(rankdir='LR')

    namespaces = set()
    edges = []

    for policy in policies:
        ns = policy["metadata"].get("namespace", "Unknown")
        name = policy["metadata"].get("name", "unnamed-policy")
        namespaces.add(ns)

        ingress_rules = policy.get("spec", {}).get("ingress", [])
        for rule in ingress_rules:
            for peer in rule.get("from", []):
                peer_ns = peer.get("namespaceSelector", {}).get("matchLabels", {}).get("project")
                if peer_ns:
                    edges.append((peer_ns, ns, name))

    for ns in namespaces:
        graph.node(ns, shape="ellipse", style="filled", color="lightblue")

    for src, dest, label in edges:
        graph.edge(src, dest, label=label)

    return graph

def save_html(graph, filename="network_policy_graph.html"):
    try:
        svg = graph.pipe(format="svg").decode("utf-8")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html = f"""<!DOCTYPE html>
<html>
<head><title>OpenShift Network Policy Graph</title></head>
<body>
<h2>Network Policy Report - {timestamp}</h2>
{svg}
</body>
</html>"""

        with open(filename, "w") as f:
            f.write(html)
        print(f"Report generated: {filename}")
    except Exception as e:
        print(f"Failed to render SVG or write file: {e}")

if __name__ == "__main__":
    policies = fetch_network_policies()
    if policies:
        graph = build_policy_graph(policies)
        save_html(graph)
    else:
        print("No policies found or unable to fetch.")


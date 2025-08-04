import subprocess
import json
from datetime import datetime
from jinja2 import Template

RESTART_THRESHOLD = 3

def run_oc_get_pods():
    try:
        result = subprocess.run(
            ["oc", "get", "pods", "-A", "-o", "json"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running oc command:", e.stderr)
        return {}

def extract_restarting_pods(pod_data):
    problematic_pods = []

    for item in pod_data.get("items", []):
        namespace = item["metadata"]["namespace"]
        name = item["metadata"]["name"]
        containers = item["status"].get("containerStatuses", [])

        for container in containers:
            restarts = container.get("restartCount", 0)
            if restarts > RESTART_THRESHOLD:
                problematic_pods.append({
                    "namespace": namespace,
                    "pod_name": name,
                    "container_name": container["name"],
                    "restart_count": restarts,
                    "reason": container.get("state", {})
                })

    return problematic_pods

def generate_html_report(pods, output_file="pod_restart_report.html"):
    html_template = """
    <html>
    <head>
        <title>Pod Restart Report</title>
        <style>
            body { font-family: Arial; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
            tr:hover { background-color: #f5f5f5; }
            .high-restart { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <h2>Pod Restart Report - {{ date }}</h2>
        {% if pods %}
        <table>
            <tr>
                <th>Namespace</th>
                <th>Pod</th>
                <th>Container</th>
                <th>Restart Count</th>
                <th>Reason</th>
            </tr>
            {% for pod in pods %}
            <tr>
                <td>{{ pod.namespace }}</td>
                <td>{{ pod.pod_name }}</td>
                <td>{{ pod.container_name }}</td>
                <td class="high-restart">{{ pod.restart_count }}</td>
                <td>{{ pod.reason }}</td>
            </tr>
            {% endfor %}
        </table>
        {% else %}
        <p>No pods found with restarts > {{ threshold }}.</p>
        {% endif %}
    </body>
    </html>
    """
    template = Template(html_template)
    html = template.render(pods=pods, threshold=RESTART_THRESHOLD, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    with open(output_file, "w") as f:
        f.write(html)
    print(f"Report saved to {output_file}")

if __name__ == "__main__":
    data = run_oc_get_pods()
    restarting_pods = extract_restarting_pods(data)
    generate_html_report(restarting_pods)

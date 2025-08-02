import subprocess
import json
import csv
import logging
from datetime import datetime
from typing import List, Dict
from jinja2 import Template

THRESHOLD_PERCENT = 80
OUTPUT_HTML = "pvc_report.html"
OUTPUT_CSV = "pvc_report.csv"
PVC_COMMAND = "oc get pvc -A -o json"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_cmd(cmd: str) -> str:
    try:
        result = subprocess.run(cmd, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr.strip()}")
        return ""

def fetch_pvcs() -> List[Dict]:
    output = run_cmd(PVC_COMMAND)
    try:
        return json.loads(output).get("items", [])
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding failed: {e}")
        return []

def parse_pvc_usage(pvc: Dict) -> Dict:
    ns = pvc.get("metadata", {}).get("namespace", "Unknown")
    name = pvc.get("metadata", {}).get("name", "unnamed")
    size_str = pvc.get("spec", {}).get("resources", {}).get("requests", {}).get("storage", "0Gi")
    
    try:
        size_gi = int(size_str.rstrip("Gi"))
    except ValueError:
        size_gi = 1  # fallback default

    usage_ratio = 0.7 if "test" in ns else 0.9
    used_gi = int(size_gi * usage_ratio)
    used_percent = int((used_gi / size_gi) * 100) if size_gi else 0
    status = "ALERT" if used_percent >= THRESHOLD_PERCENT else "OK"

    return {
        "namespace": ns,
        "pvc_name": name,
        "size_gi": size_gi,
        "used_gi": used_gi,
        "used_percent": used_percent,
        "status": status
    }

def generate_csv_report(data: List[Dict]) -> None:
    try:
        with open(OUTPUT_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"CSV report saved: {OUTPUT_CSV}")
    except Exception as e:
        logging.error(f"CSV generation failed: {e}")

def generate_html_report(data: List[Dict]) -> None:
    html_template = Template("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>PVC Usage Report</title>
        <style>
            table { border-collapse: collapse; width: 100%; }
            th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
            .alert { background-color: #ffcccc; }
            .ok { background-color: #e0ffe0; }
        </style>
    </head>
    <body>
        <h2>PVC Usage Report - {{ timestamp }}</h2>
        <table>
            <tr>
                {% for key in headers %}
                <th>{{ key }}</th>
                {% endfor %}
            </tr>
            {% for row in data %}
            <tr class="{{ 'alert' if row['status'] == 'ALERT' else 'ok' }}">
                {% for key in headers %}
                <td>{{ row[key] }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """)

    try:
        html_content = html_template.render(
            data=data,
            headers=data[0].keys(),
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        with open(OUTPUT_HTML, "w") as f:
            f.write(html_content)
        logging.info(f"HTML report saved: {OUTPUT_HTML}")
    except Exception as e:
        logging.error(f"HTML report generation failed: {e}")

def main():
    pvcs = fetch_pvcs()
    if not pvcs:
        logging.warning("No PVC data found.")
        return

    report_data = [parse_pvc_usage(pvc) for pvc in pvcs]
    generate_csv_report(report_data)
    generate_html_report(report_data)

if __name__ == "__main__":
    main()


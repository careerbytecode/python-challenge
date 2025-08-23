#!/usr/bin/env python3

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime
from html import escape
from pathlib import Path
from typing import Dict, List, Tuple, Optional

HSTS_ANNOTATION = "haproxy.router.openshift.io/hsts_header"

SECURITY_COLORS = {
    "SECURE": "#22c55e",
    "NEEDS_REDIRECT": "#f59e0b",
    "INSECURE_HTTP": "#ef4444",
    "WEAK_REENCRYPT_NO_BACKEND_CA": "#f59e0b",
    "REVIEW_PASSTHROUGH": "#3b82f6",
    "WARN_HSTS_MISSING": "#eab308",
    "REVIEW": "#9ca3af",
}

def run_command(cmd: List[str]) -> Tuple[int, str, str]:
    try:
        process = subprocess.run(
            cmd, 
            text=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            check=False,
            timeout=60
        )
        return process.returncode, process.stdout, process.stderr
    except subprocess.TimeoutExpired:
        print("Command timed out", file=sys.stderr)
        sys.exit(2)
    except FileNotFoundError:
        print("oc command not found", file=sys.stderr)
        sys.exit(2)

def get_routes_data(namespace: Optional[str], selector: Optional[str]) -> Dict:
    cmd = ["oc", "get", "routes", "-o", "json"]
    
    if namespace:
        cmd += ["-n", namespace]
    else:
        cmd += ["-A"]
    
    if selector:
        cmd += ["-l", selector]
    
    returncode, stdout, stderr = run_command(cmd)
    
    if returncode != 0:
        print(f"Failed to fetch routes: {stderr or stdout}", file=sys.stderr)
        sys.exit(1)
    
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        print("Could not parse oc output", file=sys.stderr)
        sys.exit(1)

def analyze_route_security(route: Dict, require_hsts: bool) -> Tuple[str, List[str]]:
    spec = route.get("spec", {}) or {}
    tls_config = spec.get("tls")
    annotations = route.get("metadata", {}).get("annotations", {}) or {}
    issues: List[str] = []

    if not tls_config:
        return "INSECURE_HTTP", ["No TLS configuration"]

    termination = (tls_config.get("termination") or "").lower()
    insecure_policy = tls_config.get("insecureEdgeTerminationPolicy") or "None"

    if termination == "edge":
        if insecure_policy != "Redirect":
            issues.append(f"Edge termination without redirect (policy: {insecure_policy})")
            status = "NEEDS_REDIRECT"
        else:
            status = "SECURE"

    elif termination == "reencrypt":
        if not tls_config.get("destinationCACertificate"):
            issues.append("Re-encrypt without destination CA certificate")
            status = "WEAK_REENCRYPT_NO_BACKEND_CA"
        else:
            status = "SECURE"

    elif termination == "passthrough":
        issues.append("Passthrough termination - verify backend HTTPS enforcement")
        status = "REVIEW_PASSTHROUGH"

    else:
        issues.append(f"Unknown termination: {termination or 'None'}")
        status = "REVIEW"

    if require_hsts and status in ("SECURE", "NEEDS_REDIRECT"):
        if not annotations.get(HSTS_ANNOTATION):
            issues.append("Missing HSTS header annotation")
            if status == "SECURE":
                status = "WARN_HSTS_MISSING"

    return status, issues

def process_routes(routes: List[Dict], require_hsts: bool) -> List[Dict]:
    results = []
    
    for route in routes:
        metadata = route.get("metadata", {}) or {}
        spec = route.get("spec", {}) or {}
        
        namespace = metadata.get("namespace", "unknown")
        name = metadata.get("name", "unknown") 
        host = spec.get("host", "no-host-set")
        path = spec.get("path", "") or ""
        
        tls = spec.get("tls") or {}
        termination = tls.get("termination", "none")
        insecure_policy = tls.get("insecureEdgeTerminationPolicy", "None")

        status, issues = analyze_route_security(route, require_hsts=require_hsts)

        full_url = host + (path if path else "")
        
        results.append({
            "namespace": namespace,
            "name": name, 
            "host": full_url,
            "termination": termination,
            "insecurePolicy": insecure_policy,
            "status": status,
            "issues": "; ".join(issues) if issues else "-",
        })
    
    security_priority = {
        "INSECURE_HTTP": 0,
        "NEEDS_REDIRECT": 1,
        "WEAK_REENCRYPT_NO_BACKEND_CA": 2,
        "WARN_HSTS_MISSING": 3,
        "REVIEW_PASSTHROUGH": 4,
        "REVIEW": 5,
        "SECURE": 6,
    }
    
    def sort_by_priority(route):
        priority = security_priority.get(route["status"], 999)
        return (priority, route["namespace"], route["name"])
    
    results.sort(key=sort_by_priority)
    
    return results

def save_csv_report(results: List[Dict], output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    fieldnames = ["namespace", "name", "host", "termination", "insecurePolicy", "status", "issues"]
    
    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    return output_path

def save_html_report(results: List[Dict], output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def create_status_badge(status: str) -> str:
        color = SECURITY_COLORS.get(status, "#9ca3af")
        return f'<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{color};margin-right:6px;"></span>{escape(status)}'

    table_rows = []
    for result in results:
        status_badge = create_status_badge(result['status'])
        
        table_rows.append(f"""
        <tr>
            <td><code>{escape(result['namespace'])}</code></td>
            <td><code>{escape(result['name'])}</code></td>
            <td>{escape(result['host'])}</td>
            <td>{escape(result['termination'])}</td>
            <td>{escape(str(result['insecurePolicy']))}</td>
            <td>{status_badge}</td>
            <td>{escape(result['issues'])}</td>
        </tr>""")

    legend_items = []
    for status in ["SECURE", "NEEDS_REDIRECT", "INSECURE_HTTP", "WEAK_REENCRYPT_NO_BACKEND_CA", "REVIEW_PASSTHROUGH", "WARN_HSTS_MISSING", "REVIEW"]:
        if status in SECURITY_COLORS:
            color = SECURITY_COLORS[status]
            legend_items.append(f'<span style="margin-right:16px;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{color};margin-right:6px;"></span>{status}</span>')
    
    legend_html = "".join(legend_items)

    html_content = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>OpenShift Route TLS Audit</title>
    <style>
        body {{
            font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Arial, sans-serif;
            max-width: 1200px;
            margin: 24px auto;
            padding: 0 16px;
        }}
        h1 {{ margin: 0; }}
        .meta {{ color: #555; margin: 6px 0 16px 0; }}
        .legend {{ margin: 8px 0 16px 0; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #e5e7eb; padding: 8px 10px; font-size: 14px; }}
        th {{ background: #f3f4f6; }}
        tr:hover {{ background: #fafafa; }}
        code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }}
    </style>
</head>
<body>
    <h1>OpenShift Route TLS Audit</h1>
    <div class="meta">Generated: {escape(timestamp)}</div>
    <div class="legend">{legend_html}</div>
    <table>
        <thead>
            <tr>
                <th>Namespace</th>
                <th>Route</th>
                <th>Host</th>
                <th>Termination</th>
                <th>Insecure Policy</th>
                <th>Status</th>
                <th>Issues</th>
            </tr>
        </thead>
        <tbody>
            {''.join(table_rows)}
        </tbody>
    </table>
</body>
</html>"""
    
    output_path.write_text(html_content, encoding="utf-8")
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Audit OpenShift Routes for TLS/HTTPS posture")
    
    parser.add_argument("-n", "--namespace", help="Namespace to scan (default: all)")
    parser.add_argument("-l", "--selector", help="Label selector")
    parser.add_argument("--require-hsts", action="store_true", help=f"Warn if {HSTS_ANNOTATION} missing")
    parser.add_argument("--out-html", default="route_tls_audit.html", help="HTML output file")
    parser.add_argument("--out-csv", default="route_tls_audit.csv", help="CSV output file")
    
    args = parser.parse_args()
    
    route_data = get_routes_data(args.namespace, args.selector)
    routes = route_data.get("items", [])
    
    if not routes:
        scope = f"namespace '{args.namespace}'" if args.namespace else "all namespaces"
        selector_info = f" (selector: {args.selector})" if args.selector else ""
        print(f"No routes found in {scope}{selector_info}")
        return
    
    results = process_routes(routes, require_hsts=args.require_hsts)
    
    html_path = save_html_report(results, Path(args.out_html))
    csv_path = save_csv_report(results, Path(args.out_csv))
    
    status_counts = {}
    for result in results:
        status = result["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    
    summary_parts = []
    for k, v in sorted(status_counts.items()):
        summary_parts.append(f"{k}:{v}")
    summary = ", ".join(summary_parts)
    print(f"Audit complete. {len(results)} routes. [{summary}]")
    print(f"HTML: {html_path}")
    print(f"CSV: {csv_path}")

if __name__ == "__main__":
    main()

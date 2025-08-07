import ssl
import socket
import argparse
from datetime import datetime
import csv

def get_ssl_expiry(domain, port=443, timeout=5):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiry_str = cert['notAfter']
                expiry_date = datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')
                return expiry_date
    except Exception as e:
        return f"Error: {e}"

def read_domains(file_path):
    domains = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                parts = line.strip().split(":")
                domain = parts[0]
                port = int(parts[1]) if len(parts) > 1 else 443
                domains.append((domain, port))
    return domains

def check_certificates(domains, threshold_days=15):
    report = []
    now = datetime.utcnow()

    for domain, port in domains:
        expiry = get_ssl_expiry(domain, port)
        if isinstance(expiry, datetime):
            days_left = (expiry - now).days
            status = "OK" if days_left > threshold_days else "EXPIRING SOON"
        else:
            days_left = "-"
            status = expiry  # Error message

        report.append({
            "domain": domain,
            "port": port,
            "expiry": expiry if isinstance(expiry, datetime) else "N/A",
            "days_left": days_left,
            "status": status
        })

    return report

def save_report_csv(report, filename="ssl_report.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['domain', 'port', 'expiry', 'days_left', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report)
    print(f"Report saved to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSL Certificate Expiry Checker")
    parser.add_argument("file", help="File containing list of domains (one per line, optional :port)")
    parser.add_argument("--threshold", type=int, default=15, help="Alert threshold in days")
    parser.add_argument("--csv", help="Path to output CSV report", default="ssl_report.csv")
    args = parser.parse_args()

    domains = read_domains(args.file)
    result = check_certificates(domains, args.threshold)
    
    for item in result:
        print(f"{item['domain']}:{item['port']} {item['status']} (Expires: {item['expiry']}, Days left: {item['days_left']})")

    save_report_csv(result, args.csv)


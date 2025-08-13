import subprocess
import time
import logging
import argparse
from pathlib import Path

logging.basicConfig(
    filename="service_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def read_services(file_path):
    path = Path(file_path)
    if not path.exists():
        logging.error(f"Service list file {file_path} not found.")
        return []
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]

def is_service_active(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip() == "active"
    except Exception as e:
        logging.error(f"Error checking {service}: {e}")
        return False

def restart_service(service):
    try:
        subprocess.run(["sudo", "systemctl", "restart", service], check=True)
        logging.warning(f"Service {service} restarted successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart {service}: {e}")

def monitor_services(services, interval):
    while True:
        for service in services:
            if not is_service_active(service):
                logging.warning(f"Service {service} is down! Restarting...")
                restart_service(service)
            else:
                logging.info(f"Service {service} is healthy.")
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Systemd Service Health Checker")
    parser.add_argument("services_file", help="File containing list of services to monitor")
    parser.add_argument("--interval", type=int, default=60, help="Check interval in seconds")
    parser.add_argument("--once", action="store_true", help="Run a single check and exit")
    args = parser.parse_args()

    services = read_services(args.services_file)
    if not services:
        print("No services to monitor. Exiting.")
        return

    if args.once:
        for service in services:
            if not is_service_active(service):
                logging.warning(f"Service {service} is down! Restarting...")
                restart_service(service)
            else:
                logging.info(f"Service {service} is healthy.")
    else:
        monitor_services(services, args.interval)

if __name__ == "__main__":
    main()

import requests
import time
import logging
import argparse
from datetime import datetime

logging.basicConfig(
    filename='api_failures.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_api(url, retries=3, backoff_factor=2):
    delay = 1
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            pass
        time.sleep(delay)
        delay *= backoff_factor
    return False

def monitor_apis(file_path):
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        print(f"Checking {url}...")
        if not check_api(url):
            logging.warning(f"API down: {url}")
            print(f"{url} is unavailable")
        else:
            print(f"{url} is online")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor API availability with retry")
    parser.add_argument("file", help="Path to the file containing API URLs (one per line)")
    args = parser.parse_args()

    print(f"Starting API monitoring at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    monitor_apis(args.file)


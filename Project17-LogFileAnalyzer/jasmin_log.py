import os
import re
import sys

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(?P<level>ERROR|CRITICAL)\s+\d+\s+\S+\s+(?P<message>.+)',
    re.IGNORECASE
)

def parse_log_file(filepath):
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        return []

    results = []
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        for line_no, line in enumerate(f, 1):
            pps = LOG_PATTERN.search(line)
            if pps:
                results.append({
                    "line": line_no,
                    "timestamp": pps["timestamp"],
                    "level": pps["level"],
                    "message": pps["message"].strip()
                })
    return results

def print_report(entries, filename):
    print(f"\nReport for: {filename}")
    print(f"Total Errors: {len(entries)}")
    for e in entries:
        print(f"[{e['timestamp']}] Line {e['line']} [{e['level']}]: {e['message']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python jasmin_log.py /var/log/jasmin/smppsrv_01.log [/var/log/jasmin/messages.log ...]")
        sys.exit(1)

    for path in sys.argv[1:]:
        entries = parse_log_file(path)
        print_report(entries, path)

if __name__ == "__main__":
    main()

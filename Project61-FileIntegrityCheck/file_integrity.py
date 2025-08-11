import argparse
import hashlib
import json
from pathlib import Path

def hash_file(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        return None

parser = argparse.ArgumentParser(description="Simple File Integrity Checker")
parser.add_argument("--init", action="store_true", help="Initialize baseline")
parser.add_argument("--check", action="store_true", help="Check against baseline")
parser.add_argument("--baseline", default="baseline.json", help="Path to baseline file")
parser.add_argument("file_list", help="Text file with file paths to monitor")
args = parser.parse_args()

file_paths = [Path(p.strip()) for p in Path(args.file_list).read_text().splitlines()]

if args.init:
    baseline = {str(p): hash_file(p) for p in file_paths}
    with open(args.baseline, "w") as f:
        json.dump(baseline, f, indent=2)
    print(f"Baseline saved to {args.baseline}")

elif args.check:
    try:
        with open(args.baseline) as f:
            baseline = json.load(f)
    except FileNotFoundError:
        print("Baseline file not found.")
        exit(1)

    for p in file_paths:
        current_hash = hash_file(p)
        baseline_hash = baseline.get(str(p))
        if current_hash != baseline_hash:
            if current_hash is None:
                print(f"MISSING: {p}")
            elif baseline_hash is None:
                print(f"NEW: {p}")
            else:
                print(f"MODIFIED: {p}")
    print("Check complete.")
else:
    parser.print_help()


#!/usr/bin/env python3
import argparse
import os
import re
import time
from collections import deque
from datetime import datetime

def get_arguments():
    parser = argparse.ArgumentParser(description="Monitor a log file for error spikes.")
    parser.add_argument("logfile", help="Path to the log file to monitor")
    parser.add_argument("--pattern", default=r"\b(ERROR|CRITICAL|FATAL|FAIL|EXCEPTION)\b",
                        help="Regex pattern to detect error lines (default: common error keywords)")
    parser.add_argument("--window", type=int, default=60,
                        help="Time window in seconds to count errors (default: 60)")
    parser.add_argument("--threshold", type=int, default=20,
                        help="Alert if error count in window >= threshold (default: 20)")
    parser.add_argument("--summary-lines", type=int, default=50,
                        help="Number of recent error lines to include in summary (default: 50)")
    parser.add_argument("--summary-file", default="log_spike_summary.txt",
                        help="File to save error summary (default: log_spike_summary.txt)")
    parser.add_argument("--poll-interval", type=float, default=0.25,
                        help="How often to check for new log lines (in seconds, default: 0.25)")
    return parser.parse_args()

def tail_log_file(filepath, interval=0.25):
    last_inode = None
    file = None
    try:
        while True:
            try:
                stats = os.stat(filepath)
                if file is None or stats.st_ino != last_inode:
                    if file:
                        file.close()
                    file = open(filepath, "r", encoding="utf-8", errors="replace")
                    file.seek(0, os.SEEK_END)
                    last_inode = stats.st_ino

                line = file.readline()
                if line:
                    yield line
                else:
                    # Handle file truncation
                    current_pos = file.tell()
                    new_stats = os.stat(filepath)
                    if new_stats.st_size < current_pos:
                        file.close()
                        file = open(filepath, "r", encoding="utf-8", errors="replace")
                        last_inode = os.stat(filepath).st_ino
                    time.sleep(interval)
            except FileNotFoundError:
                time.sleep(interval)
    finally:
        if file:
            file.close()

def save_summary(filename, error_lines, window, threshold, count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Log Spike Summary\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Window: Last {window} seconds\n")
        f.write(f"Threshold: {threshold}\n")
        f.write(f"Errors in window: {count}\n\n")
        f.write("## Recent error lines:\n\n")
        for line in error_lines:
            f.write(line if line.endswith("\n") else line + "\n")

def monitor_log():
    args = get_arguments()
    error_pattern = re.compile(args.pattern, re.IGNORECASE)

    error_timestamps = deque()
    recent_errors = deque(maxlen=max(args.summary_lines, 1))

    print(f"Watching log file: {args.logfile}")
    print(f"Error pattern: {args.pattern}")
    print(f"Window: {args.window}s | Threshold: {args.threshold} errors")
    print(f"Summary will be saved to: {args.summary_file}")
    print("(Press Ctrl+C to stop)\n")

    try:
        for line in tail_log_file(args.logfile, args.poll_interval):
            current_time = time.time()

            if error_pattern.search(line):
                error_timestamps.append(current_time)
                recent_errors.append(line)

            while error_timestamps and error_timestamps[0] < current_time - args.window:
                error_timestamps.popleft()

            if len(error_timestamps) >= args.threshold:
                print(f"Spike detected at {datetime.now().strftime('%H:%M:%S')}! {len(error_timestamps)} errors in last {args.window}s.")
                save_summary(args.summary_file, list(recent_errors)[-args.summary_lines:], args.window, args.threshold, len(error_timestamps))
                print(f"Summary saved to {args.summary_file}\n")
                error_timestamps.clear()  # Cooldown

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor_log()


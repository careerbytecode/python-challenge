#!/usr/bin/env python3
import os
import time
import psutil
import argparse

LIMITS_PATH = "/proc/{pid}/limits"
FD_DIR_PATH = "/proc/{pid}/fd"

def safe_read_lines(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read().splitlines()
    except Exception:
        return None

def get_fd_count(pid):
    fd_path = FD_DIR_PATH.format(pid=pid)
    try:
        return len(os.listdir(fd_path))
    except Exception:
        return None

def get_fd_limits(pid):
    limits_path = LIMITS_PATH.format(pid=pid)
    lines = safe_read_lines(limits_path)
    if not lines:
        return (None, None)
    for line in lines:
        if line.lower().startswith("max open files"):
            parts = [p for p in line.split() if p.strip()]
            if len(parts) >= 6:
                soft_raw, hard_raw = parts[3], parts[4]
                def to_int(x):
                    try:
                        return int(x) if x.isdigit() else None
                    except Exception:
                        return None
                soft = to_int(soft_raw)
                hard = to_int(hard_raw)
                return (soft, hard)
    return (None, None)

def pct(a, b):
    if not b or b <= 0 or a is None:
        return None
    return (a / b) * 100.0

def collect_process_fd_stats():
    stats = []
    for proc in psutil.process_iter(["pid", "name", "username", "cmdline"]):
        pid = proc.info["pid"]
        name = proc.info.get("name") or "unknown"
        user = proc.info.get("username") or "unknown"
        try:
            fd_count = get_fd_count(pid)
            soft, hard = get_fd_limits(pid)
            usage = pct(fd_count, soft) if fd_count is not None else None
            cmd = " ".join(proc.info.get("cmdline") or [])[:120] 
            stats.append({
                "pid": pid,
                "user": user,
                "name": name,
                "fd": fd_count,
                "soft": soft,
                "hard": hard,
                "usage": usage,
                "cmd": cmd
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return stats

def format_row(row):
    def fmt(v):
        return "-" if v is None else str(v)
    def fmt_pct(v):
        return "-" if v is None else f"{v:.1f}%"
    return f"{row['pid']:>6}  {row['user'][:12]:<12}  {row['name'][:18]:<18}  {fmt(row['fd']):>6}  {fmt(row['soft']):>6}  {fmt(row['hard']):>8}  {fmt_pct(row['usage']):>7}  {row['cmd']}"

def print_table(stats, threshold, top):
    stats_sorted = sorted(stats, key=lambda r: (r["fd"] is None, r["fd"] or -1), reverse=True)
    if top:
        stats_sorted = stats_sorted[:top]

    header = "   PID  USER         NAME                FDs   SOFT     HARD   USAGE   COMMAND"
    print(header)
    print("-" * len(header))
    for row in stats_sorted:
        line = format_row(row)
        if row["usage"] is not None and row["usage"] >= threshold:
            # Mark high-usage rows
            print("!!! " + line)
        else:
            print("    " + line)

    high = [r for r in stats if r["usage"] is not None and r["usage"] >= threshold]
    print("\nSummary: total processes scanned: {}, above threshold ({}%): {}".format(len(stats), threshold, len(high)))

def main():
    ap = argparse.ArgumentParser(description="Open File Descriptor Leak Detector")
    ap.add_argument("--threshold", type=float, default=80.0, help="Warn if usage >= THRESHOLD%% of soft limit (default: 80)")
    ap.add_argument("--top", type=int, default=30, help="Show top N rows by FD count (default: 30)")
    ap.add_argument("--watch", type=int, help="Refresh every N seconds (watch mode)")
    args = ap.parse_args()

    try:
        if args.watch:
            while True:
                os.system("clear")
                print(f"Open FD Leak Detector  |  threshold={args.threshold:.0f}%  |  top={args.top}  |  {time.strftime('%Y-%m-%d %H:%M:%S')}")
                stats = collect_process_fd_stats()
                print_table(stats, threshold=args.threshold, top=args.top)
                time.sleep(max(1, args.watch))
        else:
            stats = collect_process_fd_stats()
            print_table(stats, threshold=args.threshold, top=args.top)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()


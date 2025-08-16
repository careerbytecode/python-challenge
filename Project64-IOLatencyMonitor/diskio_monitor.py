#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys
import time
import signal

def read_proc_diskstats():
    stats = {}
    try:
        with open("/proc/diskstats") as f:
            for line in f:
                parts = line.split()
                if len(parts) < 14:
                    continue
                dev = parts[2]
                # skip loops, ram disks, partitions like sda1
                if dev.startswith(("loop", "ram")) or any(ch.isdigit() for ch in dev[-1]):
                    continue
                stats[dev] = list(map(int, [
                    parts[3],   # reads completed
                    parts[5],   # sectors read
                    parts[6],   # ms spent reading
                    parts[7],   # writes completed
                    parts[9],   # sectors written
                    parts[10],  # ms spent writing
                    parts[12],  # ms doing I/O
                    parts[13],  # weighted ms doing I/O
                ]))
    except FileNotFoundError:
        return {}
    return stats

def sample_proc(interval):
    a = read_proc_diskstats()
    time.sleep(interval)
    b = read_proc_diskstats()

    rows = []
    for dev, old in a.items():
        new = b.get(dev)
        if not new:
            continue

        dr   = new[0] - old[0]
        sr   = new[1] - old[1]
        mr   = new[2] - old[2]
        dw   = new[3] - old[3]
        sw   = new[4] - old[4]
        mw   = new[5] - old[5]
        mdio = new[6] - old[6]
        mwt  = new[7] - old[7]

        ops = dr + dw or 1

        rs    = dr  / interval
        ws    = dw  / interval
        rkb   = (sr * 512) / 1024 / interval
        wkb   = (sw * 512) / 1024 / interval
        await_ms = (mr + mw) / ops
        util  = (mdio / (interval * 1000)) * 100

        rows.append({
            'dev':   dev,
            'r/s':   rs,
            'w/s':   ws,
            'rKiB/s': rkb,
            'wKiB/s': wkb,
            'await': await_ms,
            '%util': util
        })

    return sorted(rows, key=lambda x: x['%util'], reverse=True)

def sample_iostat(interval):
    cmd = ["iostat", "-x", "-d", str(interval), "2"]
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []

    lines = [l for l in out.splitlines() if l.strip()]
    idx = next(i for i,l in enumerate(lines) if l.lower().startswith("device"))
    hdr = lines[idx].split()
    col = {name.lower(): pos for pos,name in enumerate(hdr)}

    rows = []
    for line in lines[idx+1:]:
        parts = line.split()
        dev = parts[0]
        if dev.startswith(("loop", "ram")):
            continue
        def get(key):
            return float(parts[col[key]]) if key in col else None
        aw = get("await") or ((get("r_await") or 0) + (get("w_await") or 0)) / 2
        rows.append({
            'dev':    dev,
            'r/s':    get("r/s"),
            'w/s':    get("w/s"),
            'rKiB/s': get("rkB/s"),
            'wKiB/s': get("wkB/s"),
            'await':  aw,
            '%util':  get("%util")
        })

    return sorted(rows, key=lambda x: x['%util'] or 0, reverse=True)

def print_table(rows, util_th, await_th):
    headers = ["DEV", "r/s", "w/s", "rKiB/s", "wKiB/s", "await", "%util"]
    print("  ".join(h.center(8) for h in headers))
    print("-" * 8 * len(headers))

    for r in rows:
        alert = (r['%util'] >= util_th) or (r['await'] >= await_th)
        mark = "!!" if alert else "  "
        vals = [
            f"{r['dev']:<8}",
            f"{r['r/s']:>6.1f}",
            f"{r['w/s']:>6.1f}",
            f"{r['rKiB/s']:>7.1f}",
            f"{r['wKiB/s']:>7.1f}",
            f"{r['await']:>6.1f}",
            f"{r['%util']:>6.1f}",
        ]
        print(f"{mark} " + "  ".join(vals))

def main():
    parser = argparse.ArgumentParser(description="Disk I/O & Latency Monitor")
    parser.add_argument("--interval", type=float, default=2.0,
                        help="seconds between samples (default 2)")
    parser.add_argument("--iterations", type=int, default=0,
                        help="number of updates, 0 = forever")
    parser.add_argument("--util-threshold", type=float, default=80.0,
                        help="highlight util ≥ this %")
    parser.add_argument("--await-threshold", type=float, default=50.0,
                        help="highlight await ≥ this ms")
    args = parser.parse_args()

    backend = sample_proc if sys.platform.startswith("linux") else lambda i: []
    if not backend or (not sample_proc and shutil.which("iostat")):
        backend = sample_iostat

    stop = False
    def on_sig(signum, frame):
        nonlocal stop
        stop = True
    signal.signal(signal.SIGINT, on_sig)

    count = 0
    while not stop:
        print("\033[2J\033[H", end="") 
        print(f"Interval={args.interval}s  util>={args.util_threshold}%  await>={args.await_threshold}ms\n")
        rows = backend(args.interval)
        if not rows:
            print("No data available (backend failed).")
            break

        print_table(rows, args.util_threshold, args.await_threshold)

        count += 1
        if args.iterations and count >= args.iterations:
            break

    print("\nExiting monitor. Goodbye!")

if __name__ == "__main__":
    main()

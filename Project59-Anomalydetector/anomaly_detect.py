import time
import psutil
import argparse
import logging
from collections import deque
from datetime import datetime

def setup_logger(log_file: str, verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )

def pct_str(v: float) -> str:
    return f"{v:.1f}%"

def read_metrics(mountpoint: str):
    cpu = psutil.cpu_percent(interval=None)            
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage(mountpoint).percent
    return {"cpu": cpu, "mem": mem, "disk": disk}

def detect_anomaly(current: float, history: deque, min_samples: int, threshold: float):
    if len(history) < min_samples:
        return False, 0.0, 0.0
    avg = sum(history) / len(history)
    # If baseline avg is tiny (e.g., near 0), use an absolute guard
    baseline = max(avg, 1.0)
    is_anom = current > baseline * (1 + threshold)
    return is_anom, avg, baseline

def main():
    p = argparse.ArgumentParser(description="System Resource Anomaly Detector")
    p.add_argument("--interval", type=float, default=5, help="Sampling interval (seconds)")
    p.add_argument("--window", type=int, default=24, help="Rolling window size (samples)")
    p.add_argument("--warmup", type=int, default=8, help="Min samples before detecting anomalies")
    p.add_argument("--threshold", type=float, default=0.25, help="Anomaly threshold (e.g., 0.25 = 25%% over baseline)")
    p.add_argument("--mount", default="/", help="Disk mountpoint to monitor (default: /)")
    p.add_argument("--log-file", default="anomaly_detector.log", help="Log file path")
    p.add_argument("--verbose", action="store_true", help="Verbose console logging")
    args = p.parse_args()

    setup_logger(args.log_file, args.verbose)
    logging.info(
        "Starting monitor | interval=%.1fs window=%d warmup=%d threshold=%.0f%% mount=%s",
        args.interval, args.window, args.warmup, args.threshold * 100, args.mount
    )

    hist = {
        "cpu": deque(maxlen=args.window),
        "mem": deque(maxlen=args.window),
        "disk": deque(maxlen=args.window),
    }

    psutil.cpu_percent(interval=None)

    try:
        while True:
            metrics = read_metrics(args.mount)
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for k, v in metrics.items():
                hist[k].append(v)

            for name in ("cpu", "mem", "disk"):
                is_anom, avg, baseline = detect_anomaly(
                    current=metrics[name],
                    history=hist[name],
                    min_samples=args.warmup,
                    threshold=args.threshold
                )
                if is_anom:
                    logging.warning(
                        "[ANOMALY] %s current=%s baseline_avg=%s (n=%d)",
                        name.upper(), pct_str(metrics[name]), pct_str(avg), len(hist[name])
                    )
                else:
                    logging.debug(
                        "%s current=%s baseline_avg=%s (n=%d)",
                        name.upper(), pct_str(metrics[name]), pct_str(avg if avg else 0), len(hist[name])
                    )

            logging.info(
                "CPU=%s MEM=%s DISK=%s",
                pct_str(metrics["cpu"]), pct_str(metrics["mem"]), pct_str(metrics["disk"])
            )

            time.sleep(args.interval)
    except KeyboardInterrupt:
        logging.info("Stopped by user.")

if __name__ == "__main__":
    main()


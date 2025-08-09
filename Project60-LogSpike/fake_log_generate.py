#!/usr/bin/env python3
import random
import time
from datetime import datetime

logfile = "/var/log/app.log"

levels = ["INFO", "DEBUG", "ERROR", "WARNING", "CRITICAL"]
messages = [
    "User login successful",
    "Connection established to database",
    "Timeout while connecting to service",
    "File not found: config.yaml",
    "Unhandled exception in processing",
    "API request completed",
    "Cache refreshed",
    "Failed to parse JSON response",
    "Memory usage exceeded threshold",
    "Disk space running low"
]

with open(logfile, "w") as f:
    for _ in range(200):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level = random.choices(
            levels,
            weights=[50, 30, 10, 7, 3],
            k=1
        )[0]
        msg = random.choice(messages)
        f.write(f"{ts} [{level}] {msg}\n")
        time.sleep(random.uniform(0.01, 0.1))

print(f"Sample log file generated at {logfile}")


from croniter import croniter
from datetime import datetime
import time

def notify(message):
    print(f"[{datetime.now()}] {message}")

# Define cron expressions
cron_expr_work = "*/10 * * * *"       # Every 10 minutes
cron_expr_break = "5-59/10 * * * *"   # Every 10 minutes, starting at :05, :15, etc.

# Set base time
base_time = datetime.now()

# Create cron iterators
cron_work = croniter(cron_expr_work, base_time)
cron_break = croniter(cron_expr_break, base_time)

# Get first scheduled times
next_work_time = cron_work.get_next(datetime)
next_break_time = cron_break.get_next(datetime)

while True:
    now = datetime.now()

    if now >= next_work_time:
        notify("🟢 Time to focus on work!")
        next_work_time = cron_work.get_next(datetime)

    if now >= next_break_time:
        notify("☕ Take a 5-minute break!")
        next_break_time = cron_break.get_next(datetime)

    time.sleep(1)

⏰ CronTaskScheduler – Focus and Break Timer Using croniter

📌 Problem Statement
Maintaining productivity while working remotely or studying can be challenging without proper time management. This tool uses cron expressions to periodically notify users when it's time to work or take a break.

💡 Scenario: Periodic Notifications Using Cron Schedules
This script simulates a simple productivity assistant in the terminal. It sends alternating reminders to:

🔁 Focus on work every 10 minutes (*/10 * * * *)

☕ Take a short break every 10 minutes but offset by 5 minutes (5-59/10 * * * *)

✅ Use Case
- Boost productivity using structured work/break cycles (e.g., Pomodoro-style).
- Useful for remote workers, developers, students, or focus training.
- Terminal-based automation using cron-like timing.

🛠️ Modules Used
- Module	Purpose
- croniter	Interprets cron expressions and schedules events
- datetime	Tracks current and future timestamps
- time	Pauses the loop efficiently with sleep()

🧠 How It Works
- Two cron expressions define work and break schedules.
- The script calculates the next execution time using croniter.
- It continuously checks if the current time matches the next scheduled event.
- On match, it prints a notification message and schedules the next one.


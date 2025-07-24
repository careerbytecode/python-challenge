import os
import shutil
import datetime
import schedule
import time

def backup_files(source_dir, backup_dir):
    # Get the current date and time for naming the backup folder
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder = os.path.join(backup_dir, f"backup_{current_time}")
    
    try:
        # Copy all files and subdirectories from source to backup folder
        shutil.copytree(source_dir, backup_folder)
        print(f"Backup successful! Files have been copied to {backup_folder}")
    
    except Exception as e:
        print(f"Error during backup: {e}")

# Function to perform scheduled backup
def job():
    source_directory = '/path/to/source'
    backup_directory = '/path/to/backup'
    backup_files(source_directory, backup_directory)

# Schedule the backup to run every day at 2:00 AM
schedule.every().day.at("02:00").do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds

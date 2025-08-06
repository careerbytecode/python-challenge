import psutil
import argparse
import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def find_zombies(clean=False):
    zombie_found = False

    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'status']):
        try:
            if proc.info['status'] == psutil.STATUS_ZOMBIE:
                zombie_found = True
                pid, ppid, name = proc.info['pid'], proc.info['ppid'], proc.info['name']
                logging.warning(f"Zombie Found -> PID: {pid}, PPID: {ppid}, Name: {name}")

                if clean:
                    try:
                        parent = psutil.Process(ppid)
                        logging.info(f"Attempting to terminate parent PID {parent.pid} ({parent.name()})")
                        parent.terminate()
                    except psutil.NoSuchProcess:
                        logging.error(f"Parent process {ppid} does not exist.")
                    except psutil.AccessDenied:
                        logging.error(f"Access denied when trying to terminate parent PID {ppid}.")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not zombie_found:
        logging.info("No zombie processes found.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Zombie Process Detector and Cleaner")
    parser.add_argument(
        '--clean',
        action='store_true',
        help="Attempt to clean zombies by terminating their parent processes"
    )
    return parser.parse_args()

if __name__ == "__main__":
    setup_logging()
    args = parse_arguments()
    find_zombies(clean=args.clean)


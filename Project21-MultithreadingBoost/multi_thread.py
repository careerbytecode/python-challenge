import threading
import time

def simulate_task(name, delay=2):
    print(f"Starting {name} (delay: {delay}s)")
    time.sleep(delay)
    print(f"Finished {name}")

def run_tasks(threaded=False, num_tasks=5, delay=2):
    start = time.time()
    threads = []

    for i in range(1, num_tasks + 1):
        if threaded:
            t = threading.Thread(target=simulate_task, args=(f"Task-{i}", delay))
            threads.append(t)
            t.start()
        else:
            simulate_task(f"Task-{i}", delay)

    if threaded:
        for t in threads:
            t.join()

    elapsed = round(time.time() - start, 2)
    mode = "Multi-threaded" if threaded else "Single-threaded"
    print(f"\nTotal time with {mode}: {elapsed} seconds")

if __name__ == "__main__":
    print("\n-+-+-+ Single Threaded -+-+-+")
    run_tasks(threaded=False)

    print("\n-+-+-+ Multi Threaded -+-+-+")
    run_tasks(threaded=True)

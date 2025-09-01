#log/logger.py

import threading
import datetime

#creates a lock so that only one thread can complete at once
#ensures only one thread writes to the log at once
_log_lock = threading.Lock()

#creates the timestamped message with the date formatted accurately
def log(message: str):
    with _log_lock:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        print(f"[{timestamp}] {message}")

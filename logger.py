#log/logger.py

import threading
import datetime

_log_lock = threading.Lock()

def log(message: str):
    """Thread-safe logging function with timestamps."""
    with _log_lock:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

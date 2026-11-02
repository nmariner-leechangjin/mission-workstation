"""Poll the web service by its Compose service name."""

import os
import time
import urllib.request


target = os.environ.get("TARGET_URL", "http://web:8000/health")
interval = float(os.environ.get("INTERVAL_SECONDS", "5"))

while True:
    try:
        with urllib.request.urlopen(target, timeout=3) as response:
            result = response.read().decode("utf-8").strip()
        print(f"GET {target} -> {result}", flush=True)
    except Exception as error:
        print(f"GET {target} -> {type(error).__name__}: {error}", flush=True)
    time.sleep(interval)

import os
import importlib
import threading
from dotenv import load_dotenv
import time
from examples.coingecko.coingecko_helper import send_request

load_dotenv()

def run_scheduler():
    while True:
        send_request()  # Execute send_request
        time.sleep(3600)  # Wait for 120 seconds (adjust as needed)

if __name__ == "__main__":
    print("Script started")

    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # Run CoinGecko API
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))
    app_api = importlib.import_module("examples.api.app")
    app_api.run(host=host, port=port)

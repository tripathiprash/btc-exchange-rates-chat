import importlib
import os
from dotenv import load_dotenv
import subprocess
from examples.coingecko.coingecko_helper import send_request
load_dotenv()

if __name__ == "__main__":

    print("script started")
    send_request()
    print("called send_request")

    # Run Discounts API
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))
    app_api = importlib.import_module("examples.api.app")
    app_api.run(host=host, port=port)

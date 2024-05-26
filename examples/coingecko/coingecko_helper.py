import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
def fetch_exchange_rates():
    url = "https://api.coingecko.com/api/v3/exchange_rates"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["rates"]
    else:
        return None

# Function to update JSONL file with exchange rates and timestamp
def update_jsonl(rates):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_folder = "./examples/data"  # Hardcoded path to the "data" folder
    jsonl_file = f"{data_folder}/exchange_rates.jsonl"

    # Check if the file exists
    if not os.path.exists(jsonl_file):
        # Create the file if it doesn't exist
        with open(jsonl_file, 'w') as file:
            pass  # Create an empty file

    # Append data to the JSONL file
    with open(jsonl_file, 'a') as file:
        for coin, data in rates.items():
            btc_data_str = json.dumps({
                "base_currency": "BTC",
                "target_currency": coin.upper(),
                "exchange_rate": data["value"],
                "timestamp": timestamp
            })
            doc_object = {"doc": btc_data_str}
            file.write(json.dumps(doc_object) + '\n')


#Process request
def send_request():
    print("send_request function called")
    exchange_rates = fetch_exchange_rates()
    if exchange_rates:
        update_jsonl(exchange_rates)
        print("Exchange rates updated successfully.")
    else:
        print("Error fetching exchange rates.")

# fetch_stocks.py (updated)
import requests, logging

logging.basicConfig(filename='pipeline.log', level=logging.INFO)
URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=10"  # 10 coins (~2KB)

def fetch_data():
    try:
        data = requests.get(URL, timeout=5).json()
        with open("crypto.json", "w") as f:
            f.write(str(data))
        logging.info("Data fetched")
    except Exception as e:
        logging.error(f"Failed: {e}")

if __name__ == "__main__":
    fetch_data()




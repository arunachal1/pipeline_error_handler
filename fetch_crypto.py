# fetch_stocks.py (updated)
import requests, logging, sqlite3

logging.basicConfig(filename='pipeline.log', level=logging.INFO)
URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=10"  # 10 coins (~2KB)

def fetch_data():
    try:
        data = requests.get(URL, timeout=5).json()
        with open("crypto.json", "w") as f:
            f.write(str(data))
        logging.info("Data fetched")
        return data
    except Exception as e:
        logging.error(f"Failed: {e}")

def save_to_db(data):  
    conn = sqlite3.connect("crypto.db")  
    c = conn.cursor()  
    c.execute("CREATE TABLE IF NOT EXISTS crypto (id INTEGER PRIMARY KEY, name TEXT, price REAL)")  
    for coin in data:  
        c.execute("INSERT INTO crypto (name, price) VALUES (?, ?)", (coin["name"], coin["current_price"]))  
    conn.commit()  
    conn.close()  

if __name__ == "__main__":
    data = fetch_data()
    save_to_db(data)




import requests, time, logging  

logging.basicConfig(filename='pipeline.log', level=logging.ERROR)  

def fetch_data(url, retries=3):  
    for _ in range(retries):  
        try:  
            data = requests.get(url, timeout=5).json()  
            return data  
        except Exception as e:  
            logging.error(f"Attempt {_+1}: {e}")  
            time.sleep(2)  
    return None  

if __name__ == "__main__":  
    data = fetch_data("https://api.twelvedata.com/stocks")  # Free API  
    if data:  
        with open("stocks.json", "w") as f:  
            f.write(str(data))  

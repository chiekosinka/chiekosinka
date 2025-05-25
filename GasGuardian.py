import requests
import time

# Задаём порог (в Gwei)
GAS_THRESHOLD = 50

def get_gas_price():
    response = requests.get("https://api.etherscan.io/api", params={
        "module": "gastracker",
        "action": "gasoracle",
        "apikey": "YourAPIKeyHere"
    })
    result = response.json()["result"]
    return int(result["ProposeGasPrice"])

def monitor_gas():
    while True:
        gas_price = get_gas_price()
        print(f"⛽ Current gas price: {gas_price} Gwei")
        if gas_price > GAS_THRESHOLD:
            print("⚠️ Gas price is high! Wait before sending transactions.")
        time.sleep(60)

if __name__ == "__main__":
    monitor_gas()

import requests
import json
import csv
import time  # Import time module for delays

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,  # Max limit per request
    "page": 1,
    "sparkline": False
}

# Open CSV for writing
with open("crypto_large_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Name", "Symbol", "Price (USD)", "Market Cap", "Market Rank",
        "24h Volume", "Price Change 24h", "Price Change 7d",
        "Price Change 30d", "ATH Price", "24h High", "24h Low",
        "Circulating Supply", "Total Supply"
    ])

    # Loop through pages to fetch 9000 coins with a delay
    for page in range(1, 37):  # 36 pages × 250 coins ≈ 9000
        params["page"] = page
        time.sleep(5)  # Add a 5-second delay between requests

        response = requests.get(url, params=params)
        
        if response.status_code == 200:  # Check for successful response
            data = response.json()
            for coin in data:
                writer.writerow([
                    coin.get("name"),
                    coin.get("symbol"),
                    coin.get("current_price"),
                    coin.get("market_cap"),
                    coin.get("market_cap_rank"),
                    coin.get("total_volume"),
                    coin.get("price_change_percentage_24h"),
                    coin.get("price_change_percentage_7d_in_currency"),
                    coin.get("price_change_percentage_30d_in_currency"),
                    coin.get("ath"),
                    coin.get("high_24h"),
                    coin.get("low_24h"),
                    coin.get("circulating_supply"),
                    coin.get("total_supply"),
                ])
        else:
            print(f"Error!! {response.status_code}")





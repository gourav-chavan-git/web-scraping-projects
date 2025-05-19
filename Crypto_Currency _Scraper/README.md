# Crypto Currency Scraper

This project collects real-time cryptocurrency market data using the [CoinGecko API](https://www.coingecko.com/en/api). It fetches data for up to 9,000 cryptocurrencies and stores it into a CSV file for analysis or visualization.

---

## 📌 Features
- Scrapes up to 9,000 cryptocurrencies using paginated API requests
- Extracts details such as:
  - Name, Symbol
  - Current Price (USD)
  - Market Cap & Rank
  - 24h Volume
  - Price Changes (24h, 7d, 30d)
  - All-Time High (ATH)
  - 24h High & Low
  - Circulating Supply, Total Supply
- Saves all data into a well-formatted `crypto_large_dataset.csv`
- Automatically respects API rate limits using delays

---

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: `requests`, `csv`, `time`
- **API**: CoinGecko REST API

---

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install requests


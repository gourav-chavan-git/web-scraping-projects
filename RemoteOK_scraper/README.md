# RemoteOK Job Listings Scraper

This Python project scrapes remote job listings from the [RemoteOK API](https://remoteok.io/api). It collects essential job data such as position titles, companies, logos, and tags, and saves the result to a CSV file.

---

## 📌 Features
- Scrapes remote job listings via RemoteOK public API
- Extracts:
  - Job Title
  - Company Name
  - Company Logo URL
  - Job Location
  - Tags (technologies, tools, skills)
- Saves all job data into a CSV file (`job_listings.csv`)

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Libraries**: `requests`, `BeautifulSoup`, `pandas`, `numpy`, `matplotlib`

---

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4 pandas numpy matplotlib

## Run the script:
- python remoteok_scraper.py

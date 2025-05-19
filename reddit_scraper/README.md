# Reddit r/algorithms Scraper

This project scrapes the top posts from the [r/algorithms](https://www.reddit.com/r/algorithms/) subreddit using the Reddit API (via `praw`). It collects metadata such as post titles, scores, comments, and author info, and saves the output to a CSV file for analysis.

---

## 📌 Features
- Collects up to 5,000 hot posts from r/algorithms
- Extracts:
  - Post Title
  - Upvotes (Score)
  - Number of Comments
  - Author Name
  - Post Date (Unix timestamp)
  - URL
  - Post Content (first 500 characters)
- Outputs the data into `reddit_algorithms_topics.csv`

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Libraries**: `praw`, `pandas`  
- **API**: Reddit API (requires credentials)

---

## 🔐 Setup

1. **Create a Reddit App**  
   Go to [Reddit Apps](https://www.reddit.com/prefs/apps) and create a script-type application to get your credentials:
   - `client_id`
   - `client_secret`
   - `user_agent`

2. **Create a `secret_keys.py` file** in the project directory:
   ```python
   REDDIT_CLIENT_ID = "your_client_id"
   REDDIT_CLIENT_SECRET = "your_client_secret"
   REDDIT_USER_AGENT = "your_user_agent"

How to Run
Install dependencies:
pip install praw pandas
Run the script:
python reddit_scraper.py

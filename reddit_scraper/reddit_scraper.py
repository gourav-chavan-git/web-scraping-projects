from secret_keys import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
import praw
import pandas as pd

# Reddit API Setup
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)

# Scrape r/algorithms
subreddit = reddit.subreddit("algorithms")  
posts = []

for post in subreddit.hot(limit=5000):  
    posts.append({
        "Title": post.title,
        "Upvotes": post.score,
        "Comments": post.num_comments,
        "Author": post.author.name if post.author else "Unknown",
        "Post Date": post.created_utc,  # Unix timestamp
        "URL": post.url,
        "Content": post.selftext[:500]  # First 500 characters of post text
    })

# Save to CSV
df = pd.DataFrame(posts)
df.to_csv("reddit_algorithms_topics.csv", index=False)






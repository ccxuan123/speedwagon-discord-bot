import os
import asyncpraw
import random

reddit = asyncpraw.Reddit(
        client_id = os.environ['REDDIT_APP_ID'],
        client_secret = os.environ['REDDIT_APP_SECRET'],
        user_agent = f"speedwagon-discord-bot:{os.environ['REDDIT_APP_ID']}:1.0"
    )

print(reddit.read_only)  # Output: True
subreddit = await  reddit.subreddit("learnpython")
async for submission in subreddit.hot(limit=10):
    print(submission.title)
"""
generate_dataset.py

Generates synthetic tweet sentiment dataset for the NLP Tweet Sentiment Classification challenge.
Produces a single raw CSV file: dataset/tweets.csv
"""

import random
import csv
import os
from datetime import datetime, timedelta

random.seed(42)

SENTIMENTS = ["positive", "negative", "neutral", "angry", "sad"]

TEMPLATES = {
    "positive": [
        "Just had the best day ever! {hashtag} so grateful",
        "Loving this {topic}! Absolutely amazing {emoji}",
        "Can't believe how great {topic} is today! {hashtag}",
        "This made my day! {mention} you're awesome {emoji}",
        "So happy right now! {topic} is the best thing ever",
        "Excited about {topic}! {hashtag} this is incredible",
        "Great news everyone! {topic} is finally here {emoji}",
    ],
    "negative": [
        "Terrible experience with {topic}. Never again. {hashtag}",
        "So disappointed in {topic}. This is unacceptable.",
        "Why does {topic} always fail when you need it most? {emoji}",
        "Absolutely furious about {topic}. {mention} fix this now",
        "Worst service ever. {topic} let me down again",
        "Can't believe {topic} would do this. Very disappointed.",
        "Failed expectations again. {topic} is a disaster {hashtag}",
    ],
    "neutral": [
        "Just checked out {topic}. It's okay I guess.",
        "Here's what happened today: {topic}. That's about it.",
        "Reminder: {topic} is happening tomorrow. {hashtag}",
        "Update on {topic}: things are proceeding as expected.",
        "New article about {topic} dropped. Worth reading.",
        "{topic} announced changes today. More details later.",
        "Meeting about {topic} went as planned. Moving on.",
    ],
    "angry": [
        "DONE with {topic}! This is RIDICULOUS {emoji}",
        "HOW is {topic} still a problem?! {hashtag} UNBELIEVABLE",
        "I am FURIOUS. {topic} has crossed a line. {mention}",
        "NO MORE. {topic} has ruined everything. Done.",
        "Why WHY WHY does {topic} keep doing this?! So angry.",
        "Absolute garbage. {topic} is the worst. {hashtag}",
        "Screaming into the void because of {topic}. ENOUGH.",
    ],
    "sad": [
        "Missing {topic} so much right now. It hurts {emoji}",
        "Crying because {topic} is over. End of an era.",
        "So sad about {topic}. Nothing feels the same.",
        "Heartbroken. {topic} is gone and I can't move on {emoji}",
        "Just thinking about {topic} makes me tear up.",
        "Why did {topic} have to end? I'm devastated.",
        "Low day. {topic} is not what it used to be {emoji}",
    ],
}

TOPICS = ["this app", "the election", "my team", "the update", "this service", "the game", 
          "this movie", "the weather", "my work", "the news", "this product", "our project"]
HASHTAGS = ["#trending", "#MustSee", "#viral", "#breaking", "#thoughts", "#update", "#rant"]
MENTIONS = ["@support", "@team", "@everyone", "@devs", "@admin", "@news"]
EMOJIS = ["😊", "😢", "😡", "🔥", "💯", "❤️", "😤", "🙏", "😭", "✨"]
LANGUAGES = ["en"] * 85 + ["es"] * 7 + ["fr"] * 5 + ["de"] * 3

SENTIMENT_COUNTS = {"positive": 14000, "negative": 12000, "neutral": 13000, "angry": 6000, "sad": 5000}

def make_tweet(sentiment):
    template = random.choice(TEMPLATES[sentiment])
    text = template.format(
        topic=random.choice(TOPICS),
        hashtag=random.choice(HASHTAGS),
        mention=random.choice(MENTIONS),
        emoji=random.choice(EMOJIS),
    )
    return text

def generate():
    os.makedirs("dataset", exist_ok=True)
    rows = []
    tweet_id = 1
    base_date = datetime(2024, 1, 1)

    for sentiment, count in SENTIMENT_COUNTS.items():
        for _ in range(count):
            text = make_tweet(sentiment)
            lang = random.choice(LANGUAGES)
            created = base_date + timedelta(minutes=random.randint(0, 525600))
            rows.append({
                "tweet_id": tweet_id,
                "text": text,
                "sentiment": sentiment,
                "language": lang,
                "created_at": created.strftime("%Y-%m-%d %H:%M:%S"),
                "char_count": len(text),
                "word_count": len(text.split()),
                "has_hashtag": "#" in text,
                "has_mention": "@" in text,
                "has_url": "http" in text,
            })
            tweet_id += 1

    random.shuffle(rows)

    fieldnames = ["tweet_id", "text", "sentiment", "language", "created_at",
                  "char_count", "word_count", "has_hashtag", "has_mention", "has_url"]

    with open("dataset/tweets.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} tweets -> dataset/tweets.csv")

if __name__ == "__main__":
    generate()

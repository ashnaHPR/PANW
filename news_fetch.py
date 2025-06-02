import os
import requests
import datetime
import json
import csv

# Use environment variable for security; fallback to hardcoded (temporary for local testing)
API_KEY = os.getenv("NEWSAPI_KEY", "9aadb2e6b74b4d28874b2e006e8f49d5")

# Spokespeople and Company
spokespeople = ["Carla Baker", "Scott McKinnon"]
company = "Palo Alto Networks"

# Build query string
joined_spokespeople = '" OR "'.join(spokespeople)
query = f'("{company}") AND ("{joined_spokespeople}")'

# News API endpoint
url = "https://newsapi.org/v2/everything"
params = {
    "q": query,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": API_KEY
}

# Get current date for logging
today = datetime.datetime.now().strftime("%Y-%m-%d")
log_file = f"logs/news_{today}.json"

# Make the request
response = requests.get(url, params=params)
data = response.json()

# Save results to log file
os.makedirs("logs", exist_ok=True)
with open(log_file, "w") as f:
    json.dump(data, f, indent=2)

# Extract relevant info from articles
results = []
if "articles" in data:
    for article in data["articles"]:
        results.append({
            "date": article.get("publishedAt", "")[:10],  # just date part YYYY-MM-DD
            "headline": article.get("title", ""),
            "source": article.get("source", {}).get("name", ""),
            "url": article.get("url", "")
        })
else:
    print("No articles found or error:", data)

# Save results to CSV
csv_file = "news_results.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["date", "headline", "source", "url"])
    writer.writeheader()
    for item in results:
        writer.writerow(item)

print(f"Saved {len(results)} news items to {csv_file}")

# Print top headlines for visibility
for i, article in enumerate(results, 1):
    print(f"{i}. {article['headline']} - {article['source']}")

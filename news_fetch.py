import os
import requests
import datetime
import json

# Use environment variable for security; fallback to hardcoded (temporary for local testing)
API_KEY = os.getenv("NEWSAPI_KEY", "your-newsapi-key-here")

# Spokespeople and Company
spokespeople = ["Carla Baker", "Scott Mckinnon"]
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
 # Use environment variable for security; fallback to hardcoded (temporary for local testing)
API_KEY = os.getenv("NEWSAPI_KEY", "9aadb2e6b74b4d28874b2e006e8f49d5")

}

# Make the request
response = requests.get(url, params=params)
data = response.json()

# Save results to JSON file
os.makedirs("data", exist_ok=True)
with open("data/news_results.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved {len(data.get('articles', []))} news articles to data/news_results.json")

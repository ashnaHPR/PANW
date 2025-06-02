import os
import requests
import json
from datetime import datetime

# Use environment variable for security
API_KEY = os.getenv("NEWSAPI_KEY", "your-newsapi-key-here")

# Company and spokespeople
company = "Palo Alto Networks"
spokespeople = ["Carla Baker", "Scott Mckinnon"]

# Properly build query: quote each spokesperson name
quoted_names = [f'"{name}"' for name in spokespeople]
query = f'("{company}") AND ({" OR ".join(quoted_names)})'

# NewsAPI request setup
url = "https://newsapi.org/v2/everything"
params = {
    "q": query,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

articles = data.get("articles", [])
print(f"📣 Found {len(articles)} articles")

# Create output directory
os.makedirs("docs", exist_ok=True)

# Generate HTML file
html_path = "docs/index.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write("<html><head><meta charset='UTF-8'><title>Palo Alto Networks News</title>")
    f.write("<style>body { font-family: Arial; padding: 20px; } table { border-collapse: collapse; width: 100%; }")
    f.write("th, td { border: 1px solid #ddd; padding: 8px; } th { background-color: #f2f2f2; }</style></head><body>")
    f.write(f"<h1>Palo Alto Networks Media Tracker</h1><p>Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}</p>")
    f.write("<table><tr><th>Date</th><th>Headline</th><th>Source</th><th>Link</th></tr>")

    for article in articles:
        date = article.get("publishedAt", "")[:10]
        title = article.get("title", "N/A")
        source = article.get("source", {}).get("name", "")
        url = article.get("url", "#")
        f.write(f"<tr><td>{date}</td><td>{title}</td><td>{source}</td><td><a href='{url}' target='_blank'>Link</a></td></tr>")

    f.write("</table></body></html>")

print(f"✅ Saved HTML to {html_path}")

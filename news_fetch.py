import os
import requests
import datetime
import json

# Use environment variable for security; fallback to a placeholder (for local testing)
API_KEY = os.getenv("NEWSAPI_KEY", "your-newsapi-key-here")

# Spokespeople and Company
spokespeople = ["Carla Baker", "Scott Mckinnon"]
company = "Palo Alto Networks"

# Build query string for NewsAPI
joined_spokespeople = '" OR "'.join(spokespeople)
query = f'("{company}") AND ("{joined_spokespeople}")'

# News API endpoint and parameters
url = "https://newsapi.org/v2/everything"
params = {
    "q": query,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": API_KEY  # <-- Correctly placed here
}

# Make the API request
response = requests.get(url, params=params)

# Check for request errors
if response.status_code != 200:
    print(f"Error: API request failed with status code {response.status_code}")
    print(response.tex

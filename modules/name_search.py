# name_search.py
import requests
from bs4 import BeautifulSoup

def search_by_name(name):
    platforms = {
        "facebook": f"https://www.facebook.com/{name}",
        "twitter": f"https://twitter.com/{name}",
        "instagram": f"https://instagram.com/{name}",
    }
    
    results = {}
    for platform, url in platforms.items():
        response = requests.get(url)
        if response.status_code == 200:
            results[platform] = url
    return results
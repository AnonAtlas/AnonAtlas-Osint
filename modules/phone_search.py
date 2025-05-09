# phone_search.py
import requests

def search_by_phone(phone):
    url = f"https://api.truecaller.com/v1/search?phone={phone}"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    response = requests.get(url, headers=headers)
    return response.json()
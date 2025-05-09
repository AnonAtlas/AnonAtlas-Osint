# email_osint.py
import requests

def analyze_email(email):
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=YOUR_API_KEY"
    response = requests.get(url)
    return response.json()
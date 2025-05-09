# ip_analysis.py
import shodan

def analyze_ip(ip):
    api = shodan.Shodan("YOUR_SHODAN_API_KEY")
    try:
        results = api.host(ip)
        return results
    except Exception as e:
        return str(e)
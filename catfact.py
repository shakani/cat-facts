import requests
import json 

x = 3

def fetch_fact() -> str:
    """
    Generates and returns random cat fact.
    """
    url = "https://catfact.ninja/fact"
    fact_json = requests.get(url) 
    fact_json = fact_json.json()
    return fact_json['fact']

if __name__ == "__main__":
    print(fetch_fact())
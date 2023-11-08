import requests
import json 

def fetch_pic() -> str:
    """
    Fetches a URL for a random cat picture.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    data = requests.get(url)
    data = data.json() 
    return data[0]['url']
    

if __name__ == "__main__":
    print(fetch_pic())
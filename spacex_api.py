import requests

def get_all_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    return response.json()

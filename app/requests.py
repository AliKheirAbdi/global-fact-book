import requests

def get_all_countries():
    r =  requests.get('https://restcountries.eu/rest/v2/all')
    all_countries = r.json()
    return all_countries

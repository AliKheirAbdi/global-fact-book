import requests

def get_all_countries():
    r =  requests.get('https://restcountries.eu/rest/v2/all')
    all_countries = r.json()
    return all_countries

def get_countries_by_region(region):
    r = requests.get(f'https://restcountries.eu/rest/v2/region/{region}')
    countries = r.json()
    return countries

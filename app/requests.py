import requests

def get_all_countries():
    r =  requests.get('https://restcountries.eu/rest/v2/all')
    all_countries = r.json()
    return all_countries

def get_countries_by_continents(continent,sub_region):
    r = requests.get(f'https://restcountries.eu/rest/v2/region/{continent}')
    all_countries = r.json()
    if continent == 'americas':
        countries = filter_americas(all_countries,sub_region)
        return countries
    return all_countries


def filter_americas(all_countries,sub_region):
    south_countries = []
    north_countries = []
    for country in all_countries:
        if country.get('subregion') == sub_region and sub_region == 'South America':
            south_countries.append(country)
        elif country.get('subregion') == sub_region and sub_region == 'Northern America':
            north_countries.append(country)
        elif country.get('subregion')  == 'Caribbean':
            north_countries.append(country)



    if sub_region == 'South America':
        return south_countries
    else:
        return  north_countries

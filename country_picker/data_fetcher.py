# country_picker/data_fetcher.py

import requests
from .utils import parse_country_names

def fetch_country_data() -> list[str]:
    """
    Fetch JSON data from the countries API and return a list of country names.
    Returns an empty list if the request fails or data is invalid.
    """
    url = "https://www.apicountries.com/countries"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return parse_country_names(data)
    except requests.RequestException:
        return []

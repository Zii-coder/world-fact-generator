import requests
import random
from rich.console import Console

consle = Console()

#Fetching API and country data
API_URL = "https://restcountries.com/v3.1/all"

def fetch_country_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        consle.print("Error fetching data!")
        return None

    def main():
        console.print("Fetch world facts")
        country_data = fetch_country_data()

        if _name_ == "_main_":
            main()

import requests
import random
from rich.console import Console

console = Console()

#Fetching API and country data
API_URL = "https://restcountries.com/v3.1/all"

def fetch_country_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        console.print("Error fetching data!")
        return None
#picking a random country
    def get_random_country(data):
        return random.choice(data)

    #Extracting key infromation about the country
    def display_country_info(country):
        name = country.get("name", {}.get("common", "Unknown"))
        capital = country.get("capital", ["Unknown"])[0]
        region = country.get("region", "Unknown")
        population = country.get("population", "Unknown")

        console.print(f"[bold cyan]{name}[/bold cyan]")
        console.print(f"Capital: [bold green]{capital}[/bold green]")
        console.print(f"Region: [bold yellow]{region}[/bold yellow]")
        console.print(f"Population: [bold magenta]{population:, }[/bold green]")



    def main():
        console.print("Fetch world facts")
        country_data = fetch_country_data()
        if country_data:
            random_country = get_random_country(country_data)
            display_country_info(random_country)

        if __name__ == "__main__":
            main()


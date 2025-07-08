import requests

API_URL = "https://restcountries.com/v3.1/name/uae"

def fetch_country_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching API data: {e}")
        return None

def display_country_info(countries):
    if not countries:
        print("No country data available.")
        return

    for country in countries:
        name = country.get("name", {}).get("common")
        capital = ", ".join(country.get("capital"))
        population = country.get("population")
        region = country.get("region")

        print("-+" * 20)
        print(f"Country   : {name}")
        print(f"Capital   : {capital}")
        print(f"Population: {population}")
        print(f"Region    : {region}")
        print("-+" * 20)

def main():
    data = fetch_country_data(API_URL)
    display_country_info(data)

if __name__ == "__main__":
    main()
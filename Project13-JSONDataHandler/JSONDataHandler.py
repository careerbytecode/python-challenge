import requests
from bs4 import BeautifulSoup
import json

def validate_json_ld(url):
    try:
        # Step 1: Fetch the webpage
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 2: Find all <script type="application/ld+json">
        scripts = soup.find_all("script", type="application/ld+json")

        for index, script in enumerate(scripts):
            try:
                # Step 3: Parse the JSON-LD
                data = json.loads(script.string)

                # Step 4: Pretty print the valid JSON-LD
                print(f"\n✅ JSON-LD block {index + 1} is valid:\n")
                print(json.dumps(data, indent=4))

            except json.JSONDecodeError as e:
                print(f"\n❌ JSON-LD block {index + 1} is invalid: {e}")

    except Exception as e:
        print(f"Error fetching page: {e}")

# Example usage:
validate_json_ld("https://www.example.com")

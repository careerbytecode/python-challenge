import requests
from bs4 import BeautifulSoup
import json
from jsonschema import validate, ValidationError

url = "https://www.healthline.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
scripts = soup.find_all("script", type="application/ld+json")
for script in scripts:
    data = json.loads(script.string)
    print(data)


try:
    validate(instance=data, schema=data)
    print("\nValid schema!")
except ValidationError as e:
    print("Validation failed:", e)

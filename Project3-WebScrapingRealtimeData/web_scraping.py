import requests
from bs4 import BeautifulSoup

def scrape_web():
    url = "https://www.scrapethissite.com/pages/forms/?per_page=20"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.text, "html.parser")
    
    table = soup.find("table", class_="table")
    results = []

    if table:
        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = []
            for td in row.find_all("td"):
                text = td.text.strip()
                cols.append(text)

            if len(cols) >= 3:
                Team_name = cols[0]
                Year = cols[1]
                Wins = cols[2]
                results.append({
                    "Team_Name": Team_name,
                    "Year": Year,
                    "Wins": Wins
                })

    return results

if __name__ == "__main__":
    data = scrape_web()
    for item in data:
        print(item)

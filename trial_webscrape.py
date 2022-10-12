from bs4 import BeautifulSoup
import requests
import csv

# URL to scrape
url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"

# Get the HTML from the URL
r = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(r.text, "html.parser")

# Get the table
table = soup.find("table", {"id": "per_game_stats"})
table_body = table.find("tbody")

# Get the rows
rows = table_body.find_all("tr")

# Get the headers
headers = [th.text for th in table.find("thead").find_all("th")]

# Write the data to a CSV file
with open("nba.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for row in rows:
        data = [td.text for td in row.find_all("td")]
        writer.writerow(data)

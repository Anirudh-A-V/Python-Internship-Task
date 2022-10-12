from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import numpy as np

# URL to scrape
url = "https://www.cnbc.com/search/?query=green%20hydrogen&qsearchterm=green%20hydrogen"

# Get the HTML from the URL
page = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(page.content, "html.parser")

# Get the table
table = soup.find("div", {"id": "searchcontainer"})

# Get the Heading
heading = table.find("div", {"class": "Card-title"})
print(heading)
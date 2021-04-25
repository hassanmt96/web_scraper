import requests
from bs4 import BeautifulSoup

res = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(res.text)

print(soup.body)

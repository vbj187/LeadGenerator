import requests
from bs4 import BeautifulSoup
import pandas

URL = 'http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

table = soup.find('table', {'class': 'table100'})

print(table)

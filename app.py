import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html'

# response = requests.get(URL)

# soup = BeautifulSoup(response.text, 'html.parser')

# # print(soup)

# table = soup.find('table', {'class': 'table100'}).tbody

# print(table)

# rows = table.find_all('tr')

# columns = [v.text for v in rows[0].find_all('td')]


def get_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_list(url):
    table = url.find('table', {'class': 'table100'}).tbody
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        return row


page = get_webpage(URL)
get_list(page)

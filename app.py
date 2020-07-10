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
    page = response.text
    return page


def get_webpage_text(htm):
    soup = BeautifulSoup(htm, 'html.parser')
    return soup.text


def get_list(htm):
    """
    for every tr with the td containing company name
    get the href attribute for to the company's website 
    """
    # https://stackoverflow.com/questions/43193969/how-to-get-an-attribute-value-using-beautifulsoup-and-python/43194401

    soup = BeautifulSoup(htm, 'lxml')
    item = soup.findAll('a', {'class': '100link'})
    nameAndUrl = []
    for tag in item:
        if tag.text != 'View From The Top Profile':
            nameAndUrl.append([tag.text, tag.get('href')])
    # print(nameAndUrl)
    # print(len(nameAndUrl))
    # print(nameAndUrl)
    return nameAndUrl


def forEachCompany(lis):
    for one, two in lis:
        print(two)


def json_to_csv_file(jsonFile, csvFile):
    # https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
    return jsonFile


one = get_webpage(URL)
two = get_webpage_text(one)
three = get_list(one)
four = forEachCompany(three)

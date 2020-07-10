import requests
from bs4 import BeautifulSoup

URL = 'http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.html'


def get_webpage(url):
    try:
        response = requests.get(url)
        page = response.text
        return page
    except:
        return None


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


def for_each_company(lis):
    for companyName, companyMainPage in lis:
        # print(companyMainPage)
        companyPageAsInput = get_webpage(companyMainPage)
        get_contact_page_link(companyPageAsInput)


def get_contact_page_link(companyPage):
    try:
        soap = BeautifulSoup(companyPage, 'html.parser')
        contact_link = soap.find(text='Contact')
        return
    except:
        soap = BeautifulSoup(companyPage, 'html.parser')
        contact_link = soap.find(text='About Us')
        return
    else:
        return None


def get_location():
    return


def json_to_csv_file(jsonFile, csvFile):
    # https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
    return


one = get_webpage(URL)
two = get_webpage_text(one)
three = get_list(one)
four = for_each_company(three)

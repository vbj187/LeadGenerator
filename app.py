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
    firstLead = slice(1)

    # print(nameAndUrl[firstLead])
    # returns [['Acquia, Inc', 'http://acquia.com']]
    return nameAndUrl[firstLead]


def for_each_company(lis):
    # print(len(lis))
    # count = 0
    for companyName, companyMainPageUrl in lis:
        get_contact_page_link(companyMainPageUrl)
        # companyPageAsInput = get_contact_page_link(companyMainPageUrl)
        # get_contact_page_link(companyPageAsInput)
        # print(companyPageAsInput)
        # count += 1
        # print(count)


def get_contact_page_link(companyPageUrl):
    # print(f"{companyPageUrl}/about-us")
    url = f"{companyPageUrl}/about-us"
    response = requests.get(url)
    page = response.text
    print(page)


def get_location():
    return


def json_to_csv_file(jsonFile, csvFile):
    # https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
    return


one = get_webpage(URL)
two = get_webpage_text(one)
three = get_list(one)
four = for_each_company(three)

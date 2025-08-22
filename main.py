import requests
from bs4 import BeautifulSoup

# url = "https://www.tcmb.gov.tr/kurlar/today.xml"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "xml")
#
# usd = soup.find("Currency", {"CurrencyCode": "USD"})
# usd_alis = usd.find("ForexBuying").text
# usd_satis = usd.find("ForexSelling").text
#
# print("USD/TRY Alış:", usd_alis)
# print("USD/TRY Satış:", usd_satis)

# urls = ["https://www.milliyet.com.tr/arama/", "https://www.sozcu.com.tr/arama?search=", "https://www.sabah.com.tr/arama?query=", "https://www.ntv.com.tr/arama?q=", "https://www.cnnturk.com/arama?q="]

def main():
    keyword = input("Please enter a keyword: ")
    links = []
    searches = [searchMilliyet(keyword), searchSabah(keyword), searchNtv(keyword)]
    for search in searches:
        links.append(search)
    return links


def searchMilliyet(keyword):
    links = []
    url_clear = "https://www.milliyet.com.tr"
    url = "https://www.milliyet.com.tr/arama/" + keyword
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}, allow_redirects=False)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tags = soup.find_all("a", class_="news__link")
    for a_tag in a_tags:
        link = a_tag.get("href")
        if link and link.startswith("/gundem"):
            link = url_clear + link
            links.append(link)
    return links

"""def searchSozcu(keyword):
    links = []
    url_clear = "https://www.sozcu.com.tr"
    url = "https://www.sozcu.com.tr/arama?search=" + keyword
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}, allow_redirects=True)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all("div", class_="col-md-6 col-lg-4 mb-4")
    for div in divs:
        a_tag = div.find("a")
        if a_tag:
            link = a_tag.get("href")
            if link.startswith("/"):
                link = url_clear + link
                links.append(link)
    return links"""

def searchSabah(keyword):
    links = []
    url_clear = "https://www.sabah.com.tr"
    url = "https://www.sabah.com.tr/arama?query=" + keyword
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}, allow_redirects=True)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all("div", attrs={"data-search-item": ""})
    for div in divs:
        a_tag = div.find("a")
        if a_tag:
            link = a_tag.get("href")
            if link.startswith("/yasam") or link.startswith("/haberplus"):
                link = url_clear + link
                links.append(link)
    return links

def searchNtv(keyword):
    links = []
    url_clear = "https://www.ntv.com.tr"
    url = "https://www.ntv.com.tr/arama?q=" + keyword
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}, allow_redirects=True)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all("div", class_="gsc-results gsc-webResult")
    for div in divs:
        a_tag = div.find("a")
        if a_tag:
            link = a_tag.get("href")
            if link.startswith("/"):
                link = url_clear + link
                links.append(link)
    return links

# def sortLinks(keyword):
#     links = []
#     searches = [searchMilliyet(keyword), searchSozcu(keyword), searchSabah(keyword)]
#     for search in searches:
#         links.append(search)
#     newsDict = {}
#     return links


for i in main():
    for j in i:
        print(j)

    print("..............")
    print("..............")
    print("..............")


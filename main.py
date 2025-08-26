import requests
from bs4 import BeautifulSoup

def main():
    keyword = input("Please enter a keyword: ")
    searchLinks(keyword)

def acquireLinks(keyword):
    searches = [searchMilliyet(keyword), searchSabah(keyword), searchSozcu(keyword)]
    links = [item for sublist in searches for item in sublist]
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

def searchSozcu(keyword):
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
    return links


def searchLinks(keyword):
    links = acquireLinks(keyword)
    newsDictionary = []

    for link in links:
        try:
            response = requests.get(link, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}, allow_redirects=True, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            header_element = soup.find("h1")
            header_text = header_element.text.strip() if header_element else "Başlık bulunamadı"
            paragraphs = soup.find_all("p")
            paragraph_texts = [p.text.strip() for p in paragraphs if p.text.strip()]
            combined_text = " ".join(paragraph_texts)
            if combined_text:
                newsDictionary.append([header_text, combined_text])

        except Exception as e:
            print(f"Hata: {link} işlenirken sorun oluştu - {e}")
            continue
    return newsDictionary
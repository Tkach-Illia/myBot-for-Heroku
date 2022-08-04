import requests
from bs4 import BeautifulSoup as bs
import random

url = ''
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.438'}

def get_html(url, params=None):
    return requests.get(url,headers=HEADERS, params=params)

def get_content_img(html):
    items = [a.get('data-src') for a in bs(html, 'html.parser').find_all('img', class_='rg_i Q4LuWd')]
    return("Не знайдено" if items == [] else items[random.randint(0, len(items)-1)])


def parse_wiki(string):
	url = 'https://uk.wikipedia.org/wiki/'+string
	html = get_html(url)
	return "Не знайдено" if html.status_code != 200 else bs(html.text, 'html.parser').find("div", {'class':'mw-parser-output'}).find("p").get_text()

def search_google_img(string):
	url = 'https://www.google.com/search?tbm=isch&q='+string
	html = get_html(url)
	return "Не знайдено" if html.status_code != 200 else get_content_img(html.text)
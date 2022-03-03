import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url, timeout=1):
    try:
        sleep(1)
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    lista_url = []

    for novidades_tecmundo in selector.css("div.tec--list__item"):
        url = novidades_tecmundo.css("a[href*='https']::attr(href)").get()
        lista_url.append(url)
    return lista_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

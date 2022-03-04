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
    selector = Selector(html_content)
    pagination = selector.css("a[href*='page']::attr(href)").get()
    return pagination


def count(string):
    if not string:
        return 0
    list = string.split()
    for i in list:
        if i.isdigit():
            return int(i)


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    writer = selector.css("div[class*='author'] p *::text").get()
    shares_count = selector.css("div[class*='toolbar__item']::text").get()
    comments_count = selector.css("button[id*='comm']::attr(data-count)").get()
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    sources = selector.css(
        ".z--mb-16 h2.z--text-base.z--font-semibold ~ div a.tec--badge::text"
    ).getall()
    categories = selector.css("div[id*='categories'] a::text").getall()

    if not writer:
        writer = selector.css("a[href*=autor]::text").get()

    return {
        "url": selector.css("meta[property*='url']::attr(content)").get(),
        "title": selector.css("h1[id$='title']::text").get(),
        "timestamp": selector.css(
            "time#js-article-date::attr(datetime)"
        ).get(),
        "writer": writer.strip() if writer else writer,
        "shares_count": count(shares_count),
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

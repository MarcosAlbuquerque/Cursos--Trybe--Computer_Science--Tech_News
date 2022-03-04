from tech_news.database import find_news
from datetime import date

# Requisito 6
def search_by_title(title):
    new = find_news()
    filter = [
        new for new in new if new["title"].lower() == title.lower()
    ]
    return [(new["title"], new["url"]) for new in filter]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

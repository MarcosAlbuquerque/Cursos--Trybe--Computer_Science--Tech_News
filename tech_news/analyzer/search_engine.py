from datetime import datetime
from tech_news.database import find_news, search_news

# Requisito 6
def search_by_title(title):
    new = find_news()
    filter = [new for new in new if new["title"].lower() == title.lower()]
    return [(new["title"], new["url"]) for new in filter]


# Requisito 7
def search_by_date(date):
    try:
        format_data = "%Y-%m-%d"
        data = datetime.strptime(date, format_data)
        data_to_str = datetime.strftime(data, format_data)
        get_all = search_news(
            {
                "timestamp": {
                    "$regex": data_to_str,
                    "$options": "i",
                }
            }
        )

        n_filter = [item for item in get_all]
        return [(new["title"], new["url"]) for new in n_filter]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    get_all = search_news({"sources": {"$regex": source, "$options": "i"}})
    n_tulpa = [new for new in get_all]

    return [(new["title"], new["url"]) for new in n_tulpa]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

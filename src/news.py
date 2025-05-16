import json
import os
import requests

from dotenv import load_dotenv
from src.config import BASE_URL, GET_DATE, QUERY

load_dotenv()
API_KEY = os.getenv("API_KEY_NEWS")


def get_news(exclude_words: list, query: str = QUERY, api_key: str = API_KEY) -> list:
    params = {
        "q": query,
        # "from": GET_DATE,
        "sortBy": "publishedAt",
        "apiKey": api_key
    }
    try:
        response = requests.get(
            url=BASE_URL,
            params=params
        )

        news_data = response.json()
        if news_data.get('status') != 'ok':
            return []

        articacles_list = news_data.get('articles', [])
        result = []

        for article in articacles_list:

            content = article.get('content').lower()
            title = article.get('title').lower()

            flag = False
            for word in exclude_words:
                if word.lower() in content or word in title:
                    flag = True

            if not flag:
                result.append({
                    'title': article.get('title'),
                    'author': article.get('author'),
                    'description': article.get('description'),
                    'url': article.get('url')
                })
        return result
    except requests.RequestException:
        return []
    except json.JSONDecoder:
        return []
    except Exception:
        return []

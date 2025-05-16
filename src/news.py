import json
import os
import requests
import logging

from dotenv import load_dotenv
from src.config import BASE_URL, GET_DATE, QUERY

# import log_config
#
# logger = log_config.get_logger(__name__)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/news.log', "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

logger.warning("Получение АPI")
load_dotenv()
logger.info('API получено')
API_KEY = os.getenv("API_KEY_NEWS")


def get_news(exclude_words: list, query: str = QUERY, api_key: str = API_KEY) -> list:
    params = {
        "q": query,
        # "from": GET_DATE,
        "sortBy": "publishedAt",
        "apiKey": api_key
    }
    try:
        logger.info("Выполнение запроса с ключевыми словами: %s", query)
        response = requests.get(
            url=BASE_URL,
            params=params
        )

        news_data = response.json()
        if news_data.get('status') != 'ok':
            logger.warning("Статей не нашлось")
            return []

        articacles_list = news_data.get('articles', [])
        result = []

        for article in articacles_list:

            content = article.get('content').lower()
            title = article.get('title').lower()

            flag = False
            logger.info("Фильтруем новости по словам исключениям: %s", ','.join(exclude_words))
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
    except requests.RequestException as ex:
        logger.error("Произошла ошибка: %s", ex)
        return []
    except json.JSONDecoder as ex:
        logger.error("Произошла ошибка: %s", ex)
        return []
    except Exception as ex:
        logger.error("Произошла ошибка: %s", ex)
        return []

import logging
from datetime import datetime

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/config.log', "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

logger.info("Обработка даты")
date_now = datetime.now()
GET_DATE = date_now.strftime("%Y-%m-%d")
logger.info("Обработка URL")
BASE_URL = "https://newsapi.org/v2/everything"
logger.info("Обработка ключевых слов")
QUERY = "Apple mask"

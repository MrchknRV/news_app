import logging
from src.config import QUERY, GET_DATE
from src.news import get_news
from src.save_to_json import save_to_json

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/main.log', "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def main():
    try:
        logger.warning("Приложение запущено")
        logger.info("Получение статей")
        result = get_news(["Twitter"], QUERY)
        file_name = f'{GET_DATE}_{QUERY.replace(" ", "_")}.json'
        file_path = f'data_news/{file_name}'

        logger.info("Запись статей в файл")
        save_to_json(result, file_path)

        logger.warning("Приложение завершило работу")
    except Exception as ex:
        logger.error("Произошла ошибка: %s", ex)


if __name__ == "__main__":
    main()

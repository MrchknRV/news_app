import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/save_to_json.log', "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def save_to_json(data: list, file_path: str) -> None:
    try:
        logger.info('Записываем данные в файл: %s', file_path)
        with open(file_path, "a", encoding="UTF-8") as file:
            json.dump(data, file, indent=4)
    except Exception as ex:
        logger.error("Произошла ошибка: %s", ex)

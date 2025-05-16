from src.config import QUERY, GET_DATE
from src.news import get_news
from src.save_to_json import save_to_json


def main():
    result = get_news(["Twitter"], QUERY)
    file_name = f'{GET_DATE}_{QUERY.replace(" ", "_")}.json'
    file_path = f'data_news/{file_name}'
    save_to_json(result, file_path)


if __name__ == "__main__":
    main()

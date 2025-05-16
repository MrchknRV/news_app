import json


def save_to_json(data: list, file_path: str) -> None:
    try:
        with open(file_path, "a", encoding="UTF-8") as file:
            json.dump(data, file, indent=4)
    except Exception:
        pass

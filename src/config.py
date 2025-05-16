from datetime import datetime

date_now = datetime.now()

GET_DATE = date_now.strftime("%Y-%m-%d")
BASE_URL = "https://newsapi.org/v2/everything"

QUERY = "Apple mask"

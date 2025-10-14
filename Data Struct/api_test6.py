import requests
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Giả lập header của trình duyệt thật
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/128.0.0.0 Safari/537.36"
}

data = requests.get(URL, headers= headers).text

tables = pd.read_html(data)
df = tables[2]
print(df)
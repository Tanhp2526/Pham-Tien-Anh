import pandas as pd
import requests

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"

# Giả lập header của trình duyệt thật
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/128.0.0.0 Safari/537.36"
}

# Tải HTML bằng requests
data = requests.get(URL, headers=headers)
html = data.text

# Đọc bảng bằng pandas
tables = pd.read_html(html)
df = tables[0]

print(df.head())

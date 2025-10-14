#import thu vien
import requests
import json
import pandas as pd

#gui yeu cau den API
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

#chuyen du lieu json text thanh Python object
results = json.loads(data.text)

#lam phang du kieu
df2 = pd.json_normalize(results)

banana = df2.loc[df2["name"] == "Banana"]
print(banana.iloc[0]["nutritions.calories"])

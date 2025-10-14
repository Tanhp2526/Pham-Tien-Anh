import requests
import json
import pandas as pd

data = requests.get("https://official-joke-api.appspot.com/jokes/ten")

results = json.loads(data.text)

df2 = pd.json_normalize(results)

print(df2.iloc[0]["punchline"])
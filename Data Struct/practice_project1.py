import pandas as pd
import numpy as np

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

tables = pd.read_html(url)
df = tables[3]

df.columns = range(df.shape[1]) # thay doi ten cac cot theo chi so

df = df[[0,2]]# giu lai cot co chi so 0 va 2

df = df.iloc[1:11, :]# hang tu 1 den 10

df.columns = ["Country", "GDP (Million USD)"]# gan ten cot


df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(int)# chuyen du lieu cot nay sang kieu int

df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000 

df.rename(columns= {"GDP (Million USD)" : "GDP (Billion USD)"})

print(df)



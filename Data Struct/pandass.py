import pandas as pd 

data = {"Student" : ["David", "Samuel", "Terry", "Evan"],
        "Age" : [27, 24, 22, 32],
        "Country" : ["UK", "Canada", "China", "USA"],
        "Course" : ["Python", "Data Structures", "Machine Learning", "Web Development"],
        "Marks" : [85, 72, 89, 76]}

df = pd.DataFrame(data)
#b = df["Marks"]
#c = df[["Country", "Course"]]
#print(c)
#df.to_csv("pandas_test.csv", index = False)
#print(df.describe())
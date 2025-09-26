from csv import reader
from app import App

apps = []

with open('file.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for name, description, category in csv_reader:
        apps.append(App(name, description, category))

print(apps)
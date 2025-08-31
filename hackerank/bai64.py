import calendar

m, d, y = map(int, input().split())

res = calendar.weekday(y,m,d)

print(calendar.day_name[res].upper())
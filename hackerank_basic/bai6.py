s = input()

s = s.replace(",", " ").replace(".", " ")

tmp = s.split()

for i in tmp:
    print(i)


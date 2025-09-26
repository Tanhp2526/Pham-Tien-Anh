s = input()

if len(s) > 3:
    if(s[-3:] == "ing"):
        s += "ly"
    else:
        s += "ing"

print(s)
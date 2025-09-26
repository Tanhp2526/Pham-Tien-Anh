def check(string):
    words = []

    words = string.split()

    dict = {}

    for key in words:
        dict[key] = words.count(key)
    
    print(dict)

string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

check(string)
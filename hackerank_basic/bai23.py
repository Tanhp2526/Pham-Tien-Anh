import textwrap

def wrap(string, max_width):
    res = textwrap.fill(string,max_width)
    return res

string = input()
max_width = int(input())
result = wrap(string, max_width)
print(result)
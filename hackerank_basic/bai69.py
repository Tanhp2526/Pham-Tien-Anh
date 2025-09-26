def merge_the_tools(s, k):
    n = len(s)
    

    for i in range(0,n,k):
        con = s[i:i+k]
        res = ""
        for c in con:
            if c not in res:
                res += c
        print(res)

string, k = input(), int(input())
merge_the_tools(string, k)
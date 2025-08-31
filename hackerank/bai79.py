
t = int(input())

for i in range(t):
    s = input().strip()  

    
    cnt1 = 0
    cnt2 = 0
    for c in s:
        if c.isdigit():
            cnt1 += 1
        elif c.isupper():
            cnt2 += 1
    
    
    tmp = set(s)
    
    
    if ((len(s) == 10)  and (cnt2 >= 2) and (cnt1 >= 3) and (len(s) == len(tmp)) and (s.isalnum())):
        print("Valid")
    else:
        print("Invalid")
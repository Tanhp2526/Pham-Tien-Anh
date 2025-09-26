t = int(input())

for i in range(t):
    s = input()
    try:
        float(s)
        
        if s.count('.') == 1 and not s.endswith('.'):
            print(True) 
        else:
            print(False)
    except:
        print(False)
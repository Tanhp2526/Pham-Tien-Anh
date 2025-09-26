t = int(input())

for i in range(t):
    s = input()
    ok = True

   
    if s.count('.') != 1:
        ok = False

    
    elif s.endswith('.'):
        ok = False
    else:
       
        if s[0] in ['+','-','.']:
            num = s[1:]
        else:
            num = s

        
        if not num.replace('.', '').isdigit():
            ok = False

    if ok:
        print(True)
    else:
        print(False)

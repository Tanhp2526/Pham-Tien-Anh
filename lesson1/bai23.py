a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a :
    if a == b == c:
        print("Tam giac deu")
    elif a == b or b == c or a == c :
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("Invalid")
def minion_game(string):
    am = "UEOAI"
    Ke = 0
    St = 0
    n = len(string)
    for i in range(n):
        if string[i] in am:
            Ke += n - i
        else:
            St += n - i

    if Ke > St:
        print("Kevin", Ke)
    elif St > Ke:
        print("Stuart", St)
    else:
        print("Draw")

s = input()
minion_game(s)
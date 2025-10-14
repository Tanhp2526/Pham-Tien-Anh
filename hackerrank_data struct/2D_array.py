def check(arr):
    max_sum = -63
    for i in range(4):
        for j in range(4):
            s = (arr[i][j] + arr[i][j+1] + arr[i][j+2]
                + arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            
            if s > max_sum:
               max_sum = s
   
    return max_sum

arr = []
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))

res = check(arr)
print(res)
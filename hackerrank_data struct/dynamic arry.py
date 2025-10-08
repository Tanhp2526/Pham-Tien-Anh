def dynamic(n, queries):
    arr = []
    for i in range(n):
        arr.append([])

    lastAnswer = 0

    answer = []

    for query in queries:
        type_q = query[0]
        x = query[1]
        y = query[2]
        idx = (x ^ lastAnswer) % n

        if type_q == 1:
            arr[idx].append(y)
        elif type_q == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answer.append(lastAnswer)
    
    return answer


n,q = list(map(int, input().split()))
queries = []
for i in range(q):
    queries.append(list(map(int, input().split())))

res = dynamic(n, queries)
print(*res, sep='\n')
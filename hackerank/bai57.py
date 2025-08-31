n = int(input())
student_markes = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_markes[name] = scores
query_name = input()

res = sum(student_markes[query_name]) / len(student_markes[query_name])

print("{:.2f}".format(res))
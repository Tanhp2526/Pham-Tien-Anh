from collections import deque

n = int(input())
dq = deque()
for i in range(n):
    cmd = input().split()
    if cmd[0] == "append":
        dq.append(int(cmd[1]))
    elif cmd[0] == "appendleft":
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == "pop":
        dq.pop()
    elif cmd[0] == "popleft":
        dq.popleft()

print(*dq)
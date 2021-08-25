from collections import deque
q = deque()

n = int(input())

for i in range(1, n+1):
    q.append(i)

cnt = 0
while len(q) > 1:
    if cnt % 2 == 0:
        q.popleft()
    else:
        q.append(q[0])
        q.popleft()
    cnt += 1


print(q[0])



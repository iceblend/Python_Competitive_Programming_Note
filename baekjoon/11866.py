from collections import deque

q = deque()
ans = []
n, k = map(int, input().split())
cnt = 1

for i in range(1, n+1):
    q.append(i)

while q:
    if cnt == k:
        ans.append(q[0])
        q.popleft()
        cnt = 1
    else:
        q.append(q[0])
        q.popleft()
        cnt += 1

print("<"+", ".join(map(str, ans))+">")

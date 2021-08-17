import sys
from collections import deque

n, m, s = map(int, input().split())
a = [[] for _ in range(n + 1)]


for _ in range(m):
    v1, v2 = map(int, input().split())
    a[v1].append(v2)
    a[v2].append(v1)

for i in range(n + 1):
    a[i].sort()


def dfs(curr):
    global check
    check[curr] = True
    print(curr, end=' ')

    for next in a[curr]:
        if check[next] == False:
            dfs(next)


def bfs(start):
    global check

    q = deque()
    q.append(start)
    check[start] = True

    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

check = [False] * (n + 1)
dfs(s)

print()

check = [False] * (n + 1)
bfs(s)
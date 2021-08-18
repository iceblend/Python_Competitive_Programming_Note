import sys
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(curr_y, curr_x):
    global adj
    global check

    if check[curr_y][curr_x] == 1:
        return False

    check[curr_y][curr_x] = 1

    for d in range(4):
        next_y = curr_y + dy[d]
        next_x = curr_x + dx[d]
        if 0 <= next_y < n and 0 <= next_x < m:
            if adj[next_y][next_x] == 1 and check[next_y][next_x] == 0:
                dfs(next_y, next_x)

    return True


adj = []
check = []
sys.setrecursionlimit(10000)

tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())

    adj = [[0] * m for _ in range(n + 1)]
    check = [[0] * m for _ in range(n + 1)]

    for i in range(k):
        x, y = map(int, input().split())
        adj[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if adj[i][j] == 1 and dfs(i, j):
                cnt += 1
    print(cnt)

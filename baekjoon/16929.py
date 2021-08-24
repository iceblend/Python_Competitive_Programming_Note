dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

n, m = map(int, input().split())
a = [input() for _ in range(n)]
dist = [[0] * m for _ in range(n)]
check = [[False] * m for _ in range(n)]


def dfs(y, x, color, cnt):
    if check[y][x]:
        if cnt - dist[y][x] >= 4:
            return True
        else:
            return False

    check[y][x] = True
    dist[y][x] = cnt

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < m:
            if a[ny][nx] == color:
                if dfs(ny, nx, color, cnt + 1):
                    return True
    return False


for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue

        dist = [[0] * m for _ in range(n)]
        ok = dfs(i, j, a[i][j], 0)
        if ok:
            print("Yes")
            exit()

print("No")

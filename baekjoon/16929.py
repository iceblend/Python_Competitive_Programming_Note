import sys
sys.setrecursionlimit(100000)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, M = map(int, input().split())
board = [input() for _ in range(N)]
check = [[0] * M for _ in range(N)]
res = False


def dfs(curr_y, curr_x, origin_y, origin_x, cnt):
    global res
    if res:
        return

    check[curr_y][curr_x] = 1

    for d in range(4):
        next_y = curr_y + dy[d]
        next_x = curr_x + dx[d]

        #if 0 <= next_y < N and 0 <= next_x < M:
        if next_y < 0 or N <= next_y or next_x < 0 or M <= next_x:
            continue

        if board[next_y][next_x] != board[origin_y][origin_x]:
            continue

        if next_y == origin_y and next_x == origin_x and cnt >= 4:
            res = True
            return

        if check[next_y][next_x] == 0:
            dfs(next_y, next_x, origin_y, origin_x, cnt + 1)
    return


for i in range(N):
    for j in range(M):
        check = [[0] * M for _ in range(N)]
        dfs(i, j, i, j, 0)

if res:
    print("Yes")
else:
    print("No")

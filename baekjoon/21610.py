#21610 상어 중학교
import copy

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

dy_d = [1, 1, -1, -1]
dx_d = [-1, 1, -1, 1]


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]     #격자 r행 c열에 있는 바구니
moves = [list(map(int, input().split())) for _ in range(M)]

# 비바라기 시전
clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
for move in moves:

    # 구름 이동 및 비 내림
    d, s = move[0] - 1, move[1]
    for c in clouds:
        c[0] = (c[0] + dy[d] * s + N) % N
        c[1] = (c[1] + dx[d] * s + N) % N
        A[c[0]][c[1]] += 1 # 해당 칸에 물양이 늘어남
    
    # 물복사버그 마법 시전
    for c in clouds:
        y, x = c[0], c[1]
        d_count = 0
        for i in range(4):
            ny = y + dy_d[i]
            nx = x + dx_d[i]
            if 0 <= ny < N and 0 <= nx < N:
                if A[ny][nx] > 0:
                    d_count += 1
        A[y][x] += d_count

    # 새구름 생성
    clouds_board = [[0] * N for _ in range(N)]
    for c in clouds:
        clouds_board[c[0]][c[1]] = 1

    newClouds = []
    for y in range(N):
        for x in range(N):
            if A[y][x] >= 2:
                if clouds_board[y][x] == 0:
                    A[y][x] -= 2
                    newClouds.append([y, x])
    clouds = newClouds

total = 0
for y in range(N):
    for x in range(N):
        total += A[y][x]

print(total)

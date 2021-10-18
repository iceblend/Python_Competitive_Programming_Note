# 21609 상어 중학교

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


# 검은색 블록 : -1, 무지개 블록 : 0, delete : -2
def dfs(y, x, check, color):
    global board

    if check[y][x] == 1:
        return [0, 0]

    if board[y][x] <= -1:
        return [0, 0]

    if board[y][x] != color and board[y][x] != 0:
        return [0, 0]

    check[y][x] = 1
    block_total = 1
    block_rainbow = 0
    if board[y][x] == 0:
        block_rainbow = 1

    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N:
            c_t, c_r = dfs(ny, nx, check, color)
            block_total += c_t
            block_rainbow += c_r

    return [block_total, block_rainbow]


def deleteBlock(y, x, check, color):
    global board

    if check[y][x] == 1:
        return 0

    if board[y][x] == -2:
        return 0

    if board[y][x] != color and board[y][x] != 0:
        return 0

    check[y][x] = 1
    board[y][x] = -2

    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N:
            deleteBlock(ny, nx, check, color)


def gravity(x):
    global board

    idx = N-2
    while idx >= 0:
        # 맨 아래칸이면 걍 올림
        if idx == N-1:
            idx -= 1

        # 해당 칸이 음직이는 블럭이고 아래 칸이 공기일때
        if board[idx][x] >= 0 and board[idx + 1][x] == -2:
            # 스왑
            board[idx][x], board[idx + 1][x] = board[idx + 1][x], board[idx][x]
            idx += 1
            continue
        
        # 아무일 없을 때
        idx -= 1


totalScore = 0
while True:
    max_v = -1
    max_r = -1
    max_pos = []
    max_color = -2

    for y in range(N):
        for x in range(N):
            if board[y][x] <= 0:
                continue

            check = [[0] * N for _ in range(N)]
            s, r = dfs(y, x, check, board[y][x])

            if s > max_v:
                max_v = s
                max_r = r
                max_pos = [y, x]
                max_color = board[y][x]
            elif s == max_v and r >= max_r:
                max_v = s
                max_r = r
                max_pos = [y, x]
                max_color = board[y][x]

    if max_v < 2:
        break

    check = [[0] * N for _ in range(N)]
    deleteBlock(max_pos[0], max_pos[1], check, max_color)
    totalScore += max_v * max_v

    # 중력 작용
    for x in range(N):
        gravity(x)

    # 90도 반시계 방향 회전
    newBoard = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            newBoard[y][x] = board[x][N - 1 - y]
    board = newBoard

    # 다시 중력 작용
    for x in range(N):
        gravity(x)

print(totalScore)

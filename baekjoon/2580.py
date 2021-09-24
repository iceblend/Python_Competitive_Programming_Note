#2580 스도쿠

# 3x3 체크
def check(x, y, v):
    global board

    sx = x // 3 * 3
    sy = y // 3 * 3
    for i in range(sy, sy+3):
        for j in range(sx, sx+3):
            if v == board[i][j]:
                return False

    for j in range(0, 9):
        if v == board[y][j]:
            return False

    for i in range(0, 9):
        if v == board[i][x]:
            return False

    return True


def search(cnt):
    global board
    global arr_zero

    # endpoint
    if cnt == len(arr_zero):
        for ty in range(9):
            for tx in range(9):
                print(board[ty][tx], end=' ')
            print()
        exit()

    y = arr_zero[cnt][0]
    x = arr_zero[cnt][1]

    for i in range(1, 10):
        if check(x, y, i):
            board[y][x] = i
            search(cnt + 1)
            board[y][x] = 0

arr_zero = []
board = [[] for _ in range(9)]
for i in range(9):
    board[i] = list(map(int, input().split()))
    for j in range(9):
        if board[i][j] == 0:
            arr_zero.append([i, j])

search(0)

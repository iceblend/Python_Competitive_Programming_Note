# 1018 체스판 다시 칠하기

def checkBoard(sy, sx, ey, ex, board):
    start_w = 0
    start_b = 0

    for i in range(sy, ey):
        for j in range(sx, ex):
            curr = board[i][j]

            # 좌상단이 W일 때
            if curr == 'W':  # 현재가 W이면서
                if (i + j) % 2 != 0:  # 좌상단하고 맞는 배수가 아닐 때
                    start_w += 1
            else:  # 현재가 B이면서
                if (i + j) % 2 == 0:  # 좌상단하고 맞는 배수가 일때
                    start_w += 1

            # 좌상단이 B일 때
            if curr == 'B':  # 현재가 B이면서
                if (i + j) % 2 != 0:  # 좌상단하고 맞는 배수가 아닐 때
                    start_b += 1
            else:  # 현재가 W이면서
                if (i + j) % 2 == 0:  # 좌상단하고 맞는 배수가 일때
                    start_b += 1

    return min(start_w, start_b)



n, m = map(int, input().split())
arr = ['' for _ in range(n)]

for i in range(n):
    arr[i] = list(input())

minV = int(1e9)
for i in range(n):
    for j in range(m):
        if i + 8 > n or j + 8 > m:
            continue
        minV = min(minV, checkBoard(i, j, i+8, j+8, arr))

print(minV)
            

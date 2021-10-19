#20057 마법사 상어와 토네이도
import math

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

tornado = [[[0, 0, 2, 0, 0],
           [0, 10, 7, 1, 0],
           [5, 0, 0, 0, 0],
           [0, 10, 7, 1, 0],
           [0, 0, 2, 0, 0]]
           ,
           [[0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0],
           [2, 7, 0, 7, 2],
           [0, 10, 0, 10, 0],
           [0, 0, 5, 0, 0]]
           ,
           [[0, 0, 2, 0, 0],
            [0, 1, 7, 10, 0],
            [0, 0, 0, 0, 5],
            [0, 1, 7, 10, 0],
            [0, 0, 2, 0, 0]]
           ,
           [[0, 0, 5, 0, 0],
            [0, 10, 0, 10, 0],
            [2, 7, 0, 7, 2],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0]]]

y, x = N//2, N//2

moveDirection = 0

moveGoal = 1
moveCount = 0
moveTwice = 0

totalScore = 0

while True:
    if y < 0 or N <= y or x < 0 or N <= x:
        break

    # 이동하기
    ny = y + dy[moveDirection]
    nx = x + dx[moveDirection]
    moveCount += 1

    # 모래 옮기기
    sand = A[ny][nx]
    A[ny][nx] = 0

    outSand = 0
    totalSand = 0
    for i in range(5):
        for j in range(5):
            cy = ny - 2 + i
            cx = nx - 2 + j

            if cy < 0 or N <= cy or cx < 0 or N <= cx:
                outSand += math.floor(sand * (tornado[moveDirection][i][j] / 100))
            else:
                makeSand = math.floor(sand * (tornado[moveDirection][i][j] / 100))
                A[cy][cx] += makeSand
                totalSand += makeSand

    # 마지막 알파자리 모래 옮기기
    ay = ny + dy[moveDirection]
    ax = nx + dx[moveDirection]

    if 0 <= ay < N and 0 <= ax < N:
        A[ay][ax] += sand - totalSand - outSand
    else:
        totalScore += sand - totalSand - outSand

    totalScore += outSand

    # 방향 전환 및 이동 양 증가
    y = ny
    x = nx
    if moveCount == moveGoal:
        moveCount = 0
        moveDirection = (moveDirection + 1) % 4
        moveTwice += 1
    if moveTwice == 2:
        moveTwice = 0
        moveGoal += 1

print(totalScore)

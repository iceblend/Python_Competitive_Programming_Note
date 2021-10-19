#20058 마법사 상어와 파이어스톰
import copy
import sys
sys.setrecursionlimit(100000)


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(pow(2, N))]
L = list(map(int, input().split()))

length = pow(2, N)
tmpA = [[0] * length for _ in range(length)]


def Rotate(sy, sx, offset):
    global A, tmpA

    for y in range(offset):
        for x in range(offset):
            tmpA[sy + x][sx + (offset - 1 - y)] = A[sy + y][sx + x]
    '''
    result[j][n - i - 1] = arr[i][j]; // 시계 방향
    result[n - j - 1][i] = arr[i][j]; // 반시계 방향
    result[n - i - 1][j] = arr[i][j]; // 상하반전
    result[i][n - j - 1] = arr[i][j]; // 좌우반전
    '''


for l in L:
    offset = pow(2, l)
    tmpA = [[0] * length for _ in range(length)]

    # 부위별로 회전 시키기
    for y in range(0, length, offset):
        for x in range(0, length, offset):
            Rotate(y, x, offset)

    # 회전 시키고 인접칸 확인
    A = copy.deepcopy(tmpA)

    for y in range(length):
        for x in range(length):
            if tmpA[y][x] <= 0:
                continue

            iceCount = 0
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < length and 0 <= nx < length:
                    if tmpA[ny][nx] > 0:
                        iceCount += 1

            if iceCount < 3:
                A[y][x] -= 1


def dfs(y, x):
    global A, check

    check[y][x] = 1
    res = 1

    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if (0 <= ny < length and 0 <= nx < length) and (check[ny][nx] == 0) and (A[ny][nx] > 0):
            res += dfs(ny, nx)

    return res


check = [[0] * length for _ in range(length)]
totalIce = 0
maxIce = 0

for y in range(length):
    for x in range(pow(2, N)):
        totalIce += A[y][x]
        if A[y][x] > 0 and check[y][x] == 0:
            maxIce = max(maxIce, dfs(y, x))

print(totalIce)
print(maxIce)

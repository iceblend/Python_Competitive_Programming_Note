ans = [[0] * 81*81 for _ in range(81*81)]
n = int(input())


def go(sy, sx, v):
    if v == 1:
        ans[sy][sx] = 1
        return

    nv = v // 3
    cnt = 1
    for ny in range(sy, sy + v, nv):
        for nx in range(sx, sx + v, nv):
            if cnt != 5:
                go(ny, nx, nv)
            cnt += 1


go(0, 0, n)
for i in range(n):
    for j in range(n):
        if ans[i][j] == 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()

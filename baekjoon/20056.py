from copy import deepcopy

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    if m != 0:
        board[r - 1][c - 1].append([m, s, d])

dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(K):
    n_board = [[[] for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동시킴
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                for b in range(len(board[y][x])):
                    nm, ns, nd = board[y][x][b]
                    ny, nx = y + dirs[nd][0] * ns, x + dirs[nd][1] * ns
                    nx = (nx + N) % N
                    ny = (ny + N) % N
                    n_board[ny][nx].append([nm, ns, nd])

    # 파이어볼 2개이상 있는칸 찾아서 4개의 파이어볼을 만듬
    for y in range(N):
        for x in range(N):
            if len(n_board[y][x]) > 1:
                cm, cs, cd = 0, 0, []
                cnt = len(n_board[y][x])
                for c in range(cnt):
                    cm += n_board[y][x][c][0]
                    cs += n_board[y][x][c][1]
                    cd.append(n_board[y][x][c][2] % 2)
                cm //= 5
                cs //= cnt
                n_board[y][x] = []
                if cm != 0:
                    if sum(cd) == 0 or sum(cd) == cnt:
                        for i in range(4):
                            n_board[y][x].append([cm, cs, i * 2])
                    else:
                        for i in range(4):
                            n_board[y][x].append([cm, cs, i * 2 + 1])
    board = deepcopy(n_board)


sum_m = 0
for y in range(N):
    for x in range(N):
        if board[y][x]:
            for b in range(len(board[y][x])):
                sum_m += board[y][x][b][0]
print(sum_m)
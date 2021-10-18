dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N = int(input())
students = [list(map(int, input().split())) for _ in range(N*N)]
board = [[0] * N for _ in range(N)]


for s in students:
    curr_s = s[0]
    curr_f = s[1:5]

    cnt_max_f = -1
    cnt_max_empty = -1
    pos = [0, 0]

    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                continue

            c_empty = 0
            c_f = 0

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] == 0:
                        c_empty += 1
                    if board[ny][nx] in curr_f:
                        c_f += 1

            if c_f > cnt_max_f:
                cnt_max_f = c_f
                cnt_max_empty = c_empty
                pos = [y, x]

            elif c_f == cnt_max_f:
                if c_empty > cnt_max_empty:
                    cnt_max_empty = c_empty
                    pos = [y, x]

    board[pos[0]][pos[1]] = curr_s

students.sort()

total = 0
for y in range(N):
    for x in range(N):
        f_cnt = 0
        c_f = students[board[y][x] - 1][1:5]

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] in c_f:
                    f_cnt += 1

        if f_cnt == 1:
            total += 1
        if f_cnt == 2:
            total += 10
        if f_cnt == 3:
            total += 100
        if f_cnt == 4:
            total += 1000

print(total)

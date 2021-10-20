# 21611 마법사 상어와 블리자드

dy_magic = [-1, 1, 0, 0]
dx_magic = [0, 0, -1, 1]

dy_board = [0, 1, 0, -1]
dx_board = [-1, 0, 1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]
res = 0


def fillBoard():
    global board, N
    isFilled = False

    cy, cx = N // 2, N // 2

    move_goal = 1
    move_count = 0
    move_direction = 0
    move_twice = 0
    while 0 <= cy < N and 0 <= cx < N:

        # 해당 칸이 비어있으면 값을 땡겨와야함, 맨처음 재낌
        if board[cy][cx] == 0 and not (cy == N // 2 and cx == N // 2):
            # 다음 구슬을 찾음
            t_move_g = move_goal
            t_move_c = move_count
            t_move_d = move_direction
            t_move_t = move_twice
            ty, tx = cy, cx
            while 0 <= ty < N and 0 <= tx < N:
                if board[ty][tx] != 0:
                    break

                # 이동
                if t_move_c == t_move_g:
                    t_move_c = 0
                    t_move_t += 1
                    t_move_d = (t_move_d + 1) % 4
                if t_move_t == 2:
                    t_move_t = 0
                    t_move_g += 1
                ty, tx = ty + dy_board[t_move_d], tx + dx_board[t_move_d]
                t_move_c += 1

            # 만약에 다음 구슬이 아예 존재하지 않는다면, 바로 리턴으로 함수 종료
            if not (0 <= ty < N and 0 <= tx < N):
                return isFilled

            # 다음 구슬이 존재한다면, 그쪽 구슬을 땡겨옴
            board[cy][cx] = board[ty][tx]
            board[ty][tx] = 0
            isFilled = True

        # 이동
        if move_count == move_goal:
            move_count = 0
            move_twice += 1
            move_direction = (move_direction + 1) % 4
        if move_twice == 2:
            move_twice = 0
            move_goal += 1
        cy, cx = cy + dy_board[move_direction], cx + dx_board[move_direction]
        move_count += 1

    return isFilled


def Explose():
    global board, N, res
    isFiled = False

    cy, cx = N // 2, N // 2

    move_goal = 1
    move_count = 0
    move_direction = 0
    move_twice = 0
    while 0 <= cy < N and 0 <= cx < N:
        c_ball = board[cy][cx]
        save_pos = []

        if board[cy][cx] > 0:
            # 다음 구슬을 찾음
            t_move_g = move_goal
            t_move_c = move_count
            t_move_d = move_direction
            t_move_t = move_twice
            ty, tx = cy, cx
            while 0 <= ty < N and 0 <= tx < N:
                if board[ty][tx] == 0:
                    break
                if board[ty][tx] != c_ball:
                    break

                save_pos.append([ty, tx])

                # 이동
                if t_move_c == t_move_g:
                    t_move_c = 0
                    t_move_t += 1
                    t_move_d = (t_move_d + 1) % 4
                if t_move_t == 2:
                    t_move_t = 0
                    t_move_g += 1
                ty, tx = ty + dy_board[t_move_d], tx + dx_board[t_move_d]
                t_move_c += 1

            # 만약에 다음 구슬이 아예 존재하지 않는다면, 바로 리턴으로 함수 종료
            if not (0 <= ty < N and 0 <= tx < N):
                return

            # save_pos가 4이상일 경우 전부 삭제
            if len(save_pos) >= 4:

                # 점수 올리기
                if c_ball == 1:
                    res += len(save_pos)
                elif c_ball == 2:
                    res += len(save_pos) * 2
                elif c_ball == 3:
                    res += len(save_pos) * 3

                for pos in save_pos:
                    board[pos[0]][pos[1]] = 0

        # 이동
        if move_count == move_goal:
            move_count = 0
            move_twice += 1
            move_direction = (move_direction + 1) % 4
        if move_twice == 2:
            move_twice = 0
            move_goal += 1
        cy, cx = cy + dy_board[move_direction], cx + dx_board[move_direction]
        move_count += 1


def fillBoard2():
    global board, N

    cy, cx = N // 2, N // 2

    move_goal = 1
    move_count = 0
    move_direction = 0
    move_twice = 0

    save_info = []
    c_ball_cnt = 0
    c_ball_color = 0
    while 0 <= cy < N and 0 <= cx < N:
        # info를 계속 저장
        if board[cy][cx] != c_ball_color:
            if c_ball_color > 0:
                save_info.append([c_ball_cnt, c_ball_color])
            c_ball_cnt = 1
            c_ball_color = board[cy][cx]
        else:
            c_ball_cnt += 1

        # 이동
        if move_count == move_goal:
            move_count = 0
            move_twice += 1
            move_direction = (move_direction + 1) % 4
        if move_twice == 2:
            move_twice = 0
            move_goal += 1
        cy, cx = cy + dy_board[move_direction], cx + dx_board[move_direction]
        move_count += 1

    # 재 입력
    board = [[0] * N for _ in range(N)]

    cy, cx = N // 2, N // 2
    move_total_count = 0
    move_goal = 1
    move_count = 0
    move_direction = 0
    move_twice = 0

    while 0 <= cy < N and 0 <= cx < N:
        if not (cy == N // 2 and cx == N // 2):
            if len(save_info) > move_total_count // 2:
                board[cy][cx] = save_info[move_total_count // 2][move_total_count % 2]
                move_total_count += 1

        # 이동
        if move_count == move_goal:
            move_count = 0
            move_twice += 1
            move_direction = (move_direction + 1) % 4
        if move_twice == 2:
            move_twice = 0
            move_goal += 1
        cy, cx = cy + dy_board[move_direction], cx + dx_board[move_direction]
        move_count += 1


for magic in magics:

    # 마법 사용 - 지우기
    cy, cx = N // 2, N // 2
    d, s = magic[0] - 1, magic[1]
    for i in range(s):
        cy += dy_magic[d]
        cx += dx_magic[d]
        board[cy][cx] = 0

    # 채우기
    fillBoard()

    # 폭발 & 채우기 반복
    Explose()

    # 구슬 변화
    isFilled = fillBoard()
    while isFilled:
        Explose()
        isFilled = fillBoard()

    # 하나의 그룹 - 2개의 구슬 A와 B로 변한다.
    fillBoard2()

print(res)

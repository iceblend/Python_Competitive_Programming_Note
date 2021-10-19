#21611 마법사 상어와 블리자드

dy_magic = [-1, 1, 0, 0]
dx_magic = [0, 0, -1, 1]

dy_board = [0, 1, 0, -1]
dx_board = [-1, 0, 1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]


def fillBoard():
    global board, N
    isFiled = False

    cy, cx = N // 2, N // 2

    move_goal = 1
    move_count = 0
    move_direction = 0
    move_twice = 0
    while 0 <= cy < N and 0 <= cx < N:

        # 해당 칸이 비어있으면 값을 땡겨와야함, 맨처음 재낌
        if board[cy][cx] == 0 and not (cy == N//2 and cx == N//2):
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
                return
            
            # 다음 구슬이 존재한다면, 그쪽 구슬을 땡겨옴
            board[cy][cx] = board[ty][tx]
            board[ty][tx] = 0
            isFiled = True
            
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

    return isFiled


def fillBoard():
    global board, N
    isFiled = False

    cy, cx = N // 2, N // 2

    move_goal = 1
    move_count = 0
    move_direction = 0
    move_twice = 0


    c_ball_color = -1
    c_ball_cnt = 0
    while 0 <= cy < N and 0 <= cx < N:
        # 현재 위치
            
        # 여기 구현해야함
        if board[cy][cx] != c_ball_color:
        


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

    return isFiled


def Explose():
    global board, N
    isFiled = False

    cy, cx = N // 2, N // 2

    move_goal = 1
    move_count = 0
    move_direction = 0
    move_twice = 0
    while 0 <= cy < N and 0 <= cx < N:
        c_ball = board[cy][cx]
        save_pos = []




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
    while fillBoard():
        Explose()

    # 하나의 그룹 - 2개의 구슬 A와 B로 변한다.
    a = 0
    # 구슬 A의 번호 : 그룹에 들어있는 구슬의 개수
    # 구슬 B의 번호 : 그룹을 이루고 있는 구슬의 번호
    # 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어간다.

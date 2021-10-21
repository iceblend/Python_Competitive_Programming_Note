#19237 어른 상어
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M, k = map(int, input().split())

# 상어가 위치한 보드 입력
board = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):  # 1씩 다 빼기
    for x in range(N):
        board[y][x] -= 1

# 상어의 현재 방향
curr_shark_d = list(map(int, input().split()))
for d in curr_shark_d:  # 1씩 다 빼기
    d -= 1

# 상어의 방향 예약입력
shark_d = [] * M
for i in range(M):
    shark_d[i] = [list(map(int, input().split())) for _ in range(4)]
    for s in shark_d[i]: # 1씩 다 빼기
        for sd in s:
            sd -= 1

# 향기
decent = [[[]] * N for _ in range(N)]

def do_decent():
    global board, decent, k
    for y in range(N):
        for x in range(N):
            if board[y][x] != -1:
                decent[y][x] = [board[y][x], k]



# 번호1 제일 강려크, 쫓아내기 가능
# NxN M개의 칸 상어 한마리씩
while True:
    # 1. 모든 상어가 자기 위치에 냄새를 뿌림
    do_decent()

    # 2. 동시에 상하좌우 인접칸 중 하나로 이동
    # 아무냄새 없는 칸 > 자신의 냄새 있는 칸
    # 한칸에 여러마리 상어가 있을경우 가장 작은번호를 가진 상어만 남음
    newBoard = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if board[y][x] != -1:
                cs_idx = board[y][x]
                cs_d = curr_shark_d[cs_idx]

                nobody = -1
                myDesent = -1
                for d in shark_d[cs_idx][cs_d]:
                    ny = y + dy[d]
                    nx = x + dx[d]






    # 3. 자신의 냄새를 그 칸에 뿌림
    do_decent()

    # 4. 냄새는 상어가 k번 이동하면 사라짐


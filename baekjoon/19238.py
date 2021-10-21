# 19238 스타트 택시
from collections import deque
import heapq

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N, M, F = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

taxiPos = list(map(int, input().split()))
guestPos = [list(map(int, input().split())) for _ in range(M)]


# 모든 손님에 대해 일일히 bfs 돌리지 말고 한번에 bfs 돌려서 계산해라
def findGuest(sy, sx):
    global N, A, guestPos
    check = [[0] * N for _ in range(N)]
    board = [[-1] * N for _ in range(N)]

    q = deque()
    q.append([sy, sx])
    check[sy][sx] = 1
    board[sy][sx] = 0

    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]
            if 0 <= ny < N and 0 <= nx < N and A[ny][nx] != 1 and check[ny][nx] == 0:
                check[ny][nx] = 1
                board[ny][nx] = board[cy][cx] + 1
                q.append([ny, nx])

    shortest_guest_idx = -1
    shortest_guest_length = int(1e9)
    for i in range(len(guestPos)):
        gy, gx = guestPos[i][0] - 1, guestPos[i][1] - 1
        length = board[gy][gx]
        if length == -1:
            print(-1)
            exit(0)
        if length < shortest_guest_length:
            shortest_guest_idx = i
            shortest_guest_length = length
    return [shortest_guest_idx, shortest_guest_length]



def bfs(sy, sx, ey, ex):
    global N, A
    check = [[0] * N for _ in range(N)]
    board = [[-1] * N for _ in range(N)]

    q = deque()
    q.append([sy, sx])
    check[sy][sx] = 1
    board[sy][sx] = 0

    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]
            if 0 <= ny < N and 0 <= nx < N and A[ny][nx] != 1 and check[ny][nx] == 0:
                check[ny][nx] = 1
                board[ny][nx] = board[cy][cx] + 1
                q.append([ny, nx])
                if ny == ey and nx == ex:
                    return board[ey][ex]

    return board[ey][ex]


while True:
    # findShortestPath_guest
    # 미리 y,x 순으로 정렬해서 최소값 찾기 쉽게
    guestPos.sort(key=lambda x: (x[0], x[1]))
    shortest_guest_idx, shortest_guest_length = findGuest(taxiPos[0] - 1, taxiPos[1] - 1)

    # 손님이 있는 곳까지 이동
    F -= shortest_guest_length
    taxiPos = [guestPos[shortest_guest_idx][0], guestPos[shortest_guest_idx][1]]
    if F <= 0:   # 연료 다 떨어지면 그자리에서 종료
        print(-1)
        exit(0)

    # 손님을 목적지 까지 전달
    length = bfs(taxiPos[0] - 1, taxiPos[1] - 1, guestPos[shortest_guest_idx][2] - 1, guestPos[shortest_guest_idx][3] - 1)
    if length == -1:
        print(-1)
        exit(0)
    F -= length
    taxiPos = [guestPos[shortest_guest_idx][2], guestPos[shortest_guest_idx][3]]
    if F < 0:   # 연료 다 떨어지면 그자리에서 종료
        print(-1)
        exit(0)

    # 도착했으니 연료 채워짐
    F += length * 2

    del guestPos[shortest_guest_idx]
    if len(guestPos) == 0:
        break

print(F)

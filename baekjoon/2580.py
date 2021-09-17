#2580 스도쿠

def check(x, y, v):
    global board

    sx = x // 3
    sy = y // 3

    for i in range(y, y+3):
        for j in range(x, x+3):




def search(arr, n):
    global board

    if len(arr) == n:
        return arr

    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:

                # 체크하기
                isIn = False
                for a in arr:
                    ax, ay, av = a[0], a[1], a[2]
                    if ax == x and ay == y:
                        isIn = True

                # 만약 arr 안에 없다면
                if isIn == False:
                    # 0 자리에 값을 이것저것 넣어서 체크 해보고 백트래킹 함
                    for i in range(1, 10):
                    





countZero = 0
board = [[] for _ in range(9)]
for i in range(9):
    board[i] = list(map(int, input().split()))
    countZero += board[i].count(0)












tc = int(input())

board = [0] * 101
board[1] = 1
board[2] = 1
board[3] = 1
board[4] = 2

for i in range(5, 101):
    board[i] = board[i-1] + board[i-5]

for _ in range(tc):
    n = int(input())
    print(board[n])


#1904 01타일

n = int(input())

board = [0] * 1000002

board[1] = 1
board[2] = 2

for i in range(3, 1000002):
    board[i] = (board[i-1] + board[i-2]) % 15746

print(board[n])

#2579 계단 오르기

board = [0] * 301
dp = [0] * 301
n = int(input())
for i in range(n):
    board[i + 1] = int(input())

for i in range(1, 301):
    dp[i] = max(board[i-1] + dp[i-3], dp[i-2]) + board[i]

print(dp[n])

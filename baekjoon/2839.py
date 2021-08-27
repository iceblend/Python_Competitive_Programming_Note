# 설탕 배달
n = int(input())

ans = int(1e9)

bong5 = 0

while bong5 * 5 <= n:
    bong5_left = n - bong5 * 5
    bong3 = bong5_left // 3
    bong3_left = bong5_left % 3

    if bong3_left == 0:
        ans = min(ans, bong5 + bong3)
    bong5 += 1

if ans == int(1e9):
    print(-1)
else:
    print(ans)

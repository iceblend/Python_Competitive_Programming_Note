#네 번째 점
x = y = 0
for _ in range(3):
    n1, n2 = map(int, input().split())
    x ^= n1
    y ^= n2
print(x, y)

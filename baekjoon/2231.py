def makeNum(x):
    total = x
    while x != 0:
        total += (x % 10)
        x = x // 10
    return total


n = int(input())

for i in range(1, n):
    if makeNum(i) == n:
        print(i)
        exit(0)

print(0)

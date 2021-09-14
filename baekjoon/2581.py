def isPrime(x):
    if x < 2:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

m = int(input())
n = int(input())

total_v = 0
total_min = int(1e9)
for i in range(m, n+1):
    if isPrime(i):
        total_min = min(i, total_min)
        total_v += i

if total_v == 0:
    print(-1)
else:
    print(total_v)
    print(total_min)

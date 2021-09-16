n, m = map(int, input().split())
arr = list(map(int, input().split()))

maxV = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            v = arr[i] + arr[j] + arr[k]
            if v <= m and v > maxV:
                maxV = v

print(maxV)

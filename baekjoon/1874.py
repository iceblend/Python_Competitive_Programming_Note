from collections import deque
s = deque()
res = []
cnt = 0

n = int(input())

for i in range(n):
    v = int(input())

    while cnt < v:
        cnt += 1
        s.append(cnt)
        res.append("+")

    if s[-1] == v:
        s.pop()
        res.append("-")
    else:
        print("NO")
        exit()

print("\n".join(res))

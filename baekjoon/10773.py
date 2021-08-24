from collections import deque
k = int(input())
s = deque()

for _ in range(k):
    n = int(input())

    if n == 0:
        s.pop()
    else:
        s.append(n)

print(sum(s))
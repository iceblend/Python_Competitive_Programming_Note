import sys
from collections import deque

q = deque()

n = int(input())

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if s.count(" ") > 0:
        _, v = s.split()
        q.append(int(v))

    else:
        if s == "pop":
            if q:
                print(q[0])
                q.popleft()
            else:
                print(-1)
        if s == "size":
            print(len(q))
        if s == "empty":
            if len(q) > 0:
                print(0)
            else:
                print(1)
        if s == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        if s == "back":
            if q:
                print(q[-1])
            else:
                print(-1)

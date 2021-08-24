import sys
from collections import deque
tc = int(input())


def go(str):
    s = deque()

    for v in str:
        if v == "(":
            s.append(v)
        elif v == ")":
            if len(s) == 0:
                print("NO")
                return
            else:
                s.pop()

    if len(s) > 0:
        print("NO")
    else:
        print("YES")


for _ in range(tc):
    str = sys.stdin.readline().rstrip()
    go(str)
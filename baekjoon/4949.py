import sys
from collections import deque

op = ("(", "[", "{")
cl = (")", "]", "}")


def go(str_):
    s = deque()
    for v in str_:
        if v in op:
            s.append(v)
        if v in cl:
            if len(s) == 0:
                print("no")
                return
            if s[-1] != op[cl.index(v)]:
                print("no")
                return
            s.pop()

    if len(s) > 0:
        print("no")
    else:
        print("yes")


while True:
    str = sys.stdin.readline().rstrip()
    if str == ".":
        break
    go(str)

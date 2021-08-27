import sys
sys.setrecursionlimit(100000)

def fibo(v):
    if v == 0:
        return 0
    if v == 1:
        return 1

    return fibo(v-1) + fibo(v-2)

n = int(input())
print(fibo(n))
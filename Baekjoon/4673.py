import sys

def d(n):
    num = n
    for s in str(n):
        num += int(s)
    return num

check = [0] * 10001

for i in range(1, 10001):
    num = d(i)
    while num <= 10000:
        check[num] += 1
        num = d(num)

for i in range(1, 10001):
    if check[i] == 0:
        sys.stdout.write(str(i) + '\n')
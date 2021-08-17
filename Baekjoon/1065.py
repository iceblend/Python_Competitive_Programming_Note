def check(n):
    if len(str(n)) <= 2:
        return True
    elif len(str(n)) == 3:
        v1 = int(str(n)[0]) - int(str(n)[1])
        v2 = int(str(n)[1]) - int(str(n)[2])
        if v1 == v2:
            return True
        else:
            return False
    else:
        v1 = int(str(n)[0]) - int(str(n)[1])
        v2 = int(str(n)[1]) - int(str(n)[2])
        v3 = int(str(n)[1]) - int(str(n)[2])
        if v1 == v2 and v2 == v3:
            return True
        else:
            return False


n = int(input())
cnt = 0
for i in range(1, n + 1):
    if check(i):
        cnt += 1
print(cnt)

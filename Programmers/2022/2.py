import math


def is_prime_number(x):
    if x == 0 or x == 1:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def transfer(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n, k):
    s = str(transfer(n, k))

    result = []

    sIdx = 0
    while sIdx < len(s):
        if s[sIdx] == '0':
            sIdx += 1
            continue

        jIdx = sIdx
        while jIdx < len(s) and s[jIdx] != '0':
            jIdx += 1
            continue

        primeGo = False
        tmp = s[sIdx:jIdx]
        # 조건 1
        if 0 < sIdx and s[sIdx-1] == '0' and jIdx < len(s)-1 and s[jIdx] == '0':
            primeGo = True
        # 조건 2
        if sIdx == 0 and jIdx < len(s) and s[jIdx] == '0':
            primeGo = True
        # 조건 3
        if jIdx == len(s) and 0 < sIdx and s[sIdx-1] == '0':
            primeGo = True
        # 조건 4
        if sIdx == 0 and jIdx == len(s):
            primeGo = True

        if primeGo:
            if is_prime_number(int(tmp)):
                if '0' not in str(tmp):
                    result.append(int(tmp))

        sIdx = jIdx


    answer = len(result)
    return answer

print(solution(11, 10))

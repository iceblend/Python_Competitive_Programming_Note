#골드바흐의 추측

MAX = 10000
check = [True] * (MAX + 1)
check[0] = check[1] = False

#에라토스테네스의 체
for i in range(2, MAX + 1):
    if check[i]:
        j = 2 * i
        while j <= MAX:
            check[j] = False
            j += i

T = int(input())
for _ in range(T):
    n = int(input())

    ans = 987654321
    ans_x1 = 0
    ans_x2 = 0

    for i in range(2, n//2 + 1):
        if check[i] and check[n-i]:
            if n-i-i < ans:
                ans = n-i-i
                ans_x1 = i
                ans_x2 = n-i

    print(ans_x1, ans_x2)

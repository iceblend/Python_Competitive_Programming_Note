#베르트랑 공준
def isPrime(n):
    if n < 2:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


while True:
    n = int(input())
    if n == 0:
        break;

    count = 0
    for i in range(n + 1, 2*n + 1):
        if isPrime(i):
            count += 1
    print(count)

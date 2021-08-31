#n개의 원판을 start에서 mid를 거쳐 end까지 옮김
def hanoi(n, start, mid, end):
    if n == 1:
        print(f"{start} {end}")
        return

    hanoi(n - 1, start, end, mid)   # 첫번째 부터 n-1개까지 end를 거쳐 mid로 옮김
    hanoi(1, start, mid, end) #맨 밑바닥 한개를 mid를 거쳐 end로 옮김
    hanoi(n - 1, mid, start, end) # mid에 있는것들을 start를 거쳐 end로 옮김


n = int(input())
print(2**n - 1) # 하노이 이동 횟수 공식
hanoi(n, 1, 2, 3)

# ACM 호텔
tc = int(input())
for _ in range(tc):
    h, w, n = map(int, input().split())

    floor = n % h
    step = n // h + 1

    if floor == 0:
        floor = h
        step -= 1
    print(floor, end='')
    if step < 10:
        print(f"0{step}")
    else:
        print(step)

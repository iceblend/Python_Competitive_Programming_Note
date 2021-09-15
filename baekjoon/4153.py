#직각삼각형

while True:
    v = list(map(int, input().split()))
    if v.count(0) == 3:
        break

    v.sort()
    if v[0]*v[0] + v[1]*v[1] == v[2]*v[2]:
        print("right")
    else:
        print("wrong")
        
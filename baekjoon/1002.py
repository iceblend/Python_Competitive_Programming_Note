#터렛
import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2) #두 원의 거리

    #중심 거리와 두 원의 위치관계식을 이용해 접점 개수를 알아냄
    if dist == 0 and r1 == r2: #동심원, 반지름 같음
        print(-1)
    elif abs(r1-r2) == dist or r1+r2 == dist: #내접, 외접
        print(1)
    elif abs(r1-r2) < dist < (r1+r2): #다른 두 점에서 만날 때
        print(2)
    else:
        print(0) # 그 외

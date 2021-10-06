from collections import deque

N, K = map(int, input().split())
arr = deque(list(map(int, input().split())))

ans = 1
robot = deque(list([0] * N))

while True:
    # 1. 회전
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 2. 한칸 이동
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            arr[i+1] -= 1
    robot[-1] = 0

    # 3. 로봇 하나 올리기
    if arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1

    if arr.count(0) >= K:
        print(ans)
        exit(0)
    ans += 1

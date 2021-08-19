# 11651 좌표 정렬하기 2
arr = []
n = int(input())

for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])

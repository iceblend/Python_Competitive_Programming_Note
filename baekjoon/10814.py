# 10814 나이순 정렬
arr = []
n = int(input())

for i in range(n):
    v = [i] + list(input().split())
    arr.append(v)

arr.sort(key=lambda x: (x[1], x[0]))

for i in range(len(arr)):
    print(arr[i][1], arr[i][2])

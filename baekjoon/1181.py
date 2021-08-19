# 1181 단어 정렬
arr = []
n = int(input())

for i in range(n):
    str = input()
    if str in arr:
        continue
    arr.append(str)

arr.sort(key=lambda x: (len(x), x))

for i in range(len(arr)):
    print(arr[i])

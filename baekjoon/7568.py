# 7568 덩치
n = int(input())
arr = []
grade_info = []

for _ in range(n):
    weight, height = map(int, input().split())
    arr.append([weight, height])


for i in range(n):
    grade = 1
    for j in range(n):
        if i == j:
            continue

        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            grade += 1

    grade_info.append(grade)

print(' '.join(map(str, grade_info)))

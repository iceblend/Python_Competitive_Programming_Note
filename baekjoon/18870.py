# 18870 좌표 압축
# 시간 초과

n = int(input())
arr = list(map(int, input().split()))

sort_arr = []
for a in arr:
    if a not in sort_arr:
        sort_arr.append(a);

sort_arr.sort()

for a in arr:
    idx = sort_arr.index(a);
    print(idx, end=' ')

# 18870 μ’ν μμΆ

n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))
dict_arr = {v : i for i, v in enumerate(sort_arr)}

for a in arr:
    print(dict_arr[a], end=' ')

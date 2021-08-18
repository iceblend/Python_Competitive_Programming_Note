str = input()
arr = []

for s in str:
    arr.append(int(s))

arr.sort(reverse=True)

for v in arr:
    print(v,end='')

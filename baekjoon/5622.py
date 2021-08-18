# 5622 다이얼
time = [
    [],
    [],
    [],
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
]

cnt = 0
str = input()

for s in str:
    for i in range(len(time)):
        if s in time[i]:
            cnt += i
            break
print(cnt)


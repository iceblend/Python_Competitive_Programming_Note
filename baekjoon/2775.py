#부녀회장이 될테야
tc = int(input())

arr = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    arr[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):

        man = 0
        for k in range(1, j + 1):
            man += arr[i-1][k]

        arr[i][j] = man

for _ in range(tc):
    k = int(input())
    n = int(input())
    print(arr[k][n])
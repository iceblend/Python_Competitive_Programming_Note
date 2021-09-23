#14888 연산자 끼워넣기

minv = int(1e10)
maxv = -int(1e10)

def do(idx, v, pl, mi, mu, di):
    global arr
    global minv
    global maxv

    if idx == len(arr):
        minv = min(v, minv)
        maxv = max(v, maxv)
        return

    if pl > 0:
        do(idx + 1, v + arr[idx], pl - 1, mi, mu, di)
    if mi > 0:
        do(idx + 1, v - arr[idx], pl, mi - 1, mu, di)
    if mu > 0:
        do(idx + 1, v * arr[idx], pl, mi, mu - 1, di)
    if di > 0:
        if v < 0:
            v = -(abs(v) // arr[idx])
        else:
            v = v // arr[idx]
        do(idx + 1, v, pl, mi, mu, di - 1)

    return

n = int(input())
arr = list(map(int, input().split()))
sa = list(map(int, input().split()))

do(1, arr[0], sa[0], sa[1], sa[2], sa[3])

print(maxv)
print(minv)
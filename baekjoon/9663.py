#9663 N-Queen

def search(arr, n):
    global count

    if len(arr) == n:
        count += 1
        return

    y = len(arr)
    for x in range(n):
        check = True
        for by, bx in enumerate(arr):
            # 같은 열에 있는 경우
            if x == bx:
                check = False
                break
            # 같은 좌상단에 있는 경우
            if y - x == by - bx:
                check = False
                break
            # 같은 우상단에 있는 경우
            if y + x == by + bx:
                check = False
                break

        if check:
            arr.append(x)
            search(arr, n)
            arr.pop(-1)


n = int(input())
count = 0

for i in range(n):
    search([i], n)

print(count)



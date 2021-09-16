#1436 영화감독 숌

n = int(input())

arr = [666]
for i in range(1, n+1):
    s = str(arr[i-1]).split('666')
    pos = (i // 10) % 2
    
    # 666 앞
    if pos == 0:
        if s[0] == '':
            s[0] = 0
        s[0] = str(int(s[0]) + 1)

    # 666 뒤
    else:
        if s[1] == '':
            s[1] = 0
        s[1] = str(int(s[1]) + 1)

    newV = s[0] + '666' + s[1]
    arr.append(newV)

print(arr[n-1])
    

# 2941 크로아티아 알파벳
calphas = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str = input()

cnt = 0
while len(str) > 0:
    is_calpha = False
    for calpha in calphas:
        if str.find(calpha) == 0:
            cnt += 1
            str = str[len(calpha):]
            is_calpha = True
            break

    if is_calpha == False:
        str = str[1:]
        cnt += 1

print(cnt)
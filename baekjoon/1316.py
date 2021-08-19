# 1316 그룹 단어 체커

cnt_group_word = 0
tc = int(input())

for _ in range(tc):
    str = input()

    is_group_word = True
    alpha_check = [0] * (ord('z') - ord('a') + 1)

    for i in range(len(str)):
        c = str[i]
        if alpha_check[ord(c) - ord('a')] == 0:
            alpha_check[ord(c) - ord('a')] = 1
            continue

        else:
            if str[i - 1] != c:
                is_group_word = False

    if is_group_word:
        cnt_group_word += 1

print(cnt_group_word)

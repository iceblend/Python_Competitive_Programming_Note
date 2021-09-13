from itertools import combinations_with_replacement


def calcScore(n, a, l):
    a_score = 0
    l_score = 0

    for i in range(11):
        if a[i] == 0 and l[i] == 0:
            continue
        elif a[i] < l[i]:
            l_score += (10 - i)
        else:
            a_score += (10 - i)

    if l_score > a_score:
        return l_score - a_score
    else:
        return -1


def solution(n, info):
    score = [0,1,2,3,4,5,6,7,8,9,10]

    lion_shoot_list = list(combinations_with_replacement(score, n))
    answer = []
    maxScore = -1

    for shoot in lion_shoot_list:
        lion_score_list = [0] * 11  # 스코어 담기
        for v in shoot:
            lion_score_list[v] += 1

        lion_score_list.reverse()   # 스코어 리버스
        score = calcScore(n, info, lion_score_list)
        if score != -1 and score > maxScore:
            answer = lion_score_list
            maxScore = score

    if maxScore < 0:
        answer = [-1]
    return answer


print(solution(3, [2,1,0,0,0,0,0,0,0,0,0]))

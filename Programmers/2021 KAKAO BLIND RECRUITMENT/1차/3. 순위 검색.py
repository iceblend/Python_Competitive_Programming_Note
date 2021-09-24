from itertools import combinations
from collections import defaultdict


def solution(infos, querys):
    answer = []
    info_dict = defaultdict(list)

    ''' dict 생성 '''
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])

        for i in range(5):
            for c in combinations(info_key, i):  # 하나의 Info에서 경우의 수 16개 만들기
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val) # 가능한 Info 조합을 key, 점수를 value에 주기

    ''' dict sort '''
    for key in info_dict.keys():
        info_dict[key].sort()


    ''' query 실행 '''
    for query in querys:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3): # and 제거
            query.remove('and')
        while '-' in query: # - 제거
            query.remove('-')
        tmp_query = ''.join(query)

        # lower Bound를 이용해 query_score 보다 큰 점수들 구하기
        if tmp_query in info_dict:
            scores = info_dict[tmp_query]

            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)

    return answer



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
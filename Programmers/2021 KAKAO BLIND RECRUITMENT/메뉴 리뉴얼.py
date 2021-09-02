from itertools import combinations # 조합 출력
from collections import Counter # 각 원소의 중복 갯수를 세어 줌


def solution(orders, course):
    answer = []
    for c in course: # course의 갯수 만큼 반복 (2개, 3개, 5개짜리 조합 찾기)
        temp = []
        for order in orders: # order에 대해 course 만큼 조합
            combi = combinations(sorted(order), c)  # 조합! ex) order:A,B,C,F,G / c:2 의 경우 AB,AC,AF...
            temp += combi
        counter = Counter(temp) # 조합된 주문에 대해 모든 주문내역 중 해당 조합의 갯수를 구함
        if len(counter) != 0 and max(counter.values()) != 1: # 주문 조합이 나온적이 없거나, 최대값이 1이면 패스
            # 아니면 최대값(현재 갯수에 해당하는 메뉴 조합 중 가장 많이 주문되었던것)을 가진 주문을 다 넣음
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

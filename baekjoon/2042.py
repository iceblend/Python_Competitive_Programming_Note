# 세그먼트 트리
# https://upcount.tistory.com/12

import sys

# 세그먼트 트리 생성
def init(node, start ,end):
    # node가 leaf node인 경우 배열의 원소 값 반환.
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    # 재귀 함수를 이용하여 왼쪽/오른쪽 자식 트리를 만들고 합을 저장.
    else:
        mid = (start + end) // 2
        tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
        return tree[node]
    
# 구간합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야하는 구간 [left, right]
def subNum(node, start, end, left, right):
    if end < left or right < start:
        return 0

    # 구해야 하는 합의 범위는 [left, right] 인데, [start, end]는 그 범위에 모두 포함되고
    # node 자식도 모두 포함되기 때문에 더 이상의 연산 호출은 비효율적임.
    if left <= start  and end <= right:
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야 한다.
    mid = (start + end) // 2
    return subNum(node*2, start ,mid, left, right) + subNum(node*2 + 1, mid+1, end, left, right)


def update(node, start, end, index, diff):

    if index < start or end < index:
        return

    tree[node] += diff

    # 리프노드가 아닌 경우 자식 노드도 값을 변경해야 함.
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
tree = [0] * 4000000

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        b = b-1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, n-1, b, diff)
    else:
        print(subNum(1, 0, n-1, b-1, c-1))


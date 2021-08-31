import sys


def init1(node, start, end):
    # node가 leaf node인 경우 배열의 원소 값 반환.
    if start == end:
        tree1[node] = arr[start]
        return tree1[node]
    # 재귀 함수를 이용하여 왼쪽/오른쪽 자식 트리를 만들고 합을 저장.
    else:
        mid = (start + end) // 2
        tree1[node] = min(init1(node * 2, start, mid), init1(node * 2 + 1, mid + 1, end))
        return tree1[node]

def init2(node, start, end):
    # node가 leaf node인 경우 배열의 원소 값 반환.
    if start == end:
        tree2[node] = arr[start]
        return tree2[node]
    # 재귀 함수를 이용하여 왼쪽/오른쪽 자식 트리를 만들고 합을 저장.
    else:
        mid = (start + end) // 2
        tree2[node] = max(init2(node * 2, start, mid), init2(node * 2 + 1, mid + 1, end))
        return tree2[node]


def minValue(node, start, end, left, right):
    if end < left or right < start:
        return 1000000001

    if left <= start and end <= right:
        return tree1[node]

    mid = (start + end) // 2
    return min(minValue(node * 2, start, mid, left, right), minValue(node * 2 + 1, mid + 1, end, left, right))

def maxValue(node, start, end, left, right):
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return tree2[node]

    mid = (start + end) // 2
    return max(maxValue(node * 2, start, mid, left, right), maxValue(node * 2 + 1, mid + 1, end, left, right))





tree1 = [0] * 4000000
tree2 = [0] * 4000000

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

init1(1, 0, n-1)
init2(1, 0, n-1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(minValue(1, 0, n - 1, a-1, b-1),end=' ')
    print(maxValue(1, 0, n - 1, a-1, b-1))
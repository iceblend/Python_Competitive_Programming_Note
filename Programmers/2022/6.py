N = 0
num_list = []
tree = [0]

def init(start, end, here):
    if start == end:
        tree[here] = num_list[start]
        return tree[here]

    mid = (start + end) // 2
    tree[here] = init(start, mid, here * 2) + init(mid + 1, end, here * 2 + 1)
    return tree[here]


def query(start, end, here, left, right):

    # 범위를 벗어나는 경우
    if left > end or right < start:
        return 0
    # 범위 내에 있는 경우
    if left <= start and end <= right:
        return tree[here]

    mid = (start + end) // 2
    # 현재 위치의 합 = 왼쪽 범위의 구간합 + 오른쪽 범위의 구간 합
    sub_sum = query(start, mid, here * 2, left, right) + query(mid + 1, end, here * 2 + 1, left, right)
    return sub_sum


def solution(board, skill):
    global N
    global num_list
    global tree

    height = len(board)
    width = len(board[0])
    N = height * width
    num_list = [0 for i in range(N)]  # 숫자를 담는 리스트
    tree = [0] * (N * 100)  # 세그먼트가 가장 많이 분할 되면 전체 노드의 4배 완전 이진 트리를 생각 하면된다.

    for i in range(height):
        for j in range(width):
            num_list[i * width + j] = board[i][j]

    init(0, N-1, 1)
    print(query(1, N + 1, 1, 1, N + 1))

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
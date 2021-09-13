from collections import deque

node = [-1] * 18
sheepList = [[] for _ in range(18)]
wolfList = [[] for _ in range(18)]
edge_child = [[] for _ in range(18)]
edge_parent = [[] for _ in range(18)]

maxSheep = 0

def search():
    q = deque()
    q.append([0, [0], []])

    while q:
        curr, sheep, wolf = q.popleft()
        parent = edge_parent[curr][0]

        # 늑대가 더 많으므로 현재 노드 접근 불가
        if len(wolf) >= len(sheep):
            continue

        # 부모로 위로 올림
        if sheep != sheepList[parent]:
            q.append([parent, sheep, wolf])
            continue
        if wolf != wolfList[parent]:
            q.append([parent, sheep, wolf])
            continue


        # 현재 노드가 양인데 sheep 리스트에 없으면 부모 리스트에 추가 후 다시 큐 실행
        if node[curr] == 0:
            if curr not in sheep:
                sheep.append(curr)
                q.append([parent, sheep, wolf])
                continue

        # 현재 노드가 늑대인데 sheep 리스트에 없으면 부모 리스트에 추가 후 다시 큐 실행
        if node[curr] == 1:
            if curr not in wolf:
                wolf.append(curr)
                q.append([parent, sheep, wolf])
                continue

        sheepList[parent] = sheep
        wolfList[parent] = wolf

        # 양과 늑대 정보 추가하고 다음 노드 탐색하기
        for next in edge_child[curr]:
            q.append([next, sheep, wolf])

    a = 0
        







def solution(info, edges):

    for i, v in enumerate(info):
        node[i] = v
    for e in edges:
        v1, v2 = e[0], e[1]
        edge_child[v1].append(v2)
        edge_parent[v2].append(v1)

    search()
    answer = 0
    return answer




print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
import heapq

INF = int(1e9)
graph = [[]]


def dijkstra(src, dst):
    global graph

    n = len(graph)
    table = [INF for i in range(n)]
    table[src] = 0
    pq = [[0, src]]

    while pq:
        w, curr = heapq.heappop(pq)

        if table[curr] < w:
            continue

        for item in graph[curr]:
            next, cost = item[0], item[1]
            cost += w
            if cost < table[next]:
                table[next] = cost
                heapq.heappush(pq, [cost, next])

    return table[dst]


def solution(n, s, a, b, fares):
    global graph
    graph = [[] for _ in range(n+1)]

    # 그래프 정리하기
    for fare in fares:
        src, dst, cost = fare[0], fare[1], fare[2]
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])


    # a,b가 i까지 같이 갔다가 i부터 각자의 길로 흩어졌을 때의 모든 경우의 수를 최단경로를 다익스트라로 구한 후
    # 그중 가장 최소값을 저장하여 return 한다.
    cost = INF
    for i in range(1, n+1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    
    return cost
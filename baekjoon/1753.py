import sys
import heapq

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)  # 최단거리 테이블

# 간선 정보 저장
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


# 다익스트라
def dijkstra(start):
    q = []
    # 시작 노드 설정, 우선순위 큐 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 인접 노드 확인
        for v in graph[now]:
            cost = dist + v[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은경우
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))


dijkstra(K)  # 다익스트라 수행

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

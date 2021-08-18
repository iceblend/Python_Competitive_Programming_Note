n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
cnt = 0

for i in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

def dfs(cur):
    global check
    global cnt

    check[cur] = 1
    cnt += 1

    for nxt in adj[cur]:
        if check[nxt] == 0:
            dfs(nxt)

dfs(1)
print(cnt - 1)

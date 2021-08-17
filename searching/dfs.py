n, m, s = 4, 5, 1
adj = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]

a = [[] for _ in range(n + 1)]
check = [False] * (n + 1)

for i in range(m):
    v1, v2 = adj[i][0], adj[i][1]
    a[v1].append(v2)
    a[v2].append(v1)


def dfs(v_curr):
    global check
    check[v_curr] = True
    print(v_curr, end=' ')

    for v_next in a[v_curr]:
        if check[v_next] == False:
            dfs(v_next)


dfs(s)

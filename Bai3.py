n, m, x = map(int, input().split())
adj = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)

def dfs(i):
    visited[i] = True
    for v in adj[i]:
        if not visited[v]:
            dfs(v)
dfs(x)

for i in range(1, n + 1):
    if not visited[i]:
        print(i)

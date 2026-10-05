import sys
from collections import defaultdict, deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])

    adj = defaultdict(list)
    indegree = defaultdict(int)
    nodes = set()

    idx = 1
    for _ in range(N):
        u = input_data[idx]
        op = input_data[idx + 1]
        v = input_data[idx + 2]
        idx += 3

        nodes.add(u)
        nodes.add(v)

        if op == '>':
            adj[u].append(v)
            indegree[v] += 1
            if u not in indegree:
                indegree[u] = 0
        else:
            adj[v].append(u)
            indegree[u] += 1
            if v not in indegree:
                indegree[v] = 0

    q = deque([node for node in nodes if indegree[node] == 0])
    visited_count = 0

    while q:
        curr = q.popleft()
        visited_count += 1

        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if visited_count == len(nodes):
        print("possible")
    else:
        print("impossible")


if __name__ == '__main__':
    solve()
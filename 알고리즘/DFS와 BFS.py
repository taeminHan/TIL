import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for i in range(N + 1)]

visited = [False] * (N + 1)
visited2 = [False] * (N + 1)

result_dfs = []
result_bfs = []


def dfs(start, graph, visited):
    visited[start] = True
    result_dfs.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i, graph, visited)


def bfs(start, graph, visited2):
    visited2[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        result_bfs.append(node)
        for k in graph[node]:
            if not visited2[k]:
                queue.append(k)
                visited2[k] = True



for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)

for x in graph:
    x.sort()

dfs(V, graph, visited)
bfs(V, graph, visited2)

print(*[_ for _ in result_dfs])
print(*[_ for _ in result_bfs])


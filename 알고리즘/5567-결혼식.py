import sys
from collections import deque

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)


def bfs(start, graph, visited):
    cnt = 0
    result = 0
    visited[start] = True
    queue = deque([start])
    cut_line = len(graph[1])
    while cut_line >= cnt:
        sub_node = queue.popleft()
        for k in graph[sub_node]:
            if not visited[k]:
                visited[k] = True
                queue.append(k)
                result += 1

        cnt += 1

    print(result)


for i in range(edge):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1, graph, visited)

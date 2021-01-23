import sys
from collections import deque

node, edge = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(node + 1)]
result = []


def bfs(start):
    cnt = 0
    check = [False] * (node + 1)
    check[start] = True
    queue = deque([start])

    while queue:
        select = queue.popleft()
        for x in graph[select]:
            if not check[x]:
                queue.append(x)
                check[x] = True
                cnt += 1
    return cnt


cut_line = -1

for i in range(edge):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)

for k in range(1, node + 1):
    main = bfs(k)
    if cut_line <= main:
        if cut_line < main:
            result = [k]
            cut_line = main
        if cut_line == main:
            result.append(k)
            cut_line = main

print(*[_ for _ in result])

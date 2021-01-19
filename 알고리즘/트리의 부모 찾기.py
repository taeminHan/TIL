import sys

sys.setrecursionlimit(10**6)
node_count = int(input())

graph = [[] for _ in range(node_count + 1)]
check = [0 for _ in range(node_count + 1)]

for _ in range(0, node_count - 1):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)


def dfs(start, graph, check):
    for i in graph[start]:
        if check[i] == 0:
            check[i] = start
            dfs(i, graph, check)

dfs(1, graph, check)

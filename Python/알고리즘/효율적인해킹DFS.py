import sys
from collections import deque

node, edge = map(int, input().split())
graph = [[] for _ in range(node + 1)]
result = []


def dfs(start):
    check = [False] * (node + 1)
    check[start] = True
    cnt = 1

    for i in graph[start]:
        if not check[i]:
            check[i] = True
            cnt += 1


for i in range(edge):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)

dfs(1)

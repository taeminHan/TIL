import sys
from collections import deque

h, w = map(int, sys.stdin.readline().rstrip().split())
check = [[False] * w for _ in range(h)]
g = []


def bfs():
    pass


for _ in range(h):
    g.append(list(sys.stdin.readline().rstrip()))

print(g)

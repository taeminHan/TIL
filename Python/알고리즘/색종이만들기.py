import sys
from collections import deque

graph = []
graph_edge = int(sys.stdin.readline().rstrip())
for i in range(0, graph_edge):
    graph.append(sys.stdin.readline().rstrip().split(" "))

countWhite = 0
countBlue = 0


def slice_square(g, edge):
    queue = deque()
    edge //= 2
    while edge < 1:
        for j in g:

            queue.append(j[:edge//2])
            queue.append(j[edge//2:])
        for k in queue:


        
slice_square(graph, graph_edge)

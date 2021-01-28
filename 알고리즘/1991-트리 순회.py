import sys


class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def front(node):
    print(node.item, end='')
    if node.left is not None:
        front(graph[node.left])
    if node.right is not None:
        front(graph[node.right])


def center(node):
    if node.left is not None:
        center(graph[node.left])
    print(node.item, end='')
    if node.right is not None:
        center(graph[node.right])



def back(node):
    if node.left is not None:
        back(graph[node.left])
    if node.right is not None:
        back(graph[node.right])
    print(node.item, end='')


graph = {}

for _ in range(int(sys.stdin.readline().rstrip())):
    a, b, c = sys.stdin.readline().rstrip().split()
    if b == '.':
        b = None
    if c == '.':
        c = None
    graph[a] = Node(a, b, c)

front(graph['A'])
print()
center(graph['A'])
print()
back(graph['A'])

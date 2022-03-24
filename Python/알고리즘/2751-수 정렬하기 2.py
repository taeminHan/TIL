import sys
from collections import deque

queue = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    queue.append(int(sys.stdin.readline().rstrip()))
queue = sorted(queue)

for i in queue:
    print(i)
import sys
from collections import deque

queue = deque()
for i in range(0, 10):
    queue.append(int(sys.stdin.readline().strip()) % 42)

print(len(set(queue)))
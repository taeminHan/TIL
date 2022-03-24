import sys
from collections import deque

C = int(sys.stdin.readline().rstrip())


for i in range(C):
    cnt = 0

    queue = deque(map(int, sys.stdin.readline().rstrip().split(" ")))
    student = queue.popleft()
    average = sum(queue) / student
    for j in queue:
        if j > average:
            cnt += 1

    print('{0:0.3f}%'.format((cnt/student) * 100))
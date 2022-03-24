import sys
from collections import deque

num = int(sys.stdin.readline())
group = deque([0, 1])

for i in range(2, num+1):
    group.append(group[i-1] + group[i-2])
print(group[num])
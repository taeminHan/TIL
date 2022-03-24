from sys import stdin
from collections import deque

num = int(stdin.readline().rstrip())
group = deque([0 for _ in range(num+1)])

for i in range(2, num + 1):
    group[i] = group[i-1] + 1
    if i % 3 == 0 and group[i] > group[i // 3] + 1:
        group[i] = group[i // 3] + 1
    elif i % 2 == 0 and group[i] > group[i // 2] + 1:
        group[i] = group[i // 2] + 1
print(group[num])
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
group = [i for i in range(1, n+1)]
result = deque()
k-=1
count = k

result.append(group[count])
del group[count]

while group:
    count += k
    if count <= len(group):
        result.append(group[count])
        del group[count]
    else:
        count = count - len(group)
        result.append(group[count])
        del group[count]
print(count)
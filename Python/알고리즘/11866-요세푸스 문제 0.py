from collections import deque

n, k = map(int, input().split())
queue = deque(i for i in range(1, n + 1))
res = []

while queue:
    queue.rotate(-(k-1))
    res.append(queue.popleft())

print('<', end='')
for j in range(len(res)):
    if j != len(res) -1:
        print('{}, '.format(res[j]), end="")
    else:
        print('{}>'.format(res[j]))
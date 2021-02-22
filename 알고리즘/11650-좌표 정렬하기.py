import sys

queue = []

for _ in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    queue.append([x, y])
queue.sort(key=lambda x: (x[0], x[1]))
for i in queue:
    print(i[0], i[1])
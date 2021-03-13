import sys

queue = []

for _ in range(int(sys.stdin.readline().rstrip())):
    queue.append(sys.stdin.readline().rstrip())

for i in (sorted(list(set(queue)), key=lambda x: (len(x), x))):
    print(i)
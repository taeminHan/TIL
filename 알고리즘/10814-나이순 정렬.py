import sys

group = []

for _ in range(int(sys.stdin.readline().rstrip())):
    i, j = input().split()
    group.append((int(i), j))

for k in sorted(group, key=lambda x: x[0]):
    print(k[0], k[1])
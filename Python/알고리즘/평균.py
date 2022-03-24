import sys

count = int(sys.stdin.readline().rstrip())
group = list(sys.stdin.readline().rstrip().split())

group = list(map(int, group))

M = max(group)

for i in group:
    group[group.index(i)] = i / M * 100
print(group)

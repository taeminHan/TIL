import sys

n = int(sys.stdin.readline().rstrip())
group = list()

min_count = 0

for _ in range(n):
    group.append(sys.stdin.readline().rstrip().split())

for i in range(1, n):
    a = group[i-1] + group[i][0] + group[i][2]

import sys

count = int(sys.stdin.readline().rstrip())

group = sys.stdin.readline().rstrip().split()

group = sorted((map(int, group)))


result = 0

for i, j in enumerate(group):
    result += j + sum(group[:int(i)])
print(result)
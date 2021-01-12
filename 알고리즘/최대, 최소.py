import sys

group = []
for i in range(0, 9):
    group.append(int(sys.stdin.readline().rstrip()))
print(max(group))
print(int(group.index(max(group))+1))
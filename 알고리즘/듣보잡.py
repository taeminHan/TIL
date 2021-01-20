import sys

listener, watcher = map(int, sys.stdin.readline().split())

group = {}
result = []
cnt = 0

for _ in range(0, listener + watcher):
    name = sys.stdin.readline().rstrip()
    try:
        group[name] += 1
    except:
        group[name] = 1

for i, j in group.items():
    if j > 1:
        cnt += 1
        result.append(i)

print(cnt)
for i in sorted(result):
    print(i)

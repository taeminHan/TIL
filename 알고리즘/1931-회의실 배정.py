import sys
meet = []
count = 0

for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    meet.append((a, b))
meet = sorted(meet, key= lambda x:(x[1], x[0]))

count = 0
start = 0

for i in meet:
    if i[0] >= start:
        start = i[1]
        count += 1
print(count)

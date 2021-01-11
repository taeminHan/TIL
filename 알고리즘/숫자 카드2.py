import sys

allCount = int(sys.stdin.readline().rstrip())
allCard = list(map(int, sys.stdin.readline().rstrip().split()))


sangCount = int(sys.stdin.readline().rstrip())
sangCard = map(int, (sys.stdin.readline().rstrip().split()))

result = {}

for i in allCard:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
real = []

for j in sangCard:
    if j not in result:
        real.append(0)
    else:
        real.append(result[j])
print(*[_ for _ in real])

"""
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))"""
from itertools import combinations

N, M = map(int, input().split())
C = combinations(range(1, N + 1), M)  # iter(tuple)
for i in C:
    print(' '.join(map(str, i)))

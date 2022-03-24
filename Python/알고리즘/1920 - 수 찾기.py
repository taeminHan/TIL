from sys import stdin, stdout
import sys
sys.setrecursionlimit(10**6)

n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())


result = []


def binary_search(i, group, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary_search(l, N, start, m - 1)
    else:
        return binary_search(l, N, m + 1, end)

for l in M:
    start = 0
    end = len(N) - 1
    print(binary_search(l, N, start, end))
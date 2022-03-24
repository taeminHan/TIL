import sys

k, n = map(int, sys.stdin.readline().rstrip().split())
cable = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(cable)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in cable:
        lines += i // mid

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
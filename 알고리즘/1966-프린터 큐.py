import sys

for i in range(int(sys.stdin.readline().rstrip())):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    imp = list(map(int, sys.stdin.readline().rstrip().split()))

    max_imp = max(imp)
    max_position = imp.index(max_imp)

    for j in range(max_position):
        if imp[0]

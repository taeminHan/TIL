import sys


for _ in range(int(sys.stdin.readline().rstrip())):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    apart = [[] for _ in range(k+1)]

    for a in range(1, n+1):
        apart[0].append(a)

    for i in range(1, k+1):
        for j in range(1, n+1):
            apart[i].append(sum(apart[i-1][:j]))
    print(apart[k][n-1])
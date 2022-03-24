import sys

N, X = sys.stdin.readline().split(" ")
group = list(sys.stdin.readline().split())

for i in group:
    if int(X) > int(i):
        print(i, end=" ")

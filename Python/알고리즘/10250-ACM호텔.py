import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    h, w, t = map(int, sys.stdin.readline().rstrip().split())
    a = t % h
    b = t // h + 1

    if a == 0:
        a = h
        b -= 1

    print(a*100 + b)
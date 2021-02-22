import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    count = 2
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if ((y-x) - 2) % 2 == 0:
        count += ((y-x) - 2) // 2
    else:
        count += ((y - x) - 2) // 2
        count += ((y - x) - 2) % 2
    print(count)
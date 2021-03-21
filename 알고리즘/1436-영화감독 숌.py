import sys

n = int(sys.stdin.readline().rstrip())


def find(count, N):
    x = 666
    while count != N:
        x += 1
        if "666" in str(x):
            count += 1
    return x


print(find(1, n))

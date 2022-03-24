import sys

x, y = map(int, sys.stdin.readline().rstrip().split())


def eratosthens(m, n):
    answer = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if answer[i]:
            for j in range(2 * i, n, i):
                answer[j] = False
    for i in range(m, n):
        if i > 1 and answer[i] is True:
            print(i)


eratosthens(x, y + 1)

import sys

n = int(sys.stdin.readline().rstrip())

while n != 1:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            n //= i
            break

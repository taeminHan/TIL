import sys
count = 1
n = int(sys.stdin.readline().rstrip())
if n == 1:
    print(1)
else:
    while n > 1:
        n -= count * 6
        count += 1

    print(count)
import sys

ch = [True] * 100000

for i in (2, int(100000 ** 0.5)):
    if ch[i]:
        for j in range(i * 2, 100000, i):
            if ch[j]:
                ch[j] = False

while True:
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        break
    for i in range(3, 100000):
        if ch[i]:
            if ch[num - i]:
                print("{} = {} + {}".format(num, i, num - i))
                break

import sys


def Han(a):
    hansu = 0
    for i in range(1, int(a) + 1):
        if i < 100:
            hansu += 1
        elif i < 1000:
            i = list(map(int, list(str(i))))
            if i[2] - i[1] == i[1] - i[0]:
                hansu += 1
    print(hansu)


num = sys.stdin.readline().rstrip()

Han(num)

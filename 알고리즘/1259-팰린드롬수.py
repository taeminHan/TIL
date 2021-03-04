import sys

while True:
    x = list(sys.stdin.readline().rstrip())
    if x == ['0']:
        break
    if len(x) % 2 == 0:
        if x[:len(x) // 2] == list(reversed(x[len(x) // 2:])):
            print("yes")
        else:
            print("no")
    else:
        if x[:len(x) // 2] == list(reversed(x[(len(x) // 2) + 1:])):
            print("yes")
        else:
            print("no")

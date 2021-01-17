import sys

mul = 1
count = [0]*10

for i in range(0, 3):
    num = int(sys.stdin.readline())
    mul *= num

mul = list(str(mul))

for j in mul:
    count[int(j)] += 1

for k in count:
    print(k)
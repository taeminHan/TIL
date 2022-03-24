import sys

count = int(sys.stdin.readline())
queue = [0, 1, 2, 4]
asd = []
for i in range(count):
    asd.append(sys.stdin.readline())

for i in asd:
    if int(i) > 3:
        for j in range(4, int(i) + 1):
            queue.append(queue[j - 1] + queue[j - 2] + queue[j - 3])
        print(queue[int(i)])
        queue = [0, 1, 2, 4]
    else:
        print(queue[int(i)])
        queue = [0, 1, 2, 4]
import sys
from collections import deque


count_data = int(sys.stdin.readline().rstrip())

queue = deque()
result = []

for _ in range(count_data):
    for j in range(int(sys.stdin.readline().rstrip())):
        option, num = sys.stdin.readline().rstrip().split()
        if option == "I":
            queue.append(int(num))
            queue = deque(sorted(queue))
        elif option == "D" and num == '1':
            try:
                queue.pop()
            except:
                pass
        elif option == "D" and num == '-1':
            try:
                queue.popleft()
            except:
                pass

    if len(queue) == 0:
        result.append("EMPTY")
    else:
        result.append('{} {}'.format(queue[-1], queue[0]))
    queue.clear()
for i in result:
    print(i)
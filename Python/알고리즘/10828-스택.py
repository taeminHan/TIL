import sys
from collections import deque

count = int(sys.stdin.readline().rstrip())
stack = deque()

for _ in range(count):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)
    del order

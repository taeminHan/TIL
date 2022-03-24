import sys
from collections import deque

stack = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    VPS = list(sys.stdin.readline().rstrip())
    for i in VPS:
        stack.append(i)
        try:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
        except IndexError:
            pass
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
    stack.clear()

import sys
from collections import deque

word_stack = deque(sys.stdin.readline().rstrip())
sec_stack = deque()
cursor = len(word_stack)

for _ in range(int(sys.stdin.readline().rstrip())):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'L':
        try:
            sec_stack.appendleft(word_stack.pop())
        except IndexError:
            continue
    elif order[0] == 'D':
        try:
            word_stack.append(sec_stack.popleft())
        except IndexError:
            continue
    elif order[0] == 'B':
        try:
            word_stack.pop()
        except IndexError:
            continue
    elif order[0] == 'P':
        word_stack.append(str(order[1]))
print(''.join(word_stack+sec_stack))
import sys
from collections import deque

n = 0
stop = True
stack = deque()
answer = deque()

count = int(sys.stdin.readline().rstrip())

for _ in range(0, count):
    num = int(sys.stdin.readline().rstrip())

    while n < num:
        n += 1
        stack.append(n)
        answer.append('+')

    if num == stack[-1]:
        stack.pop()
        answer.append('-')
    else:
        stop = False

if not stop:
    print("NO")
else:
    for k in answer:
        print(k)
import sys
from collections import deque

num = []
stack = deque()
result = 0

n = int(sys.stdin.readline().rstrip())

form = list(sys.stdin.readline().rstrip())


for _ in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

for i in form:
    if i.isalpha():
        stack.append(num[ord(i) - 65])
    elif i == '+':
        stack.append(stack.pop() + stack.pop())
    elif i == '-':
        first_pop = stack.pop()
        second_pop = stack.pop()
        stack.append(second_pop - first_pop)
    elif i == '/':
        first_pop = stack.pop()
        second_pop = stack.pop()
        stack.append(second_pop / first_pop)
    elif i == '*':
        stack.append(stack.pop() * stack.pop())

print('{:.2f}'.format(stack[0]))

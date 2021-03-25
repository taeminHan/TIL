import collections as cs
import sys

num = int(sys.stdin.readline().rstrip())
raw_postfixGroup = list(sys.stdin.readline().rstrip())
for i in range(num):
    = []sys.stdin.readline().rstrip().split()
remake = []
result = []

group = cs.deque([i + 1 for i in range(num)])

for i in raw_postfixGroup:
    if i == '+':
        remake.append(i)
    elif i == '-':
        remake.append(i)
    elif i == '*':
        remake.append(i)
    elif i == '/':
        remake.append(i)
    else:
        remake.append(int(ord(i)) - 64)
for i in remake:
    if i == '+':
        num1 = result[-1]
        num2 = result[-2]
        if len(result) == 2:
            del result
            result = [num2 + num1]
        else:
            del result[-2:]
            result.append(num1 + num2)
    elif i == '-':
        num1 = result[-1]
        num2 = result[-2]
        if len(result) == 2:
            del result
            result = [num2 - num1]
        else:
            del result[-2:]
            result.append(num2 - num1)
    elif i == '*':
        num1 = result[-1]
        num2 = result[-2]
        if len(result) == 2:
            del result
            result = [num2 * num1]
        else:
            del result[-2:]
        result.append(num1 * num2)
    elif i == '/':
        num1 = result[-1]
        num2 = result[-2]
        if len(result) == 2:
            del result
            result = [num2 / num1]
        else:
            del result[-2:]
        result.append(num2 / num1)
    else:
        result.append(i)

if result[0] == float:
    print(float(result[0]))
else:
    print(int(result[0]))
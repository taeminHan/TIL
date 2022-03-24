import sys


num1, num2 = sys.stdin.readline().rstrip().split()
num1 = ''.join(reversed(list(num1)))
num2 = ''.join(reversed(list(num2)))

print(max(int(num1), int(num2)))
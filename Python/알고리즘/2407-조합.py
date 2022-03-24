import sys
import math

n, m = map(int, sys.stdin.readline().rstrip().split())

a = math.factorial(n)
b = (math.factorial(n - m)) * (math.factorial(m))

print(a // b)

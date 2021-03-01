import sys
import math


a, b = map(int, sys.stdin.readline().rstrip().split())
print(math.gcd(a, b))
print(a*b//math.gcd(a,b))

for
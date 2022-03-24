import math
import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a*b//math.gcd(a, b))
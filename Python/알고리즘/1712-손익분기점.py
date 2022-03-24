import sys
import math

a, b, c = map(int, sys.stdin.readline().rstrip().split())

if b >= c:
    print("-1")
else:
    print(a//(c-b) + 1)

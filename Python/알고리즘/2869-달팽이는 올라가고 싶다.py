import sys
import math
a, b, v = map(int, sys.stdin.readline().rstrip().split())
print(math.ceil((v-b) / (a-b)))
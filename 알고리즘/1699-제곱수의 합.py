import sys
import math

n = int(sys.stdin.readline().rstrip())

pow_list = []
for i in range(1, n + 1):
    if i ** 2 < n:
        pow_list.append(i ** 2)
m = [j for j in range(1, n + 1)]

for i in m:
    for j in pow_list:
        if j < n-j:

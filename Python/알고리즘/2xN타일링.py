import sys
from collections import deque

tile = deque([0, 1, 2, 3, 5, 8])

count = int(sys.stdin.readline())

for i in range(6, count + 1):
    tile.append((tile[i - 2] + tile[i - 1]) % 10007)
print(tile[count])

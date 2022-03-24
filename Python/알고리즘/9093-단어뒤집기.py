import sys
from collections import deque

result = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    for i in sys.stdin.readline().rstrip().split():
        result.append(''.join(reversed(i)))
    print(' '.join(result))
    result.clear()

import sys
from collections import deque

result = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    sent = sys.stdin.readline().rstrip().split()
    for i in sent:
        result.append(''.join(reversed(i)))
    print(' '.join(result))
    result.clear()

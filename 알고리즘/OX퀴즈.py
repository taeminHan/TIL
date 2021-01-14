import sys
from collections import deque

count = int(sys.stdin.readline().rstrip())
group = deque()

cnt = 0

for i in range(count):
    word = list(sys.stdin.readline().rstrip().split("X"))
    for j in word:
        if len(j) != 0:
            for k in range(0, len(j)+1):
                cnt += k
    print(cnt)
    cnt = 0
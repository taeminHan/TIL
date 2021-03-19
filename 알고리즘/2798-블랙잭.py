import sys
from collections import deque

count, num = map(int, sys.stdin.readline().rstrip().split())
card = deque(map(int, sys.stdin.readline().rstrip().split()))

result = deque()
length = len(card)

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            if card[i] + card[j] + card[k] <= num:
                result.append(card[i] + card[j] + card[k])

result.append(num)
result = sorted(result)
print(result[-2])
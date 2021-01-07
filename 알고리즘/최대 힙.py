from collections import deque
import sys

count = int(sys.stdin.readline())
heap = deque()
answer = deque()
col = []

for i in range(count):
    asd = int(sys.stdin.readline())
    col.append(asd)

for num in col:
    if num == 0 and len(heap) == 0:
        answer.append(0)
    elif num == 0 and len(heap) > 0:
        answer.append(heap.popleft())
    elif num != 0:
        if len(heap) == 0:
            heap.append(num)
        else:
            for s in list(heap):
                if s < num:
                    heap.insert(heap.index(s), num)
                elif heap[-1] > num:
                    heap.append(num)
for a in answer:
    print(a)
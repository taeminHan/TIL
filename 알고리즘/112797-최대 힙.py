import sys
import heapq as hq

heap = []

for _ in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        hq.heappush(heap, (-num))
    else:
        try:
            print(-1 * hq.heappop(heap))
        except:
            print(0)
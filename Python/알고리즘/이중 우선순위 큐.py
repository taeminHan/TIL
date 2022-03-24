import heapq as hq
import sys

count_data = int(sys.stdin.readline().rstrip())

queue = []
result = []
hq.heapify(queue)

for _ in range(count_data):
    for j in range(int(sys.stdin.readline().rstrip())):
        option, num = sys.stdin.readline().rstrip().split()
        if option == "I":
            hq.heappush(queue, int(num))
        else:
            if num == '1':
                try:
                    queue = list(queue)
                    queue.pop()
                    hq.heapify(queue)
                except:
                    pass
            elif num == '-1':
                try:
                    hq.heappop(queue)
                except:
                    pass

    if len(queue) == 0:
        result.append("EMPTY")
    else:
        result.append('{} {}'.format(queue[-1], queue[0]))
    queue.clear()
for i in result:
    print(i)
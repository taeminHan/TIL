import sys
from collections import deque

while True:
    w, h = map(int, input().split())

    find_x = [-1, -1, 0, 1, 1, 1, 0, -1]
    find_y = [0, 1, 1, 1, 0, -1, -1, -1]

    queue = deque()
    cnt = 0

    if w == 0 and h == 0:
        break
    else:
        graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    queue.append((i, j))
                    graph[i][j] = 2

                    while queue:
                        x, y = queue.popleft()
                        for k in range(8):
                            new_x = x + find_x[k]
                            new_y = y + find_y[k]
                            if 0 <= new_x < h and 0 <= new_y < w:
                                if graph[new_x][new_y] == 1:
                                    queue.append((new_x, new_y))
                                    graph[new_x][new_y] = 2
                    else:
                        cnt += 1

    print(cnt)

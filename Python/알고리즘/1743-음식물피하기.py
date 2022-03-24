from collections import deque
n, m, k = map(int, input().split())
a = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]
ans = 0

def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1
    check[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not check[nx][ny] and a[nx][ny]:
                q.append((nx, ny))
                check[nx][ny] = True
                cnt += 1
    return cnt

for _ in range(k):
    r, c = map(int, input().split())
    a[r-1][c-1] = 1
for i in range(n):
    for j in range(m):
        if not check[i][j] and a[i][j]:
            ans = max(ans, bfs(i, j))
print(ans)

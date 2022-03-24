import sys

node, edge = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(node + 1)]

check = [0] * (node + 1)

for i in range(edge):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0


def bfs(x):
    queue = [x]
    while queue:
        v = queue.pop()
        for a in graph[v]:
            if check[a] == 0:
                queue.append(a)
                check[a] = 1


for j in range(1, node + 1):
    if check[j] == 0:
        bfs(j)
        cnt += 1

print(cnt)


"""
import sys

N,M=map(int,sys.stdin.readline().split())

graph=[[]for i in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visit_list=[0]*(N+1)

def bfs(v):
    q=[v]
    while q:
        v=q.pop(0)
        for i in graph[v]:
            if visit_list[i]==0:
                q.append(i)
                visit_list[i]=1

answer=0
for i in range(1,N+1):
    if visit_list[i]==0:
        bfs(i)
        answer+=1

sys.stdout.write(str(answer))
"""

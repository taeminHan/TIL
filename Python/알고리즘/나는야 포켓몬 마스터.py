import sys

poke_cnt, problem_cnt = map(int, sys.stdin.readline().rstrip().split(" "))

queue1 = {}
queue2 = {}

for i in range(1, poke_cnt + 1):
    pokename = str(sys.stdin.readline().rstrip())
    queue1[str(i)] = pokename
    queue2[pokename] = str(i)
for j in range(problem_cnt):
    Que = sys.stdin.readline().rstrip()
    try:
        print(queue1[str(Que)])

    except:
        print(queue2[str(Que)])
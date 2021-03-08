import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip()) + 1

asd = []

answer = [True] * n

for i in range(2, int(n ** 0.5) + 1):
    if answer[i]:
        for j in range(2 * i, n, i):
            answer[j] = False
for i in range(m, n):
    if i > 1 and answer[i] is True:
        asd.append(i)

print(sum(asd))
print(asd[0])
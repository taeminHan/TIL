import sys

n = int(sys.stdin.readline().rstrip())
matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))


matrix2 = [[0] * 3 for i in range(n)]


for i in range(n):
    if i == 0:
        matrix2[i] = matrix[i]
    else:
        matrix2[i][0] = matrix[i][0] + min(matrix2[i - 1][1], matrix2[i - 1][2])
        matrix2[i][1] = matrix[i][1] + min(matrix2[i - 1][0], matrix2[i - 1][2])
        matrix2[i][2] = matrix[i][2] + min(matrix2[i - 1][0], matrix2[i - 1][1])

print(min(matrix2[-1]))
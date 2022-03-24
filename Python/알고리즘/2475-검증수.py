import sys

koi = list(map(int, sys.stdin.readline().rstrip().split()))
result = []
for i in koi:
    result.append(i**2)

print(sum(result) % 10)
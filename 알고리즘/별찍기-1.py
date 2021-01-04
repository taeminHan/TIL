from sys import stdin

num = int(stdin.readline())
for i in range(1, num+1):
    for j in range(i):
        continue
    print("*"*i)
import sys

dial = {'1':2, 'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10, '0':11}

word = list(sys.stdin.readline().rstrip())
result = 0

for i in word:
    for j in dial:
        if i in j:
            result += dial[j]

print(result)
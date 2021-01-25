import sys

sentence = list(map(str, sys.stdin.readline().rstrip().split(" ")))
if sentence[0] == '':
    del sentence[0]
elif sentence[-1] == '':
    del sentence[-1]
print(len(sentence))
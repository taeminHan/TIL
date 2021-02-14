import sys

sent = sys.stdin.readline().rstrip()

cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_word:
        sent = sent.replace(i, "*")
print(len(sent))
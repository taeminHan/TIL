import sys

count = int(sys.stdin.readline().rstrip())
count2 = count

for _ in range(count):
    word = list(sys.stdin.readline().rstrip())
    for i in range(len(word)):
        if word[i] in word[i+2:] and word[i] != word[i+1]:
            count2 -= 1
            break
        else:
            continue
print(count2)
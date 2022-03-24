import sys

count = int(sys.stdin.readline().rstrip())

for _ in range(count):
    word_count, words = sys.stdin.readline().rstrip().split()
    result = []
    for i in words:
        result.append(int(word_count) * i)
    print(''.join(result))
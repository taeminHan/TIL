word = input()
word = word.lower()
cnt = 0
word_map = {}

for i in list(word):
    try:
        word_map[i] += 1
    except KeyError:
        word_map[i] = 1

length = [k for k,v in word_map.items() if max(word_map.values()) == v]
if len(length)> 1:
    print("?")
else:
    print(''.join(length).upper())
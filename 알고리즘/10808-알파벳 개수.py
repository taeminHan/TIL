from string import ascii_lowercase

ascii = ascii_lowercase
word = input()
res = []
for i in ascii:
    res.append(str(word.count(i)))
print(' '.join(res))

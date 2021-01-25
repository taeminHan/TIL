from string import ascii_lowercase
word = list(ascii_lowercase)
q = list(input())
result = []

for i in word:
    try:
        if q.index(i) in result:
            pass
        else:
            result.append(q.index(i))
    except:
        result.append(-1)
print(*[_ for _ in result])
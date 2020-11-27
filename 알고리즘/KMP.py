string = input().split("-")
result = []
for i in string:
    result.append(str(i)[0])
print(''.join(result))
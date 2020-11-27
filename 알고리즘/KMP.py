string_Group = input().split("-")
resultCount = []
for i in string_Group:
    resultCount.append(i[0])
print(''.join(resultCount))
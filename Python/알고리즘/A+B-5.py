group = []
while True:
    a, b = input().split()
    if int(a) == 0 and int(b) == 0:
        break
    else:
        group.append(int(a)+int(b))
for i in group:
    print(i)
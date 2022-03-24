a, b = input().split(' ')

if int(a) > int(b):
    a, b = int(b), int(a)
x = []
if (int(b) - int(a)) < 2:
    x.append(0)
    print(0)

else:
    for i in range(int(a)+1, int(b)):
        x.append(i)
    print(len(x))
    for i in x:
        print(i, end=' ')
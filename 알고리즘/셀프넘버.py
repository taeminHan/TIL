
self_num = [_ for _ in range(1, 10001)]

for i in range(1, 10001):
    if i < 10:
        self_num[i+i] = 0
    elif i < 100:
        self_num[i + int(list(str(i))[0]) + int(list(str(i))[1])] = 0
    elif i < 1000:
        if i + int(list(str(i))[0]) + int(list(str(i))[1]) + int(list(str(i))[2]) <= 10000:
            self_num[i + int(list(str(i))[0]) + int(list(str(i))[1]) + int(list(str(i))[2])] = 0
    elif i < 10000:
        if i + int(list(str(i))[0]) + int(list(str(i))[1]) + int(list(str(i))[2]) + int(list(str(i))[3]) < 10000:
            self_num[i + int(list(str(i))[0]) + int(list(str(i))[1]) + int(list(str(i))[2]) + int(list(str(i))[3])] = 0

for j in self_num:
    if j != 0 and j-1 != 0:
        print(j-1)
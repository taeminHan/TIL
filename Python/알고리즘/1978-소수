count = int(input())
num_list = map(int, input().split(" "))

result_count = 0
for i in num_list:
    mid_count = 0
    if i == 1:
        pass
    elif i == 2:
        result_count += 1
    else:
        for j in range(2, i):
            if i % j == 0:
                mid_count += 1
        if mid_count == 0:
            result_count += 1

print(result_count)
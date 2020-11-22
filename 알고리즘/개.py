count = int(input())
sum_list = []
for i in range(1, count+1):
    a, b = input().split(" ")
    sum_list.append(int(a)+int(b))

for i in range(1, count+1):
    print("Case #"+str(i)+":", sum_list[i-1])
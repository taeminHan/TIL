a = int(input())
b = a
count = 0

while True:
    if b == a % 10 * 10 + (a // 10 + a % 10) % 10:
        count = count + 1
        print(count)
        break
    else:
        a = a % 10 * 10 + (a // 10 + a % 10) % 10
        count = count + 1

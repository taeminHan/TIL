import sys

count = 1
x = int(sys.stdin.readline().rstrip())

while True:
    if x == 1:
        print('{}/{}'.format(1, 1))
        break
    else:
        x -= count
        if count >= x:
            count += 1
            j = 1
            if count % 2 == 0:
                for _ in range(x - 1):
                    count -= 1
                    j += 1
                print('{}/{}'.format(j, count))
            else:
                for _ in range(x - 1):
                    count -= 1
                    j += 1
                print('{}/{}'.format(count, j))
            break

        else:
            count += 1

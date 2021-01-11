import sys

group_S = set()
count = int(sys.stdin.readline())

for i in range(count):
    option = sys.stdin.readline().rstrip()

    if option == 'all':
        group_S = set(_ for _ in range(1, 21))
    elif option == 'empty':
        group_S.clear()
    else:
        option, num = option.split(" ")
        num = int(num)
        if option == 'add':
            group_S.add(num)
        elif option == 'remove':
            group_S.discard(num)
        elif option == 'check':
            if num in group_S:
                print(1)
            else:
                print(0)
        elif option == 'toggle':
            if num in group_S:
                group_S.discard(num)
            else:
                group_S.add(num)
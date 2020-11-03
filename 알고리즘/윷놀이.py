for i in range(0, 3):

    a = input().split(' ')

    if a.count('0') == 1:
        print('A')
    elif a.count('0') == 2:
        print('B')
    elif a.count('0') == 3:
        print('C')
    elif a.count('0') == 4:
        print('D')
    elif a.count('1') == 4:
        print('E')

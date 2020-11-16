while True:
    b = int(input('머시기:'))
    for i in range(1, b + 1):
        if i % 2 == 1:
            continue
        else:
            print(i, end=' ')

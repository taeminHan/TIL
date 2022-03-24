import sys

while True:

    sentence = sys.stdin.readline().rstrip('\n')
    if not sentence:
        break
    low_count, upper_count, dig_count, white_count = 0, 0, 0, 0

    for i in sentence:
        if i.islower():
            low_count += 1
        elif i.isupper():
            upper_count += 1
        elif i.isdigit():
            dig_count += 1
        elif i.isspace():
            white_count += 1

    print(low_count, upper_count, dig_count, white_count)

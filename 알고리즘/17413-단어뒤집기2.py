import sys
import re
sent = sys.stdin.readline().rstrip()
com = re.compile(r'<.+?>')


if re.split(r'<.+?>', sent):
    sp = list(filter(lambda x: x != '', re.split(r'<.+?>', sent)))
    for i in sp:
        sp = (re.sub(i, str(i)[::-1], sent))
        print(sp+'?')
    print(sp)
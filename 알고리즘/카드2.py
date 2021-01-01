import sys
import collections

"""
파이썬의 collections 모듈은, 파이썬에 내장된 일반 자료형의(dict, list, set, tuple) 컨테이너 타입을 조금 더 발전시킨 형태의 구현체이다.
파이썬 2.7 까지는 네임드튜플, 디큐, 카운터, 순서형 딕셔너리, 기본 딕셔너리의 다섯 개의 컨테이너를 구현하고 있었으나
파이썬 3부터는 체인맵, 유저 딕셔너리, 유저 리스트, 유저 스트링 등의 자료구조가 추가되었다.
"""

num = int(sys.stdin.readline().rstrip())
group = collections.deque([i+1 for i in range(num)])

while len(group) > 1:
    group.popleft()
    group.append(group[0])
    group.popleft()

print(group[0])

"""
원본
num = int(input())
group = []
for i in range(num):
    group.append(i+1)

for i in range(num):
    if len(group) == 1:
        break
    else:
        group.remove(i+1)
        group.append(group[0])
        del group[0]
print(group[0])
"""
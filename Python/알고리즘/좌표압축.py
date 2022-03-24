import sys

count = int(sys.stdin.readline())
raw_group = list(map(int, sys.stdin.readline().rstrip().split(" ")))
sort_group = sorted(set(raw_group))

sort_group = {sort_group[i]: i for i in range(len(sort_group))}
print(*[sort_group[i] for i in raw_group])  # 애스터리스크 언패킹 이용


"""import sys

count = int(sys.stdin.readline())
raw_group = sys.stdin.readline().rstrip().split(" ")
raw_group = list(map(str, raw_group))

mapping_group = sorted(list(map(int, set(raw_group))))

for i, v in enumerate(mapping_group):
    raw_group[raw_group.index(str(v))] = i

print(" ".join(list(map(str, raw_group))))
"""
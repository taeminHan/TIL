import sys

x, y, w, h = map(int, sys.stdin.readline().split())

print(min(min(w-x, x-0), min(h-y, y-0)))

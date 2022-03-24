from math import factorial as f

n, k = map(int, input().split())

if k < 0 or k > n:
    print(0)
else:
    print(f(n)//(f(k) * f(n - k)))
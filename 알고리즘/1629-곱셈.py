import sys

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    print(pow(a, b, c))
import sys

n = int(sys.stdin.readline().rstrip())
data = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

for target in targets:
    if target in data:
        print(1)
    else:
        print(0)

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

# 0 a b : 합집합, a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합친다.
# 1 a b : 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산.

print(parent)


def find(target):
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

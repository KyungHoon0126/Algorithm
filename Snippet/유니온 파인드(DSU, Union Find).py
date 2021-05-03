# 유니온 파인드(DSU, Disjoint set Union) : Union과 Find라는 연산을 지원하는 자료구조, 집합을 관리하는 트리 형태의 자료구조(서로소 집합, 분리집합)
#                                        보통 배열에서 인덱스를 노드로 나타내어 각 인덱스의 값에 해당 인덱스의 부모 노드를 저장한다.

# 유니온(Union) : 서로 다른 disjoint set을 합치는 것. 이때 합쳐지는 기준은 보통 union by rank 즉, 항상 작은 쪽을 큰 쪽에 합친다는 의미.
#                서로 다른 두 트리(집합)를 합치는 연산, 각 트리의 루트 노드 비교 후 작은 루트 노드를 기준으로 합친다.
#                union 연산을 하기 위해서 사전에 반드시 find 연산이 필요함.

# 파인드(Find) : 어떤 노드를 인자로 넘겼을 때, 해당 노드의 루트 노드를 찾는 연산.
#               임이의 두 노드가 연결되어 있는지(루트 노드가 같은지) 확인할 때 사용.


import sys

# 만약 재귀를 사용해서 풀어야 하는 문제라면, 아래의 코드를 상단에 쓰는 것은 선택이 아닌 필수.
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편.
sys.setrecursionlimit(10 ** 6)

# 배열의 인덱스 : 노드 / 배열의 인덱스 값 : 부모 노드를 저장.
parent = [0, 1, 2, 3, 4, 5]


# find 연산
def find(target):
    if target == parent[target]:
        return target

    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]


# union 연산
def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 루트 노드를 기준으로 합친다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 3과 노드 5가 같은 집합인지 비교
# 출력 결과 : 다른 집합입니다!
if find(3) == find(5):
    print("같은 집합입니다!")
else:
    print("다른 집합입니다!")

print(parent)
# 노드 3과 노드 5를 union 연산(합친다.)
# 즉 인덱스 5 = 노드 5에 부모노드 3을 저장. -> 작은 루트 노드를 기준으로 합치기 때문.
union(3, 5)
print(parent)

# 노드 3과 노드 5가 같은 집합인지 비교
# 출력 결과 : 같은 집합입니다!
if find(3) == find(5):
    print("같은 집합입니다!")
else:
    print("다른 집합입니다!")

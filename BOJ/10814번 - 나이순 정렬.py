import sys

n = int(input())
members = []

# int(sys.stdin.readline().rstrip()) # 하나의 정수를 입력받을 때
# map(int,sys.stdin.readline().split()) # 여러개의 정수를 입력받을 때

# sys.stdin.readline().rstrip() # 하나만 입력받을 때
# sys.stdin.readline().split() # 여러개를 입력받을 때

for i in range(n):
    members.append(sys.stdin.readline().split())

# for i in range(n):
#     members.append(input().split())

print(members)

members.sort(key=lambda x: int(x[0]), reverse=False)

for age, name in members:
    print(age, name)

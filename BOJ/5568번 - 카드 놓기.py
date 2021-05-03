import sys
from itertools import permutations

input = sys.stdin.readline

n, case = int(input()), int(input())

# int()로 바꾸어서 cards에 저장한 것 밖에 없고 정답은 똑같이 나오는데 안됨.
# cards = [int(input().rstrip()) for _ in range(n)]
cards = [input().rstrip() for _ in range(n)]

answer = set()  # set 자료형, 중복 허용 X, 순서 X

# set 자료형
# add() : 값 1개 추가 / update() : 값 여러개 추가 / remove() : 특정 값 제거

for i in permutations(cards, case):
    # answer.add(int(strㅈ(i[0]) + str(i[1])))
    answer.add(''.join(i))

print(answer)
print(len(answer))

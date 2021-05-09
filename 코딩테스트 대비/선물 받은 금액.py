# 선물 받은 금액

cnt = int(input())  # 사람의 수를 입력 받는다.
names = list(input().split())  # 사람 수만큼 이름을 입력 받는다.
hash_map = {}  # 금액 변화를 저장할 dict
use_money = {}  # 쓴 금액을 저장할 dict

for i in names:
    hash_map[i] = []

print(hash_map)

for i in range(cnt):
    # 이름, 가격, 사람 수, 사람 이름
    data = list(input().split())
    name = data[0]  # 선물을 하는 사람의 이름
    money = data[1]  # 선물을 하는 사람이 쓸 수 있는 금액
    people_cnt = data[2]  # 선물 받은 사람의 수

    # 쓴 금액 저장
    use_money[name] = [int(money)]

    if int(money) == 0 and int(people_cnt) == 0:
        continue

    # 각 사람이 받을 수 있는 선물 금액
    each_money = str(int(money) // int(people_cnt))

    # 각 사람이 받을 수 있는 금액을 저장.
    for i in data[3:len(data)]:
        # i : 사람 이름, hash_map의 key 값
        if i in hash_map.keys():
            hash_map[i].append(each_money)
        else:
            hash_map[i] = [each_money]

    # 선물을 하는 사람의 남은 금액을 저장. (보유 금액 - (각 사람이 받는 금액 * 사람 수))
    hash_map[name].append(str(int(money) - (int(each_money) * int(people_cnt))))

    print(hash_map)

print(use_money)
for idx, i in enumerate(hash_map):
    sum = 0
    for value in hash_map[i]:
        sum += int(value)

    print(f'{i} {sum - use_money[i][0]}')

'''

dave laura owen vick amr

dave 200 3 laura owen vick
owen 500 1 dave
amr 150 2 vick owen
laura 0 2 amr vick
vick 0 0

'''

# 4번 - 줄다리기

from itertools import combinations
import copy


# 인원을 인자로 입력받음.
def tug(n):
    # 입력한 무게가 인원과 동일한지 비교하기위한 변수
    people_cnt = 0
    # 입력받은 무게를 저장하기 위한 배열
    people_weights = []
    # 한 팀의 최대 무게 - 최대 인원의 무게 합(경우의 수)
    diff = []

    #  모든 사람의 수(n명), 최대 100명까지.
    # if i > 100:
    #   exit()

    # 인원 수 만큼 몸무게를 입력받음.
    while people_cnt < n:
        weight = int(input("무게를 입력 : "))
        # 몸무게 조건
        # if 1 > weight or weight > 450:
        #     break
        people_weights.append(weight)
        people_cnt += 1

    print('입력받은 몸무게 : ', people_weights)

    # n // 2 : 모든 사람의 수 // 2
    # 한 팀에 들어갈 수 있는 최대 인원
    max_team_members_cnt = n // 2

    print('한 팀에 들어갈 수 있는 최대 인원 : ', max_team_members_cnt)

    # people_weights / 2 : 무게 전체의 합 / 2
    # 한 팀의 최대 무게 합(무게를 최대한 같게 만들어야 하기 때문)
    max_team_weight = sum(people_weights) / 2

    print('한 팀의 최대 무게 합 : ', max_team_weight)

    # 조합을 이용해 경우의 수를 찾는다.
    # 한 팀에 들어갈 수 있는 최대 인원으로 입력 받은 무게의 경우의 수를 구함.
    total = combinations(people_weights, max_team_members_cnt)

    print('경우의 수 : ', list(copy.deepcopy(total)))

    for i in total:
        # 110.0 - [30, 110, 70, 40, 120, 80, 50, 160, 130, 90]
        # 한 팀의 최대 무게 - 한 팀에 들어갈 수 있는 최대 인원의 무게 총합 경우의 수
        diff.append(abs(max_team_weight - sum(i)))

    print('최대 무게와 경우의 수 무게 총합 편차 : ', diff)
    print('최대 무게와 경우의 수 무게 총합 최소 편차 값 : ', min(diff))
    # 한 팀 최대 무게에서 경우의 수 무게 편차 최솟값을 빼고 더해 각 팀의 무게를 구한다.
    print(int(max_team_weight - min(diff)), int(max_team_weight + min(diff)))

    team_one = int(max_team_weight - min(diff))
    team_two = int(max_team_weight + min(diff))

    return [n, max(team_one, team_two)]


# n : 모든 사람의 수 (n명)
n = int(input("인원을 입력하세요 : "))
print(tug(n))

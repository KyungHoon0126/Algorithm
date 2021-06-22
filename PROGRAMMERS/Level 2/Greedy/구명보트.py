# 한 번에 최대 2명 탑승 가능, 무게 제한.
# 구명보트 개수의 최솟값을 구하라.


def solution2(people, limit):
    answer = 0

    # 무게 순으로 정렬
    people.sort()
    #  0  1  2  3
    # 50 50 70 80

    # 가장 가벼운 사람
    i = 0
    # 가장 무거운 사람
    j = len(people) - 1  # 3

    while i <= j:
        answer += 1
        # j == 0 : 인원이 한 명밖에 없을 경우
        if j == 0:
            break
        # 가장 가벼운 사람의 무게 + 가장 무거운 사람의 무게 > 구명보트의 무게
        elif people[i] + people[j] > limit:
            j -= 1
        # 가장 가벼운 사람의 무게 + 가장 무거운 사람의 무게 <= 구명보트의 무게
        elif people[i] + people[j] <= limit:
            i += 1
            j -= 1

    print(answer)
    return answer

# solution([70, 50, 80, 50], 100)
# solution([70, 80, 50], 100)
# solution([1, 1, 7, 8], 9)

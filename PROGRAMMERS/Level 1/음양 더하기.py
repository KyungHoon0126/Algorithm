def solution(absolutes, signs):
    sum = 0

    for i in range(0, len(absolutes)):
        if signs[i]:
            sum += absolutes[i]
        else:
            sum += absolutes[i] * -1

    return sum


# solution([4,7,12], [True, False, True])
solution([1, 2, 3], [False, False, True])
def solution(x):
    answer = True
    sum = 0
    for i in list(str(x)):
        sum += int(i)

    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer


solution(13)
import math


def solution(n):
    answer = ''
    su = '수'
    bak = '박'
    if n % 2 == 0:
        answer = (su + bak) * math.floor((n / 2))
    else:
        answer = ((su + bak) * math.floor((n / 2))) + su
    return answer


solution(4)
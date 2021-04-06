def solution(s):
    answer = ''

    for i in s.split(' '):
        for idx, j in enumerate(i):
            if idx % 2 == 0:
                answer += j.upper()
            else:
                answer += j.lower()
        answer += ' '
    return answer[:len(list(answer)) - 1]


solution("try hello world")
def solution(n):
    answer = ''
    while n >= 1:
        n, r = divmod(n, 3)
        answer += str(r)
    answer = int(answer, 3)

    return answer


solution(125)
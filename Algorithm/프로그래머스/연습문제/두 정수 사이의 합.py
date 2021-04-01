def solution(a, b):
    answer = 0
    first = 0
    second = 0

    first = a if a < b else b
    second = b if b > a else a

    print(first, second)

    for i in range(first, second + 1):
        answer += i

    return answer
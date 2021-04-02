def solution(s):
    answer = ''
    length = len(list(s))
    mok, nmg = divmod(len(list(s)), 2)
    alphabets = list(s)

    if length % 2 == 0:
        answer = alphabets[mok - 1] + alphabets[mok]
    if length % 2 != 0:
        answer = alphabets[mok]

    return answer
def solution(s):
    answer = True
    str = list(s)
    pCnt = 0
    yCnt = 0

    for i in range(0, len(str)):
        if str[i].lower() == 'p':
            pCnt += 1
        elif str[i].lower() == 'y':
            yCnt += 1

    return True if pCnt == yCnt else False
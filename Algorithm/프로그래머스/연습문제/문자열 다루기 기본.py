def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        for i in range(0, len(s)):
            answer = True if s[i].isdigit() else False
            if answer == False:
                break
    return answer
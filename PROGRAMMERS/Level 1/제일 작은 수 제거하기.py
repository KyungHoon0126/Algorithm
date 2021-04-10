def solution(arr):
    answer = arr
    if len(arr) > 1:
        answer.remove(min(arr))
    else:
        answer[0] = -1
    return answer
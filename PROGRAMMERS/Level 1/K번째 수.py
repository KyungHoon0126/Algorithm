def solution(array, commands):
    answer = []
    for i in commands:
      answer.append(sorted(array[i[0] - 1:i[1]])[i[2] - 1])
    return answer


# 2부터 5까지 잘라서 3번째 수, 4부터 4까지 잘라서 1번째 수, 1부터 7까지 잘라서 3번째 수
solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
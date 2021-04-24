def solution(n, arr1, arr2):
    answer = []
    for i in zip(arr1, arr2):
      answer.append(bin(i[0]|i[1])[2:].zfill(n).replace('0', ' ').replace('1', '#'))
    return answer
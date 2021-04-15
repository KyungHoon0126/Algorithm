def solution(phone_number):
    length = len(phone_number)
    answer = len(phone_number[0:length - 4]) * '*' + phone_number[length - 4:length]
    return answer
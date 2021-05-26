import copy


def convert(number, n):
    answer = []
    while number >= 1:
        number, r = divmod(number, n)
        answer.append(r)

    return ''.join(map(str, answer))


def solution(n):
    temp = copy.deepcopy(n)
    n_binary_num = convert(n, 2)

    while True:
        temp += 1
        binary_num = convert(temp, 2)

        if str(n_binary_num).count('1') == str(binary_num).count('1'):
            return temp

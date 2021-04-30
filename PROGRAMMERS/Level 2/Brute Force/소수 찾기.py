
from itertools import permutations

def is_prime_number(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return True


def solution(numbers):
    answer = 0
    nums = [int(i) for i in numbers]
    num_permus = []

    # 숫자의 길이 만큼 조합을 구해야함. 단 0과 1이 아닌 숫자이어야하고 중복은 없어야 함.
    for i in range(1, len(numbers) + 1):
        for j in list(set(permutations(nums, i))):
            if j[0] != 0:
                num_permus.append(int(''.join(map(str, j))))

    # 소수 판별
    for val in num_permus:
        if is_prime_number(val):
            answer += 1

    return answer
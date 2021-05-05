# N진수 -> 10진수 : int()
# 2진수 -> bin() / 8진수 -> oct() / 16진수 -> hex()

# 10진수 N진수 변환 함수.

'''
Case 1
'''


def convert1(number, n):
    answer = []
    # 변환할 수(number)를 N으로 나누어 나머지를 더함.
    while number >= 1:
        number, r = divmod(number, n)
        answer.append(r)
    # 더한 나머지를 역순으로 출력.
    return int(''.join(map(str, answer[::-1])))


'''
Case 2
'''
import string

# string.digits : 0123456789
# string.ascii_lowercase : abcdefghijklmnopqrstuvwxyz

tmp = string.digits + string.ascii_lowercase


def convert2(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]  # 0
    else:
        return convert2(q, base) + tmp[r]

# print(convert1(12, 2)) # 1200

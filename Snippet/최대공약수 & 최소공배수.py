# 최대공약수(GCD) & 최소공배수(LCM)

# 최대공약수(GCD) : 유클리드 호제법을 이용해 구함.
def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


# 최소 공배수(LCM) : 최대공약수(GCD)를 이용해 최소 공배수를 구함.
def lcm(n, m):
    return int((n * m) / gcd(n, m))


# 최대공약수(GCD) & 최소공배수(LCM)을 구하는 solution.
def solution(n, m):
    gcd_number = gcd(n, m)
    lcm_number = lcm(n, m)
    print(f'최대 공약수(GCD) : {gcd_number} / 최소 공배수(LCM) : {lcm_number}')


# 모듈 이용
import math

math.factorial(5)

n, m = int(input().split())
math.gcd(n, m)  # 최대공약수
math.lcm(n, m)  # 최소공배수

# 최소공배수 : int((n * m) / math.gcd(n * m))

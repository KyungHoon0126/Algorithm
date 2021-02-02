def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print("최대 공약수 : ", gcd(192, 162))

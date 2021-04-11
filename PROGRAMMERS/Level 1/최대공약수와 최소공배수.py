def getGcd(n, m):
    if n % m == 0:
        return m
    else:
        print(f'n, m : {n, m}')
        print(f'n % m : {n % m}')
        return getGcd(m, n % m)


def solution(n, m):
    answer = []
    gcd = getGcd(n, m)
    lcm = int((n * m) / gcd)
    answer.append(gcd)
    answer.append(lcm)
    return answer


solution(2, 5)
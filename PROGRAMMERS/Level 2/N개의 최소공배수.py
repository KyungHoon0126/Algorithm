def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def lcm(n, m):
    return int(n * m / gcd(n, m))


def solution(arr):
    # arr = [2, 6, 8, 14]
    while True:
        # arr의 끝 값 2개를 가져와서 최소 공배수를 구한 후 append
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


print(solution([2, 6, 8, 14]))

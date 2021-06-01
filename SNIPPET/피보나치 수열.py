def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)


print([fibo(x) for x in range(1, 10)])

# 다이나믹 프로그래밍, DP(Dynamic Programming) 방식으로 구현

# d = [0] * (n + 1)
d = [0] * (99 + 1)


# Top-Down, 탑다운 다이나믹 프로그래밍
def fibo_by_top_down(n):
    # 한 번 계산된 결과르 메모이제이션(Memoization)하기 위한 리스트 초기화

    # 종료 조건(1 혹은 2일 때 1을 반환)
    if n == 1 or n == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[n] != 0:
        return d[n]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[n] = fibo_by_top_down(n - 1) + fibo_by_top_down(n - 2)
    return d[n]


print(fibo_by_top_down(99))


# Bottom-Up, 보텀업 다이나믹 프로그래밍
def fibo_by_bottom_up(n):
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1

    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[n]


print(fibo_by_bottom_up(99))

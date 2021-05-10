# 부분합 수열을 이용한 연속부분 최대합 구하기.

MIN = -2 ** 31 - 1


def partial_sum(arr):
    # 1.
    arr = [0] + arr
    N = len(arr)
    p_sum = [0] * N
    ans = MIN

    # 2.
    for i in range(1, N):
        p_sum[i] = p_sum[i - 1] + arr[i]

    # 3.
    for hi in range(1, N):
        for lo in range(1, hi + 1):
            ans = max(ans, p_sum[hi] - p_sum[lo - 1])

    return ans


#  [-1000, -1000, -1000, -1000]
print(partial_sum([-2, -3, 4, -1, -2, 1, 5, -3]))


# 동적 계획법을 이용한 연속부분 최대합 구하기
def get_partial_sum_by_dynamic_programming(arr):
    cache = [None] * len(arr)
    # 1.
    cache[0] = arr[0]

    # 2.
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i - 1]) + arr[i]

    return max(cache)


print(get_partial_sum_by_dynamic_programming([-2, -3, 4, -1, -2, 1, 5, -3]))

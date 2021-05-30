def solution(n):
    answer = 0

    # 1부터 N까지 순회
    for i in range(1, n + 1):
        sum = 0
        # i부터 N까지의 합
        for j in range(i, n + 1):
            sum += j
            # 합이 같다면 answer += 1
            if sum == n:
                answer += 1
                break
            # 값이 N보다 크면 더 더할 필요가 없으므로 break
            elif sum > n:
                break

    return answer

def solution(n, times):
    answer = 0
    left = 0  # 최소 범위
    right = max(times) * n  # 최대 범위

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for time in times:
            count += mid // time
            # 심사 인원수를 넘으면 다음 단계
            if count >= n:
                break

        # n명을 심사 할 수 있는 경우. 즉 검사를 할 수 있다면 시간을 줄여본다.
        if count >= n:
            answer = mid
            right = mid - 1
        # 만약 검사를 할 수 없다면, 시간을 늘려본다.
        elif count < n:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))

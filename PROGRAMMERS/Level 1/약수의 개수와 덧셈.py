def solution(left, right):
    answer = 0
    nums = [[] * 1 for _ in range(right - left + 1)]

    cnt = 0
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                nums[cnt].append(j)
        cnt += 1

    for i in nums:
        if len(i) % 2 == 0:
            answer += i[-1]
        else:
            answer -= i[-1]

    return answer
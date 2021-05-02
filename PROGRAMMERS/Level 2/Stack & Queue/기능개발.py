# 기능개발

from collections import deque


def solution(progresses, speeds):
    answer = []
    stack = deque()  # 남아 있는 진행률을 담을 stack

    for p, s in zip(progresses, speeds):
        cnt = 1
        while True:
            if s * cnt >= 100 - p:
                stack.append(cnt)
                break
            else:
                cnt += 1

    while stack:
        curProcess = stack.popleft()
        cnt = 1
        for i in range(len(stack)):
            if curProcess >= stack[i]:
                cnt += 1
            else:
                break

        for i in range(cnt - 1):
            stack.popleft()

        answer.append(cnt)
    return answer

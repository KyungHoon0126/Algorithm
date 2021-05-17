# 스택/큐 - 주식가격

from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        curPrice = prices.popleft()
        count = 0

        for i in prices:
            if curPrice > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer

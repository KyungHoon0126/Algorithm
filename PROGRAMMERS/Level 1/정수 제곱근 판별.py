import math

def solution(n):
    return int(pow(math.sqrt(n) + 1, 2)) if (math.sqrt(n) + 1) % 1 == 0 else -1

solution(121)
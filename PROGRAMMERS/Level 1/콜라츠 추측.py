import math

def solution(num):
    answer = 0

    while True:
      if num == 1 or answer >= 500:
        break
      elif num % 2 != 0:
        num = num * 3 + 1
        answer += 1
      else:
        num = math.ceil(num / 2)
        answer += 1

    return -1 if answer >= 500 else answer